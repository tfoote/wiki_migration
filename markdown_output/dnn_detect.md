## Nodes



```clearsilver
name = dnn_detect
desc = dnn_detect uses the [[https://docs.opencv.org/3.3.0/d2/d58/tutorial_table_of_content_dnn.html|OpenCV Deep Neural Network module]] to find objects in an image stream and provide their bounding boxes.

srv {
  0.name= ~detect
  0.desc= Trigger a detection when in single-shot mode
  0.type= dnn_detect/Detect
}
sub {
  0.name= /camera
  0.desc= The images to be processed.
  0.type= sensor_msgs/Image
}
pub {
  0.name= /dnn_objects
  0.type= dnn_detect/DetectedObjectArray
  0.desc= Details of detected objects
  1.name= /dnn_images
  1.type= sensor_msgs/Image
  1.desc= Input image with detected objects outlined
}
param {
  0.name= ~single_shot
  0.type= bool
  0.desc= If set, detection is only performed when the `detect` service is called
  0.default= false
  1.name= ~publish_images
  1.type= bool
  1.desc= If set, images with objects outlined will be published
  1.default= true
  2.name= ~data_dir
  2.type= string
  2.desc= Path to directory containing data
  3.name= ~protonet_file
  3.type= string
  3.desc= Name of protonet file, relative to `data_dir`
  4.name= ~caffe_model_file
  4.type= string
  4.desc= Name of caffe model file, relative to `data_dir`
  5.name= ~min_confidence
  5.type= float
  5.desc= Minimum confidence (0..1) for an object to be included in the results
  5.default= 0.2
  6.name= ~im_size
  6.type= int
  6.desc= size of image (pixels) to operate on 
  6.default=300
  7.name= ~scale_factor
  7.type= float
  7.default=0.007843
  7.desc= Scale factor for model - the intensity values in the image are multiplied by this
  8.name= ~mean_val
  8.type= float
  8.desc = Mean value for model - this is subtracted from the intensity values in the image
  8.default= 127.5
  9.name= ~class_names
  9.type= string
  9.desc= Comma delimited list of class names
9.default=background, aeroplane, bicycle, bird, boat, bottle, bus, car, cat, chair, cow, diningtable, dog, horse, motorbike, person, pottedplant, sheep, sofa, train, tvmonitor
}
```



## Installation



```
sudo apt install ros-kinetic-dnn-detect
```



## Sample Usage

The sample launch file uses
[chuanqi305's MobileNet-SSD](https://github.com/chuanqi305/MobileNet-SSD)

A camera node, such as [usb_cam](usb_cam) needs to be running

For example: 

```
rosrun usb_cam usb_cam_node
```



Then `dnn_detect` can be launched: 

```
roslaunch dnn_detect dnn_detect.launch camera:=/usb_cam image:=image_raw
```

 and the
results viewed with: {{ rqt_image_view /dnn_images or:


```
rostopic echo /dnn_objects
```


