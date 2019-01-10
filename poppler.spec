#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3A6A4DB839EAA6D7 (aacid@kde.org)
#
Name     : poppler
Version  : 0.72.0
Release  : 4
URL      : https://poppler.freedesktop.org/poppler-0.72.0.tar.xz
Source0  : https://poppler.freedesktop.org/poppler-0.72.0.tar.xz
Source99 : https://poppler.freedesktop.org/poppler-0.72.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-3.0
Requires: poppler-bin = %{version}-%{release}
Requires: poppler-data = %{version}-%{release}
Requires: poppler-lib = %{version}-%{release}
Requires: poppler-license = %{version}-%{release}
Requires: poppler-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : curl-dev
BuildRequires : freetype-dev
BuildRequires : glibc-bin
BuildRequires : glibc-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(cairo-pdf)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(nss)
BuildRequires : qtbase-extras
BuildRequires : tiff-dev
BuildRequires : zlib-dev
Patch1: CVE-2018-20481.patch
Patch2: CVE-2018-20551.patch
Patch3: CVE-2018-20650.patch

%description
This is poppler, a PDF rendering library.
Poppler is a fork of the xpdf PDF viewer developed by Derek Noonburg
of Glyph and Cog, LLC.  The purpose of forking xpdf is twofold.
First, we want to provide PDF rendering functionality as a shared
library, to centralize the maintenance effort.  Today a number of
applications incorporate the xpdf code base, and whenever a security
issue is discovered, all these applications exchange patches and put
out new releases.  In turn, all distributions must package and release
new version of these xpdf based viewers.  It's safe to say that
there's a lot of duplicated effort with the current situation.  Even if
poppler in the short term introduces yet another xpdf derived code
base to the world, we hope that over time these applications will
adopt poppler.  After all, we only need one application to use poppler
to break even.

%package bin
Summary: bin components for the poppler package.
Group: Binaries
Requires: poppler-data = %{version}-%{release}
Requires: poppler-license = %{version}-%{release}
Requires: poppler-man = %{version}-%{release}

%description bin
bin components for the poppler package.


%package data
Summary: data components for the poppler package.
Group: Data

%description data
data components for the poppler package.


%package dev
Summary: dev components for the poppler package.
Group: Development
Requires: poppler-lib = %{version}-%{release}
Requires: poppler-bin = %{version}-%{release}
Requires: poppler-data = %{version}-%{release}
Provides: poppler-devel = %{version}-%{release}

%description dev
dev components for the poppler package.


%package lib
Summary: lib components for the poppler package.
Group: Libraries
Requires: poppler-data = %{version}-%{release}
Requires: poppler-license = %{version}-%{release}

%description lib
lib components for the poppler package.


%package license
Summary: license components for the poppler package.
Group: Default

%description license
license components for the poppler package.


%package man
Summary: man components for the poppler package.
Group: Default

%description man
man components for the poppler package.


%prep
%setup -q -n poppler-0.72.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
pushd ..
cp -a poppler-0.72.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547229827
mkdir -p clr-build
pushd clr-build
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
%cmake .. -DENABLE_XPDF_HEADERS=ON -DENABLE_UTILS=ON -DENABLE_LIBOPENJPEG=none
make  %{?_smp_mflags} VERBOSE=1
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -march=haswell -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -march=haswell -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -march=haswell -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -march=haswell -mzero-caller-saved-regs=used "
export CFLAGS="$CFLAGS -march=haswell -m64"
export CXXFLAGS="$CXXFLAGS -march=haswell -m64"
%cmake .. -DENABLE_XPDF_HEADERS=ON -DENABLE_UTILS=ON -DENABLE_LIBOPENJPEG=none
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1547229827
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/poppler
cp COPYING %{buildroot}/usr/share/package-licenses/poppler/COPYING
cp COPYING3 %{buildroot}/usr/share/package-licenses/poppler/COPYING3
cp cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/poppler/cmake_modules_COPYING-CMAKE-SCRIPTS
pushd clr-build-avx2
%make_install_avx2  || :
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/haswell/pdfdetach
%exclude /usr/bin/haswell/pdffonts
%exclude /usr/bin/haswell/pdfimages
%exclude /usr/bin/haswell/pdfinfo
%exclude /usr/bin/haswell/pdfseparate
%exclude /usr/bin/haswell/pdfsig
%exclude /usr/bin/haswell/pdftocairo
%exclude /usr/bin/haswell/pdftohtml
%exclude /usr/bin/haswell/pdftoppm
%exclude /usr/bin/haswell/pdftops
%exclude /usr/bin/haswell/pdftotext
%exclude /usr/bin/haswell/pdfunite
%exclude /usr/bin/pdfdetach
%exclude /usr/bin/pdffonts
%exclude /usr/bin/pdfimages
%exclude /usr/bin/pdfinfo
%exclude /usr/bin/pdfseparate
%exclude /usr/bin/pdfsig
%exclude /usr/bin/pdftocairo
%exclude /usr/bin/pdftohtml
%exclude /usr/bin/pdftoppm
%exclude /usr/bin/pdftops
%exclude /usr/bin/pdftotext
%exclude /usr/bin/pdfunite

%files data
%defattr(-,root,root,-)
%exclude /usr/lib64/girepository-1.0/Poppler-0.18.typelib
%exclude /usr/share/gir-1.0/Poppler-0.18.gir

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/poppler/Annot.h
%exclude /usr/include/poppler/Array.h
%exclude /usr/include/poppler/BuiltinFont.h
%exclude /usr/include/poppler/BuiltinFontTables.h
%exclude /usr/include/poppler/CMap.h
%exclude /usr/include/poppler/CachedFile.h
%exclude /usr/include/poppler/Catalog.h
%exclude /usr/include/poppler/CharCodeToUnicode.h
%exclude /usr/include/poppler/CharTypes.h
%exclude /usr/include/poppler/CompactFontTables.h
%exclude /usr/include/poppler/CurlCachedFile.h
%exclude /usr/include/poppler/CurlPDFDocBuilder.h
%exclude /usr/include/poppler/DateInfo.h
%exclude /usr/include/poppler/Decrypt.h
%exclude /usr/include/poppler/Dict.h
%exclude /usr/include/poppler/Error.h
%exclude /usr/include/poppler/ErrorCodes.h
%exclude /usr/include/poppler/FileSpec.h
%exclude /usr/include/poppler/FontEncodingTables.h
%exclude /usr/include/poppler/FontInfo.h
%exclude /usr/include/poppler/Form.h
%exclude /usr/include/poppler/Function.h
%exclude /usr/include/poppler/Gfx.h
%exclude /usr/include/poppler/GfxFont.h
%exclude /usr/include/poppler/GfxState.h
%exclude /usr/include/poppler/GfxState_helpers.h
%exclude /usr/include/poppler/GlobalParams.h
%exclude /usr/include/poppler/Hints.h
%exclude /usr/include/poppler/JArithmeticDecoder.h
%exclude /usr/include/poppler/JBIG2Stream.h
%exclude /usr/include/poppler/JPXStream.h
%exclude /usr/include/poppler/Lexer.h
%exclude /usr/include/poppler/Linearization.h
%exclude /usr/include/poppler/Link.h
%exclude /usr/include/poppler/LocalPDFDocBuilder.h
%exclude /usr/include/poppler/MarkedContentOutputDev.h
%exclude /usr/include/poppler/Movie.h
%exclude /usr/include/poppler/NameToCharCode.h
%exclude /usr/include/poppler/NameToUnicodeTable.h
%exclude /usr/include/poppler/Object.h
%exclude /usr/include/poppler/OptionalContent.h
%exclude /usr/include/poppler/Outline.h
%exclude /usr/include/poppler/OutputDev.h
%exclude /usr/include/poppler/PDFDoc.h
%exclude /usr/include/poppler/PDFDocBuilder.h
%exclude /usr/include/poppler/PDFDocEncoding.h
%exclude /usr/include/poppler/PDFDocFactory.h
%exclude /usr/include/poppler/PSOutputDev.h
%exclude /usr/include/poppler/PSTokenizer.h
%exclude /usr/include/poppler/Page.h
%exclude /usr/include/poppler/PageTransition.h
%exclude /usr/include/poppler/Parser.h
%exclude /usr/include/poppler/PopplerCache.h
%exclude /usr/include/poppler/PreScanOutputDev.h
%exclude /usr/include/poppler/ProfileData.h
%exclude /usr/include/poppler/Rendition.h
%exclude /usr/include/poppler/SecurityHandler.h
%exclude /usr/include/poppler/Sound.h
%exclude /usr/include/poppler/SplashOutputDev.h
%exclude /usr/include/poppler/StdinCachedFile.h
%exclude /usr/include/poppler/StdinPDFDocBuilder.h
%exclude /usr/include/poppler/Stream-CCITT.h
%exclude /usr/include/poppler/Stream.h
%exclude /usr/include/poppler/StructElement.h
%exclude /usr/include/poppler/StructTreeRoot.h
%exclude /usr/include/poppler/TextOutputDev.h
%exclude /usr/include/poppler/UTF.h
%exclude /usr/include/poppler/UnicodeCClassTables.h
%exclude /usr/include/poppler/UnicodeCompTables.h
%exclude /usr/include/poppler/UnicodeDecompTables.h
%exclude /usr/include/poppler/UnicodeMap.h
%exclude /usr/include/poppler/UnicodeMapFuncs.h
%exclude /usr/include/poppler/UnicodeMapTables.h
%exclude /usr/include/poppler/UnicodeTypeTable.h
%exclude /usr/include/poppler/ViewerPreferences.h
%exclude /usr/include/poppler/XRef.h
%exclude /usr/include/poppler/cpp/poppler-document.h
%exclude /usr/include/poppler/cpp/poppler-embedded-file.h
%exclude /usr/include/poppler/cpp/poppler-font.h
%exclude /usr/include/poppler/cpp/poppler-global.h
%exclude /usr/include/poppler/cpp/poppler-image.h
%exclude /usr/include/poppler/cpp/poppler-page-renderer.h
%exclude /usr/include/poppler/cpp/poppler-page-transition.h
%exclude /usr/include/poppler/cpp/poppler-page.h
%exclude /usr/include/poppler/cpp/poppler-rectangle.h
%exclude /usr/include/poppler/cpp/poppler-toc.h
%exclude /usr/include/poppler/cpp/poppler-version.h
%exclude /usr/include/poppler/fofi/FoFiBase.h
%exclude /usr/include/poppler/fofi/FoFiEncodings.h
%exclude /usr/include/poppler/fofi/FoFiIdentifier.h
%exclude /usr/include/poppler/fofi/FoFiTrueType.h
%exclude /usr/include/poppler/fofi/FoFiType1.h
%exclude /usr/include/poppler/fofi/FoFiType1C.h
%exclude /usr/include/poppler/glib/poppler-action.h
%exclude /usr/include/poppler/glib/poppler-annot.h
%exclude /usr/include/poppler/glib/poppler-attachment.h
%exclude /usr/include/poppler/glib/poppler-date.h
%exclude /usr/include/poppler/glib/poppler-document.h
%exclude /usr/include/poppler/glib/poppler-enums.h
%exclude /usr/include/poppler/glib/poppler-features.h
%exclude /usr/include/poppler/glib/poppler-form-field.h
%exclude /usr/include/poppler/glib/poppler-layer.h
%exclude /usr/include/poppler/glib/poppler-macros.h
%exclude /usr/include/poppler/glib/poppler-media.h
%exclude /usr/include/poppler/glib/poppler-movie.h
%exclude /usr/include/poppler/glib/poppler-page.h
%exclude /usr/include/poppler/glib/poppler-structure-element.h
%exclude /usr/include/poppler/glib/poppler.h
%exclude /usr/include/poppler/goo/FixedPoint.h
%exclude /usr/include/poppler/goo/GooCheckedOps.h
%exclude /usr/include/poppler/goo/GooLikely.h
%exclude /usr/include/poppler/goo/GooList.h
%exclude /usr/include/poppler/goo/GooString.h
%exclude /usr/include/poppler/goo/GooTimer.h
%exclude /usr/include/poppler/goo/ImgWriter.h
%exclude /usr/include/poppler/goo/JpegWriter.h
%exclude /usr/include/poppler/goo/PNGWriter.h
%exclude /usr/include/poppler/goo/TiffWriter.h
%exclude /usr/include/poppler/goo/gdir.h
%exclude /usr/include/poppler/goo/gfile.h
%exclude /usr/include/poppler/goo/gmem.h
%exclude /usr/include/poppler/goo/grandom.h
%exclude /usr/include/poppler/goo/gstrtod.h
%exclude /usr/include/poppler/goo/gtypes.h
%exclude /usr/include/poppler/poppler-config.h
%exclude /usr/include/poppler/qt5/poppler-annotation.h
%exclude /usr/include/poppler/qt5/poppler-export.h
%exclude /usr/include/poppler/qt5/poppler-form.h
%exclude /usr/include/poppler/qt5/poppler-link.h
%exclude /usr/include/poppler/qt5/poppler-media.h
%exclude /usr/include/poppler/qt5/poppler-optcontent.h
%exclude /usr/include/poppler/qt5/poppler-page-transition.h
%exclude /usr/include/poppler/qt5/poppler-qt5.h
%exclude /usr/include/poppler/splash/Splash.h
%exclude /usr/include/poppler/splash/SplashBitmap.h
%exclude /usr/include/poppler/splash/SplashClip.h
%exclude /usr/include/poppler/splash/SplashErrorCodes.h
%exclude /usr/include/poppler/splash/SplashFTFont.h
%exclude /usr/include/poppler/splash/SplashFTFontEngine.h
%exclude /usr/include/poppler/splash/SplashFTFontFile.h
%exclude /usr/include/poppler/splash/SplashFont.h
%exclude /usr/include/poppler/splash/SplashFontEngine.h
%exclude /usr/include/poppler/splash/SplashFontFile.h
%exclude /usr/include/poppler/splash/SplashFontFileID.h
%exclude /usr/include/poppler/splash/SplashGlyphBitmap.h
%exclude /usr/include/poppler/splash/SplashMath.h
%exclude /usr/include/poppler/splash/SplashPath.h
%exclude /usr/include/poppler/splash/SplashPattern.h
%exclude /usr/include/poppler/splash/SplashScreen.h
%exclude /usr/include/poppler/splash/SplashState.h
%exclude /usr/include/poppler/splash/SplashTypes.h
%exclude /usr/include/poppler/splash/SplashXPath.h
%exclude /usr/include/poppler/splash/SplashXPathScanner.h
%exclude /usr/lib64/haswell/libpoppler-cpp.so
%exclude /usr/lib64/haswell/libpoppler-glib.so
%exclude /usr/lib64/haswell/libpoppler-qt5.so
%exclude /usr/lib64/haswell/libpoppler.so
%exclude /usr/lib64/libpoppler-cpp.so
%exclude /usr/lib64/libpoppler-glib.so
%exclude /usr/lib64/libpoppler-qt5.so
%exclude /usr/lib64/libpoppler.so
%exclude /usr/lib64/pkgconfig/poppler-cairo.pc
%exclude /usr/lib64/pkgconfig/poppler-cpp.pc
%exclude /usr/lib64/pkgconfig/poppler-glib.pc
%exclude /usr/lib64/pkgconfig/poppler-qt5.pc
%exclude /usr/lib64/pkgconfig/poppler-splash.pc
%exclude /usr/lib64/pkgconfig/poppler.pc

%files lib
%defattr(-,root,root,-)
%exclude /usr/lib64/haswell/libpoppler-cpp.so.0
%exclude /usr/lib64/haswell/libpoppler-cpp.so.0.5.0
%exclude /usr/lib64/haswell/libpoppler-glib.so.8
%exclude /usr/lib64/haswell/libpoppler-glib.so.8.11.0
%exclude /usr/lib64/haswell/libpoppler-qt5.so.1
%exclude /usr/lib64/haswell/libpoppler-qt5.so.1.17.0
%exclude /usr/lib64/libpoppler-cpp.so.0
%exclude /usr/lib64/libpoppler-cpp.so.0.5.0
%exclude /usr/lib64/libpoppler-glib.so.8
%exclude /usr/lib64/libpoppler-glib.so.8.11.0
%exclude /usr/lib64/libpoppler-qt5.so.1
%exclude /usr/lib64/libpoppler-qt5.so.1.17.0
/usr/lib64/haswell/libpoppler.so.83
/usr/lib64/haswell/libpoppler.so.83.0.0
/usr/lib64/libpoppler.so.83
/usr/lib64/libpoppler.so.83.0.0

%files license
%defattr(0644,root,root,0755)
%exclude /usr/share/package-licenses/poppler/COPYING
%exclude /usr/share/package-licenses/poppler/COPYING3
%exclude /usr/share/package-licenses/poppler/cmake_modules_COPYING-CMAKE-SCRIPTS

%files man
%defattr(0644,root,root,0755)
%exclude /usr/share/man/man1/pdfdetach.1
%exclude /usr/share/man/man1/pdffonts.1
%exclude /usr/share/man/man1/pdfimages.1
%exclude /usr/share/man/man1/pdfinfo.1
%exclude /usr/share/man/man1/pdfseparate.1
%exclude /usr/share/man/man1/pdfsig.1
%exclude /usr/share/man/man1/pdftocairo.1
%exclude /usr/share/man/man1/pdftohtml.1
%exclude /usr/share/man/man1/pdftoppm.1
%exclude /usr/share/man/man1/pdftops.1
%exclude /usr/share/man/man1/pdftotext.1
%exclude /usr/share/man/man1/pdfunite.1
