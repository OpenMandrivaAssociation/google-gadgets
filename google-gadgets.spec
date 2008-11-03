%define build_oem 1

%define svnrel 941

Summary:	Google Gadgets for Linux
Name:		google-gadgets
Version:	0.10.3
Release:	%mkrel -c svn%svnrel 1
License:	Apache License
Group:		Toys
#Source0:	http://google-gadgets-for-linux.googlecode.com/files/%name-for-linux-%version.tar.bz2
Source0:	http://google-gadgets-for-linux.googlecode.com/files/%name-for-linux-r%svnrel.tar.bz2
Patch0:		google-gadgets-for-linux-0.10.3-fix-linkage.patch
URL:		http://code.google.com/p/google-gadgets-for-linux/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	libltdl-devel
BuildRequires:	gtk2-devel
BuildRequires:	qt4-devel
BuildRequires:	desktop-file-utils
BuildRequires:	zip
BuildRequires:	dbus-devel
BuildRequires:	startup-notification-devel
%if %mdkversion < 200900
BuildRequires:	QtWebKit-devel
BuildRequires:	mozilla-firefox-devel
%else
BuildRequires:	xulrunner-devel-unstable
%endif
BuildRequires:	librsvg-devel
BuildRequires:	flex
BuildRequires:	libgstreamer0.10-plugins-base-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
Google Gadgets for Linux provides a platform for running desktop gadgets
under Linux, catering to the unique needs of Linux users. It is compatible
with the gadgets written for Google Desktop for Windows as well as the
Universal Gadgets on iGoogle.

#-----------------------------------------------------------------------
%package common
Summary:        Google Gadgets for Linux - common modules
Group:          Toys
Requires:	curl
Conflicts:	%name < 0.10.3-0.svn929.5
Conflicts:	%name-gtk < 0.10.3-0.svn929.5

%description common
Google Gadgets for Linux provides a platform for running desktop gadgets
under Linux, catering to the unique needs of Linux users. It is compatible
with the gadgets written for Google Desktop for Windows as well as the
Universal Gadgets on iGoogle.

This package contains common modules of Google Gadgets.

%files common -f %name.lang
%defattr(-,root,root)
%doc NEWS THANKS README ChangeLog
%_datadir/pixmaps/google-gadgets.png
%_datadir/mime/packages/00-google-gadgets.xml
%_iconsdir/*/*/*/*
%_datadir/google-gadgets
%dir %_libdir/google-gadgets/modules
%_libdir/google-gadgets/modules/analytics-usage-collector.so
%_libdir/google-gadgets/modules/curl-xml-http-request.so
%_libdir/google-gadgets/modules/dbus-script-class.so
%_libdir/google-gadgets/modules/default-framework.so
%_libdir/google-gadgets/modules/default-options.so
%_libdir/google-gadgets/modules/gtk-flash-element.so
%_libdir/google-gadgets/modules/gst-audio-framework.so
%_libdir/google-gadgets/modules/gst-video-element.so
%_libdir/google-gadgets/modules/google-gadget-manager.so
%_libdir/google-gadgets/modules/libxml2-xml-parser.so
%_libdir/google-gadgets/modules/linux-system-framework.so

%if %mdkversion < 200900
%post common
%update_mime_database

%postun common
%clean_mime_database
%endif

#-----------------------------------------------------------------------
%define libname %mklibname ggadget 1.0 0

%package -n %libname
Summary:	Google Gadgets for Linux - shared libs
Group:		Toys

%description -n %libname
This package contains shared library of Google Gadgets.

%files -n %libname
%defattr(-,root,root)
%_libdir/libggadget-1.0.so.0*
%_libdir/libggadget-dbus-1.0.so.0*
%_libdir/libggadget-js-1.0.so.0*
%_libdir/libggadget-xdg-1.0.so.0*
%_libdir/libggadget-npapi-1.0.so.0*

#-----------------------------------------------------------------------
%define libqt %mklibname ggadget-qt 1.0 0

%package -n %libqt
Summary:	Google Gadgets for Linux - qt4 libs
Group:		Toys

%description -n %libqt
This package contains qt4 library of Google Gadgets.

%files -n %libqt
%defattr(-,root,root)
%_libdir/libggadget-qt-1.0.so.0*

#-----------------------------------------------------------------------
%package qt
Summary:	Google Gadgets for Linux - qt4 host
Group:		Toys
Provides:	google-gadgets = %version-%release
Obsoletes:	google-gadgets < 0.10.3-0.svn929.3
Requires:	google-gadgets-common = %version

%description qt
Google Gadgets for Linux provides a platform for running desktop gadgets
under Linux, catering to the unique needs of Linux users. It is compatible
with the gadgets written for Google Desktop for Windows as well as the
Universal Gadgets on iGoogle.

This package contains qt4 host of Google Gadgets.

%post qt
update-alternatives --install %{_bindir}/ggl google-gadgets %{_bindir}/ggl-qt 10
%if %mdkversion < 200900
%update_menus
%update_desktop_database
%endif

%postun qt
if ! [ -e %{_bindir}/ggl-qt ]; then
  update-alternatives --remove google-gadgets %{_bindir}/ggl-qt
fi
%if %mdkversion < 200900
%clean_menus
%clean_desktop_database
%endif

%files qt
%defattr(-,root,root)
%_bindir/ggl-qt
%_datadir/applications/ggl-qt.desktop
%_libdir/google-gadgets/modules/qt-edit-element.so
%_libdir/google-gadgets/modules/qt-system-framework.so
%_libdir/google-gadgets/modules/qt-xml-http-request.so
%_libdir/google-gadgets/modules/qtwebkit-browser-element.so
%if %mdkversion >= 200900
%_libdir/google-gadgets/modules/qt-script-runtime.so
%endif

#-----------------------------------------------------------------------
%define libgtk %mklibname ggadget-gtk 1.0 0

%package -n %libgtk
Summary:	Google Gadgets for Linux - gtk2 libs
Group:		Toys

%description -n %libgtk
This package contains gtk2 library of Google Gadgets.

%files -n %libgtk
%defattr(-,root,root)
%_libdir/libggadget-gtk-1.0.so.0*

#-----------------------------------------------------------------------
%package gtk
Summary:	Google Gadgets for Linux - gtk2 host
Group:		Toys
Provides:	google-gadgets = %version-%release
Obsoletes:	google-gadgets < 0.10.3-0.svn929.3
Conflicts:      %name < 0.10.0
Requires:	google-gadgets-common = %version-%release
Conflicts:	google-gadgets-common < 0.10.3-0.svn929.5

%description gtk
Google Gadgets for Linux provides a platform for running desktop gadgets
under Linux, catering to the unique needs of Linux users. It is compatible
with the gadgets written for Google Desktop for Windows as well as the
Universal Gadgets on iGoogle.

This package contains gtk2 host of Google Gadgets.

%post gtk
update-alternatives --install %{_bindir}/ggl google-gadgets %{_bindir}/ggl-gtk 10
%if %mdkversion < 200900
%update_menus
%update_desktop_database
%endif

%postun gtk
if ! [ -e %{_bindir}/ggl-gtk ]; then
  update-alternatives --remove google-gadgets %{_bindir}/ggl-gtk
fi
%if %mdkversion < 200900
%clean_menus
%clean_desktop_database
%endif

%files gtk
%defattr(-,root,root)
%_bindir/ggl-gtk
%_datadir/applications/ggl-gtk.desktop
%_libdir/google-gadgets/gtkmoz-browser-child
%_libdir/google-gadgets/modules/gtk-edit-element.so
%_libdir/google-gadgets/modules/gtk-system-framework.so
%_libdir/google-gadgets/modules/gtkmoz-browser-element.so
%_libdir/google-gadgets/modules/smjs-script-runtime.so

#-----------------------------------------------------------------------
%define develname %mklibname %name -d

%package -n %develname
Summary:	Google Gadgets for Linux - Development files
Group:		Toys
Provides:   %name-devel = %version
Requires:	%libname = %version
Requires:	%libgtk = %version
Requires:	%libqt = %version

%description -n %develname
This package contains developement files of Google Gadgets.

%files -n %develname
%defattr(-,root,root)
%_includedir/*
%_libdir/google-gadgets/include
%_libdir/google-gadgets/modules/*.la
%_libdir/*.la
%_libdir/*.so
%_libdir/pkgconfig/*.pc

#-----------------------------------------------------------------------

%prep
#setup -q -n %name-for-linux-%version
%setup -q -n %name
%patch0 -p0

%build
sh autotools/bootstrap.sh
%configure2_5x --disable-static --disable-werror --disable-update-mime-database --disable-update-desktop-database \
%if %build_oem
	--with-oem-brand="%{product_distribution} %{product_version} for %{product_arch}"
%endif

%make

%install
rm -rf %{buildroot}
%makeinstall_std

desktop-file-install --vendor='' \
	--dir %buildroot%_datadir/applications \
	--remove-category='Network' \
	%buildroot%_datadir/applications/*.desktop

%find_lang %name

%clean
rm -rf %{buildroot}
