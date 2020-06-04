Name:       ansible-role-dci-sync-registry
Version:    0.0.VERS
Release:    2%{?dist}
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
mkdir -p %{buildroot}%{_datadir}/dci/roles/dci-sync-registry
chmod 755 %{buildroot}%{_datadir}/dci/roles/dci-sync-registry

cp -r defaults %{buildroot}%{_datadir}/dci/roles/dci-sync-registry
cp -r files %{buildroot}%{_datadir}/dci/roles/dci-sync-registry
cp -r tasks %{buildroot}%{_datadir}/dci/roles/dci-sync-registry
cp -r templates %{buildroot}%{_datadir}/dci/roles/dci-sync-registry
cp -r handlers %{buildroot}%{_datadir}/dci/roles/dci-sync-registry

%if 0%{?rhel} && 0%{?rhel} < 8
pathfix.py -pni "%{__python2}" %{buildroot}%{_datadir}/dci/roles/dci-sync-registry/files/fetch_images.py
%else
pathfix.py -pni "%{__python3}" %{buildroot}%{_datadir}/dci/roles/dci-sync-registry/files/fetch_images.py
%endif

%files
%doc README.md
%license LICENSE
%{_datadir}/dci/roles/dci-sync-registry


%changelog
* Thu Jun 04 2020 Bill Peck <bpeck@rehdat.com> - 0.0.1-2
- Rebuild for RHEL-8
* Thu Nov 13 2018 Dimitri Savineau <dsavinea@redhat.com> - 0.0.1-1
- Initial release
