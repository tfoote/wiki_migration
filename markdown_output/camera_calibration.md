This package uses OpenCV camera calibration, described
[here](http://docs.opencv.org/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html).
For detailed information on the parameters produced by the calibration,
see [this description](image_pipeline/CameraInfo).

The code API listed for this package is for convenience only. This
package has no supported code API.

For pinhole type cameras this package names the distortion model as
\'\'\'plumb_bob\'\'\' or \'\'\'rational_polynomial\'\'\', depending on
number of parameters used. See
[documentation](http://docs.ros.org/melodic/api/sensor_msgs/html/distortion__models_8h.html)

Support for fisheye type of camera introduced in melodic.

For fisheye type cameras this package uses \'\'\'equidistant\'\'\'
distortion model but names it as \'\'\'fisheye\'\'\'.

For fisheye type cameras this package uses \'\'\'equidistant\'\'\'
distortion model with the name \'\'\'equidistant\'\'\', according to
[documentation](http://docs.ros.org/melodic/api/sensor_msgs/html/distortion__models_8h.html).

## Supported hardware

\`camera_calibration\` will work with any camera driver node satisfying
the standard ROS camera interface. See the
[image_pipeline hardware requirements](image_pipeline#Hardware_Requirements).

## Tutorials

There are tutorials on how to run the calibration tool for
[monocular](camera_calibration/Tutorials/MonocularCalibration) and
[stereo](camera_calibration/Tutorials/StereoCalibration) cameras.

## Usage

### Camera Calibrator

To run the \`cameracalibrator.py\` node for a monocular camera using an
8x6 chessboard with 108mm squares:

```
rosrun camera_calibration cameracalibrator.py --size 8x6 --square 0.108 image:=/my_camera/image camera:=/my_camera
``` When you click on the \"Save\" button after a
succesfull calibration, the data (calibration data and images used for
calibration) will be written to /tmp/calibrationdata.tar.gz.

To run the \`cameracalibrator.py\` node for a stereo camera:

```
rosrun camera_calibration cameracalibrator.py --size 8x6 --square 0.108 right:=/my_stereo/right/image_raw left:=/my_stereo/left/image_raw left_camera:=/my_stereo/left right_camera:=/my_stereo/right
``` \`cameracalibrator.py\` supports the following
options:

```
Chessboard Options:
    You must specify one or more chessboards as pairs of --size and
    --square options.

    -p PATTERN, --pattern=PATTERN
                        calibration pattern to detect - 'chessboard',
                        'circles', 'acircles'
    -s SIZE, --size=SIZE
                        chessboard size as NxM, counting interior corners
                        (e.g. a standard chessboard is 7x7)
    -q SQUARE, --square=SQUARE
                        chessboard square size in meters

  ROS Communication Options:
    --approximate=APPROXIMATE
                        allow specified slop (in seconds) when pairing images
                        from unsynchronized stereo cameras
    --no-service-check  disable check for set_camera_info services at startup

  Calibration Optimizer Options:
    --fix-principal-point
                        fix the principal point at the image center
    --fix-aspect-ratio  enforce focal lengths (fx, fy) are equal
    --zero-tangent-dist
                        set tangential distortion coefficients (p1, p2) to
                        zero
    -k NUM_COEFFS, --k-coefficients=NUM_COEFFS
                        number of radial distortion coefficients to use (up to
                        6, default 2)
```

cameracalibrator.py supports the following options:
```
Chessboard Options:
    You must specify one or more chessboards as pairs of --size and
    --square options.

    -p PATTERN, --pattern=PATTERN
                        calibration pattern to detect - 'chessboard',
                        'circles', 'acircles'
    -s SIZE, --size=SIZE
                        chessboard size as NxM, counting interior corners
                        (e.g. a standard chessboard is 7x7)
    -q SQUARE, --square=SQUARE
                        chessboard square size in meters

  ROS Communication Options:
    --approximate=APPROXIMATE
                        allow specified slop (in seconds) when pairing images
                        from unsynchronized stereo cameras
    --no-service-check  disable check for set_camera_info services at startup
    --queue-size=QUEUE_SIZE
                        image queue size (default 1, set to 0 for unlimited)

  Calibration Optimizer Options:
    --fix-principal-point
                        for pinhole, fix the principal point at the image
                        center
    --fix-aspect-ratio  for pinhole, enforce focal lengths (fx, fy) are equal
    --zero-tangent-dist
                        for pinhole, set tangential distortion coefficients
                        (p1, p2) to zero
    -k NUM_COEFFS, --k-coefficients=NUM_COEFFS
                        for pinhole, number of radial distortion coefficients
                        to use (up to 6, default 2)
    --fisheye-recompute-extrinsicsts
                        for fisheye, extrinsic will be recomputed after each
                        iteration of intrinsic optimization
    --fisheye-fix-skew  for fisheye, skew coefficient (alpha) is set to zero
                        and stay zero
    --fisheye-fix-principal-point
                        for fisheye,fix the principal point at the image
                        center
    --fisheye-k-coefficients=NUM_COEFFS
                        for fisheye, number of radial distortion coefficients
                        to use fixing to zero the rest (up to 4, default 4)
    --fisheye-check-conditions
                        for fisheye, the functions will check validity of
                        condition number
    --disable_calib_cb_fast_check
                        uses the CALIB_CB_FAST_CHECK flag for
                        findChessboardCorners
    --max-chessboard-speed=MAX_CHESSBOARD_SPEED
                        Do not use samples where the calibration pattern is
                        moving faster                      than this speed in
                        px/frame. Set to eg. 0.5 for rolling shutter cameras.
```

#### Unsynchronized Stereo

By default, the \`image_pipeline\` assumes that stereo cameras are
triggered to capture images simultaneously, and that matching image
pairs have identical timestamps. This is the ideal situation, but
requires hardware support.

Starting in Diamondback, you will be able to calibrate stereo pairs that
are not (or inexactly) synchronized.

To enable approximate timestamp matching, give the
\`\--approximate=0.01\` option. This permits a \"slop\" of 0.01s between
image pairs. If you still don\'t see a display window, or it is
sporadically updated, try increasing the slop.

#### Dual Checkerboards

Starting in Diamondback, you will be able to use multiple size
checkerboards to calibrate a camera.

To use multiple checkerboards, give multiple \`\--size\` and
\`\--square\` options for additional boards. Make sure the boards have
different dimensions, so the calibration system can tell them apart.

### Camera Check

To run the command-line utility to check the calibration of a monocular
camera:

```
rosrun camera_calibration cameracheck.py --size 8x6 monocular:=/forearm image:=image_rect
``` To run the command-line utility to check the
calibration of a stereo camera:

```
rosrun camera_calibration cameracheck.py --size 8x6 stereo:=/wide_stereo image:=image_rect
```

## Nodes

```clearsilver
node.0 {
name=cameracalibrator.py
desc=`cameracalibrator.py` subscribes to ROS raw image topics, and presents a calibration window.  It can run in both monocular and stereo modes. The calibration window shows the current images from the cameras, highlighting the checkerboard.  When the user presses the '''CALIBRATE''' button, the node computes the camera calibration parameters.  When the user clicks '''COMMIT''', the node uploads these new calibration parameters to the camera driver using a service call.

sub{
0.name= image
0.type= sensor_msgs/Image
0.desc= raw image topic, for monocular cameras
1.name= left
1.type= sensor_msgs/Image
1.desc= raw left image topic, for stereo cameras
2.name= right
2.type= sensor_msgs/Image
2.desc= raw right image topic, for stereo cameras
}
srv_called{
0.name= camera/set_camera_info
0.type= sensor_msgs/SetCameraInfo
0.desc= Sets the camera info for a monocular camera
1.name= left_camera/set_camera_info
1.type= sensor_msgs/SetCameraInfo
1.desc= Sets the camera info for the left camera of a stereo pair
2.name= right_camera/set_camera_info
2.type= sensor_msgs/SetCameraInfo
2.desc= Sets the camera info for the right camera of a stereo pair
}
}
node.1 {
name=cameracheck.py
desc=`cameracheck.py` subscribes to ROS rectified image topics and their associated camera_info, and prints out an error estimate.  It can run in both monocular and stereo modes. The program expects to see a standard checkerboard target.

sub{
0.name= monocular/image
0.type= sensor_msgs/Image
0.desc= rectified image topic, for monocular cameras
1.name= monocular/camera_info
1.type= sensor_msgs/CameraInfo
1.desc= camera info for the monocular camera
2.name= stereo/left/image
2.type= sensor_msgs/Image
2.desc= rectified left image topic, for stereo cameras
3.name= stereo/right/image
3.type= sensor_msgs/Image
3.desc= rectified right image topic, for stereo cameras
4.name= stereo/camera_info
4.type= sensor_msgs/CameraInfo
4.desc= camera info for the stereo pair
}
}
```
