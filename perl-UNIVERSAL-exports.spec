%define module	UNIVERSAL-exports
%define name	perl-%{module}
%define version	0.05
%define release	%mkrel 3

%define _provides_exceptions perl(UNIVERSAL)


Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Lightweight, universal exporting of variables
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		http://www.cpan.org/modules/by-module/UNIVERSAL/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:  perl(Exporter::Lite)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This is an alternative to Exporter intended to provide a universal, lightweight
subset of its functionality.

%prep
%setup -q -n %{module}-%{version}

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


