# Roboception Dynamics API

The rc_dynamics_api provides an API for easy handling of the
dynamic-state data streams provided by
[Roboception's](http://roboception.com)
[rc_visard](http://rc-visard.com) stereo camera with self-localization.

Dynamic-state estimates of the rc_visard relate to its self-localization
and ego-motion estimation. These states refer to rc_visard's current
pose, velocity, or acceleration and are published on demand via several
data streams. For a complete list and descriptions of these dynamics
states and the respective data streams please refer to
[rc_visard's user manual](http://doc.rc-visard.com).

## Tools

Currently, the rc_dynamics_api comes with the following tool which is
also meant as an example on how to use this API:

### rcdynamics_stream

Connect with an rc_visard device and request a specific data stream. The
received data messages containing aspects of rc_visard's dynamic state
can be simply printed to std::out or saved as .csv-file.

Simplest example: Connect to rc_visard with specified IP address and
request the 'imu' stream. A certain amount of messages are received
and simply print to std::out 

```sh
./tools/rcdynamics_stream -v 10.0.2.99 -s imu
```

 Different use case
with more command line parameters: Connect to rc_visard with specified
IP address and request the 'pose_rt' stream for 10 seconds. The client
host's network interface to be used to receive the data is specified as
'eth0'. Messages are stored in the specified file as .csv-lines.


```sh
./tools/rcdynamics_stream -v 10.0.2.99 -s pose_rt -i eth0 -a -t10 -o poses.csv
```


