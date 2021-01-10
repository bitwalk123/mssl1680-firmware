%define current_kernel %(uname -r)

%global debug_package %{nil}
%global firmware_release 1

%global _firmwarepath   /usr/lib/firmware
%define _binaries_in_noarch_packages_terminate_build 0

Name:           mssl1680-firmware
Version:        1.0.git20180803.6451db2
Release:        %{firmware_release}%{?dist}
Summary:	Firmware for silead mmsl1680 touchscreen.
License:        GPLv3
Group:          Hardware/Other
URL:            https://github.com/edward-p/mssl1680-firmware

Source:         %{name}-%{version}.tar.xz

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Firmware for silead mmsl1680 touchscreen.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/%{_firmwarepath}/silead
cp -r mssl1680.fw %{buildroot}/%{_firmwarepath}/silead/mssl1680.fw


%post
%postun

%files
%defattr(-,root,root)
%doc LICENSE README.md
%dir %{_firmwarepath}
%{_firmwarepath}/*

%changelog
* Sun Jan 10 2021 Fuhito Suguri <bitwalk@users.sourceforge.net> - 1.0.git20180803.6451db2-1
- initial version from upstream
