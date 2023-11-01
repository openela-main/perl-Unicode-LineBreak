# Run optional test
%bcond_without perl_Unicode_LineBreak_enables_optional_test

Name:           perl-Unicode-LineBreak
Version:        2017.004
Release:        6%{?dist}
Summary:        UAX #14 Unicode Line Breaking Algorithm
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Unicode-LineBreak/
Source0:        http://search.cpan.org/CPAN/authors/id/N/NE/NEZUMI/Unicode-LineBreak-%{version}.tar.gz

BuildRequires:  libthai-devel
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  pkgconfig
BuildRequires:  sed
BuildRequires:  sombok-devel
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode) >= 1.98
BuildRequires:  perl(Exporter)
BuildRequires:  perl(MIME::Charset) >= 1.006.2
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(Test::More) >= 0.45
%if %{with perl_Unicode_LineBreak_enables_optional_test}
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.00
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Encode) >= 1.98
Requires:       perl(MIME::Charset) >= 1.006.2


%if 0%{?rhel} == 6
%filter_from_provides /^perl(Unicode::LineBreak)$/d
%filter_from_requires /^perl(Unicode::LineBreak::Constants)$/d
%{?perl_default_filter}
%endif

%if 0%{?fedora} > 14 || 0%{?rhel} > 6
%{?filter_setup:
%filter_from_requires /perl(Unicode::LineBreak::Constants)/d
%filter_from_provides /^perl(Unicode::LineBreak)$/d
}
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Unicode::LineBreak::Constants\\)
%global __requires_exclude %__requires_exclude|^perl\\(constant\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Encode\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(MIME::Charset\\)\s*$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Unicode::LineBreak\\)$
%endif


%description
Unicode::LineBreak performs Line Breaking Algorithm described in Unicode
Standards Annex #14 [UAX #14]. East_Asian_Width informative properties
defined by Annex #11 [UAX #11] will be concerned to determine breaking
positions.


%prep
%setup -q -n Unicode-LineBreak-%{version}
# Remove bundled library
rm -rf sombok
sed -i -e '/^sombok/d' MANIFEST


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}


%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

mkdir -p $RPM_BUILD_ROOT%{_mandir}/ja/man3
for mod in Text::LineFold Unicode::GCString Unicode::LineBreak; do
  mv $RPM_BUILD_ROOT%{_mandir}/man3/POD2::JA::$mod.3pm \
     $RPM_BUILD_ROOT%{_mandir}/ja/man3/$mod.3pm
done

%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%doc Changes Changes.REL1 README Todo.REL1
%license ARTISTIC GPL
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Unicode*
%{perl_vendorarch}/Text
%{perl_vendorarch}/POD2
%{_mandir}/man3/*
%{_mandir}/ja/man3/*


%changelog
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.004-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.004-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 2017.004-3
- Rebuild due to bug in RPM (RHBZ #1468476)

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2017.004-2
- Perl 5.26 rebuild

* Fri Apr 14 2017 Xavier Bachelot <xavier@bachelot.org> 2017.004-1
- Update to 2017.004.
- Drop EL5 support.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.003-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu May 19 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2016.003-2
- Perl 5.24 re-rebuild of bootstrapped packages

* Mon May 16 2016 Xavier Bachelot <xavier@bachelot.org> 2016.003-1
- Update to 2016.003.
- Clean up specfile.

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2015.12-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2015.12-1
- 2015.12 bump

* Fri Sep 11 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2015.07.16-1
- 2015.07.16 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2013.11-6
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2013.11-5
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 18 2014 Xavier Bachelot <xavier@bachelot.org> 2013.11-2
- Fix filtering for EL7.

* Mon Dec 02 2013 Xavier Bachelot <xavier@bachelot.org> 2013.11-1
- Update to 2013.11.

* Mon Oct 21 2013 Xavier Bachelot <xavier@bachelot.org> 2013.10-1
- Update to 2013.10.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 2012.06-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 2012.06-2
- Perl 5.16 rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 2012.06-1
- 2012.06 bump (to fix building)

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 2011.11-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 22 2011 Xavier Bachelot <xavier@bachelot.org> 2011.11-2
- Filter out bad requires perl(Unicode::LineBreak::Constants).
- Adapt provides and requires filtering to handle all 3 variants
  (EL5; F14/EL6; F15+).

* Fri Nov 18 2011 Xavier Bachelot <xavier@bachelot.org> 2011.11-1
- Update to 2011.11.

* Mon Oct 17 2011 Xavier Bachelot <xavier@bachelot.org> 2011.05-4
- Drop patch and revert to stricter provides filtering.

* Mon Oct 10 2011 Xavier Bachelot <xavier@bachelot.org> 2011.05-3
- Add patch to fix provides.
- Fix provides filtering.

* Mon Aug 01 2011 Xavier Bachelot <xavier@bachelot.org> 2011.05-2
- Filter provides.

* Tue May 17 2011 Xavier Bachelot <xavier@bachelot.org> 2011.05-1
- Spec clean up.
- Add a BR: on sombok-devel.

* Mon May 02 2011 Xavier Bachelot <xavier@bachelot.org> 2011.04.26-1
- Specfile autogenerated by cpanspec 1.78.
