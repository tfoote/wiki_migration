## Overview

The srs_mixed_reality server is an component of the
[SRS Project](http://srs-project.eu/) for elderly care robot named
[Care-O-Bot](http://ros.org/wiki/care-o-bot). Using the information from
the map server,
[Household database](http://ros.org/wiki/srs_object_database) and
[SRS Knowledge Database](http://ros.org/wiki/srs_knowledge) it provides
augmented reality stream for the
[UI_PRI](http://ros.org/wiki/srs_ui_pri) user interface.

## System architecture

The Mixed reality server consists of 5 nodes:

### MRS

This node streams as a standard MJPEG/HTTP videostream the map
information and augmented reality -- household objects such a furniture
and graspable objects. It also provides the functionality to stream
selected ROS image topics.

The MRS node subscribes to /control_mrs topic which feeds object
information for the augmented map drawing. The topic is published by the
ControlMRS node.

### ControlMRS

This node generates the combined information for the augmented reality
using service calls to the SRS Household Database (info about the object
size, grasping possibility and icon) and SRS Knowledge Database (info
about name, class and pose).

The published topic (/control_mrs) structure is:



```
string command # Can be ADD or REMOVE (add or remove object from augmented map)

uint32 virtual_obj_number # the unique number of the object on the virtual map

uint32 virtual_obj_count  # total number of the objects drawn on current frame of the virtual map

string topic # name of the image topic which will be augmented

int32 id # ID of the object in HH DB

string label # Text to label the drawn object

int32 type # Possible types:
# 1 - CONTOUR_RECTANGLE; (only for augmentation level 2)
# 2 - CONTOUR_ELIPSE; (only for </nowiki>augmentation level 2)
# 3 - USE IMAGE (only for augmentation level 3)

float32 x # Center of the drawn object on x axis

float32 y # Center of the drawn object on y axis

float32 width # Width of the object bounding box

float32 height # Height of the object bounding box

float32 angle # Rotation of the object in Degrees

string clr 
# clr - Color of the object representation shape in HTML color – for exmple #FF0000 red
# (valid only for augmentation level 2)

sensor_msgs/Image image # topview image icon for the object (only for augmentation level 3)
```



### RealityPublusher

This node provide information to the UI about the objects located on the
augmented map.

The published topic - /map_active_areas consists of ros header and array
of data which conatains all the objects presented on the virtual map.


```
Header header

uint32[] object_id # IDs of the object in Household Database

string[] object_name # Object names – eg. Table, Fridge and etc.

string[] object_base_shape # Object base shapes (currently rectangle or ellipse)

uint32[] object_type # Object types such as furniture, unknown.

uint32[] x1 # Top left corners of object bounding box (x axis) in pixel coordinates

uint32[] y1 # Top left corners of object bounding box (y axis) in pixel coordinates

uint32[] x2 # Bottom right corners of object bounding box (x axis) in pixels

uint32[] y2 # Bottom right corners of object bounding box (y axis) in pixels

uint32[] angle # Bounding box rotation angles in degrees

bool[] graspable # Grasping possibility
```



### MapTF

This node converts the coordinates, and sizes from ROS metric to pixel
coordinates on virtual map and vice versa. It is provided as a ROS
service srs_mixed_reality_server/MapTransform:



```
uint32 transform_type 
# Transform type can be:
# 1 - transform position from metric to map pixel coordinates
# 2 - transform size from metric to map pixel size
# 3 - transform position from pixel to metric coordinates
# 4 - transform size from pixels on map to metric
geometry_msgs/Point world_coordinates (input point in metric - types 1 and 2 or pixels - types 3 and 4)
---

geometry_msgs/Point map_coordinates (output point in pixels - types 1 and 2 or metric - types 3 and 4)
```



It also publishes the position of the robot in pixel map coordinates on
topic /maptf.

### Assisted Detection Node

The Care-O-Bot assisted detection feature enables the user to initiate
the detection process on selected region and choose the right object in
the UI_PRI, when multiple detections are available. This is implemented
via the assisted detector node in the Mixed reality server, BB Estimator
and srs_assisted_detection stack. Assisted Detector node This node
operates as an ROS service /srs_assisted_detector called from the UI_PRI
via the ROSBridge. The service have the following input parameters:


```
uint32 operation # 1 UIDetection, 2 BBMove, 3 Test
std_msgs/String name # Name of the detected object
int16[2] p1 # x1,y1 coordinates of the selected region in the UI /operation mode 2/
int16[2] p2  # x2,y2 coordinates of the selected region in the UI /operation mode 2/
```

 The service response is:


```
string[] object_name # Array of the object labels detected
uint32[] x1 # Array of the object x1 coordinates detected
uint32[] y1 # Array of the object y1 coordinates detected
uint32[] x2 # Array of the object x2 coordinates detected
uint32[] y2 # Array of the object y2 coordinates detected
std_msgs/String message # response from the BBMove if any
```

 Operation modes

1\. Operation mode 1 - UIDetect The user start the detection process in
the UI_PRI via clicking on the Detect button. The service
/srs_assisted_detector is called. It triggers the call to UIDetect
service and converting the received array of detected objects from 3d
bounding boxes to camera pixel coordinates via the BB Estimator Alt
service. The output of the detected objects with the corresponding pixel
coordinates is then passed back to the UI_PRI. After that an 2d
rectangle around the object is displayed in the UI video. The user can
select particular object and its id is passed via the UIAnswer service.

2\. Operation mode 2 -- if the detection is not successful the user can
select an region of interest and the robot will be repositioned to allow
better detection. The /srs_assisted_detector service is called with
operation value 2 and p1,p2 coordinates of the selected points. The
assisted detector calls BB Estimator to transform the coordinates from
2d to 3d bounding box and then calls the BBMove service. The response of
the BBMove service is then passed to the UI. And if it possible the
BBMove service repositions the robot to enable better detection.

3\. Operation mode 3 -- This mode is for test purpose only. It allows to
test if the Assisted detector node is running, the communication path
and the video overlay augmentation in the UI_PRI. In this mode the
service /srs_assisted_detector returns coordinates and name of a test
object - Milk box.

[Assisted Detection Theory of operation](attachment:diagram1.png)

## Installation

These SRS package is not open to the public. If you want to run the
packages, please write to goa@ipa.fhg.de, fmw@ipa.fhg.de. You can then
fetch the source from the [github](https://github.com/ipa320/srs).


```
rosmake srs_mixed_reality_server
```



## Configuration

The node can be configured via its launch file -- MRS.launch. You can
customize the virtual map size and the augmentation level -- 0 draw map
only, 1 draw map and graphical representation of the objects (rectangles
and ellipses) and 2 draw map with image icons. 

```
<param name="mapWidth"           value="1024" type="int"/>
<param name="mapHeight"          value="1024" type="int"/>
<param name="augmentationLevel"  value="2"    type="int"/>
```



## To start Mixed Reality Server



```
roslaunch srs_mixed_reality_server MRS.launch
```



## Dependencies

In order to generate augmented map you need following components
compiled and running: 

```
roscore

Care-O-bot simulation in gazebo or the real robot

cob_2dnav (Care-O-Bot navigation stack)

srs_knowledge (SRS Knowledge Database)

srs_object_database (The Household Objects Database)

rosbridge (to communicate to the UI_PRI)
```



## Testing

You can test the output result using the UI_PRI on iPad or using a
standard websockets compliant browser -- as Google Chrome.


```
To view a snapshot - please open: 
http://127.0.0.1:8080/snapshot?topic=/map 

To view the live stream - please open: 
http://127.0.0.1:8080/stream?topic=/map

You can monitor any ROS image topic for example:
http://127.0.0.1:8080/stream?topic=/stereo/right/image_raw 

Note: replace 127.0.0.1 with the IP of your ROS server where you run the MRS.
```


