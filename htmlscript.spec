%bcond_with qt5

Name:		htmlscript
Version:	1.2.0
Release:	1
Summary:	Tool for displaying HTML generated by scripts
License:	GPLv3
Group:		System/Configuration/Other
URL:		https://github.com/OpenMandrivaSoftware/htmlscript
Source0:	https://github.com/OpenMandrivaSoftware/htmlscript/archive/%{version}.tar.gz
%if %{with qt5}
BuildRequires:	qmake5
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5WebEngineWidgets)
%else
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:	cmake(Qt6WebEngineWidgets)
%endif
BuildSystem:	cmake
%if %{with qt5}
BuildOption:	-DQT_VERSION:STRING="5"
%endif

%description
A tool for displaying HTML generated by scripts.

It is used by om-welcome and om-control-center.

%files
%doc LICENSE
%{_bindir}/htmlscript
%{_bindir}/enable-repo
%{_bindir}/disable-repo
%{_datadir}/htmlscript
