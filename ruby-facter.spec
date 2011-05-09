%define		pkgname facter
%define		subver	rc5
%define		rel		1
Summary:	Ruby module for collecting simple facts about a host operating system
Name:		ruby-%{pkgname}
Version:	1.5.9
Release:	0.%{subver}.%{rel}
License:	GPL v2+
Group:		Networking/Admin
Source0:	http://puppetlabs.com/downloads/facter/%{pkgname}-%{version}%{subver}.tar.gz
# Source0-md5:	9fe23f971d2659122df387804bdff77a
URL:		http://www.puppetlabs.com/puppet/related-projects/facter/
BuildRequires:	docutils
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
Obsoletes:	facter
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
Ruby module for collecting simple facts about a host Operating system.
Some of the facts are preconfigured, such as the hostname and the
operating system. Additional facts can be added through simple Ruby
scripts

%prep
%setup -q -n %{pkgname}-%{version}%{subver}

%build

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
%doc README TODO etc/facter.conf
%attr(755,root,root) %{_bindir}/facter
%{ruby_sitelibdir}/facter
%{ruby_sitelibdir}/facter.rb
