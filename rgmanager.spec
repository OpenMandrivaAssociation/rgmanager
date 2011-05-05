%define name rgmanager
%define version 1.9.30
%define release %mkrel 5

Summary: HA Resource Group Failover for Red Hat Enterprise Linux
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: System
#Url: 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: chkconfig initscripts glibc ncurses libxml2 bash grep sed gawk magma ccs
BuildRequires: glibc-devel ncurses-devel libxml2-devel magma ccs

%description
Red Hat Resource Group Manager provides high availability of critical server
applications in the event of planned or unplanned system downtime.

%prep
%setup -q

%build
./configure --incdir=%{_includedir} \
	--kernel_src=/usr/src/linux \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
	--sbindir=%{_sbindir} \
	--sharedir=%{_datadir}/%name

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_initrddir}
%makeinstall DESTDIR=$RPM_BUILD_ROOT
mv -vf $RPM_BUILD_ROOT/etc/init.d/%name $RPM_BUILD_ROOT%{_initrddir}/%name

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING
%{_initrddir}/%name
%{_datadir}/%name/*
%{_sbindir}/*
%{_mandir}/man8/

