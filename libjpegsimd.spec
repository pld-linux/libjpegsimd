# NOTE: JPEG SIMD code is now developed as part of libjpeg-turbo library
Summary:	Library for handling different JPEG files - x86 SIMD version
Summary(pl.UTF-8):	Biblioteka do manipulacji plikami w formacie JPEG - wersja x86 SIMD
Name:		libjpegsimd
%define	libjpegver	6b
%define	simdver		1.02
Version:	%{libjpegver}.%{simdver}
Release:	0.1
License:	distributable
Group:		Libraries
Source0:	http://cetus.sakura.ne.jp/softlab/jpeg-x86simd/sources/jpegsrc-%{libjpegver}-x86simd-%{simdver}.tar.bz2
# Source0-md5:	520b8aaaaa8c22eb1f30cade836177ce
Patch0:		%{name}-asm.patch
Patch1:		libjpeg-include.patch
Patch2:		%{name}-stack.patch
URL:		http://cetus.sakura.ne.jp/softlab/jpeg-x86simd/jpegsimd.html
BuildRequires:	libtool
BuildRequires:	nasm
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libjpegsimd package contains a library of functions for manipulating
JPEG images using x86 SIMD (MMX and SSE) extensions.

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę funkcji do manipulacji plikami JPEG z
wykorzystaniem rozszerzeń SIMD procesorów x86 (MMX i SSE).

%package devel
Summary:	Headers for developing programs using libjpegsimd
Summary(de.UTF-8):	Header zum Entwickeln von Programmen mit libjpegsimd
Summary(es.UTF-8):	Archivos de inclusión para desarrollar programas usando libjpegsimd
Summary(pl.UTF-8):	Pliki nagłówkowe libjpegsimd
Summary(pt_BR.UTF-8):	Arquivos de inclusão para desenvolver programas usando libjpegsimd
Summary(ru.UTF-8):	Хедеры для разработки программ, использующих libjpegsimd
Summary(uk.UTF-8):	Хедери для розробки програм, що використовують libjpegsimd
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The libjpegsimd-devel package includes the header files necessary for
developing programs which will manipulate JPEG files using the
libjpegsimd library.

%description devel -l de.UTF-8
Dieses Paket bietet alles, was Sie brauchen, um Programme zur
Manipulation von JPEG-Grafiken, einschließlich Dokumentation, zu
entwickeln.

%description devel -l es.UTF-8
Este paquete es todo lo que necesitas para desarrollar programas que
manipulen imágenes JPEG, incluso documentación.

%description devel -l fr.UTF-8
Ce package est tout ce dont vous avez besoin pour développer des
programmes manipulant des images JPEG, et comprend la documentation.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki potrzebne do programowania z wykorzystaniem
biblioteki libjpegsimd. Zawiera także dokumentację.

%description devel -l pt_BR.UTF-8
Este pacote é tudo que você precisa para desenvolver programas que
manipulam imagens JPEG, incluindo documentação.

%description devel -l ru.UTF-8
В этом пакете содержится все необходимое для разработки программ,
которые работают с JPEG-изображениями включая документацию.

%description devel -l uk.UTF-8
Цей пакет містить все необхідне для розробки програм, котрі працюють з
JPEG-зображеннями, включаючи документацію.

%package static
Summary:	Static library for developing programs using libjpegsimd
Summary(pl.UTF-8):	Biblioteka statyczna libjpegsimd
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com libjpegsimd
Summary(ru.UTF-8):	Статическая библиотека для программирования с libjpegsimd
Summary(uk.UTF-8):	Статична бібліотека для програмування з libjpegsimd
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static library for developing programs using libjpegsimd.

%description static -l pl.UTF-8
Statyczna biblioteka libjpegsimd.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com libjpegsimd.

%description static -l ru.UTF-8
Этот пакет содержит статические библиотеки, необходимые для написания
программ, использующих libjpegsimd.

%description static -l uk.UTF-8
Цей пакет містить статичні бібліотеки, необхідні для написання
програм, що використовують libjpegsimd.

%package progs
Summary:	Simple clients for manipulating JPEG images
Summary(de.UTF-8):	Einfachen Clients zur Manipulation von JPEG
Summary(fr.UTF-8):	Clients simples pour manipuler de telles images
Summary(pl.UTF-8):	Kilka prostych programów do manipulowania na plikach JPEG
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description progs
Simple clients for manipulating JPEG images. Libjpeg client programs
include cjpeg, djpeg, jpegtran, rdjpgcom and wrjpgcom. Djpeg
decompresses a JPEG file into a regular image file. Jpegtran can
perform various useful transformations on JPEG files. Rdjpgcom
displays any text comments included in a JPEG file. Wrjpgcom inserts
text comments into a JPEG file.

%description progs -l pl.UTF-8
Kilka prostych programów do obróbki plików JPEG, w tym: cjpeg, djpeg,
jpegtran, rdjpgcom i wrjpgcom. djpeg dekompresuje plik JPEG do
zwykłego pliku obrazu, jpegtran potrafi wykonywać różne
przekształcenia na plikach JPEG. rdjpgcom wyświetla komentarze
tekstowe dołączone do pliku JPEG, a wrjpgcom wstawia takie komentarze.

%prep
%setup -q -n jpeg-%{libjpegver}x
%patch0 -p1
%patch1 -p1
%patch2 -p1

cp -f %{_datadir}/libtool/config.sub .

%build
%configure2_13 \
	--enable-shared \
	--enable-static

%{__make} \
	libdir=%{_libdir}

LD_PRELOAD=$PWD/.libs/%{name}.so \
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	exec_prefix=$RPM_BUILD_ROOT%{_prefix} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README change.log
%lang(ja) %doc simd_{README,cdjpeg,changes}.ja.txt
%attr(755,root,root) %{_libdir}/libjpeg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjpeg.so.62

%files devel
%defattr(644,root,root,755)
%doc {libjpeg,structure}.doc
%attr(755,root,root) %{_libdir}/libjpeg.so
%{_libdir}/libjpeg.la
%{_includedir}/jconfig.h
%{_includedir}/jerror.h
%{_includedir}/jmorecfg.h
%{_includedir}/jpeglib.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libjpeg.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cjpeg
%attr(755,root,root) %{_bindir}/djpeg
%attr(755,root,root) %{_bindir}/jpegtran
%attr(755,root,root) %{_bindir}/rdjpgcom
%attr(755,root,root) %{_bindir}/wrjpgcom
%{_mandir}/man1/cjpeg.1*
%{_mandir}/man1/djpeg.1*
%{_mandir}/man1/jpegtran.1*
%{_mandir}/man1/rdjpgcom.1*
%{_mandir}/man1/wrjpgcom.1*
