Summary:	Tea timer
Summary(pl):	Herbaciany sekundnik
Name:		teatime
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	gtk+-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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

gzip -9nf AUTHORS

cp teatime.png $RPM_BUILD_ROOT%{_pixmapsdir}

cat >$RPM_BUILD_ROOT%{_applnkdir}/Office/teatime.desktop << EOF
[Desktop Entry]
Name=Tea timer
Name[pl]=Herbaciany sekundnik
Comment=Remember about tea!
Comment[pl]=Pamiêtaj o herbacie!
Icon=teatime.png
Exec=teatime
Terminal=0
Type=Application
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_datadir}/%{name}
%{_applnkdir}/Office/*
