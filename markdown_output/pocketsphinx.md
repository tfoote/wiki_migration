## Overview

This package provides access to the
[CMU Pocket Sphinx](http://cmusphinx.sourceforge.net/) speech
recognizer. It uses gstreamer to automatically split the incoming audio
into utterances to be recognized, and offers services to start and stop
recognition.

Currently, the recognizer *requires* a language model and dictionary
file. These can be automatically built from a corpus of sentances using
the
[Online Sphinx Knowledge Base Tool](http://www.speech.cs.cmu.edu/tools/lmtool.html).
Example launch files, language models, and dictionary files can be found
in the *demo* directory of the package. The *voice_cmd* example controls
a mobile base using commands such as "*move forward*" or "*stop*".
The *robocup* example uses some of the standard items and names from the
RoboCup@Home contest, for instance, it should recognize "*hello, my
name is Michael*" or "*Bring me the Original Pringles*".

## Installing

### Ubuntu Users

{ }}}}

{ }}}}

{ }}}}

{ }}}}

### Non-Ubuntu Users

There is nothing to build, however, to install pocketsphinx itself we
will need to run rosdep. In a directory under your ROS package path, do
the following: 

```
git clone https://github.com/mikeferguson/pocketsphinx
sudo apt-get install gstreamer0.10-pocketsphinx
```



## Nodes



```clearsilver
name=recognizer.py
desc=Interface to pocket sphinx.
pub {
  0.name=~output
  0.type = std_msgs/String
  0.desc = Complete utterance as heard by pocket sphinx.
}
srv {
  1.name = ~start
  1.type = std_srvs/Empty
  1.desc = Connect the audio stream to the speech recognizer and start listening.
  2.name = ~stop
  2.type = std_srvs/Empty
  2.desc = Disconnect audio stream from speech recognizer.
}
param {
  0.name = ~lm
  0.type = str
  0.desc = Location of language model file.
  0.default = required
  1.name = ~dict
  1.type = str
  1.desc = Location of dictionary file.
  1.default = required
}
```


