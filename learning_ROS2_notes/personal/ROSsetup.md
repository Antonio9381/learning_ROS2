# installation of ros2:

sudo apt install software-properties-common -y
  - sudo: run command as administrator
  - apt: is like winget for linux
  - software-properties-common: A utility package that lets Ubuntu manage additional software repositories because ROS isn't included in Ubuntu by default.

sudo add-apt-repository universe -y
  - repository is like software warehouse, and we are choosing the warehouse universe because the ros2 jazzy live in it

sudo apt install curl -y
  - curl: use to download things from the internet like downloading ros2, so you can use web link to download stuff to the computer

sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
-o /usr/share/keyrings/ros-archive-keyring.gpg
  - this download ros signing key, so we know ros is genuine
  - -sSL: s for silent / S for show error / L for follow redirect
  - -o: output location, saying saving the key in /usr/share/keyrings/ros-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
  - echo: print text on terminal
  - |: pipe operator saying output of the left side become the input of the right side
  - tee: Writes text into a file /etc/apt/sources.list.d/ros2.list This file tells Ubuntu where ROS packages live.

sudo apt update
  - refreshing the linus app store catalogue

sudo apt install ros-jazzy-desktop -y
  - download ros jazzy

echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
  - .bashrc: A script that runs every time a terminal opens.
  - source mean: Run a script in the current shell.
  - Where ROS is installed
  - Where ROS packages are
  - Which commands belong to ROS
  - Which libraries belong to ROS
  - without this ROS command won't work
