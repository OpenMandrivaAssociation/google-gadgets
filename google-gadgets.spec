Summary:	Google Gadgets for Linux
Name:		google-gadgets
Version:	0.9.3
Release:	%mkrel 1
License:	Apache License
Group:		Toys
Source0:	http://google-gadgets-for-linux.googlecode.com/files/%name-for-linux-%version.tar.gz
Patch0:		google-gadgets-0.9.2-add-missing-linking-libs.patch
URL:		http://code.google.com/p/google-gadgets-for-linux/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	libltdl-devel
BuildRequires:	gtk2-devel
BuildRequires:	qt4-devel
%if %mdkversion < 200900
BuildRequires:	QtWebKit-devel
%endif
BuildRequires:	mozilla-firefox-devel
BuildRequires:	librsvg-devel
BuildRequires:	libgstreamer0.10-plugins-base-devel
Requires:	%name-host = %version
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
Google Gadgets for Linux provides a platform for running desktop gadgets
under Linux, catering to the unique needs of Linux users. It is compatible
with the gadgets written for Google Desktop for Windows as well as the
Universal Gadgets on iGoogle.

%files -f %name.lang
%defattr(-,root,root)
%doc NEWS THANKS README ChangeLog
%_datadir/applications/google-gadgets.desktop
%_datadir/google-gadgets
%dir %_libdir/google-gadgets/modules
%_libdir/google-gadgets/modules/curl-xml-http-request.so
%_libdir/google-gadgets/modules/dbus-script-class.so
%_libdir/google-gadgets/modules/default-framework.so
%_libdir/google-gadgets/modules/default-options.so
%_libdir/google-gadgets/modules/google-gadget-manager.so
%_libdir/google-gadgets/modules/libxml2-xml-parser.so
%_libdir/google-gadgets/modules/linux-system-framework.so

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
Provides:	google-gadgets-host = %version

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
%defattr(-,root,root)
%_bindir/ggl-qt
%_libdir/google-gadgets/modules/qt-edit-element.so
%_libdir/google-gadgets/modules/qt-system-framework.so
%_libdir/google-gadgets/modules/qt-xml-http-request.so
%_libdir/google-gadgets/modules/qtwebkit-browser-element.so

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
Provides:	google-gadgets-host = %version

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
%defattr(-,root,root)
%_bindir/ggl-gtk
%_libdir/google-gadgets/gtkmoz-browser-child
%_libdir/google-gadgets/modules/gst-audio-framework.so
%_libdir/google-gadgets/modules/gst-mediaplayer-element.so
%_libdir/google-gadgets/modules/gtk-edit-element.so
%_libdir/google-gadgets/modules/gtk-system-framework.so
%_libdir/google-gadgets/modules/gtkmoz-browser-element.so
%_libdir/google-gadgets/modules/smjs-script-runtime.so

#-----------------------------------------------------------------------
%define develname %mklibname %name -d

%package -n %develname
Summary:	Google Gadgets for Linux - Development files
Group:		Toys
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
%setup -q -n %name-for-linux-%version
%patch0 -p0

%build
sh autotools/bootstrap.sh
%configure2_5x --disable-static --disable-werror
%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %buildroot%_datadir/applications
cat > %buildroot%_datadir/applications/google-gadgets.desktop <<EOF
[Desktop Entry]
Type=Application
Exec=%_bindir/ggl
Name=Google Gadgets
Comment=Google Gadgets for Linux
Icon=toys_section
Categories=Utility;
EOF

%find_lang %name

%clean
rm -rf %{buildroot}
