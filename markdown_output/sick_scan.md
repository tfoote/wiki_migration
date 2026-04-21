ROS packages for SICK laser scaners. This driver provides the
measurement data as
[PointCloud2](http://docs.ros.org/api/sensor_msgs/html/msg/PointCloud2.html)
and
[LaserScan](http://docs.ros.org/api/sensor_msgs/html/msg/LaserScan.html)
data. The use of
[PointCloud2](http://docs.ros.org/api/sensor_msgs/html/msg/PointCloud2.html)
data is recommended.

The
[LaserScan](http://docs.ros.org/api/sensor_msgs/html/msg/LaserScan.html)
data should only be used for debugging purposes. They provide the raw
data for each scan plane in a different coordinate frame. Due to the
geometry of the scanning planes of the MRS1104 there is no coordinate
transformation between the scan planes that can be described by
[tf](http://wiki.ros.org/tf) messages, therefore no
[tf](http://wiki.ros.org/tf) messages are published. That is why the
[PointCloud2](http://docs.ros.org/api/sensor_msgs/html/msg/PointCloud2.html)
data should be used.

## Devices Supported

The driver supports at least the scanners listed below and has also been
tested with these devices:

  -- ------------------ -- ----------------------------------------------------------------------------------------------------------------------------------- -- ----------------------------------------------------- -- -------------- --
     **device name**       **part no.**                                                                                                                           **description**                                          **tested?**    
     MRS6124               [6065086](https://www.sick.com/de/de/mess-und-detektionsloesungen/3d-lidar-sensoren/mrs6000/mrs6124r-131001/p/p533545)                 24 layer (standard)                                      ✔ \[stable\]   
     MRS1104               [1081208](https://www.sick.com/sg/en/detection-and-ranging-solutions/3d-lidar-sensors/mrs1000/mrs1104c-111011/p/p495044)               4 layer                                                  ✔ \[stable\]   
     LMS1104               [1092445](https://www.sick.com/us/en/detection-and-ranging-solutions/2d-lidar-sensors/lms1000/c/g387151)                               1 layer (based on MRS1104 technology)                    ✔ \[stable\]   
     TiM551                [1060445](https://www.sick.com/media/docs/9/29/229/Operating_instructions_TiM55x_TiM56x_TiM57x_de_IM0051229.PDF)                       1 layer max. range: 10m, ang. resol. 1.00\[deg\]         ✔ \[stable\]   
                                                                                                                                                                  Scan-Rate: 15 Hz                                                        
     TiM561                [1071419](https://www.sick.com/media/docs/9/29/229/Operating_instructions_TiM55x_TiM56x_TiM57x_de_IM0051229.PDF)                       1 layer max. range: 10m, ang. resol. 0.33 \[deg\]        ✔ \[stable\]   
                                                                                                                                                                  Scan-Rate: 15 Hz                                                        
     TiM571                [1079742](https://www.sick.com/media/docs/9/29/229/Operating_instructions_TiM55x_TiM56x_TiM57x_de_IM0051229.PDF)                       1 layer max. range: 25m, ang. resol. 0.33 \[deg\]        ✔ \[stable\]   
                                                                                                                                                                  Scan-Rate: 15 Hz                                                        
     TiM781                [1096807](https://www.sick.com/de/de/mess-und-detektionsloesungen/2d-lidar-sensoren/tim7xx/tim781-2174101/p/p594148)                   1 layer max. range: 25 m, ang. resol. 0.33 \[deg\]       ✔ \[stable\]   
                                                                                                                                                                  Scan-Rate: 15 Hz                                                        
     TiM781S               [1096363](https://www.sick.com/de/de/mess-und-detektionsloesungen/2d-lidar-sensoren/tim7xx/tim781s-2174104/p/p594149)                  1 layer max. range: 25 m, ang. resol. 0.33 \[deg\]       ✔ \[stable\]   
                                                                                                                                                                  Scan-Rate: 15 Hz                                                        
     LMS4xxx-Family        [1091423](https://www.sick.com/de/de/mess-und-detektionsloesungen/2d-lidar-sensoren/lms4000/lms4111r-13000/p/p578044?ff_data)          1 layer max. range: 3 m, ang. resol. 0,0833 \[deg\]      ✔ \[stable\]   
                                                                                                                                                                  Scan-Rate: 600 Hz                                                       
     LMS511-10100 PRO      [1046135](https://www.sick.com/media/docs/4/14/514/Operating_instructions_LMS5xx_LASER_MEASUREMENT_SENSORS_en_IM0037514.PDF)           1 layer max. range: 80m, ang. resol. 0.167 \[deg\]       ✔ \[stable\]   
                                                                                                                                                                  Scan-Rate: 100 Hz                                                       
     LMS1xx-Family         [e.g. 1041114](https://www.sick.com/media/docs/1/31/331/Operating_instructions_LMS1xx_Laser_Measurement_Sensors_en_IM0031331.PDF)      1 layer max. range: 28m, ang. resol. 0.25 \[deg\]        ✔ \[stable\]   
                                                                                                                                                                  Scan-Rate: 15 Hz                                                        
     RMS3xx                [8021530](https://www.sick.com/media/docs/4/04/504/Operating_instructions_RMS3xx_en_IM0075504.PDF)                                     Radar Sensor                                             ✔ \[stable\]   
                                                                                                                                                                  Opening angle: +/- 50 \[deg\]                                           
  -- ------------------ -- ----------------------------------------------------------------------------------------------------------------------------------- -- ----------------------------------------------------- -- -------------- --

For scanners of the series Tim3xx this driver should work but has not
been tested yet.

## Installation from sources

Major revisons of the software are released as binary packages. And can
therefore be installed via the package manager. The driver is constantly
being developed further, so we recommend that you check out and compile
the software from the devel branch of the repository. The following
actions are necessary for this:

```bash
source /opt/ros/<rosdistro>/setup.bash
mkdir -p ~/ros_catkin_ws/src/
cd ~/ros_catkin_ws/src/
git clone -b devel --single-branch git://github.com/SICKAG/sick_scan.git
cd ..
catkin_make
source ~/ros_catkin_ws/install/setup.bash
```

## First steps

1\. Use the
[SICK SOPAS ET Software](https://www.sick.com/de/de/sopas-engineering-tool-2018/p/p367244)
to determine or set the IP address of the laser scanner. 1. Change Ip
address is in the launch-file associated with your scanner type. 1.
Launch the node e.g. ```
roslaunch sick_scan sick_mrs_1xxx.launch
``` 1. Launch rviz
```
rviz rviz
``` 1. Select **`'laser`**' as fixed frame. And
add a new PointCloud decoder subscribed at topic **`'cloud`**'. 1.
Enjoy.

## Troubleshooting

1\. Check Scanner IP in the launch file. 1. Check Ethernet connection to
scanner with netcat e.g. `nc -z -v -w5 \$SCANNERIPADDRESS 2112`.

-   For further details about setting up the correct ip settings see
    [IP configuration](https://github.com/SICKAG/sick_scan/blob/master/doc/ipconfig/ipconfig.md) 1.
    View node startup output wether the IP connection could be
    established 1. Check the scanner status using the LEDs on the
    device. The LED codes are described in the above mentioned operation
    manuals. 1. Further testing and troubleshooting informations can
    found in the file test/readme_testplan.txt 1. If you stop the
    scanner in your debugging IDE or by other hard interruption (like
    Ctrl-C), you must wait until 60 sec. before the scanner is up and
    running again. During this time the MRS6124 reconnects twice. . If
    you do not wait this waiting time you could see one of the following
    messages:
-   TCP connection error
-   Error-Message 0x0d 1. Amplitude values in rviz: If you see only one
    color in rviz try the following:
-   Set the min/max-Range of intensity display in the range \[0\...200\]
    and switch on the intensity flag in the lauch file 1. In case of
    network problems check your own ip address and the ip address of
    your laser scanner (by using SOPAS ET).
-   List of own IP-addresses: ifconfig\|grep "inet addr"
-   Try to ping scanner ip address (used in launch file) 1. If the
    driver stops during init phase please stop the driver with ctrl-c
    and restart (could be caused due to protocol ASCII/Binary
    cola-dialect).

## Support

-   In case of technical support please open a new issue. Under
    <https://github.com/SICKAG/sick_scan/issues>. For optimal support,
    add the following information to your request: 1. Scanner model
    name, 1. Ros node startup log, 1. Sopas file of your scanner
    configuration. The instructions at
    <http://sickusablog.com/create-and-download-a-sopas-file/> show how
    to create the Sopas file.
-   In case of application support please use
    <https://supportportal.sick.com>.
