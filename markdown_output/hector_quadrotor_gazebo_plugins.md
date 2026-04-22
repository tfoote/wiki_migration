## Available Plugins

### Barometer Plugin

This plugin simulates a sensor that measures the altitude of the vehicle
based on barometric pressure according to the International Standard
Atmosphere (ISA). See
<http://en.wikipedia.org/wiki/Atmospheric_pressure> for details.

#### Published Topics

-   `pressure_height`
    ([geometry_msgs/msg/PointStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PointStamped.html)):
    The z value of the Point contains the current altitude minus the
    configured elevation. x and y are always zero.

#### XML Parameters

-   `updateRate` (double): output rate of the sensor in milliseconds
-   `robotNamespace` (string): namespace prefix for topic names
-   `frameId` (string): frame_id included in the message header
-   `topicName` (string): name of the sensor output topic (defaults to
    `pressure_height`)

```{=html}
<!-- -->
```
-   `elevation` (double): elevation of the ground or zero for altitude
    above Mean Sea Level MSL (defaults to 0.0)
-   `qnh` (double): barometric pressure adjusted to sea level in
    hPa/mbar (defaults to standard pressure 1013.25 hPa, see
    <http://en.wikipedia.org/wiki/QNH>)

```{=html}
<!-- -->
```
-   `offset` (double): a constant offset added to the range
-   `drift` (double): standard deviation of the drift error
-   `driftFrequency` (double): mean frequency of the drift
-   `gaussianNoise` (double): standard deviation of the additive
    Gaussian noise

Notes:

-   [mav_msgs/msg/Height](https://docs.ros.org/en/rolling/p/mav_msgs/msg/Height.html)
    can be used as alternate message type if compiled with
    `-DUSE_MAV_MSGS`.
-   There is no direct output of the atmospheric pressure. The parameter
    `qnh` is currently unused.
-   The plugin uses the sensor error model from package
    [hector_gazebo_plugins](hector_gazebo_plugins).

### Simple Controller Plugin

The simple quadrotor plugin is a generic controller for quadrotors that
enables teleoperated flying in Gazebo. PID controllers are used to
control the velocities and yaw rate by calculating the necessary forces
and torques acting on the body. It is called "simple controller" as it
makes some assumptions that usually hold for quadrotors during hovering
and non-aerobatic maneuvers.

The controller uses a cascade of two PID controllers for the horizontal
movement and two separate PID controllers for the yaw rate and vertical
velocity.

The plugin currently does not provide position, heading or altitude
control. You can implement your own position controller on top of it.

#### Subscribed Topics

-   `cmd_vel`
    ([geometry_msgs/msg/Twist](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Twist.html)):
    The desired velocities and yaw rate of the quadrotor. The angular
    velocities around x- and y-axis are ignored.

#### XML Parameters

-   `updateRate` (double): update rate of the controller in Hz (should
    always be zero = simulation rate)
-   `robotNamespace` (string): namespace prefix for topic names
-   `bodyName` (string): name of the quadrotor body link in Gazebo
-   `topicName` (string): name of the twist command input topic
    (defaults to `cmd_vel`)
-   `imuTopic` (string): name of the imu topic
    ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html))
    to be subscribed and used as current orientation and angular rates
    source. If empty, ground truth information from Gazebo is used for
    control (default).
-   `stateTopic` (string): name of the state topic
    ([nav_msgs/msg/Odometry](https://docs.ros.org/en/rolling/p/nav_msgs/msg/Odometry.html))
    to be subscribed and used as current velocity and acceleration
    source. If empty, ground truth information from Gazebo is used for
    control (default).
-   `maxForce` (double): if greater than 0, upper limit of total
    thrust along the z-axis (defaults to unlimited)

### Quadrotor Propulsion Plugin / Quadrotor Aerodynamics Plugin

The propulsion and aerodynamics plugins simulate the propulsion system
(motors and propellers) and drag, respectively. They take the motor
voltages and the wind vector as input.

#### Subscribed Topics

-   `motor_pwm`
    ([hector_uav_msgs/msg/MotorPWM](https://docs.ros.org/en/rolling/p/hector_uav_msgs/msg/MotorPWM.html)):
    The commanded motor voltages for the four motors. The voltage is
    given as pulse width in the range of 0 to 255 (full battery
    voltage).
-   `wind`
    ([geometry_msgs/msg/Vector3](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Vector3.html)):
    You can specify a wind vector using this topic, which is substracted
    from the quadrotor's base velocity to calculate the drag forces.

#### Published Topics

-   `motor_status`
    ([hector_uav_msgs/msg/MotorStatus](https://docs.ros.org/en/rolling/p/hector_uav_msgs/msg/MotorStatus.html)):
    The simulated motor speeds and currents.
-   `wrench_out`
    ([geometry_msgs/msg/Wrench](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Wrench.html)):
    The resulting forces and moments generated by the propulsion system
    (for debugging purposes mainly).
-   `supply`
    ([hector_uav_msgs/msg/Supply](https://docs.ros.org/en/rolling/p/hector_uav_msgs/msg/Supply.html)):
    The simulated motor speeds and currents.

#### XML Parameters

-   `updateRate` (double): update rate of the controller in Hz (should
    always be zero = simulation rate)
-   `controlRate` (double): update rate of the controller rate in Hz.
    If greater than 0, the simulation will be throttled if new motor
    voltages arrive slower than this rate.
-   `controlDelay` (double): tolerance for the delay of the voltage
    timestamps compared to the simulation time
-   `robotNamespace` (string): namespace prefix for topic names
-   `bodyName` (string): name of the quadrotor body link in Gazebo
-   `voltageTopicName` (string): name of the motor voltage input topic
    (defaults to `motor_pwm`)
-   `statusTopic` (string): name of the motor status topic (defaults
    to `motor_status`)
-   `wrenchTopic` (string): name of the wrench output topic (defaults
    to `wrench_out`)

#### ROS Parameters

A bunch of parameters that describe the quadrotor model are loaded from
the ROS parameter server during plugin initialization.

#### Matlab Compilation

The differential equations that describe the quadrotor system are
implemented as Matlab scripts and compiled to C libraries using the
[Matlab Coder](http://www.mathworks.de/products/matlab-coder/) in
package [hector_quadrotor_model](hector_quadrotor_model). You need a
version of Matlab installed on your computer and available in the system
path to compile the model. Otherwise these plugins will not be
available.
