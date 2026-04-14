## Description

The node \'\'kinect_2d_scanner\'\' makes easy to connect to a Kinect
sensor and publish equivalent 2D \"fake laser\" scans.

  -- -------------------------------------------------------------------------------------- --
     \<:width=\"99%\"\> ![](attachment:kinect_2d_scanner_screenshot_rviz_reconfigure.png)   
  -- -------------------------------------------------------------------------------------- --

Internally, the node uses \`mrpt-hwdrivers\` which in turn uses
\`libfreenect\` to directly open the sensor. Since only 2D scan data is
published here, you should employ this node only if you won\'t need the
3D points.

\'\'\'All obstacles within a frustum\'\'\' are considered and the
minimum distance is kept in each direction. The horizontal FOV of the
frustum is automatically computed from the intrinsic parameters of the
range camera, but the vertical FOV must be provided by the user, and
\'\'\'can be set to be asymetric\'\'\' which may be useful depending on
the zone of interest where to look for obstacles. See
[this video](http://www.youtube.com/watch?v=87WCumXwA38) for an
illustration of the frustum geometry and 3D obstacle points.

  -- ----------------------------------------------------------------------------- --
     \<:width=\"99%\"\> ![](attachment:kinect_2d_scanner_screenshot_frustum.png)   
  -- ----------------------------------------------------------------------------- --

All spatial transformations are riguorously taken into account in this
class, using the depth camera intrinsic calibration parameters.
[Calibration data](http://www.mrpt.org/Kinect_calibration) should be
provided in the format expected by MRPT (explain me!), but default
values will be used otherwise.

## Usage

Test with:

```bash
roscd kinect_2d_scanner
roslaunch kinect_2d_scanner_test.launch
```

Read
[kinect_2d_scanner_test.launch](http://mrpt-ros-pkg.googlecode.com/svn/trunk/mrpt_hwdrivers/kinect_2d_scanner/kinect_2d_scanner_test.launch)
for more details.

This node implements the [dynamic_reconfigure](dynamic_reconfigure)
interface.
