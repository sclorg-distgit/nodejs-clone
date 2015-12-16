%{?scl:%scl_package nodejs-%{srcname}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global srcname clone

Name:           %{?scl_prefix}nodejs-%{srcname}
Version:        0.2.0
Release:        3.sc1%{?dist}
Summary:        Deep cloning of objects and arrays
License:        MIT
URL:            https://github.com/pvorb/node-clone
Source0:        http://registry.npmjs.org/%{srcname}/-/%{srcname}-%{version}.tgz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs010

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}nodeunit
BuildRequires:  %{?scl_prefix}npm(underscore)
%endif

%description
Offers foolproof deep cloning of variables in JavaScript.

%prep
%setup -q -n package
rm -rf node_modules/

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{srcname}
cp -pr package.json clone.js %{buildroot}%{nodejs_sitelib}/%{srcname}

%nodejs_symlink_deps


%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
nodeunit test.js
%endif

%files
%doc README.md LICENSE
%{nodejs_sitelib}/%{srcname}

%changelog
* Tue Jan 13 2015 Tomas Hrcka <thrcka@redhat.com> - 0.2.0-3
- Add provides_requires macro

* Mon Jan 12 2015 Tomas Hrcka <thrcka@redhat.com> - 0.2.0-2
- Enable software collection support

* Fri Dec 19 2014 Piotr Popieluch <piotr1212@gmail.com> - 0.2.0-1
- updated to latest upstream

* Sat Dec  6 2014 Piotr Popieluch <piotr1212@gmail.com> - 0.1.18-2
- Added LICENSE to %%files
- Added rm -rf node_modules to %%prep
- Capitalized summary
- Removed Group tag

* Fri Nov 21 2014 Piotr Popieluch <piotr1212@gmail.com> - 0.1.18-1
- Initial package
