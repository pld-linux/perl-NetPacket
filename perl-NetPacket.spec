%define		pdir	NetPacket
Summary:	NetPacket - modules to assemble/disassemble network packets of various Internet protocols
Summary(pl.UTF-8):	NetPacket - moduły składania/rozkładania pakietów różnych protokołów internetowych
Name:		perl-NetPacket
Version:	1.6.0
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	17ba0407dada096f046f513387e88818
Patch0:		%{name}-ethernet.patch
URL:		http://search.cpan.org/dist/NetPacket/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"NetPacket" provides a base class for a cluster of modules related to
decoding and encoding of network protocols. Each "NetPacket"
descendent module knows how to encode and decode packets for the
network protocol it implements. At present, decoding/encoding for the
following protocols has been implemented: Ethernet (802.3 and 802.2),
ARP, ICMP, IGMP, IP, UDP, TCP, LLC, Spanning Tree (802.1D and 802.1w)
and LACP (not complete yet).

%description -l pl.UTF-8
"NetPacket" stanowi klasę bazową dla zbioru modułów służących do
rozkodowywania i kodowania protokołów sieciowych. Każdy z tych modułów
umie rozkodować i zakodować implementowany przez siebie protokół
sieciowy. Aktualnie zaimplementowane jest rozkodowywanie/kodowanie
następujących protokołów: Ethernet (802.3 i 802.2), ARP, ICMP, IGMP,
IP, UDP, TCP, LLC, Spanning Tree (802.1D and 802.1w) i LACP (jeszcze
nie dokończone).

%prep
%setup -q -n %{pdir}-%{version}
%patch0 -p1

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
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/%{pdir}
%{_mandir}/man3/*
