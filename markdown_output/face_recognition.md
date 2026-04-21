The ProcRob face_recognition package can be downloaded from
<https://github.com/procrob/face_recognition> . For usage guide, please
see below. For details of the face recognition algorithm used, please
see <http://www.shervinemami.info/faceRecognition.html> .

## Installation



```
{#!wiki buildsystem rosbuild

This instalation process is for '''rosbuild''' (ROS Fuerte or earlier version)
Assuming that your rosbuild workspace (rosws) is under '''~/rosbuild_ws''', if not replace '''~/rosbuild_ws''' with appropriate location. It also assumes you're running Bash shell, if you're running Zsh, source appropriate '''setup.zsh''' file.

Execute:
{{{
$ cd ~/rosbuild_ws
$ rosws set face_recognition --git git://github.com/procrob/procrob_functional.git
$ rosws update
```

 In new terminal 

```
$ rosmake face_recognition
```



## How the face recognition works:

Training images are stored in the **data** directory.\
Training images are listed in the **train.text** file.\
The **train.txt** follows a specific format which is best understood by
looking at the example **train.txt** file provided in the package. Note
that person numbers start from 1, and spaces or special characters are
not allowed in persons' names).\
The program trains from the training examples listed in the
**train.txt** and create an Eigenfaces database which is stored in the
**facedata.xml** file.\
Face detection is performed using a haarcascade classifier
(haarcascade_frontalface_alt.xml).\
The **data** folder, and **train.txt**, **facedata.xml** and
**haarcascade_frontalface_alt.xml** files should be placed in the
program's working directory (i.e. the directory from which you execute
the program).\

When the face_recognition program starts:\
If **facedata.xml** exists, the Eigenfaces database is loaded from
**facedata.xml**.\
If **facedata.xml** does not exist, the program tries to train and
create Eigenfaces database from the training images listed in
**train.txt**, if any.\
Regardless of if the Eigenfaces database is loaded/created at start up
or not, you can always add training images directly from the video
stream and then update the Eigenfaces database by (re)training.\
Note: when the program (re)trains, the content of **facedata.xml** is
disregarded and the program trains only based on the training images
listed in **train.txt**.

## Fserver

Fserver is a ROS node that provides a simple actionlib server interface
for performing different face recognition functionalities in video
stream.

To start the Fserver node 

```
$ roscd face_recognition
$ rosrun face_recognition Fserver
```



### FaceRecognitionGoal message

This message includes 2 fields:

-   *int* **order_id**
-   *string* **order_argument**

The FaceRecognitionGoal message has 2 fields: an **order_id** which is
an integer specifying a goal and an **order_argument** which is a string
used to specify an argument for the goal if necessary. The face
recognition actionlib server (i.e. **Fserver**) accepts 5 different
goals:

-   **order_id** = 0 recognise_once: Goal is to acknowledge the first
    face recognized in the video stream. When the first face is
    recognized with a confidence value higher than the desirable
    confidence value threshold, the name of the recognized person and
    its confidence value are sent back to the client as result.
-   **order_id** = 1 recognise_continuous: Goal is to continuously
    recognise faces in the video stream. For every face recognized with
    a confidence value higher than the desirable confidence value
    threshold, the name of the recognized person and its confidence
    value are sent back to the client as feedback. This goal is
    persuaded for infinite time until it is cancelled or preempted by
    another goal.
-   **order_id** = 2 and **order_argument** = 'person_name'
    add_face_images: Goal is to acquire training images for a NEW
    person. The video stream is processed for detecting a face which is
    saved and used as a training image for the new person. This process
    is continued until the desired number of training images for the new
    person is acquired. The name of the new person is provided as
    **order_argument**. The acquired images are stored in the 'data'
    folder and are added to the list of training images in **train.txt**
-   **order_id** = 3 train: Goal is to (re)train the Eigenfaces database
    from the training images listed in the 'train.txt'.
-   **order_id** = 4 exit: Goal is to exit the program.

### Subscribed Topic:

-   **/camera/image_raw** (standard ROS image transport) A video stream

### Parameters:

-   **confidence_value** (*double*, default = 0.88) A face recognized
    with confidence value higher than the "confidence_value" threshold
    is accepted as valid.

```{=html}
<!-- -->
```
-   **show_screen_flag** (*boolean*, default = true) If output screen is
    shown.

```{=html}
<!-- -->
```
-   **add_face_number** (*int*, default = 25) A parameter for the
    'add_face_images' goal (order_id = 2) which determines the number
    of training images for a new person to be acquired from the video
    stream

## Fclient

**Fclient** is a ROS node that implements an actionlib client example
for the face_recognition simple actionlib server (i.e. 'Fserver').
'Fclient' is provided for demonstration and testing purposes.

### Subscribed topics

-   **fr_order** (face_recognition/FRClientGoal) Each **FRClientGoal**
    message has an **order_id** and an **order_argument** which specify
    a goal to be executed by the **Fserver**. After receiving a message,
    **Fclient** sends the corresponding goal to the **Fserver**. By
    registering relevant call back functions, **Fclient** receives
    feedback and result information from the execution of goals in the
    **Fserver** and prints such information on its terminal.

## Tutorial

(You have to install gscam to do this tutorial) An exercise of using
Fserver and Fclient:\

-   Run roscore 

```
$ roscore
```


-   In a separate terminal publish a video stream on topic
    **/camera/image_raw**. If you have the gscam package installed and
    configured, you can use it to publish images from your web cam as
    follows: 

```
$ roscd gscam/bin
$ rosrun gscam gscam /gscam/image_raw:=/camera/image_raw
```


-   In separate terminals run the face recognition server and client as
    follows: 

```
$ rosrun face_recognition Fserver
$ rosrun face_recognition Fclient
```


-   In another terminal publish following messages on topic /fr_order to
    test different face recognition functionalities.
-   After each command notice the output of Fserver and Fclient.
    

```
$ rostopic pub -1 /fr_order face_recognition/FRClientGoal -- 2 "your_name"
```


-   To acquire training images for your face: you should try to appear
    in the video stream! 

```
$ rostopic pub -1 /fr_order face_recognition/FRClientGoal -- 3 "none"
```


-   To retrain and update the database, so that you can be recognized
    

```
$ rostopic pub -1 /fr_order face_recognition/FRClientGoal -- 1 "none"
```


-   To recognise faces continuously. This would not stop until you
    preempt or cancel the goal. So lets preempt it by sending the next
    goal. 

```
$ rostopic pub -1 /fr_order face_recognition/FRClientGoal -- 2 "your_friend's_name"
```


-   To add training images for a new person 

```
$ rosmake face_recognition
```

0
-   To recognize once a face. 

```
$ rosmake face_recognition
```

1
-   To recognize continuously 

```
$ rosmake face_recognition
```

2
-   To exit }}}}



```
$ rosmake face_recognition
```

3

## How the face recognition works:

Training images are stored in the **data** directory.\
Training images are listed in the **train.text** file.\
The 'train.txt' follows a specific format which is best understood by
looking at the example **train.txt** file provided in the package. Note
that person numbers start from 1, and spaces or special characters are
not allowed in persons' names).\
The program trains from the training examples listed in the
**train.txt** and create an Eigenfaces database which is stored in the
**facedata.xml** file.\
Face detection is performed using a haarcascade classifier
(haarcascade_frontalface_alt.xml).\
The **data** folder, and **train.txt**, **facedata.xml** and
**haarcascade_frontalface_alt.xml** files should be placed in the
program's working directory (i.e. the directory from which you execute
the program).\

When the face_recognition program starts:\
If **facedata.xml** exists, the Eigenfaces database is loaded from
**facedata.xml**.\
If **facedata.xml** does not exist, the program tries to train and
create Eigenfaces database from the training images listed in
**train.txt**, if any.\
Regardless of if the Eigenfaces database is loaded/created at start up
or not, you can always add training images directly from the video
stream and then update the Eigenfaces database by (re)training.\
Note: when the program (re)trains, the content of **facedata.xml** is
disregarded and the program trains only based on the training images
listed in **train.txt**.

## Fserver

Fserver is a ROS node that provides a simple actionlib server interface
for performing different face recognition functionalities in video
stream.

To start the Fserver node 

```
$ rosmake face_recognition
```

4

### FaceRecognitionGoal message

This message includes 2 fields:

-   *int* **order_id**
-   *string* **order_argument**

The FaceRecognitionGoal message has 2 fields: an **order_id** which is
an integer specifying a goal and an **order_argument** which is a string
used to specify an argument for the goal if necessary. The face
recognition actionlib server (i.e. **Fserver**) accepts 5 different
goals:

-   **order_id** = 0 recognise_once: Goal is to acknowledge the first
    face recognized in the video stream. When the first face is
    recognized with a confidence value higher than the desirable
    confidence value threshold, the name of the recognized person and
    its confidence value are sent back to the client as result.
-   **order_id** = 1 recognise_continuous: Goal is to continuously
    recognise faces in the video stream. For every face recognized with
    a confidence value higher than the desirable confidence value
    threshold, the name of the recognized person and its confidence
    value are sent back to the client as feedback. This goal is
    persuaded for infinite time until it is cancelled or preempted by
    another goal.
-   **order_id** = 2 and **order_argument** = 'person_name'
    add_face_images: Goal is to acquire training images for a NEW
    person. The video stream is processed for detecting a face which is
    saved and used as a training image for the new person. This process
    is continued until the desired number of training images for the new
    person is acquired. The name of the new person is provided as
    **order_argument**. The acquired images are stored in the 'data'
    folder and are added to the list of training images in **train.txt**
-   **order_id** = 3 train: Goal is to (re)train the Eigenfaces database
    from the training images listed in the 'train.txt'.
-   **order_id** = 4 exit: Goal is to exit the program.

### Subscribed Topic:

-   **/camera/image_raw** (standard ROS image transport) A video stream

### Parameters:

-   **confidence_value** (*double*, default = 0.88) A face recognized
    with confidence value higher than the "confidence_value" threshold
    is accepted as valid.

```{=html}
<!-- -->
```
-   **show_screen_flag** (*boolean*, default = true) If output screen is
    shown.

```{=html}
<!-- -->
```
-   **add_face_number** (*int*, default = 25) A parameter for the
    'add_face_images' goal (order_id = 2) which determines the number
    of training images for a new person to be acquired from the video
    stream

## Fclient

**Fclient** is a ROS node that implements an actionlib client example
for the face_recognition simple actionlib server (i.e. 'Fserver').
'Fclient' is provided for demonstration and testing purposes.

### Subscribed topics

-   **fr_order** (face_recognition/FRClientGoal) Each **FRClientGoal**
    message has an **order_id** and an **order_argument** which specify
    a goal to be executed by the **Fserver**. After receiving a message,
    **Fclient** sends the corresponding goal to the **Fserver**. By
    registering relevant call back functions, **Fclient** receives
    feedback and result information from the execution of goals in the
    **Fserver** and prints such information on its terminal.

## Tutorial

An exercise of using Fserver and Fclient:\

-   Run roscore 

```
$ rosmake face_recognition
```

5
-   In separate terminal publish a video stream on topic
    **/camera/image_raw**.
-   For example you can use **usb_cam** to publish images from your web
    cam as follows:
-   Install [http://wiki.ros.org/usb_cam](usb_cam) package
-   Run 

```
$ rosmake face_recognition
```

6
-   In separate terminals run the face recognition server and client as
    follows: 

```
$ rosmake face_recognition
```

7
-   In another terminal publish following messages on topic /fr_order to
    test different face recognition functionalities.
-   After each command notice the output of Fserver and Fclient.
    

```
$ rosmake face_recognition
```

8
-   To acquire training images for your face: you should try to appear
    in the video stream! 

```
$ rosmake face_recognition
```

9
-   To retrain and update the database, so that you can be recognized
    

```
$ roscd face_recognition
$ rosrun face_recognition Fserver
```

0
-   To recognise faces continuously. This would not stop until you
    preempt or cancel the goal. So lets preempt it by sending the next
    goal. 

```
$ roscd face_recognition
$ rosrun face_recognition Fserver
```

1
-   To add training images for a new person 

```
$ roscd face_recognition
$ rosrun face_recognition Fserver
```

2
-   To recognize once a face. 

```
$ roscd face_recognition
$ rosrun face_recognition Fserver
```

3
-   To recognize continuously 

```
$ roscd face_recognition
$ rosrun face_recognition Fserver
```

4
-   To exit }}}}
