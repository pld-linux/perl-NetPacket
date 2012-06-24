%include	/usr/lib/rpm/macros.perl
%define	pdir	NetPacket
%define	pnam	NetPacket
Summary:	NetPacket - modules to assemble/disassemble network packets of various Internet protocols
Summary(pl):	NetPacket - modu�y sk�adania/rozk�adania pakiet�w r�nych protoko��w internetowych
Name:		perl-%{pnam}
Version:	0.04
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	3bf136cd3b555d50ba4b1ce81968f695
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"NetPacket" provides a base class for a cluster of modules related to
decoding and encoding of network protocols.  Each "NetPacket"
descendent module knows how to encode and decode packets for the
network protocol it implements.  At present, decoding/encoding for the
following protocols has been implemented: Ethernet (802.3 and 802.2),
ARP, ICMP, IGMP, IP, UDP, TCP, LLC, Spanning Tree (802.1D and 802.1w)
and LACP (not complete yet).

%description -l pl
"NetPacket" stanowi klas� bazow� dla zbioru modu��w s�u��cych do
rozkodowywania i kodowania protoko��w sieciowych. Ka�dy z tych modu��w
umie rozkodowa� i zakodowa� implementowany przez siebie protok�
sieciowy. Aktualnie zaimplementowane jest rozkodowywanie/kodowanie
nast�puj�cych protoko��w: Ethernet (802.3 i 802.2), ARP, ICMP, IGMP,
IP, UDP, TCP, LLC, Spanning Tree (802.1D and 802.1w) i LACP (jeszcze
nie doko�czone).

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name .packlist | xargs -r rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/%{pnam}.pm
%{perl_vendorlib}/%{pnam}
%{_mandir}/man3/*
