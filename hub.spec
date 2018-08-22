#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hub
Version  : 2.5.0
Release  : 10
URL      : https://github.com/github/hub/archive/v2.5.0.tar.gz
Source0  : https://github.com/github/hub/archive/v2.5.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT WTFPL
Requires: hub-bin
Requires: hub-license
BuildRequires : buildreq-golang
BuildRequires : go
Patch1: 0001-build-for-clr.patch

%description
This is a Go package for manipulating paragraphs of text.
See http://go.pkgdoc.org/github.com/kr/text for full documentation.

%package bin
Summary: bin components for the hub package.
Group: Binaries
Requires: hub-license

%description bin
bin components for the hub package.


%package doc
Summary: doc components for the hub package.
Group: Documentation

%description doc
doc components for the hub package.


%package license
Summary: license components for the hub package.
Group: Default

%description license
license components for the hub package.


%prep
%setup -q -n hub-2.5.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export GOPATH="$PWD"
go build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/hub
cp LICENSE %{buildroot}/usr/share/doc/hub/LICENSE
cp vendor/github.com/BurntSushi/toml/COPYING %{buildroot}/usr/share/doc/hub/vendor_github.com_BurntSushi_toml_COPYING
cp vendor/github.com/BurntSushi/toml/cmd/toml-test-decoder/COPYING %{buildroot}/usr/share/doc/hub/vendor_github.com_BurntSushi_toml_cmd_toml-test-decoder_COPYING
cp vendor/github.com/BurntSushi/toml/cmd/toml-test-encoder/COPYING %{buildroot}/usr/share/doc/hub/vendor_github.com_BurntSushi_toml_cmd_toml-test-encoder_COPYING
cp vendor/github.com/BurntSushi/toml/cmd/tomlv/COPYING %{buildroot}/usr/share/doc/hub/vendor_github.com_BurntSushi_toml_cmd_tomlv_COPYING
cp vendor/github.com/atotto/clipboard/LICENSE %{buildroot}/usr/share/doc/hub/vendor_github.com_atotto_clipboard_LICENSE
cp vendor/github.com/kballard/go-shellquote/LICENSE %{buildroot}/usr/share/doc/hub/vendor_github.com_kballard_go-shellquote_LICENSE
cp vendor/github.com/kr/pretty/License %{buildroot}/usr/share/doc/hub/vendor_github.com_kr_pretty_License
cp vendor/github.com/kr/text/License %{buildroot}/usr/share/doc/hub/vendor_github.com_kr_text_License
cp vendor/github.com/mattn/go-colorable/LICENSE %{buildroot}/usr/share/doc/hub/vendor_github.com_mattn_go-colorable_LICENSE
cp vendor/github.com/mattn/go-isatty/LICENSE %{buildroot}/usr/share/doc/hub/vendor_github.com_mattn_go-isatty_LICENSE
cp vendor/github.com/mitchellh/go-homedir/LICENSE %{buildroot}/usr/share/doc/hub/vendor_github.com_mitchellh_go-homedir_LICENSE
cp vendor/github.com/ogier/pflag/LICENSE %{buildroot}/usr/share/doc/hub/vendor_github.com_ogier_pflag_LICENSE
cp vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/doc/hub/vendor_golang.org_x_crypto_LICENSE
cp vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/doc/hub/vendor_golang.org_x_sys_LICENSE
cp vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/doc/hub/vendor_gopkg.in_yaml.v2_LICENSE
cp vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/doc/hub/vendor_gopkg.in_yaml.v2_LICENSE.libyaml
cp vendor/gopkg.in/yaml.v2/NOTICE %{buildroot}/usr/share/doc/hub/vendor_gopkg.in_yaml.v2_NOTICE

## install_append content
mkdir -p %{buildroot}/usr/bin
install -m 755 hub-%{version} %{buildroot}/usr/bin/hub
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hub

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/hub/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/hub/LICENSE
/usr/share/doc/hub/vendor_github.com_BurntSushi_toml_COPYING
/usr/share/doc/hub/vendor_github.com_BurntSushi_toml_cmd_toml-test-decoder_COPYING
/usr/share/doc/hub/vendor_github.com_BurntSushi_toml_cmd_toml-test-encoder_COPYING
/usr/share/doc/hub/vendor_github.com_BurntSushi_toml_cmd_tomlv_COPYING
/usr/share/doc/hub/vendor_github.com_atotto_clipboard_LICENSE
/usr/share/doc/hub/vendor_github.com_kballard_go-shellquote_LICENSE
/usr/share/doc/hub/vendor_github.com_mattn_go-colorable_LICENSE
/usr/share/doc/hub/vendor_github.com_mattn_go-isatty_LICENSE
/usr/share/doc/hub/vendor_github.com_mitchellh_go-homedir_LICENSE
/usr/share/doc/hub/vendor_github.com_ogier_pflag_LICENSE
/usr/share/doc/hub/vendor_golang.org_x_crypto_LICENSE
/usr/share/doc/hub/vendor_golang.org_x_sys_LICENSE
/usr/share/doc/hub/vendor_gopkg.in_yaml.v2_LICENSE
/usr/share/doc/hub/vendor_gopkg.in_yaml.v2_LICENSE.libyaml
