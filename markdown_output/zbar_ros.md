This package is a lightweight wrapper around the
[Zbar](http://zbar.sourceforge.net/) barcode processing library. It
provides a node and a nodelet with equivalent interface. The `image`
topic is a lazy subscription that is active only when the `barcode`
topic has a client.

## Node API

### barcode_reader_node

The `barcode_reader_node` listens to image data (camera or otherwise)
on the incoming topic, outputs the contents of any barcodes detected in
the images.

#### Subscribed Topics

- `image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Image input to scan for barcodes.

#### Published Topics

- `barcode`
  ([std_msgs/msg/String](https://docs.ros.org/en/rolling/p/std_msgs/msg/String.html)):
  Barcodes detected in image input.

#### Parameters

- `~throttle_repeated_barcodes` (`double`): Time (s) to throttle any
  repeated barcode scans. If `0.0`, all detected barcodes will be
  output as fast as the node can process the incoming images.

## Nodelet API

Same API as node, available as `zbar_ros/barcode_reader_nodelet`.
