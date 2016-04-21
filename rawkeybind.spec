Summary:	Workaround for X11 limitation with 255 keycodes
Summary(pl.UTF-8):	Obejście dla ograniczenia 255 kodów klawiszowych dla X11
Name:		rawkeybind
Version:	0.1
Release:	0.1
License:	GPL v2+
Group:		X11/Tools
Source0:	http://www.isaev.ru/rawkeybind/%{name}-%{version}.tgz
# Source0-md5:	fa3b869edab5efe8d78c236b97d79a6d
URL:		http://www.isaev.ru/rawkeybind/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program is a workaround for X11 limitation with 255 keycodes.

WARNING: the binary is SUID root!

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(4755,root,root) %{_bindir}/%{name}
%attr(644,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%{_mandir}/man1/*.1*
