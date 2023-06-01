#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : knotes
Version  : 23.04.1
Release  : 56
URL      : https://download.kde.org/stable/release-service/23.04.1/src/knotes-23.04.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.1/src/knotes-23.04.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.1/src/knotes-23.04.1.tar.xz.sig
Summary  : Popup notes
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0 LGPL-2.0 LGPL-3.0
Requires: knotes-bin = %{version}-%{release}
Requires: knotes-data = %{version}-%{release}
Requires: knotes-lib = %{version}-%{release}
Requires: knotes-license = %{version}-%{release}
Requires: knotes-locales = %{version}-%{release}
BuildRequires : akonadi-contacts-dev
BuildRequires : akonadi-dev
BuildRequires : akonadi-mime-dev
BuildRequires : akonadi-notes-dev
BuildRequires : akonadi-search-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : grantlee-dev
BuildRequires : grantleetheme-dev
BuildRequires : kcalendarcore-dev
BuildRequires : kcalutils-dev
BuildRequires : kcontacts-dev
BuildRequires : kdnssd-dev
BuildRequires : kglobalaccel-dev
BuildRequires : kimap-dev
BuildRequires : kimap-staticdev
BuildRequires : kmime-dev
BuildRequires : knotifyconfig-dev
BuildRequires : kontactinterface-dev
BuildRequires : kpimtextedit-dev
BuildRequires : ktextaddons-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : libkdepim-dev
BuildRequires : pimcommon-dev
BuildRequires : qt6base-dev
BuildRequires : qtx11extras-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
KNotes -- Notes for the K Desktop Environment
=============================================

%package bin
Summary: bin components for the knotes package.
Group: Binaries
Requires: knotes-data = %{version}-%{release}
Requires: knotes-license = %{version}-%{release}

%description bin
bin components for the knotes package.


%package data
Summary: data components for the knotes package.
Group: Data

%description data
data components for the knotes package.


%package doc
Summary: doc components for the knotes package.
Group: Documentation

%description doc
doc components for the knotes package.


%package lib
Summary: lib components for the knotes package.
Group: Libraries
Requires: knotes-data = %{version}-%{release}
Requires: knotes-license = %{version}-%{release}

%description lib
lib components for the knotes package.


%package license
Summary: license components for the knotes package.
Group: Default

%description license
license components for the knotes package.


%package locales
Summary: locales components for the knotes package.
Group: Default

%description locales
locales components for the knotes package.


%prep
%setup -q -n knotes-23.04.1
cd %{_builddir}/knotes-23.04.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685590679
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1685590679
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/knotes
cp %{_builddir}/knotes-%{version}/.krazy.license %{buildroot}/usr/share/package-licenses/knotes/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/knotes-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/knotes/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/knotes-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/knotes/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/knotes-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/knotes/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/knotes-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/knotes/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/knotes-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/knotes/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/knotes-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/knotes/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/knotes-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/knotes/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/knotes-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/knotes/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/knotes-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/knotes/e458941548e0864907e654fa2e192844ae90fc32 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang knotes
%find_lang akonadi_notes_agent
%find_lang libnoteshared
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/akonadi_notes_agent
/V3/usr/bin/knotes
/usr/bin/akonadi_notes_agent
/usr/bin/knotes

%files data
%defattr(-,root,root,-)
/usr/share/akonadi/agents/notesagent.desktop
/usr/share/applications/org.kde.knotes.desktop
/usr/share/config.kcfg/knotesglobalconfig.kcfg
/usr/share/config.kcfg/notesagentsettings.kcfg
/usr/share/dbus-1/interfaces/org.kde.KNotes.xml
/usr/share/dbus-1/interfaces/org.kde.kontact.KNotes.xml
/usr/share/icons/hicolor/128x128/apps/knotes.png
/usr/share/icons/hicolor/16x16/actions/knotes_alarm.png
/usr/share/icons/hicolor/16x16/actions/knotes_close.png
/usr/share/icons/hicolor/16x16/actions/knotes_date.png
/usr/share/icons/hicolor/16x16/actions/knotes_delete.png
/usr/share/icons/hicolor/16x16/apps/knotes.png
/usr/share/icons/hicolor/22x22/apps/knotes.png
/usr/share/icons/hicolor/32x32/apps/knotes.png
/usr/share/icons/hicolor/48x48/apps/knotes.png
/usr/share/icons/hicolor/64x64/apps/knotes.png
/usr/share/icons/hicolor/scalable/apps/knotes.svg
/usr/share/knotes/print/themes/background-color/theme.desktop
/usr/share/knotes/print/themes/background-color/theme.html
/usr/share/knotes/print/themes/big-title/theme.desktop
/usr/share/knotes/print/themes/big-title/theme.html
/usr/share/knotes/print/themes/default/theme.desktop
/usr/share/knotes/print/themes/default/theme.html
/usr/share/knotifications5/akonadi_notes_agent.notifyrc
/usr/share/knsrcfiles/knotes_printing_theme.knsrc
/usr/share/kxmlgui5/knotes/knotes_part.rc
/usr/share/kxmlgui5/knotes/knotesappui.rc
/usr/share/kxmlgui5/knotes/knotesui.rc
/usr/share/metainfo/org.kde.knotes.appdata.xml
/usr/share/qlogging-categories5/knotes.categories
/usr/share/qlogging-categories5/knotes.renamecategories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/akonadi_notes_agent/index.cache.bz2
/usr/share/doc/HTML/ca/akonadi_notes_agent/index.docbook
/usr/share/doc/HTML/ca/knotes/index.cache.bz2
/usr/share/doc/HTML/ca/knotes/index.docbook
/usr/share/doc/HTML/de/akonadi_notes_agent/index.cache.bz2
/usr/share/doc/HTML/de/akonadi_notes_agent/index.docbook
/usr/share/doc/HTML/de/knotes/index.cache.bz2
/usr/share/doc/HTML/de/knotes/index.docbook
/usr/share/doc/HTML/en/akonadi_notes_agent/index.cache.bz2
/usr/share/doc/HTML/en/akonadi_notes_agent/index.docbook
/usr/share/doc/HTML/en/knotes/index.cache.bz2
/usr/share/doc/HTML/en/knotes/index.docbook
/usr/share/doc/HTML/en/knotes/select-notes-folder.png
/usr/share/doc/HTML/es/akonadi_notes_agent/index.cache.bz2
/usr/share/doc/HTML/es/akonadi_notes_agent/index.docbook
/usr/share/doc/HTML/es/knotes/index.cache.bz2
/usr/share/doc/HTML/es/knotes/index.docbook
/usr/share/doc/HTML/et/akonadi_notes_agent/index.cache.bz2
/usr/share/doc/HTML/et/akonadi_notes_agent/index.docbook
/usr/share/doc/HTML/et/knotes/index.cache.bz2
/usr/share/doc/HTML/et/knotes/index.docbook
/usr/share/doc/HTML/fr/akonadi_notes_agent/index.cache.bz2
/usr/share/doc/HTML/fr/akonadi_notes_agent/index.docbook
/usr/share/doc/HTML/fr/knotes/index.cache.bz2
/usr/share/doc/HTML/fr/knotes/index.docbook
/usr/share/doc/HTML/it/akonadi_notes_agent/index.cache.bz2
/usr/share/doc/HTML/it/akonadi_notes_agent/index.docbook
/usr/share/doc/HTML/it/knotes/index.cache.bz2
/usr/share/doc/HTML/it/knotes/index.docbook
/usr/share/doc/HTML/nl/akonadi_notes_agent/index.cache.bz2
/usr/share/doc/HTML/nl/akonadi_notes_agent/index.docbook
/usr/share/doc/HTML/nl/knotes/index.cache.bz2
/usr/share/doc/HTML/nl/knotes/index.docbook
/usr/share/doc/HTML/pt/akonadi_notes_agent/index.cache.bz2
/usr/share/doc/HTML/pt/akonadi_notes_agent/index.docbook
/usr/share/doc/HTML/pt/knotes/index.cache.bz2
/usr/share/doc/HTML/pt/knotes/index.docbook
/usr/share/doc/HTML/pt_BR/akonadi_notes_agent/index.cache.bz2
/usr/share/doc/HTML/pt_BR/akonadi_notes_agent/index.docbook
/usr/share/doc/HTML/pt_BR/knotes/index.cache.bz2
/usr/share/doc/HTML/pt_BR/knotes/index.docbook
/usr/share/doc/HTML/ru/akonadi_notes_agent/index.cache.bz2
/usr/share/doc/HTML/ru/akonadi_notes_agent/index.docbook
/usr/share/doc/HTML/ru/knotes/index.cache.bz2
/usr/share/doc/HTML/ru/knotes/index.docbook
/usr/share/doc/HTML/sv/akonadi_notes_agent/index.cache.bz2
/usr/share/doc/HTML/sv/akonadi_notes_agent/index.docbook
/usr/share/doc/HTML/sv/knotes/index.cache.bz2
/usr/share/doc/HTML/sv/knotes/index.docbook
/usr/share/doc/HTML/tr/akonadi_notes_agent/index.cache.bz2
/usr/share/doc/HTML/tr/akonadi_notes_agent/index.docbook
/usr/share/doc/HTML/uk/akonadi_notes_agent/index.cache.bz2
/usr/share/doc/HTML/uk/akonadi_notes_agent/index.docbook
/usr/share/doc/HTML/uk/knotes/index.cache.bz2
/usr/share/doc/HTML/uk/knotes/index.docbook

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libknotesprivate.so.5.23.1
/V3/usr/lib64/libnotesharedprivate.so.5.23.1
/V3/usr/lib64/qt5/plugins/pim5/kcms/knotes/kcm_knote_action.so
/V3/usr/lib64/qt5/plugins/pim5/kcms/knotes/kcm_knote_collection.so
/V3/usr/lib64/qt5/plugins/pim5/kcms/knotes/kcm_knote_display.so
/V3/usr/lib64/qt5/plugins/pim5/kcms/knotes/kcm_knote_editor.so
/V3/usr/lib64/qt5/plugins/pim5/kcms/knotes/kcm_knote_misc.so
/V3/usr/lib64/qt5/plugins/pim5/kcms/knotes/kcm_knote_network.so
/V3/usr/lib64/qt5/plugins/pim5/kcms/knotes/kcm_knote_print.so
/V3/usr/lib64/qt5/plugins/pim5/kcms/summary/kcmknotessummary.so
/V3/usr/lib64/qt5/plugins/pim5/kontact/kontact_knotesplugin.so
/usr/lib64/libknotesprivate.so.5
/usr/lib64/libknotesprivate.so.5.23.1
/usr/lib64/libnotesharedprivate.so.5
/usr/lib64/libnotesharedprivate.so.5.23.1
/usr/lib64/qt5/plugins/pim5/kcms/knotes/kcm_knote_action.so
/usr/lib64/qt5/plugins/pim5/kcms/knotes/kcm_knote_collection.so
/usr/lib64/qt5/plugins/pim5/kcms/knotes/kcm_knote_display.so
/usr/lib64/qt5/plugins/pim5/kcms/knotes/kcm_knote_editor.so
/usr/lib64/qt5/plugins/pim5/kcms/knotes/kcm_knote_misc.so
/usr/lib64/qt5/plugins/pim5/kcms/knotes/kcm_knote_network.so
/usr/lib64/qt5/plugins/pim5/kcms/knotes/kcm_knote_print.so
/usr/lib64/qt5/plugins/pim5/kcms/summary/kcmknotessummary.so
/usr/lib64/qt5/plugins/pim5/kontact/kontact_knotesplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/knotes/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/knotes/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/knotes/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/knotes/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/knotes/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/knotes/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/knotes/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/knotes/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f knotes.lang -f akonadi_notes_agent.lang -f libnoteshared.lang
%defattr(-,root,root,-)

