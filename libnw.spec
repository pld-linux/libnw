#
%bcond_without static	# don't build static

Summary:	libnw - NeverWinter Night game resources manupulation tool
Summary(pl):	libnw - narzêdzia do edycji zasobów gry NeverWinter Night
Name:		libnw
Version:	1.30.02
Release:	0.1
Copyright:	GPL
Group:		Games/Utilities
Source0:	http://dl.sourceforge.net/openknights/%{name}-%{version}.tar.gz
# Source0-md5:	7c7dc1ca4d80710647f1d4401bdc654b
URL:		http://openknights.sourceforge.net/
BuildRequires:	awk
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	perl >= 5.6.0
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
-- empty --

%description -l pl
-- pusty --

%package devel
Summary:	libnw - development files
Summary(pl):	libnw - pliki nag³ówkowe
Group:		Development/Games
Requires:	%{name} = %{version}
%description devel
-- empty --

%description -l pl devel
-- pusty --

%package static
Summary:	libnw - static library
Summary(pl):	libnw - biblioteka statyczna
Group:		Development/Games
Requires:	%{name} = %{version}
%description static
-- empty --

%description -l pl static
-- pusty --

%package utils
Summary:	libnw - utilities programs
Summary(pl):	libnw - programy narzêdziowe.
Group:		Games/Utilities
Requires:	%{name} = %{version}
%description utils
-- empty --

%description -l pl utils
-- pusty --

%prep
%setup -q

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
%{_libdir}/libnw.0.0.0
%{_datadir}/%{name}/*
%{_mandir}/man3/*

%files devel
%defattr(644, root, root, 755)
%doc
%{_libdir}/libnw.la
%{_includedir}/libnw/*.h

%if %{with static}
%files static
%defattr(644,root,root,755)
%doc
%{_libdir}/libnw.a
%endif

%files utils
%{_bindir}/*
%{_mandir}/man1/*
