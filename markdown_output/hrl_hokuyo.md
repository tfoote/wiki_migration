## Usage



```
cd src/hrl_hokuyo
 python hokuyo_processing.py -h
```



The output will be: 

```
Usage: hokuyo_processing.py [options]

Options:
  -h, --help            show this help message and exit
  -t HOKUYO_TYPE        hokuyo_type. urg or utm
  -a AVG                number of scans to average
  -n HOKUYO_NUMBER      hokuyo number. 0,1,2 ...
  -f                    flip the hokuyo scan
  --ang_range=ANG_RANGE
                        max angle of the ray to display (degrees)
```

 1. Given an appropriate
hokuyo number and type this will visualize the hokuyo scans in a pygame
window. 1. Prior to running hokuyo_processing.py, launch a hokuyo_node.
Look at cody_utm0.launch for an example. 1. Alternately, look at
hokuyo_scan.py

## ROS API

Subscribes to sensor_msgs/LaserScan.

## TODOs

1\. URG support is outdated - uses player. Needs to be changed.

## Troubleshooting

1\. roslaunch ele_utm.launch gives this error: Failed to open port
/dev/robot/hokuyo_hokuyo_serial_number> error=2 : No such file or
directory 1. Restart udev: 1. `sudo /etc/init.d/udev restart` (For
Hardy Heron, Ubuntu 8.04) 1. `sudo restart udev` (For Lucid Lynx,
Ubuntu 10.04) 1. `ls /dev/robot` - you should see your Hokuyo
device. 1. If you don't see it, try unplugging it from the usb port,
power cycling the UTM, plugging the UTM back into the usb port and
restarting udev.
