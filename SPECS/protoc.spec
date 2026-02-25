%global debug_package %{nil}

# Turn off strip'ng of binaries
%global __strip /bin/true

Name:           protoc
Version:        34.0
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
* Thu Feb 26 2026 Jamie Curnow <jc@jc21.com> - 34.0-1
- v34.0

* Fri Jan 30 2026 Jamie Curnow <jc@jc21.com> - 33.5-1
- v33.5

* Tue Jan 13 2026 Jamie Curnow <jc@jc21.com> - 33.4-1
- v33.4

* Mon Jan 12 2026 Jamie Curnow <jc@jc21.com> - 33.3-1
- v33.3

* Sun Dec 7 2025 Jamie Curnow <jc@jc21.com> - 33.2-1
- v33.2

* Thu Nov 13 2025 Jamie Curnow <jc@jc21.com> - 33.1-1
- v33.1

* Thu Oct 16 2025 Jamie Curnow <jc@jc21.com> - 33.0-1
- v33.0

* Sat Sep 13 2025 Jamie Curnow <jc@jc21.com> - 32.1-1
- v32.1

* Fri Aug 15 2025 Jamie Curnow <jc@jc21.com> - 32.0-1
- v32.0

* Thu May 29 2025 Jamie Curnow <jc@jc21.com> - 31.1-1
- v31.1

* Thu May 15 2025 Jamie Curnow <jc@jc21.com> - 31.0-1
- v31.0

* Thu Mar 27 2025 Jamie Curnow <jc@jc21.com> - 30.2-1
- v30.2

* Fri Mar 14 2025 Jamie Curnow <jc@jc21.com> - 30.1-1
- v30.1

* Wed Mar 5 2025 Jamie Curnow <jc@jc21.com> - 30.0-1
- v30.0

* Mon Feb 24 2025 Jamie Curnow <jc@jc21.com> - 29.3-1
- v29.3
