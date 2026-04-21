## Overview

The AWS [DeepRacer](https://www.amazon.com/dp/B07JMHRKQG) vehicle is a
1/18th scale RC car that can drive itself using a reinforcement learning
model. The vehicle comes with six sample
[projects](https://aws.amazon.com/deepracer/robotics-projects) and
open-source device software, providing developers with the opportunity
to prototype robotics applications for use with AWS
[DeepRacer](https://www.amazon.com/dp/B07JMHRKQG) hardware.

The AWS [DeepRacer](https://www.amazon.com/dp/B07JMHRKQG) comes with all
required libraries and packages preinstalled. The vehicle\'s device
software includes **Ubuntu 20.04 Focal Fossa**, **Intel® OpenVINO™
toolkit 2021.1.110**, **ROS 2 Foxy Fitzroy**, and **Python 3.8**.

The
[DeepRacer Launcher ROS package](https://github.com/aws-deepracer/aws-deepracer-launcher)
launches all required AWS
[DeepRacer](https://www.amazon.com/dp/B07JMHRKQG) core application
nodes, including those for perception, decision, navigation, and
application support. For more information about the AWS
[DeepRacer](https://www.amazon.com/dp/B07JMHRKQG) core application and
components, refer to information
[here](https://github.com/aws-deepracer/aws-deepracer-launcher).

### License

The source code is released under
[Apache 2.0](https://aws.amazon.com/apache-2-0/).

### Supported ROS Distributions

-   Foxy

## Software

The AWS [DeepRacer](https://www.amazon.com/dp/B07JMHRKQG) device with
the upgraded OpenSource software contains the following:

1\. **ROS 2 Foxy and dependencies**: ROS 2 Foxy (**ros-foxy-desktop**),
CV Bridge (**ros-foxy-cv-bridge**), image transport
(**ros-foxy-image-transport**), standard messages
(**ros-foxy-std-msgs**), and sensor messages (**ros-foxy-sensor-msgs**)
are installed on the [DeepRacer](https://www.amazon.com/dp/B07JMHRKQG)
device.

2\. **Intel OpenVino toolkit and its dependencies:** Intel OpenVino
toolkit (**intel-openvino-dev-ubuntu20-2021.1.110**) and its
dependencies are preinstalled on the AWS DeepRacer device. The AWS
[DeepRacer](https://www.amazon.com/dp/B07JMHRKQG) core application uses
Intel OpenVino to optimize reinforcement learning models and run
inference on them.

3\. **Tensorflow:** A custom built **Tensorflow v2.4.0** wheel with no
AVX support is installed on the AWS
[DeepRacer](https://www.amazon.com/dp/B07JMHRKQG) device.

4\. **AWS DeepRacer Debian packages**: 1.
**aws-deepracer-sample-models**: This package installs three sample
models deployed by default on the AWS DeepRacer device. 2.
**aws-deepracer-util**: This package installs utility scripts required
by the AWS DeepRacer core application. 3.
**aws-deepracer-device-console**: This package installs the UI component
of the AWS DeepRacer device console. 4. **aws-deepracer-core**: This
package installs all ROS 2 Foxy packages required for AWS
[DeepRacer](https://www.amazon.com/dp/B07JMHRKQG) core application
functionality.

## AWS DeepRacer Core Components

The AWS [DeepRacer](https://www.amazon.com/dp/B07JMHRKQG) application
includes packages for perception, decision, navigation, and application
support.

### Perception

Use these nodes to enable the AWS DeepRacer device\'s use of sensors for
perceiving its environment.

-   [camera_node](https://github.com/aws-deepracer/aws-deepracer-camera-pkg):
    This node reads and publishes data from the camera.
-   [sensor_fusion_node](https://github.com/aws-deepracer/aws-deepracer-sensor-fusion-pkg):
    This node combines and publishes camera and LiDAR data (if a LiDAR
    sensor is installed) as a single message.

### Decision

Use this node to determine the actions the AWS DeepRacer device should
perform based on the data it perceives.

-   [inference_node](https://github.com/aws-deepracer/aws-deepracer-inference-pkg):
    This node runs inference on the perceived data using the selected
    machine learning model.

### Navigation

Use these nodes to enable the vehicle\'s use of its motor and hardware
to move through the environment.

-   [deepracer_navigation_node](https://github.com/aws-deepracer/aws-deepracer-navigation-pkg):
    This node collects model inference results and publishes a servo
    message with throttle and steering angle values based on the action
    space for the selected machine learning model.
-   [servo_node](https://github.com/aws-deepracer/aws-deepracer-servo-pkg):
    This node maps the input servo throttle and servo angle ratios to
    raw PWM values that set on the servo or motor to move the vehicle.

### Application Support

Use these nodes to support core application functionality.

-   [ctrl_node](https://github.com/aws-deepracer/aws-deepracer-ctrl-pkg):
    As the main node, this exposes services used by backend webserver
    API calls.
-   [software_update_node](https://github.com/aws-deepracer/aws-deepracer-systems-pkg):
    This node is responsible for the software update system managing the
    following packages: **aws-deepracer-core**, **aws-deepracer-util**,
    **aws-deepracer-sample-models**, and **aws-deepracer-webserver**.
-   [model_loader_node](https://github.com/aws-deepracer/aws-deepracer-systems-pkg):
    This node is responsible for extracting tar.gz model files from USB
    and those uploaded from the console.
-   [otg_control_node](https://github.com/aws-deepracer/aws-deepracer-systems-pkg):
    This node is responsible for enabling and disabling the OTG
    connection and publishing the connection status.
-   [network_monitor_node](https://github.com/aws-deepracer/aws-deepracer-systems-pkg):
    This node is responsible for connecting to WiFi based on the
    configuration file on USB and communicating the network connection
    status.
-   [device_info_node](https://github.com/aws-deepracer/aws-deepracer-device-info-pkg):
    This node provides hardware and software version information.
-   [battery_node](https://github.com/aws-deepracer/i2c_pkg): This node
    reads and publishes vehicle battery level information.
-   [model_optimizer_node](https://github.com/aws-deepracer/aws-deepracer-model-optimizer-pkg):
    This node runs the model optimizer on the selected machine learning
    model.
-   [status_led_node](https://github.com/aws-deepracer/aws-deepracer-status-led-pkg):
    This node controls blinking and solid light functionality for the
    status LEDs found on the side of the AWS
    [DeepRacer](https://www.amazon.com/dp/B07JMHRKQG) device.
-   [usb_monitor_node](https://github.com/aws-deepracer/aws-deepracer-usb-monitor-pkg):
    This node monitors USB connections and publishes a notification if a
    required file is found.
-   [webserver_publisher_node](https://github.com/aws-deepracer/aws-deepracer-webserver-pkg):
    This node is a collection of FLASK APIs called from the front end.
    These APIs call ROS services and return results to the front end.
