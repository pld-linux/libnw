#
# Conditional build:
%bcond_without static	# don't build static library
#
Summary:	libnw - NeverWinter Night game resources manupulation tool
Summary(pl):	libnw - narzêdzia do edycji zasobów gry NeverWinter Night
Name:		libnw
Version:	1.30.02
Release:	1
License:	BSD
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/openknights/%{name}-%{version}.tar.gz
# Source0-md5:	7c7dc1ca4d80710647f1d4401bdc654b
URL:		http://openknights.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool
BuildRequires:	perl-base >= 1:5.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libnw is a library of common routines for extracting and manipulating
resources from BioWare's NeverWinter Nights game.

%description -l pl
libnw to biblioteka wspólnych funkcji do wyci±gania i przetwarzania
danych z gry NeverWinter Nights firmy BioWare.

%package devel
Summary:	Header files for libnw library
Summary(pl):	Pliki nag³ówkowe biblioteki libnw
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libnw library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libnw.

%package static
Summary:	Static libnw library
Summary(pl):	Statyczna biblioteka libnw
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnw library.

%description static -l pl
Statyczna biblioteka libnw.

%package utils
Summary:	libnw - utilities programs
Summary(pl):	libnw - programy narzêdziowe
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}

%description utils
Several programs for extracting and manipulating resources from
BioWare's NeverWinter Nights game.

%description utils -l pl
Ró¿ne programy do wyci±gania i przetwarzania zasobów z gry NeverWinter
Nights firmy BioWare.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	%{?without_static:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README README.License-Torlack README.tech TODO
%attr(755,root,root) %{_libdir}/libnw.so.*.*.*
%{_datadir}/%{name}
%{_mandir}/man3/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnw.so
%{_libdir}/libnw.la
%{_includedir}/libnw

%if %{with static}
%files static
%defattr(644,root,root,755)
%{_libdir}/libnw.a
%endif

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
