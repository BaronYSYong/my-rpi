# memo error for building docker in raspberry pi
```
ImportError: cannot import name _remove_dead_weakref
```
* try upgrade from python 2.7.9 to python 2.7.14 to solve this
	* https://tecadmin.net/install-python-2-7-on-ubuntu-and-linuxmint/

```
error: option --install-layout not recognized
CMake Error at catkin_generated/safe_execute_install.cmake:4 (message):
```
solve with
```
./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release -DSETUPTOOLS_DEB_LAYOUT=OFF
```

```
ImportError: No module named catkin.environment_cache
```
try :
```
apt-get install python-catkin-tools
./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release -DSETUPTOOLS_DEB_LAYOUT=OFF --install-space /opt/ros/kinetic -j2
```

```
AttributeError: install_layout
```
try 
```
pip install -U setuptools
```
