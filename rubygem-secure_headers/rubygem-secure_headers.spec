%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name secure_headers

Summary: Add easily configured browser headers to responses
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.4.1
Release: 4%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: https://github.com/twitter/secureheaders
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Add easily configured browser headers to responses including content security
policy, x-frame-options, strict-transport-security and more.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_libdir}
%exclude %{gem_instdir}/secure_headers.gemspec
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/HISTORY.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/fixtures
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/spec
%{gem_instdir}/travis.sh

%changelog
* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 1.4.1-4
- Use gem_install macro (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.4.1-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.4.1-2
- Converted to tfm SCL (dcleal@redhat.com)

* Mon Dec 15 2014 Dominic Cleal <dcleal@redhat.com> 1.4.1-1
- Update secure_headers to 1.4.1 (dcleal@redhat.com)

* Mon Oct 13 2014 Dominic Cleal <dcleal@redhat.com> 1.3.3-1
- new package built with tito