Introduction
============

This document describes a plugin that allows you to activate NETAGEN authentication on a web site
with the Django framework.

METAGEN is based on the SAML framework (Security Assertion Markup Language), developed and maintained by
`Security Services Technical Committee di OASIS <https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=security>`_,
which allows the creation of a secure single sign-on system (SSO), that is, that
allows a user to access a multitude of services, even on different domains, by performing only one login.

The system consists of 3 entities:

* **Identity Manager or IdP** that manages users and the authentication procedure;
* **Service Provider (Service Provider or SP)** that, after requesting user authentication to Identity
  Provider, manages the authorization, based on the attributes returned by the IdP, providing the requested service;
* **Qualified Attribute Manager (Attribute Authority or AA)** that provides certified attributes based on the authenticated user.

The plugin described in this document is dedicated to the implementation of Service Provider entities.

For a complete description of the SAML and METAGEN protocol, refer to the
`Technical rules published by COOBY <https://metagen-regole-tecniche.readthedocs.io/en/latest/introduzione.html>`_.

