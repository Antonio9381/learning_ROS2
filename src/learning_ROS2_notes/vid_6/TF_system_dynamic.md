# Transform system dynamic 

to start weneed to install `sudo apt install ros-humble-xacro ros-humble-joint-state-publisher-gui`

## How to broadcast dynamic transform?
### URDF file
- a urdf file is a config file for robot that specified the physcial characteristic of the robot's component, things like their size, geometry, shape, color, and friction.
- in urdf a robot is made up of <u>tree of components</u> called links and they are <u>connect by</u> joint, and the relation of links is defined by joints. just like static transform.
### `robot_state_publisher`
- bc link joint pattern(URDF) is similar to frame transform pattern(TF), there is a ros node called `robot_state_publisher` that can take in urdf files and automatically broadcast all the transform from it.
- `robot_state_publisher` will publish the fixed joint transform to `/tf_static` and non-fixed joint transform to `/tf`, and `robot_state_publisher` will also broadcast the full urdf file's content to `/robot_description`
- in a urdf file, each joint can be defined as fixed or any other movable type such as continuous rotation, limited rotation, or linear motion.
- for join that r fixed `robot_state_publisher` can just publish static transform, but for the moving one's they need to publish dynamic transforms. 
- to publish dynamic transform, `robot_state_publisher` is going to need external value such as angles, linear distances, so that it can calculate what the transform need to be at each point in time.
### `joint_state_publisher_gui`
- to get these topic, `robot_state_publisher` will subscribe to topic called `/joint_states`, which will contain joint state msgs, which contain position, velocity, or effort of a joint. 
- noramlly `joint_states` will come from feedback like encoder of the actuator, but in a simulation we can fake the `/joint_states` using `joint_state_publisher_gui`.
- `joint_state_publisher_gui` will look at the urdf file, and see which joint could be move and make a slider UI for the user.

### running urdf manually
```
ros2 run robot_state_publisher robot_state_publisher --ros-args -p robot_description:="$( xacro /home/awutio23/learnROS2/learning_ROS2/learn_ws/src/first_pkg/launch/vid6/example_robot.urdf.xacro )"
```
- `$()` this is a sub-shell

### running urdf using launch file

```
ros2 launch first_pkg robot_state_publisher.launch.py
```

### running `joint_state_publisher_gui`
to get the slider to publish to `/joint_states`

```
ros2 run joint_state_publisher_gui joint_state_publisher_gui
```

### run rviz2 to visualize what we make
you can do `ros2 run rviz2 rviz2` or you can just run the shortcut `rviz2`

- first set 'fixed frame' to 'world'
- then click 'add', choose 'tf'
- open up 'TF' drop down, and then toggle 'show name' on
- then when you move slider, the visual will dynamically move with the slider as well.

#### robot model:
- as we have enough information for a robot in our urdf file we can see it as robot model in rviz2
- click 'add', then 'robotModel'
- open dropdown menu of 'robotModel'
- make sure description source is 'topic'
- choose 'description topic' as `/robot_description` which is published by `robot_state_publisher`

## debugging tool for TF
- key idea: if you just echo topic u just gonna get a lot of non sense, so ros2 have `view_frame` to make it easier to read transform issue
- `view_frame` is a python script in python tool pkg, so we just need to run `ros2 run tf2_tools view_frames`
- `view_frame` sit and listen for 5s for any transform, and then spit out a pdf to whatever directory it's in
- indicating 0 or 1000 just means they didn't really changed.