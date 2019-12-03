Name:          opusfile
Version:       0.11
Release:       2
Summary:       A high-level API provides seeking, decode, and playback of Opus streams
License:       BSD
URL:           http://www.opus-codec.org/
Source0:       http://downloads.xiph.org/releases/opus/%{name}-%{version}.tar.gz

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
* Sat Nov 30 2019 daiqianwen <daiqianwen@huawei.com> - 0.11-2
- Package init
