%define libpthread_stubs %mklibname xcb 1
Name: libpthread-stubs
Summary: PThread Stubs for XCB
Version: 0.3
Release: %mkrel 2
Group: System/X11
License: MIT
URL: http://xcb.freedesktop.org
Source0: http://xcb.freedesktop.org/dist/libpthread-stubs-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-proto-devel >= 1.2.0
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: libxslt-proc

%description
PThread Stubs for XCB

%prep
%setup -q -n libpthread-stubs-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%{_libdir}/pkgconfig/pthread-stubs.pc


