## Overview

More information can be found
[here](http://code.google.com/p/thermalvis-ros-pkg/)

## Dependencies

-   [vslam](http://www.ros.org/wiki/vslam) : Really just the SBA package
    within this, but I find it easier (and more interesting) to just
    compile the whole thing.
-   [OpenCV](http://opencv.org/)

## ROS Nodes

```clearsilver
node.0 {
 name = calibrator
 desc = For the geometric calibration of both thermal-infrared cameras and regular cameras (both intrinsic and extrinsic). 
param {
group.0 {
name=Dynamically Reconfigurable Parameters
desc=See the [[dynamic_reconfigure]] package for details on dynamically reconfigurable parameters.
0.name= ~alpha
0.default= 0.0
0.type= double
0.desc=Alpha level for undistortion and new cam mat Range: -1.0 to 1.0
1.name= ~autoAlpha
1.default= True
1.type= bool
1.desc=Automatically find best alpha level 
2.name= ~trackingMode
2.default= False
2.type= bool
2.desc=Attempt to track pattern rather than redetect 
3.name= ~flowThreshold
3.default= 0.0001
3.type= double
3.desc=Sensitivity for optical flow algorithm Range: 0.0 to 1.0
4.name= ~maxFrac
4.default= 0.05
4.type= double
4.desc=Maximum proportion of minor image dimension that points may drift between frames for tracking Range: 0.0 to 1.0
5.name= ~errorThreshold
5.default= 0.0
5.type= double
5.desc=Error threshold for feature exlusion from tracker Range: 0.0 to 200.0
6.name= ~stopCapturing
6.default= False
6.type= bool
6.desc=stopCapturing 
7.name= ~contrastLeft
7.default= 1.0
7.type= double
7.desc=Contrast left Range: 0.0 to 10.0
8.name= ~brightnessLeft
8.default= 0.0
8.type= double
8.desc=Brightness left Range: -50.0 to 50.0
9.name= ~normLeft
9.default= False
9.type= bool
9.desc=Histogramm equalisation left 
10.name= ~invertLeft
10.default= False
10.type= bool
10.desc=Invert left 
11.name= ~contrastRight
11.default= 1.0
11.type= double
11.desc=Contrast left Range: 0.0 to 10.0
12.name= ~brightnessRight
12.default= 0.0
12.type= double
12.desc=Brightness right Range: -50.0 to 50.0
13.name= ~normRight
13.default= False
13.type= bool
13.desc=Histogramm equalisation right 
14.name= ~invertRight
14.default= False
14.type= bool
14.desc=Invert left 
15.name= ~adjustMSERLeft
15.default= False
15.type= bool
15.desc=adjustMSERLeft 
16.name= ~deltaLeft
16.default= 8
16.type= int
16.desc=deltaLeft Range: 0 to 100
17.name= ~maxVarLeft
17.default= 0.25
17.type= double
17.desc=maxVarLeft Range: 0.0 to 2.0
18.name= ~minDivLeft
18.default= 0.2
18.type= double
18.desc=minDivLeft Range: 0.0 to 2.0
19.name= ~areaThresholdLeft
19.default= 1.01
19.type= double
19.desc=areaThresholdLeft Range: 0.0 to 5.0
20.name= ~adjustMSERRight
20.default= False
20.type= bool
20.desc=adjustMSERRight 
21.name= ~deltaRight
21.default= 8
21.type= int
21.desc=deltaRight Range: 0 to 100
22.name= ~maxVarRight
22.default= 0.25
22.type= double
22.desc=maxVarRight Range: 0.0 to 2.0
23.name= ~minDivRight
23.default= 0.2
23.type= double
23.desc=minDivRight Range: 0.0 to 2.0
24.name= ~areaThresholdRight
24.default= 1.01
24.type= double
24.desc=areaThresholdRight Range: 0.0 to 5.0
}
}
}
```

#### Examples

For intrinsic calibration only:

```
$ roslaunch thermalvis calibrator_monoexample.launch
```

For stereo calibration:

```
$ roslaunch thermalvis calibrator_stereoexample.launch
```

```clearsilver
node.0 {
 name = streamer
 desc = For streaming from and controlling the Thermoteknix Miricle 110K and 307K cameras. 
param {
group.0 {
name=Dynamically Reconfigurable Parameters
desc=See the [[dynamic_reconfigure]] package for details on dynamically reconfigurable parameters.
0.name= ~inputDatatype
0.default= 1
0.type= int
0.desc=Pixel format of input Possible values are: 8bit (0): 8-bit single channel, raw (1): Raw 16-bit format, mm (2): 8-bit dual channel (multimodal), 16uc1 (3): 16-bit from kinect depth
1.name= ~forceInputGray
1.default= False
1.type= bool
1.desc=Forces color input to be converted to gray 
2.name= ~framerate
2.default= -1.0
2.type= double
2.desc=Desired Framerate Range: -1.0 to 100.0
3.name= ~normMode
3.default= 0
3.type= int
3.desc=Histogram Normalization Mode Possible values are: standard (0): Standard dynamic range, equalize (1): Equalization, clahe (2): CLAHE, clahe_adaptive (3): Adaptive Contrast Enhancement, centralized (4): Centers intensities around median, expanded (5): Centers intensities around mid-range
4.name= ~normFactor
4.default= 0.0
4.type= double
4.desc=Normalization factor Range: 0.0 to 1.0
5.name= ~filterMode
5.default= 0
5.type= int
5.desc=Image Filtering Mode Possible values are: none (0): No filtering, gaussian (1): Gaussian Filter, bilateral (2): Bilateral Filter, adaptive_bilateral (3): Adaptive Bilateral Filter
6.name= ~filterParam
6.default= 2.0
6.type= double
6.desc=Filter param Range: 0.0 to 20.0
7.name= ~output16bit
7.default= True
7.type= bool
7.desc=Activate 16-bit (raw) output 
8.name= ~output8bit
8.default= False
8.type= bool
8.desc=Activeate 8-bit (mono) output 
9.name= ~outputColor
9.default= True
9.type= bool
9.desc=Activate color output 
10.name= ~map
10.default= 0
10.type= int
10.desc=A color mapping parameter which is edited via an enum Possible values are: GRAYSCALE (0): Grayscale coloring, CIECOMP (1): CIECOMP coloring, BLACKBODY (2): Blackbody coloring, RAINBOW (3): Rainbow coloring, IRON (4): Iron coloring, BLUERED (5): Blue-red coloring, JET (6): Jet coloring, ICE (7): Ice coloring, ICEIRON (8): Ice and iron coloring, ICEFIRE (9): Ice and fire coloring, REPEATED (10): Ice and fire coloring, HIGHLIGHTED (11): Highlights dominant pixels as red
11.name= ~extremes
11.default= True
11.type= bool
11.desc=Allow b/w color mapping 
12.name= ~writeImages
12.default= False
12.type= bool
12.desc=Activate write output 
13.name= ~outputFormat
13.default= 4
13.type= int
13.desc=Output image format Possible values are: jpg (0): JPEG, pgm (1): PGM, bmp (2): BMP, ppm (3): PPM, png (4): PNG
14.name= ~outputType
14.default= 2
14.type= int
14.desc=Output image type Possible values are: CV_8UC1 (0): 8-bit single channel, CV_8UC3 (1): 8-bit triple channel, CV_16UC1 (2): 16-bit single channel
15.name= ~writeQuality
15.default= 1.0
15.type= double
15.desc=Write quality Range: 0.0 to 1.0
16.name= ~keepOriginalNames
16.default= True
16.type= bool
16.desc=Keep original names 
17.name= ~loopMode
17.default= False
17.type= bool
17.desc=Re-loop once finished 
18.name= ~undistortImages
18.default= False
18.type= bool
18.desc=Activate image undistortion 
19.name= ~rectifyImages
19.default= False
19.type= bool
19.desc=Activate image rectification 
20.name= ~alpha
20.default= 0.0
20.type= double
20.desc=Alpha level for undistortion Range: -1.0 to 1.0
21.name= ~autoAlpha
21.default= True
21.type= bool
21.desc=Automatically find best alpha level 
22.name= ~temporalSmoothing
22.default= False
22.type= bool
22.desc=Regulate change in median intensity (8-bit only) 
23.name= ~maxShift
23.default= 2
23.type= int
23.desc=Maximum amount of intensity shift (8-bit only) Range: 0 to 20
24.name= ~temporalMemory
24.default= 5
24.type= int
24.desc=Maximum amount of past frames to consider Range: 0 to 100
25.name= ~removeDuplicates
25.default= False
25.type= bool
25.desc=Remove consecutive duplicate frames 
26.name= ~markDuplicates
26.default= False
26.type= bool
26.desc=Mark consecutive duplicate frames 
27.name= ~dumpDuplicates
27.default= False
27.type= bool
27.desc=Output duplicates to a log-file 
28.name= ~dumpTimestamps
28.default= False
28.type= bool
28.desc=Output timestamps to console 
29.name= ~fusionFactor
29.default= 0.6
29.type= double
29.desc=Scaling range for modality fusion Range: 0.0 to 1.0
30.name= ~syncMode
30.default= 0
30.type= int
30.desc=Input synchronization mode Possible values are: hardSync (0): Image and camera_info topics must be fully synchronized, softSync (1): Image and camera_info topics do not have to be fully synchronized, imageOnly (2): To be used when no camera_info topic is present
31.name= ~syncDiff
31.default= 0.005
31.type= double
31.desc=Maximum difference in seconds for soft sync Range: 0.0 to 1.0
32.name= ~readThermistor
32.default= False
32.type= bool
32.desc=Read thermistor values 
33.name= ~shutterPeriod
33.default= 10
33.type= int
33.desc=No. of polls between shutter switching Range: 0 to 1000
34.name= ~serialPollingRate
34.default= 10.0
34.type= double
34.desc=Rate (per sec) for serial polling Range: 0.0 to 100.0
35.name= ~maxNucInterval
35.default= 45
35.type= int
35.desc=Maximum NUC interval (in sec) Range: 5 to 300
36.name= ~maxNucThreshold
36.default= 0.2
36.type= double
36.desc=Maximum NUC threshold (in deg) Range: 0.0 to 5.0
37.name= ~maxThermistorDiff
37.default= 0.5
37.type= double
37.desc=Maximum temp difference between consecutive thermistor readings Range: 0.0 to 10.0
38.name= ~verboseMode
38.default= False
38.type= bool
38.desc=Display additional debug info 
39.name= ~drawReticle
39.default= False
39.type= bool
39.desc=Overlay reticle 
}
}
}
```

#### Examples

Should act as a driver for a Thermoteknix Miricle 110K or 307K camera,
allowing the reading of the thermistor, and control of camera settings,
along with streaming in the raw 14-bit/pixel mode.

```
$ roslaunch thermalvis streamer_example.launch
```

```clearsilver
node.0 {
 name = flow
 desc = Highly configurable sparse optical flow for thermal-infrared video. 
param {
group.0 {
name=Dynamically Reconfigurable Parameters
desc=See the [[dynamic_reconfigure]] package for details on dynamically reconfigurable parameters.
0.name= ~softSync
0.default= False
0.type= bool
0.desc=Attempt to pair images and camera info that may not be strictly sync'ed 
1.name= ~syncDiff
1.default= 0.005
1.type= double
1.desc=Maximum difference in seconds for soft sync Range: 0.0 to 1.0
2.name= ~detector_1
2.default= 1
2.type= int
2.desc=Detector #1 Possible values are: OFF (0): No detector implemented, GFTT (1): Hessian features (GFTT), FAST (2): FAST, HARRIS (3): Harris features (GFTT)
3.name= ~sensitivity_1
3.default= 0.1
3.type= double
3.desc=Detector #1 sensitivity Range: 0.0 to 1.0
4.name= ~detector_2
4.default= 0
4.type= int
4.desc=Detector #2 Possible values are: OFF (0): No detector implemented, GFTT (1): Hessian features (GFTT), FAST (2): FAST, HARRIS (3): Harris features (GFTT)
5.name= ~sensitivity_2
5.default= 0.1
5.type= double
5.desc=Detector #2 sensitivity Range: 0.0 to 1.0
6.name= ~detector_3
6.default= 0
6.type= int
6.desc=Detector #3 Possible values are: OFF (0): No detector implemented, GFTT (1): Hessian features (GFTT), FAST (2): FAST, HARRIS (3): Harris features (GFTT)
7.name= ~sensitivity_3
7.default= 0.1
7.type= double
7.desc=Detector #3 sensitivity Range: 0.0 to 1.0
8.name= ~maxFrac
8.default= 0.05
8.type= double
8.desc=Maximum proportion of minor image dimension that points may drift between frames for tracking Range: 0.0 to 1.0
9.name= ~maxFeatures
9.default= 100
9.type= int
9.desc=Maximum number of features to attempt tracking Range: 0 to 500
10.name= ~newDetectionFramecountTrigger
10.default= 10
10.type= int
10.desc=Number of frames to wait before attempting re-detections Range: 0 to 100
11.name= ~maximumDetectionFeatures
11.default= 300
11.type= int
11.desc=Maximum number of features to allow detector to return Range: 0 to 1000
12.name= ~minDistance
12.default= 5.0
12.type= double
12.desc=Minimum spatial separation between features Range: 0.0 to 20.0
13.name= ~flowThreshold
13.default= 0.0001
13.type= double
13.desc=Sensitivity for optical flow algorithm Range: 0.0 to 1.0
14.name= ~minTrackedFeaturesPerDetector
14.default= 50
14.type= int
14.desc=Minimum number of features to be tracked by each detector Range: 0 to 500
15.name= ~maxTrackedFeaturesPerDetector
15.default= 300
15.type= int
15.desc=Maximum number of features to be tracked by each detector Range: 0 to 500
16.name= ~nearSearchHistory
16.default= 5
16.type= int
16.desc=How many frames to search back for recently lost features Range: 0 to 1000
17.name= ~farSearchHistory
17.default= 48
17.type= int
17.desc=How many frames to search back for historically lost features Range: 0 to 1000
18.name= ~delayTimeout
18.default= 2.0
18.type= double
18.desc=Timeout in seconds before NUC is assumed Range: 0.0 to 10.0
19.name= ~maxProjectionsPerFeature
19.default= 10
19.type= int
19.desc=Maximum number of projections of feature to publish Range: 0 to 100
20.name= ~minPointsForWarning
20.default= 16
20.type= int
20.desc=Minimum number of tracks below which a warning is triggered Range: 0 to 100
21.name= ~drawingHistory
21.default= 10
21.type= int
21.desc=Number of projections for the feature tail in the debug image Range: 0 to 100
22.name= ~debugMode
22.default= True
22.type= bool
22.desc=Publish output 
}
}
}
```

#### Examples

Should publish a customized \'\'\'tracks\'\'\' topic containing sparse
optical flow information.

```
$ roslaunch thermalvis flow_example.launch
```

```clearsilver
node.0 {
 name = monoslam
 desc = Monocular SLAM with a hand-held thermal-infrared camera. 
param {
group.0 {
name=Dynamically Reconfigurable Parameters
desc=See the [[dynamic_reconfigure]] package for details on dynamically reconfigurable parameters.
0.name= ~minStartupScore
0.default= 0.8
0.type= double
0.desc=Minimum keyframe pair score for initialization Range: 0.0 to 1.0
1.name= ~flowback
1.default= 3
1.type= int
1.desc=Flowback frames (per adjustment) Range: 0 to 10
2.name= ~keyframeSpacing
2.default= 5
2.type= int
2.desc=See the paper, variable K Range: 0 to 100
3.name= ~maxKeyframeSeparation
3.default= 15
3.type= int
3.desc=Maximum number of frames separating keyframes Range: 0 to 100
4.name= ~minKeyframeScore
4.default= 20.0
4.type= double
4.desc=Minimum required keyframe score Range: 0.0 to 100.0
5.name= ~adjustmentFrames
5.default= 50
5.type= int
5.desc=Adjustment frames Range: 1 to 100
6.name= ~motionThreshold
6.default= 20.0
6.type= double
6.desc=Maximum amount of tolerated motion Range: 1.0 to 100.0
7.name= ~framesForTriangulation
7.default= 8
7.type= int
7.desc=Number of frames a feature must appear in before it's triangulated Range: 1 to 100
8.name= ~min3dPtsForPnP
8.default= 24
8.type= int
8.desc=Minimum number of points to use to estimate pose of camera Range: 0 to 100
9.name= ~camerasPerSys
9.default= 10
9.type= int
9.desc=Cameras to consider for each bundle adjustment Range: 0 to 100
10.name= ~minTrackedFeatures
10.default= 50
10.type= int
10.desc=Minimum number of features that must be tracked Range: 0 to 500
11.name= ~maxGuides
11.default= 5
11.type= int
11.desc=Maximum number of camera views to consider for initial pose estimate Range: 0 to 100
12.name= ~minGeometryScore
12.default= 30.0
12.type= double
12.desc=Minimum required geometry score Range: 0.0 to 100.0
13.name= ~requiredTrackFrac
13.default= 0.8
13.type= double
13.desc=Required proportion of tracks to be maintained between frames Range: 0.0 to 1.0
14.name= ~dataTimeout
14.default= 5.0
14.type= double
14.desc=Time (sec) after which no data triggers program exit Range: 0.0 to 60.0
15.name= ~initialStructureIterations
15.default= 1000
15.type= int
15.desc=Number of iterations to perform finalizing initial structure Range: 0 to 1000
16.name= ~poseEstimateIterations
16.default= 10
16.type= int
16.desc=Number of iterations to perform when putatively estimating a camera pose Range: 0 to 1000
17.name= ~fullSystemIterations
17.default= 10
17.type= int
17.desc=Number of iterations to perform each cycle on the full system Range: 0 to 1000
18.name= ~keyframeIterations
18.default= 10
18.type= int
18.desc=Number of iterations to perform each cycle on the keyframes Range: 0 to 1000
19.name= ~subsequenceIterations
19.default= 100
19.type= int
19.desc=Number of iterations to perform each cycle on the subsequence Range: 0 to 1000
20.name= ~debugMode
20.default= False
20.type= bool
20.desc=Display additional debug info 
21.name= ~timeDebug
21.default= False
21.type= bool
21.desc=Display timing information 
22.name= ~timeSpacing
22.default= 5
22.type= int
22.desc=Number of frames to wait before publishing timing info Range: 0 to 100
}
}
}
```

#### Examples

I recommend making sure that you have got the \'\'\'flow\'\'\' node
working effectively before trying to run the \'\'\'monoslam\'\'\' node.
```
$ roslaunch thermalvis monoslam_example.launch
```

```clearsilver
node.0 {
 name = depth
 desc = Real-time depth from stereo from thermal-infrared video [in progress]. 
param {
group.0 {
name=Dynamically Reconfigurable Parameters
desc=See the [[dynamic_reconfigure]] package for details on dynamically reconfigurable parameters.
0.name= ~alpha
0.default= 0.0
0.type= double
0.desc=Alpha level for undistortion Range: -1.0 to 1.0
1.name= ~autoAlpha
1.default= True
1.type= bool
1.desc=Automatically find best alpha level 
}
}
}
```

#### Examples

This should simply produce a depth map from two video streams.

```
$ roslaunch thermalvis calibrator_monoexample.launch
```0

```
$ roslaunch thermalvis calibrator_monoexample.launch
```1

#### Examples

This node requires a bag file to exist which contains relevant topics
for 3D thermal mapping.

```
$ roslaunch thermalvis calibrator_monoexample.launch
```2
