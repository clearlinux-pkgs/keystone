#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : keystone
Version  : 9.0.0
Release  : 82
URL      : http://tarballs.openstack.org/keystone/keystone-9.0.0.tar.gz
Source0  : http://tarballs.openstack.org/keystone/keystone-9.0.0.tar.gz
Source1  : keystone.tmpfiles
Summary  : OpenStack Identity
Group    : Development/Tools
License  : Apache-2.0
Requires: keystone-bin
Requires: keystone-python
Requires: keystone-config
Requires: keystone-data
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
Patch1: 0002-Default-Keystone-HTTPD-configuration.patch
Patch2: 0005-Serve-keystone-via-nginx-with-uwsgi.patch
Patch3: 0006-Set-default-syslog.patch
Patch4: 0001-Remove-admin_token_auth.patch

%description
Documentation for running Keystone with Apache HTTPD is in
doc/source/apache-httpd.rst

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
Requires: dogpile.cache-python
Requires: jsonschema-python
Requires: msgpack-python-python
Requires: oauthlib-python
Requires: oslo.db-python
Requires: oslo.middleware-python
Requires: oslo.policy-python
Requires: oslo.service-python
Requires: oslo.utils-python
Requires: pycadf-python
Requires: pysaml2-python

%description python
python components for the keystone package.


%prep
cd ..
%setup -q -n keystone-9.0.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

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
/usr/share/uwsgi/keystone/admin.ini
/usr/share/uwsgi/keystone/public.ini

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
