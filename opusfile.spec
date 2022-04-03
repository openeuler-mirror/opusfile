Name:          opusfile
Version:       0.12
Release:       1
Summary:       A high-level API provides seeking, decode, and playback of Opus streams
License:       BSD
URL:           http://www.opus-codec.org/
Source0:       http://downloads.xiph.org/releases/opus/%{name}-%{version}.tar.gz
Patch0000:     0001-fix-MemorySanitizer-use-of-uninitialized-value.patch

BuildRequires:  gcc  libogg-devel openssl-devel opus-devel

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
* Sun Apr 03 2022 misaka00251 <misaka00251@misakanet.cn> - 0.12-1
- Upgrade package version

* Web 02 Jun 2021 zhaoyao<zhaoyao32@huawei.com> - 0.11-4
- fixs faileds: /bin/sh: gcc: command not found.

* Thu Dec 03 2020 maminjie <maminjie1@huawei.com> - 0.11-3
- fix MemorySanitizer: use-of-uninitialized-value

* Sat Nov 30 2019 daiqianwen <daiqianwen@huawei.com> - 0.11-2
- Package init

