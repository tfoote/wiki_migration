# Overview

**stdr_parser** is a Yaml/XML parser created for
[STDR Simulator](stdr_simulator). Its job is to parse resource files
(robots and sensors) and create the according stdr_msgs. Also, provided
a stdr_msgs message **stdr_parser** can save it to a Yaml or XML file.
The parser structure is such that it can be "easily" extended with
more file types (such as JSON f.e.) by changing only specific source
files (the filetype parser and writer). A brief overview of the parsing
steps follow.

## How the stdr_parser works

### Step 1 : Recursive file parsing

**stdr_parser** takes as input a Yaml or XML file and initially does a
"blind" parsing of the file, meaning that no validation is performed.
Of course if the file does not exist or is malformed, a
`ParserException` is thrown. This initial parsing creates a tree
consisting of stdr_parser::Node objects and represents the initial file.
As the following sections describe, for convenience reasons you can have
**filename** tags in your robot or sensor file, which are used for
including other resources (for example in a robot you can include laser
and sonar sensors without writing them from the scratch). During the
parsing the specific filenames are parsed also recursively.

When a **filename** tag is found, during the parsing step, a
stdr_parser::Node is created tagged as *filename*. For example a robot
XML resource follows: ```
<robot>
  <robot_specifications>
    <footprint>
      <radius>0.3</radius>
    </footprint>
    <laser>
      <filename>hokuyo.xml</filename>
      <laser_specifications>
        <pose>
          <theta>1.57</theta>
        </pose>
      </laser_specifications>
    </laser>
  </robot_specifications>
<robot>
``` where `hokuyo.xml` ,may
contain the following (not fully functional, just to showcase):
```
<laser>
  <laser_specifications>
    <max_range>4</max_range>
    <pose>
      <x>0</x>
      <y>0</y>
      <theta>0</theta>
    </pose>
    <noise>
      <filename>gauss_small.xml</filename>
    </noise>
  </laser_specifications>
</laser>
``` and the **gauss_small.xml**
```
<noise>
  <noise_specifications>
    <noise_mean>0</noise_mean>
    <noise_std>0.03</noise_std>
  </noise_specifications>
</noise>
```

In addition, every `stdr_parser::Node` contains a level value that is
increased when the recurrent file depth increases. After the first step,
the tree will look like that (the levels in \[ \]):
```
├ robot [0]
│ ├ robot_specifications [0]
│ │ ├ footprint [0]
│ │ │ ├ radius [0]
│ │ │ │ ├ 0.3 [0]
│ │ ├ laser [0]
│ │ │ ├  filename [0]
│ │ │ │ ├ laser [1]
│ │ │ │ │ ├ laser_specifications [1]
│ │ │ │ │ │ ├ max_range [1]
│ │ │ │ │ │ │ ├ 4 [1]
│ │ │ │ │ │ ├ pose [1]
│ │ │ │ │ │ │ ├ x [1]
│ │ │ │ │ │ │ │ ├ 0 [1]
│ │ │ │ │ │ │ ├ y [1]
│ │ │ │ │ │ │ │ ├ 0 [1]
│ │ │ │ │ │ │ ├ theta [1]
│ │ │ │ │ │ │ │ ├ 0 [1]
│ │ │ │ │ │ ├ noise [1]
│ │ │ │ │ │ │ ├ filename [1]
│ │ │ │ │ │ │ │ ├ noise [2]
│ │ │ │ │ │ │ │ │ ├ noise_specifications [2]
│ │ │ │ │ │ │ │ │ │ ├ noise_mean [2]
│ │ │ │ │ │ │ │ │ │ │ ├ 0 [2]
│ │ │ │ │ │ │ │ │ │ ├ noise_std [2]
│ │ │ │ │ │ │ │ │ │ │ ├ 0.03 [2]
│ │ │ ├ laser_specifications [0]
│ │ │ │ ├ pose [0]
│ │ │ │ │ ├ theta [0]
│ │ │ │ │ │ ├ 1.57 [0]
```

### Step 2 : 'filename' tag elimination

The second step is to eliminate the `filename` tags from the tree. To do
so a sanity check is performed: the parent node and the child node of a
`filename` node must be the same. If the above holds, the `filename`
node is eliminated, as well as its child and the child's children are
connected to `filename`'s parent. The result follows:
```
├ robot [0]
│ ├ robot_specifications [0]
│ │ ├ footprint [0]
│ │ │ ├ radius [0]
│ │ │ │ ├ 0.3 [0]
│ │ ├ laser [0]
│ │ │ ├ laser_specifications [1]
│ │ │ │ ├ max_range [1]
│ │ │ │ │ ├ 4 [1]
│ │ │ │ ├ pose [1]
│ │ │ │ │ ├ x [1]
│ │ │ │ │ │ ├ 0 [1]
│ │ │ │ │ ├ y [1]
│ │ │ │ │ │ ├ 0 [1]
│ │ │ │ │ ├ theta [1]
│ │ │ │ │ │ ├ 0 [1]
│ │ │ │ ├ noise [1]
│ │ │ │ │ ├ noise_specifications [2]
│ │ │ │ │ │ ├ noise_mean [2]
│ │ │ │ │ │ │ ├ 0 [2]
│ │ │ │ │ │ ├ noise_std [2]
│ │ │ │ │ │ │ ├ 0.03 [2]
│ │ │ ├ laser_specifications [0]
│ │ │ │ ├ pose [0]
│ │ │ │ │ ├ theta [0]
│ │ │ │ │ │ ├ 1.57 [0]
```

### Step 3 : Node merging

The third step is the recursive node merging. In this step the
**stdr_multiple_allowed.xml** file under
`stdr_resources/resources/specifications` is of crucial importance.
There, the tags that can have multiple occurrences under a specific tag
are placed. The current implementation allows multiple occurrences in
these tags:

-   robot
-   laser
-   sonar All the other tags are recursively merged, if multiple
    occurrences exist under any other tag. The tree after this step
    follows: ```
├ robot [0]
│ ├ robot_specifications [0]
│ │ ├ footprint [0]
│ │ │ ├ radius [0]
│ │ │ │ ├ 0.3 [0]
│ │ ├ laser [0]
│ │ │ ├ laser_specifications [1]
│ │ │ │ ├ max_range [1]
│ │ │ │ │ ├ 4 [1]
│ │ │ │ ├ pose [1]
│ │ │ │ │ ├ x [1]
│ │ │ │ │ │ ├ 0 [1]
│ │ │ │ │ ├ y [1]
│ │ │ │ │ │ ├ 0 [1]
│ │ │ │ │ ├ theta [1]
│ │ │ │ │ │ ├ 0 [1]
│ │ │ │ │ │ ├ 1.57 [0]
│ │ │ │ ├ noise [1]
│ │ │ │ │ ├ noise_specifications [2]
│ │ │ │ │ │ ├ noise_mean [2]
│ │ │ │ │ │ │ ├ 0 [2]
│ │ │ │ │ │ ├ noise_std [2]
│ │ │ │ │ │ │ ├ 0.03 [2]
```

### Step 4 : Value merging

In this step we have supposedly merged all the possible tags and we are
prepared to merge the value nodes. Here the level value plays its role,
as during the value merging, the values with higher level are overridden
by those with lower level. This helps to easily write resource files by
changing only some aspects of the included files (in the specific
example the robot has a laser but the scientist wants to change the
laser's orientation). The final tree follows: ```
├ robot [0]
│ ├ robot_specifications [0]
│ │ ├ footprint [0]
│ │ │ ├ radius [0]
│ │ │ │ ├ 0.3 [0]
│ │ ├ laser [0]
│ │ │ ├ laser_specifications [1]
│ │ │ │ ├ max_range [1]
│ │ │ │ │ ├ 4 [1]
│ │ │ │ ├ pose [1]
│ │ │ │ │ ├ x [1]
│ │ │ │ │ │ ├ 0 [1]
│ │ │ │ │ ├ y [1]
│ │ │ │ │ │ ├ 0 [1]
│ │ │ │ │ ├ theta [1]
│ │ │ │ │ │ ├ 1.57 [0]
│ │ │ │ ├ noise [1]
│ │ │ │ │ ├ noise_specifications [2]
│ │ │ │ │ │ ├ noise_mean [2]
│ │ │ │ │ │ │ ├ 0 [2]
│ │ │ │ │ │ ├ noise_std [2]
│ │ │ │ │ │ │ ├ 0.03 [2]
```

### Step 5 : Validation

This is the final parsing step where the validation is performed.
Crucial role plays the **stdr_specifications.xml** file under
`stdr_resources/resources/specifications`. There for every valid tag,
the allowed and required children are specified. (Look at the end of the
page for the file's contents). The validation step reads this file and
performs **allowed** and **required** checks for all tree nodes.

### Message creation  / saving messages to files

After the tree is fully created, **stdr_parser** can create the
according **stdr_msgs**. This is performed seamlessly by using
templates. An example of creating a **stdr_msgs::RobotMsg** follows:
```
stdr_msgs::RobotMsg msg = stdr_parser::Parser::createMessage<stdr_msgs::RobotMsg>("simple_robot.yaml");
```

In a similar way a **stdr_msgs** message can be saved to a Yaml or XML
file: ```
stdr_msgs::RobotMsg msg = stdr_parser::Parser::createMessage<stdr_msgs::RobotMsg>("simple_robot.yaml");
stdr_parser::Parser::saveMessage(msg,"test.xml");
```

### Exceptions

If anything goes wrong an `ParserException` is thrown. The way to use it
in a source code file follows: ```
try
  {
    stdr_parser::Parser::saveMessage(
      stdr_parser::Parser::createMessage
      <stdr_msgs::RobotMsg>      //!< Type
      ("pandora_robot.yaml"),    //!< Input file
      "test.xml"            //!< Output file
    );
  }
  catch(ParserException ex)
  {
    ROS_ERROR(" === STDR PARSER ERROR ===\n%s",ex.what());
  }
```

The `ParserException` exceptions hold a trail of the error for better
debugging. Example: ```
<laser>
  <laser_specifications>
    <max_range>4</max_range>
    <pose>
      <x>0</x>
      <y>0</y>
      <theta>0</theta>
    </pose>
    <noise>
      <filename>gauss_small.xml</filename>
    </noise>
  </laser_specifications>
</laser>
```0

## Using YAML files

In this section typical (and fully functional) YAML file examples for
the five basic message types will be provided.

### Noise

```
<laser>
  <laser_specifications>
    <max_range>4</max_range>
    <pose>
      <x>0</x>
      <y>0</y>
      <theta>0</theta>
    </pose>
    <noise>
      <filename>gauss_small.xml</filename>
    </noise>
  </laser_specifications>
</laser>
```1

### Footprint

```
<laser>
  <laser_specifications>
    <max_range>4</max_range>
    <pose>
      <x>0</x>
      <y>0</y>
      <theta>0</theta>
    </pose>
    <noise>
      <filename>gauss_small.xml</filename>
    </noise>
  </laser_specifications>
</laser>
```2

### Laser

```
<laser>
  <laser_specifications>
    <max_range>4</max_range>
    <pose>
      <x>0</x>
      <y>0</y>
      <theta>0</theta>
    </pose>
    <noise>
      <filename>gauss_small.xml</filename>
    </noise>
  </laser_specifications>
</laser>
```3

### Sonar

```
<laser>
  <laser_specifications>
    <max_range>4</max_range>
    <pose>
      <x>0</x>
      <y>0</y>
      <theta>0</theta>
    </pose>
    <noise>
      <filename>gauss_small.xml</filename>
    </noise>
  </laser_specifications>
</laser>
```4

### Robot

```
<laser>
  <laser_specifications>
    <max_range>4</max_range>
    <pose>
      <x>0</x>
      <y>0</y>
      <theta>0</theta>
    </pose>
    <noise>
      <filename>gauss_small.xml</filename>
    </noise>
  </laser_specifications>
</laser>
```5

## Using XML files

In this section typical (and fully functional) XML file examples for the
five basic message types will be provided.

### Noise

```
<laser>
  <laser_specifications>
    <max_range>4</max_range>
    <pose>
      <x>0</x>
      <y>0</y>
      <theta>0</theta>
    </pose>
    <noise>
      <filename>gauss_small.xml</filename>
    </noise>
  </laser_specifications>
</laser>
```6

### Footprint

```
<laser>
  <laser_specifications>
    <max_range>4</max_range>
    <pose>
      <x>0</x>
      <y>0</y>
      <theta>0</theta>
    </pose>
    <noise>
      <filename>gauss_small.xml</filename>
    </noise>
  </laser_specifications>
</laser>
```7

### Laser

```
<laser>
  <laser_specifications>
    <max_range>4</max_range>
    <pose>
      <x>0</x>
      <y>0</y>
      <theta>0</theta>
    </pose>
    <noise>
      <filename>gauss_small.xml</filename>
    </noise>
  </laser_specifications>
</laser>
```8

### Sonar

```
<laser>
  <laser_specifications>
    <max_range>4</max_range>
    <pose>
      <x>0</x>
      <y>0</y>
      <theta>0</theta>
    </pose>
    <noise>
      <filename>gauss_small.xml</filename>
    </noise>
  </laser_specifications>
</laser>
```9

### Robot

```
<noise>
  <noise_specifications>
    <noise_mean>0</noise_mean>
    <noise_std>0.03</noise_std>
  </noise_specifications>
</noise>
```0

## stdr_specifications.xml

The contents of the `stdr_specifications.xml` file follow (not all tags
are functional in the current **STDR Simulator** version):

### environment

-   allowed
-   map,robot,rfid_tag
-   required
-   map

### map

-   allowed
-   filename,map_specifications
-   required
-   map_specifications

### map_specifications

-   allowed
-   image,resolution,origin,free_thresh,negate,occupied_thresh
-   required
-   image,resolution

### origin

-   allowed
-   x,y,theta
-   required
-   \-

### robot

-   allowed
-   filename,robot_specifications
-   required
-   robot_specifications

### robot_specifications

-   allowed
-   initial_pose,footprint,laser,sonar,rfid,kinematic
-   required
-   \-

### initial_pose

-   allowed
-   x,y,theta
-   required
-   \-

### pose

-   allowed
-   x,y,theta
-   required
-   \-

### footprint

-   allowed
-   filename,footprint_specifications
-   required
-   footprint_specifications

### footprint_specifications

-   allowed
-   radius,points
-   required
-   \-

### points

-   allowed
-   point
-   required
-   \-

### point

-   allowed
-   x,y
-   required
-   x,y

### laser

-   allowed
-   filename,laser_specifications
-   required
-   laser_specifications

### laser_specifications

-   allowed
-   max_angle,min_angle,max_range,min_range,num_rays,frequency,frame_id,pose,noise
-   required
-   \-

### noise

-   allowed
-   filename,noise_specifications
-   required
-   noise_specifications

### noise_specifications

-   allowed
-   noise_mean,noise_std
-   required
-   \-

### sonar

-   allowed
-   filename,sonar_specifications
-   required
-   sonar_specifications

### sonar_specifications

-   allowed
-   cone_angle,max_range,min_range,frequency,frame_id,pose,noise
-   required
-   \-

### rfid

-   allowed
-   filename,rfid_specifications
-   required
-   rfid_specifications

### rfid_specifications

-   allowed
-   angle_span,signal_cutoff,max_range,frequency,frame_id,pose
-   required
-   \-

### kinematic

-   allowed
-   filename,kinematic_specifications
-   required
-   kinematic_specifications

### kinematic_specifications

-   allowed
-   type
-   required
-   type

### rfid_tag

-   allowed
-   x,y,message
-   required
-   x,y

### x

-   default
-   0

### y

-   default
-   0

### theta

-   default
-   0

### max_angle

-   default
-   1.57

### min_angle

-   default
-   -1.57

### max_range

-   default
-   4

### min_range

-   default
-   0

### num_rays

-   default
-   180

### frequency

-   default
-   10

### frame_id

### frequency

-   default
-   0

### noise_std

-   default
-   0

### noise_std

-   default
-   0.3

### cone_angle

-   default
-   1.0
