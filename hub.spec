#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hub
Version  : 2.3.0.pre8
Release  : 5
URL      : https://github.com/github/hub/archive/v2.3.0-pre8.tar.gz
Source0  : https://github.com/github/hub/archive/v2.3.0-pre8.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause LGPL-3.0 MIT WTFPL
Requires: hub-bin
BuildRequires : go
Patch1: build.patch

%description
PACKAGE
package shellquote
import "github.com/kballard/go-shellquote"
Shellquote provides utilities for joining/splitting strings using sh's
word-splitting rules.

%package bin
Summary: bin components for the hub package.
Group: Binaries

%description bin
bin components for the hub package.


%prep
%setup -q -n hub-2.3.0-pre8
%patch1 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491334018
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1491334018
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hub
