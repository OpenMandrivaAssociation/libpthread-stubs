# Debug package is empty so disable it
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	PThread Stubs for XCB
Name:		libpthread-stubs
Version:	0.4
Release:	3
Group:		System/X11
License:	MIT
Url:		https://xcb.freedesktop.org
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2

BuildRequires:	xsltproc
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)

%description
PThread Stubs for XCB.

%package devel
Summary:	PThread Stubs for XCB
Group:		Development/X11
Obsoletes:	libpthread-stubs

%description devel
PThread Stubs for XCB.

%prep
%autosetup -p1

%build
%configure \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files devel
%{_libdir}/pkgconfig/pthread-stubs.pc
