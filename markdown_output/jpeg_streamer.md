## Nodes



```clearsilver
node.0 {
 name = jpeg_streamer
 desc = Given a <<MsgLink(sensor_msgs/CompressedImage)>> topic, creates a JPEG-over-HTTP stream.
 sub{
  0.name= image
  0.type= sensor_msgs/CompressedImage
  0.desc= Image topic (e.g., /camera/image_raw/compressed)
 }
 param{
  0.name= ~port
  0.default= 8080
  0.type= int
  0.desc= HTTP port to listen on
  1.name= ~skip
  1.default= 0
  1.type= int
  1.desc= Throw out this many images for every image used
  2.name= ~start_threads
  2.default= 1
  2.type= int
  2.desc= Number of threads to spawn initially. One thread per client.
  3.name= ~max_threads
  3.default= 16
  3.type= int
  3.desc= Limit on number of concurrent clients. Idle threads will be removed.
  }
```


