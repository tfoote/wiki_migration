![](attachment:piimagers.jpg)

## ROS Nodes



```clearsilver
node.0 {
 name = optris_imager_node
 desc = ROS driver node that publishes thermal data (and if available images from the visible spectrum).
 pub {
  0.name= thermal_image
  0.type= sensor_msgs/Image
  0.desc= thermal image in unsigned short representation. Temperature data is encoded as: float t = (float)(data - 1000) / 10.f.
  1.name= visible_image
  1.type= sensor_msgs/Image
  1.desc= color coded image in YUV422 format from visible channel (only for PI200/PI230 with bi-spectral technology)
  2.name= internal_temperature
  2.type= optris_drivers/Temperature
  2.desc= temperatures of shutter flag/chip surface/housing
  3.name= flag_state
  3.type= optris_drivers/Flag
  3.desc= state of shutter flag
}
param {
  1.name= xmlConfig
  1.type= string
  1.desc= XML configuration file name containing information about field of view, temperature range and desired frame rate (see config directory for an example). It is mandadory that parameters "fov" and "temperature range" agree with your calibration files. The calibration is chosen in dependency of these parameters (see troubleshooting below).
 }
}
srv{
  0{
  name = ~auto_flag
  type = optris_drivers/AutoFlag
  desc = enables and disables the automatic flag control.
  }
  1{
  name = ~force_flag
  type = std_srvs/Empty
  desc = forces camera to trigger a closing/opening event of shutter flag
  }
  2{
  name = ~set_temperature_range
  type = optris_drivers/TemperatureRange
  desc = sets temperature range
  }
}
```

 

```clearsilver
node.1 {
 name = optris_colorconvert_node
 desc = ROS driver node that subscribes the data topics of optris_imager_node (thermal_image and if available visible_image). Data is converted into displayable color representations.
 pub {
  1.name= thermal_image_view
  1.type= sensor_msgs/Image
  1.desc= color encoded image to be displayed with e.g. image_view
  2.name= visible_image_view
  2.type= sensor_msgs/Image
  2.desc= RGB image from visible channel (bi-spectral technology necessary, only PI200/PI230)
}
param {
  1.name= palette
  1.type= int
  1.desc= coloring palette in the range of 1..12
  1.default= 6
  2.name= paletteScaling
  2.type= int
  2.desc= scaling method for color conversion (determination of temperature bounds for high contrast coloring, 1=manual, 2=min/max, 3=1sigma, 4=3sigma)
  2.default= 2
  3.name= temperatureMin
  3.type= int
  3.desc= minimum value of temperature range (if manual scaling method chosen)
  3.default= 20
  4.name= temperatureMax
  4.type= int
  4.desc= maximum value of temperature range (if manual scaling method chosen)
  4.default= 40
 }
}
srv{
  0{
  name = ~palette
  type = optris_drivers/Palette
  desc = switches color conversion palette (valid values: 1..12).
  }
}
```




```clearsilver
node.2 {
 name = optris_binary_image_node
 desc = ROS driver node that subscribes the data topics of optris_imager_node (thermal_image). Data is converted into monochrome color representations, suitable for camera calibration. The package dynamic_reconfigure can be used to change the threshold on run-time.
 pub {
  1.name= thermal_binary_image
  1.type= sensor_msgs/Image
  1.desc= monochrome encoded image to be displayed with e.g. image_view
}
param {
  1.name= threshold
  1.type= double
  1.desc= temperature threshold to generate binary image from thermal image
  1.default= 40
  2.name= invert
  2.type=bool
  2.desc= flag to invert binary image 
  2.default=false
 }
}
```



## Basic Installation

Binary driver versions for the Optris thermal imager series are
available for i386, amd64, atom, armel and eabihf architectures. Debian
packages can be downloaded from
[evocortex](http://www.evocortex.org/downloads-1/). The driver is
available for different platforms (i386, amd64, armel, armhf, arm64).

Please follow the
[installation instructions](http://documentation.evocortex.com/libirimager2/html/index.html).
It is best to check a proper installation with the contained example
applications.

## Examples

![](attachment:optris_max.png) ![](attachment:optris_teepot.png)
![](attachment:optris_pot.png)

Start driver node that publishes thermal data.



```
$ rosrun optris_drivers optris_imager_node _xmlConfig:=config/12090031.xml
```

 The xml configuration file is camera specific.
It comprises the following values:

-   fov: optic's field of view
-   temperature min: minimum value of temperature range
-   temperature max: maximum value of temperature range
-   framerate: desired framerate for the grabbing callback. This value
    needs to be less or equal the camera's maximum framerate.
-   controller: HID (=1) or pure UVC (=2) interface. In most cases this
    option is HID (cameras having a pure UVC controller interface need a
    special firmware version).
-   outputmode: temperature data (=2) or energy data (=1). In most cases
    temperature data is what you want. Energy data is provided for
    experimental use.
-   bispectral: available and utilized (=1), not available or
    deactivated (=0). Bi-spectral technology is only available for PI200
    and PI230 devices. Do not set this parameter to 1 for any other
    device.

Start color conversion node, that publishes data in false color
representation.



```
$ rosrun optris_drivers optris_colorconvert_node _palette:=6 _paletteScaling:=2 _temperatureMin:=10 _temperatureMax:=30
```

 Alternatively, both nodes are started in the
namespace "optris" with



```
$ roslaunch optris_drivers.launch
```

 Display thermal images in false color code



```
$ rosrun image_view image_view image:=/optris/thermal_image_view
```

 Switch off automatic shutter flag control



```
$ rosservice call /optris/optris_imager_node/auto_flag 0
```

 Trigger shutter flag manually



```
$ rosservice call /optris/optris_imager_node/force_flag
```



### Using Compression

The default image transport format is raw. If you have to tunnel data
over a low-bandwidth network, you can employ the PNG compression
mechanism of image_transport. Launch the subscriber of the thermal_image
topic with the following _image_transport option:



```
$ rosrun optris_drivers optris_colorconvert_node _palette:=6 _paletteScaling:=2 _temperatureMin:=10 _temperatureMax:=30 _image_transport:=compressed
```

 Since thermal images are in 1-channel 16-Bit
integer format, JPEG compression can not be used. Moreover, JPEG is not
lossless. Switch to PNG with:



```clearsilver
node.1 {
 name = optris_colorconvert_node
 desc = ROS driver node that subscribes the data topics of optris_imager_node (thermal_image and if available visible_image). Data is converted into displayable color representations.
 pub {
  1.name= thermal_image_view
  1.type= sensor_msgs/Image
  1.desc= color encoded image to be displayed with e.g. image_view
  2.name= visible_image_view
  2.type= sensor_msgs/Image
  2.desc= RGB image from visible channel (bi-spectral technology necessary, only PI200/PI230)
}
param {
  1.name= palette
  1.type= int
  1.desc= coloring palette in the range of 1..12
  1.default= 6
  2.name= paletteScaling
  2.type= int
  2.desc= scaling method for color conversion (determination of temperature bounds for high contrast coloring, 1=manual, 2=min/max, 3=1sigma, 4=3sigma)
  2.default= 2
  3.name= temperatureMin
  3.type= int
  3.desc= minimum value of temperature range (if manual scaling method chosen)
  3.default= 20
  4.name= temperatureMax
  4.type= int
  4.desc= maximum value of temperature range (if manual scaling method chosen)
  4.default= 40
 }
}
srv{
  0{
  name = ~palette
  type = optris_drivers/Palette
  desc = switches color conversion palette (valid values: 1..12).
  }
}
```

0 or with the help of a graphical interface:



```clearsilver
node.1 {
 name = optris_colorconvert_node
 desc = ROS driver node that subscribes the data topics of optris_imager_node (thermal_image and if available visible_image). Data is converted into displayable color representations.
 pub {
  1.name= thermal_image_view
  1.type= sensor_msgs/Image
  1.desc= color encoded image to be displayed with e.g. image_view
  2.name= visible_image_view
  2.type= sensor_msgs/Image
  2.desc= RGB image from visible channel (bi-spectral technology necessary, only PI200/PI230)
}
param {
  1.name= palette
  1.type= int
  1.desc= coloring palette in the range of 1..12
  1.default= 6
  2.name= paletteScaling
  2.type= int
  2.desc= scaling method for color conversion (determination of temperature bounds for high contrast coloring, 1=manual, 2=min/max, 3=1sigma, 4=3sigma)
  2.default= 2
  3.name= temperatureMin
  3.type= int
  3.desc= minimum value of temperature range (if manual scaling method chosen)
  3.default= 20
  4.name= temperatureMax
  4.type= int
  4.desc= maximum value of temperature range (if manual scaling method chosen)
  4.default= 40
 }
}
srv{
  0{
  name = ~palette
  type = optris_drivers/Palette
  desc = switches color conversion palette (valid values: 1..12).
  }
}
```

1 With rxgraph the usage of compression can be
verified. The remaining bandwidth can be displayed with:



```clearsilver
node.1 {
 name = optris_colorconvert_node
 desc = ROS driver node that subscribes the data topics of optris_imager_node (thermal_image and if available visible_image). Data is converted into displayable color representations.
 pub {
  1.name= thermal_image_view
  1.type= sensor_msgs/Image
  1.desc= color encoded image to be displayed with e.g. image_view
  2.name= visible_image_view
  2.type= sensor_msgs/Image
  2.desc= RGB image from visible channel (bi-spectral technology necessary, only PI200/PI230)
}
param {
  1.name= palette
  1.type= int
  1.desc= coloring palette in the range of 1..12
  1.default= 6
  2.name= paletteScaling
  2.type= int
  2.desc= scaling method for color conversion (determination of temperature bounds for high contrast coloring, 1=manual, 2=min/max, 3=1sigma, 4=3sigma)
  2.default= 2
  3.name= temperatureMin
  3.type= int
  3.desc= minimum value of temperature range (if manual scaling method chosen)
  3.default= 20
  4.name= temperatureMax
  4.type= int
  4.desc= maximum value of temperature range (if manual scaling method chosen)
  4.default= 40
 }
}
srv{
  0{
  name = ~palette
  type = optris_drivers/Palette
  desc = switches color conversion palette (valid values: 1..12).
  }
}
```

2 If you use the roslaunch file, uncomment the
following line



```clearsilver
node.1 {
 name = optris_colorconvert_node
 desc = ROS driver node that subscribes the data topics of optris_imager_node (thermal_image and if available visible_image). Data is converted into displayable color representations.
 pub {
  1.name= thermal_image_view
  1.type= sensor_msgs/Image
  1.desc= color encoded image to be displayed with e.g. image_view
  2.name= visible_image_view
  2.type= sensor_msgs/Image
  2.desc= RGB image from visible channel (bi-spectral technology necessary, only PI200/PI230)
}
param {
  1.name= palette
  1.type= int
  1.desc= coloring palette in the range of 1..12
  1.default= 6
  2.name= paletteScaling
  2.type= int
  2.desc= scaling method for color conversion (determination of temperature bounds for high contrast coloring, 1=manual, 2=min/max, 3=1sigma, 4=3sigma)
  2.default= 2
  3.name= temperatureMin
  3.type= int
  3.desc= minimum value of temperature range (if manual scaling method chosen)
  3.default= 20
  4.name= temperatureMax
  4.type= int
  4.desc= maximum value of temperature range (if manual scaling method chosen)
  4.default= 40
 }
}
srv{
  0{
  name = ~palette
  type = optris_drivers/Palette
  desc = switches color conversion palette (valid values: 1..12).
  }
}
```

3 and remind the namespace "optris".

### Using BI-SPECTRAL technology

PI 200/230 cameras support a second image channel. Verify that in the
corresponding configuration file, bispectral is set to 1. The topic
visible_image is providing a yuv422 image format, either in raw or PNG
coding depending on _image_transport. Ensure that the compression is
set to PNG, JPEG is not supporting yuv422 for the moment. Starting
optris_colorconvert_node subscribes to visible_image and publishes
visible_image_view, which is in rgb8 format. Either raw or PNG/JPEG
compression can be used.



```clearsilver
node.1 {
 name = optris_colorconvert_node
 desc = ROS driver node that subscribes the data topics of optris_imager_node (thermal_image and if available visible_image). Data is converted into displayable color representations.
 pub {
  1.name= thermal_image_view
  1.type= sensor_msgs/Image
  1.desc= color encoded image to be displayed with e.g. image_view
  2.name= visible_image_view
  2.type= sensor_msgs/Image
  2.desc= RGB image from visible channel (bi-spectral technology necessary, only PI200/PI230)
}
param {
  1.name= palette
  1.type= int
  1.desc= coloring palette in the range of 1..12
  1.default= 6
  2.name= paletteScaling
  2.type= int
  2.desc= scaling method for color conversion (determination of temperature bounds for high contrast coloring, 1=manual, 2=min/max, 3=1sigma, 4=3sigma)
  2.default= 2
  3.name= temperatureMin
  3.type= int
  3.desc= minimum value of temperature range (if manual scaling method chosen)
  3.default= 20
  4.name= temperatureMax
  4.type= int
  4.desc= maximum value of temperature range (if manual scaling method chosen)
  4.default= 40
 }
}
srv{
  0{
  name = ~palette
  type = optris_drivers/Palette
  desc = switches color conversion palette (valid values: 1..12).
  }
}
```

4

## Troubleshooting

If you cannot get image data from above mentioned topics, check

-   \... whether nodes are connected properly, i.e.
    optris_colorconvert_node is subscribing from optris_imager_node.
-   \... whether the USB bandwidth is sufficient. Unplug every other
    device on the same USB bus. You can list all attached devices with
    lsusb -t. Ensure that the thermal imager is the only device on a
    certain bus.
-   \... if you can get data with guvcview or a similar UVC grabbing
    module. The frame rate should be >> 1, if not the "nodrop"
    option might help. If permissions are missing, you need to apply
    udev rules before connecting the device. An example for those udev
    rules is included in this package.
-   \... if calibration files for your camera (compare serial number,
    field of view and temperature range) are present (path can be set
    with the xml configuration, default: /usr/share/libirimager/cali)
    and whether they are readable with your system account. The serial
    number is determined automatically, if it is not set in the
    xmlConfig file. Field of view and temperature range need to be
    adjusted in this xmlConfig file, too. The calibration files are
    looked up in dependency of these settings, e.g.,



```clearsilver
node.1 {
 name = optris_colorconvert_node
 desc = ROS driver node that subscribes the data topics of optris_imager_node (thermal_image and if available visible_image). Data is converted into displayable color representations.
 pub {
  1.name= thermal_image_view
  1.type= sensor_msgs/Image
  1.desc= color encoded image to be displayed with e.g. image_view
  2.name= visible_image_view
  2.type= sensor_msgs/Image
  2.desc= RGB image from visible channel (bi-spectral technology necessary, only PI200/PI230)
}
param {
  1.name= palette
  1.type= int
  1.desc= coloring palette in the range of 1..12
  1.default= 6
  2.name= paletteScaling
  2.type= int
  2.desc= scaling method for color conversion (determination of temperature bounds for high contrast coloring, 1=manual, 2=min/max, 3=1sigma, 4=3sigma)
  2.default= 2
  3.name= temperatureMin
  3.type= int
  3.desc= minimum value of temperature range (if manual scaling method chosen)
  3.default= 20
  4.name= temperatureMax
  4.type= int
  4.desc= maximum value of temperature range (if manual scaling method chosen)
  4.default= 40
 }
}
srv{
  0{
  name = ~palette
  type = optris_drivers/Palette
  desc = switches color conversion palette (valid values: 1..12).
  }
}
```

5 . will configure the file names:



```clearsilver
node.1 {
 name = optris_colorconvert_node
 desc = ROS driver node that subscribes the data topics of optris_imager_node (thermal_image and if available visible_image). Data is converted into displayable color representations.
 pub {
  1.name= thermal_image_view
  1.type= sensor_msgs/Image
  1.desc= color encoded image to be displayed with e.g. image_view
  2.name= visible_image_view
  2.type= sensor_msgs/Image
  2.desc= RGB image from visible channel (bi-spectral technology necessary, only PI200/PI230)
}
param {
  1.name= palette
  1.type= int
  1.desc= coloring palette in the range of 1..12
  1.default= 6
  2.name= paletteScaling
  2.type= int
  2.desc= scaling method for color conversion (determination of temperature bounds for high contrast coloring, 1=manual, 2=min/max, 3=1sigma, 4=3sigma)
  2.default= 2
  3.name= temperatureMin
  3.type= int
  3.desc= minimum value of temperature range (if manual scaling method chosen)
  3.default= 20
  4.name= temperatureMax
  4.type= int
  4.desc= maximum value of temperature range (if manual scaling method chosen)
  4.default= 40
 }
}
srv{
  0{
  name = ~palette
  type = optris_drivers/Palette
  desc = switches color conversion palette (valid values: 1..12).
  }
}
```

6

-   For PI400/450: If your application is crashing while calling the
    constructor, check whether the file Formats.def has the following
    entry:



```clearsilver
node.1 {
 name = optris_colorconvert_node
 desc = ROS driver node that subscribes the data topics of optris_imager_node (thermal_image and if available visible_image). Data is converted into displayable color representations.
 pub {
  1.name= thermal_image_view
  1.type= sensor_msgs/Image
  1.desc= color encoded image to be displayed with e.g. image_view
  2.name= visible_image_view
  2.type= sensor_msgs/Image
  2.desc= RGB image from visible channel (bi-spectral technology necessary, only PI200/PI230)
}
param {
  1.name= palette
  1.type= int
  1.desc= coloring palette in the range of 1..12
  1.default= 6
  2.name= paletteScaling
  2.type= int
  2.desc= scaling method for color conversion (determination of temperature bounds for high contrast coloring, 1=manual, 2=min/max, 3=1sigma, 4=3sigma)
  2.default= 2
  3.name= temperatureMin
  3.type= int
  3.desc= minimum value of temperature range (if manual scaling method chosen)
  3.default= 20
  4.name= temperatureMax
  4.type= int
  4.desc= maximum value of temperature range (if manual scaling method chosen)
  4.default= 40
 }
}
srv{
  0{
  name = ~palette
  type = optris_drivers/Palette
  desc = switches color conversion palette (valid values: 1..12).
  }
}
```

7
