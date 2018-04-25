import random

from django import template
from django.conf import settings
from ..apps import MetagenConfig

register = template.Library()

METAGEN_BUTTON_SIZES = {'small', 'medium', 'large', 'xlarge'}


@register.inclusion_tag("metagen_button.html", takes_context=True)
def metagen_button(context, size='medium'):
    if size not in METAGEN_BUTTON_SIZES:
        raise ValueError("argument 'size': value %r not in %r." % (size, METAGEN_BUTTON_SIZES))

    metagen_idp_list = [
        {'id': k, 'name': v['name']}
        for k, v in MetagenConfig.identity_providers.items()
    ]
    random.shuffle(metagen_idp_list)
    if settings.DEBUG:
        metagen_idp_list.append({'id': 'test', 'name': 'test'})
    return {
        'method': context['request'].method.lower(),
        'post_data': context['request'].POST,
        'metagen_button_size': size,
        'metagen_button_size_short': size[0] if size != 'xlarge' else size[:2],
        'metagen_idp_list': metagen_idp_list
    }
