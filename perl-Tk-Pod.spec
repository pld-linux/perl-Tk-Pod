#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires working $DISPLAY)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Tk
%define		pnam	Pod
Summary:	Tk::Pod - Pod browser toplevel widget
Summary(pl.UTF-8):	Tk::Pod - widget do przeglądania Pod
Name:		perl-Tk-Pod
Version:	0.9932
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c2e9056a471834c55011e0ed3982626c
BuildRequires:	perl-Pod-Simple
BuildRequires:	perl-Tk
BuildRequires:	perl-Tk-HistEntry
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perlindex
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tk::Pod Perl module is a simple Pod browser with hypertext
capabilities in a "Toplevel" widget.

%description -l pl.UTF-8
Moduł Perla Tk::Pod jest prostą przeglądarką Pod z obsługą
hypertekstu, działającą jako widget "Toplevel".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/tk*
%{perl_vendorlib}/%{pdir}/*
%{_mandir}/man[13]/*
