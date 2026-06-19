# setting up ros2 workspace(ws) & packages | use talker and listener - vid 5
## creating ws
- go to the directory you want this set up in and then type `mkdir -p learn_ws/src`
- change into the directory `cd learn_ws`, build directory using colcon `colcon build --symlink-install`

## creating package
- change into the src directory `cd src`
- created empty package: `ros2 pkg create --build-type ament_python py_package_name`

## creating launch file
- create a lunch directory for your launch files 
- create launch file with name `*.launch.py`

## edit setup.py so that ros know how to build
```
from setuptools import find_packages, setup

#personally added:
import os
from glob import glob
#

package_name = 'first_pkg'

# This gets the directory where setup.py itself lives
pkg_dir = os.path.dirname(os.path.abspath(__file__))

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        #personally added:
        # Automatically installs ALL launch files across ALL video folders
        *[
            (
                os.path.join('share', package_name, os.path.dirname(
                    os.path.relpath(f, pkg_dir)
                )),
                [os.path.relpath(f, pkg_dir)]
            )
            for f in glob(os.path.join(pkg_dir, 'launch/**/*.launch.py'), recursive=True)
            if os.path.isfile(f)
        ],
        # edit done 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='awutio23',
    maintainer_email='ant938153@gamil.com',
    description='ROS2 learning pkg',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
```

## edit the package.xml file
- tell ros and colcon about our dependencies
- add `<exec_depend>demo_nodes_py</exec_depend>` into package.xml

## build the package
- cd back to the workspace directory
```
# First time or after changing setup.py:
cd ~/learnROS2/learning_ROS2/learn_ws
rm -rf build/ install/ log/
source /opt/ros/humble/setup.bash
colcon build --symlink-install
source install/setup.bash
```
```
# No rebuild needed if using --symlink-install and only editing existing files
source install/setup.bash
ros2 launch py_first_package listener.launch.py

# Only rebuild if you ADD a new file
colcon build --symlink-install && source install/setup.bash
```
## to launch the launch file
- type `ros2 launch first_pkg talker.launch.py`
    - `ros2 lauch <pkg name> <launch file name>`
