See <http://rc-visard.com> and <http://doc.rc-visard.com> for more
details.



```wiki
This package is still in development and the API might change in the future. Please report any bugs or feature requests on [[https://github.com/roboception/rc_visard_ros/issues|GitHub]].
```



## Overview

This component provides an interactive markers based graphical interface
on rviz. It's focus is to manage, edit and define regions of interest
for a specific module on the rc_visard sensor.

## Configuration

### Parameters

-   `device`: The ID of the device, i.e. Roboception rc_visard sensor.
    This can be either:

```{=html}
<!-- -->
```
-   serial number, e.g. `02912345`. 

```wiki
Preceed with a colon (`:02912345`) when passing this on the commandline or setting it via rosparam (see https://github.com/ros/ros_comm/issues/1339). This is not neccessary when specifying it as a string in a launch file.
```



```{=html}
<!-- -->
```
-   user defined name must be unique among all reachable sensors. If no
    device or host is given, this parameter works if just one rc_visard
    is connected.

## Launch

Using command line parameters:

For the [ItemPick](https://roboception.com/product/itempick/) module:


```bash
$ roslaunch rc_roi_manager_gui interactive_roi_selection.launch device:=:<serial_number> pick_module:=rc_itempick
```



For the [BoxPick](https://roboception.com/product/boxpick/) module:


```bash
$ roslaunch rc_roi_manager_gui interactive_roi_selection.launch device:=:<serial_number> pick_module:=rc_boxpick
```



## Report a Bug

## Acknowledgements

[Included page rosin/acknowledgement not found](Included page rosin/acknowledgement not found)
