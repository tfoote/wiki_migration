## Nodes

The `mono_calibration` and `stereo_calibration` node can be used to
calibrate monocular and stereo cameras and can be used for every
robot/camera. They are general purpose calibration nodes which perform
automatic calibration; only images of a checkerboard calibration object
located somewhere on disk are needed.



```clearsilver
node.0{
name=mono_calibration
desc= The `mono_calibration` node performs automatic monocular camera calibration of a camera using jpg images of a checkerboard calibration object.
param {
  0.name=~folder
  0.type= string
  0.default=`.`
  0.desc= Folder where images are saved.

  1.name= ~pattern_size
  1.type= string
  1.default=`9x6`
  1.desc= Size of calibration object (see OpenCV documentation).

  2.name= ~square_size
  2.type= string
  2.default=`0.03`
  2.desc= Size of single checkerboard square.

  3.name= ~image_prefix
  3.type= string
  3.default=`camera`
  3.desc= Prefix of image files.

  4.name= ~camera_name
  4.type= string
  4.default=`camera`
  4.desc= Name of camera.

  5.name= ~frame_id
  5.type= string
  5.default=`/camera`
  5.desc= ROS frame id of camera.

  6.name= ~output_file
  6.type= string
  6.default=`./camera.yaml`
  6.desc= Path to yaml file where camera calibration results are saved.

  7.name= ~alpha
  7.type= float
  7.default=`0`
  7.desc= All pixels in undistorted cropped image are valid, set to 1.0 to preserve every pixel from original image.

  8.name= ~verbose
  8.type= bool
  8.default=`false`
  8.desc= Set to `true` to output more info to terminal.
}
}

node.1{
name=stereo_calibration
desc= The `stereo_calibration` node performs automatic stereo camera calibration using jpg images of a checkerboard calibration object.
param {
  0.name=~folder
  0.type= string
  0.default=`.`
  0.desc= Folder where images are saved.

  1.name= ~pattern_size
  1.type= string
  1.default=`9x6`
  1.desc= Size of calibration object (see OpenCV documentation).

  2.name= ~square_size
  2.type= string
  2.default=`0.03`
  2.desc= Size of single checkerboard square.


  3.name= ~image_prefix_l
  3.type= string
  3.default=`left`
  3.desc= Prefix of image files of left camera.

  4.name= ~camera_name_l
  4.type= string
  4.default=`left`
  4.desc= Name of left camera.

  5.name= ~frame_id_l
  5.type= string
  5.default=`/left`
  5.desc= ROS frame id of left camera.

  6.name= ~output_file_l
  6.type= string
  6.default=`./left.yaml`
  6.desc= Path to yaml file where camera calibration results of the left camera are saved.


  7.name= ~image_prefix_r
  7.type= string
  7.default=`right`
  7.desc= Prefix of image of right files.

  8.name= ~camera_name_r
  8.type= string
  8.default=`right`
  8.desc= Name of right camera.

  9.name= ~frame_id_r
  9.type= string
  9.default=`/right`
  9.desc= ROS frame id of right camera.

  10.name= ~output_file_r
  10.type= string
  10.default=`./right.yaml`
  10.desc= Path to yaml file where camera calibration resultsof the right camera are saved.

  11.name= ~calibration_urdf_in
  11.type= string
  11.default=``
  11.desc= Optional: Set path to urdf file which will be read while updating baseline

  12.name= ~calibration_urdf_out
  12.type= string
  12.default=``
  12.desc= Optional: Set path to urdf file in which baseline property should be saved

  13.name= ~calibration_urdf_out
  13.type= string
  13.default=`cam_r_`
  13.desc= Optional: Prefix of baseline property in urdf file

  14.name= ~alpha
  14.type= float
  14.default=`0`
  14.desc= All pixels in undistorted cropped image are valid, set to 1.0 to preserve every pixel from original image.

  15.name= ~verbose
  15.type= bool
  15.default=`false`
  15.desc= Set to `true` to output more info to terminal.
}
}
```


