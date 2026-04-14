## Overview

Xbot_talker is a voice interactive ROS package for XBot-U robots. The
package has multiple functions such as offline command word recognition,
offline TTS, and offline conversation.

## Nodes

```clearsilver
name = xbot_talker
desc = The `xbot_talker` node takes in <<SrvLink(xbot_talker/play)>> and <<SrvLink(xbot_talker/chat)>> services. The service can be called via a ROS [[Services|service]]. This node also provides /xbot/talk_state topic that can be used to Monitor operating status.

 srv {
    0.name = /xbot/play
    0.type = xbot_talker/play
    0.desc = Call this service to play the audio file of the specified path or convert text to voice playback.
    1.name = /xbot/chat
    1.type = xbot_talker/chat
    1.desc = Call this service to start voice conversation with the robot.
  }
 pub {
   0.name = /xbot/talker_state
   0.type = xbot_talker/talk_monitor
   0.desc = Get the state data from this topic. 
   1.name = /welcome/leave
   1.type = std_msgs/Bool
   1.desc = Get the True or False data from this topic and control the robot to navigate.
 }
param {
  0.name = ~base_path
  0.type = string
  0.default = `"$(find xbot_talker)"`
  0.desc =  Home directory of voice interactive configuration files and audio files.Please use the default value.
}
```
