The photo package provides access to digital cameras. Much of the
underlying functionality is provide by the
[ gPhoto ]( http://gphoto.sourceforge.net/ ) libary. The system package
libgphoto2-2-dev or equivalent is required.

## Nodes



```clearsilver
node.0{
name= photo_node
desc= The usb camera node interfaces with standard USB cameras (e.g. the Logitech Quickcam) using libusb_cam and publishes images as sensor_msgs::Image.

srv {
  0.name= get_config
  0.type= photo/GetConfig
  0.desc= queries the value of a parameter

  1.name= set_config
  1.type = photo/SetConfig
  1.desc= sets the value for a given parameter

  2.name= capture
  2.type= photo/Capture
  2.desc= Image width
  
}
```



### test_photo

Calls the set_config service of photo_node and attempts to set the
exptime parameter to `20`.
