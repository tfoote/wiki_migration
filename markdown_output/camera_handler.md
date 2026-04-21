# Vision sensor

In V-REP it is possible to simulate a vision sensor. Vision sensors are
added to the scene with \[menu bar \--> Add \--> Vision sensor\].
After a double-click on a vision-sensor, we can set some parameters like
the resolution and the field of view of the camera. In addition we added
a GUI to set the frequency of acquisition and the type of color coding
(RGB or grayscale) that should be used.

![Camera Settings](attachment:VSgui.png)

NB: Start and stop the simulation two times after you change the
parameters in the GUI.

The handler will publish a stream of images in low-bandwidth compressed
formats using image_transport. In addition a topic called
'/vrep/camera_info' will be created. It contains the intrinsic camera
parameters.

## Publishers

Let's suppose we have a vision sensor in V-REP called
"Vision_sensor_0". The plugin will create the following topics:



```
/vrep/Vision_sensor_0
 /vrep/Vision_sensor_0/Camerainfo
 /vrep/Vision_sensor_0/compressed
 /vrep/Vision_sensor_0/compressed/parameter_descriptions
 /vrep/Vision_sensor_0/compressed/parameter_updates
 /vrep/Vision_sensor_0/compressedDepth
 /vrep/Vision_sensor_0/compressedDepth/parameter_descriptions
 /vrep/Vision_sensor_0/compressedDepth/parameter_updates
 /vrep/Vision_sensor_0/theora
 /vrep/Vision_sensor_0/theora/parameter_descriptions
 /vrep/Vision_sensor_0/theora/parameter_updates
```


