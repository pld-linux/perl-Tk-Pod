#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires working $DISPLAY)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Tk
%define		pnam	Pod
Summary:	Tk::Pod - Pod browser toplevel widget
Summary(pl):	Tk::Pod - widget do przegl�dania Pod
Name:		perl-Tk-Pod
Version:	0.9929
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4f39a0868d40ca3aaf9fd52d5cfc61ed
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

%description -l pl
Modu� Perla Tk::Pod jest prost� przegl�dark� Pod z obs�ug�
hypertekstu, dzia�aj�c� jako widget "Toplevel".

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
