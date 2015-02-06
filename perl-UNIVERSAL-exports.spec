%define upstream_name	 UNIVERSAL-exports
%define upstream_version 0.05

%if %{_use_internal_dependency_generator}
%define __noautoprov 'perl\\(UNIVERSAL\\)'
%else
%define _provides_exceptions perl(UNIVERSAL)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Lightweight, universal exporting of variables
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/UNIVERSAL/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Exporter::Lite)
BuildArch:	noarch

%description
This is an alternative to Exporter intended to provide a universal, lightweight
subset of its functionality.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/UNIVERSAL
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 401991
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.05-4mdv2009.0
+ Revision: 258710
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.05-3mdv2009.0
+ Revision: 246672
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.05-1mdv2008.1
+ Revision: 136364
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Dec 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2007.0
+ Revision: 97351
- new version
- Import perl-UNIVERSAL-exports

* Tue May 16 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.03-6mdk
- Don't provide perl(UNIVERSAL)

* Sat Apr 29 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.03-5mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL

* Thu Dec 22 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.03-4mdk
- Fix BuildRequires

* Mon Nov 21 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.03-3mdk
- Remove UNIVERSAL::require from this package, it's now in a separate CPAN
  distribution
- Change summary
- add make test

* Thu Oct 27 2005 Lenny Cartier <lenny@mandriva.com> 0.03-2mdk
- rebuild

* Tue Nov 16 2004 Oden Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.03-1mdk
- initial contrib.

