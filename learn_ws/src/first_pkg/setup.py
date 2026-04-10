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
