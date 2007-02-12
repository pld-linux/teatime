Summary:	Tea timer
Summary(pl.UTF-8):   Herbaciany sekundnik
Name:		teatime
Version:	0.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	3e9e4da2a764df34ebe49fae1bfc63e3
Source1:	%{name}.desktop
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
You make tea, then you forget about it, so you find it cold after a
hour or so? Tea timer is solution for you.

%description -l pl.UTF-8
Robisz sobie herbatę, po czym o niej zapominasz, znajdując ją zimną za
godzinę? Herbaciany sekundnik jest rozwiązaniem twoich problemów.

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
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Office

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_datadir}/%{name}
%{_applnkdir}/Office/*
