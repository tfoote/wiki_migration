## About

The \`carl_tools\` package contains miscellaneous functionality and
tools for the CARL robot. This currently includes an automatic
calibration system for the transforms between CARL\'s sensors and their
respective mounts, and an arm current logger.

## Nodes

```clearsilver
node.0 {
  name = camera_external_calibration
  desc = This node automatically determines transformations between CARL's depth sensors and their respective mounts.
  sub {
    0.name = asus_marker_tracker/ar_pose_marker
    0.type = ar_track_alvar_msgs/AlvarMarkers
    0.desc = AR marker poses detected from the Asus camera.
  }
  pub {
    0.name = asus_controller/command
    0.type = std_msgs/Float64
    0.desc = Send position commands to the Asus servo controller.
  }
  param {
    0.name = calibration_marker_id
    0.type = int
    0.desc = ID number for the calibration AR marker.
    0.default = 200
  }
}
node.1 {
  name = current_logger
  desc = Log currents on the JACO arm and finger joints to a text file.
  sub {
    0.name = jaco_arm/joint_states
    0.type = sensor_msgs/JointState
    0.desc = Arm joint states.
  }
  param {
    0.name = filename
    0.type = string
    0.desc = Name of file to save currents to.  If the file already exists, it new current readings will be appended to the end of the file, otherwise it will create the file.
    0.default = "arm_currents.txt"
  }
```

## Installation

To install the \`carl_bot\` package, you can install from source with
the following commands: . ```shell
cd /(your catkin workspace)/src
git clone https://github.com/WPI-RAIL/carl_bot.git
cd ..
catkin_make
catkin_make install
```

## Startup

External camera calibration can be started with the following launch
command: . ```
roslaunch carl_tools camera_external_calibration.launch
``` Optionally, an rviz interface for
visualizing the calibration process and final calculated transforms can
be launched with: . ```
roslaunch carl_tools view_calibration.launch
``` Current logging can be
started by running the current_logger node, with an optional parameter
for the output file name (replace \<output_filename\>), and it will
continue to log currents until the node is terminated. .
```
rosrun carl_tools current_logger _filename:=<output_filename>
```

## Calibration Procedure

To calibrate the cameras, first make sure a unique AR tag is placed in a
known location with respect to the robot. By default, the calibration
node expects a maximum size (12 cm) AR marker with ID 200 centered on
the screw holes of CARL\'s top plate. Once this marker is placed and
unobstructed, simply launch the calibration node and wait. When the
transform is calculated, further instructions will be provided in the
terminal where the node was launched.
