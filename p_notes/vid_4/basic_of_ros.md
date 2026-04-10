# basic of ros
## node
- node are lil component that can output stuff and do stuff
- to run node `ros2 run <package name> <node name>`

## topic
- topic is a communication system that node can subscribe and publish
- to see topic list `ros2 topic list` 
- to see a topic's data `ros2 topic echo <topic name (eg /scan)> --no-arr`
    - `--no-arr` is just saying don't print it as array 

## service 
- service is single msg request reply communication 
- see serice list `ros2 service list`
- to call service manually `ros2 service call <service name (eg /stop_motor)>`

## remapping & parameter 
- we do remapping if let's say one node is publishing onto a /scan but the expected recieving node is subscribing /laser_scan
- another time we might do remapping is when let's say we have two ladar, and both of them is publishing onto /scan. remapping allow us to change the name, so that one ladar can publish to /scan1 and another ladar can publish to /scan2.
- to remap: `ros2 run <pkg name> <node name> --ros-args -p serial_port:=/dev/ttyUSB0 -r scan:scan1`
    - `-p` for parameter
    - `-r` for remapping
- namespace: help us remap everything in a node to keep different nodes seperated
    - to run namespace (ns): `ros2 run <pkg name> <node name> --ros-args -p serial_port:=/dev/ttyUSB0 -r __ns:=scanner2`
    - basically namespace make a directory to store the parameter the nodes, so that it is display as /scanner1/scan, /scanner2/scan, /scanner3/scan and not /scan1, /scan2, /scan3