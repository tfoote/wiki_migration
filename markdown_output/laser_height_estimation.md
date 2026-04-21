![](attachment:laser_height_estimation_mirrors_01.png)

![](attachment:laser_height_estimation_mirrors_02.png)

## CAD Files

The CAD files to build your own can be found
[here](http://www.thingiverse.com/thing:3949) on
[thingiverse](http://www.thingiverse.com)

## Usage

The package provides a height estimate using a Hokuyo laser scanner.

## Details

Laser scan data is split using
[laser_scan_splitter](laser_scan_splitter) and the regions being
reflected downward or upward are fed into the height estimation system.

## Example

You can run the [laser_height_estimation](laser_height_estimation) on a
pre-recorded bag file that comes with the package. First, make sure you
have the [scan_tools](scan_tools) stack downloaded and installed by
following the instructions [here](scan_tools#Installing).

Next, make sure you have the necessary tools installed:



```shell
rosmake rviz tf rosbag
```



Finally, run the demo:



```shell
roslaunch laser_height_estimation demo.launch
```



## Nodes

## References

This package was inspired by the work of
[Grzonka et al](http://www.slawomir.de/publications/grzonka09icra/grzonka09icra.pdf)
[He et al](http://groups.csail.mit.edu/rrg/papers/icra08-rh.pdf)

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports.

Please use our [Trac](http://robotics.ccny.cuny.edu/trac/) to
[report bugs](http://robotics.ccny.cuny.edu/trac/newticket?component=ccny_vision/ar_pose&type=defect)
or
[request features](http://robotics.ccny.cuny.edu/trac/newticket?component=ccny_vision/ar_pose&type=enhancement).
