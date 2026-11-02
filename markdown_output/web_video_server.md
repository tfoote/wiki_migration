## About

This package provides a video stream of a ROS image transport topic that
can be accessed via HTTP.

#### Parameters

- `~port` (`integer`, default: `8080`): Port number to listen for http
  requests.
- `~address` (`string`, default: `0.0.0.0`): Address to listen for http
  requests
- `~server_threads` (`integer`, default: `1`): The number of threads
  used to serve HTTP requests (these are not used for actual image
  streams).
- `~ros_threads` (`integer`, default: `2`): The number of threads
  running ros spinners. These threads are used to do the actual image
  encoding. These threads are shared between all current streams so the
  number does not need to match the number of connections.

## Usage

The web_video_server opens a local port and waits for incoming HTTP
requests. As soon as a video stream of a ROS image topic is requested
via HTTP, it subscribes to the corresponding topic and creates an
instance of the video encoder. The encoded raw video packets are served
to the client. Parameters can be specified by adding additional them to
the query string. To connect to the node with your browser, use the
following URLs:

### Available URLs

- Overview of available ROS topics: `http:*localhost:8080/` \* Webpage
  showing a video stream:
  `http:*localhost:8080/stream_viewer?topic={ROS_TOPIC}`
- Video stream URL: `http:*localhost:8080/stream?topic={ROS_TOPIC}` \*
  Snapshot of next image:
  `http:*localhost:8080/snapshot?topic={ROS_TOPIC}`

Several parameters can be configure via the video stream URL - Example:
<http://localhost:8888/stream?topic=depthcloud_encoded&bitrate=250000&type=vp8>

### Image Parameters

These are the parameters that can be used to configure a stream or
snapshot:

- `width` (`integer`, default: `original width`): The image stream will
  be resized to a new width and height. This parameter has to be used in
  conjunction with the height parameter.
- `height` (`integer`, default: `original height`): The image stream
  will be resized to a new width and height. This parameter has to be
  used in conjunction with the height parameter.
- `quality` (`integer`, default: `90`): The jpeg image quality
  (1\...100). This parameter can be used to reduce the size of the
  resulting stream.
- `invert` (`none`): Rotates the image by 180 degrees before streaming.
- `default_transport` (`string`, default: `"raw"`): The image transport
  to use (raw, compressed, theora).

### Snapshot Parameters

These are the parameters that can be used to configure a snapshot:

- `quality` (`integer`, default: `95`): The jpeg image quality
  (1\...100). This parameter can be used to reduce the size of the
  resulting stream.

### Stream Parameters

These are the parameters that can be used to configure a stream:

- `type` (`string`, default: `mjpeg`): The encoding method for the
  stream (mjpeg, vp8, ros_compressed, png, h264).

Additional parameters can be specified for each encoding type as
described below.

#### Mjpeg Stream Parameters

These are the parameters that can be used to configure a mjpeg stream:

- `quality` (`integer`, default: `95`): The jpeg image quality
  (1\...100). This parameter can be used to reduce the size of the
  resulting stream.

#### VP8 Stream Parameters

These are the parameters that can be used to configure a vp8 stream:

- `bitrate` (`integer`, default: `100000`): Maximum bitrate setting.
  Note that a small bitrate could significantly increase the latency due
  to a delayed transmission of larger intra frames.
- `qmin` (`integer`, default: `10`): Minimum quantizer.
- `qmax` (`integer`, default: `42`): Maximum quantizer.
- `gop` (`integer`, default: `250`): Keyframe interval, this determines
  the maximum distance between I-frames.
- `quality` (`string`, default: `realtime`): The encoding quality.

More information on the quality and profile parameter of the VP8 codec
can be found here: <http://www.webmproject.org/docs/encoder-parameters>

### Unsupported customizations

#### Control image subscription rate

Rate at which `web_video_server` subscribes a image topic depends on
the publisher's publish rate. With a fast publish rate, a client host
may unintentionally get busy.

As of version 0.2.1, `web_video_server` does not come with a feature
to control the rate at which the frontend subscribes to an image topic.
You can work this around on your client.

One way is to republish the image topic with a lower rate. You can use
[throttle from topic_tools package](https://index.ros.org/p/topic_tools).

### ROS-Compressed Stream Example

rostopic list output:



```
$ rostopic list
/usb_cam/camera_info
/usb_cam/image_raw/compressed
```



View compressed stream at:
`http:*localhost:8080/stream?topic=/usb_cam/image_raw&type=ros_compressed`*

Node and topic diagram (output of
[rqt_graph](https://index.ros.org/p/rqt_graph)). **NOTE** this graph is
**NOT** showing compressed image topic, so this screenshot isn't
showing exactly the same situation we're running above where the box in
the middle should be the compressed image topic. Hope this still gives
an idea of relationship:

![alt Node and topic diagram](doc/rqt_graph-output-usb_cam-sample.png)

## Latency

The web_video_server tries to minimize internal coding latency by
avoiding a B-frame encoding scheme and by forcing the codec to keep its
internal network buffer as small as possible. On the browser side,
however, HTML5 does not allow any control of the video playback buffer.
Depending on the Internet connection, the browser might cache a few
seconds of video data first before starting the video playback. Best
performance with respect to latency and stability has been achieve with
recent versions of the Chrome browser.

## Source Code

Source code is available at
<https://github.com/RobotWebTools/web_video_server>.

## Support

Please send bug reports to the
[GitHub Issue Tracker](https://github.com/RobotWebTools/web_video_server/issues).
Feel free to contact us at any point with questions and comments.

- robot-web-tools@googlegroups.com
