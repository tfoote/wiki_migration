## Overview

This Package is the modified version of well known monocular SLAM
framework [PTAM](http://ewokrampage.wordpress.com/) presented by Klein &
Murray in their
[paper](http://www.robots.ox.ac.uk/~gk/publications.html#2007ISMAR) at
ISMAR07. We modified the
[original code](http://www.robots.ox.ac.uk/~gk/PTAM/) such that:

-   it is compatible with ROS.

```{=html}
<!-- -->
```
-   it runs on-board a computationally limited platform (e.g. at 20Hz on
    an ATOM 1.6GHz single core processor)

```{=html}
<!-- -->
```
-   it is robust in outdoor and self-similar environments such as grass.

This version of PTAM was successfully used in the European project
[sFly](http://www.sfly.org) to estimate a 6DoF pose for long-term vision
based navigation of a micro helicopter in large outdoor environments.

Please study the original
[PTAM website](http://www.robots.ox.ac.uk/~gk/PTAM/) and the
corresponding
[paper](http://www.robots.ox.ac.uk/~gk/publications.html#2007ISMAR)
before using this code. Also, be aware of the
[license](http://www.robots.ox.ac.uk/~gk/PTAM/download.html) that comes
with it.

**Note:** This package is under active development. It is meant for
research use only
([license](http://www.robots.ox.ac.uk/~gk/PTAM/download.html)) and at
your own responsibility.

## Nodes

-   [ptam](/): The main node described here
-   [remote_ptam](/remote_ptam): Node for displaying PTAM information
    and managing PTAM from a remote (ground) station
-   [ptam_visualizer](/ptam_visualizer): Node to store map, keyframe and
    path information and visualize it in RViz
-   [cameracalibrator](/cameracalibrator): Node to calibrate the camera.
    Copy the obtained calibration to the fix parameter file.

## Modifications to the Original Code

PTAM has been ported to be compatible to the Robot Operating System
(ROS) such that:

-   the input image taken from an image node and a verification image
    including the features found, is published. This enables the user to
    handle PTAM on an embedded system without human-machine interfaces.

```{=html}
<!-- -->
```
-   the 6DoF pose is published as a pose with a covariance estimation
    calculated from PTAM's internal bundle adjustment.

```{=html}
<!-- -->
```
-   the visualization of camera keyframes, trajectory and features is
    ported to RVIZ such that visualization can be done on a ground
    station, if necessary.

```{=html}
<!-- -->
```
-   tuning parameters can be changed dynamically in a GUI for dynamic
    reconfiguration.

### Keyframe Handling

In PTAM, the map is defined as a set of keyframes together with their
observed features. In order to minimize the computational complexity,
here we set a maximum number of keyframes retained in the map. If this
number is exceeded, the keyframe furthest away from the current MAV pose
gets deleted along with the features associated with it. If the maximum
number of retained keyframes is infinite, then the algorithm is
equivalent to the original PTAM, while if we set a maximum of 2
keyframes we obtain a visual odometry framework. Naturally, the larger
the number of retained keyframes, the lower the estimation drift, but
also the larger the computational complexity.

### Improved Feature Handling for More Robust Maps

When flying outdoors, we experienced severe issues with self-similarity
of the environment - e.g. the asphalt in urban areas or the grass in
rural areas. Naturally, features extracted at higher pyramidal levels
are more robust to scene ambiguity. Thus, while the finest-scale
features are included for tracking, we omit them in map-handling - i.e.
we only store features extracted in the highest 3 pyramidal levels. This
improves

Thus, while the finest-scale features are included for tracking, we omit
them in map-handling \-- i.e. we only store features extracted in the
highest 3 pyramidal levels. This improves tracking quality when moving
away from a given feature (e.g. when taking-off with a MAV with a
downward-looking camera), making it possible to navigate over both grass
and asphalt.

Since this vision algorithm is keyframe-based, it has high measurement
rates when tracking. However, at keyframe generation the frame-rate
drops remarkably. Using only features detected at the highest pyramidal
levels also reduces drastically the number of newly added features upon
keyframe generation. This results to great speed-ups with
keyframe-generation running at 13Hz (in contrast to the 7Hz of the
original PTAM) and normal tracking rates of around 20Hz on an onboard
Atom computer 1.6GHz.

Concerning the type of features we augmented the choice for the corner
detector by the [AGAST](http://www6.in.tum.de/Main/ResearchAgast)
features. Compared to the
[FAST](http://www.edwardrosten.com/work/fast.html) derivatives, the
[AGAST](http://www6.in.tum.de/Main/ResearchAgast) corner detector is
more repetitive and usually slightly faster as described in
[this](http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&ved=0CCoQFjAB&url=http%3A%2F%2Fwww.springerlink.com%2Findex%2F5nv7941h32t65740.pdf&ei=JdGhT8-JDomi8QSfv-XfCA&usg=AFQjCNFs_Y4RWxf-7cwb8j08RaXkGXnW0A)
paper. In self-similar structures, it is crucial that the corner
detector is highly repetitive. Hence we suggest here to use the
[AGAST](http://www6.in.tum.de/Main/ResearchAgast) corner detector
instead of [FAST](http://www.edwardrosten.com/work/fast.html).

### Re-Initialization After Failure Mode

For automatic initialization we ensure that the baseline is sufficiently
large by calculating the rotation-compensated median pixel disparity.
For rotation compensation we use efficient
[second-order minimization](http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=3&ved=0CEQQFjAC&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D1308092&ei=wRSfT7uzM4L88gTioOCGDw&usg=AFQjCNGhE6CgDaTQ8yv3a3Fc2rVLkOOyaw)
techniques (ESM) in order to keep PTAM independent of IMU readings. For
re-initializations, we store the median scene depth and pose of the
closest keyframe and propagate this information to the new initialized
map. This way we minimize large jumps in scale and pose at
re-initializations.

### Inverted Index Structure for Map-point Filtering

On each frame, PTAM projects the 3D points from the map into the current
image according to the motion-model prior, which allows then
point-correspondences to be established for tracking. Since no filtering
on point visibility is preceding this step, it scales linearly with the
number of points in the map. We implemented an inverted index structure
based on the grouping of map points inside keyframes which allows
discarding large groups of map-points with low probability of being in
the field-of-view. The search for visible points is performed by
re-projecting a small set of distinct map-points from every keyframe
which permits inference on their visibility from the current keyframe.
The total number of points that need evaluation by reprojection is
thereby significantly reduced leading to a scaling of the system in
linear order of the visible keyframes rather than in linear order with
the overall number of keyframes in the map.

## Using ETHZASL-PTAM

To use ETHZASL_PTAM you need an environment with sufficient contrast
(i.e. texture) and light. If your shutter speed is above 5ms to obtain
an image with sufficient contrast it is very likely that the algorithm
does not work properly because of motion blur. This depends on
vehicle's motion and vibrations. For good performance on MAVs you may
ensure:

-   a shutter speed below 5ms
-   no over/under saturated image regions
-   no self-similar structures

### Camera Calibration

The camera model used in PTAM is made for wide angle lenses (>90°). The
[cameracalibrator](/cameracalibrator) node in this package is unchanged
with respect to the original code - except the ROS compatibility. You
should have a re-projection error of below 0.5. If you have problems
calibrating your camera, please have a look at
[this](http://www.robots.ox.ac.uk/~gk/PTAM/usage.html) page.

### Initialization

The manual initialization procedure is the same as on the
[PTAM website](http://www.robots.ox.ac.uk/~gk/PTAM/):

-   Hit space to start initializing
-   translate the camera (no rotation)
-   Hit space again as soon as the disparity is sufficient

For automatic initialization, enable the !AutoInit checkbox in the
dynamic reconfigure GUI. This activates also the re-initialization
procedure if the map is lost.

### Remote Interface

The node [remote_ptam](/remote_ptam) catches the image and information
published by PTAM such that you can visualize it on a ground station
offboard your vehicle. This remote interface accepts nearly all inputs
as the original PTAM GUI:

-   \[space\] for initialization
-   \[r\] for full map reset
-   \[q\] quits PTAM
-   \[s\] enable/disable image streaming for remote node
-   \[a\] experimental: map reset while storing last pose and scale for
    propagation upon re-initialization

It also displays the map grid and the initialization trails but not the
features in the image nor in a 3D view. See the
[remote_ptam](/remote_ptam) node documentation for more details.

### Running onboard the vehicle

Usually the robot on which PTAM runs does not have any display means and
PTAM is controlled remotely using [remote_ptam](/remote_ptam). In such
cases the built PTAM GUI can be disabled to free additional computation
resources: set the fix parameter gui=False. For further speed-up and
performance boost of PTAM onboard the robot you may consider the
following settings:

-   !InitLevel: 1 *for robust and fast initialization on self-similar
    structures*
-   !MaxStereoInitLoops: 4 *for fast map initialization, prevents
    hanging on degenerated sets*
-   !MaxPatchesPerFrame: 300 *maximal number of features per frame*
-   MaxKF: 15 *maximal number of KFs to be retained in the map, do not
    go lower than 5 to maintain good drift performance*
-   UseKFPixelDist: True *generates new KF based on pixel disparity.
    This is usually more robust than the built in KF request in PTAM*
-   !NoLevelZeroMapPoints: True *only use map features in down sampled
    image pyramids. This greatly improves robustness in self-similar
    structures*

### Map Export and Map Display in RViz

The node [ptam_visualizer](/ptam_visualizer) fetches the 3D features,
keyframes and actual pose from the PTAM framework and prepares the data
to be visualized in RViz. Simply start the node and RViz to start the
streaming. The node also allows to store map, path and keyframe data to
a file.

## Tutorials

!! under construction !! please check regularly for updates

## Node Information



```clearsilver
node.0{
  name = ptam
  desc = main framework derived from the original [[http://ewokrampage.wordpress.com/|PTAM]]
  sub{
  0.name = image
  0.type = sensor_msgs/Image
  0.desc = the input image to be processed by PTAM
  1.name = vslam/key_pressed
  1.type = std_msgs/String
  1.desc = topic used by the [[/remote_ptam|remote_ptam]] node to send keyboard commands to the PTAM interface
  2.name = vslam/imu
  2.type = sensor_msgs/Imu
  2.desc = Experimental: IMU readings to estimate a better rotation between frames. We do not recommend to use this since PTAM's estimate using the Small Blurry Images for rotation estimation is already very good.
}
  pub{
  0.name = vslam/info
  0.type = ptam_com/ptam_info
  0.desc = Contains information on the current status of PTAM such as framerate, number of keyframes, tracking and map quality as well as string messages
  1.name = vslam/pose
  1.type = geometry_msgs/PoseWithCovarianceStamped
  1.desc = PoseWidthCovarianceStamped for the 6DoF pose calculated by PTAM. This is the world seen from the camera.
  2.name = vslam/preview
  2.type = sensor_msgs/Image
  2.desc = down sampled image used by the [[/remote_ptam|remote_ptam]] node to visualize the current camera view and PTAM status
}
  srv{
  0.name = vslam/pointcloud
  0.type = ptam_com::PointCloud
  0.desc = point cloud service to visualize 3D points in RViz
  1.name = vslam/keyframes
  1.type = ptam_com::KeyFrame_srv
  1.desc = keyframe service to visualize keyframes in RViz
}
# Autogenerated param section. Do not hand edit.
param {
group.0 {
name=Dynamically Reconfigurable Parameters
desc=See the [[dynamic_reconfigure]] package for details on dynamically reconfigurable parameters.
0.name= ~Scale
0.default= 1.0
0.type= double
0.desc=Scale Range: 0.01 to 30.0
1.name= ~MotionModelSource
1.default= CONSTANT
1.type= str
1.desc=selects the source for the motion model. Possible values are: MM_CONSTANT (CONSTANT): use constant motion model., MM_IMU (IMU): use imu orientation for the motion model., MM_FULL_POSE (FULL_POSE): use full pose estimated externally for motion model.
2.name= ~MaxPatchesPerFrame
2.default= 500.0
2.type= double
2.desc=max features per frame Range: 10.0 to 1000.0
3.name= ~MaxKFDistWiggleMult
3.default= 3.0
3.type= double
3.desc='distance' after which a new kf is requested Range: 0.1 to 10.0
4.name= ~UseKFPixelDist
4.default= False
4.type= bool
4.desc=use AutoInitPixel as new KF request criteria 
5.name= ~NoLevelZeroMapPoints
5.default= False
5.type= bool
5.desc=do not add map points at level zero 
6.name= ~EpiDepthSearchMaxRange
6.default= 100.0
6.type= double
6.desc=depth variance to search for features Range: 1.0 to 100.0
7.name= ~CoarseMin
7.default= 20.0
7.type= double
7.desc=min number of features for coarse tracking Range: 1.0 to 100.0
8.name= ~CoarseMax
8.default= 60.0
8.type= double
8.desc=max number of features for coarse tracking Range: 1.0 to 100.0
9.name= ~CoarseRange
9.default= 30.0
9.type= double
9.desc=Pixel search radius for coarse features Range: 1.0 to 100.0
10.name= ~CoarseSubPixIts
10.default= 8.0
10.type= double
10.desc=coarse tracking sub-pixel iterations Range: 1.0 to 100.0
11.name= ~DisableCoarse
11.default= False
11.type= bool
11.desc=enable/disable coarse tracking 
12.name= ~CoarseMinVelocity
12.default= 0.006
12.type= double
12.desc=speed above which coarse stage is used Range: 0.0 to 1.0
13.name= ~TrackingQualityGood
13.default= 0.3
13.type= double
13.desc=min ratio features visible/features found for good tracking Range: 0.0 to 1.0
14.name= ~TrackingQualityLost
14.default= 0.13
14.type= double
14.desc=max ratio features visible/features found before lost Range: 0.0 to 1.0
15.name= ~TrackingQualityFoundPixels
15.default= 100
15.type= int
15.desc=min pixels to be found for good tracking Range: 1 to 1000
16.name= ~MaxIterations
16.default= 20.0
16.type= double
16.desc=max iterations for bundle adjustment Range: 1.0 to 100.0
17.name= ~MaxKF
17.default= 0
17.type= int
17.desc=number of keyframes kept in the map (0 or 1 = inf) Range: 0 to 1000
18.name= ~BundleMethod
18.default= LOCAL_GLOBAL
18.type= str
18.desc=bundleadjustment method Possible values are: LOCAL_GLOBAL (LOCAL_GLOBAL): local and global bundle adjustment, LOCAL (LOCAL): local bundle adjustment only, GLOBAL (GLOBAL): global bundle adjustment only
19.name= ~UpdateSquaredConvergenceLimit
19.default= 1e-06
19.type= double
19.desc=limit for convergence in bundle adjustment Range: 0.0 to 1.0
20.name= ~BundleDebugMessages
20.default= False
20.type= bool
20.desc=print bundle debug messages 
21.name= ~FASTMethod
21.default= FAST9_nonmax
21.type= str
21.desc=FAST corner method Possible values are: FAST9 (FAST9): FAST 9, FAST10 (FAST10): FAST 10, FAST9_nonmax (FAST9_nonmax): FAST 9 with nonmax suppression, AGAST12d (AGAST12d): AGAST 12 pixel diamond, OAST16 (OAST16): AGAST 16 pixel circular
22.name= ~Thres_lvl0
22.default= 10
22.type= int
22.desc=threshold for FAST features on level 0 Range: 0 to 255
23.name= ~Thres_lvl1
23.default= 15
23.type= int
23.desc=threshold for FAST features on level 1 Range: 0 to 255
24.name= ~Thres_lvl2
24.default= 15
24.type= int
24.desc=threshold for FAST features on level 2 Range: 0 to 255
25.name= ~Thres_lvl3
25.default= 10
25.type= int
25.desc=threshold for FAST features on level 3 Range: 0 to 255
26.name= ~AdaptiveThrs
26.default= False
26.type= bool
26.desc=adaptive threshold for corner extraction 
27.name= ~AdaptiveThrsMult
27.default= 5.0
27.type= double
27.desc=controls adaptive threshold to MaxPatches*N corners Range: 0.5 to 20.0
28.name= ~RotationEstimatorBlur
28.default= 0.75
28.type= double
28.desc=small images for the rotation estimator blur Range: 0.0 to 10.0
29.name= ~UseRotationEstimator
29.default= True
29.type= bool
29.desc=small images for the rotation estimator enable/disable 
30.name= ~MiniPatchMaxSSD
30.default= 100000
30.type= int
30.desc=MiniPatch tracking threshhold Range: 0 to 10000000
31.name= ~PlaneAlignerRansacs
31.default= 100
31.type= int
31.desc=number of dominant plane RANSACs Range: 0 to 1000
32.name= ~RelocMaxScore
32.default= 9000000
32.type= int
32.desc=score for relocalization Range: 0 to 90000000
33.name= ~AutoInit
33.default= False
33.type= bool
33.desc=enable auto initialization 
34.name= ~AutoInitPixel
34.default= 20
34.type= int
34.desc=min pixel distance for auto initialization Range: 1 to 100
35.name= ~MaxStereoInitLoops
35.default= 10
35.type= int
35.desc=max # of loops for stereo initialization Range: 1 to 100
}
group.1{
      name = Static parameters
      desc = parameters that are statically set
0.name= ~InitLevel
0.default= 1
0.desc= minimal pyramidal level for map initialization. Use higher levels on self-similar structures Range 0 to 3
1.name= ~gui
1.default= true
1.desc= enables/disables the graphical feedback. Disable this on onboard computers
2.name= ~ImageSizeX
2.default= 752
2.desc= x-dimensions of the input image to be processed by PTAM
3.name= ~ImageSizeY
3.default= 480
3.desc= y-dimensions of the input image to be processed by PTAM
4.name= ~ARBuffer_width
4.default= 1200
4.desc= width resolution of the graphical feedback window
5.name= ~ARBuffer_height
5.default= 960
5.desc= height resolution of the graphical feedback window
6.name= ~WiggleScale
6.default= 0.1
6.desc= Multiplier for the distance at which a new KF is requested
7.name= ~BundleMEstimator
7.default= Tukey
7.desc= Estimator to be used for bundle adjustment. Possible values are: Huber, Cauchy, Tukey
8.name= ~TrackerMEstimator
8.default= Tukey
8.desc= Estimator to be used for bundle adjustment. Possible values are: Huber, Cauchy, Tukey
9.name= ~MinTukeySigma
9.default= 0.4
9.desc= Sigma value for Tukey estimator
10.name= ~CandidateMinSTScore
10.default= 70
10.desc= minimal Shi-Tomasi score for a point to be considered as a candidate feature 
11.name= ~Cam_fx
11.default= --
11.desc= Camera focal length in x. Retrieve this value from the [[/cameracalibrator|cameracalibrator]] node
12.name= ~Cam_fy
12.default= --
12.desc= Camera focal length in y. Retrieve this value from the [[/cameracalibrator|cameracalibrator]] node
13.name= ~Cam_cx
13.default= --
13.desc= Camera center in x. Retrieve this value from the [[/cameracalibrator|cameracalibrator]] node
14.name= ~Cam_cy
14.default= --
14.desc= Camera center in y. Retrieve this value from the [[/cameracalibrator|cameracalibrator]] node
15.name= ~Cam_s
15.default= --
15.desc= Camera distortion factor. Retrieve this value from the [[/cameracalibrator|cameracalibrator]] node
16.name= ~Calibrator_BlurSigma
16.default= 1.0
16.desc= blur factor for the [[/cameracalibrator|cameracalibrator]]
17.name= ~Calibrator_MeanGate
17.default= 10
17.desc= mean value for the [[/cameracalibrator|cameracalibrator]]
18.name= ~Calibrator_MinCornersForGrabbedImage
18.default= 20
18.desc= min # of corners for the [[/cameracalibrator|cameracalibrator]]
19.name= ~Calibrator_Optimize
19.default= 0
19.desc= optimize flag for the [[/cameracalibrator|cameracalibrator]]
20.name= ~Calibrator_Show
20.default= 0
20.desc= show flag for the [[/cameracalibrator|cameracalibrator]]
21.name= ~Calibrator_NoDistortion
21.default= 0
21.desc= enable/disable distortion flag for the [[/cameracalibrator|cameracalibrator]]
22.name= ~CameraCalibrator_MaxStepDistFraction
22.default= 0.3
22.desc= max step for the [[/cameracalibrator|cameracalibrator]]
23.name= ~CameraCalibrator_CornerPatchSize
23.default= 20
23.desc= size for patches used in the [[/cameracalibrator|cameracalibrator]]
24.name= ~GLWindowMenu_Enable
24.default= true
24.desc= use the openGL window
25.name= ~GLWindowMenu_mgvnMenuItemWidth
25.default= 90
25.desc= openGL window size
26.name= ~GLWindowMenu_mgvnMenuTextOffset
26.default= 20
26.desc= offset for text display in the openGL window
}
}
}
# End of autogenerated section. You may edit below.
```


