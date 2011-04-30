# TODO
# for man - rst2man.py needed (docutils snap?)
Summary:	Facter
Summary(pl.UTF-8):	Facter
Name:		facter
Version:	1.5.9rc5
Release:	0.1
License:	GPL v2+
Group:		Networking/Admin
Source0:	http://puppetlabs.com/downloads/facter/%{name}-%{version}.tar.gz
# Source0-md5:	9fe23f971d2659122df387804bdff77a
#Patch0: %{name}-amd64.patch
URL:		http://www.puppetlabs.com/puppet/related-projects/facter/
BuildRequires:	docutils
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby
#%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Facter.

%description -l pl.UTF-8
Facter.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_sitelibdir}

ruby install.rb \
	--no-man \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO etc/facter.conf
%attr(755,root,root) %{_bindir}/facter
%{ruby_sitelibdir}/facter
%{ruby_sitelibdir}/facter.rb
