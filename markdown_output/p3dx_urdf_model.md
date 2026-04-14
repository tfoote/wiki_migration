\

This package is based on package [p2os_urdf](p2os-purdue). This package
contains URDF model of robot Pioneer3dx with laser scaner, 16 ultrasonic
sensors, 10 bumpers, gyroscope, accelerometer and camera. All names of
links contain special format of names which is decribed below. This URDF
file should be used with [V-REP](http://www.coppeliarobotics.com/) model
of Pioneer3dx found in
[our github](https://github.com/hrnr/robo-rescue-simulation-vrep) repo.

### NAMING CONVENTION

. Robot links use this naming convention: . FOR SENSORS: .
robot_id/node_name(category of sensors)/sensor + number from 0 to n
example: . 0/ultrasonicSensors/sensor0 FOR JOINTS (non fixed): .
robot_id/node_name(category e.g. arm,base)/joint + number from 0 to n
example: . 0/base/joint0 OTHER PARTS: . robot_id/part_name example: .
0/top_plate . Parameter robot_id is set in top level xacro script. It
must include / at the end of indetifier (robot_id=p3dx/) . This
parameter is NOT good substitution for tf_prefix. It should be used in
case there is need for specific namespace.
