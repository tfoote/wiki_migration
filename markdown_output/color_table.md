## ROS Nodes

```clearsilver
node.0 {
 name = color_table
 desc = Read a bag file recorded from the kinect and generate color lookup tables.
}
```

#### Obtaining the bag file

1\. Launch the openni_kinect driver ```
roslaunch openni_camera openni_node.launch
```

2\. Verify that the kinect is publishing the image. Run the following
command in a separate tab. ```
rosrun image_view image_view image:=/camera/rgb/image_color
```

3\. Ensure that the kinect is pointing at some appropriate colors that
you wish to segment. Run the following command in a separate tab to
record the bag file. ```
rosbag record /camera/rgb/image_color
``` More instructions on using
rosbag are available [here](rosbag/Commandline#record);

#### Constructing the color lookup table

1\. Launch the tool ```
rosrun color_table color_table
```

2\. Open up a bag file *(Ctrl + 0)*

3\. The default color table is automatically loaded. Use the
classification window to adjust the color table. *Remember to save the
table when you are done!*
