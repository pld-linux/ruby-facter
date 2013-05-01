%define		pkgname facter
Summary:	Ruby module for collecting simple facts about a host operating system
Name:		ruby-%{pkgname}
Version:	1.6.18
Release:	2
License:	GPL v2+
Group:		Development/Languages
Source0:	http://downloads.puppetlabs.com/%{pkgname}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	c209df5909ccd4112c19cf4b535027a7
URL:		http://puppetlabs.com/puppet/related-projects/facter/
BuildRequires:	docutils
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
Requires:	net-tools
Requires:	which
# dmidecode and pciutils are not available on all arches
%ifarch %{ix86} %{x8664} ia64
Requires:	dmidecode
Requires:	pciutils
%endif
Obsoletes:	facter < 1.5.9
# due arch specific dependencies
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of arch dependant requires
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
	--sitelibdir=%{ruby_vendorlibdir} \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md etc/facter.conf
%attr(755,root,root) %{_bindir}/facter
%{ruby_vendorlibdir}/facter
%{ruby_vendorlibdir}/facter.rb
