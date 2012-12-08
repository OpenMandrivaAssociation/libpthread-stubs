# Debug package is empty so disable it
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define libpthread_stubs %mklibname xcb 1

Name:		libpthread-stubs
Summary:	PThread Stubs for XCB
Version:	0.3
Release:	4
Group:		System/X11
License:	MIT
URL:		http://xcb.freedesktop.org
Source0:	http://xcb.freedesktop.org/dist/libpthread-stubs-%{version}.tar.bz2

BuildRequires:	x11-proto-devel >= 1.2.0
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	libxslt-proc

%description
PThread Stubs for XCB.

%prep
%setup -q -n libpthread-stubs-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files 
%{_libdir}/pkgconfig/pthread-stubs.pc


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3-3mdv2011.0
+ Revision: 661517
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3-2mdv2011.0
+ Revision: 602597
- rebuild

* Thu Nov 12 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.3-1mdv2010.1
+ Revision: 465409
- New version: 0.3

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.1-6mdv2010.0
+ Revision: 425692
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.1-5mdv2009.1
+ Revision: 351487
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.1-4mdv2009.0
+ Revision: 222971
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1-3mdv2008.1
+ Revision: 178992
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Tue Feb 27 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 0.1-1mdv2007.0
+ Revision: 126720
- Importing libpthread-stubs to the repository. We don't need pthread-stubs at
  all, so this package basically generates a pkgconfig file saying so.

