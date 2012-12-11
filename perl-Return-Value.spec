%define upstream_name    Return-Value
%define upstream_version 1.666001

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Polymorphic Return Values
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Return/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Polymorphic return values are really useful. Often, we just want to know if
something worked or not. Other times, we'd like to know what the error text
was. Still others, we may want to know what the error code was, and what the
error properties were. We don't want to handle objects or data structures for
every single return value, but we do want to check error conditions in our code
because that's what good programmers do.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Return
%{_mandir}/*/*

%changelog
* Tue Jul 07 2009 Jérôme Quelin <jquelin@mandriva.org> 1.666.1-1mdv2010.0
+ Revision: 393136
- update to 1.666001
- using %%perl_convert_version
- fixed license field

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.30.2-4mdv2009.0
+ Revision: 258327
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.30.2-3mdv2009.0
+ Revision: 246406
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.30.2-1mdv2008.1
+ Revision: 136347
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Jan 20 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.30.2-1mdv2007.0
+ Revision: 111160
- Import perl-Return-Value

* Sat Jan 20 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.30.2-1mdv2007.1
- first mdv release

