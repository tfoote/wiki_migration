```wiki
opencv2 ROS package deprecated (ROS Electric). It is now a third party package.
```

# Overview

For documentation on OpenCV, please see the
[Official OpenCV documentation](http://opencv.org/documentation.html).
For additional libraries to help you use OpenCV with ROS, please see the
[cv_bridge](cv_bridge) package and [vision_opencv](vision_opencv) stack.

{

## Package/stack dependencies

### When on Fuerte releasing for Electric

You just need the following: 1. `manifest.xml`
```
<rosdep name="opencv2"/>
```

### When on Electric releasing for Electric

The OpenCV rosdep is defined in the [vision_opencv](vision_opencv)
stack. You may depend on OpenCV by adding the following:

1\. `manifest.xml` ```
<depend package="cv_bridge" />

  <rosdep name="opencv2.3"/>
```

1\. `stack.xml` ```
<depend stack="vision_opencv" />
```

### Getting OpenCV

If you have updated your package and stack files following the
directions above, you can simply type:

```
rosdep install <your-package>
```

and [rosdep](rosdep) will automatically bring in the appropriate OpenCV
for your system.

*Manual apt-get install*

If you need to install OpenCV manually on Ubuntu, please follow the
instructions below.

1\. Verify that you have the latest ROS sources added to apt. See the
section
[ Setting up sources](http://www.ros.org/wiki/unstable/Installation/Ubuntu ) 1.
Install libopencv2.3-dev with apt. ```
sudo apt-get update
sudo apt-get install libopencv2.3-dev
``` }}}}

{

## Package/stack dependencies

### OpenCV only dependency

You just need the following: 1. `manifest.xml`
```
<rosdep name="opencv2"/>
```

### vision-opencv dependency

The OpenCV rosdep is defined in the [vision_opencv](vision_opencv)
stack. You may depend on OpenCV by adding the following:

1\. `manifest.xml` ```
<depend package="cv_bridge" />

  <rosdep name="opencv2"/>
```

1\. `stack.xml` ```
<depend stack="vision_opencv" />
```

### Getting OpenCV

If you have updated your package and stack files following the
directions above, you can simply type:

```
rosdep install <your-package>
```

and [rosdep](rosdep) will automatically bring in the appropriate OpenCV
for your system.

*Manual apt-get install*

If you need to install OpenCV manually on Ubuntu, please follow the
instructions below. ```
<rosdep name="opencv2"/>
```0 }}}}

## Report a Bug

If your issue is related to the OpenCV packaged in ROS (it is too old,
you would like to see a backport in there \...), please file a bug using
the link at [vision_opencv](vision_opencv).

For issues specific to OpenCV:

-   Send your question to the
    [OpenCV Answers](http://answers.opencv.org/).
-   [Report a bug](http://code.opencv.org/projects/opencv/issues?set_filter=1).

## Relationship to standalone library

{ }}}}

```
<rosdep name="opencv2"/>
```1}
