## Installation

Use the following to install the gscam package (ubuntu 12.04). 1. Create
a catkin workspace (see
[Catkin Tutorial](ROS/Tutorials/catkin/CreateWorkspace)) 1. Install
wstool (if not already installed) (see [wstool Tutorial](wstool)) 1.
Install gscam package ```
sudo apt-get install ros-hydro-gscam
``` 1. Switch to catkin
workspace into src folder ```
cd ~/catkin_ws/src
``` 1. Add gscam
repositories ```
wstool init
wstool set gscam --git https://github.com/ros-drivers/gscam.git
wstool update
``` 1. Load additional packages for
gstreamer ```
sudo apt-get install gstreamer-0.10 libgstreamer0.10-0 libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev gstreamer0.10-ffmpeg gstreamer0.10-gconf gstreamer0.10-tools gstreamer0.10-x
``` 1. Build catkin workspace (see
[Catkin Tutorial](ROS/Tutorials/catkin/CreateWorkspace))
```
cd ..
catkin_make
```

## Documentation

See the video_player node documentation.

## Nodes

### video_player

This node has two main functions. 1. It can play a video.avi-file with
the VLC-Media-Player and closes automatically after playing back the
file. 1. It can publish the video-data to a topic, which the ROS
environment can deal with. The modus can be changed in the launch file.

```clearsilver
param {
  0.name = mode
  0.type = string
  0.desc = Describes in which way the node works (VLC-playback, ROS-stream). "mode_I" => VLC player, "mode_II" => ROS-stream. Default: "mode_II" = ROS-stream.  
}
param {
  1.name = gscam_config
  1.type = string
  1.desc = Used for calling the gstreamer. Example: "filesrc location=~/catkin_ws/src/tools_robin/video_player/data/Video1/Video.avi ! avidemux name=demux demux.video_00 ! decodebin  ! ffmpegcolorspace  ! video/x-raw-rgb ! identity name=ros ! fakesin"; 
}
```

### test_client

A simple node to test the video_player.

## Launch Files

Use roslaunch files to load the video_player_node and the parameter
mode.

-   \'\'\'video_player.launch\'\'\' - Launches the video_player_node.

## Test Video Player

By calling ```
roscore
roslaunch video_player video_player.launch
rosrun video_player test_client ~/catkin_ws/src/tools_robin/video_player/data/Video1
``` one can test the video player.
