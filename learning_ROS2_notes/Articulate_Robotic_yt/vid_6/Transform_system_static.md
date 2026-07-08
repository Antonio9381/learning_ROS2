# The ROS Transform System (TF) | Getting Ready to Build Robots with ROS #6 - static

always run this to get started:
`source /opt/ros/humble/setup.bash`

ros transform system is called TF2

- ros transform <u>tree is made up of</u> frame that are <u>connected and defined by</u> transforms
- node can broadcast either static or dynamic transforms 

## boradcasting static transform (static_transform_publisher node)
`ros2 run tf2_ros static_transform_publisher <x> <y> <z> <yaw> <pitch> <roll> <parent_frame> <child_frame>`

### e.g.:
`ros2 run tf2_ros static_transform_publisher 2 1 0 0.785 0 0 world robot_1`
- robot_1 move reference to world

`ros2 run tf2_ros static_transform_publisher 1 0 0 0 0 0 robot_1 robot_2`
- robot_2 move reference to robot_1

## to visualize if above work use rviz2
`ros2 run rviz2 rviz2`

- click 'add' button in rviz2
- click 'TF' click 'ok'
- change fixed frame to 'world', 'robot_1', or 'robot_2'
