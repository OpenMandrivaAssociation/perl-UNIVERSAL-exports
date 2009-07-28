%define upstream_name	 UNIVERSAL-exports
%define upstream_version 0.05

%define _provides_exceptions perl(UNIVERSAL)

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Lightweight, universal exporting of variables
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/UNIVERSAL/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl(Exporter::Lite)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This is an alternative to Exporter intended to provide a universal, lightweight
subset of its functionality.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/UNIVERSAL
%{_mandir}/man3/*
