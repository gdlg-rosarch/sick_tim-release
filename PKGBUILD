# Script generated with Bloom
pkgdesc="ROS - A ROS driver for the SICK TiM and the SICK MRS 1000 laser scanners."
url='http://wiki.ros.org/sick_tim'

pkgname='ros-lunar-sick-tim'
pkgver='0.0.12_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('libusbx'
'ros-lunar-catkin'
'ros-lunar-diagnostic-updater'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-roscpp'
'ros-lunar-roslaunch'
'ros-lunar-sensor-msgs'
)

depends=('libusbx'
'ros-lunar-diagnostic-updater'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-robot-state-publisher'
'ros-lunar-roscpp'
'ros-lunar-sensor-msgs'
'ros-lunar-xacro'
)

conflicts=()
replaces=()

_dir=sick_tim
source=()
md5sums=()

prepare() {
    cp -R $startdir/sick_tim $srcdir/sick_tim
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

