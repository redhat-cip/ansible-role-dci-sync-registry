Name:       ansible-role-dci-sync-registry
Version:    0.1.0
Release:    1.VERS%{?dist}
Summary:    ansible-role-dci-sync-registry
License:    ASL 2.0
URL:        https://github.com/redhat-cip/ansible-role-dci-sync-registry
Source0:    ansible-role-dci-sync-registry-%{version}.tar.gz

BuildArch:  noarch
Requires:   ansible
BuildRequires:    /usr/bin/pathfix.py

%description
An Ansible role that sync DCI registry

%prep
%setup -qc


%build

%install

%if 0%{?rhel} && 0%{?rhel} < 8
PYTHON="%{__python2}"
%else
PYTHON="%{__python3}"
%endif

make install BUILDROOT=%{buildroot} DATADIR=%{_datadir}/dci/roles PYTHON=$PYTHON

%files
%doc README.md
%license LICENSE
%{_datadir}/dci/roles/dci-sync-registry


%changelog
* Mon Sep 26 2022 Frederic Lepied <flepied@redhat.com> 0.1.0-1
- use a Makefile

* Thu Jun 04 2020 Bill Peck <bpeck@rehdat.com> - 0.0.1-2
- Rebuild for RHEL-8

* Thu Nov 13 2018 Dimitri Savineau <dsavinea@redhat.com> - 0.0.1-1
- Initial release
