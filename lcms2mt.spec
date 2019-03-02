%define major 2
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Summary:	Color Management Engine, Multi-Threaded fork
Name:		lcms2mt
Version:	2.9
Release:	1
License:	MIT
Group:		Graphics
Url:		http://git.ghostscript.com/?p=thirdparty-lcms2.git;a=shortlog;h=refs/heads/lcms2mt
# No tarball releases -- packaged from git, 2019/03/02
Source0:	%{name}-%{version}.tar.xz
Patch0:		lcms2mt-2.9-compile.patch
Patch1:		lcms2mt-2.9-link-libm.patch
BuildRequires:	jbig-devel
BuildRequires:	tiff-devel
BuildRequires:	pkgconfig(zlib)

%description
LittleCMS intends to be a small-footprint, speed optimized color management
engine in open source form. LCMS2 is the current version of LCMS, and can be
parallel installed with the original (deprecated) lcms.

%package -n %{libname}
Summary:	Libraries for LittleCMS
Group:		System/Libraries

%description -n %{libname}
This package provides the shared lcms2 library.

%package -n %{devname}
Summary:	Development files for LittleCMS
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for LittleCMS2.

%prep
%autosetup -p1

%build
%configure
sed -i -e 's,define CMSEXPORT,define CMSEXPORT __attribute__((visibility("default"))),g' include/lcms2mt.h
%make

%install
%make_install
# No need to re-export from an external application...
sed -i -e 's,define CMSEXPORT __attribute__((visibility("default"))),define CMSEXPORT,g' include/lcms2mt.h

install -D -m 644 include/lcms2mt.h %{buildroot}%{_includedir}/lcms2mt.h
install -D -m 644 include/lcms2mt_plugin.h %{buildroot}%{_includedir}/lcms2mt_plugin.h
# Previous name of the fork, still used in e.g. mupdf 1.14.0
ln -s lcms2mt.h %{buildroot}%{_includedir}/lcms2art.h
ln -s lcms2mt_plugin.h %{buildroot}%{_includedir}/lcms2art_plugin.h

%files -n %{libname}
%{_libdir}/liblcms2mt.so.%{major}*

%files -n %{devname}
%doc doc/*.pdf
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
