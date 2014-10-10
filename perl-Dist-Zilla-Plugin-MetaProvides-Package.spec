%define upstream_name    Dist-Zilla-Plugin-MetaProvides-Package
%define upstream_version 2.000001

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Extract namespaces/version from traditional packages for provides

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla::App::Tester)
BuildRequires:	perl(Dist::Zilla::MetaProvides::ProvideRecord)
BuildRequires:	perl(Dist::Zilla::Plugin::MetaProvides)
BuildRequires:	perl(Dist::Zilla::Role::MetaProvider::Provider)
BuildRequires:	perl(Dist::Zilla::Util::Test::KENTNL)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Module::Extract::Namespaces)
BuildRequires:	perl(Module::Extract::VERSION)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Autobox)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More) >= 0.960
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(Throwable)
BuildArch:	noarch

%description
Extract namespaces/version from traditional packages for provides.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.json META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*


