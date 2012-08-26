%define		pkgname facter
Summary:	Ruby module for collecting simple facts about a host operating system
Name:		ruby-%{pkgname}
Version:	1.6.6
Release:	1
License:	GPL v2+
Group:		Networking/Admin
Source0:	http://downloads.puppetlabs.com/%{pkgname}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	47670a59301d6c3e31a1c68747b139c8
URL:		http://www.puppetlabs.com/puppet/related-projects/facter/
BuildRequires:	docutils
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
Requires:	net-tools
Requires:	which
# dmidecode and pciutils are not available on all arches
%ifarch %{ix86} %{x8664} ia64
Requires:	dmidecode
Requires:	pciutils
%endif
Obsoletes:	facter
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
Facter is a lightweight program that gathers basic node information
about the hardware and operating system. Facter is especially useful
for retrieving things like operating system names, hardware
characteristics, IP addresses, MAC addresses, and SSH keys.

Facter is extensible and allows gathering of node information that may
be custom or site specific. It is easy to extend by including your own
custom facts. Facter can also be used to create conditional
expressions in Puppet that key off the values returned by facts.

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_sitelibdir}
%{__ruby} install.rb \
	--quick \
	--no-man \
	--no-rdoc \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README.md etc/facter.conf
%attr(755,root,root) %{_bindir}/facter
%{ruby_sitelibdir}/facter
%{ruby_sitelibdir}/facter.rb
