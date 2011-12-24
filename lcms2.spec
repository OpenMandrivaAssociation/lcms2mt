%define major 2
%define libname %mklibname lcms2_ %major
%define develname %mklibname -d lcms2

Name: lcms2
Version: 2.3
Release: %mkrel 1
Summary: Color Management Engine
License: MIT
URL: http://www.littlecms.com/
Source0: http://www.littlecms.com/%{name}-%{version}.tar.gz
Group: Graphics
BuildRequires: jpeg-devel
BuildRequires: tiff-devel
BuildRequires: zlib-devel

%description
LittleCMS intends to be a small-footprint, speed optimized color management
engine in open source form. LCMS2 is the current version of LCMS, and can be
parallel installed with the original (deprecated) lcms.

%package -n %libname
Summary: Libraries for %{name}
Group: System/Libraries
Requires: %name = %{version}

%description -n %libname
This package provides the shared lcms2 library.

%package -n %develname
Summary: Development files for LittleCMS
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %develname
Development files for LittleCMS2.

%prep
%setup -q

%build
%configure2_5x --disable-static --program-suffix=2
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_bindir}/*
%{_mandir}/man1/*

%files -n %libname
%defattr(-,root,root,-)
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %develname
%defattr(-,root,root,-)
%doc doc/*.pdf
%{_includedir}/*
%{_libdir}/*.so
#%{_libdir}/*.la
%{_libdir}/pkgconfig/%{name}.pc
