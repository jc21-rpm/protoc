%global debug_package %{nil}

# Turn off strip'ng of binaries
%global __strip /bin/true

Name:           protoc
Version:        29.3
Release:        1%{?dist}
Summary:        Protocol Buffers - Google's data interchange format
License:        Apache-2.0
URL:            https://github.com/grpc/grpc
Source:         https://github.com/protocolbuffers/protobuf/releases/download/v%{version}/protobuf-%{version}.tar.gz
BuildRequires:  bazel

%description
%{summary}.

%prep
%setup -q -n protobuf-%{version}

%build
bazel build :protoc :protobuf --enable_bzlmod

%install

rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp bazel-bin/%{name} %{buildroot}/usr/bin
chmod +x %{buildroot}/usr/bin/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/%{name}

%changelog
* Mon Feb 24 2025 Jamie Curnow <jc@jc21.com> - 29.3-1
- v29.3
