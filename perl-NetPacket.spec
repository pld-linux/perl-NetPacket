%include	/usr/lib/rpm/macros.perl
%define         pnam NetPacket

Summary:	NetPacket do disassembly of network packets of various Internet protocols
Name:		perl-%{pnam}
Version:	0.03
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/authors/id/T/TI/TIMPOTTER/%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The NetPacket module do disassembly of network packets of various Internet
protocols. At present, decoding for the following protocols has been 
implemented: Ethernet (802.3 and 802.2), ARP, ICMP, IGMP, IP, UDP and TCP.

%prep
%setup -q -n %{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
gzip -9nf README 
find $RPM_BUILD_ROOT -name .packlist | xargs -r rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pnam}.pm
%{perl_sitelib}/%{pnam}
%{_mandir}/man3/*
%doc *.gz
