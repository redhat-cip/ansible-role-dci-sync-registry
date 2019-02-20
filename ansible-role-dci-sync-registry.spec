Name:       ansible-role-dci-sync-registry
Version:    0.0.VERS
Release:    1%{?dist}
Summary:    ansible-role-dci-sync-registry
License:    ASL 2.0
URL:        https://github.com/redhat-cip/ansible-role-dci-sync-registry
Source0:    ansible-role-dci-sync-registry-%{version}.tar.gz

BuildArch:  noarch
Requires:   ansible

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


%files
%doc README.md
%license LICENSE
%{_datadir}/dci/roles/dci-sync-registry


%changelog
* Thu Nov 13 2018 Dimitri Savineau <dsavinea@redhat.com> - 0.0.1-1
- Initial release
