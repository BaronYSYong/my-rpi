# memo error for building docker in raspberry pi

## ImportError: cannot import name _remove_dead_weakref
* try upgrade from python 2.7.9 to python 2.7.14 to solve this
	* https://tecadmin.net/install-python-2-7-on-ubuntu-and-linuxmint/

## error: option --install-layout not recognized
* solve with
```
./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release -DSETUPTOOLS_DEB_LAYOUT=OFF
```

## ImportError: No module named catkin.environment_cache
* try:
```
apt-get install python-catkin-tools
./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release -DSETUPTOOLS_DEB_LAYOUT=OFF --install-space /opt/ros/kinetic -j2
```
## AttributeError: install_layout
* try:
```
pip install -U setuptools
```
## ImportError: /usr/lib/python2.7/dist-packages/PyQt5/QtCore.so: undefined symbol: PyUnicodeUCS4_FromUnicode
* try:
```
sudo apt-get update
sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools
```
```
# nm -D /usr/bin/python2.7 | grep FromUnicode
001d21c0 T PyInt_FromUnicode
001f1c28 T PyLong_FromUnicode
00118514 T PyUnicodeUCS4_FromUnicode
# which python
/usr/local/bin/python
# nm -D /usr/local/bin/python | grep FromUnicode
00052774 T PyInt_FromUnicode
00063c88 T PyLong_FromUnicode
0009f828 T PyUnicodeUCS2_FromUnicode
```

## Could not find a package configuration file provided by "Eigen3"
```
cp /usr/share/cmake-3.0/Modules/FindEigen3.cmake /usr/share/cmake-3.6/Modules/
```

## Could not find a package configuration file provided by "OpenCV"
try
```
apt-get install libopencv-dev
```
