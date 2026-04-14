```clearsilver
name = pr2_read_text
desc = This package provides code for PR2 reading text using its prosilica camera.
sub {
  0.name = prosilica/image_rect_color
  0.type = sensor_msgs/Image
  0.desc = Rectified color image from prosilica camera
  1.name = base_odometry/state
  1.type = pr2_mechanism_controllers/BaseOdometryState
  1.desc = PR2 state message, indicate moving or stable
}
pub {
  0.name = prosilica/text_detect
  0.type = sensor_msgs/Image
  0.desc = Output detection result image
}
```

### Tutorials

The following is the tutorial of making PR2 literate:

First switch prosilica camera into streaming mode. For more information
on Prosilica camera:
[prosilica_camera](http://www.ros.org/wiki/prosilica_camera)
```
rosrun dynamic_reconfigure dynparam set_from_parameters prosilica_driver _trigger_mode:=streaming
```

Also use dynamic_reconfigure to set frame rate to 1. With lower frame
rate, the camera generate less data publishing through the topic. See
the [dynamic_reconfigure](dynamic_reconfigure) package for details on
dynamically reconfigurable parameters. You can also do the previous step
together in dynamic_reconfigure GUI.

Then kill sound_play node before running pr2_read_text.
```
rosnode kill sound_play
``` We had some problems with sound_play on our
PR2, it keep generating very low and deep voice for text-to-speech. So,
instead, we use festival directly as a system call, but we have to kill
the [sound_play](sound_play) otherwise the sound device will be occupied
by [sound_play](sound_play) node . It\'s only a temporary solution right
now.

Now you can finally making PR2 literate: ```
roslaunch pr2_read_text read_text_from_pr2.launch
``` Drive
around the PR2 using teleop, and facing it towards text, it will start
reading! You can also see the detection result with
[image_view](image_view) (default turned on in the launch file)

You can also record the required topics and reproduce the action later
using the bag file ```
roslaunch pr2_read_text read_text_from_bag.launch <bag_file>
```
