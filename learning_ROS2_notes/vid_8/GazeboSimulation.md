# simulation with Gazebo

## install gazebo is ROS2

### ROS2 jazzy

```
sudo apt update
sudo apt install ros-jazzy-ros-gz
```

#### test if gazebo is successfully installed for jazzy

```
gz sim
```

### ROS2 humble

```
sudo apt update
sudo apt install ros-humble-ros-gz
```

```
ros2 pkg list | grep ros_gz
```

check if gazebo is part of the ros2 pkg

```
source /opt/ros/jazzy/setup.bash
gz sim
```

run sim to check if it works.

```
find /usr/share -type f \( -name "*.sdf" -o -name "*.world" \) 2>/dev/null | grep -Ei "gz|gazebo|world" | sort
```

check what example worlds we have in jazzy gazebo

```
gz sim /opt/ros/jazzy/share/ros_gz_sim_demos/worlds/vehicle.sdf

gz sim /opt/ros/jazzy/share/ros_gz_sim_demos/worlds/dvl.sdf
```

try running one of the world in gazebo

#### test if gazebo is successfully installed humble

```
ign gazebo
```

in the video he suggest to test out with one of the sample environment:

```
gazebo /usr/share/gazebo-11/worlds/seesaw.world
```

## add ROS2 jazzy into bashrc for it to run every terminal start up

### without this

```
source /opt/ros/jazzy/setup.bash
gz sim
```

without adding jazzy to bashrc, we would need source to tell the terminal where our environment is.

### adding it to bashrc

```
grep "source /opt/ros/jazzy/setup.bash" ~/.bashrc
```

check whether bashrc already have "source /opt/ros/jazzy/setup.bash"

if not, run:

```
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
```

## check if gazebo is one of the package in ROS2

```
ros2 pkg list | grep ros_gz
```

## use ros to get robot into simulation environment

### gazebo model stucture:

gazebo uses SDF to describe models, which is similar to ROS2 version of URDF. Gazebo have a tool that convert URDF to SDF. URDF only describe a robot, SDF describe the robot as well as the world that it is simulated in.

any file with .world is sdf file, but also inside a world all those models can be have it's own sdf file. this allow us to reuse models inside different worlds, or reuse world to test different robot. 

### gazebo interaction with ROS2

when gazebo want to interact with ROS2, it need a plug in. plug-ins tell gazebo what to do at a time, if we want to control the robot or check sensor value, we have to request gazebo thru plug-ins.

#### gazebo map

before we learn:

- robot_state_publisher take urdf file and convert it to /robot_description
- robot_state_publisher take /joint_states and convert it to "TF System"

Gazebo:

- gazebo use a spawner script that read and simulate /robot_description, so we can visually visualize activity of the robot
- gazebo use joint state publisher plugin to publish how the joints are moving in the simulation to /joint_states topic
- gazebo use joint controller plugin to take input from ROS2 and force the joint to move in the simulation 
- gazebo also also for any amount of sensor plugins to publish to sensor topic (/my_sensor /another_sensor ...)

