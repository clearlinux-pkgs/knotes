#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : knotes
Version  : 19.08.0
Release  : 10
URL      : https://download.kde.org/stable/applications/19.08.0/src/knotes-19.08.0.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.0/src/knotes-19.08.0.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.0/src/knotes-19.08.0.tar.xz.sig
Summary  : Popup notes
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0 LGPL-2.1
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
BuildRequires : grantlee-dev
BuildRequires : grantleetheme-dev
BuildRequires : kcalcore-dev
BuildRequires : kcalutils-dev
BuildRequires : kcontacts-dev
BuildRequires : kdnssd-dev
BuildRequires : kglobalaccel-dev
BuildRequires : kimap-dev
BuildRequires : kmime-dev
BuildRequires : knotifyconfig-dev
BuildRequires : kontactinterface-dev
BuildRequires : kpimtextedit-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : libkdepim-dev
BuildRequires : pimcommon-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtx11extras-dev

%description
4.13:
-----
KNotes printing theme support:
- note name : use "name"
- note description: use "description" keyword
- current date time: use "currentDateTime" keyword
- allow to inform that we have an alarm: use "hasAlarm" keyword
- show alarm info: use "alarm" keyword (return date time as long format)
- allow to inform that note is locked: use "isLock" keyword
- note backgroundcolor name : use "backgroundColorName" keyword

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
%setup -q -n knotes-19.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565938795
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1565938795
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/knotes
cp COPYING %{buildroot}/usr/share/package-licenses/knotes/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/knotes/COPYING.DOC
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/knotes/COPYING.LIB
cp cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/knotes/cmake_modules_COPYING-CMAKE-SCRIPTS
pushd clr-build
%make_install
popd
%find_lang akonadi_notes_agent
%find_lang knotes
%find_lang libnoteshared

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/share/kconf_update/knotes-15.08-kickoff.sh
/usr/share/kconf_update/knotes.upd
/usr/share/knotes/print/themes/background-color/theme.desktop
/usr/share/knotes/print/themes/background-color/theme.html
/usr/share/knotes/print/themes/big-title/theme.desktop
/usr/share/knotes/print/themes/big-title/theme.html
/usr/share/knotes/print/themes/default/theme.desktop
/usr/share/knotes/print/themes/default/theme.html
/usr/share/knotifications5/akonadi_notes_agent.notifyrc
/usr/share/knsrcfiles/knotes_printing_theme.knsrc
/usr/share/kontact/ksettingsdialog/knotes.setdlg
/usr/share/kservices5/kcmknotessummary.desktop
/usr/share/kservices5/knote_config_action.desktop
/usr/share/kservices5/knote_config_collection.desktop
/usr/share/kservices5/knote_config_display.desktop
/usr/share/kservices5/knote_config_editor.desktop
/usr/share/kservices5/knote_config_misc.desktop
/usr/share/kservices5/knote_config_network.desktop
/usr/share/kservices5/knote_config_print.desktop
/usr/share/kservices5/kontact/knotesplugin.desktop
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
/usr/share/doc/HTML/sv/akonadi_notes_agent/index.cache.bz2
/usr/share/doc/HTML/sv/akonadi_notes_agent/index.docbook
/usr/share/doc/HTML/sv/knotes/index.cache.bz2
/usr/share/doc/HTML/sv/knotes/index.docbook
/usr/share/doc/HTML/uk/akonadi_notes_agent/index.cache.bz2
/usr/share/doc/HTML/uk/akonadi_notes_agent/index.docbook
/usr/share/doc/HTML/uk/knotes/index.cache.bz2
/usr/share/doc/HTML/uk/knotes/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libknotesprivate.so.5
/usr/lib64/libknotesprivate.so.5.12.0
/usr/lib64/libnotesharedprivate.so.5
/usr/lib64/libnotesharedprivate.so.5.12.0
/usr/lib64/qt5/plugins/kcm_knote.so
/usr/lib64/qt5/plugins/kcm_knotessummary.so
/usr/lib64/qt5/plugins/kontact_knotesplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/knotes/COPYING
/usr/share/package-licenses/knotes/COPYING.DOC
/usr/share/package-licenses/knotes/COPYING.LIB
/usr/share/package-licenses/knotes/cmake_modules_COPYING-CMAKE-SCRIPTS

%files locales -f akonadi_notes_agent.lang -f knotes.lang -f libnoteshared.lang
%defattr(-,root,root,-)

