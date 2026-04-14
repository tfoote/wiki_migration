## Nodes

```clearsilver
node.0{
name=image_capture
desc= The `image_capture` node captures images from one or more cameras and saves them to the filesystem.
param {
  0.name=~numCams 
  0.default=`1`
  0.type= integer
  0.desc= Number of cameras to capture from.

  1.name= ~output_folder
  1.default=`/tmp`
  1.type= string
  1.desc= Output folder where captured images are saved

  2.name= ~camera$i
  2.default=`/stereo/left/image_raw`
  2.type= string
  2.desc= Image topic of camera$i. Repeat for every camera (e.g. camera1, camera2, camera3)

  3.name= ~file_prefix$i
  3.default=`false`
  3.type= string
  3.desc= File prefix for images from camera$i. Repeat for every camera (e.g. file_prefix1, file_prefix2, file_prefix3)
}
srv {
  0.name= ~capture()
  0.type= cob_calibration_srvs/Capture
  0.desc= Acquire image from all cameras and save as jpg to output folder. 
}
}
```
