# django-metagen-demo
Demo of a SAML2 METAGEN authentication for Django,
based on [python3-saml](https://github.com/onelogin/python3-saml).


# Introduction
This is a django project with one demo app, that shows how to use
Single Sign On authentication through a SAML2 METAGEN Identity Provider (SAML).

Technical documentation on SAML2 METAGEN and SAML is available at:
https://github.com/gridworkz/metagen-testenv-backoffice and
https://github.com/gridworkz/metagen-testenv-identityserver


# Installation

## General overview

* Install django-metagen via pip in your virtualenv and add it to the project INSTALLED_APPS.
* Add metagen urls to your project url patterns
* Generate X.509 certificates and store them somewhere
* Register your SP with the IdP.

* Change the ``saml/settings.json`` and ``saml/advanced_settings.json``
  configuration files using your metadata (only for test purpose).

* Start the app server


## Local development details

A **test identity provider** can be installed on your development environment (your laptop?), following instructions at:
https://github.com/gridworkz/metagen-testenv-identityserver

Here are more detailed steps with some suggestions:

* choose a domain for your Service Provider (i.e. metagen.yourdomain.com)

* generate self-signed certificates for your SP (you can do that here:
  https://developers.onelogin.com/saml/online-tools/x509-certs/obtain-self-signed-certs)

* put the content of the generated certificates under ``saml/certs/``
  (name them: sp.crt, sp.key and sp.csr; CSR is not useed here, I think)

* modify your /etc/hosts file, to redirect both
  ``metagen-testenv-identityserver`` and ``metagen.yourdomain.com`` to your ``localhost``
  ```
  echo "127.0.0.1 metagen-testenv-identityserver" | sudo tee -a /etc/hosts
  ```

* start the dockerized service with
  ```
  docker-compose up
  ```

* visit https://metagen-testenv-identityserver:8080, go to section
  **Service Provider**/**Metadata Creation**

* fill in the form:
    * **Entity ID**: http://metagen.yourdomain.com
    * **Certificate**: put the content of the sp.crt, with no headers in the text area
    * **Single Logout Service/Binding**: keep HTTP-POST
    * **Single Logout Service/Location**: http://metagen.yourdomain.com/?sls
    * **Assertion consumer Service/Binding**: HTTP-POST is ok
    * **Assertion consumer Service/Location**: http://metagen.yourdomain.com/?acs
    * **Attribute  Consuming Service**:
        * **Name and Description**: `test/test` should be ok
        * choose all fields you want returned from the IdP to your
          app, you'll see them in the page returned after the
          user was logged in
    * **Organization**: this section can be left empty.

* pressing **Download** will not work as non-HTTPS urls will not validate,
  so, copy *the XML code* in the text area and save it to a
  ``metadata-yourdomain.xml`` file; that will be your SP's metadata

* press the **Save** button, that will **register** the SP with the data
  you just inserted into the IdP.

* press the **Users** button and create a new user,
  only entering those fields that you want to see later;
  a note: in this interface new users cannot be modified, only deleted
  and re-created; that's ok, not everything can be perfect

# Useful debugging tools

- browser extensions to track SAML requests and response
  (they exist both for Chrome and Firefox)
- the "tools" tab within the ``carbon`` admin interface of the IdP server
  (https://localhost:9443, admin/admin), that allows the verification of the requests.


# Execution

When the server is running, the home page shows a login button that
starts the SSO workflow.

Pressing the login button, a request is packed and sent to the IdP.

The IdP responds by redirecting you to its own login page.

You insert your credential (one of the users you just created)

The IdP redirects you to your SP, and a page with the attributes of the
signed in user are shown.

# TODOs

- improve session management

- improve user data storage

- tests

- improve doc



Copyright (c) 2018, the respective contributors, as shown by the AUTHORS file.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
