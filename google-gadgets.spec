# We actually use libtool to load modules
%define dont_remove_libtool_files 1

# Currently broken
%bcond_with xulrunner

Summary:	Google Gadgets for Linux
Name:		google-gadgets
Version:	0.11.3
Release:	0.1292.1
License:	Apache License
Group:		Toys
# Actually svn rev. 1292 -- the latest released version doesn't build
# with modern compilers
Url:		http://code.google.com/p/google-gadgets-for-linux/
Source0:	http://google-gadgets-for-linux.googlecode.com/files/%{name}-for-linux-%{version}.tar.xz
Patch0:		google-gadgets-for-linux-0.11.2-default-disable-xulrunner.patch
Patch1:		ggadgets-compile.patch
Patch2:		google-gadgets-for-linux-0.12-xulrunner-2.0.patch

BuildRequires:	desktop-file-utils
BuildRequires:	flex
BuildRequires:	zip
BuildRequires:	curl-devel
BuildRequires:	libltdl-devel
BuildRequires:	gtk2-devel
BuildRequires:	qt4-devel
BuildRequires:	dbus-devel
BuildRequires:	startup-notification-devel
%if %{with xulrunner}
Buildrequires:	xulrunner-devel
%endif
BuildRequires:	webkitgtk-devel
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	librsvg-devel
BuildRequires:	libgstreamer0.10-plugins-base-devel

%description
Google Gadgets for Linux provides a platform for running desktop gadgets
under Linux, catering to the unique needs of Linux users. It is compatible
with the gadgets written for Google Desktop for Windows as well as the
Universal Gadgets on iGoogle.

#-----------------------------------------------------------------------

%package common
Summary:	Google Gadgets for Linux - common modules
Group:		Toys
Requires:	curl
Conflicts:	%{name} < 0.10.3-2
Conflicts:	%{name}-tk < 0.10.3-2
Obsoletes:	%{name}-webkit
Obsoletes:	%{name}-xul

%description common
Google Gadgets for Linux provides a platform for running desktop gadgets
under Linux, catering to the unique needs of Linux users. It is compatible
with the gadgets written for Google Desktop for Windows as well as the
Universal Gadgets on iGoogle.

This package contains common modules of Google Gadgets.

%files common -f %{name}.lang
%doc NEWS THANKS README ChangeLog
%{_datadir}/pixmaps/google-gadgets.png
%{_datadir}/mime/packages/00-google-gadgets.xml
%{_iconsdir}/*/*/*/*
%{_datadir}/google-gadgets
%dir %{_libdir}/google-gadgets/modules
%{_libdir}/google-gadgets/modules/analytics-usage-collector.*
%{_libdir}/google-gadgets/modules/curl-xml-http-request.*
%{_libdir}/google-gadgets/modules/dbus-script-class.*
%{_libdir}/google-gadgets/modules/default-framework.*
%{_libdir}/google-gadgets/modules/default-options.*
%{_libdir}/google-gadgets/modules/gst-audio-framework.*
%{_libdir}/google-gadgets/modules/gst-video-element.*
%{_libdir}/google-gadgets/modules/google-gadget-manager.*
%{_libdir}/google-gadgets/modules/html-flash-element.*
%{_libdir}/google-gadgets/modules/libxml2-xml-parser.*
%{_libdir}/google-gadgets/modules/linux-system-framework.*
%{_libdir}/google-gadgets/modules/soup-xml-http-request.*
%{_libdir}/google-gadgets/modules/webkit-script-runtime.*
%if %{with xulrunner}
%{_libdir}/google-gadgets/modules/smjs-script-runtime.*
%endif

#-----------------------------------------------------------------------

%define majorggadget 0
%define libggadget %mklibname ggadget 1.0 %{majorggadget}

%package -n %{libggadget}
Summary:	Google Gadgets for Linux - shared libs
Group:		Toys

%description -n %{libggadget}
This package contains shared library of Google Gadgets.

%files -n %{libggadget}
%{_libdir}/libggadget-1.0.so.%{majorggadget}*

#-----------------------------------------------------------------------

%define majorggadgetdbus 0
%define libggadgetdbus %mklibname ggadget-dbus 1.0 %{majorggadgetdbus}

%package -n %{libggadgetdbus}
Summary:	Google Gadgets for Linux - shared libs
Conflicts:	%{_lib}ggadget1.0_0 < 0.11.0-6
Group:		Toys

%description -n %{libggadgetdbus}
This package contains shared library of Google Gadgets.

%files -n %{libggadgetdbus}
%{_libdir}/libggadget-dbus-1.0.so.%{majorggadgetdbus}*

#-----------------------------------------------------------------------

%define majorggadgetjs 0
%define libggadgetjs %mklibname ggadget-js 1.0 %{majorggadgetjs}

%package -n %{libggadgetjs}
Summary:	Google Gadgets for Linux - shared libs
Conflicts:	%{_lib}ggadget1.0_0 < 0.11.0-6
Group:		Toys

%description -n %{libggadgetjs}
This package contains shared library of Google Gadgets.

%files -n %{libggadgetjs}
%{_libdir}/libggadget-js-1.0.so.%{majorggadgetjs}*

#-----------------------------------------------------------------------

%define majorggadgetxdg 0
%define libggadgetxdg %mklibname ggadget-xdg 1.0 %{majorggadgetxdg}

%package -n %{libggadgetxdg}
Summary:	Google Gadgets for Linux - shared libs
Conflicts:	%{_lib}ggadget1.0_0 < 0.11.0-6
Group:		Toys

%description -n %{libggadgetxdg}
This package contains shared library of Google Gadgets.

%files -n %{libggadgetxdg}
%{_libdir}/libggadget-xdg-1.0.so.%{majorggadgetxdg}*

#-----------------------------------------------------------------------

%define majorggadgetnpapi 0
%define libggadgetnpapi %mklibname ggadget-npapi 1.0 %{majorggadgetnpapi}

%package -n %{libggadgetnpapi}
Summary:	Google Gadgets for Linux - shared libs
Conflicts:	%{_lib}ggadget1.0_0 < 0.11.0-6
Group:		Toys

%description -n %{libggadgetnpapi}
This package contains shared library of Google Gadgets.

%files -n %{libggadgetnpapi}
%{_libdir}/libggadget-npapi-1.0.so.%{majorggadgetnpapi}*

#-----------------------------------------------------------------------

%define majorqt 0
%define libqt %mklibname ggadget-qt 1.0 %{majorqt}

%package -n %{libqt}
Summary:	Google Gadgets for Linux - qt4 libs
Group:		Toys

%description -n %{libqt}
This package contains qt4 library of Google Gadgets.

%files -n %{libqt}
%{_libdir}/libggadget-qt-1.0.so.%{majorqt}*

#-----------------------------------------------------------------------

%package qt
Summary:	Google Gadgets for Linux - qt4 host
Group:		Toys
Provides:	google-gadgets-host = %{version}
Provides:	google-gadgets = %{version}-%{release}
Obsoletes:	google-gadgets < %{version}-%{release}
Requires:	google-gadgets-common = %{version}
Requires:	%{libqt} >= %{version}-%{release}

%description qt
Google Gadgets for Linux provides a platform for running desktop gadgets
under Linux, catering to the unique needs of Linux users. It is compatible
with the gadgets written for Google Desktop for Windows as well as the
Universal Gadgets on iGoogle.

This package contains qt4 host of Google Gadgets.

%post qt
update-alternatives --install %{_bindir}/ggl google-gadgets %{_bindir}/ggl-qt 10

%postun qt
if ! [ -e %{_bindir}/ggl-qt ]; then
  update-alternatives --remove google-gadgets %{_bindir}/ggl-qt
fi

%files qt
%_bindir/ggl-qt
%{_datadir}/applications/ggl-qt.desktop
%{_libdir}/google-gadgets/modules/qt-edit-element.*
%{_libdir}/google-gadgets/modules/qt-system-framework.*
%{_libdir}/google-gadgets/modules/qt-xml-http-request.*
%{_libdir}/google-gadgets/modules/qtwebkit-browser-element.*
%{_libdir}/google-gadgets/modules/qt-script-runtime.*

#-----------------------------------------------------------------------

%define majorgtk 0
%define libgtk %mklibname ggadget-gtk 1.0 %{majorgtk}

%package -n %{libgtk}
Summary:	Google Gadgets for Linux - gtk2 libs
Group:		Toys

%description -n %{libgtk}
This package contains gtk2 library of Google Gadgets.

%files -n %{libgtk}
%{_libdir}/libggadget-gtk-1.0.so.%{majorgtk}*

#-----------------------------------------------------------------------

%package gtk
Summary:	Google Gadgets for Linux - gtk2 host
Group:		Toys
Provides:	google-gadgets-host = %{version}
Provides:	google-gadgets = %{version}-%{release}
Conflicts:      %{name} < 0.10.3-2
Conflicts:	google-gadgets-common < 0.10.3-2
Requires:	google-gadgets-common = %{version}-%{release}
Requires:	%{libgtk} >= %{version}-%{release}
Obsoletes:	google-gadgets < %{version}-%{release}
Obsoletes:	google-gadgets-xul

%description gtk
Google Gadgets for Linux provides a platform for running desktop gadgets
under Linux, catering to the unique needs of Linux users. It is compatible
with the gadgets written for Google Desktop for Windows as well as the
Universal Gadgets on iGoogle.

This package contains gtk2 host of Google Gadgets.

%post gtk
update-alternatives --install %{_bindir}/ggl google-gadgets %{_bindir}/ggl-gtk 10

%postun gtk
if ! [ -e %{_bindir}/ggl-gtk ]; then
  update-alternatives --remove google-gadgets %{_bindir}/ggl-gtk
fi

%files gtk
%{_bindir}/ggl-gtk
%{_datadir}/applications/ggl-gtk.desktop
%{_datadir}/applications/ggl-designer.desktop
%{_libdir}/google-gadgets/modules/gtk-edit-element.*
%{_libdir}/google-gadgets/modules/gtk-flash-element.*
%{_libdir}/google-gadgets/modules/gtk-system-framework.*
%{_libdir}/google-gadgets/modules/gtkwebkit-browser-element.*
%if %{with xulrunner}
%{_libdir}/google-gadgets/gtkmoz-browser-child
%{_libdir}/google-gadgets/modules/gtkmoz-browser-element.*
%endif

#-----------------------------------------------------------------------

%define majorwk 0
%define libwebkitjs %mklibname ggadget-webkitjs 1.0 %{majorwk}

%package -n %{libwebkitjs}
Summary:	Google Gadgets for Linux - shared webkit js libs
Group:		Toys

%description -n %{libwebkitjs}
This package contains shared webkit js library of Google Gadgets.

%files -n %{libwebkitjs}
%{_libdir}/libggadget-webkitjs-1.0.so.%{majorwk}*

#-----------------------------------------------------------------------

%define devname %mklibname %{name} -d

%package -n %{devname}
Summary:	Google Gadgets for Linux - Development files
Group:		Toys
Provides:	%{name}-devel = %{version}
Requires:	%{libggadget} = %{version}
Requires:	%{libggadgetdbus} = %{version}
Requires:	%{libggadgetnpapi} = %{version}
Requires:	%{libggadgetjs} = %{version}
Requires:	%{libggadgetxdg} = %{version}
Requires:	%{libgtk} = %{version}
Requires:	%{libqt} = %{version}
Requires:	%{libwebkitjs} = %{version}

%description -n %{devname}
This package contains developement files of Google Gadgets.

%files -n %{devname}
%{_includedir}/*
%{_libdir}/google-gadgets/include
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

#-----------------------------------------------------------------------

%prep
%setup -qn %{name}-for-linux-%{version}
%patch0 -p0
%patch1 -p1 -b .compile~
%patch2 -p0 -b .xul

libtoolize --force --ltdl
aclocal
autoheader
automake -a
autoconf

%build
# As of 0.11.3-1292, -fpermissive and -fno-strict-aliasing are needed to
# even start getting things to build.
CFLAGS="%{optflags} -fpermissive -fno-strict-aliasing" \
CXXFLAGS="%{optflags} -fpermissive -fno-strict-aliasing" \
%configure2_5x \
	--with-browser-plugins-dir=%{_libdir}/mozilla/plugins/ \
	--disable-static \
%if !%{with xulrunner}
	--disable-gtkmoz-browser-element \
	--disable-smjs-script-runtime \
%endif
	--disable-werror \
	--disable-update-mime-database \
	--disable-update-desktop-database \
	--with-oem-brand="%{product_distribution} %{product_version} for %{product_arch}"

%make

%install
%makeinstall_std

desktop-file-install --vendor='' \
	--dir %{buildroot}%{_datadir}/applications \
	--remove-category='Network' \
	--remove-category='News' \
	--add-category='Utility' \
	--remove-mime-type='app/gg' \
	%{buildroot}%{_datadir}/applications/*.desktop

# Just because we load modules with libtool doesn't mean we have
# to ship .la mess for libraries...
rm -f %{buildroot}%{_libdir}/*.la

%find_lang %{name} || touch %{name}.lang
