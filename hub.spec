#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hub
Version  : 2.14.2
Release  : 62
URL      : https://github.com/github/hub/archive/v2.14.2/hub-2.14.2.tar.gz
Source0  : https://github.com/github/hub/archive/v2.14.2/hub-2.14.2.tar.gz
Summary  : A command-line tool that makes git easier to use with GitHub
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause MIT WTFPL
Requires: hub-bin = %{version}-%{release}
Requires: hub-data = %{version}-%{release}
Requires: hub-license = %{version}-%{release}
BuildRequires : buildreq-golang
BuildRequires : go
Patch1: 0001-build-for-clr.patch

%description
hub is a command line tool that wraps git in order to extend it with extra
features and commands that make working with GitHub easier.

%package bin
Summary: bin components for the hub package.
Group: Binaries
Requires: hub-data = %{version}-%{release}
Requires: hub-license = %{version}-%{release}

%description bin
bin components for the hub package.


%package data
Summary: data components for the hub package.
Group: Data

%description data
data components for the hub package.


%package license
Summary: license components for the hub package.
Group: Default

%description license
license components for the hub package.


%prep
%setup -q -n hub-2.14.2
cd %{_builddir}/hub-2.14.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1595021208
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}  GOFLAGS='-mod=vendor -buildmode=pie -v'


%install
export SOURCE_DATE_EPOCH=1595021208
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/hub
cp %{_builddir}/hub-2.14.2/LICENSE %{buildroot}/usr/share/package-licenses/hub/9a434a6f4942dc25eed6b92c9f0047a81cb897eb
cp %{_builddir}/hub-2.14.2/vendor/github.com/BurntSushi/toml/COPYING %{buildroot}/usr/share/package-licenses/hub/568dd3613cf8145e8dbb35eeb920bd7d0c662b44
cp %{_builddir}/hub-2.14.2/vendor/github.com/atotto/clipboard/LICENSE %{buildroot}/usr/share/package-licenses/hub/5485efdb8b4f1167116feb7f4df9798329000329
cp %{_builddir}/hub-2.14.2/vendor/github.com/kballard/go-shellquote/LICENSE %{buildroot}/usr/share/package-licenses/hub/3afc456546a3fa3e82c0d21844cd9911d7d4464b
cp %{_builddir}/hub-2.14.2/vendor/github.com/kr/pretty/License %{buildroot}/usr/share/package-licenses/hub/cc6dc9e0c55f91b1cd26225dbf4e68a276136861
cp %{_builddir}/hub-2.14.2/vendor/github.com/kr/text/License %{buildroot}/usr/share/package-licenses/hub/9893c30cda569ecb5d3f8d615986e948947cd56d
cp %{_builddir}/hub-2.14.2/vendor/github.com/mattn/go-colorable/LICENSE %{buildroot}/usr/share/package-licenses/hub/5ca808f075931c5322193d4afd5a3370c824f810
cp %{_builddir}/hub-2.14.2/vendor/github.com/mattn/go-isatty/LICENSE %{buildroot}/usr/share/package-licenses/hub/5b53018d7f0706e49275a92d36b54cfbfbb71367
cp %{_builddir}/hub-2.14.2/vendor/github.com/mitchellh/go-homedir/LICENSE %{buildroot}/usr/share/package-licenses/hub/5ad2002bc8d2b22e2034867d159f71ba6258e18f
cp %{_builddir}/hub-2.14.2/vendor/github.com/russross/blackfriday/LICENSE.txt %{buildroot}/usr/share/package-licenses/hub/da34754c05d40ff81f91de8c1b85ea6e5503e21d
cp %{_builddir}/hub-2.14.2/vendor/github.com/shurcooL/sanitized_anchor_name/LICENSE %{buildroot}/usr/share/package-licenses/hub/c111106ab0af1873aa6350f797759fe1519c8be1
cp %{_builddir}/hub-2.14.2/vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/hub/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/hub-2.14.2/vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/hub/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/hub-2.14.2/vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/hub/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/hub-2.14.2/vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/hub/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/hub-2.14.2/vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/package-licenses/hub/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/hub-2.14.2/vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/hub/ad00ce7340d89dc13ccc59920ef75cb55af5b164
cp %{_builddir}/hub-2.14.2/vendor/gopkg.in/yaml.v2/NOTICE %{buildroot}/usr/share/package-licenses/hub/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
%make_install
## install_append content
mkdir -p %{buildroot}/usr/bin
install -m 755 bin/hub %{buildroot}/usr/bin/hub
ln -s hub %{buildroot}/usr/bin/git-hub
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/git-hub
/usr/bin/hub

%files data
%defattr(-,root,root,-)
/usr/share/vim/vimfiles/ftdetect/pullrequest.vim
/usr/share/vim/vimfiles/syntax/pullrequest.vim

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/hub/3afc456546a3fa3e82c0d21844cd9911d7d4464b
/usr/share/package-licenses/hub/5485efdb8b4f1167116feb7f4df9798329000329
/usr/share/package-licenses/hub/568dd3613cf8145e8dbb35eeb920bd7d0c662b44
/usr/share/package-licenses/hub/5ad2002bc8d2b22e2034867d159f71ba6258e18f
/usr/share/package-licenses/hub/5b53018d7f0706e49275a92d36b54cfbfbb71367
/usr/share/package-licenses/hub/5ca808f075931c5322193d4afd5a3370c824f810
/usr/share/package-licenses/hub/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/hub/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
/usr/share/package-licenses/hub/9893c30cda569ecb5d3f8d615986e948947cd56d
/usr/share/package-licenses/hub/9a434a6f4942dc25eed6b92c9f0047a81cb897eb
/usr/share/package-licenses/hub/ad00ce7340d89dc13ccc59920ef75cb55af5b164
/usr/share/package-licenses/hub/c111106ab0af1873aa6350f797759fe1519c8be1
/usr/share/package-licenses/hub/cc6dc9e0c55f91b1cd26225dbf4e68a276136861
/usr/share/package-licenses/hub/d6a5f1ecaedd723c325a2063375b3517e808a2b5
/usr/share/package-licenses/hub/da34754c05d40ff81f91de8c1b85ea6e5503e21d
