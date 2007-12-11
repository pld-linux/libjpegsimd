Summary:	Library for handling different jpeg files
Summary(de.UTF-8):	Library zum Verarbeiten verschiedener jpeg-Dateien
Summary(es.UTF-8):	Biblioteca para manipulación de diferentes archivos jpegs
Summary(fr.UTF-8):	Bibliothèque pour gérer différents fichiers jpeg
Summary(pl.UTF-8):	Biblioteka do manipulacji plikami w formacie jpeg
Summary(pt_BR.UTF-8):	Biblioteca para manipulação de diferentes arquivos jpegs
Summary(ru.UTF-8):	Библиотека для обработки различных jpeg-файлов
Summary(tr.UTF-8):	jpeg resimlerini işleme kitaplığı
Summary(uk.UTF-8):	Бібліотека для обробки різноманітних jpeg-файлів
Name:		libjpegsimd
%define	libjpegsimdver	6b
%define	simdver		1.02
Version:	%{libjpegsimdver}.%{simdver}
Release:	0.1
License:	distributable
Group:		Libraries
Source0:	http://cetus.sakura.ne.jp/softlab/jpeg-x86simd/sources/jpegsrc-6b-x86simd-1.02.tar.bz2
# Source0-md5:	520b8aaaaa8c22eb1f30cade836177ce
URL:		http://cetus.sakura.ne.jp/softlab/jpeg-x86simd/jpegsimd.html
Patch0:		%{name}-asm.patch
Patch1:		libjpeg-include.patch
BuildRequires:	libtool
BuildRequires:	nasm
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libjpegsimd package contains a library of functions for manipulating
JPEG images.

This version uses MMX and SSE extensions.

%description -l de.UTF-8
Dieses Paket ist eine Library mit Funktionen zur Manipulation von
jpeg-Bildern, zusammen mit einfachen Clients zur Manipulation von
jpeg.

%description -l es.UTF-8
Este paquete contiene una biblioteca de funciones y programas
sencillos que manipulan imágenes jpeg.

%description -l fr.UTF-8
Bibliothèque de fonctions qui manipulent des images jpeg, et clients
simples pour manipuler de telles images.

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę funkcji do manipulacji plikami jpeg.

%description -l pt_BR.UTF-8
Este pacote contém uma biblioteca de funções e programas simples que
manipulam imagens jpeg.

%description -l ru.UTF-8
Библиотека функций для обработки jpeg-изображений и простые клиенты
для такой обработки.

%description -l tr.UTF-8
Bu paket, jpeg şekillerini işlemek için kitaplıklar ve basit
istemciler içerir.

%description -l uk.UTF-8
Бібліотека функцій для обробки jpeg-зображень та прості клієнти для
такої обробки.

%package devel
Summary:	Headers for developing programs using libjpegsimd
Summary(de.UTF-8):	Header und statische Libraries zum Entwickeln von Programmen mit libjpegsimd
Summary(es.UTF-8):	Archivos de inclusión y bibliotecas para desarrollar programas usando libjpegsimd
Summary(fr.UTF-8):	Bibliothèques statiques et en-têtes pour développer avec libjpegsimd
Summary(pl.UTF-8):	Pliki nagłówkowe libjpegsimd
Summary(pt_BR.UTF-8):	Arquivos de inclusão e bibliotecas para desenvolver programas usando libjpegsimd
Summary(ru.UTF-8):	Хедеры и библиотека для разработки программ, использующих libjpegsimd
Summary(tr.UTF-8):	libjpegsimd için geliştirme kitaplıkları ve başlık dosyaları
Summary(uk.UTF-8):	Хедери та бібліотека для розробки програм, що використовують libjpegsimd
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The libjpegsimd-devel package includes the header files and static
libraries necessary for developing programs which will manipulate JPEG
files using the libjpegsimd library.

If you are going to develop programs which will manipulate JPEG
images, you should install libjpegsimd-devel. You'll also need to have the
libjpegsimd package installed.

%description devel -l de.UTF-8
Dieses Paket bietet alles, was Sie brauchen, um Programme zur
Manipulation von jpeg-Grafiken, einschließlich Dokumentation, zu
entwickeln.

%description devel -l es.UTF-8
Este paquete es todo lo que necesitas para desarrollar programas que
manipulen imágenes jpeg, incluso documentación.

%description devel -l fr.UTF-8
Ce package est tout ce dont vous avez besoin pour développer des
programmes manipulant des images jpg, et comprend la documentation.

%description devel -l pl.UTF-8
Ten pakiet pozwoli Ci na programowanie z wykorzystaniem formatu jpeg.
Zawiera także dokumentację.

%description devel -l pt_BR.UTF-8
Este pacote é tudo que você precisa para desenvolver programas que
manipulam imagens jpeg, incluindo documentação.

%description devel -l ru.UTF-8
В этом пакете содержится все необходимое для разработки программ,
которые работают с jpeg-изображениями включая документацию.

%description devel -l tr.UTF-8
Bu paket, jpeg resimlerini işleyen programlar geliştirmeniz için
gereken başlık dosyalarını, kitaplıkları ve ilgili yardım belgelerini
içerir.

%description devel -l uk.UTF-8
Цей пакет містить все необхідне для розробки програм, котрі працюють з
jpeg-зображеннями, включаючи документацію.

%package progs
Summary:	Simple clients for manipulating jpeg images
Summary(de.UTF-8):	Einfachen Clients zur Manipulation von jpeg
Summary(fr.UTF-8):	Clients simples pour manipuler de telles images
Summary(pl.UTF-8):	Kilka prostych programów do manipulowania na plikach jpeg
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description progs
Simple clients for manipulating jpeg images. Libjpeg client programs
include cjpeg, djpeg, jpegtran, rdjpgcom and wrjpgcom. Djpeg
decompresses a JPEG file into a regular image file. Jpegtran can
perform various useful transformations on JPEG files. Rdjpgcom
displays any text comments included in a JPEG file. Wrjpgcom inserts
text comments into a JPEG file.

%description progs -l de.UTF-8
Einfachen Clients zur Manipulation von jpeg.

%description progs -l fr.UTF-8
Clients simples pour manipuler de telles images.

%description progs -l pl.UTF-8
Kilka prostych programów do manipulowania na plikach jpeg.

%package static
Summary:	Static libraries for developing programs using libjpegsimd
Summary(pl.UTF-8):	Biblioteki statyczne libjpegsimd
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com libjpegsimd
Summary(ru.UTF-8):	Статическая библиотека для программирования с libjpegsimd
Summary(uk.UTF-8):	Статична бібліотека для програмування з libjpegsimd
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for developing programs using libjpegsimd.

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

%prep
%setup  -q -n jpeg-%{libjpegsimdver}x
%patch0 -p1
%patch1 -p1

cp -f %{_datadir}/libtool/config.sub .

%build
%configure2_13 \
	--enable-shared \
	--enable-static

%{__make} \
	libdir=%{_libdir}

LD_PRELOAD=$PWD/.libs/%{name}.so make test

%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {libjpeg,structure}.doc

%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
