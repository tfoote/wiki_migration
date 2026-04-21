## Interface

The `dp_ptu47_pan_tilt_stage` package provides a `dp_ptu47` node
that controls the actual hardware. The node advertises 4 different
services:

-   **control** - accepts a service request (*SendCommand.srv*) that
    controls the unit via pan/tilt angles ```
1 float32 pan_angle
  2 float32 tilt_angle
  3 bool wait_finished
  4 ---
  5 float32 pan_angle
  6 float32 tilt_angle
```
-   **control_trajectory** - accepts a service request
    (*SendTrajectory.srv*) that controls a set of angles (trajectory)
    together with a certain tolerance ```
1 float32[] pan_angles
  2 float32[] tilt_angles
  3 float32 tolerance
  4 ---
  5 float32 pan_angle
  6 float32 tilt_angle
```
-   **get_limits** - accepts a service request (*GetLimits.srv*) that
    obtains the current set of software limits set for the unit
    ```
1 ---
  2 float32 min_pan
  3 float32 max_pan
  4 float32 min_tilt
  5 float32 max_tilt
```
-   **reset** - sends a service request (*Reset.srv*) that resets the
    unit ```
1 ---
```

## Usage examples

The easiest way to send the unit to a specific pan/tilt angle is to use
the *SendCommand* and/or *SendTrajectory* sevice requests. Start the
service node with

```
$ roslaunch dp_ptu47_pan_tilt_stage dp.launch
```

Note: the head cart HCC has the PT unit on the /dev/ttyUSB3 device port,
which is what *dp.launch* contains.

A small tool part of the package can issue commands conveniently:
```
$ rosrun dp_ptu47_pan_tilt_stage dp_ptu47_trigger 
[...] Syntax is: dp_ptu47_trigger [pan_angle tilt_angle]... tolerance
```

## Data capture

The main purpose of the unit is to facilitate data acquisition using
other sensing devices. Here's an example for capturing data from
several topics on the PR2 robot, by following a given trajectory:
```
1 # Topics to record
  2 TOPICS="/narrow_stereo/left/image_raw /narrow_stereo/right/image_raw /narrow_stereo/left/camera_info /narrow_stereo/right/camera_info /narrow_stereo_textured/left/image_raw /narrow_stereo_textu    red/right/image_raw /narrow_stereo_textured/left/camera_info /narrow_stereo_textured/right/camera_info /dp_ptu47/pan_tilt_status /dp_ptu47/pan_tilt_status_stamped /tf"
  3 # Trajectory to follow
  4 TRAJECTORY="-150 0"
  5 for i in -30 -20 -10 0 10 20
  6 do
  7 TRAJECTORY="$TRAJECTORY -150 $i 150 $i 150 `expr $i + 5` -150 `expr $i + 5`"
  8 done
  9 TRAJECTORY="$TRAJECTORY -150 0 0 0"
 10 
 11 #echo $TOPICS
 12 #echo $TRAJECTORY
 13 
 14 
 15 if [ ! -z "$1" ]
 16 then
 17     echo "Recording $1.bag"
 18     rosrecord -F $1 $TOPICS &
 19     rosrun dp_ptu47_pan_tilt_stage dp_ptu47_trigger 0 0
 20     sleep 1
 21     rosrun dp_ptu47_pan_tilt_stage dp_ptu47_trigger $TRAJECTORY
 22     ps | grep rosrecord | awk '{print $1}' | xargs kill -sigint
 23     echo "Done"
 24 else
 25     echo "Usage:"
 26     echo "$0 object_name"
 27 fi
```
