A ROS package for the Arduino Nicla Vision board

## Description

This ROS package enables the
[Arduino Nicla Vision](https://docs.arduino.cc/hardware/nicla-vision/)
board to be ready-to-use in the ROS world!

The implemented architecture is described in the above image: the
Arduino Nicla Vision board streams the sensors data to a ROS-running
machine through TCP/UDP socket. This package will be running on the
ROS-running machine, allowing to deserialize the received info, and
stream it in the corresponding ROS topics

Here a list of the available sensors with their respective ROS topics:

-   **2MP color camera** streams on
-   `/nicla/camera/camera_info`
-   `/nicla/camera/image_raw`
-   `/nicla/camera/image_raw/compressed`
-   **Time-of-Flight (distance) sensor** streams on:
-   `/nicla/tof`
-   **Microphone** streams on:
-   `/nicla/audio`
-   `/nicla/audio_info`
-   `/nicla/audio_stamped`
-   `/nicla/audio_recognized`
-   **Imu** streams on:
-   `/nicla/imu`

The user can easily configure this package, by launch parameters, to
receive sensors data via either UDP or TCP socket connections,
specifying also the socket IP address. Moreover, the user can decide
which sensor to be streamed within the ROS environment. In this
repository you can find the Python code optimised for receiving the data
by the board, and subsequently publishing it through ROS topics.

## Package List

-   [Nicla Vision Drivers repository](https://github.com/ADVRHumanoids/nicla_vision_drivers.git)
-   [Nicla Vision ROS repository](https://github.com/ADVRHumanoids/nicla_vision_ros.git)
-   [Nicla Vision ROS2 repository](https://github.com/ADVRHumanoids/nicla_vision_ros2.git)

## License

Distributed under the Apache-2.0 License. See LICENSE for more
information.

## Citation

If you use this work or take inspiration from it, please cite
(publication in progress)

------------------------------------------------------------------------

Check full information
[here](https://github.com/ADVRHumanoids/nicla_vision_ros)
