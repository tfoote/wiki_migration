# Introduction

The speex_audio node allow to capture, stream, and play audio using ht
every efficient [Speex](http://www.speex.org/) audio codec. The node is
able to to capture audio from a microphone and publishes audio messages
on the speex_capture/ topic. Also, the node listens to speex_play/ topic
and outputs the audio messages to speakers.

# Download and first check

The `speex` module is available
[here](https://github.com/domesici/speex_audio). You can obtain the
source code using the git or downloading the compressed file.

## Use git

Use git recommended method is using the git control version system. If
you don't have git yet, using ubuntu you can install it as follow:
```
$ sudo apt-get install git-core
``` after that you can obtain the most up-to-date
of rt-wmp as follow: ```
$ git clone git://github.com/domesici/speex_audio.git
``` This, will create a ros
directory called `speex_audio`.

## Use .tar.gz or .zip file

To download the code compressed in tar.gz or zip file, you can follow
[this](https://github.com/domesici/speex_audio/archives/master) link.

Once decompressed, you can rename the directory as to `speex_audio`.

## Compiling the node

This directory should be moved to a path contained in the
`\$ROS_PACKAGE_PATH` environment variable or, alternatively, the path
where the directory is should be added to `\$ROS_PACKAGE_PATH` (see
[here](http://www.ros.org/wiki/ROS/EnvironmentVariables) for details).

It is necessary to configure package as follows:
```
$ cd speex_audio
    $ cmake .
```

After that we can try to compile the node. In the `speex_audio`
directory type: ```
$ rosmake
``` If all went ok you will read:
```
[ rosmake ] Results:
     [ rosmake ] Built 15 packages with 0 failures.
```

If the built ends succefully, 'bin' folder is created that will
contain the 'speex_node' binary file.

# First Test

Test that speex_audio node can work successfully with ALSA by capturing
audio from your microphone and playing it back through your speakers.

Before executing the following command, make sure your microphone is
enabled and selected as your default audio input device. Besides, you
could use headphones in order to avoid the annoying voice feedback.

```
$ rosrun speex_audio speex_node speex_capture:=speex_play
```

The above command should play audio from the microphone through the
speakers. If no audio is heard, make sure your system is setup to
capture audio from the proper source.

Once it is working, let's follow.

# Test on ros-rt-wmp network
