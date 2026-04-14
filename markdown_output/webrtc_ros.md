## Overview

A ROS wrapper that allows for streaming of ROS video topics over
[WebRTC](http://www.webrtc.org/).

## Usage

webrtc_ros_server_node operates similar to
[web_video_server](http://wiki.ros.org/web_video_server). It provides a
way of streaming ROS topics to a web browser. By default it provides a
webpage at the root path of the web server that allows you to browse all
video topics and stream any of them. A small Javascript library is also
served to simplify the usage. See the topic stream web page source for a
simple example of usage.

A simple protocol that uses JSON over !WebSockets is used as the WebRTC
signaling channel.

## Nodes

```clearsilver
node.1 {
  name = webrtc_ros_server_node
  desc = Node that provides a web server, signaling channel over !WebSocket and webrtc peer to connect to.
  param {
    0.name = ~port
    0.type = string
    0.default = 8080
    0.desc = The port to run the web server and !WebSocket server on.
    1.name = ~image_transport
    1.type = string
    1.default = raw
    1.desc = Transport type that is used to subscribe to ROS image topics
  }
}
```
