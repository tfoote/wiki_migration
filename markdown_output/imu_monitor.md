## Nodes

API below is for information purposes only. imu_monitor is only
supported to monitor PR2 imu

### imu_monitor.py

The IMU Monitor, `imu_monitor.py`, monitors the drift on the IMU
gyroscopes on the PR2. It detects when the PR2 base is not moving, and
then start monitoring the drift of the gyroscopes around the vertical
axis.

#### Subscribed Topics

- `torso_lift_imu/data`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  The IMU data (accelerometers, gyroscopes, etc)
- `base_odometry/odometer`
  ([pr2_mechanism_controllers/msg/Odometer](https://docs.ros.org/en/rolling/p/pr2_mechanism_controllers/msg/Odometer.html)):
  The PR2 base odometry

#### Published Topics

- `/diagnostics`
  ([diagnostic_msgs/msg/DiagnosticArray](https://docs.ros.org/en/rolling/p/diagnostic_msgs/msg/DiagnosticArray.html)):
  Diagnostics about the status of the IMU drift.
