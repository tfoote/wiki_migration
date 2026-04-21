## About

This package provides a video stream of a ROS image transport topic that
can be accessed via HTTP.



```clearsilver
param {
  0.name = ~port
  0.type = integer
  0.desc = Port number to listen for http requests.
  0.default = 8080

  1.name = ~address
  1.type = string
  1.desc = Address to listen for http requests
  1.default = 0.0.0.0

  2.name = ~server_threads
  2.type = integer
  2.desc = The number of threads used to serve HTTP requests (these are not used for actual image streams).
  2.default = 1

  3.name = ~ros_threads
  3.type = integer
  3.desc = The number of threads running ros spinners. These threads are used to do the actual image encoding. These threads are shared between all current streams so the number does not need to match the number of connections.
  3.default = 2

}
```



## Usage

The web_video_server opens a local port and waits for incoming HTTP
requests. As soon as a video stream of a ROS image topic is requested
via HTTP, it subscribes to the corresponding topic and creates an
instance of the video encoder. The encoded raw video packets are served
to the client. Parameters can be specified by adding additional them to
the query string. To connect to the node with your browser, use the
following URLs:

### Available URLs

-   Overview of available ROS topics: `http:*localhost:8080/` \*
    Webpage showing a video stream:
    `http:*localhost:8080/stream_viewer?topic={ROS_TOPIC}`
-   Video stream URL: `http:*localhost:8080/stream?topic={ROS_TOPIC}`
    \* Snapshot of next image:
    `http:*localhost:8080/snapshot?topic={ROS_TOPIC}`

Several parameters can be configure via the video stream URL - Example:
<http://localhost:8888/stream?topic=depthcloud_encoded&bitrate=250000&type=vp8>

### Image Parameters

These are the parameters that can be used to configure a stream or
snapshot:



```clearsilver
param {
  no_header= True
  0.name= width
  0.type= integer
  0.default= original width
  0.desc= The image stream will be resized to a new width and height. This parameter has to be used in conjunction with the height parameter.
  1.name= height
  1.type= integer
  1.default= original height
  1.desc= The image stream will be resized to a new width and height. This parameter has to be used in conjunction with the height parameter.
  2.name= quality
  2.type= integer
  2.default= 90
  2.desc= The jpeg image quality (1...100). This parameter can be used to reduce the size of the resulting stream.
  3.name= invert
  3.type= none
  3.default=
  3.desc= Rotates the image by 180 degrees before streaming.
  4.name= default_transport
  4.type= string
  4.default= "raw"
  4.desc= The image transport to use (raw, compressed, theora).
}
```



### Snapshot Parameters

These are the parameters that can be used to configure a snapshot:



```clearsilver
param {
  no_header= True
  0.name= quality
  0.type= integer
  0.default= 95
  0.desc= The jpeg image quality (1...100). This parameter can be used to reduce the size of the resulting stream.
}
```



### Stream Parameters

These are the parameters that can be used to configure a stream:



```clearsilver
param {
  no_header= True
  0.name= type
  0.type= string
  0.default= mjpeg
  0.desc= The encoding method for the stream (mjpeg, vp8, ros_compressed, png, h264).
}
```

 Additional parameters can be specified for each
encoding type as described below.

#### Mjpeg Stream Parameters

These are the parameters that can be used to configure a mjpeg stream:



```clearsilver
param {
  no_header= True
  0.name= quality
  0.type= integer
  0.default= 95
  0.desc= The jpeg image quality (1...100). This parameter can be used to reduce the size of the resulting stream.
}
```



#### VP8 Stream Parameters

These are the parameters that can be used to configure a vp8 stream:



```clearsilver
param {
  no_header= True
  0.name = bitrate
  0.type = integer
  0.desc = Maximum bitrate setting. Note that a small bitrate could significantly increase the latency due to a delayed transmission of larger intra frames.
  0.default = 100000

  1.name = qmin
  1.type = integer
  1.desc = Minimum quantizer.
  1.default = 10

  2.name = qmax
  2.type = integer
  2.desc = Maximum quantizer.
  2.default = 42

  3.name = gop
  3.type = integer
  3.desc = Keyframe interval, this determines the maximum distance between I-frames.
  3.default = 250

  4.name = quality
  4.type = string
  4.desc = The encoding quality.
  4.default = realtime
}
```

 More information on the quality and profile
parameter of the VP8 codec can be found here:
<http://www.webmproject.org/docs/encoder-parameters>

### Unsupported customizations

#### Control image subscription rate

Rate at which `web_video_server` subscribes a image topic depends on
the publisher's publish rate. With a fast publish rate, a client host
may unintentionally get busy.

As of version 0.2.1, `web_video_server` does not come with a feature
to control the rate at which the frontend subscribes to an image topic.
You can work this around on your client.

One way is to republish the image topic with a lower rate. You can use
[throttle from topic_tools package](topic_tools/throttle#throttle_message_.28rate.29).

### ROS-Compressed Stream Example

rostopic list output:



```
$ rostopic list
/usb_cam/camera_info
/usb_cam/image_raw/compressed
```



View compressed stream at:
`http:*localhost:8080/stream?topic=/usb_cam/image_raw&type=ros_compressed`*

Node and topic diagram (output of [rqt_graph](rqt_graph)). **NOTE** this
graph is **NOT** showing compressed image topic, so this screenshot
isn't showing exactly the same situation we're running above where the
box in the middle should be the compressed image topic. Hope this still
gives an idea of relationship:

![alt Node and topic diagram\|width="700"](attachment:rqt_graph-output-usb_cam-sample.png)

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

-   robot-web-tools@googlegroups.com
