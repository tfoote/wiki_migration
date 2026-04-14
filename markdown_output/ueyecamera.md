Maintainer: yogesh@cim.mcgill.ca

A ROS node for the uEye USB camera from IDS Imaging Development Systems.

The following parameters are supported:

\- cameraid: Sets the camera ID, 0 means the first available camera
(default = 0).

\- width: Width of the image (default = 640).

\- height: Height of the image (default = 480).

\- rate: Camera image publishing rate (default = 5 Hz).

\- left: If the image width is less than the max_width supported by the
sensor, then this parameter sets the left position of the image. If not
set, then the image is automatically positioned at the center of the
sensor.

\- top: If the image height is less than the max_height supported by the
sensor, then this parameter sets the top position of the image. If not
set, then image is automatically positioned at the center of the sensor.
