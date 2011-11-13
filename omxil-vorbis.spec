Summary:	Vorbis decoder component for Bellagio OpenMAX IL
Summary(pl.UTF-8):	Komponent dekodujący Vorbis dla implementacji Bellagio OpenMAX IL
Name:		omxil-vorbis
Version:	0.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/omxil/libomxvorbis-%{version}.tar.gz
# Source0-md5:	66039038637f634ab591095fae511e1c
URL:		http://omxil.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libomxil-bellagio-devel >= 0.9
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	libomxil-bellagio >= 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/usr/%{_lib}/bellagio

%description
Vorbis component is an audio decoder component for Bellagio OpenMAX IL
that uses libvorbis for decoding.

%description -l pl.UTF-8
Komponent Vorbis to komponent dekodujący dźwięk dla implementacji
Bellagio OpenMAX IL, wykorzystujący do dekodowania bibliotekę
libvorbis.

%prep
%setup -q -n libomxvorbis-%{version}

# warning about set but unused variable
sed -i -e 's/ -Werror//' configure.ac

%build
# rebuild for as-needed to work
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libomxvorbis.so*
