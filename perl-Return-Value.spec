%define module      Return-Value
%define name        perl-%{module}
%define version     1.30.2
%define up_version  1.302
%define release     %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Polymorphic Return Values
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Return/%{module}-%{up_version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Polymorphic return values are really useful. Often, we just want to know if
something worked or not. Other times, we'd like to know what the error text
was. Still others, we may want to know what the error code was, and what the
error properties were. We don't want to handle objects or data structures for
every single return value, but we do want to check error conditions in our code
because that's what good programmers do.

%prep
%setup -q -n %{module}-%{up_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Return
%{_mandir}/*/*


