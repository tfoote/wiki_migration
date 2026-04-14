## About

text_locator is a ROS package that can detect and recognize text in
images from the MS kinect / Asus Xtion sensors. Also, it can give you
spatial information about the text, ie. where the text is in the 3D
space, with respect to the sensor.

example usage video:

[Youtube](https://www.youtube.com/watch?v=nBe_H5m3WLs)

## Installation

Install the text_locator package from the github repo (see
[here](https://github.com/vonovak/text_locator/blob/master/README.md)).
Then download the CCV library from
[here](http://libccv.org/doc/doc-swt/), and compile it. The result will
be a static library file, libccv.a. Copy this file to the /lib folder of
the package.

To compile CCV, extract the tarball, cd to \[extractedCCV\]/lib folder,
run ./configure followed by make. When configuring, the \'swscale\' is
the only component that is needed. The other compilation options (enable
SSE2, use openmp etc..) are optional.

## Launching

Run

```
roslaunch text_locator text_locator.launch
``` The output of the node is advertised on
text_locator_topic.

## Documentation

More detailed documentation is included in the git repo\'s readme file
[here](https://github.com/vonovak/text_locator).
