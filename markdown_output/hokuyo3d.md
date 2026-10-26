  -- ------------------------------------------- -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     ![Experimental\|](attachment:1Column.png)      **EXPERIMENTAL**: This status indicates that this software is experimental code at best. There are known issues and missing functionality. The APIs are completely unstable and likely to change. Use in production systems is not recommended. All code starts at this level. For more information see the ROS-Industrial software status [page](Industrial/Software_Status).   
  -- ------------------------------------------- -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

![PointCloud published by hokuyo3d node\|width=100%](attachment:hokuyo3d_pointcloud.png)

## Supported Hardware

This driver should work with VSSP 1.0/1.1-compliant HOKUYO 3D-LIDARs.

## ROS API



```clearsilver
node.0 {
name=hokuyo3d
desc=`hokuyo3d` is a driver for VSSP 1.0/1.1 (Volumetric Scanning Sensor Protocol) compliant Hokuyo 3D LIDARs.
pub{
0.name= ~/hokuyo_cloud
0.type= sensor_msgs/PointCloud
0.desc= Output of measured point cloud in PointCloud message type which contains all multi echos with intensity. Published on demand.
1.name= ~/hokuyo_cloud2
1.type= sensor_msgs/PointCloud2
1.desc= Output of measured point cloud in PointCloud2 message type which contains all multi echos with intensity. Published on demand.
2.name= ~/imu
2.type= sensor_msgs/Imu
2.desc= Output of embedded 6D gyro and accelerometer data.
3.name= ~/mag
3.type= sensor_msgs/MagneticField
3.desc= Output of embedded 3D magnetic field vector.
}
param {
0.name= ~ip
0.default= "192.168.0.10"
0.type= string
0.desc= IP address of the sensor.
1.name= ~port 
1.default= 10940
1.type= int
1.desc= TCP Port of the sensor.
2.name= ~interlace
2.default= 4
2.type= int
2.desc= Interlace setting of laser scanning. One means no interlace.
3.name= ~frame_id
3.default= "hokuyo3d"
3.type= string
3.desc= The TF frame ID in which point clouds will be returned.
4.name= ~range_min
4.default=0.0
4.type= float
4.desc=Points within range_min are dropped. This parameter is useful to remove ghost points nearby for early development version of this 3D sensors.
5.name= ~output_cycle
5.default="field"
5.type= string
5.desc= Specifies timing of point cloud output. "frame": outputs for each interlace cycle (several fields), "field": one horizontal scan (tens of lines), "line": one vertical scan
}
}
```


