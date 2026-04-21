## Elemental Description

System to create gesture recognition models by means of learning real
recorded gestures. Basic implementations to generate models based on
methods like DTW, HMM and GMM methods are provided. This work is
explained in more detail in the paper:

﻿Iñigo-Blasco, Pablo, F. Díaz-del-Río, D. Cagigas-Muñiz, T. Murillo, S.
Vicente-Díaz, J.L. Font-Calvo, and M.J. Domínguez-Morales. 2012.
"Validation of Dynamic Human Body Recognition Algorithms based on Robot
Programming by Demonstration methods using 3D cameras."

\[youtube:
<http://www.youtube.com/watch?feature=player_embedded&v=d1CBGEBkZ1w>\]

## Tutorial

### GETTING RAW DATA FROM KINECT

First create a raw kinect gesture bag file from the kinect sensor. See
<http://www.youtube.com/watch?feature=player_embedded&v=d1CBGEBkZ1w>

Here we show an example about how to do it: ```
$ roslaunch rtcus_kinect_gestures record_gesture.launch
 $ sleep 10;rosbag record /tf --duration=20 -o kinect_bag_file_raw_data.bag
```

Basically the first command set up the environment: rviz, kinect and
opennitrack (skeleton traking) to start the recording, the second
command records the skeleton state during the time (20 secs).

**RECOMENDED**

You should store the bag file into the
rtcus_kinect_gestures/data/bags/\<gesture_name_folder\>/\<bag_gesture_file.bag\>
then this bag file will be included in the system database and no futher
database configuration will be needed. ```
$ mkdir `rospack find rtcus_kinect_gestures`/data/bags/my_gesture_name
 $ mv kinect_bag_file_raw_data.bag `rospack find rtcus_kinect_gestures`/data/bags/my_gesture_name
```

### ALTERNATIVE: Using recorded gestures from existing dataset

In any case we have a dataset in this ftp: url. We encourage you that
begin with these tests. You can download with. Be patient, the size is
2GB: ```
$ wget ftp://anon:anon@conde.eii.us.es/gestures_bags.tar.gz
 $ zcat gestures_bags.tar.gz | tar xvf - -C `rospack find rtcus_kinect_gestures`/data/bags
``` Please warn us if this link is broken.

**OPTIONAL**

After having your raw kinect gesture bag file check if it has been
created properly. For this propose you can use a launch file designed in
our package: reproduce_gesture.launch For instance if we want to test
the file: \"come_here/come_here_2_2011-11-06-18-25-54.bag\" do this:
```
$ roslaunch rtcus_kinect_gestures reproduce_gesture.launch bag_file:=`rospack find rtcus_kinect_gestures`/data/bags/come_here/come_here_2_2011-11-06-18-25-54.bag use_bag:=True
```

### CREATING THE GESTURE LATENT-SPACE FILE

After this we have to generate \"the gestures latent-space files\" from
the raw kinect data of the wave and come_here gestures. They are stored
in the folders: rtcus_kinect_gestures/data/bags/wave and
rtcus_kinect_gestures/data/bags/come_here Notice that each of these
folders can have multiple bag files of the specific gestures: The most
files the better model will be generated. There is a last requirement we
have to accomplish. Specify the latent space configuration of the
come_here and wave gestures. They have to be stored in theirs bag
folders. A few of configurations files are provided with the package. In
any case here you have a example:

```
$ cat data/bags/wave/wave.config.yaml 
  > name: wave
  > frames: [ {target: /left_elbow_1, fixed: /left_shoulder_1, position: "", rotation: "p"}, {target: /left_shoulder_1, fixed: /neck_1, position: "", rotation: "rpy"}]
  > #time for each demonstration. A bag file can be much larger than this duration. Then the bag file will be splited in <bag time duration>/time_per_demonstration.
  > time_per_demonstration: 4.0
  > sampling_frequency: 50
  > # waiting time between demonstrations, in seconds
  > seconds_to_start_recording: 0
  > # stop the bag file listening between two demonstrations of duration time_per_demonstration
  > wait_seconds: 1
```

Once created (if not is already created) this file, we can reproduce the
bag file and create the \"gesture latent-space file\". This kind of
files will be stored in the folder:
rtcus_kinect_gestures/data/bags/\<gesture_name\>/). Here we show an
example to get the gesture come_here: the gesture file.

First we will create the wave gesture from the bags files stored in
rtcus_kinect_gestures/data/bags/come_here/ folder
```
$ roscore
 $ rosrun rtcus_kinect_gestures batch_gesture_entries_from_bags.py --gesture come_here --split True
```

The split parameter True says that the output will be two different
files: come_here_for_training.gesture.yaml and
come_here_for_evaluation.gesture.yaml. They both will be stored on
rtcus_kinect_gestures/data/gestures/ folder.

Now we will create the wave gesture from the bags files stored in
rtcus_kinect_gestures/data/bags/wave/ ```
$ rosrun rtcus_kinect_gestures batch_gesture_entries_from_bags.py --gesture wave 
 $ ls `rospack find rtcus_kinect_gestures`/data/gestures
  > -rw-rw-r-- 1 geus geus 212494 2011-12-2 13:01 come_here_for_evaluation.gesture.yaml
  > -rw-rw-r-- 1 geus geus 228079 2011-12-2 13:01 come_here_for_training.gesture.yaml
  > -rw-rw-r-- 1 geus geus 109744 2011-12-2 13:01 wave.gesture.yaml
```

Now we already have the gesture files stored in our database.

### CREATING THE GESTURE RECOGNIZERS (gestuer models)

To see more about this gestures you can plot them with:
```
$ rosrun rtcus_kinect_gestures batch_models_from_gesture_database.py --gesture wave_for_training --negative-gestures come_here_for_training
 $ rosrun rtcus_kinect_gestures batch_models_from_gesture_database.py --gesture come_here_for_training --negative-gestures wave_for_training
```

**ALTERNATIVE** Download built models: ```
$ wget http://rtc-us-ros-pkg.svn.sourceforge.net/viewvc/rtc-us-ros-pkg/datasets/gesture_recognition_datasets.zip?revision=261 -O gestures_bags.zip
 $ unzip gestures_bags.zip
```

### EVALUATION OVER OTHERS GESTURES AND GENERATING THE REPORT

```
$ rosrun rtcus_kinect_gestures batch_evaluate_gestures.py --gesture-entries come_here_for_evaluation,wave_for_evaluation --output evaluation_data
```

INTERNAL NOTE: A cache json file with the result will be stored in the
report folder (internal and time saving proposes). Then the report style
can be changed. Add the parameter \"-r True\" to rebuild and regenerate
the cache.

The resulting report will be stored in the
rtcus_kinect_gestures/report/report.html file ```
$ mkdir `rospack find rtcus_kinect_gestures`/data/bags/my_gesture_name
 $ mv kinect_bag_file_raw_data.bag `rospack find rtcus_kinect_gestures`/data/bags/my_gesture_name
```0

That is If you have any question ask us! :-)

### ANOTHER TUTORIAL EXAMPLE

Only one model ie: HMMGestureModel

```
$ mkdir `rospack find rtcus_kinect_gestures`/data/bags/my_gesture_name
 $ mv kinect_bag_file_raw_data.bag `rospack find rtcus_kinect_gestures`/data/bags/my_gesture_name
```1
