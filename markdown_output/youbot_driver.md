## About

This package contains the drivers for the Kuka youBot. This is required
for [youbot_oodl](youbot_oodl). It is recommended to use
[youbot_oodl](youbot_oodl) instead of this package for any real
application.

## Installation

### Debian

Install the debian package using `apt-get`: ```
sudo apt-get install ros-groovy-youbot-driver
```
This will install the code, set the permissions of the binaries, copy
the config files to a set location, and install the `udev` rules for
the Hokuyo sensor. You must set the environment variable
YOUBOT_CONFIG_FOLDER_LOCATION to point to the config folder before
running the package. The debian install will have put it at
/opt/ros/groovy/etc/youbot_driver/config/, so set the variable to that.
```
export YOUBOT_CONFIG_FOLDER_LOCATION=/opt/ros/groovy/etc/youbot_driver/config/
``` If you do not wish to do this every time you
start a new terminal, you can put that line in `.bashrc` in the home
directory, `/.bashrc`. That way, the variable will be defined for
every terminal you start.

### From Source

#### Download and Make

To install from source, get the package from the git repository in the
typical way. First, create a folder for the package within the `src`
folder of your catkin workspace. `cd` to the folder, then do
```
git init
git pull http://github.com/WPI-RAIL/youbot_driver.git
``` Go to the root of your catkin workspace and
make it. ```
catkin_make
```

#### Set Capabilities of Binaries

The binaries need to have the proper capabilites to run. If they do not
have the right permissions, they will be unable to communicate over
Ethercat, and the drivers will not run. To set the capabilities to their
proper values, use `setcap` on each binary: ```
sudo setcap cap_net_raw+ep [your_catkin_workspace]/devel/lib/youbot_driver/base_arm_gripper_test
sudo setcap cap_net_raw+ep [your_catkin_workspace]/devel/lib/youbot_driver/displayIpAddress
```

#### Config File Location Variable

You must set the environment variable YOUBOT_CONFIG_FOLDER_LOCATION to
point to the config folder before running the package. The config folder
can be found right in the source folder for the package.
```
export YOUBOT_CONFIG_FOLDER_LOCATION=[your_catkin_workspace]/src/youbot_driver/config
``` If you do not wish to do this every time you
start a new terminal, you can put that line in `.bashrc` in the home
directory, `/.bashrc`. That way, the variable will be defined for
every terminal you start.

#### Hokuyo UDEV Rule

Finally, you should also install the `udev` rules for the Hokuyo
sensor. These are important for any other youBot packages which use the
Hokuyo, such as [youbot_navigation](youbot_navigation). These rules do
two things whenever you plug in the Hokuyo: 1.Set the permissions of the
Hokuyo's usb channel to have public read and write access. 2.Create a
symbolic link at `/dev/sensors/hokuyo` to whichever usb channel the
sensor was plugged into, usually `/dev/ttyACM0` or `/dev/ttyACM1`.
To install the rules, copy the `47-hokuyo.rules` file from the
udev_rules folder included in the source to /etc/udev/rules.d/
```
sudo cp [your_catkin_workspace]/src/youbot_driver/udev_rules/47-hokuyo.rules /etc/udev/rules.d/
```

### Verifying the Hokuyo udev rules

If you wish to confirm that the rules work, run `udevadm monitor` and
plug in the Hokuyo. The output should reflect the fact that the port has
been given read and write access and a symbolic link in
`/dev/sensors/hokuyo` was created. You may also do
```
ls -all /dev/sensors/hokuyo
``` to check. If the rules are not installed
properly, the file will not exist or will not have public read and write
access. If the rules are working properly, it should look like this:
```
lrwxrw-rw- 1 root root 11 Jun 11 11:11 /dev/sensors/hokuyo -> ../ttyACM0
```

## Using this Package

It is recommended to use [youbot_oodl](youbot_oodl) instead of this
package for any actual application. You can test the base, arm, and
gripper motors by running the base_arm_gripper_test. Be sure to have the
robot off the ground because it will move around some while testing the
base. ```
rosrun youbot_driver base_arm_gripper_test
``` If this fails with the message that there
was no socket connection on `eth1` or `eth0`, go into the
`youbot-ethercat.cfg` config file and change `EthernetDevice` to
`eth0` or `eth1`.

There is also a program to write the youBot's IP Address to its LCD
display through a serial connection. You must give it the serial port
through which it is connected, the ethercat connection it should use to
communicate to the arm, and the name of its connection to the network.
For example: ```
export YOUBOT_CONFIG_FOLDER_LOCATION=/opt/ros/groovy/etc/youbot_driver/config/
```0

------------------------------------------------------------------------

  -- ------------------------------------------------- -- ---------- -- -------------------------- --
     <tablewidth="100%"> ![](attachment:wpi.png)      <:99%>      ![](attachment:rail.png)   
  -- ------------------------------------------------- -- ---------- -- -------------------------- --
