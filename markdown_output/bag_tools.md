## Installation

Install this package by first cloning and building the srv_tools
package, as described on the
[ROS wiki srv_tools](http://wiki.ros.org/srv_tools) page. Next, install
this package to make it available to rosrun.

```
catkin_make install --pkg bag_tools
```

## bag_tools

### extract_stereo_images

Extracts stereo images from a list of bagfiles to a folder. The images
extracted are rectified and syncronized. ```
rosrun bag_tools extract_stereo_images OUT_DIR FILETYPE STEREO_BASE_TOPIC BAGFILE [BAGFILE...]
```

### bag_add_time_offset.py

```
usage: bag_add_time_offset.py [-h] -o OUTPUT_BAGFILE -i INPUT_BAGFILE
                              [INPUT_BAGFILE ...] -of OFFSET -t TOPIC
                              [TOPIC ...]

Shift the publishing time of given topics in input bagfile.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_BAGFILE     output bagfile
  -i INPUT_BAGFILE [INPUT_BAGFILE ...]
                        input bagfile(s)
  -of OFFSET            time offset to add in seconds
  -t TOPIC [TOPIC ...]  topic(s) to change
```

### change_camera_info.py

```
usage: change_camera_info.py [-h] inbag outbag replacement [replacement ...]

Change camera info messages in a bagfile.

positional arguments:
  inbag        input bagfile
  outbag       output bagfile
  replacement  replacement in form "TOPIC=CAMERA_INFO_FILE", e.g.
               /stereo/left/camera_info=my_new_info.yaml

optional arguments:
  -h, --help   show this help message and exit
```

### check_delay.py

```
usage: check_delay.py [-h] inbag [inbag ...]

Checks the delay in a bagfile between publishing (recording) time and the time
stamp in the header (if exists). Prints out min, max and mean delays.

positional arguments:
  inbag       input bagfile(s)

optional arguments:
  -h, --help  show this help message and exit
```

### cut.py

```
usage: cut.py [-h] --inbag INBAG [INBAG ...] --outbag OUTBAG --start START
              --duration DURATION

Cuts out a section from an input bagfile and writes it to an output bagfile

optional arguments:
  -h, --help            show this help message and exit
  --inbag INBAG [INBAG ...]
                        input bagfile(s)
  --outbag OUTBAG       output bagfile
  --start START         start time
  --duration DURATION   duration of the resulting part
```

### replace_msg_time_with_hdr.py

```
usage: replace_msg_time_with_hdr.py [-h] -o OUTPUT_BAGFILE -i INPUT_BAGFILE

Create a new bagfile from an existing one replacing the message time for the
header time.

optional arguments:
  -h, --help         show this help message and exit
  -o OUTPUT_BAGFILE  output bagfile
  -i INPUT_BAGFILE   input bagfile
```

### add_header_time_offset.py

```
usage: add_header_time_offset.py [-h] -o OFFSET -i BAGFILE [BAGFILE ...] -t
                                 TOPIC [TOPIC ...]

Changes header timestamps using given offset, can change /tf as well.

optional arguments:
  -h, --help            show this help message and exit
  -o OFFSET             time offset to add in seconds
  -i BAGFILE [BAGFILE ...]
                        input bagfile(s)
  -t TOPIC [TOPIC ...]  topics to change
```

### camera_info_parser.py

Parses camera info yaml files and returns the content as
sensor_msgs.msg.CameraInfo.

### change_frame_id.py

```
usage: change_frame_id.py [-h] -o OUTPUT_BAGFILE -i INPUT_BAGFILE -f FRAME_ID
                          -t TOPIC [TOPIC ...]

reate a new bagfile from an existing one replacing the frame id of requested
topics.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_BAGFILE     output bagfile
  -i INPUT_BAGFILE      input bagfile
  -f FRAME_ID           desired frame_id name in the topics
  -t TOPIC [TOPIC ...]  topic(s) to change
```

### image_sequence_publisher.py

Publishes a folder full of images as if it was a normal camera topic and
it\'s related camera info topic.

#### Example Launch File

```
<launch>
  <node name="img_pub" pkg="bag_tools" type="image_sequence_publisher.py" output="screen">
    <param name="image_dir" value="/tmp/seq"/>
    <param name="file_pattern" value="*.png"/>
    <param name="camera_info_file" value="/tmp/seq/camera_info.yaml"/>
    <param name="frequency" value="10"/>
  </node>
</launch>
```

### make_video.py

```
rosrun bag_tools extract_stereo_images OUT_DIR FILETYPE STEREO_BASE_TOPIC BAGFILE [BAGFILE...]
```0
