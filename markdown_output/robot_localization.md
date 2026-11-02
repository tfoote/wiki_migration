1.  pragma section-numbers off

{} {} {} {} {} {} {} 

```
{#!wiki version noetic
Documentation for {{{robot_localization
```

 is now
[hosted on docs.ros.org](http://docs.ros.org/noetic/api/robot_localization/html/index.html).
}}}}

## Troubleshooting

### Troubleshooting robot_localization

#### Troubleshooting ekf_localization

Before reading this page, please make sure you have read all of the
[tutorials](https://index.ros.org/p/robot_localization), as they will
have important information.

##### The Position Estimate is Generally Poor/Wrong

- First - and this is critical - double-check *all* of your sensor data,
  one sensor at a time. See the
  [sensor data preparation tutorial](https://index.ros.org/p/robot_localization)
  for more information.
- If you have an IMU, make sure all the angles increase and decrease
  correctly as described in
  [REP-103](http://www.ros.org/reps/rep-0103.html). Keep in mind that
  ROS uses a right-handed coordinate frame. The same goes for angular
  velocities. Make sure they are positive and negative when they should
  be. For example, if you have a ground robot and turn it
  counter-clockwise, its yaw angle should increase and its yaw velocity
  should be positive. You may have to convert your yaw angle to Euler
  angles if you can't interpret quaternions. Check your acceleration
  signs as well.
- Covariances are important. Make sure you understand what they mean and
  that your values make sense. Do *not* use massive covariance values
  for variables you want to ignore or that aren't measured by your
  sensor. Use the sensor's configuration boolean vector instead.
- If you have an odometry source that measures orientation and/or
  rotational velocity, ensure that the angles increase and decrease in
  the correct direction.
- frame_ids matter. Read up on message specs to determine what the
  correct frame_id and (when applicable) child_frame_id values are.
- Next, double check your sensor configurations. See the
  [best practices tutorial](https://index.ros.org/p/robot_localization)
  for more information.

##### The filtered position estimate is unstable, i.e., the robot's position jumps around wildly

This can be attributable to several things:

**\*Sensor Configuration** - The first thing to check is whether or not
you are fully utilizing each sensor. Even if your sensor doesn't
directly measure a given variable, it may be in your best interests to
fuse a 0 measurement for that variable into the filter. For example, if
you have a vehicle operating in a planar environment and your robot only
has X velocity, then fusing 0 measurement values for Y and Z velocity
will increase the filter's stability. See the
[Tutorials](https://index.ros.org/p/robot_localization) page for more
information.

**\*Timing** - Timing is important for EKFs and UKFs.
`ekf_localization_node` and `ukf_localization_node` use a combination of
the current ROS time for the node and the message timestamps to
determine how far ahead to project the state estimate in time. It is
therefore critically important (for distributed systems) that the clocks
are synchronized. If, for example, you run `ekf_localization_node` on
machine A, but your measurements come from machine B, then you can get
into situations wherein your sensor's measurements are ahead of or
behind the host machine's time. This can lead to situations in which
the filter believes it has to project the state estimate across a
relatively long span of time, leading to large jumps in the state
estimate.

**\*Inconsistent Measurements** - EKFs and UKFs will calculate
near-optimal solutions given measurements with known noise
characteristics. However, they have their limits. If the sensor data
going into it is inconsistent, then the output will reflect that. For
example, if two velocity measurements have opposing signs, you will see
strange behavior. If you are fusing absolute pose information (position
or orientation), set that sensor's *differential* setting to true.

##### I'm still having trouble. What can I do?

If you have read all of the documentation and troubleshooting found
here, then feel free to ask a question on the
[ROS Answers site](http://answers.ros.org/questions/). Also, look over
[previously asked questions about robot_localization](http://answers.ros.org/questions/scope:all/sort:activity-desc/tags:robot_localization/page:1/).
If you do ask a new question, please ensure that you do the following:

- Post your entire launch file for any packages in `robot_localization`,
  **but** please remove any of the XML comments in the launch file,
  especially if you are starting from the template launch files provided
  by `robot_localization`. Additionally, if you are posting a question
  about `ekf_localization_node` or `ukf_localization_node` and you did
  **not** modify any of the covariance parameters, please remove those
  matrices from the launch file.

<!-- -->

- Post either a sample input message for each sensor input (e.g.,
  `odom0`, `imu0`, etc.) or a bag file. If you post a bag file, it makes
  debugging *much* easier if users only post the raw sensor data and
  transforms, and do NOT run any `robot_localization` nodes. Note that
  simply not recording them using `rosbag` is insufficient, as the
  *odom*->*base_link* (and/or *map*->*odom*) transform will still be
  in the /tf topic, which will interfere with analysis.

<!-- -->

- Be sure to tag any new questions with `robot_localization`.
