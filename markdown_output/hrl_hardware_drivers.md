A more detailed coding tutorial, application overviews, and a servo
disassembly can be found on
[Hizook.com](http://www.hizook.com/blog/2010/03/14/robotis-dynamixel-servos-overview-applications-tear-down-and-open-source-software).
Robotis Dynamixel servos and USB2Dynamixel adaptors (used for
communication with the servos) can be purchased online.

This package includes a stand-alone library (lib_robotis.py) for
querying and controlling Robotis Dynamixel Servos. The code is written
entirely in Python and is thread-safe, so that multiple servo objects
can be controlled / queried "simultaneously" on the same USB2Dynamixel
bus (within the same process). The library should function on Linux,
Mac, and Windows (yay, python!), and the only dependency is pyserial for
communications. The code has only been tested on the RX-28 and RX-64
variants. Sample usage is shown below; more comprehensive explanations
can be found on
[Hizook.com](http://www.hizook.com/blog/2010/03/14/robotis-dynamixel-servos-overview-applications-tear-down-and-open-source-software).



```
from lib_robotis import *
dyn = USB2Dynamixel_Device('/dev/ttyUSB0')
p = Robotis_Servo( dyn, 11 )
t = Robotis_Servo( dyn, 12 )
t.move_angle( math.radians( 10 ), blocking = False )
p.move_angle( math.radians( 10 ), blocking = False )
```

 ROS wrappers (messages and services) have also
been implemented to query and control the servos remotely. Again, sample
usage is shown below and more comprehensive explanations can be found on
[Hizook.com](http://www.hizook.com/blog/2010/03/14/robotis-dynamixel-servos-overview-applications-tear-down-and-open-source-software).



```
import roslib
roslib.load_manifest('robotis')
import rospy
from robotis.ros_robotis import *

poller = ROS_Robotis_Poller( '/dev/ttyUSB0', [11,12], ['pan', 'tilt'] )
rospy.spin()
poller.stop()
```

 Essentially, the poller is implemented thusly:



```
import roslib
roslib.load_manifest('robotis')
import rospy

import robotis.lib_robotis as rs
print 'Sample Server: '

# Important note: You cannot (!) use the same device in another
# process. The device is only "thread-safe" within the same process
# (i.e.  between servos (and callbacks) instantiated within that
# process)

dev_name = '/dev/ttyUSB0'
ids = [11, 12]
names = ['pan', 'tilt']

dyn = rs.USB2Dynamixel_Device( dev_name )

servos = [ rs.Robotis_Servo( dyn, i ) for i in ids ]
ros_servers = [ ROS_Robotis_Server( s, n ) for s,n in zip( servos, names ) ]

try:
    while not rospy.is_shutdown():
        [ s.update_server() for s in ros_servers ]
        time.sleep(0.001)
except:
    pass
```

 Older libraries (robotis_servo.py) are also
present, but are now deprecated.



```
./robotis_servo -h # this will print out the command line params that the code accepts.

./robotis_servo -d /dev/ttyUSB0 --ang=30 --id=1 # moves a servo with id 1 connected to ttyUSB0 to angle 30 degrees.
```


