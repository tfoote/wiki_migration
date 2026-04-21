## Nodes

API below is for information purposes only. imu_monitor is only
supported to monitor PR2 imu



```clearsilver
node.0 {
  name=imu_monitor.py
  desc=The IMU Monitor, `imu_monitor.py`, monitors the drift on the IMU gyroscopes on the PR2. It detects when the PR2 base is not moving, and then start monitoring the drift of the gyroscopes around the vertical axis.
  pub{
    0.name= /diagnostics
    0.type= diagnostic_msgs/DiagnosticArray
    0.desc= Diagnostics about the status of the IMU drift.
  }
  sub{
    0.name= torso_lift_imu/data
    0.type= sensor_msgs/Imu
    0.desc= The IMU data (accelerometers, gyroscopes, etc)
    1.name= base_odometry/odometer
    1.type= pr2_mechanism_controllers/Odometer
    1.desc= The PR2 base odometry
  }
```


