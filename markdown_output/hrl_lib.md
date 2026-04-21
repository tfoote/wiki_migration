This package provides a home for a useful set of miscellaneous Python
modules each too small to warrant having their own package.

## Utilities

### load_dynamic_config

This is a dynamic_reconfigure client that set the parameters given to it
on startup and unset/restore those same parameters when it exits.
Created for setting camera parameters on start up for the
laser_interface_node and restoring the default settings on shutdown.

On the command line: 

```
$ rosrun hrl_lib load_dynamic_config <node_name> <yaml_file>
```



Example usage in roslaunch file: 

```
<node name="$(anon dynam_load)" pkg="hrl_lib" type="load_dynamic_config" args="/wide_stereo_both $(find laser_interface)/office_exposure.yaml"/>
```



## Modules

-   util.py: A variety of utility functions for coding in Python.

```{=html}
<!-- -->
```
-   rutils.py: Utility classes for working with rospy.

```{=html}
<!-- -->
```
-   transforms.py: Basic functions for creating/decomposing homogeneous
    transformation matrices.

```{=html}
<!-- -->
```
-   data_process.py: various functions for processing time series data
    (histogram, gradient, interpolate, etc)

```{=html}
<!-- -->
```
-   data_display.py: display for time series that allow users to select
    segments from a GUI (based on pylab)
