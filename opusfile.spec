Name:          opusfile
Version:       0.11
Release:       4
Summary:       A high-level API provides seeking, decode, and playback of Opus streams
License:       BSD
URL:           http://www.opus-codec.org/
Source0:       http://downloads.xiph.org/releases/opus/%{name}-%{version}.tar.gz
Patch0000:     0001-fix-MemorySanitizer-use-of-uninitialized-value.patch
Patch0001:     Fix-short-circuit-test-when-seeking-in-short-files.patch

BuildRequires: libogg-devel openssl-devel opus-devel

%description
The opusfile library provides seeking, decode, and playback of Opus streams in the Ogg
container (.opus files) including over http(s) on posix and windows systems.
opusfile depends on libopus and libogg.The included opusurl library for http(s) access
depends on opusfile and openssl.

%package devel
Summary:       Development package for opusfile package
Requires:      %{name} = %{version}-%{release} pkgconfig

%description devel
Development package for opusfile package.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure --disable-static
%make_build

%install
%make_install
%delete_la

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%doc AUTHORS COPYING
%{_libdir}/{libopusfile.so.*,libopusurl.so.*}

%files devel
%doc %{_docdir}/%{name}
%{_includedir}/opus/opus*
%{_libdir}/pkgconfig/{opusfile.pc,opusurl.pc}
%{_libdir}/{libopusfile.so,libopusurl.so}

%changelog
* Tue Dec 14 2021 chenchen <chen_aka_jan@163.com> -  0.11-4
- Fix short-circuit test when seeking in short files

* Thu Dec 03 2020 maminjie <maminjie1@huawei.com> - 0.11-3
- fix MemorySanitizer: use-of-uninitialized-value

* Sat Nov 30 2019 daiqianwen <daiqianwen@huawei.com> - 0.11-2
- Package init

