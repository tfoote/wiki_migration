## Overview

This package provides shared memory driver for various NTP daemons (such
as ntpd and chrony).

## Time server configuration

### ntpd

Just add to \`/etc/ntp.conf\`: ```
server 127.127.28.2 minpoll 4 maxpoll 4
fudge 127.127.28.2 time1 0.5 stratum 12 refid ROS
```

### chrony

Add this to \`/etc/chrony/chrony.conf\`: ```
refclock SHM 2 delay 0.5 refid ROS
```

Note that chrony does not allow set stratum (topic not very accurate),
but i hope delay option does same thing.

## Node

```clearsilver
node.0 {
 name= shm_driver
 desc= This node sends time from topic to time server.
 sub {
  0.name= ~time_ref
  0.type= sensor_msgs/TimeReference
  0.desc= Time source topic.
 }
 param {
  0.name= ~shm_unit
  0.type= int
  0.desc= SHM Unit (must be same as in time server config).
  0.default= 2
 }
}
```
