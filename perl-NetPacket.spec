%include	/usr/lib/rpm/macros.perl
%define         pnam NetPacket

Summary:	NetPacket do disassembly of network packets of various Internet protocols
Summary(pl):	Modu³ NetPacket do rozk³adania pakietów ró¿nych protoko³ów internetowych
Name:		perl-%{pnam}
Version:	0.04
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pnam}/%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The NetPacket module do disassembly of network packets of various
Internet protocols. At present, decoding for the following protocols
has been implemented: Ethernet (802.3 and 802.2), ARP, ICMP, IGMP, IP,
UDP and TCP.

%description -l pl
Modu³ NetPacket rozk³ada pakiety sieciowe ró¿nych internetowych
protoko³ów. Aktualnie ma zaimplementowane dekodowanie nastêpuj±cych
protoko³ów: Ethernet (802.3 i 802.2), ARP, ICMP, IGMP, IP, UDP i TCP.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name .packlist | xargs -r rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/%{pnam}.pm
%{perl_vendorlib}/%{pnam}
%{_mandir}/man3/*
