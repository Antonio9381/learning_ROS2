# Colon workspace

--- 

## note link

first note

--- 

To createm build and run custom nodes we need packages, but first we need a ws.

we can use ws to maintain our future packages.

## terms to learn for ws:

1. ament: provide underlying build system and tools for ROS2 packages.
  - ament_cmake: for Cmake-based build system for C/C++ nodes and libraries.
  - ament_python: provide tools for packing and installing python nodes and libraries
2. colon (COmmand Line COLlectioN): general-purpose tool to guild and manage entire ws with various build system, including ament, cmake, make, and more. 
3. you can have cmake and python packages in one ws

## to make ws

```
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
```

packages live in src directory.

## to make packages

```
ros2 pkg create --build-type ament_python bme_MOGI_git_tut
```

we alway want to mention 'ament_python' because the default is always 'ament_cmake'

## adding a note

all the python script should live in the directory with '__init__.py'

therefore to add our first node, we can just add a python file like so:

```
touch hello_world.py
```

## now the ws look like

```
bme_MOGI_git_tut
├── bme_MOGI_git_tut
│   └── __init__.py
├── package.xml
├── resource
│   └── bme_MOGI_git_tut
├── setup.cfg
├── setup.py
└── test
    ├── test_copyright.py
    ├── test_flake8.py
    └── test_pep257.py
```

---

# 1. package.xml ⭐⭐⭐⭐⭐

The **identity card** of your package.

It tells ROS:

- Package name
- Version
- Description
- Author/Maintainer
- License
- Dependencies

Example:

```xml
<depend>rclpy</depend>
```

### Edit this when:

- Adding dependencies
- Changing package information
- Publishing your package

---

# 2. setup.py ⭐⭐⭐⭐⭐

The **installer** for your Python package.

When you run:

```bash
colcon build
```

ROS uses `setup.py` to install your package.

It also tells ROS which Python files are executable nodes.

Example:

```python
entry_points={
    'console_scripts': [
        'talker = bme_MOGI_git_tut.publisher:main',
        'listener = bme_MOGI_git_tut.listener:main',
    ],
}
```

This lets you run:

```bash
ros2 run bme_MOGI_git_tut talker
```

### Edit this when:

- Adding a new node
- Renaming a node

---

# 3. setup.cfg ⭐⭐⭐

Contains installation settings for Python.

Usually looks like:

```ini
[develop]
script_dir=$base/lib/bme_MOGI_git_tut

[install]
install_scripts=$base/lib/bme_MOGI_git_tut
```

### Edit this?

Almost never.

---

# 4. resource/

```text
resource/
└── bme_MOGI_git_tut
```

Allows ROS to discover your package.

### Edit this?

Never (unless you know why).

---

# 5. bme_MOGI_git_tut/ ⭐⭐⭐⭐⭐

This is where **your code lives**.

Example:

```text
bme_MOGI_git_tut/
├── __init__.py
├── publisher.py
├── subscriber.py
├── service_server.py
├── service_client.py
└── utils.py
```

You'll spend most of your time here.

---

# 6. __init__.py

Marks this folder as a Python package.

Usually empty.

### Edit this?

Rarely.

---

# 7. test/

```text
test/
├── test_copyright.py
├── test_flake8.py
└── test_pep257.py
```

Contains automatic tests.

### Files

- **test_flake8.py** → Checks coding style.
- **test_pep257.py** → Checks documentation.
- **test_copyright.py** → Checks license headers.

### Edit this?

Usually not while learning.

---

# What You'll Use Most

As a beginner, you'll mainly work with:

```text
package.xml
```

and

```text
bme_MOGI_git_tut/
```

Inside your package folder you'll create files like:

```text
publisher.py
subscriber.py
robot_controller.py
```

---

# Build Process

```text
colcon build
      │
      ▼
setup.py
      │
      ▼
Installs Python package
      │
      ▼
package.xml
      │
      ▼
ROS knows dependencies
      │
      ▼
resource/
      │
      ▼
ROS discovers package
      │
      ▼
Python source files
      │
      ▼
ros2 run package_name executable
```

---

# Quick Summary

| File/Folder | Purpose | Edit Often? |
|-------------|---------|-------------|
| `package.xml` | Package information & dependencies | ✅ Yes |
| `setup.py` | Defines executable nodes | ✅ Yes |
| `setup.cfg` | Installation settings | ❌ Rarely |
| `resource/` | ROS package discovery | ❌ No |
| `bme_MOGI_git_tut/` | Your Python code | ✅ Yes |
| `__init__.py` | Makes folder a Python package | ❌ Rarely |
| `test/` | Automated tests | ❌ Rarely |

---

# Common Folders in Larger ROS 2 Packages

You may also see:

| Folder | Purpose |
|---------|---------|
| `launch/` | Starts multiple ROS nodes together |
| `config/` | YAML parameter files |
| `urdf/` | Robot models |
| `meshes/` | 3D models |
| `worlds/` | Gazebo simulation worlds |
| `rviz/` | RViz configuration files |

These are not created by default but are very common in real ROS 2 projects.
