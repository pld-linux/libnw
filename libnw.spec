Summary:	libnw
Summary(pl):	libnw
Name:		libnw
Version:	1.30.02
Release:	0
Copyright:	GPL
Group:		Games/Utilities
Source0:	http://dl.sourceforge.net/openknights/%{name}-%{version}.tar.gz
# Source0-md5:	7c7dc1ca4d80710647f1d4401bdc654b
URL:		http://openknights.sourceforge.net/
BuildRequires:	awk
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	perl
#Requires:
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%package devel
Summary:	libnw -
Summary(pl):	libnw -
Group:		Development/Games
Requires:	%{name} = %{version}
%description devel
%description -l pl devel

%package static
Summary:	libnw -
Summary(pl):	libnw -
Group:		Development/Games
Requires:	%{name} = %{version}
%description static
%description -l pl static

%prep
%setup -q

#%patch

%build
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	%{?_without_static:--disable-static}

%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(755,root,root) %{_libdir}/libnw.0.0.0
%attr(,,)

%files devel
%defattr(644, root, root, 755)
%doc
%attr(755, root, root) %{_libdir}/libnw.la
%attr(644, root, root) %{_includedir}/libnw/*.h

%files static
%defattr(644,root,root,755)
%doc
%attr(644,root,root) %{_libdir}/libnw.a
