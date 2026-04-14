## General Philosophy

The \`sound_play\` node considers each sound (built-in, wave file or
synthesized text) as an entity that can be playing, playing repeatedly
or stopped. Nodes change the state of a sound by publishing to the
\`robotsound\` topic. Multiple sounds can be played at once.

## Supported Hardware

This node has been tested on the Logitech USB speakers on the PR2 and on
some built-in Intel sound-cards, but should support any sound card that
is supported by SDL. Because it accesses SDL via pygame, it has no
control over which sound device is used. You will have to configure SDL
and ALSA/OSS to default to the sound device you want to use.

## API Stability

-   The C++ and Python APIs are stable.

```{=html}
<!-- -->
```
-   The ROS API and in particular the message format should not be
    relied on and may change at any time to support extended
    functionality.

### Known Limitations

Please let us know if these limitations actually bother you.

-   Two nodes independently using the same sound may have strange
    interactions. For example one node may stop a sound that was started
    by the other one.

```{=html}
<!-- -->
```
-   There is no way to tell when a sound stops playing.

```{=html}
<!-- -->
```
-   When a sound is played multiple times, at most two copies of that
    sound will accumulate in the queue at once.

## C++/Python API

C++ and Python bindings are provided. It should be unnecessary to
directly generate messages when playing sounds from C++ or Python.
Documentation of the language bindings are in
[doxygen](http://docs.ros.org/latest-available/api/sound_play/html/index.html).

## Command-line utilities

The following utilities can be used to play sound when
\`soundplay_node.py\` is running. For help on getting
\`soundplay_node.py\` running refer to the
[tutorial](sound_play/Tutorials/ConfiguringAndUsingSpeakers).

### Playing a .WAV or .OGG file

The \`play.py\` script can play any \`.WAV\` or \`.OGG\` file. The file
must be available on the computer on which \`soundplay_node.py\` is
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
by specifying their integer identifier using \`playbuiltin.py\`.
```
$ rosrun sound_play playbuiltin.py 
Usage: /u/blaise/ros/ros-pkg/stacks/sound_drivers/sound_play/scripts/playbuiltin.py <sound_id>

Plays one of the built-in sounds based on its integer ID. Look at the <<MsgLink(sound_play/SoundRequest)>> message definition for IDs.
```

For example (\`soundplay_node.py\` should be running first):
```
$ rosrun sound_play playbuiltin.py 2
Playing sound 2".
```

To get an up-to-date list of the built-in sounds, consult the definition
of the \<\<MsgLink(sound_play/SoundRequest)\>\> message. The relevant
information is below the \"\`Sounds\`\" comment.

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
The \`say.py\` script gives command-line access to this functionality.
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

Examples (\`soundplay_node.py\` should be running first):
```
$ rosrun sound_play say.py 'Hello world'
Saying: Hello world.
$ echo Hello again|rosrun sound_play say.py
Awaiting something to say on standard input.
Saying: Hello again
```

### Silencing the Robot

The most immediate way to silence the robot is to use \`alsamixer\` to
mute or lower the volume. In some cases, a node that had requested a
continuous sound could crash with the sound still playing. In order to
stop that sound the \`shutup.py\` script can be used.

The \`shutup.py\` script sends a stop command on all sounds every 100ms
until it is terminated. This behavior will immediately stop any
continuous sounds that were playing, and will cut short any new sounds
that are played. It will not completely silence the robot, however, as
the first tens of milliseconds of newly requested sounds will be played
before they are silenced.

For example: ```
$ rosrun sound_play shutup.py 
Sending stopall command every 100 ms.
Note: This will not prevent a node that is continuing to issue commands
from producing sound.
Press Ctrl+C to exit.
```

### Testing Sound Play Node Operation

To test that \`soundplay_node.py\` is operating correctly, you can use
the \`test.py\` script. It will play the various built-in sounds, and
exercise the \`.WAV\` playing and text-to-speech capabilities. To run
it: ```
$ rosrun sound_play test.py
```

## Nodes

```clearsilver
node {
 0{
 name = soundplay_node.py
 desc = `soundplay_node.py` subscribes to `robotsound` and plays sounds on the sound card. This node must be running before the command-line utilities described below will work.
 sub {
  0{
  name= robotsound
  type= sound_play/SoundRequest
  desc= Topic for playing sound. 
  }
 }
 pub {
  0{
  name= diagnostics
  type= diagnostic_msgs/DiagnosticArray
  desc= Reports driver diagnostic information. Detection of a disconnected sound device can only happen when no sounds have been played for a few seconds.
  }
 }
 }
}
```

### Example Launch File

The following launch file, which starts \`soundplay_node.py\`, can be
found in \`soundplay_node.launch\`: ```
$rosrun sound_play play.py /usr/share/xemacs21/xemacs-packages/etc/sounds/im_so_happy.wav
Playing "/usr/share/xemacs21/xemacs-packages/etc/sounds/im_so_happy.wav".
```0

### Message Format

\'\'\'Programmers should use the C++/Python bindings to send messages to
\`robotsound\`, rather than creating messages themselves.\'\'\' If you
need the information in this section for something other than satisfying
curiosity, you are probably doing something wrong.

Sound commands are issued to \`soundplay_node.py\` via a
\<\<MsgLink(sound_play/SoundRequest)\>\> message. Commands define two
things: a sound, and what to do with that sound.

The sound is defined by the \`sound\` (int) and \`arg\` (string) fields
of the message, and can be one of four types:

-   \'\'a built-in sound\'\', identified by its identifier in \`sound\`
-   \'\'a file\'\', identified by \`PLAY_FILE\` in \`sound\` and the
    file name (absolute path on the computer running
    \`soundplay_node.py\`) in \`arg\`
-   \'\'some text to be synthesized into speech\'\', identified by
    \`SAY\` in \`sound\` and the text in \`arg\`
-   \'\'the wildcard sound\'\', that can only be used when stopping
    sound, identified by \`ALL\` in \`sound\`

The action that can be carried out on a sound can be:

-   stop playing the sound
-   play the sound once (if it is already playing, it will be played
    again after the current playback ends)
-   play the sound continuously

Each message on the \`robotsound\` topic will cause a sound to
transition between the playing continuously, playing once (or twice) and
stopped states. For example, a backing up sound could be initiated by
sending a command for a backing up sound to play continuously. When the
robot stops backing up, a stop command will stop playback. Likewise,
verbal debugging messages could be used by telling a sound to play once.
In this case there is no need to stop playing the sound.

The special wildcard sound can be used to stop playback on all sounds.
