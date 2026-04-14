## Overview

This package provides capability to run the Text-To-Speech,
Speech-To-Text and Skill functionality of
[Mycroft AI](http://https://mycroft.ai/) as ROS nodes allowing any node
to be configured as a
[Mycroft Skill](http://https://https://mycroft.ai/documentation/mycroft-software-hardware/#mycroft-skills)

## Installation

Clone the repo into src ```
cd ~/catkin_ws/src
git clone https://github.com/injones/mycroft_ros.git
```

### Install dependencies

The dev_setup.sh can be used to install dependencies and configure the
package for use.

### Mycroft setup

Mycroft can be configured using either
\'\'\'\'\'/.mycroft/mycroft.conf\'\'\'\'\' or
\'\'\'\'\'/etc/mycroft/mycroft.conf\'\'\'\'\'

## Usage

Follow the steps below to run the package.

### Launching nodes

To launch all Mycroft nodes run the following ```
roslaunch mycroft_ros mycroft.launch
```

### Creating Mycroft Skills from ROS nodes

ROS nodes that are used as !MycroftSkill\'s should be placed within
their own directory under your packages \'\'\'scripts\'\'\' directory
with any relevent \'\'\'vocab\'\'\', \'\'\'dialog\'\'\' and
\'\'\'regex\'\'\' directories which should contain required intent and
entity files.

### Using the RosMycroftSkill

The \'\'\'mycroft_ros\'\'\' Python module provides helper functions and
classes for convenience such as the \'\'\'\'!RosMycroftSkill\'\'\'\'
class which can be used to register nodes as Mycroft Skills within the
Skill Manager of Mycroft.

#### Example skill

```python
class ExampleSkill(RosMycroftSkill):

    def __init__(self):
        super(ExampleSkill, self).__init__("/path/to/directory/")
        self.register_intent(IntentBuilder("MycroftRos").require("mycroft").require("ros"), self.example)
        self.register_intent_file("mytest.intent", self.mytest)
        if self.initialise():
            rospy.loginfo("MycroftSkill created")
        else:
            rospy.loginfo("Error creating MycroftSkill")

    def example(self, data):
        rospy.loginfo("MycroftRos callback")
        user_response = self.get_response(dialog="say something cool to me")
        rospy.loginfo("Response: " + user_response)

    def mytest(self, data):
        rospy.loginfo("mytest callback")
        rospy.loginfo("testentity: " + data.entities.get("testentity", ""))

if __name__ == "__main__":
    rospy.init_node('mycroft_skill_test')
    example = ExampleSkill()
    rospy.spin()
    rospy.on_shutdown(example.shutdown)
```

## catkin_virtualenv

This package makes use of the \'\'\'\'catkin_virtualenv\'\'\'\' ROS
package to run the \'\'mycroft_message_bus\'\', \'\'mycroft_tts\'\',
\'\'mycroft_stt\'\' and \'\'mycroft_skills\'\' nodes in a seperate
Python virtual environment.

## ROS Nodes

```clearsilver
node.0 {
  name = mycroft_message_bus
  desc = Creates the !MessageBus !WebSocket used for communication between Mycroft source code
}
node.1 {
  name = mycroft_tts
  desc = Manages the Text-To-Speech engine used by Mycroft
  sub {
    0.name = mycroft/speak
    0.type = std_msgs/String
    0.desc = String for Mycroft TTS to read
    1.name = mycroft/stop
    1.type = std_msgs/String
    1.desc = Signal to Mycroft to stop the TTS from speaking
  }
}
node.2 {
  name = mycroft_stt
  desc = Manages the Speech-To-Text engine used by Mycroft
  pub {
    0.name = mycroft/speech
    0.type = mycroft_ros/Speech
    0.desc = Publish list of Strings received from Mycroft STT engine
  }
}
node.3 {
  name = mycroft_skills
  desc = Configures and manages the Skill Manager
  sub {
    0.name = mycroft/utterance
    0.type = std_msgs/String
    0.desc = String to pass directly to the intent service of the Skill Manager
    1.name = mycroft/remove_skill
    1.type = std_msgs/String
    1.desc = Path of skill to remove from Skill Manager as a String
  }
  pub {
    0.name = mycroft/skill_id
    0.type = mycroft/IntentResponse
    0.desc = Returns intent name that was matched based on user speech, the user's utterance as a String, the entities belonging to the intent to the topic ''''mycroft/skill_id'''' where ''''skill_id'''' is the ID of the Mycroft Skill that the matched intent belongs to.
  }
  srv {
    0.name = mycroft/register_skill
    0.type = mycroft_ros/MycroftSkill
    0.desc = Creates and registers a new Mycroft Skill within the Skill Manager
  }
  result {
    0.name = get_response
    0.type =  mycroft/GetResponseResult
    0.desc = Returns user response as a String
    1.name = ask_yesno
    1.type = mycroft/GetResponseResult
    1.desc = Returns the String "yes" or "no" based on user response
  }
}
```
