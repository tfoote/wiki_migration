Mech Turk ROS package contains tools to annotation images
(sensor_msgs/Image) with boxes and outlines of objects. The package
provide:

-   image_snapper.py - a node to send all images from a topic for
    annotation
-   session_2_messages.py - retrieve all annotations from a session and
    send them as messages
-   link_topic.py - a temporary tool to register remote publishers in
    the local core
-   annotate_image_action_server.py - multi-goal action server
    implementing AnnotateImageAction

## ROS API

```clearsilver
node.0 {
name=image_snapper
desc=Captures images and submits them for annotation
sub{
0.name= image
0.type= sensor_msgs/Image
0.desc= Stream of images 
}
param{
  0.name=~server
  0.default=`"default"`
  0.type= string
  0.desc= The URL or alias of the server.
  1.name=~session
  1.default=REQUIRED
  1.type= string
  1.desc= The name of the session
  2.name=~submit_enabled
  2.default=False
  2.type= bool
  2.desc= if enabled, the images are submitted for annotation. The submission is disabled by default.
  3.name=~jpeg_output_dir
  3.default=EMPTY
  3.type= bool
  3.desc= The folder name where to save images. If unset, the images are not saved locally.

}
}
node.1 {
name=annotate_image_action
desc=Anntoate image action server provides an implementation of AnnotateImage action.  
sub {
  0.name= annotate_image_action/goal
  0.type= mech_turk_ros/AnnotateImageActionGoal
  0.desc=An image to annotate. 
  1.name= annotate_image_action/cancel
  1.type= actionlib_msgs/GoalID
  1.desc= A request to cancel a specific goal.
  2.name= annotation
  2.type= mech_turk_ros_msgs/ExternalImageAnnotation
  2.desc= The topic on which annotation server broadcasts the annotations (can be specified through ~annotation_topic)
}
pub {
  0.name= annotate_image_action/feedback
  0.type= mech_turk_ros/AnnotateImageActionFeedback
  0.desc= Feedback is not provided.
  1.name= annotate_image_action/status
  1.type= actionlib_msgs/GoalStatusArray
  1.desc= Provides status information on the goals that are sent to the `annotate_image` action.
  2.name= annotate_image_action/result
  2.type= mech_turk_ros/AnnotateImageActionResult
  2.desc= Result contains the mech_turk_ros_msgs/ExternalImageAnnotation with the resulting annotation.
}
param{
  0.name=~server
  0.default=`"default"`
  0.type= string
  0.desc= The URL or alias of the server.
  1.name=~session
  1.default=REQUIRED
  1.type= string
  1.desc= The name of the session
  2.name=~annotation_topic
  2.default="annotation"
  2.type= string
  2.desc= New name of the topic on which the server publishes annotations
  3.name=/run_id
  3.default=
  3.type= string
  3.desc= Run ID is used to generate unique image IDs.
}
}
node.2 {
name=link_topic
desc=Links local annotation topic to the remote server annotation topic. Remote topic "/annotation" is linked to the local "annotation" topic. Local topic can be remapped or specified in "~local_topic_name". Either "url" or "server" is required.

pub {
  0.name= annotation
  0.type= mech_turk_ros_msgs/ExternalImageAnnotation
  0.desc= Annotations from the remote server
}
param{
  0.name=~url
  0.default=NONE
  0.type= string
  0.desc= The URL of the remote web server
  1.name=~server
  1.default=NONE
  1.type= string
  1.desc= The alias of the remote web server
  2.name=~remote_topic_name
  2.default=/annotation
  2.type= string
  2.desc= The name of the remote topic to link from  
}
}
node.3 {
name=session_2_messages
desc=Downloads all annotations from the server and publishes them as messages.
pub {
  0.name= annotation
  0.type= mech_turk_ros_msgs/ExternalImageAnnotation
  0.desc= Annotations from the remote server
}
param{
  1.name=~server
  1.default="default"
  1.type= string
  1.desc= The alias of the remote web server
  2.name=~target_session
  2.default=REQUIRED
  2.type= string
  2.desc= The name of the annotation session on the server
  3.name=~quality_filter
  3.default="none"
  3.type= string
  3.desc= The quality filter: "none" - no filtering, "good" - only good submissions.
  
}
}
```

## Image UID

Mech turk ROS generates unique IDs for images to refer to images in the
annotations. The image unique ID is formed as: `run_id.topic.secs.nsecs`
. We replace "/" with "-" in the topic name to ensure that the UID
can be used as part of a URL.

This UID format is used by image_snapper and
annotation_image_action_server to identify images on the annotation
server. The UID is then saved in the ImageReference.uid field. The
image_snapper and annotate_image_action_server require the image header
to have a non-empty time stamp.
