Name:           ros-hydro-sick-tim
Version:        0.0.5
Release:        0%{?dist}
Summary:        ROS sick_tim package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       libusbx
Requires:       ros-hydro-diagnostic-updater
Requires:       ros-hydro-driver-base
Requires:       ros-hydro-dynamic-reconfigure
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-sensor-msgs
BuildRequires:  libusbx-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-diagnostic-updater
BuildRequires:  ros-hydro-driver-base
BuildRequires:  ros-hydro-dynamic-reconfigure
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-sensor-msgs

%description
A ROS driver for the SICK TiM series of laser scanners. Currently, the pacakge
supports serveral types of TiM310 and TiM551 scanners.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Wed May 06 2015 Martin Günther <mguenthe@uos.de> - 0.0.5-0
- Autogenerated by Bloom

* Mon Mar 16 2015 Martin Günther <mguenthe@uos.de> - 0.0.4-0
- Autogenerated by Bloom

* Fri Jan 09 2015 Martin Günther <mguenthe@uos.de> - 0.0.3-0
- Autogenerated by Bloom

* Mon Sep 01 2014 Martin Günther <mguenthe@uos.de> - 0.0.2-0
- Autogenerated by Bloom

