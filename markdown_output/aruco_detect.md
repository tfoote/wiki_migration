## Nodes

### aruco_detect

aruco_detect detects the pose of
[aruco markers](http://docs.opencv.org/3.1.0/d5/dae/tutorial_aruco_detection.html).

#### Subscribed Topics

- `/camera/compressed`
  ([sensor_msgs/msg/CompressedImage](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CompressedImage.html)):
  The images to be processed.
- `/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  The intrinsic parameters of the camera used to acquire the images.

#### Published Topics

- `/fiducial_vertices`
  ([fiducial_msgs/msg/Fiducials](https://docs.ros.org/en/rolling/p/fiducial_msgs/msg/Fiducials.html)):
  The vertices of detected fiducials.
- `/fiducial_transforms`
  ([fiducial_msgs/msg/FiducialTransforms](https://docs.ros.org/en/rolling/p/fiducial_msgs/msg/FiducialTransforms.html)):
  The transforms showing the pose of the fiducials relative to the
  camera.

#### Parameters

There are two categories of ROS [Parameters](Parameters) that can be
used to configure the `aruco_detect` node: general and detection.

##### General parameters

#### Parameters

- `~dictionary` (`int`, default: `7 (DICT_5X5_1000)`): The aruco
  dictionary to use. Possible values: 0 (DICT_4X4_50), 1 (DICT_4X4_100),
  2 (DICT_4X4_250), 3 (DICT_4X4_1000), 4 (DICT_5X5_50), 5
  (DICT_5X5_100), 6 (DICT_5X5_250), 7 (DICT_5X5_1000), 8 (DICT_6X6_50),
  9 (DICT_6X6_100), 10 (DICT_6X6_250), 11 (DICT_6X6_1000), 12
  (DICT_7X7_50), 13 (DICT_7X7_100), 14 (DICT_7X7_250), 15
  (DICT_7X7_1000), 16 (DICT_ARUCO_ORIGINAL).
- `~fiducial_len` (`double`, default: `0.14`): The length of one side of
  a fiducial in meters, used by the pose estimation.
- `~fiducial_len_override` (`string`): A string expressing exceptions to
  `fiducial_len`. This can contain individual fiducial IDs, or ranges
  of them. Example: `"1-10: 0.05, 12: 0.06"` sets the length of
  fiducials 1 to 10 to 5cm and the length of fiducial 12 to 6cm.
- `~ignore_fiducials` (`string`): A string expressing fiducials to be
  ignored. This can contain individual fiducial IDs, or ranges of them.
  Example: `"1-10, 12"` ignores fiducials 1 to 10 and 12.
- `~publish_images` (`bool`, default: `false`): If set, images will be
  published with the detected markers shown.

##### Detection parameters

The
[detector parameters](http://docs.opencv.org/trunk/d1/dcd/structcv_1_1aruco_1_1DetectorParameters.html)
used in the library are paramaters of the `aruco_detect` node. They
can also be set via [dynamic reconfigure](dyncamic_reconfigure).

- `~adaptiveThreshConstant` (`int`, default: `7`): Constant for adaptive
  thresholding before finding contours.
- `~adaptiveThreshWinSizeMax` (`int`, default: `53`): Minimum window
  size for adaptive thresholding before finding contours.
- `~adaptiveThreshWinSizeMin` (`int`, default: `3`): Maximum window size
  for adaptive thresholding before finding contours.
- `~adaptiveThreshWinSizeStep` (`int`, default: `4`): Increments from
  adaptiveThreshWinSizeMin to adaptiveThreshWinSizeMax during the
  thresholding.
- `~cornerRefinementMaxIterations` (`int`, default: `30`): Maximum
  number of iterations for stop criteria of the corner refinement
  process.
- `~cornerRefinementWinSize` (`int`, default: `5`): Minimum error for
  the stop criteria of the corner refinement process.
- `~cornerRefinementMinAccuracy` (`double`, default: `0.01`): Minimum
  error for the stop criteria of the corner refinement process
- `~doCornerRefinement` (`bool`, default: `true`): Whether to do
  supbixel corner refinement.
- `~errorCorrectionRate` (`double`, default: `0.6`): Error correction
  rate respect to the maximum error correction capability for each
  dictionary.
- `~minCornerDistanceRate` (`double`, default: `0.05`): Minimum distance
  between corners for detected markers relative to its perimeter.
- `~markerBorderBits` (`int`, default: `1`): Number of bits of the
  marker border, i.e. marker border width.
- `~maxErroneousBitsInBorderRate` (`double`, default: `0.04`): Maximum
  number of accepted erroneous bits in the border (i.e. number of
  allowed white bits in the border).
- `~minDistanceToBorder` (`int`, default: `3`): Minimum distance of any
  corner to the image border for detected markers (in pixels).
- `~minMarkerDistanceRate` (`double`, default: `0.05`): minimum mean
  distance beetween two marker corners to be considered similar, so that
  the smaller one is removed. The rate is relative to the smaller
  perimeter of the two markers.
- `~minMarkerPerimeterRate` (`double`, default: `0.1`): Determine
  minumum perimeter for marker contour to be detected. This is defined
  as a rate respect to the maximum dimension of the input image.
- `~maxMarkerPerimeterRate` (`double`, default: `4.0`): Determine
  maximum perimeter for marker contour to be detected. This is defined
  as a rate respect to the maximum dimension of the input image.
- `~minOtsuStdDev` (`double`, default: `5.0`): Minimun standard
  deviation in pixels values during the decodification step to apply
  Otsu thresholding (otherwise, all the bits are set to 0 or 1 depending
  on mean higher than 128 or not).
- `~perspectiveRemoveIgnoredMarginPerCell` (`double`, default: `0.13`):
  Width of the margin of pixels on each cell not considered for the
  determination of the cell bit. Represents the ratio with respect to
  the total size of the cell.
- `~perspectiveRemovePixelPerCell` (`int`, default: `8`): Number of bits
  (per dimension) for each cell of the marker when removing the
  perspective.
- `~polygonalApproxAccuracyRate` (`double`, default: `0.01`): Number of
  bits (per dimension) for each cell of the marker when removing the
  perspective.
