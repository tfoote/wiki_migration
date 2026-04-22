## Overview

`polled_camera` defines the ROS interface that client nodes use to
request images from a polling camera driver node (e.g.
[prosilica_camera](prosilica_camera)). The protocol is:

-   The camera driver advertises a service call
    `<camera>/request_image` of type
    [polled_camera/srv/GetPolledImage](https://docs.ros.org/en/rolling/p/polled_camera/srv/GetPolledImage.html).
-   The client calls the service, specifying an output namespace.
-   On receiving a request, the driver captures an image and returns its
    time stamp in the service response.
-   The driver publishes (latching) the
    [sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)
    and
    [sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)
    to `<response_namespace>/image_raw` and
    `<response_namespace>/camera_info`.
-   Clients subscribe to the response topics just like any other camera
    image stream.
-   When a disconnection causes the number of subscribers to drop to
    zero, the publisher shuts down.

See the [code API](http://www.ros.org/doc/api/polled_camera/html/)
(unstable) for more information on writing polled camera drivers or
clients.

There are several reasons for publishing images to topics instead of
returning them from the service call:

-   Consistency. Client-side processing is always performed in an image
    callback, regardless of what type of camera is used.
-   Visibility. Topics can be monitored in [image_view](image_view) or
    [rviz](rviz).
-   Reproducibility. Topics can be [bagged](rosbag) and played back
    later.
-   Compression: Can take advantage of
    [image_transport](image_transport) to compressed images, if desired.

## Nodes

### poller

Continually requests images from a polled camera at a specified rate in
Hz, making the camera look like it is capturing continuously.

Usage: 

```
# Poll "my_camera" at 5 Hz, publishing in namespace my_polled_output/.
$ poller 5 camera:=my_camera output:=my_polled_output
```

 

```clearsilver
pub {
  0.name = <output>/image_raw
  0.type = sensor_msgs/Image
  0.desc = Image topic, actually published by the camera driver. `output` should be remapped by the user.
  1.name = <output>/camera_info
  1.type = sensor_msgs/CameraInfo
  1.desc = Info topic, actually published by the camera driver. `output` should be remapped by the user.
}
srv_called {
  0.name = <camera>/request_image
  0.type = polled_camera/GetPolledImage
  0.desc = The camera driver's polled image service. `camera` should be remapped by the user to the camera namespace.
}
```


