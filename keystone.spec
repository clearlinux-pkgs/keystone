#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : keystone
Version  : 8.0.1
Release  : 79
URL      : http://tarballs.openstack.org/keystone/keystone-8.0.1.tar.gz
Source0  : http://tarballs.openstack.org/keystone/keystone-8.0.1.tar.gz
Source1  : keystone.tmpfiles
Summary  : OpenStack Identity
Group    : Development/Tools
License  : Apache-2.0
Requires: keystone-bin
Requires: keystone-python
Requires: keystone-config
Requires: keystone-data
BuildRequires : Babel
BuildRequires : Jinja2-python
BuildRequires : Mako
BuildRequires : MarkupSafe
BuildRequires : Paste
BuildRequires : PasteDeploy
BuildRequires : PyYAML
BuildRequires : Pygments-python
BuildRequires : Routes
BuildRequires : SQLAlchemy
BuildRequires : Sphinx
BuildRequires : Tempita
BuildRequires : WebOb
BuildRequires : WebTest
BuildRequires : aioeventlet
BuildRequires : alembic
BuildRequires : amqp
BuildRequires : anyjson
BuildRequires : bashate
BuildRequires : beautifulsoup4-python
BuildRequires : cffi
BuildRequires : coverage
BuildRequires : cryptography
BuildRequires : decorator
BuildRequires : discover
BuildRequires : docutils-python
BuildRequires : dogpile.cache
BuildRequires : dogpile.core
BuildRequires : enum34
BuildRequires : eventlet
BuildRequires : extras
BuildRequires : fixtures
BuildRequires : flake8-python
BuildRequires : funcsigs-python
BuildRequires : futures
BuildRequires : greenlet
BuildRequires : hacking
BuildRequires : httplib2-python
BuildRequires : idna
BuildRequires : ipaddress
BuildRequires : iso8601
BuildRequires : jsonschema-python
BuildRequires : keystone-data
BuildRequires : keystonemiddleware
BuildRequires : kombu
BuildRequires : ldappool
BuildRequires : linecache2
BuildRequires : lxml
BuildRequires : mccabe-python
BuildRequires : mox3-python
BuildRequires : msgpack-python
BuildRequires : netaddr
BuildRequires : netifaces
BuildRequires : oauthlib
BuildRequires : openssl
BuildRequires : oslo.concurrency
BuildRequires : oslo.config
BuildRequires : oslo.context
BuildRequires : oslo.db
BuildRequires : oslo.i18n
BuildRequires : oslo.log
BuildRequires : oslo.messaging
BuildRequires : oslo.middleware
BuildRequires : oslo.policy
BuildRequires : oslo.serialization
BuildRequires : oslo.utils
BuildRequires : oslosphinx
BuildRequires : oslotest
BuildRequires : osprofiler
BuildRequires : passlib
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : posix_ipc
BuildRequires : prettytable
BuildRequires : py-python
BuildRequires : pyOpenSSL
BuildRequires : pyasn1
BuildRequires : pycadf-python
BuildRequires : pycparser
BuildRequires : pycrypto
BuildRequires : pyflakes-python
BuildRequires : pymongo
BuildRequires : pysaml2
BuildRequires : pysqlite
BuildRequires : pytest
BuildRequires : python-dateutil
BuildRequires : python-dev
BuildRequires : python-editor
BuildRequires : python-keystoneclient
BuildRequires : python-ldap
BuildRequires : python-memcached
BuildRequires : python-mimeparse
BuildRequires : python-mock
BuildRequires : python-subunit
BuildRequires : pytz
BuildRequires : repoze.lru
BuildRequires : repoze.who
BuildRequires : requests
BuildRequires : retrying
BuildRequires : setuptools
BuildRequires : six
BuildRequires : sqlalchemy-migrate
BuildRequires : sqlparse
BuildRequires : stevedore
BuildRequires : tempest-lib
BuildRequires : testrepository
BuildRequires : testresources
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : tox
BuildRequires : traceback2
BuildRequires : trollius
BuildRequires : unittest2
BuildRequires : virtualenv
BuildRequires : waitress-python
BuildRequires : wrapt-python
BuildRequires : zope.interface
Patch1: 0002-Default-Keystone-HTTPD-configuration.patch
Patch2: 0003-Integrate-OSprofiler-in-Keystone.patch
Patch3: 0004-disable-admin_token-by-default.patch
Patch4: 0005-Serve-keystone-via-nginx-with-uwsgi.patch
Patch5: 0006-Set-default-syslog.patch

%description
This is a database migration repository.
More information at
http://code.google.com/p/sqlalchemy-migrate/

%package bin
Summary: bin components for the keystone package.
Group: Binaries
Requires: keystone-data
Requires: keystone-config

%description bin
bin components for the keystone package.


%package config
Summary: config components for the keystone package.
Group: Default

%description config
config components for the keystone package.


%package data
Summary: data components for the keystone package.
Group: Data

%description data
data components for the keystone package.


%package python
Summary: python components for the keystone package.
Group: Default
Requires: cryptography
Requires: jsonschema-python
Requires: keystonemiddleware
Requires: oslo.config
Requires: pycadf-python
Requires: python-memcached
Requires: stevedore

%description python
python components for the keystone package.


%prep
%setup -q -n keystone-8.0.1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/keystone.conf
## make_install_append content
install -d -m 755 %{buildroot}/usr/share/defaults/keystone
install -p -D -m 644 etc/*.templates %{buildroot}/usr/share/defaults/keystone
install -p -D -m 644 etc/*.ini %{buildroot}/usr/share/defaults/keystone
install -p -D -m 644 etc/*.sample %{buildroot}/usr/share/defaults/keystone
install -p -D -m 644 etc/*.json %{buildroot}/usr/share/defaults/keystone
install -p -D -m 755 tools/sample_data.sh %{buildroot}%{_datadir}/keystone/sample_data.sh
install -p -D -m 644 httpd/wsgi-keystone.conf %{buildroot}%{_datadir}/keystone/
for i in %{buildroot}/usr/share/defaults/keystone/*.sample; do mv $i ${i%.*}; done;
install -m 0755 -d %{buildroot}/usr/share/defaults/httpd/conf.d
install -p -D -m 644 httpd/wsgi-keystone.conf  %{buildroot}/usr/share/defaults/httpd/conf.d
install -m 0755 -d %{buildroot}/usr/share/uwsgi/keystone
install -p -D -m 644 httpd/public.ini  %{buildroot}/usr/share/uwsgi/keystone
install -p -D -m 644 httpd/admin.ini  %{buildroot}/usr/share/uwsgi/keystone
install -m 0755 -d %{buildroot}/usr/share/nginx/conf.d
install -p -D -m 644 httpd/keystone.conf %{buildroot}/usr/share/nginx/conf.d
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/keystone-all
/usr/bin/keystone-manage
/usr/bin/keystone-wsgi-admin
/usr/bin/keystone-wsgi-public

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/keystone.conf

%files data
%defattr(-,root,root,-)
/usr/share/defaults/httpd/conf.d/wsgi-keystone.conf
/usr/share/defaults/keystone/default_catalog.templates
/usr/share/defaults/keystone/keystone-paste.ini
/usr/share/defaults/keystone/keystone.conf
/usr/share/defaults/keystone/logging.conf
/usr/share/defaults/keystone/policy.json
/usr/share/defaults/keystone/policy.v3cloudsample.json
/usr/share/keystone/sample_data.sh
/usr/share/keystone/wsgi-keystone.conf
/usr/share/nginx/conf.d/keystone.conf
/usr/share/uwsgi/keystone/admin.ini
/usr/share/uwsgi/keystone/public.ini

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
