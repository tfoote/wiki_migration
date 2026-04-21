## ROS API



```clearsilver
node.0 {
name=odor_bar
desc=`odor_bar` is a visualization tool that displays the current odor concentration by the means of a bar of visualization_msgs/Marker (cubes in this case). In a (near) future we expect to add this functionality for other data besides odor concentration. 
pub{
0.name= odor_bars
0.type= visualization_msgs/Marker
0.desc= A set of markers (cubes) proportional to the received chemical data.
}
sub{
0.name= nose
0.type= lse_sensor_msgs/Nostril
0.desc= Chemical data from the MOX sensor(s).
}
param {
0.name= ~bar_frame_id
0.default= /base_link
0.type= string
0.desc= The frame_id of the odor bar. By default it moves with the robot.
1.name= ~nose_frame_id
1.default= /base_nose
1.type= string
1.desc= The frame_id from the nostril to extract the data from.
2.name= ~scale/x
2.default= 0.15
2.type= float
2.desc= The size of the x component of the cube.
3.name= ~scale/y
3.default= 0.15
3.type= float
3.desc= The size of the y component of the cube.
4.name= ~scale/z
4.default= 0.15
4.type= float
4.desc= The size of the z component of the cube.
5.name= ~hsv_s
5.default= 1.0
5.type= float
5.desc= The S (saturation) component of the HSV color space. It should be constant.
6.name= ~hsv_v
6.default= 1.0
6.type= float
6.desc= The V (value) component of the HSV color space. It should be constant.
7.name= ~hue_max
7.default= 200.0
7.type= float
7.desc= The maximum value for H (hue) component of the HSV color space.
8.name= ~hue_min
8.default= 0.0
8.type= float
8.desc= The minimum value for H (hue) component of the HSV color space.
}
}
```


