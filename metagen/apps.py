# -*- coding: utf-8 -*-
import pkg_resources
from xml.etree import ElementTree as et
from django.conf import settings
from django.apps import AppConfig

from .app_settings import METAGEN_IDENTITY_PROVIDERS, app_settings


def get_idp_config(id, name=None):
    xml_path = pkg_resources.resource_filename('metagen', 'metagen-idp-metadata/metagen-idp-%s.xml' % id)
    idp_metadata = et.parse(xml_path).getroot()
    sso_path = './/{%s}SingleSignOnService[@Binding="%s"]' % \
               (app_settings.SAML_METADATA_NAMESPACE, app_settings.BINDING_REDIRECT_URN)
    slo_path = './/{%s}SingleLogoutService[@Binding="%s"]' % \
               (app_settings.SAML_METADATA_NAMESPACE, app_settings.BINDING_REDIRECT_URN)

    try:
        sso_location = idp_metadata.find(sso_path).attrib['Location']
    except (KeyError, AttributeError) as err:
        raise ValueError("Missing metadata SingleSignOnService for %r: %r" % (id, err))

    try:
        slo_location = idp_metadata.find(slo_path).attrib['Location']
    except (KeyError, AttributeError) as err:
        raise ValueError("Missing metadata SingleLogoutService for %r: %r" % (id, err))

    return {
        'name': name,
        'idp': {
            "entityId": idp_metadata.get("entityID"),
            "singleSignOnService": {
                "url": sso_location,
                "binding": app_settings.BINDING_REDIRECT_URN
            },
            "singleLogoutService": {
                "url": slo_location,
                "binding": app_settings.BINDING_REDIRECT_URN
            },
            "x509cert": idp_metadata.find(".//{%s}X509Certificate" % app_settings.XML_SIGNATURE_NAMESPACE).text
        }
    }


class MetagenConfig(AppConfig):
    name = 'metagen'
    verbose_name = "METAGEN Authentication"

    identity_providers = {
        id: get_idp_config(id, name) for id, name in METAGEN_IDENTITY_PROVIDERS
    }

    @staticmethod
    def get_saml_settings(idp_id=None):
        if idp_id is None:
            return app_settings.config
        else:
            saml_settings = dict(app_settings.config)
            saml_settings.update({'idp': MetagenConfig.identity_providers[idp_id]['idp']})
            return saml_settings
