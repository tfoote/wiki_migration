# IMU Handler

In the folder imu_handler/modelVREP you will find the file IMU.ttt. It
is a model of the IMU sensor that you can attach to any object in the
scene.

When the plugin find an IMU sensor it publishes a message
sensor_msgs/Imu: orientation, angular velocity and specific
acceleration.
