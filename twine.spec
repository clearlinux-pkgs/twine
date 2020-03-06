#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : twine
Version  : 3.1.1
Release  : 3
URL      : https://files.pythonhosted.org/packages/7e/2f/e2a91a8ab97e8c9830ce297132631aef5dcd599f076123d1ebb26f1941b6/twine-3.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/7e/2f/e2a91a8ab97e8c9830ce297132631aef5dcd599f076123d1ebb26f1941b6/twine-3.1.1.tar.gz
Summary  : Collection of utilities for publishing packages on PyPI
Group    : Development/Tools
License  : Apache-2.0
Requires: twine-bin = %{version}-%{release}
Requires: twine-license = %{version}-%{release}
Requires: twine-python = %{version}-%{release}
Requires: twine-python3 = %{version}-%{release}
Requires: importlib_metadata
Requires: keyring
Requires: readme_renderer
Requires: requests
Requires: requests-toolbelt
Requires: setuptools
Requires: tqdm
BuildRequires : buildreq-distutils3
BuildRequires : keyring
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : requests
BuildRequires : requests-toolbelt
BuildRequires : setuptools
BuildRequires : setuptools_scm-python
BuildRequires : tox
BuildRequires : tqdm
BuildRequires : virtualenv

%description
.. image:: https://img.shields.io/pypi/v/twine.svg
:target: https://pypi.org/project/twine

%package bin
Summary: bin components for the twine package.
Group: Binaries
Requires: twine-license = %{version}-%{release}

%description bin
bin components for the twine package.


%package license
Summary: license components for the twine package.
Group: Default

%description license
license components for the twine package.


%package python
Summary: python components for the twine package.
Group: Default
Requires: twine-python3 = %{version}-%{release}

%description python
python components for the twine package.


%package python3
Summary: python3 components for the twine package.
Group: Default
Requires: python3-core
Provides: pypi(twine)
Requires: pypi(keyring)
Requires: pypi(pkginfo)
Requires: pypi(readme_renderer)
Requires: pypi(requests)
Requires: pypi(requests_toolbelt)
Requires: pypi(setuptools)
Requires: pypi(tqdm)

%description python3
python3 components for the twine package.


%prep
%setup -q -n twine-3.1.1
cd %{_builddir}/twine-3.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583456182
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/twine
cp %{_builddir}/twine-3.1.1/LICENSE %{buildroot}/usr/share/package-licenses/twine/7f6eb21389a5af4de0e7927a25fe236bc0cd3a75
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/twine

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/twine/7f6eb21389a5af4de0e7927a25fe236bc0cd3a75

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
