%define upstream_name	 SVK
%define upstream_version v2.2.3

Name:       svk
Version:    %perl_convert_version %{upstream_version}
Release:    6

Summary:	Decentralized version control system based on Subversion
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://svk.elixus.org/
Source0:    http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		SVK-v2.0.1-fix-SVKMERGE-with-Emacs.patch

BuildRequires:	shared-mime-info
# For apxs2
BuildRequires:	apache-devel
BuildRequires:  perl-devel
BuildRequires:	perl(Algorithm::Annotate)
BuildRequires:	perl(Algorithm::Diff)
BuildRequires:  perl(App::CLI)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:	perl(Class::Autouse)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:	perl(Clone)
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl(Data::Hierarchy)
BuildRequires:	perl-File-BaseDir
BuildRequires:	perl-File-MimeInfo
BuildRequires:	perl-File-Type
BuildRequires:	perl(FreezeThaw)
BuildRequires:  perl(Internals)
BuildRequires:	perl-IO-Digest
BuildRequires:  perl(List::MoreUtils)
BuildRequires:	perl-Locale-Maketext-Lexicon
BuildRequires:	perl-Locale-Maketext-Simple
BuildRequires:	perl-PerlIO-eol
BuildRequires:	perl-PerlIO-via-symlink
BuildRequires:  perl(Path::Class)
BuildRequires:	perl(Pod::Simple)
BuildRequires:	perl(Regexp::Shellish)
BuildRequires:	perl(Sort::Versions)
BuildRequires:	perl-SVN-Mirror >= 0.66
BuildRequires:  perl(SVN::Core)
BuildRequires:	perl(Text::Diff)
BuildRequires:	perl-TimeDate
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(version)
BuildRequires:	perl(YAML)
BuildRequires:  perl(YAML::Syck)

BuildArch:	noarch

Requires:	perl-SVK = %{version}

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
Requires:	perl(Term::ReadKey)
Requires:	perl(Data::Hierarchy)
Requires:	perl-Regexp-Shellish
Requires:	perl-Pod-Simple
Requires:	perl-IO-Digest
Requires:	perl-Clone
Requires:	perl(version)
Requires:	perl-Time-Progress
# not really needed, but I prefer to have more features enabled by defaut
Requires:	perl-File-MimeInfo
Requires:	perl-Locale-Maketext-Simple
# rpm doesn't find and generate this.
Provides:	perl(SVK::Version)

%description -n perl-SVK
This package provides the base modules needed by svk.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1 -b .emacs

%build
perl Makefile.PL --skip INSTALLDIRS=vendor
%make

%check
# should be corrected in new version, thanks for rgs for spotting this
export LC_ALL=C
#APXS=/usr/sbin/apxs prove -b t/*.t

# don't leave non-writable directories
chmod -R +w t

%install
%makeinstall_std

# emacs
install -d %{buildroot}%{_datadir}/emacs/site-lisp
install -m 644 utils/*.el %{buildroot}%{_datadir}/emacs/site-lisp/

%files -n perl-SVK
%doc README CHANGES COMMITTERS CHANGES-1.0
%{perl_vendorlib}/SVK
%{perl_vendorlib}/SVK.pm
%{_mandir}/man3/*

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/emacs/site-lisp/*.el

%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.3-2mdv2011.0
+ Revision: 615051
- the mass rebuild of 2010.1 packages

* Tue Mar 23 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.2.3-1mdv2010.1
+ Revision: 526889
- update to v2.2.3

  + Bruno Cornec <bcornec@mandriva.org>
    - svk now needs perl-Time-Progress

* Tue Sep 15 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.2.1-1mdv2010.0
+ Revision: 443023
- skip tests, very few of them are failing (reported upstream)
- update to 2.2.1

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - keep bash completion in its own package

  + Michael Scherer <misc@mandriva.org>
    - rebuilt against 5.10

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 02 2007 Michael Scherer <misc@mandriva.org> 2.0.2-1mdv2008.0
+ Revision: 58196
- 2.0.2

* Fri Jun 29 2007 Pixel <pixel@mandriva.com> 2.0.1-2mdv2008.0
+ Revision: 45738
- make SVKMERGE=Emacs use emacsclient instead of gnuserv
- package *.el files for emacs

* Sun Apr 22 2007 Michael Scherer <misc@mandriva.org> 2.0.1-1mdv2008.0
+ Revision: 16825
- update to 2.0.1


* Sun Jan 14 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.0-4mdv2007.0
+ Revision: 108798
- real working bash completion update

* Fri Jan 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.0-3mdv2007.1
+ Revision: 108051
- fix bash completion installation
- update bash-completion
- decompress bash-completion file

* Wed Jan 03 2007 Michael Scherer <misc@mandriva.org> 2.0.0-2mdv2007.1
+ Revision: 103900
- add more doc
- add a Requires on perl-version, spotted by guillomovitch

* Wed Jan 03 2007 Michael Scherer <misc@mandriva.org> 2.0.0-1mdv2007.1
+ Revision: 103721
- fix BuildRequires
- version 2.0.0

* Fri Dec 22 2006 Michael Scherer <misc@mandriva.org> 1.99_90-1mdv2007.1
+ Revision: 101422
- update to 2.0 rc1

* Mon Dec 18 2006 Michael Scherer <misc@mandriva.org> 1.99_04-1mdv2007.1
+ Revision: 98386
- add missing BuildRequires
- fix rpmlint warning about bash completion file
- upgrade to 1.99_04
- Import svk

* Fri Jul 21 2006 Michael Scherer <misc@mandriva.org> 1.08-1mdv2007.0
- New version 1.08

* Fri Jul 07 2006 Olivier Blin <oblin@mandriva.com> 1.07-3mdv2007.0
- add explicit perl-Clone requires, since rpm's perl.req skips
  "require" statements that aren't flush against the left edge
  (for svk mkdir)
- buildrequires perl-Clone for tests
- Patch0: add missing "use Clone" in tests

* Fri Apr 28 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.07-2mdk
- Add perl-IO-Digest in dependencies (or else, svk merge crashes)

* Mon Feb 27 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.07-1mdk
- 1.07
- Drop patch 0
- Mark bash-completion file as config

* Wed Feb 01 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.06-2mdk
- Patch 0: silence warnings with perl 5.8.8

* Sun Dec 11 2005 Michael Scherer <misc@mandriva.org> 1.06-1mdk
- New release 1.06

* Sat Nov 26 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-3mdk
- bash-completion 
- spec cleanup
- don't ship empty directories

* Fri Oct 07 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.05-2mdk
- Fix BuildRequires
- %%mkrel

* Fri Oct 07 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.05-1mdk
- 1.05
- Remove libsvn* from BuildRequires due to subversion package reorganisation

* Thu Aug 25 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.04-1mdk
- 1.04

* Sat Aug 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.03-1mdk
- 1.03

* Wed Aug 17 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.02-1mdk
- 1.02
- Fix requires (thanks to David Faure)
- Use prove instead of "make test", because tests are ok but not exit values,
  and "make test" isn't happy with that.

* Wed Jul 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.01-1mdk
- 1.01
- Fix apxs location

* Wed May 11 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.00-1mdk
- 1.00

* Mon May 02 2005 Michael Scherer <misc@mandriva.org> 0.994-1mdk
- New release 0.994

* Wed Apr 27 2005 Michael Scherer <misc@mandriva.org> 0.993-1mdk
- New release 0.993

* Sat Apr 23 2005 Michael Scherer <misc@mandriva.org> 0.992-2mdk
- fix my own bugreport #15295

* Wed Apr 20 2005 Michael Scherer <misc@mandrake.org> 0.992-1mdk
- New release 0.992
- use %%check

* Fri Apr 01 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.991-1mdk
- 0.991

* Tue Mar 15 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.30-2mdk
- Fix automatic dependencies of perl-SVK
- svk now requires perl-SVK of the same version

* Tue Mar 15 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.30-1mdk
- 0.30
- Requires File::Type manually

* Wed Feb 02 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.29-1mdk
- 0.29

* Tue Dec 21 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.27-1mdk
- New release
- Update descriptions
- Turn off the CPAN autoinstaller

* Fri Nov 12 2004 Stefan van der Eijk <stefan@mandrake.org> 0.26-2mdk
- BuildRequires
- Todo: somehow turn off the cpan autoinstaller for missing perl modules

* Fri Nov 12 2004 Michael Scherer <misc@mandrake.org> 0.26-1mdk
- New release 0.26

* Tue Oct 26 2004 Michael Scherer <misc@mandrake.org> 0.25-1mdk
- New release 0.25

* Mon Oct 25 2004 Michael Scherer <misc@mandrake.org> 0.23-1mdk
- New release 0.23

* Wed Oct 06 2004 Michael Scherer <misc@mandrake.org> 0.22-1mdk
- New release 0.22

* Sat Sep 25 2004 Michael Scherer <misc@mandrake.org> 0.21-1mdk
- New release 0.21

* Sun Sep 05 2004 Michael Scherer <misc@mandrake.org> 0.20-1mdk
- New release 0.20

* Wed Sep 01 2004 Michael Scherer <misc@mandrake.org> 0.19-2mdk 
- BuildRequires

* Tue Aug 24 2004 Michael Scherer <misc@mandrake.org> 0.19-1mdk
- New release 0.19

* Mon Aug 09 2004 Stefan van der Eijk <stefan@eijk.nu> 0.18-3mdk
- still some more BuildRequires

* Sun Aug 08 2004 Stefan van der Eijk <stefan@eijk.nu> 0.18-2mdk
- BuildRequires to avoid endless looping

* Fri Aug 06 2004 Michael Scherer <misc@mandrake.org> 0.18-1mdk
- New release 0.18
- add missing BuildRequires

* Mon Jul 26 2004 Michael Scherer <misc@mandrake.org> 0.17-2mdk 
- add a missing Requires

* Mon Jul 19 2004 Michael Scherer <misc@mandrake.org> 0.17-1mdk
- New release 0.17

* Thu Jul 01 2004 Michael Scherer <misc@mandrake.org> 0.16-1mdk
- New release 0.16
- reenable rpmbuildupdate

* Sat Jun 19 2004 Michael Scherer <misc@mandrake.org> 0.15-1mdk
- New release 0.15

* Thu Apr 29 2004 Michael Scherer <misc@mandrake.org> 0.14-1mdk 
- 0.14

* Mon Apr 12 2004 Michael Scherer <misc@mandrake.org> 0.13-1mdk
- New release 0.13
- enable test

* Sat Apr 03 2004 Michael Scherer <misc@mandrake.org> 0.12-1mdk 
- first Mandrakelinux package

