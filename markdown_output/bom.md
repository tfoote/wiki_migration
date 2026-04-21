## Algorithms

Bayesian object mapper (bom) is a package for semantic SLAM. This
package consists of:

### Objects detection and localization

Using Bayesian fusion of a semantic data (SSD\\YOLO) and depth data
(laser scan\\depth camera). Each object is assign with identity in the
form of a joint probability function of its traits (shape, class, etc.).

### Objects update

Recognizing, associating and updating objects identity with new
observations.

## Example - experiment

[Youtube](https://www.youtube.com/watch?v=mQHh478gTg8)

## Example - Gazebo simulation

[Youtube](https://www.youtube.com/watch?v=-H25q_Vcol8)

## Nodes

```clearsilver
node.0 {
  name=ssd_node
  desc=`ssd_node` takes in an RGB image and produce a list with potential objects, their corresponding class and bounding boxes. This node is forked from https://github.com/balancap/SSD-Tensorflow.
  sub{
    0.name= camera/image_raw/
    0.type= sensor_msgs/Image
    0.desc= RGB camera input stream.
  }

pub{
    0.name= im_info
    0.type= object_detector_ssd_tf_ros/SSD_Outputs
    0.desc= List of objects with their probability mass functions, their detection probability and bounding boxes.
    1.name= ssd_image_output
    1.type= sensor_msgs/Image
    1.desc= An RGB image with the detected objects and their most probable class, mainly for debugging.
  }
}

node.1 {
  name=Object_Detection
  desc=`Object_Detection` fuses the semantic information stream from the `ssd_node` with the depth data stream (laser scan).
  sub{
    0.name= /im_info
    0.type= object_detector_ssd_tf_ros/SSD_Outputs
    0.desc= List of objects.
    1.name= /scan
    1.type= sensor_msgs/LaserScan
    1.desc= Laser scanner observations.
    2.name= /odom
    2.type= nav_msgs/Odometry
    2.desc= Robots odometry data.
    3.name= /slam_out_pose
    3.type= geometry_msgs/PoseStamped
    3.desc= Localization data.

  }

pub{
    0.name= /Theta_List
    0.type= joint_object_localizer/OG_List
    0.desc= List of objects identities and parameters.
  }

param{
  0.name= /Array/round
  0.default=[5,16]
  0.type= int array
  0.desc= Association between objects class and circles.
  1.name= /Array/rectangle
  1.default=[2,14,18,20]
  1.type= int array
  1.desc= Association between objects class and rectangles.
  2.name= /Array/elliptical
  2.default= [3,8,9,12,15,17]
  2.type= int array
  2.desc=  Association between objects class and ellipticals.
  3.name= /Array/object_list
  3.default= [2,3,5,8,9,12,14,15,16,17,18,20]
  3.type= int array
  3.desc=  Association between objects and available likelihood fumctions.
  4.name= /Cord_cor/Simulation/Correction
  4.default=0.15
  4.type= double
  4.desc=  Camera field of view correction factor.
}
}

node.2 {
  name=Object_Mapper
  desc=`Object_Mapper` keep tracks on the mapped objects. It associates new observations with the objects and choose whether to update a certain objects or to create new one.
  sub{
    0.name= /Theta_List
    0.type= joint_object_localizer/OG_List
    0.desc= List of objects.
  }

pub{
    0.name= /object_mapped_values
    0.type= object_mapping/Object_Map
    0.desc= List of objects identities and parameters.
  }

param{
  0.name= /Array/rectangle
  0.default=[2,14,18,20]
  0.type= int array
  0.desc= Association between objects class and rectangles.
  1.name= /Array/elliptical
  1.default= [3,8,9,12,15,17]
  1.type= int array
  1.desc=  Association between objects class and ellipticals.

}
}
```

## References

This work is summarized in a yet to be published paper - "Representing
and updating object identities in semantic SLAM".
