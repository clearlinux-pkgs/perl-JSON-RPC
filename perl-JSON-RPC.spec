#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-JSON-RPC
Version  : 1.06
Release  : 16
URL      : https://cpan.metacpan.org/authors/id/D/DM/DMAKI/JSON-RPC-1.06.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DM/DMAKI/JSON-RPC-1.06.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libj/libjson-rpc-perl/libjson-rpc-perl_1.06-2.debian.tar.xz
Summary  : 'JSON RPC 2.0 Server Implementation'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-JSON-RPC-license = %{version}-%{release}
Requires: perl-JSON-RPC-perl = %{version}-%{release}
Requires: perl(Apache2::Const)
Requires: perl(Plack::Request)
BuildRequires : buildreq-cpan

%description
# NAME
JSON::RPC - JSON RPC 2.0 Server Implementation
# SYNOPSIS
# app.psgi
use strict;
use JSON::RPC::Dispatch;

%package dev
Summary: dev components for the perl-JSON-RPC package.
Group: Development
Provides: perl-JSON-RPC-devel = %{version}-%{release}
Requires: perl-JSON-RPC = %{version}-%{release}

%description dev
dev components for the perl-JSON-RPC package.


%package license
Summary: license components for the perl-JSON-RPC package.
Group: Default

%description license
license components for the perl-JSON-RPC package.


%package perl
Summary: perl components for the perl-JSON-RPC package.
Group: Default
Requires: perl-JSON-RPC = %{version}-%{release}

%description perl
perl components for the perl-JSON-RPC package.


%prep
%setup -q -n JSON-RPC-1.06
cd %{_builddir}
tar xf %{_sourcedir}/libjson-rpc-perl_1.06-2.debian.tar.xz
cd %{_builddir}/JSON-RPC-1.06
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/JSON-RPC-1.06/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-JSON-RPC
cp %{_builddir}/JSON-RPC-1.06/LICENSE %{buildroot}/usr/share/package-licenses/perl-JSON-RPC/b521ffb0d39409ed04226ace1a30c1835e04ba62
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-JSON-RPC/20c6cfc967977049efff30eec694ce3d5a2fe8b2
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/JSON::RPC.3
/usr/share/man/man3/JSON::RPC::Constants.3
/usr/share/man/man3/JSON::RPC::Dispatch.3
/usr/share/man/man3/JSON::RPC::Legacy.3
/usr/share/man/man3/JSON::RPC::Legacy::Client.3
/usr/share/man/man3/JSON::RPC::Legacy::Procedure.3
/usr/share/man/man3/JSON::RPC::Legacy::Server.3
/usr/share/man/man3/JSON::RPC::Legacy::Server::Apache2.3
/usr/share/man/man3/JSON::RPC::Legacy::Server::CGI.3
/usr/share/man/man3/JSON::RPC::Legacy::Server::Daemon.3
/usr/share/man/man3/JSON::RPC::Parser.3
/usr/share/man/man3/JSON::RPC::Procedure.3
/usr/share/man/man3/JSON::RPC::Test.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-JSON-RPC/20c6cfc967977049efff30eec694ce3d5a2fe8b2
/usr/share/package-licenses/perl-JSON-RPC/b521ffb0d39409ed04226ace1a30c1835e04ba62

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/JSON/RPC.pm
/usr/lib/perl5/vendor_perl/5.34.0/JSON/RPC/Constants.pm
/usr/lib/perl5/vendor_perl/5.34.0/JSON/RPC/Dispatch.pm
/usr/lib/perl5/vendor_perl/5.34.0/JSON/RPC/Legacy.pm
/usr/lib/perl5/vendor_perl/5.34.0/JSON/RPC/Legacy/Client.pm
/usr/lib/perl5/vendor_perl/5.34.0/JSON/RPC/Legacy/Procedure.pm
/usr/lib/perl5/vendor_perl/5.34.0/JSON/RPC/Legacy/Server.pm
/usr/lib/perl5/vendor_perl/5.34.0/JSON/RPC/Legacy/Server/Apache2.pm
/usr/lib/perl5/vendor_perl/5.34.0/JSON/RPC/Legacy/Server/CGI.pm
/usr/lib/perl5/vendor_perl/5.34.0/JSON/RPC/Legacy/Server/Daemon.pm
/usr/lib/perl5/vendor_perl/5.34.0/JSON/RPC/Parser.pm
/usr/lib/perl5/vendor_perl/5.34.0/JSON/RPC/Procedure.pm
/usr/lib/perl5/vendor_perl/5.34.0/JSON/RPC/Test.pm
