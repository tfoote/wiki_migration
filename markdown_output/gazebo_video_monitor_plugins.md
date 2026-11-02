![width="600px"](doc/gazebo_video_monitor_plugins.png)

## Tutorials

There is a set of
[tutorials](#tutorials-1) that
explains which are the available video plugins and how to use them.

## Tutorials

### Intro

All the plugins in this package are based on a custom camera sensor.
This type of sensor provides access to synchronized frames from a set of
cameras. The frames that the sensor generates are forwarded to a sensor
plugin (just as you would expect with any other sensor). The plugin has
at least one video recorder. The recorder is responsible for processing
the frames and creating videos. What each of the plugins in the package
does is decide which frames to give to the recorder every time. By
managing the frames in different ways, you can create plugins that
accommodate different use cases.

![width="700px"](doc/gvm-design.png)

In the next tutorials, we'll find out how to configure the multicamera
sensor, as well as which are the available video plugins and how to use
them.

### Tutorials

- [Configuring a gvm multicamera sensor](#configuring-a-gvm-multicamera-sensor):
  This tutorial walks you through how to configure a gvm multicamera
  sensor
- [Utility Plugins](#utility-plugins):
  This tutorial presents various utility plugins that are useful for the
  video plugins
- [Gazebo Video Monitor Plugin](#gazebo-video-monitor-plugin):
  This tutorial presents the gazebo video monitor plugin
- [Gazebo Multi Video Monitor Plugin](#gazebo-multi-video-monitor-plugin):
  This tutorial presents the gazebo multi video monitor plugin
- [Gazebo Multi Camera Monitor Plugin](#gazebo-multi-camera-monitor-plugin):
  This tutorial presents the gazebo multi camera monitor plugin
- [Gazebo Multi View Monitor Plugin](#gazebo-multi-view-monitor-plugin):
  This tutorial presents the gazebo multi view monitor plugin

## Configuring a gvm multicamera sensor

- **Description:** This tutorial walks you through how to configure a
  gvm multicamera sensor
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Utility Plugins](#utility-plugins)

### Background

If you are not curious about why the configuration of the sensor looks
like the way it does, you may skip this section.

We want to have a set of cameras that are running inside Gazebo. Cameras
are sensors, and sensors are part of a link in a model. This means, a
sensor cannot exist by itself, but we have to attach it to a link. We
need to pick a model, create a multicamera sensor, and give ownership of
the sensor to a link of that model. This is accomplished with the
multicamera bootstrapper plugin.



```
<plugin
  name="multicamera_bootstrapper_plugin"
  filename="libgvm_multicamera_bootstrapper_plugin.so">
  <sensor name="camera" type="gvm_multicamera">
    ...
  </sensor>
  <sensorReference>
    <model>ground_plane</model>
    <link>link</link>
  </sensorReference>
</plugin>
```



The configuration of the bootstrapper plugin consists of two parts. The
first one has the multicamera sensor configuration, and the second one
specifies the model to which we want to give the sensor. The plugin
reads this information and gets the sensor up and running for us. The
model should be one that we know it's always there, like ground_plane,
and exists throughout the duration of the simulation. You want this, so
you may delete your robot model at some point but keep the cameras there
for your next test.

### Bootstrapping

Start with the following boilerplate XML code.



```
<plugin
  name="multicamera_bootstrapper_plugin"
  filename="libgvm_multicamera_bootstrapper_plugin.so">
  <!-- gvm_multicamera sensor configuration goes here -->
  
  <sensorReference>
    <model>ground_plane</model>
    <link>link</link>
  </sensorReference>
</plugin>
```



The bootstrapper plugin is a model plugin responsible for spawning the
cameras and loading the video plugin of your choice. The code above will
create a multicamera sensor and attach it to ground_plane. Mind here
that it's the sensor that gets attached to ground_plane. The individual
cameras can still be attached to other (robot) links later, and thus
move along with them.

### Multicamera Sensor

Next, you need to configure the cameras. For this, you must configure a
sensor of type `gvm_multicamera`. A gvm_multicamera sensor is a sensor
that produces synchronized frames from a set of cameras. The
configuration of the sensor is like the one of the regular
[camera sensor](http://sdformat.org/spec?ver=1.7&elem=sensor#sensor_camera),
only here, there can be multiple instances of the camera code. The
number of instances is dependent on the video plugin (described later).



```
<sensor name="video_monitor_dual_camera" type="gvm_multicamera">
  <update_rate>30</update_rate>
  <!-- <always_on>true</always_on> -->
  <!-- <visualize>true</visualize> -->

  <camera name="world_camera">
    <pose>3.0 0 1.0 0 0 3.1416</pose>
    <horizontal_fov>1.5708</horizontal_fov>
    <image>
      <width>640</width>
      <height>480</height>
      <format>R8G8B8</format>
    </image>
    <clip>
      <near>0.01</near>
      <far>100</far>
    </clip>
  </camera>

  <camera name="robot_camera">
    <pose>-0.5 0 0.3 0 0 0</pose>
    <horizontal_fov>0.823599</horizontal_fov>
    <image>
      <width>640</width>
      <height>480</height>
      <format>R8G8B8</format>
    </image>
    <clip>
      <near>0.01</near>
      <far>10</far>
    </clip>
  </camera>

  <!-- video plugin configuration goes here -->
</sensor>
```



Inside the sensor configuration, you specify the frame rate
(`update_rate`) of the cameras, and you may also enable the camera
visualizations (`visualize`). The visualizations are useful when you
want to position the cameras, as you get immediate feedback on the given
poses.

![width="500px"](doc/camera-visualization.jpg)

For each camera of the sensor, you need to configure the usual
parameters, such as resolution, format, and field of view. Furthermore,
you may want to give a pose to a camera. This pose is relative to the
link that the camera is attached to. Initially, a camera is attached to
the same link as the sensor. The link can be changed in the video plugin
configuration (described later). The link can also be changed at runtime
with a ROS service (also described later).

### Video Plugin

A video plugin is responsible for recording the videos. It receives the
frames from the cameras, decides which ones to pick, and uses them as
the source for the next video frame. A video plugin has one or more
recorders. A recorder is actually the one that processes the frames and
creates the video. So, a video plugin could record multiple videos at a
time.



```
<plugin name="video_monitor_plugin" filename="libgazebo_video_monitor_plugin.so">
  <setCameraService>gazebo/set_camera</setCameraService>
  <startRecordingService>gazebo/start_recording</startRecordingService>
  <stopRecordingService>gazebo/stop_recording</stopRecordingService>
  <savePath>/var/tmp/gazebo_video_monitor</savePath>
  <recorder>
    <width>640</width>
    <height>480</height>
    <bitRate>590000</bitRate>
    <logMetadata>true</logMetadata>
    <logWallTime>false</logWallTime>
    <addTimestampInFilename>true</addTimestampInFilename>
  </recorder>
  <cameraReference name="robot_camera">
    <model>my_robot</model>
    <link>gripper_link</link>
  </cameraReference>
</plugin>
```



Each video plugin defines its own custom configuration, but all of them
have the same basic configuration shown above.

- **setCameraService**: The name of the ROS service for configuring the
  pose of a camera and the link to which the camera should be attached
- **startRecordingService**: The name of the ROS service for starting a
  video recording
- **stopRecordingService**: The name of the ROS service for stopping a
  video recording
- **savePath**: The directory under which all videos are saved

Then follows the configuration of the recorder.

- **width**: The width of the video
- **height**: The height of the video
- **bitRate**: The bit rate of the video
- **logMetadata**: A flag to indicate whether to write time metadata on
  the video
- **logWallTime**: A flag to indicate whether log the wall time, instead
  of the real time, on the video
- **addTimestampInFilename**: A flag to indicate whether to append the
  start timestamp of the recording in the filename of the video

And lastly, there can be zero or more instances of **cameraReference**.
`cameraReference` is used to configure the link to which a camera
should be attached. It has an attribute `name` that should match the
name of a camera configured in the sensor.

- **model**: The name of the model with which to associate the camera
- **modelParam**: If the name of the model is not always the same, you
  may skip the **model** parameter, and specify here the parameter on
  the parameter server that holds the name of the model
- **link**: The name of the link to which to attach the camera

### SetCamera Service

All plugins expose a ROS service for dynamically reconfiguring a camera.
With the service, you can update the link to which a camera should be
attached, as well as the pose of the camera with respect to that link.
You may use the camera visualizations to help you with this process.



```
rosservice call /gazebo/set_camera "{camera_name: robot_camera, model_name: robot-0001, link_name: gripper_link, pose: {x: 0.0, y: -0.05, z: -0.1, roll: -0.2, pitch: 0.0, yaw: 0.0}}"
```



The service request expects the names of the camera, model, and link,
and the pose of the camera in xyz and rpy.

### Conclusion

You now know what each parameter of the sensor configuration represents.
Move on to the next tutorials to find out what each video plugin does,
and how to use it.

## Utility Plugins

- **Description:** This tutorial presents various utility plugins that
  are useful for the video plugins
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Gazebo Video Monitor Plugin](#gazebo-video-monitor-plugin)

A set of utility plugins is available to be used along with the monitor
plugins.

### Camera Contains Plugin

![width="500px"](doc/camera-contains-plugin.jpg)

Publishes a list of camera names when one or more of the tracked models
enter the space of a box container.

Multiple instances of this plugin can be used to automatically
transition the video to specific cameras when activity is detected in
certain areas.

To use the plugin, add one or more configurations like the following in
your world file:



```
<plugin name="container" filename="libcamera_contains_plugin.so">
  <!-- Rate at which to check for collisions with the tracked models -->
  <updateRate>30</updateRate>
  <visualize>false</visualize>
  <trackedModels>[robot_model_name]</trackedModels>
  <cameras>[camera_0, camera_1]</cameras>
  <topic>gazebo/camera_select</topic>
  <pose>3 0 1 0 0 0</pose>  <!-- Pose of the container -->
  <size>2 3 2</size>  <!-- Size of the container -->
</plugin>
```



The camera names to publish is dependent on the video plugin used. For
instance, for the multi-view plugin, you might configure something like
this:



```
<cameras>[camera_0, '', '', camera_1]</cameras>
```



This means the second and third view in the video will be blacked out.

## Gazebo Video Monitor Plugin

- **Description:** This tutorial presents the gazebo video monitor
  plugin
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Gazebo Multi Video Monitor Plugin](#gazebo-multi-video-monitor-plugin)

![width="600px"](doc/video-monitor-plugin.png)

The gazebo video monitor plugin records videos in the format shown
above.

It assumes two cameras: one which can be used to get a view of the world
and another one which can be attached to a robot to get a view from its
perspective. Additionally, time metadata are logged in the video to make
tracking of world and robot events easier.

The plugin exposes two ROS services to control the recordings:

Use the start_recording service to initiate a recording. Setting
disable_window to true removes the second view from the recording.
world_as_main_view can be used to set the world or robot camera as the
main view of the recording.



```
rosservice call /gazebo/start_recording "{disable_window: false, world_as_main_view: false}"
```



Use the stop_recording service to save or discard a recording. The
filename must be given without the extension (.mp4). The recording is
saved in the directory defined in the plugin configuration.



```
rosservice call /gazebo/stop_recording "{discard: false, filename: navigation-test}"
```



See an example configuration of the plugin in
[gazebo_video_monitor_plugin.world](https://github.com/nlamprian/gazebo_video_monitors/blob/ros1/gazebo_video_monitor_plugins/test/worlds/gazebo_video_monitor_plugin.world).

## Gazebo Multi Video Monitor Plugin

- **Description:** This tutorial presents the gazebo multi video monitor
  plugin
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Gazebo Multi Camera Monitor Plugin](#gazebo-multi-camera-monitor-plugin)

![width="600px"](doc/multi-video-monitor-plugin.gif)

The gazebo multi-video monitor plugin records multiple videos from
different cameras simultaneously.

An arbitrary number of cameras can be set up, and the plugin will read
and record a video for each one of them. Time metadata can be logged in
the videos as well.

The plugin exposes two ROS services to control the recordings:

Use the start_recording service to initiate a recording. There are no
arguments.



```
rosservice call /gazebo/start_recording "{}"
```



Use the stop_recording service to save or discard a recording. The
filename must be given without the extension (.mp4). The recordings are
saved together in the subdirectory under the directory defined in the
plugin configuration.



```
rosservice call /gazebo/stop_recording "{discard: false, filename: navigation-test}"
```



See an example configuration of the plugin in
[gazebo_multi_video_monitor_plugin.world](https://github.com/nlamprian/gazebo_video_monitors/blob/ros1/gazebo_video_monitor_plugins/test/worlds/gazebo_multi_video_monitor_plugin.world).

## Gazebo Multi Camera Monitor Plugin

- **Description:** This tutorial presents the gazebo multi camera
  monitor plugin
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Gazebo Multi View Monitor Plugin](#gazebo-multi-view-monitor-plugin)

![width="600px"](doc/multi-camera-monitor-plugin.gif)

The gazebo multi-camera monitor plugin records videos with a
multi-camera setup. See the gif above (the video was created
automatically; no editing was done).

An arbitrary number of cameras can be set up, from which the plugin can
select and configure the video stream. The cameras can be updated
dynamically during the recording. Time metadata can be logged in the
videos as well.

The plugin exposes two ROS services to control the recordings:

Use the start_recording service to initiate a recording. You can
optionally specify the cameras with which to initialize the video
stream.



```
rosservice call /gazebo/start_recording "{cameras: {names: []}}"
```



Use the stop_recording service to save or discard a recording. The
filename must be given without the extension (.mp4). The recording is
saved in the directory defined in the plugin configuration.



```
rosservice call /gazebo/stop_recording "{discard: false, filename: navigation-test}"
```



Publish a message to the camera_select topic to update the video stream.
You can specify one or two cameras for the main and window view,
respectively.



```
rostopic pub /gazebo/camera_select gazebo_video_monitor_msgs/Strings "{names: [camera_0, camera_2]}"
```



See an example configuration of the plugin in
[gazebo_multi_camera_monitor_plugin.world](https://github.com/nlamprian/gazebo_video_monitors/blob/ros1/gazebo_video_monitor_plugins/test/worlds/gazebo_multi_camera_monitor_plugin.world).

## Gazebo Multi View Monitor Plugin

- **Description:** This tutorial presents the gazebo multi view monitor
  plugin
- **Tutorial Level:** BEGINNER

![width="600px"](doc/multi-view-monitor-plugin.gif)

The gazebo multi-view monitor plugin records videos with up to 4
parallel camera streams.

An arbitrary number of cameras can be set up, from which the plugin can
select and configure the video stream. The cameras can be updated
dynamically during the recording. Time metadata can be logged in the
videos as well.

The plugin exposes two ROS services to control the recordings:

Use the start_recording service to initiate a recording. You can pass as
arguments the cameras with which to initialize the video stream. An
empty camera name results in a null camera stream in the respective
quadrant.



```
rosservice call /gazebo/start_recording "{cameras: {names: ['', camera_1, camera_2, '']}}"
```



Use the stop_recording service to save or discard a recording. The
filename must be given without the extension (.mp4). The recording is
saved in the directory defined in the plugin configuration.



```
rosservice call /gazebo/stop_recording "{discard: false, filename: navigation-test}"
```



Publish a message to the camera_select topic to update the video stream.
You can specify up to 4 cameras for the top left, top right, bottom
left, and bottom right quadrant, respectively. A camera name can be left
empty to disable the respective quadrant.



```
rostopic pub /gazebo/camera_select gazebo_video_monitor_msgs/Strings "{names: [camera_3, camera_1, '', camera_2]}"
```



See an example configuration of the plugin in
[gazebo_multi_view_monitor_plugin.world](https://github.com/nlamprian/gazebo_video_monitors/blob/ros1/gazebo_video_monitor_plugins/test/worlds/gazebo_multi_view_monitor_plugin.world).
