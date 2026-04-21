This package is a lightweight wrapper around the
[Zbar](http://zbar.sourceforge.net/) barcode processing library. It
provides a node and a nodelet with equivalent interface. The `image`
topic is a lazy subscription that is active only when the `barcode`
topic has a client.

## Node API

```clearsilver
name = barcode_reader_node
desc = The `barcode_reader_node` listens to image data (camera or otherwise) on the incoming topic, outputs the contents of any barcodes detected in the images.
sub {
  0.name = image
  0.type = sensor_msgs/Image
  0.desc = Image input to scan for barcodes.
}
pub{
  0.name = barcode
  0.type = std_msgs/String
  0.desc = Barcodes detected in image input.
}
param {
  0.name = ~throttle_repeated_barcodes
  0.type = double
  0.desc = Time (s) to throttle any repeated barcode scans. If `0.0`, all detected barcodes will be output as fast as the node can process the incoming images.
}
```

## Nodelet API

Same API as node, available as `zbar_ros/barcode_reader_nodelet`.
