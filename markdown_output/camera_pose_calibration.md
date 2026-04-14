```
{#!wiki version indigo_and_newer

{{{#!wiki caution
This is a new package. This package is unrelated to the camera_pose_calibration package which was supported up to and including Groovy.
```

More information can be found in the readme at
<https://github.com/delftrobotics/camera_pose_calibration> }}}} { or

```
sudo apt-get install ros-fuerte-camera-pose
``` Make sure you add \`/opt/ros/diamondback\` or
\`/opt/ros/electric\` to you ROS_PACKAGE_PATH.

Source-only installations are currently quite difficult because of the
large number of dependencies. This will become easier in future
releases.

### Setting up your launch files

![](attachment:high_level_flow_launch.png)

To use the camera pose calibration, you need to include on of the
calibration_tf_publisher.launch file in your own launch file:

```

``` This launch file will listen to the output of
the calibration optimization routine, and publish the result to
[tf](tf). The result of the calibration will also be saved to disk
(/tmp/megacal_cache.bag) so the last calibration results get
automatically loaded when you restart the cameras. Initially, when the
camera\'s are still uncalibrated, nothing will get published to
[tf](tf). Only once the first checkerboard has been captured, the tf
publishing will start.

### Running calibration

Before running the calibration, start your own launch files that start
up the cameras. Make sure this launch file includes the calibration tf
publisher as described above. While calibrating, it is okay to keep
nodes that are not related to the calibration running. This makes it
possible to do \'online\' calibration.

The camera pose calibration package has a few sample launch files, for
2, 3 or 4 camera\'s.

Launching with arguments could look like this:

```

``` To make these launch files work for your own
camera setup, you need to specify several arguments to the launch files:

-   \'\'\'camera\[n\]\_ns\'\'\': the namespace of the \[n\]th camera. In
    this namespace, the calibration expects to find the image topics
    \`camera_info\` and \`image_rect\` for the \[n\]th camera. You
    should repeat this parameter for all your camera\'s.

```{=html}
<!-- -->
```
-   \'\'\'checker_rows\'\'\': the number of checker corners
    horizontally.

```{=html}
<!-- -->
```
-   \'\'\'checker_cols\'\'\': the number of checker corners vertically.

```{=html}
<!-- -->
```
-   \'\'\'checker_size\'\'\': the size of one checker (in meters).

![\|width=\"400\"](attachment:checker.png)

Once the calibration launch file is running (and shows no errors), you
can start capturing checkerboard poses. The calibration viewer helps you
run and debug capturing checkerboard poses.

\'\'\'Some basic checks:\'\'\'

-   You see images for every camera in your system
-   The entire checkerboard is visible in all cameras simultaneously
-   The checkerboard corners are detected in each camera (shown by green
    circles on all corners)

The bar below each image shows how long the checkerboard has been
stationary in that image. Once all the bars are green, you\'ll hear a
\'beep\' sound, indicating that a calibration sample was captured.

After every checkerboard capture, the non-linear optimizer will compute
the relative camera poses and publish the results to [tf](tf). You can
capture as many checkerboard poses as you want.

![\|width=\"700\"](attachment:aggregate.png)

![\|width=\"300\"](attachment:success.png)

}}}}
