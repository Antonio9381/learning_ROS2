```
cd ~/Documents/ROS2/dir2026/learnROS2/ros2_ws/src/learning_ROS2/learn_ws/src
ros2 pkg create vid07_something --build-type ament_python --dependencies rclpy std_msgs
```
  - whenever new video or new pkg need to be created do it in the thing

__________________________________________________________________________________________________________

```
mkdir -p snapshots
```
- create directory for snapshot

```
tar --exclude='build' --exclude='install' --exclude='log' \ -czf snapshots/learnROS2_source_snapshot_$(date +%Y-%m-%d_%H-%M-%S).tar.gz learnROS2
```
- create snap shot

```
ls -lh snapshots
```
- check for snapshot

_________________________________________________________________________________________________________

```
cd ~/Documents/ROS2/dir2026/learnROS2/ros2_ws/src/learning_ROS2/learn_ws
colcon build
source install/setup.bash
```
