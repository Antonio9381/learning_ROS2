# Linux Directory Structure (Ubuntu / WSL)

When you open WSL and browse to:

```text
\\wsl.localhost\Ubuntu-24.04\
```

or

```bash
cd /
```

you are at the Linux filesystem root.

Think of `/` as the Linux equivalent of `C:\` on Windows.

---

# Directory Overview

```text
/
├── bin
├── boot
├── dev
├── etc
├── home
├── lib
├── media
├── mnt
├── opt
├── proc
├── root
├── run
├── snap
├── srv
├── sys
├── tmp
├── usr
└── var
```

---

# /home

User files and personal directories.

Equivalent:

```text
Windows:
C:\Users\<username>

Linux:
/home/<username>
```

Example:

```text
/home/awooo23
├── Documents
├── Downloads
├── ros2_ws
└── Projects
```

Commands:

```bash
cd ~
pwd
```

Output:

```text
/home/awooo23
```

For ROS development, most of your work should live here.

Example:

```bash
mkdir -p ~/ros2_ws/src
```

---

# /mnt

Mounted drives.

Used to access Windows drives from Linux.

Examples:

```text
/mnt/c = C:\
/mnt/d = D:\
/mnt/e = E:\
```

Example:

```bash
cd /mnt/c/Users/awooo/Desktop
```

Equivalent:

```text
C:\Users\awooo\Desktop
```

Useful for:
- Accessing Windows files
- Copying files between Linux and Windows

Not recommended for:
- ROS workspaces
- Large software builds

---

# /etc

System configuration files.

Think:

```text
Windows Registry
+
System Settings
```

Examples:

```text
/etc/hosts
/etc/passwd
/etc/apt
```

Common uses:

```bash
cat /etc/os-release
```

Contains Ubuntu version information.

---

# /usr

Installed programs and libraries.

Equivalent:

```text
C:\Program Files
```

Contains:

```text
/usr/bin
/usr/lib
/usr/share
```

Examples:

```bash
which python3
```

Output:

```text
/usr/bin/python3
```

---

# /opt

Optional software packages.

Many large applications install here.

ROS installs into:

```text
/opt/ros/jazzy
```

Example:

```bash
ls /opt/ros
```

Output:

```text
jazzy
```

Important ROS command:

```bash
source /opt/ros/jazzy/setup.bash
```

---

# /bin

Essential Linux commands.

Contains commands such as:

```text
ls
cp
mv
rm
cat
pwd
```

Example:

```bash
which ls
```

Output:

```text
/usr/bin/ls
```

Historically these commands lived in /bin.

---

# /boot

Files needed to start Linux.

Contains:

```text
Linux kernel
Bootloader files
Startup files
```

Normally you never modify anything here.

---

# /dev

Devices represented as files.

Linux treats hardware like files.

Examples:

```text
/dev/ttyUSB0
/dev/null
/dev/sda
```

ROS users often encounter:

```text
/dev/ttyUSB0
/dev/ttyACM0
```

for:

- STM32
- Arduino
- LiDAR
- GPS
- Serial devices

Example:

```bash
ls /dev/tty*
```

---

# /proc

Virtual filesystem showing running system information.

Examples:

```bash
cat /proc/cpuinfo
```

Shows CPU information.

```bash
cat /proc/meminfo
```

Shows RAM information.

Files here are generated dynamically.

---

# /sys

Kernel and hardware information.

Used for:

- Drivers
- Hardware management
- Device configuration

Usually not touched by beginners.

---

# /tmp

Temporary files.

Equivalent:

```text
Windows:
%TEMP%
```

Anything here can be deleted automatically.

Example:

```bash
cd /tmp
```

Useful for:
- Downloads
- Testing scripts
- Temporary builds

---

# /var

Variable data.

Contains:

```text
Logs
Package cache
Databases
```

Examples:

```text
/var/log
/var/cache
```

Useful command:

```bash
sudo tail /var/log/syslog
```

View system logs.

---

# /root

Administrator account home directory.

Equivalent:

```text
Windows Administrator
```

Example:

```text
/root
```

Normal users should not store files here.

---

# /run

Temporary runtime information.

Stores:

```text
Process information
System services
Sockets
```

Automatically recreated after reboot.

---

# /media

Removable storage devices.

Examples:

```text
USB drives
External hard drives
SD cards
```

Example:

```text
/media/awooo23/USB_DRIVE
```

---

# /srv

Service data.

Used by:

```text
Web servers
FTP servers
Network services
```

Most desktop users never touch this.

---

# /snap

Applications installed using Snap.

Examples:

```bash
snap list
```

Typical programs:

```text
Discord
VSCode
Firefox
```

---

# ROS Workspace Structure

Recommended ROS location:

```text
/home/awooo23/ros2_ws
├── src
├── build
├── install
└── log
```

Meaning:

```text
src      = Source code
build    = Temporary build files
install  = Built packages
log      = Build logs
```

Create it:

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
```

Verify:

```bash
pwd
```

Output:

```text
/home/awooo23/ros2_ws
```

This is where your ROS projects should live.
