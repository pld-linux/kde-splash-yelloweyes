%define		_splash		yelloweyes

Summary:	KDE splash screen
Summary(pl):	Ekran startowy KDE
Name:		kde-splash-%{_splash}
Version:	2.0
Release:	1
License:	Creative Commons Attribution ShareAlike 1.0
Group:		X11/Amusements
Source0:	http://www.kde-look.org/content/files/43923-yelloweyes.tar.gz
# Source0-md5:	304068b1c07dcda0ba1c16038140783e
URL:		http://www.kde-look.org/content/show.php?content=43923
Requires:	kde-splash-moodin
Requires:	kdebase-desktop >= 9:3.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A KDE splash screen featuring a kitty with yellow eyes.

%description -l pl
Ekran startowy KDE z kotem o ¿ó³tych oczach.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}
install %{_splash}/* $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_datadir}/apps/ksplash/Themes/%{_splash}
