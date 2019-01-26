#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hub
Version  : 2.8.3
Release  : 19
URL      : https://github.com/github/hub/archive/v2.8.3.tar.gz
Source0  : https://github.com/github/hub/archive/v2.8.3.tar.gz
Summary  : cli interface for Github
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause MIT WTFPL
Requires: hub-bin = %{version}-%{release}
Requires: hub-license = %{version}-%{release}
BuildRequires : buildreq-golang
BuildRequires : go
Patch1: 0001-build-for-clr.patch

%description
## TOML parser and encoder for Go with reflection
TOML stands for Tom's Obvious, Minimal Language. This Go package provides a
reflection interface similar to Go's standard library `json` and `xml`
packages. This package also supports the `encoding.TextUnmarshaler` and
`encoding.TextMarshaler` interfaces so that you can define custom data
representations. (There is an example of this below.)

%package bin
Summary: bin components for the hub package.
Group: Binaries
Requires: hub-license = %{version}-%{release}

%description bin
bin components for the hub package.


%package license
Summary: license components for the hub package.
Group: Default

%description license
license components for the hub package.


%prep
%setup -q -n hub-2.8.3
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
mkdir -p %{buildroot}/usr/share/package-licenses/hub
cp LICENSE %{buildroot}/usr/share/package-licenses/hub/LICENSE
cp vendor/github.com/BurntSushi/toml/COPYING %{buildroot}/usr/share/package-licenses/hub/vendor_github.com_BurntSushi_toml_COPYING
cp vendor/github.com/BurntSushi/toml/cmd/toml-test-decoder/COPYING %{buildroot}/usr/share/package-licenses/hub/vendor_github.com_BurntSushi_toml_cmd_toml-test-decoder_COPYING
cp vendor/github.com/BurntSushi/toml/cmd/toml-test-encoder/COPYING %{buildroot}/usr/share/package-licenses/hub/vendor_github.com_BurntSushi_toml_cmd_toml-test-encoder_COPYING
cp vendor/github.com/BurntSushi/toml/cmd/tomlv/COPYING %{buildroot}/usr/share/package-licenses/hub/vendor_github.com_BurntSushi_toml_cmd_tomlv_COPYING
cp vendor/github.com/atotto/clipboard/LICENSE %{buildroot}/usr/share/package-licenses/hub/vendor_github.com_atotto_clipboard_LICENSE
cp vendor/github.com/kballard/go-shellquote/LICENSE %{buildroot}/usr/share/package-licenses/hub/vendor_github.com_kballard_go-shellquote_LICENSE
cp vendor/github.com/kr/pretty/License %{buildroot}/usr/share/package-licenses/hub/vendor_github.com_kr_pretty_License
cp vendor/github.com/kr/text/License %{buildroot}/usr/share/package-licenses/hub/vendor_github.com_kr_text_License
cp vendor/github.com/mattn/go-colorable/LICENSE %{buildroot}/usr/share/package-licenses/hub/vendor_github.com_mattn_go-colorable_LICENSE
cp vendor/github.com/mattn/go-isatty/LICENSE %{buildroot}/usr/share/package-licenses/hub/vendor_github.com_mattn_go-isatty_LICENSE
cp vendor/github.com/mitchellh/go-homedir/LICENSE %{buildroot}/usr/share/package-licenses/hub/vendor_github.com_mitchellh_go-homedir_LICENSE
cp vendor/github.com/russross/blackfriday/LICENSE.txt %{buildroot}/usr/share/package-licenses/hub/vendor_github.com_russross_blackfriday_LICENSE.txt
cp vendor/github.com/shurcooL/sanitized_anchor_name/LICENSE %{buildroot}/usr/share/package-licenses/hub/vendor_github.com_shurcooL_sanitized_anchor_name_LICENSE
cp vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/hub/vendor_golang.org_x_crypto_LICENSE
cp vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/hub/vendor_golang.org_x_sys_LICENSE
cp vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/package-licenses/hub/vendor_gopkg.in_yaml.v2_LICENSE
cp vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/hub/vendor_gopkg.in_yaml.v2_LICENSE.libyaml
cp vendor/gopkg.in/yaml.v2/NOTICE %{buildroot}/usr/share/package-licenses/hub/vendor_gopkg.in_yaml.v2_NOTICE

## install_append content
mkdir -p %{buildroot}/usr/bin
install -m 755 hub-%{version} %{buildroot}/usr/bin/hub
ln -s hub  %{buildroot}/usr/bin/git-hub
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/git-hub
/usr/bin/hub

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/hub/LICENSE
/usr/share/package-licenses/hub/vendor_github.com_BurntSushi_toml_COPYING
/usr/share/package-licenses/hub/vendor_github.com_BurntSushi_toml_cmd_toml-test-decoder_COPYING
/usr/share/package-licenses/hub/vendor_github.com_BurntSushi_toml_cmd_toml-test-encoder_COPYING
/usr/share/package-licenses/hub/vendor_github.com_BurntSushi_toml_cmd_tomlv_COPYING
/usr/share/package-licenses/hub/vendor_github.com_atotto_clipboard_LICENSE
/usr/share/package-licenses/hub/vendor_github.com_kballard_go-shellquote_LICENSE
/usr/share/package-licenses/hub/vendor_github.com_kr_pretty_License
/usr/share/package-licenses/hub/vendor_github.com_kr_text_License
/usr/share/package-licenses/hub/vendor_github.com_mattn_go-colorable_LICENSE
/usr/share/package-licenses/hub/vendor_github.com_mattn_go-isatty_LICENSE
/usr/share/package-licenses/hub/vendor_github.com_mitchellh_go-homedir_LICENSE
/usr/share/package-licenses/hub/vendor_github.com_russross_blackfriday_LICENSE.txt
/usr/share/package-licenses/hub/vendor_github.com_shurcooL_sanitized_anchor_name_LICENSE
/usr/share/package-licenses/hub/vendor_golang.org_x_crypto_LICENSE
/usr/share/package-licenses/hub/vendor_golang.org_x_sys_LICENSE
/usr/share/package-licenses/hub/vendor_gopkg.in_yaml.v2_LICENSE
/usr/share/package-licenses/hub/vendor_gopkg.in_yaml.v2_LICENSE.libyaml
/usr/share/package-licenses/hub/vendor_gopkg.in_yaml.v2_NOTICE
