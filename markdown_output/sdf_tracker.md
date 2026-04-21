## Documentation

This package provides an implementation of the truncated Signed Distance
Function tracking algorithm, proposed
[here](http://oru.diva-portal.org/smash/record.jsf?pid=diva2:548296).

## Installation

Clone the repository and add it to your ROS_PACKAGE_PATH



```
export ROS_PACKAGE_PATH=/your_path/oru-ros-pkg/:$ROS_PACKAGE_PATH
```



The following commands should build the sdf_tracker library and the
sdf_tracker_node



```
roscd sdf_tracker
rosmake
```



## Running the Node

Using an openNI compatible depth-sensor you can get the node up and
running with:



```
roslaunch openni_launch openni.launch &
rosrun sdf_tracker sdf_tracker_node _param1:=val1 _param2:=val2 ...etc
```



![](attachment:sdf.jpg)

### Parameters

The parameters enable/disable certain features of the node and control
the settings for the tracker. The current list of supported parameters
are:

-   !ImageWidth - *int* - width in pixels, default **640** (useful if
    you want to try QVGA or QQVGA modes)
-   !ImageHeight - *int* - height in pixels, degault **480** (ditto
    above)
-   !InteractiveMode - *bool* - you wish to display a rendering of the
    reconstructed model for interactive use, default **true**
-   !MaxWeight - *double* - relates to the *inertia* of the model and
    its sensitivity to change, default **64.0**
-   !CellSize - *double* - length of the sides of each individual voxel,
    smaller voxels lead to more detail, but require more memory per
    cubic meter, default **0.01**
-   GridSizeX - *int* - Number of voxels in the first dimension
    (right-left), default **256**
-   GridSizeY - *int* - Number of voxels in the second dimension
    (up-down), default **256**
-   GridSizeZ - *int* - Number of voxels in the third dimension
    (front-back), default **256**
-   !PositiveTruncationDistance - *double* - Positive value at which the
    distance field is clipped, in meters, default **0.1**
-   !NegativeTruncationDistance - *double* - Negative value at which the
    distance field is clipped, in meters, default **-0.04**. Note that
    this should be at least larger than the !CellSize.
-   !RobustStatisticCoefficient - *double* - Parametrizes a Huber weight
    function for the residuals. default **0.02**
-   Regularization - *double* - Sets a penalty on large updates between
    frames, default **0.01**
-   !MinPoseChangeToFuseData - *double* - Ensures that the model is only
    updated when motion occurs. For kinect/Xtion sensors this is a good
    idea. Default "0.01"
-   !ConvergenceCondition - *double* - If the estimated motion
    (described by a velocity vector) has a norm less than this, do no
    further iterations. Default ** 0.0001**
-   !MaximumRaycastSteps - *int* - When rendering the reconstructed
    model, step at most this many times along each pixel-ray before
    giving up. Default *12*
-   FocalLengthX - *double* - focal length *fx* of a pinhole camera
    model, measured in pixels, default **520.0**
-   FocalLengthY - *double* - focal length *fy* of a pinhole camera
    model, measured in pixels, default **520.0**
-   CenterPointX - *double* - principal point *cx* of a pinhole camera
    model, measured in pixels, default **319.5**
-   CenterPointY - *double* - principal point *cy* of a pinhole camera
    model, measured in pixels, default **239.5**

Aside from these parameters which directly control the behavior of the
tracker, other parameters can be set as well. These are specific to the
ROS node.

-   depth_registered - *bool* - if enabled, will cause the node to
    listen to the depth_registered topic, default **false**
-   c_name - *string* - the name of the camera, default is **camera**.
-   !OutputTriangles - *bool* - if enabled, will cause the node to call
    the tracker's saveTriangles() method before exiting. This will
    produce a file in the current directory called triangles.obj,
    generated using the marching tetrahedrons algorithm. Default
    **false**.
-   !OutputVolume - *bool* - if enabled, will cause the node to call the
    tracker's saveSDF method before exiting. This will produce a file
    in the current directory called sdf_volume.vti. This file can later
    be loaded using the loadSDF method. vti files can be opened using
    Paraview. Default **false**.
-   !LoadVolume - *string* - Provide the filename (e.g.
    "sdf_volume.vti") of the VTK image file containing an sdf volume
    that should be loaded at start. Default **"none"**.

```{=html}
<!-- -->
```
-   !UseTexture - *bool* - included for convenience. Edit the
    rgbCallback function to do something fun. Default **false**.

An example:



```
rosrun sdf_tracker sdf_tracker_node _c_name:="camera2" _depth_registered:="true" _OutputTriangles:="true" _CellSize:=0.02 _GridSizeX:=300
```



This will start the node, listening to /camera2/depth_registered/image,
using a voxel-size of 2cm in a grid of 300x256x256. Triangles will be
dumped to "triangles.obj" at the end of execution, which can be viewed
in meshlab.

![](attachment:mesh.jpg)

### Initial pose

The initial starting point of the camera is at the center of the
specified volume, looking along the z-axis. To change the initial camera
pose, relative to the volume set the *pose_offset* parameter of the
SDF_Parameter class and pass this to the constructor when initializing
your SDFTracker, e.g.,



```cplusplus
//Parameters for an SDFtracker object 
SDF_Parameters myParameters;

//Pose Offset as a transformation matrix
Eigen::Matrix4d initialTransformation = 
Eigen::MatrixXd::Identity(4,4);

//define translation offsets in x y z
initialTransformation(0,3) = 0.5;  //x 
initialTransformation(1,3) = 0.3;  //y
initialTransformation(2,3) = -1.4; //z

myParameters.pose_offset = initialTransformation;

//create the tracker object
SDFTracker myTracker(myParameters);
```



## Shutdown

In the interactive mode, pressing *q* or *<ESC>* sets a flag to notify
the node that it's time to shut down. Terminating the program with
ctrl-C works, but will not output triangles.

If interactive mode is not enabled, you will need to find some other way
of deciding when to stop running the program.
