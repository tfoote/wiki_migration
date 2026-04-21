Home of the unnoficial ROS driver for MatrixVision BlueFox cameras.

## Installing the mvIMPACT Acquire Library

1\. Download the latest drivers from Matrix-Vision
[ drivers page](http://www.matrix-vision.com/mvvirtualdevice-442.html ):
. Select mvBlueFOX / mvBlueFOX-MLC in the drop down fields. Download the
latest Linux drivers (e.g. mvVirtualDevice x86_XXXXXXXX.tgz) and unpack
the archive in to a directory: ```shell
$ cd ~/src (or wherever you want to install this package)
$ tar xvzf mvVirtualDevice\ x86_XXXXXXXX.tgz

# It  may just be enough to copy the contents of the “lib” folder (including sumlinks) into /usr/local/lib, as:
$ cd your_path_to_mvIMPACT_acquire-XXXXXXX/lib
$ sudo cp -P lib* /usr/local/lib/
$ sudo ldconfig

# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# NEEDS REVISION:
# Copy the included udev rules for the device from your mv_bluefox_driver directory (TODO)
$ sudo cp path_to/mv_bluefox_driver/rules/51-mvbf.rules /etc/udev/rules.d/
# Unplug the camera and restart the udev service:
$ sudo service udev restart
# Plug back the camera

# Now, compile the apps given as demo:
$ cd your_path_to_mvIMPACT_acquire-XXXXXXX/apps
$ make

# You may want to run the wxPropGrid to test the camera
$ cd your_path_to_mvIMPACT_acquire-XXXXXXX/wxPropGrid
$ make
# Run the wxPropView program
$./wxPropView
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

## Example

The driver can be run as a regular node by launching:
```shell
roslaunch mv_bluefox_driver camera_node.launch
```

OR

The driver can be launched as a *nodelet* as: ```shell
roslaunch mv_bluefox_driver camera_nodelet.launch
```

The camera can be calibrated via the
[camera_calibration](camera_calibration) package from
[image_pipeline](image_pipeline) by launching: ```shell
roslaunch mv_bluefox_driver calibrate_camera.launch
```
**NOTE:** You must modify the checkerboard patter calibration parameters
to suit your own.

After a *.yaml* calibration file has been properly generated, the actual
rectified images can be processed further via
[image_pipeline](image_pipeline)'s [image_proc](image_proc). Thus, the
following launchers achieve that, respectively. ```shell
roslaunch mv_bluefox_driver camera_node_proc.launch
```
OR ```shell
roslaunch mv_bluefox_driver camera_nodelet_proc.launch
```

## Nodes

```clearsilver
 name = mv_bluefox_driver
 desc = The `mv_bluefox_driver` node wraps the official driver for MatrixVision ''BlueFox'' devices and advertises <<MsgLink(sensor_msgs/Image)>> messages published by `image_transport::Publisher` ([[http://www.ros.org/doc/api/image_transport/html/classimage__transport_1_1Publisher.html|API]]) as well as the corresponding camera information as <<MsgLink(sensor_msgs/CameraInfo)>>. These can be further processed via the [[image_pipeline]]'s [[image_proc]] (see the [[#Example|Example]] section for launching).

 pub {
   0{
    name = ~camera_info
    type = sensor_msgs/CameraInfo
    desc = Camera parameters information server
   }
   1{
    name = ~image_raw
    type = sensor_msgs/Image
    desc = Unprocessed (raw) image data
   }
  }
 param{
    0.name = ~frame_id
    0.type = string
    0.default = `camera`
    0.desc = The camera's frame name (id).

    1.name = ~calibration_file
    1.type = string
    1.default = `""`
    1.desc = The camera_info path and name for the calibration `yaml` file (e.g. "whatever_path/mv_bluefox_calibration.yaml")
 
}
```

## TODO

1\. Add more configurable parameters. For now, only the default camera
resolution is being used.
