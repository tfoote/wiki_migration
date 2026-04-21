<<MsgSrvDoc(carl_dynamixel)>>

## About

The `carl_dynamixel` package is a package which launches the correct
nodes and controllers from the 'dynamixel_motors' package. It also has
a sensor_msgs/JointState publisher.

## Nodes

```clearsilver
node.0 {
  name = back_joint_node
  desc = `back_joint_node` will take the position information and publish it as a 'sensor_msgs/JointState'
  sub {
    0.name = motor_states/back_port
    0.type = 'dynamixel_msgs/MotorStateList'
    0.desc = a list of the motor states connected to the dynamixelUSB controller.
  }
  pub {
    0.name = dynamixel_back
    0.type = 'sensor_msgs/JointState'
    0.desc = publishes the joint state information for all of the motors connected to the dynamixelUSB controller.
  }
  param {
    0.name = back_servos/num_servos
    0.type = `int`
    0.desc = number of servos connected to the dynamixelUSB
    1.name = back_servos/1/id
    1.type = `int`
    1.desc = the id number of the first servo connected
    2.name = back_servos/1/link_name
    2.type = `string`
    2.desc = the link_name number of the first servo connected
  }
}
node.1 {
  name = front_joint_node
  desc = `front_joint_node` will take the position information and publish it as a 'sensor_msgs/JointState'
  sub {
    0.name = motor_states/front_port
    0.type = 'dynamixel_msgs/MotorStateList'
    0.desc = a list of the motor states connected to the dynamixelUSB controller.
  }
  pub {
    0.name = dynamixel_front
    0.type = 'sensor_msgs/JointState'
    0.desc = publishes the joint state information for all of the motors connected to the dynamixelUSB controller.
  }
  param {
    0.name = front_servos/num_servos
    0.type = `int`
    0.desc = number of servos connected to the dynamixelUSB
    1.name = front_servos/1/id
    1.type = `int`
    1.desc = the id number of the first servo connected
    2.name = front_servos/1/link_name
    2.type = `string`
    2.desc = the link_name number of the first servo connected
  }
}
node.2 {
  name = servo_pan_tilt
  desc = `servo_pan_tilt` allows velocity-based panning and tilting for the servos.
  sub {
    0.name = asus_controller/tilt
    0.type = 'std_msgs/Float64'
    0.desc = Tilt command subscriber (rad/s) for the back servo (asus depth sensor mount).
  }
  sub {
    1.name = creative_controller/pan
    1.type = 'std_msgs/Float64'
    1.desc = Pan command subscriber (rad/s) for the front servo (creative depth sensor mount).
  }
  sub {
    2.name = dynamixel_back
    2.type = 'sensor_msgs/JointState'
    2.desc = Joint state updates for the back servo.
  }
  sub {
    3.name = dynamixel_front
    3.type = 'sensor_msgs/JointState'
    3.desc = Joint state updates for the front servo.
  }
  pub {
    0.name = asus_controller/command
    0.type = 'std_msgs/Float64'
    0.desc = Position command (rad) for the back servo (asus depth sensor mount).
  }
  pub {
    1.name = creative_controller/command
    1.type = 'std_msgs/Float64'
    1.desc = Position command (rad) for the front servo (creative depth sensor mount).
  }
  srv {
    0.name = asus_controller/look_at_point
    0.type = carl_dynamixel/LookAtPoint
    0.desc = Center asus camera on a given point.
  }
  srv {
    1.name = asus_controller/look_at_frame
    1.type = carl_dynamixel/LookAtFrame
    1.desc = Center asus camera on a given coordinate frame.
  }
}
```

## Installation

### Source

To install from source, execute the following: ```shell
cd /path/to/your/catkin/workspace/src
git clone https://github.com/WPI-RAIL/carl_bot.git
cd /path/to/your/catkin/workspace
catkin_make 
catkin_make install
```

### Ubuntu Package

To install the Ubuntu package, execute the following:
```
sudo apt-get install ros-indigo-carl-bot
```

### Startup

The `carl_dynamixel` package contains a `carl_servos.launch` This
file launches an instance of the `dynamixel_manager` and
`tilt_controller_spawner` nodes from the 'dynamixel_motor'
metapackage. It also launches the 'back_joints_node' and
`front_joints_node`, as well as the `servo_pan_tilt` node for
velocity commands. To launch these nodes, the following command can be
used:

. ```
roslaunch carl_dynamixel carl_servos.launch
```

Once this launches the following topics becomes available:

```clearsilver
node.0 {
  name = Available Topics
  desc = the topics to which the launch files publishes and subscribes.
pub {
    0.name = motor_states/back_port
    0.type = 'dynamixel_msgs/MotorStateList'
    0.desc = a list of the motor states connected to the dynamixelUSB controller at back of robot.
    1.name = motor_states/front_port
    1.type = 'dynamixel_msgs/MotorStateList'
    1.desc = a list of the motor states connected to the dynamixelUSB controller at front of robot.
    2.name = asus_controller/state
    2.type = 'dynamixel_msgs/JointState'
    2.desc = information about the servo associated with the asus_controller
    3.name = creative_controller/state
    3.type = 'dynamixel_msgs/JointState'
    3.desc = information about the servo associated with the creative_controller
  }
sub {
    0.name = asus_controller/command
    0.type = 'std_msgs/Float64'
    0.desc = the command in radians to which the servo on the asus_controller should go. 0 radians = 512 out of the possible 1023. Commands range from -2.618 to 2.618 when the servo can traverse its full range.
    1.name = creative_controller/command
    1.type = 'std_msgs/Float64'
    1.desc = the command in radians to which the servo on the asus_controller should go. 0 radians = 512 out of the possible 1023. Commands range from -2.618 to 2.618 when the servo can traverse its full range.
    2.name = asus_controller/tilt
    2.type = 'std_msgs::Float64'
    2.desc = Velocity command (rad/s) to move the back servo.
    3.name = creative_controller/pan
    3.type = 'std_msgs::Float64'
    3.desc = Velocity command (rad/s) to move the front servo.
  }
}
```

## Expansion

This package can support up to 5 servos per USB device.

### Wiring

To add a servo to the USB device simply attach the 3-pin wire, on the
right connector of the servo, to an open connector on the power
distribution board.

### Code

To make sure the newly attached servo has its 'sensor_msgs/JointState'
published and that it can be controlled a controller and the joint state
information needs to be added.

#### Controller

Just by attaching the servo, some information will automatically be
published to the 'motor_states/<port>' topic, where the port is the
specific USBDynamixel it is plugged into. To make sure the servo can be
moved a YAML file needs to be made. Copy and paste the following code
into carl_dynamixel/config/example.yaml

```
example_controller:
    controller:
        package: dynamixel_controllers
        module: joint_position_controller
        type: JointPositionController
    joint_name: example_joint
    joint_speed: 0.5
    motor:
        id: 1
        init: 512
        min: 0
        max: 1023
```

The id for the servo can be found from the 'motor_states/<port>'
topic

Now add to the launch file: ```
<!-- Start example joint controller -->
    <rosparam file="$(find carl_dynamixel)/config/example.yaml" command="load"/>
    <node name="example_controller_spawner" pkg="dynamixel_controllers" type="controller_spawner.py"
          args="--manager=dxl_manager
                --port back_port
                example_controller"
          output="screen"/>
```

Now launch the file and the new servo should have specific joint
information published on the 'example_controller/state' topic and
publishing a Float64 to the 'example_controller/command' will move the
servo to that position.

#### Joint State

Joint state publishers are already set up, however, to add a new servo
the following lines need to be added to either back_servos.yaml or
front_servos.yaml depending on which USB port they are plugged into.

```
"2": 
    id: 2
    link_name: joint_2
```

Also the variable num_servos should be changed to match the number of
servos.

The following is an example of the modified back_servos.yaml file.

```
back_servos: 
   num_servos: 3
   "1": 
    id: 1
    link_name: asus_servo_asus_servo_arm_joint 
   "2": 
    id: 2
    link_name: joint_2
   "3": 
    id: 12
    link_name: joint_3
```

## Support

Please send bug reports to the
[GitHub Issue Tracker](https://github.com/WPI-RAIL/rovio/issues). Feel
free to contact me at any point with questions and comments.

-   [Russell Toris](Russell Toris)
-   rctoris@wpi.edu
-   [Academic Website](http://users.wpi.edu/~rctoris/)
