Summary:	Tea timer
Summary(pl):	Herbaciany sekundnik
Name:		teatime
Version:	0.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
You make tea, then you forget about it, so you find it cold after a
hour or so? Tea timer is solution for you.

%description -l pl
Robisz sobie herbatê, po czym o niej zapominasz, znajduj±c j± zimn± za
godzinê? Herbaciany sekundnik jest rozwi±zaniem twoich problemów.

%prep
%setup -q

%build
sh ./autogen.sh
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Office,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install teatime.png $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT/%{_applnkdir}/Office

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_datadir}/%{name}
%{_applnkdir}/Office/*
