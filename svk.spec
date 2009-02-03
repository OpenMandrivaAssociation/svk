%define realname	SVK
%define name		svk
%define version		2.0.2
%define release		%mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Decentralized version control system based on Subversion
Source0:        http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/%{realname}-v%{version}.tar.bz2
Patch0:		SVK-v2.0.1-fix-SVKMERGE-with-Emacs.patch
Url:		http://svk.elixus.org/
Requires:	perl-SVK = %{version}
BuildRequires:	perl-Algorithm-Annotate
BuildRequires:	perl-Algorithm-Diff
BuildRequires:	perl-Class-Autouse
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-File-BaseDir
BuildRequires:	perl-Data-Hierarchy
BuildRequires:	perl-File-MimeInfo
BuildRequires:	perl-File-Type
BuildRequires:	perl-FreezeThaw
BuildRequires:	perl-IO-Digest
BuildRequires:	perl-Locale-Maketext-Lexicon
BuildRequires:	perl-Locale-Maketext-Simple
BuildRequires:	perl-PerlIO-eol
BuildRequires:	perl-PerlIO-via-symlink
BuildRequires:	perl-Pod-Simple
BuildRequires:	perl-Regexp-Shellish
BuildRequires:	perl-Sort-Versions
BuildRequires:	perl-SVN-Mirror >= 0.66
BuildRequires:	perl-Text-Diff
BuildRequires:	perl-TimeDate
BuildRequires:	perl-YAML
BuildRequires:	perl-Clone
BuildRequires:	shared-mime-info
BuildRequires:  perl-devel
BuildRequires:  perl(YAML::Syck)
BuildRequires:  perl(App::CLI)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(Internals)
BuildRequires:  perl-version
# For apxs2
BuildRequires:	apache-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
svk is a decentralized version control system written in Perl.
It uses the subversion filesystem but provides some other powerful features.

It allows you to work in a disconnected fashion with the possibility to merge
back your changes to the main repository.

%package -n perl-SVK
Summary:	Perl modules used by SVK
Group:		Development/Perl
# for some strange reason, not detected by our scripts
Requires:	perl-SVN-Mirror >= 0.66
Requires:	perl-File-Type
Requires:	perl-Class-Autouse
Requires:	perl-Term-ReadKey
Requires:	perl-Data-Hierarchy
Requires:	perl-Regexp-Shellish
Requires:	perl-Pod-Simple
Requires:	perl-IO-Digest
Requires:	perl-Clone
Requires:	perl-version
# not really needed, but I prefer to have more features enabled by defaut
Requires:	perl-File-MimeInfo
Requires:	perl-Locale-Maketext-Simple
# rpm doesn't find and generate this.
Provides:	perl(SVK::Version)

%description -n perl-SVK
This package provides the base modules needed by svk.

%prep
%setup -q -n %{realname}-v%{version}
%patch0 -p1 -b .emacs

%build
%{__perl} Makefile.PL --skip INSTALLDIRS=vendor
%make

%check
# should be corrected in new version, thanks for rgs for spotting this
export LC_ALL=C
APXS=/usr/sbin/apxs prove -b t/*.t

# don't leave non-writable directories
chmod -R +w t

%install
rm -rf %{buildroot}
%makeinstall_std

# emacs
install -d %{buildroot}%{_datadir}/emacs/site-lisp
install -m 644 utils/*.el %{buildroot}%{_datadir}/emacs/site-lisp/


%clean
rm -rf %{buildroot}

%files -n perl-SVK
%defattr(-,root,root)
%doc README CHANGES COMMITTERS CHANGES-1.0
%{perl_vendorlib}/SVK
%{perl_vendorlib}/SVK.pm
%{_mandir}/man3/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/emacs/site-lisp/*.el
