import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/awutio23/learnROS2/learning_ROS2/learn_ws/install/first_pkg'
