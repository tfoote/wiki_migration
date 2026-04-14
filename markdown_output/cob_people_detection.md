## Introduction

This package contains software for detecting heads and faces and
recognizing people. Head and face detection utilize the Viola-Jones
classifier on depth or color images, respectively. Face recognition of
previously learned people is based on either Eigenfaces or Fisherfaces.
The recognition method can be configured and trained with a simple
interface as explained in the next section.

![](attachment:people_detection_image.png)
![\|width=\"280\"](attachment:person_recognition_algorithm.png)

## Quick Start

To use people detection and recognition clone the repository to your
disc and build it. \'\'\'Remark: the current cob_perception_common
release is not yet compatible with cob_people_detection. You might need
to download and build it manually from
<https://github.com/ipa-rmb/cob_perception_common.git> if you encounter
build problems.\'\'\'

For beginners: go to your home folder, create a catkin workspace,
download the code, install dependencies, build: ```
cd && mkdir -p catkin_ws/src && cd catkin_ws/src && catkin_init_workspace && cd ..
catkin_make && cd src
git clone https://github.com/ipa-rmb/cob_people_perception.git
git clone https://github.com/ipa-rmb/cob_perception_common.git
cd .. && source devel/setup.bash
rosdep install --from-path src/ -y -i
catkin_make -DCMAKE_BUILD_TYPE="Release"
```

Then install (<http://wiki.ros.org/openni_launch>) and start the Openni
driver (old Kinect, Asus) with ```
roslaunch openni_launch openni.launch
``` or the Openni2
driver (new Asus, <http://wiki.ros.org/openni2_launch>) with
```
roslaunch openni2_launch openni2.launch
``` or any other driver according to your used
sensor.

When using the openni or openni2 driver, please ensure that
\'\'\'depth_registration\'\'\' is activated (e.g. by using rosrun
rqt_reconfigure rqt_reconfigure). Also check that the
\'\'\'camera_namespace\'\'\' argument and the camera topics
\'\'\'colorimage_in_topic\'\'\' and \'\'\'pointcloud_rgb_in_topic\'\'\',
which are set in the `ros/launch/people_detection.launch` file,
correspond to the topic names of your camera driver.

Then launch people detection with ```
roslaunch cob_people_detection people_detection.launch
``` or with
```
roslaunch cob_people_detection people_detection.launch using_nodelets:=true
``` The second version uses nodelets for the first
stages of data processing which might yield a substantially better
runtime if your processor is fast enough on single core usage.

Now a window should pop up and present you with the current image of the
camera. Heads will be framed with a light blue rectangle and detected
faces are indicated in light green. For your convenience, the package
contains a client for easy usage of people detection. Start the client
with ```
rosrun cob_people_detection people_detection_client
```

No identification data will be available the first time you start the
people detection node on your computer. To record some data adjust the
frame rate of the camera, first, by choosing \'\'5 - activate/deactivate
sensor message gateway\'\' in the client and then enter 1 to activate
the sensor message gateway. The frame rate should be chosen somewhere
between 5 and 30 Hz depending on your computer\'s power.
```
Choose an option:
1 - capture face images
2 - update database labels
3 - delete database entries
4 - load recognition model (necessary if new images/persons were added to the database)
>> 5 - activate/deactivate sensor message gateway <<
6 - get detections
q - Quit

Type 1 to activate or 2 to deactivate the sensor message gateway: 1
At which target frame rate (Hz) shall the sensor message gateway operate: 20
Gateway successfully opened.
```

Now select \'\'1 - capture face images\'\' from the menu of the client
and enter the name of the first person to capture. \'\'\'Please do not
use any whitespaces in the name.\'\'\' Following, you are asked to
select how to record the data: manually by pressing a button or
automatically. In the manual mode, you have to press \'\'c\'\' each time
an image shall be captured and \'\'q\'\' to finish recording. Make sure
that only one person is in the image during recording, otherwise no data
will be accepted because the matching between face and label would be
ambiguous. ```
Choose an option:
>> 1 - capture face images <<
2 - update database labels
3 - delete database entries
4 - load recognition model (necessary if new images/persons were added to the database)
5 - activate/deactivate sensor message gateway
6 - get detections
q - Quit

Input the label of the captured person: ChuckNorris
Mode of data capture: 0=manual, 1=continuous: 0
Recording job was sent to the server ...
Waiting for the capture service to become available ...
[ INFO] [1345100028.962812337]: waitForService: Service [/cob_people_detection/face_capture/capture_image] has not been advertised, waiting...
[ INFO] [1345100028.985320699]: waitForService: Service [/cob_people_detection/face_capture/capture_image] is now available.
Hit 'q' key to quit or 'c' key to capture an image.
Image capture initiated ... 
   image 1 successfully captured.
Image capture initiated ... 
   image 2 successfully captured.
Image capture initiated ... 
   image 3 successfully captured.
Image capture initiated ... 
   image 4 successfully captured.
Finishing recording ...
Data recording finished successfully.
Current State: SUCCEEDED   Message: Manual capture finished successfully.
```

In the automatic recording mode you have to specify the number of images
that shall be collected and the time between two recordings. We
recommend to capture between 40 and 100 images per person. Make sure to
take snapshots from different perspectives and under different
illumination conditions (shadows on your face may look very different!).
```
Choose an option:
>> 1 - capture face images <<
2 - update database labels
3 - delete database entries
4 - load recognition model (necessary if new images/persons were added to the database)
5 - activate/deactivate sensor message gateway
6 - get detections
q - Quit

Input the label of the captured person: ChuckNorris
Mode of data capture: 0=manual, 1=continuous: 1
How many images shall be captured automatically? 50
What is the desired delay time in seconds between two recordings? 0.8
Recording job was sent to the server ...
Data recording finished successfully.
Current State: SUCCEEDED   Message: Continuous capture of 50 images finished successfully.
```

If you are using one of the more modern recognition methods (choices
2=LDA2D or 3=PCA2D, can be set in file
`cob_people_detection/ros/launch/face_recognizer_params.yaml` as
parameter `recognition_method`) then please be aware that they require
at least \'\'\'two different people in the training data\'\'\'. The next
step, building a recognition model, will not start with only one person
available with these algorithms. If you quit the program before
recording a second person, the program might not start anymore. Then
please delete all data from
`~/.ros/cob_people_detection/files/training_data`, start the program and
record two people.

After training, you need to build a recognition model with the new data.
To do so, just select \'\'4 - load recognition model\'\' from the
client\'s menu. In the following prompt you can either list all persons
that you captured and that shall be recognized by the system, e.g. by
typing ```
Choose an option:
1 - capture face images
2 - update database labels
3 - delete database entries
>> 4 - load recognition model (necessary if new images/persons were added to
>> the database) <<
5 - activate/deactivate sensor message gateway
6 - get detections
q - Quit

Enter the labels that should occur in the recognition model. By sending an empty list, all available data will be used.
Enter label (finish by entering 'q'): ChuckNorris
Enter label (finish by entering 'q'): OlliKahn
Enter label (finish by entering 'q'): q
Recognition model is loaded by the server ...

A new recognition model is currently loaded or generated by the server. The following labels will be covered: 
   - ChuckNorris
   - OlliKahn
The new recognition model has been successfully loaded.
Current State: SUCCEEDED   Message: Model successfully loaded.
``` or you can directly enter \'\'q\'\' and
all available persons will be trained.

After all steps succeeded, you can watch the recognition results in the
display. Although you may access all training data functions (update,
delete, etc.) from the client directly you may also access the files
directly, which are located in your home folder at
`~/.ros/cob_people_detection/files/training_data`.

## Detailed Documentation

### Overview

![\|width=\"1024\"](attachment:people_detection_scheme.png)

The cob_people_detection pipeline contains the steps head detection,
face detection, face recognition and detection tracking. Around the
pipeline there exist several nodes that provide the sensor data and
control the behaviour. The Coordinator node is the interface between
cob_people_detection and other programs. This node can open or close the
data gateway to the recognition pipeline by adjusting the behaviour of
the Sensor Message Gateway node. Furthermore, the Coordinator can handle
requests for detections in form of an action. The purpose of the Sensor
Message Gateway node is to pass sensory data at a defined rate, which
might be zero, i.e. no messages are forwarded to the pipeline.

The first step of person recognition is the Head Detector node which
detects heads in the depth image of RGB-D data. Following, the Face
Detector determines the locations of faces within these head regions.
Then the Face Recognizer identifies the name of each detected face. The
recognition results are finally collected by the Detection Tracker and
published as a topic
\`/cob_people_detection/detection_tracker/face_position_array\` that can
be subscribed to if continuous detection results are desired. If
detection of faces is supposed to happen only on demand, use the
\`get_detections_server\` action of the Coordinator.

The Face Capture node facilitates learning of new persons or the
modification of training data. The action \`add_data_server\` realizes
the addition of new training data. After the capture of new training
data the recognition model has to be rebuilt to incorporate the new
data. To do so, call the action \`load_model_server\` of the Face
Recognizer after recording new images. The People Detection Display node
can be used to display the results in a live image and to verify which
data is recorded during training.

### People Detection Client Interface

The people detection client is a convenient interface to all functions
of the people detection software. Its source code is furthermore a good
place to learn the C++ interface of people detection if it shall be
called directly from your software.

The menu provides you with the following functions: 1. \'\'\'Capture
face images\'\'\' records images for the face recognition component. Its
modes of operation have already been discussed in the Quick Start
section. 1. \'\'\'Update database labels\'\'\' updates the label of
training data items. The entries that shall be updated can be selected
either by index or by label. 1. \'\'\'Delete database entries\'\'\'
deletes data from the training set. The data is selected either by index
or by label. 1. \'\'\'Load recognition model\'\'\' This function loads
or trains a recognition model for the desired compilation of people from
the training set. See example in the Quick Start section. It is
necessary to run this function whenever new training data has been
recorded and shall be used. 1. \'\'\'Activate/deactivate sensor message
gateway\'\'\' controls the gateway which passes sensory data at a given
rate to the pipeline. 1. \'\'\'Get detections\'\'\' is an example for
the action interface to the results. The action can also be called when
the gateway is closed - then it will be automatically opened for a short
time until the detections are received. The other way of accessing the
detection results is to simply open the gateway and subscribe to the
/cob_people_detection/detection_tracker/face_position_array topic.

```
roslaunch openni_launch openni.launch
```0

## Support

Please consult to see if your problem is already known.

Please use the
[mailing list](http://www.care-o-bot-research.org/contributing/mailing-lists)
for additional support or feature discussion.

## References

If you are using this software in your work, please cite the Humanoids
paper from 2013.

1\. Ninghang Hu, Richard Bormann, Thomas Zwölfer, and Ben Kröse,
\"Multi-User Identification and Efficient User Approaching by Fusing
Robot and Ambient Sensors,\" in Proceedings of the IEEE Conference on
Robotics and Automation (ICRA), 2014. 1. Richard Bormann, Thomas
Zwölfer, Jan Fischer, Joshua Hampp, and Martin Hägele, \"Person
Recognition for Service Robotics Applications,\" in Proceedings of the
13th International IEEE-RAS International Conference on Humanoid Robots,
2013. 1. Jan Fischer, Daniel Seitz, and Alexander Verl, \"Face Detection
using 3-D Time-of-Flight and Colour Cameras,\" in: Neumann, Kristin
(Ed.) u.a.; International Federation of Robotics u.a.: Joint
International Conference of ISR/ROBOTIK2010: Munich, 7-9 June 2010.
Berlin; Offenbach: VDE-Verlag, 2010, S. 112-116.
