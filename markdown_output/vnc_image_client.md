## Nodes

```clearsilver

name=vnc_image_client.py
desc=Allows to publish a [[http://en.wikipedia.org/wiki/Virtual_Network_Computing|VNC]] stream to a specified image topic. If the VNC server has a password set, the password can either be passed as parameter or entered during node start-up.
param {

  1.name= ~host
  1.default=`localhost`
  1.type= string
  1.desc= VNC server host
  2.name= ~port
  2.default=`5901`
  2.type= integer
  2.desc= VNC server port
  3.name= ~password
  3.default=`""`
  3.type= string
  3.desc= Password for the VNC server. If the VNC server has a password and this parameter is not set, the password is requested during node start-up.
  4.name=~image_topic 
  4.default=`"vnc_image"`
  4.type= string
  4.desc= The name of the image topic on which the VNC stream will be published
  5.name=~publish_rate
  5.default=`15`
  5.type= integer
  5.desc= Maxmimum frame rate for the image topic
}
pub {
  0.name= ~<image_topic>
  0.type= sensor_msgs/Image
  0.desc= The images from the VNC stream
}
```

## Usage

```
rosrun vnc_image_client vnc_image_client.py \
     _host:=<vnc_host> _port:=<vnc_port> _password:=<your_secret> \
     _image_topic:=<image_output_topic> _publish_rate:=<image_publish_rate>
``` An example launch file is provieded in the
\`launch\` folder.
