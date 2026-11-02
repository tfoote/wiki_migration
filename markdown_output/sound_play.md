## General Philosophy

The `sound_play` node considers each sound (built-in, wave file or
synthesized text) as an entity that can be playing, playing repeatedly
or stopped. Nodes change the state of a sound by publishing to the
`robotsound` topic. Multiple sounds can be played at once.

## Supported Hardware

This node has been tested on the Logitech USB speakers on the PR2 and on
some built-in Intel sound-cards, but should support any sound card that
is supported by SDL. Because it accesses SDL via pygame, it has no
control over which sound device is used. You will have to configure SDL
and ALSA/OSS to default to the sound device you want to use.

## API Stability

- The C++ and Python APIs are stable.

<!-- -->

- The ROS API and in particular the message format should not be relied
  on and may change at any time to support extended functionality.

### Known Limitations

Please let us know if these limitations actually bother you.

- Two nodes independently using the same sound may have strange
  interactions. For example one node may stop a sound that was started
  by the other one.

<!-- -->

- There is no way to tell when a sound stops playing.

<!-- -->

- When a sound is played multiple times, at most two copies of that
  sound will accumulate in the queue at once.

## C++/Python API

C++ and Python bindings are provided. It should be unnecessary to
directly generate messages when playing sounds from C++ or Python.
Documentation of the language bindings are in
[doxygen](http://docs.ros.org/latest-available/api/sound_play/html/index.html).

## Command-line utilities

The following utilities can be used to play sound when
`soundplay_node.py` is running. For help on getting
`soundplay_node.py` running refer to the
[tutorial](#how-to-configure-and-use-speakers-with-sound_play).

### Playing a .WAV or .OGG file

The `play.py` script can play any `.WAV` or `.OGG` file. The file
must be available on the computer on which `soundplay_node.py` is
running, and an absolute path should be given.



```
$ rosrun sound_play play.py --help
Usage: /u/blaise/ros/ros-pkg/stacks/sound_drivers/sound_play/scripts/play.py sound_to_play.(ogg|wav)

Plays an .OGG or .WAV file. The path to the file should be absolute, and be valid on the computer on which sound_play is running.
```



For example (soundplay_node.py should be running first):


```
$rosrun sound_play play.py /usr/share/xemacs21/xemacs-packages/etc/sounds/im_so_happy.wav
Playing "/usr/share/xemacs21/xemacs-packages/etc/sounds/im_so_happy.wav".
```



### Playing a built in sound

Some standard sounds are built-into the driver, and can be played only
by specifying their integer identifier using `playbuiltin.py`.


```
$ rosrun sound_play playbuiltin.py 
Usage: /u/blaise/ros/ros-pkg/stacks/sound_drivers/sound_play/scripts/playbuiltin.py <sound_id>

Plays one of the built-in sounds based on its integer ID. Look at the <<MsgLink(sound_play/SoundRequest)>> message definition for IDs.
```



For example (`soundplay_node.py` should be running first):


```
$ rosrun sound_play playbuiltin.py 2
Playing sound 2".
```



To get an up-to-date list of the built-in sounds, consult the definition
of the
[sound_play/msg/SoundRequest](https://docs.ros.org/en/rolling/p/sound_play/msg/SoundRequest.html)
message. The relevant information is below the "`Sounds`" comment.



```
$ cat `rospack find sound_play`/msg/SoundRequest.msg
# Sounds
byte BACKINGUP = 1
byte NEEDS_UNPLUGGING = 2
byte NEEDS_PLUGGING = 3
byte NEEDS_UNPLUGGING_BADLY = 4
byte NEEDS_PLUGGING_BADLY = 5

# Sound identifiers that have special meaning
byte ALL = -1 # Only legal with PLAY_STOP
byte PLAY_FILE = -2
byte SAY = -3

byte sound # Selects which sound to play (see above)

# Commands
byte PLAY_STOP = 0 # Stop this sound from playing
byte PLAY_ONCE = 1 # Play the sound once
byte PLAY_START = 2 # Play the sound in a loop until a stop request occurs

byte command # Indicates what to do with the sound

string arg # file name or text to say
```



### Saying Some Text

The sound node can also be used to synthesize speech using the
[festival speech synthesis system](http://www.cstr.ed.ac.uk/projects/festival/).
The `say.py` script gives command-line access to this functionality.
This script can take its input from the command line, or if the
command-line is empty it can take input from standard input.



```
$ rosrun sound_play say.py --help
$ rosrun sound_play say.py --help
Usage: /u/blaise/ros/ros-pkg/stacks/sound_drivers/sound_play/scripts/say.py 'String to say.'
       /u/blaise/ros/ros-pkg/stacks/sound_drivers/sound_play/scripts/say.py < file_to_say.txt

Says a string. For a string on the command line, you must use quotes as
appropriate. For a string on standard input, the command will wait for
EOF before saying anything.
```



Examples (`soundplay_node.py` should be running first):


```
$ rosrun sound_play say.py 'Hello world'
Saying: Hello world.
$ echo Hello again|rosrun sound_play say.py
Awaiting something to say on standard input.
Saying: Hello again
```



### Silencing the Robot

The most immediate way to silence the robot is to use `alsamixer` to
mute or lower the volume. In some cases, a node that had requested a
continuous sound could crash with the sound still playing. In order to
stop that sound the `shutup.py` script can be used.

The `shutup.py` script sends a stop command on all sounds every 100ms
until it is terminated. This behavior will immediately stop any
continuous sounds that were playing, and will cut short any new sounds
that are played. It will not completely silence the robot, however, as
the first tens of milliseconds of newly requested sounds will be played
before they are silenced.

For example: 

```
$ rosrun sound_play shutup.py 
Sending stopall command every 100 ms.
Note: This will not prevent a node that is continuing to issue commands
from producing sound.
Press Ctrl+C to exit.
```



### Testing Sound Play Node Operation

To test that `soundplay_node.py` is operating correctly, you can use
the `test.py` script. It will play the various built-in sounds, and
exercise the `.WAV` playing and text-to-speech capabilities. To run
it: 

```
$ rosrun sound_play test.py
```



## Nodes

### soundplay_node.py

`soundplay_node.py` subscribes to `robotsound` and plays sounds on
the sound card. This node must be running before the command-line
utilities described below will work.

#### Subscribed Topics

- `robotsound`
  ([sound_play/msg/SoundRequest](https://docs.ros.org/en/rolling/p/sound_play/msg/SoundRequest.html)):
  Topic for playing sound.

#### Published Topics

- `diagnostics`
  ([diagnostic_msgs/msg/DiagnosticArray](https://docs.ros.org/en/rolling/p/diagnostic_msgs/msg/DiagnosticArray.html)):
  Reports driver diagnostic information. Detection of a disconnected
  sound device can only happen when no sounds have been played for a few
  seconds.

### Example Launch File

The following launch file, which starts `soundplay_node.py`, can be
found in `soundplay_node.launch`: 

```
<launch>
  <node name="soundplay_node" pkg="sound_play" type="soundplay_node.py"/>
</launch>
```



### Message Format

**Programmers should use the C++/Python bindings to send messages to
`robotsound`, rather than creating messages themselves.** If you need
the information in this section for something other than satisfying
curiosity, you are probably doing something wrong.

Sound commands are issued to `soundplay_node.py` via a
[sound_play/msg/SoundRequest](https://docs.ros.org/en/rolling/p/sound_play/msg/SoundRequest.html)
message. Commands define two things: a sound, and what to do with that
sound.

The sound is defined by the `sound` (int) and `arg` (string) fields
of the message, and can be one of four types:

- *a built-in sound*, identified by its identifier in `sound`
- *a file*, identified by `PLAY_FILE` in `sound` and the file name
  (absolute path on the computer running `soundplay_node.py`) in
  `arg`
- *some text to be synthesized into speech*, identified by `SAY` in
  `sound` and the text in `arg`
- *the wildcard sound*, that can only be used when stopping sound,
  identified by `ALL` in `sound`

The action that can be carried out on a sound can be:

- stop playing the sound
- play the sound once (if it is already playing, it will be played again
  after the current playback ends)
- play the sound continuously

Each message on the `robotsound` topic will cause a sound to
transition between the playing continuously, playing once (or twice) and
stopped states. For example, a backing up sound could be initiated by
sending a command for a backing up sound to play continuously. When the
robot stops backing up, a stop command will stop playback. Likewise,
verbal debugging messages could be used by telling a sound to play once.
In this case there is no need to stop playing the sound.

The special wildcard sound can be used to stop playback on all sounds.

## How to Configure and Use Speakers with sound_play

- **Note:** This tutorial assumes that you have completed the previous
  tutorials: [ROS tutorials](ROS/Tutorials).
- **Description:** This tutorial is an introduction to setting up and
  using USB speakers connected to a desktop computer. After reading it,
  you should be able to bring up the speakers, configure the speakers,
  and play sounds.
- **Keywords:** sound, speakers, driver
- **Tutorial Level:** BEGINNER
- **Next Tutorial:** How to Create a Sound Interface
  [How to Create a Sound Interface](#how-to-create-a-sound-interface)

### Compiling



```
$ rosdep install sound_play
$ rosmake sound_play
```



### Powered On and Plugged In

Make sure that your USB speakers are connected to your desktop and
powered on.

You can check that the speaker/sound card is recognized by the unix
kernel by using:



```
$ cat /proc/asound/cards
```

 You will see something similar to:

. 

```
0 [Intel          ]: HDA-Intel - HDA Intel
                      HDA Intel at 0xfdff8000 irq 16
 1 [Speaker        ]: USB-Audio - Logitech USB Speaker
                      Logitech Logitech USB Speaker at usb-0000:00:1d.7-6.1.3, full speed
```



### Configuring the Sound Driver to Use Your Speaker

To designate which sound card the driver uses, run:



```
$ asoundconf set-default-card [device #]
```

 *(i.e. In the above example, `asoundconf
set-default-card 0` would configure the driver to use the Intel card
.)*

This will create .asoundrc.asoundconf in your home directory. To make
the driver use these settings, add the following line to /.asoundrc by
using the command:



```
$ echo 'include ".asoundrc.asoundconf"' >> ~/.asoundrc
```

 (Optional) To set this default to all users,
copy this to the system-wide driver configuration file:



```
$ sudo cp ~/.asoundrc.asoundconf /etc/asound.conf
```



### Starting a roscore

For sound_play to work properly, a ros core must be running. In a **new
terminal**:



```
$ roscore
```



### Starting the sound_play node

In another **new terminal**, start the sound_play node. This node will
play sounds when it receives sound messages:



```
$ rosrun sound_play soundplay_node.py
```

 You will see:

. 

```
sound_play node is ready to play sound
```



### Playing Sound

In a **new terminal**, test that your speaker is configured properly and
playing sound. Try saying "hello world":



```
$ rosrun sound_play say.py "hello world"
```

 You will see:

. 

```
Saying: hello world
```



And you should hear "Hello world"

### Troubleshooting

If you encounter problems in this Tutorial, have a look at the
[Troubleshooting page](#troubleshooting-1), it
may have a solution for you.

------------------------------------------------------------------------

## Tutorials

- [How to Configure and Use Speakers with sound_play](#how-to-configure-and-use-speakers-with-sound_play):
  This tutorial is an introduction to setting up and using USB speakers
  connected to a desktop computer. After reading it, you should be able
  to bring up the speakers, configure the speakers, and play sounds.
- [How to Create a Sound Interface](#how-to-create-a-sound-interface):
  This tutorial covers how to create an interface for using
  `sound_play`. The interface uses a node acting as a 'funnel' as a
  convenient way to route sound commands through `sound_play`. 1.
  [Install New Festival Voices](http://ubuntuforums.org/showthread.php?t=751169).

Create a new tutorial:

## Troubleshooting

1.  format wiki
2.  language en

### Errors when using package

#### Error: The driver can't connect to the sound card



```
Exception in sound startup. Is the speaker connected? Have you configured ALSA? Can aplay play sound? Have a look at http://pr.willowgarage.com/wiki/sound_play/Troubleshooting Will retry in 5 seconds. Error message: No available audio device
```



**Solution**

- Is the sound device connected (if you are trying to use USB speakers,
  for example). Run "lsusb" to check the speaker.

<!-- -->

- Is the sound device turned off in alsamixer? Use alsamixer to turn on
  all channels. Pressing 'm' mutes and unmutes a channel.

<!-- -->

- Is the sound card configured correctly? (See **Have you told ALSA
  which device to use?** below.)

<!-- -->

- Is the speaker disabled? The Logitech USB speaker can get in a mode
  where a red light shows on the speaker. In this mode the speaker is
  disabled, and ALSA may remember the fact that the speaker was disabled
  despite unplug/plug sequences. To fix this, use **alsamixer**, select
  the PCM control. Press **m** to enable/disable the speaker (the LED
  should turn red/blue). When the LED is blue, quit alsamixer and run:
  

```
sudo /etc/init.d/alsa-util restart
```

 The speaker should now default to the enabled
  state.

#### There is a red light on the speaker

See **Error: The driver can't connect to the sound card**.

#### Error: There are no error messages and no sound

**Solution**

- Is the volume set to zero or muted? Use alsamixer to check.

#### Error: Sound coming out of wrong device

Sound plays from the wrong audio device.

**Solution:**

- Have you told ALSA which device to use? To see which cards are
  installed: 

```
cat /proc/asound/cards
```

 To use card 1 by default:
  

```
asoundconf set-default-card 1
sudo cp ~/.asoundrc.asoundconf /etc/asound.conf
```



#### Error: There is no sound if the speaker is disconnected and reconnected

If the speaker is disconnected and then reconnected, soundplay_node.py
will not play any sound, and will not report any error messages.

**Solution:** Due to limitations of pygame, soundplay_node.py cannot
detect that the speaker was disconnected unless it is left idle for
about ten to twenty seconds. If you disconnect and reconnect the
speaker, you will have to either restart soundplay_node.py, or have it
not play any sound for at least ten to twenty seconds.

#### Error: Speech synthesis does not work, but playing sounds works

Festival is not installed 

```
Saying "Hello world".
sh: text2wave: not found
```



Festival has no voices installed 

```
Saying "Hello world".

WARNING
No default voice found in ("/usr/share/festival/voices/")
either no voices unpacked or voice-path is wrong
Scheme interpreter will work, but there is no voice to speak with.
WARNING

-=-=-=-=-=- EST Error -=-=-=-=-=-
{FND} Feature Token_Method not defined

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
```



**Solution:**

- Install the festival and festvox-kallpc16k packages
  

```
rosdep install sound_play
```



#### Error : Sound voulme is small

**Solution:**

- Use mixer program to change volumes 

```
alsamixer
```



### Other sources of help

If these troubleshooting tips are not sufficient, you may be able to
find an answer on the [ALSA web page](http://www.alsa-project.org/) or
the [unofficial ALSA wiki](http://alsa.opensrc.org/). And please update
the wiki or let us know when you find the solution.

## How to Create a Sound Interface

- **Description:** This tutorial covers how to create an interface for
  using `sound_play`. The interface uses a node acting as a 'funnel'
  as a convenient way to route sound commands through `sound_play`.
- **Keywords:** sound, sound_play
- **Tutorial Level:** INTERMEDIATE

### Background

#### Prerequisites

This tutorial assumes that your linux sound drivers and speaker system
are already working and that `sound_play` is working from the
terminal, all of which can be tested in the
[Configuring and Using Speakers](#how-to-configure-and-use-speakers-with-sound_play)
tutorial. The node created in this tutorial uses the `sound_play`
convenience wrapper package to play sound. See the
sound_play documentation for details.

#### Examples and References

[Configuring and Using Speakers](#how-to-configure-and-use-speakers-with-sound_play),
sound_play Package Summary,
[sound_play/SoundRequest.msg](http://www.ros.org/doc/api/sound_play/html/msg/SoundRequest.html)

#### Dependencies

The structure built in this tutorial will depend on `sound_play` and
will require sound assets for testing.

### One Method for Structuring the Interface

This structure routes all sound instructions, given in the form of
`yak` commands, through a single node, here called `yak_node`.
`yak_node` is then the sole node responsible for dealing with
`SoundClient()` and `sound_play`, and acts as a 'funnel', allowing
multiple requesters to play sounds.

`SoundClient()` requires full path names, and can also become
overloaded and produce a segmentation fault. This partitioning of the
structure allows both of these issues to be handled in a single node.

A suitable speaker command should communicate a file name,
text-to-speech string, or built-in sound, and a command for type of
input. Here, speaker commands have a string for a file name or for
text-to-speech, and a command for playing the `.wav` file or for using
text-to-speech. More command types could be added for playing `.ogg`
or built-in files if needed.

### Code and Explanation

**Note:** It is convenient to save all sound assets in the same
directory, as `SoundClient()` requires full path names to play sound
assets. `SoundClient()` also prefers all sound assets to be `.wav`
or `.ogg` files.

All sound instructions in the form of `yak` commands are published to
the `yak` topic, to which `yak_node` subscribes.



```python
#!/usr/bin/env python
import roslib; roslib.load_manifest('sound_yak')
import rospy, os, sys
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
from sound_yak.msg import yak_cmd

# directory with sound assets - change as needed
soundAssets = '/home/shiloh/devel/audio_assets/'
# duration of yak throttle
throttle = 3 # seconds

def sound_translator(data):
    print data
    global allow_yak
    if rospy.Time.now() <= allow_yak: # Throttles yak to avoid
        print("Sound throttled")      # SoundClient segfault
        return
    # when to reallow yak
    allow_yak = rospy.Time.now() + rospy.Duration.from_sec(throttle)
    if data.cmd == "wav":
        soundhandle.playWave(soundAssets + data.param)
    if data.cmd == "say":
        soundhandle.say(data.param)

def yak_init():
    rospy.init_node('yak_node', anonymous = True)
    global allow_yak
    allow_yak = rospy.Time.now()
    rospy.Subscriber('yak', yak_cmd, sound_translator)
    rospy.spin()

if __name__ == '__main__':
    soundhandle = SoundClient()
    rospy.sleep(1)
    
    yak_init()
```



`SoundClient()` may produce a segmentation fault if too many sound
commands are given in a short period of time, so sound commands are
throttled in lines 14-20. Sounds can only be played when the current
time is later than time `allow_yak`, and every time a sound is played,
`allow_yak` is updated to the current time plus a throttle time, here
3 seconds, defined in line 11.

Lines 21-24 process `yak` commands. `SoundClient()`'s `playWave`
requires full path names for sound assets. A convenient solution allows
the parameter to be the file name only and concatenates the path name to
the folder containing sound assets, as in line 22.

### Publishing yak commands

Like any other ROS topic, `yak` commands are imported, set, and
published. `yak_cmd` is imported as usual near the beginning of the
file. `yak.cmd` and `yak.param` are both set before
`pub.publish(yak)` in the callback method, then `global yak =
yak_cmd()` and `global pub = rospy.Publisher('yak', yak_cmd)` are
set in the initialization method.

The callback should contain: 

```python
yak.cmd = 'wav'
yak.param = 'hello.wav'
pub.publish(yak)
```

 The initializer
should contain: 

```python
global yak
yak = yak_cmd()
global pub
pub = rospy.Publisher('yak', yak_cmd)
```



### Running the interface

After a `roscore` is running, `rosrun sound_play soundplay_node.py`,
and `rosrun sound_yak yak_node.py` (or whichever package you put it
in) in a new tab. Also run your nodes that send `yak` commands. Here
is a checklist for running `yak_node`: 1. Ensure that a `roscore` is
running. 

```
$ roscore
```

 1. `rosrun sound_play
soundplay_node.py` in a new tab. 

```
$ rosrun sound_play soundplay_node.py
```

 1. `rosrun
sound_yak yak_node.py` (or whichever package you put it in) in a new
tab. 

```
$ rosrun sound_yak yak_node.py
```

 1. Run your nodes that send `yak`
commands. 

```
$ rosrun my_pack my_node.py
```
