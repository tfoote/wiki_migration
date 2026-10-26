The [cob_base_velocity_smoother](cob_base_velocity_smoother) package
provides two implementations for a velocity smoother that both read
velocity messages (geometry_msgs::Twist) and then publish messages of
the same type for "smoothed" velocity to avoid jerky behavior.

The two nodes available are:

- `cob_base_velocity_smoother`
- `velocity_smoother`

## Hardware Requirements

To use this package you either need a real or a simulated Care-O-Bot
(see [cob_bringup](cob_bringup) and [cob_bringup_sim](cob_bringup_sim)
respectively).

## ROS API

The following states the ROS API for the `cob_base_velocity_smoother`
node.



```clearsilver
 name = cob_base_velocity_smoother
 desc = The `cob_base_velocity_smoother` node takes in [[http://ros.org/doc/api/geometry_msgs/html/msg/Twist.html|geometry_msgs/Twist]] messages from the navigation or teleoperation device and publishes recalculated [[http://ros.org/doc/api/geometry_msgs/html/msg/Twist.html|geometry_msgs/Twist]] messages to avoid jerky behavior.

sub{
 0.name = input
 0.type = geometry_msgs/Twist
 0.desc = movement command published by the navigation or teleoperation device.
}

pub{
 0.name = output
 0.type = geometry_msgs/Twist
 0.desc = recalculated movement command
}

param{
 0.name = ~circular_buffer_capacity
 0.type = int
 0.default = 12 for cob3, 6 for raw3
 0.desc = Specifies the capacity of the internal circular buffer (number of saved velocity messages).

 1.name = ~maximal_time_delay
 1.type = double
 1.default = 4.0 [seconds]
 1.desc = Specifies the maximal time delay for saved messages (older messages will be deleted).

 2.name = ~thresh_max_acc
 2.type = double
 2.default = 0.02 [m/s^2]
 2.desc = Specifies the threshold for the maximal allowed acceleration.

 3.name = ~loop_rate
 3.type = double
 3.default = 30.0 [Hz]
 3.desc = Specifies the ros loop rate of the velocity smoother.

 4.name = ~min_input_rate
 4.type = double
 4.default = 9.0 [Hz]
 4.desc = Specifies the minimal input rate that is expected before filling the buffer with zeros.

 5.name = ~maximal_time_delay_to_stop
 5.type = double
 5.default = 0.1 [seconds]
 5.desc = Specifies the maximal time-delay until stopping the robot when there are no incoming messages.

}
```



## Usage

All hardware configuration is done in the
[cob_hardware_config](cob_hardware_config) package. Parameter files for
both nodes have to be placed in "cob_hardware_config/\$(env
ROBOT)/config/" for each ROBOT.
