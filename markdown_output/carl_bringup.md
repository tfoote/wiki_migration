## About

The `carl_bringup` package contains launch files for initializing all
of CARL's systems including CARL's segway base, CARL's sensors,
CARL's jaco manipulator, and CARL's robot description model. There are
currently 5 included launch files: arm.launch, base.launch,
robot_model.launch, sensors.launch, and carl_bringup.launch. Arm.launch
launches the jaco arm; base.launch launches the segway base;
robot_model.launch launches the urdf robot model; sensors.launch
launches the asus camera, hokuyo laser scanner, computer battery
monitor, sensor servos, and the top frame and base IMUs; and
carl_bringup.launch launches everything.

## Startup

The `carl_bringup.launch` file will start necessary nodes for running
CARL at a basic level. This includes the ROS wrapper for the arm,
interactive manipulation, the segway rmp control nodes, camera servo
control, teleoperation for the previous packages, launch files for each
camera, the robot model, and basic safety nodes. This is run as follows:

. 

```
roslaunch carl_bringup carl_bringup.launch
```



Individual modules of the CARL robot can also be launched using the
`arm.launch`, `base.launch`, and `sensors.launch` files for the
JACO arm, Segway RMP base, and ASUS and Creative depth sensors,
respectively. These are run with the following command (replace <module
name> with the desired module):

. 

```
roslaunch carl_bringup <module name>.launch
```



The `robot_model.launch` file will separately launch nodes required
for visualization of the robot, and can be run individually to provide
visualization for individual modules if the `carl_bringup.launch` file
is not used. This is run as follows: . 

```
roslaunch carl_bringup robot_model.launch
```



## Troubleshooting Sensors

### Asus

If problems with the asus occur, try manually installing the drivers:



```
git clone https://github.com/OpenNI/OpenNI.git
cd OpenNI/Platform/Linux/CreateRedist
./RedistMaker
cd ../Redist/OpenNI-Bin-Dev-Linux-x64-v1.5.7.10/
sudo ./install.sh
```

 If problems occur regarding failure to stat usb
device, disable xHCI and EHCI Hand-off in BIOS.

### Hokoyu

If there are issues with the hokoyo, try setting the permissions with:



```
sudo chmod a+rw /dev/ttyACM0
```

 Alternatively, add yourself to the group which
has rw access by default, then re-login:



```
sudo adduser $USER dialout
```



### Phidgets IMU

If a Phidgets IMU is not connecting properly, permissions may not be
correctly set. To use the Phidgets IMU as a user other than root, you
need to create a udev rule. Create a file called `99-phidgets.rules`,
with the following line:



```
SUBSYSTEMS=="usb", ACTION=="add", ATTRS{idVendor}=="06c2", ATTRS{idProduct}=="00[3-a][0-f]", MODE="666"
```



Copy this file into the `/etc/udev/rules.d` directory. You may need to
reboot your computer for this to take effect.
