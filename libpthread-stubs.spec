# Debug package is empty so disable it
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	PThread Stubs for XCB
Name:		libpthread-stubs
Version:	0.3
Release:	5
Group:		System/X11
License:	MIT
Url:		http://xcb.freedesktop.org
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2

BuildRequires:	xsltproc
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)

%description
PThread Stubs for XCB.

%prep
%setup -q

%build
%configure2_5x \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files 
%{_libdir}/pkgconfig/pthread-stubs.pc

