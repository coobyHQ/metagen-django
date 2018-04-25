Installation
=============

The plugin can be installed at the user level or at the system level if you have
administrator privileges. The advice is still to use a *virtual environment*
at the user level, such as *virtualenv* (or *pyvenv* for Python 3) to not conflict
with dependencies of other Python applications.

For the installation it is necessary to clone the repository:

.. code-block:: bash

  pip install https://github.com/gridworkz/metagen-django/archive/master.zip

then install the dependencies:

.. code-block:: bash

  pip install -e git+https://github.com/gridworkz/python3-saml.git#egg=python3-saml
  pip install -e git+https://github.com/mehcode/python-xmlsec.git@15e6ce62658cc707dbdce94a13b6bfce8352a7ac#egg=xmlsec


Requirements
------------

The plugin is based on the library `python3-saml <https://github.com/onelogin/python3-saml>` fron OneLogin.
This library has a series of dependencies to be installed before installing the plugin for METAGEN.

On Linux Debian the command to install dependencies would be:

.. code-block:: bash

  apt-get install libxml2-dev libxmlsec1-dev libxmlsec1-openssl

On a CentOS Linux the prerequisites are installed with the command:

.. code-block:: bash

  yum install libxml2-devel xmlsec1-devel xmlsec1-openssl-devel libtool-ltdl-devel

For further details consult the library documentation
`python-xmlsec <https://github.com/mehcode/python-xmlsec>`

Demo
----

To run the demo with the Django development server:

.. code-block:: bash

  cd example
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py runserver

Then log in with a browser at the address `https://<sp_domain>:8000` to see the demo.
