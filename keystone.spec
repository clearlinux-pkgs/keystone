#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC36CDCB4DF00C68C (infra-root@openstack.org)
#
Name     : keystone
Version  : 13.0.1
Release  : 95
URL      : http://tarballs.openstack.org/keystone/keystone-13.0.1.tar.gz
Source0  : http://tarballs.openstack.org/keystone/keystone-13.0.1.tar.gz
Source1  : keystone.tmpfiles
Source99 : http://tarballs.openstack.org/keystone/keystone-13.0.1.tar.gz.asc
Summary  : OpenStack Identity
Group    : Development/Tools
License  : Apache-2.0
Requires: keystone-bin
Requires: keystone-config
Requires: keystone-python3
Requires: keystone-license
Requires: keystone-python
Requires: Babel
Requires: Paste
Requires: PasteDeploy
Requires: Routes
Requires: SQLAlchemy
Requires: Sphinx
Requires: WebOb
Requires: WebTest
Requires: bandit
Requires: bcrypt
Requires: cryptography
Requires: dogpile.cache
Requires: fixtures
Requires: flake8-docstrings
Requires: jsonschema
Requires: keystonemiddleware
Requires: lxml
Requires: oauthlib
Requires: openstackdocstheme
Requires: oslo.cache
Requires: oslo.concurrency
Requires: oslo.config
Requires: oslo.context
Requires: oslo.db
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.messaging
Requires: oslo.middleware
Requires: oslo.policy
Requires: oslo.serialization
Requires: oslo.utils
Requires: oslotest
Requires: osprofiler
Requires: passlib
Requires: pbr
Requires: pycadf
Requires: pymongo
Requires: pysaml2
Requires: python-keystoneclient
Requires: python-memcached
Requires: python-mock
Requires: pytz
Requires: reno
Requires: scrypt
Requires: six
Requires: sqlalchemy-migrate
Requires: stevedore
Requires: testtools
BuildRequires : buildreq-distutils3
BuildRequires : dogpile.cache-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : jsonschema-python
BuildRequires : msgpack-python-python
BuildRequires : oauthlib-python
BuildRequires : oslo.db-python
BuildRequires : oslo.middleware-python
BuildRequires : oslo.policy-python
BuildRequires : oslo.service-python
BuildRequires : oslo.utils-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pycadf-python
BuildRequires : pyrsistent-python
BuildRequires : pysaml2-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
Team and repository tags
        ========================

%package bin
Summary: bin components for the keystone package.
Group: Binaries
Requires: keystone-config
Requires: keystone-license

%description bin
bin components for the keystone package.


%package config
Summary: config components for the keystone package.
Group: Default

%description config
config components for the keystone package.


%package license
Summary: license components for the keystone package.
Group: Default

%description license
license components for the keystone package.


%package python
Summary: python components for the keystone package.
Group: Default
Requires: keystone-python3

%description python
python components for the keystone package.


%package python3
Summary: python3 components for the keystone package.
Group: Default
Requires: python3-core

%description python3
python3 components for the keystone package.


%prep
%setup -q -n keystone-13.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533789342
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/keystone
cp LICENSE %{buildroot}/usr/share/doc/keystone/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/keystone.conf

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/keystone-manage
/usr/bin/keystone-wsgi-admin
/usr/bin/keystone-wsgi-public

%files config
%defattr(-,root,root,-)
%config /usr/etc/keystone/keystone-paste.ini
%config /usr/etc/keystone/sso_callback_template.html
/usr/lib/tmpfiles.d/keystone.conf

%files license
%defattr(-,root,root,-)
/usr/share/doc/keystone/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
