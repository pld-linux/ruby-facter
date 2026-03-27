%define		pkgname facter
Summary:	Ruby module for collecting simple facts about a host operating system
Name:		ruby-%{pkgname}
Version:	4.10.0
Release:	1
License:	Apache v2.0
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	b9495a64e9234494a0750da02769ed00
Patch0:		ruby-facter-shebang.patch
URL:		https://github.com/puppetlabs/facter
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
Requires:	ruby-hocon >= 1.3
Requires:	ruby-thor >= 1.0.1
Obsoletes:	facter < 1.5.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%patch -P0 -p1

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_bindir}/facter
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
