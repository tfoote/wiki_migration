ROS driver for thingmagic RFID serial readers using the
[ Mercury API](http://www.thingmagic.com/index.php/manuals-firmware#Mercury_API).
Currently only supports serial/USB communications.

### Supported Devices

Supports serial reader interface through the SDK. This should include
the Mercury5e and Mercury6e series, USB, Vega, Micro and Nano readers.
Currently only tested with the
[USB Pro](http://www.thingmagic.com/usb-pro-rfid-reader) reader.

## ROS Nodes

```clearsilver
node.0 {
 name = thing_reader_node
 desc = ROS node asynchronously reports RFID tag reads. 
 pub {
  0.name= rfid
  0.type= std_msgs/String
  0.desc= RFID tag identification as hex string.
 }
 param {
  0.name = port
  0.type = string
  0.desc = Serial port.
  0.default = /dev/ttyACM0
 }
}
```
