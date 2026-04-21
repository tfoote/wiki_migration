## Installation



```
svn co http://alufr-ros-pkg.googlecode.com/svn/trunk/freiburg_tools/gaussian_process
svn co http://alufr-ros-pkg.googlecode.com/svn/trunk/wifi_tools
rosdep install gaussian_process
sudo apt-get install libiw-dev
rosmake wifi_tools
```



## Example

### wifi_stumbler



```
~/ros_workspace/wifi_tools# rosrun wifi_tools wifitumbler
[ INFO] [1370261175.398384924]: mac_addr=00:23:CD:14:E1:DF
[ INFO] [1370261175.398595103]: mac_addr=E4:CE:8F:69:92:12
[ INFO] [1370261175.398655961]: mac_addr=00:25:4B:1A:FE:11
[ INFO] [1370261175.398707724]: mac_addr=00:1B:86:3B:32:32
[ INFO] [1370261175.398753935]: Found 4 AP.
```



This node has to be run by root authority.

## Nodes



```clearsilver
node.0 {
  name = wifi_stumbler
  desc = `wifi_stumbler` node collects wifi signal data.
  pub {
    0.name = wifi_tools/wifi_data
    0.type = wifi_tools/WifiData
    0.desc = The set of wifi signal strengthes and mac addresses.
  }
}
node.1 {
  name = wifi_mapping
  desc = `wifi_mapping` node associate wifi data to tf
  sub {
    0.name = wifi_tools/wifi_data
    0.type = wifi_tools/WifiData
    0.desc = wifi signal data.
    1.name = tf
    1.type = tf/tfMessage
    1.desc = This node needs `/odom` and `/base_link` transforms.
  }
  srv{
    0.name=/wifi_mapping/o2file 
    0.type= std_srvs/Empty
    0.desc= Output wifi map to .pcd file.
  }
}
node.3 {
  name = wifi_gaussian_process
  desc = `wifi_gaussian_process` node publish mean and covariance of wifi signals expressed by gaussian_process.
  pub {
    0.name = wifi_gpmean
    0.type = sensor_msgs/PointCloud2
    0.desc = A mean map of wifi signal. Topic names are suffixed by mac address.
    1.name = wifi_gpcov
    1.type = sensor_msgs/PointCloud2
    1.desc = A covariance map of wifi signal. Topic names are suffixed by mac address.
  }
  param {
    0.name= ~gp_x_min
    0.default=0.0
    0.type= double
    0.desc= Minimum range (x) of GP maps.
    1.name= ~gp_x_max
    1.default=10.0
    1.type= double
    1.desc= Maximum range (x) of GP maps.
    2.name= ~gp_y_min
    2.default=0.0
    2.type= double
    2.desc= Minimum range (y) of GP maps.
    3.name= ~gp_x_max
    3.default=10.0
    3.type= double
    3.desc= Maximum range (y) of GP maps.
    4.name= ~gp_x_interval
    4.default=1.0
    4.type= double
    4.desc= Interpolation interval (x).
    5.name= ~gp_y_interval
    5.default=1.0
    5.type= double
    5.desc= Interpolation interval (y).
    6.name= ~path_wifimap
    6.default="$(find wifi_tools)/map"
    6.type= string
    6.desc= Which file (.pcd) to use for the gp map.

  }
}
```



## Questions & Bugs

ito\[at\]informatik.uni-freiburg.de
