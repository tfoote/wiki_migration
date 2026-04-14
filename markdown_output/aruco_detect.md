## Nodes

```clearsilver
name = aruco_detect
desc = aruco_detect detects the pose of [[http://docs.opencv.org/3.1.0/d5/dae/tutorial_aruco_detection.html|aruco markers]].

sub {
  0.name= /camera/compressed
  0.desc= The images to be processed.
  0.type= sensor_msgs/CompressedImage
  1.name= /camera_info
  1.desc= The intrinsic parameters of the camera used to acquire the images.
  1.type= sensor_msgs/CameraInfo
}
pub {
  0.name= /fiducial_vertices
  0.type= fiducial_msgs/Fiducials
  0.desc= The vertices of detected fiducials.
  1.name= /fiducial_transforms
  1.type= fiducial_msgs/FiducialTransforms
  1.desc= The transforms showing the pose of the fiducials relative to the camera.
}
```

#### Parameters

There are two categories of ROS [Parameters](Parameters) that can be
used to configure the \`aruco_detect\` node: general and detection.

##### General parameters

```clearsilver
param {
  0.name= ~dictionary
  0.type= int
  0.desc= The aruco dictionary to use. Possible values: 0 (DICT_4X4_50), 1 (DICT_4X4_100), 2 (DICT_4X4_250), 3 (DICT_4X4_1000), 4 (DICT_5X5_50), 5 (DICT_5X5_100), 6 (DICT_5X5_250), 7 (DICT_5X5_1000), 8 (DICT_6X6_50), 9 (DICT_6X6_100), 10 (DICT_6X6_250), 11 (DICT_6X6_1000), 12 (DICT_7X7_50), 13 (DICT_7X7_100), 14 (DICT_7X7_250), 15 (DICT_7X7_1000), 16 (DICT_ARUCO_ORIGINAL).
  0.default= 7 (DICT_5X5_1000)
  1.name= ~fiducial_len
  1.type= double
  1.desc= The length of one side of a fiducial in meters, used by the pose estimation.
  1.default= 0.14
  2.name= ~fiducial_len_override
  2.type= string
  2.default=
  2.desc= A string expressing exceptions to `fiducial_len`. This can contain individual fiducial IDs, or ranges of them.  Example: `"1-10: 0.05, 12: 0.06"` sets the length of fiducials 1 to 10 to 5cm and the length of fiducial 12 to 6cm.
  3.name= ~ignore_fiducials
  3.type = string
  3.default=
  3.desc= A string expressing fiducials to be ignored. This can contain individual fiducial IDs, or ranges of them.  Example: `"1-10, 12"` ignores fiducials 1 to 10 and 12.
  4.name= ~publish_images
  4.type= bool
  4.desc= If set, images will be published with the detected markers shown.
  4.default= false
}
```

##### Detection parameters

The
[detector parameters](http://docs.opencv.org/trunk/d1/dcd/structcv_1_1aruco_1_1DetectorParameters.html)
used in the library are paramaters of the \`aruco_detect\` node. They
can also be set via [dynamic reconfigure](dyncamic_reconfigure).

```clearsilver
param {
  no_header=True
  0.name= ~adaptiveThreshConstant
  0.desc= Constant for adaptive thresholding before finding contours.
  0.default=7
  0.type= int
  1.name= ~adaptiveThreshWinSizeMax
  1.desc= Minimum window size for adaptive thresholding before finding contours.
  1.default=53
  1.type= int
  2.name= ~adaptiveThreshWinSizeMin
  2.desc= Maximum window size for adaptive thresholding before finding contours.
  2.default= 3
  2.type= int
  3.name= ~adaptiveThreshWinSizeStep
  3.desc= Increments from adaptiveThreshWinSizeMin to adaptiveThreshWinSizeMax during the thresholding.
  3.default=4
  3.type= int
  4.name= ~cornerRefinementMaxIterations
  4.desc= Maximum number of iterations for stop criteria of the corner refinement process.
  4.default= 30
  4.type= int
  5.name= ~cornerRefinementWinSize
  5.desc= Minimum error for the stop criteria of the corner refinement process.
  5.default= 5
  5.type= int
  6.name= ~cornerRefinementMinAccuracy
  6.desc= Minimum error for the stop criteria of the corner refinement process
  6.type= double
  6.default= 0.01
  7.name= ~doCornerRefinement
  7.desc= Whether to do supbixel corner refinement.
  7.default= true
  7.type= bool
  8.name= ~errorCorrectionRate
  8.desc= Error correction rate respect to the maximum error correction capability for each dictionary.
  8.default= 0.6
  8.type= double
  9.name= ~minCornerDistanceRate
  9.desc= Minimum distance between corners for detected markers relative to its perimeter.
  9.default= 0.05
  9.type= double
  10.name= ~markerBorderBits
  10.desc= Number of bits of the marker border, i.e. marker border width.
  10.default= 1
  10.type= int
  11.name= ~maxErroneousBitsInBorderRate
  11.desc= Maximum number of accepted erroneous bits in the border (i.e. number of allowed white bits in the border).
  11.default= 0.04
  11.type= double
  12.name= ~minDistanceToBorder
  12.desc= Minimum distance of any corner to the image border for detected markers (in pixels).
  12.default= 3
  12.type=int
  13.name= ~minMarkerDistanceRate
  13.desc= minimum mean distance beetween two marker corners to be considered similar, so that the smaller one is removed. The rate is relative to the smaller perimeter of the two markers.
  13.default= 0.05
  13.type= double
  14.name= ~minMarkerPerimeterRate
  14.desc= Determine minumum perimeter for marker contour to be detected. This is defined as a rate respect to the maximum dimension of the input image.
  14.default= 0.1
  14.type= double
  15.name= ~maxMarkerPerimeterRate
  15.desc= Determine maximum perimeter for marker contour to be detected. This is defined as a rate respect to the maximum dimension of the input image.
  15.default= 4.0
  15.type= double
  16.name= ~minOtsuStdDev
  16.desc= Minimun standard deviation in pixels values during the decodification step to apply Otsu thresholding (otherwise, all the bits are set to 0 or 1 depending on mean higher than 128 or not).
  16.default= 5.0
  16.type= double
  17.name= ~perspectiveRemoveIgnoredMarginPerCell
  17.desc= Width of the margin of pixels on each cell not considered for the determination of the cell bit. Represents the ratio with respect to the total size of the cell.
  17.default= 0.13
  17.type= double
  18.name= ~perspectiveRemovePixelPerCell
  18.desc= Number of bits (per dimension) for each cell of the marker when removing the perspective.
  18.default= 8
  18.type= int
  19.name= ~polygonalApproxAccuracyRate
  19.desc= Number of bits (per dimension) for each cell of the marker when removing the perspective.
  19.default= 0.01
  19.type= double
```
