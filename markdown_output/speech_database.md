## Documentation

See the speech_database node documentation.

## Nodes

```clearsilver
name = speech_database
desc = This node sends request to the soundplay_node to play audio files that contain synthesised speech. It checks with a dictonary if the to-be-synthesised text has been handled before. If so, the existing audio file is used, otherwise, synthesised speech is downloaded from Google. The filename is a 50 character string and is chosen randomly. To determine whether an audio file that corresponds to the text already exists, the node accesses a json dictionary that contains pre-downloaded files with synthesised speech. It holds  strings as keys and filenames as values.
sub {
  0.name = /speech
  0.type = std_msgs/String
  0.desc = text to be synthesised
}
pub {
  0.name = /robotsound
  0.type = sound_play/SoundRequest
  0.desc = Request message for playing audio files
}
param {
  0.name = ~audioPath
  0.type = string
  0.desc = path to folder that contains audio files
  1.name = ~language
  1.type = string
  1.desc = Language abbreviation (en, de, fr, etc.) for speech synthesis
  2.name = ~jsonPath
  2.type = string
  2.desc = path to json file that holds the speech database
}
```

## Launch Files

Use roslaunch files to load this files.

-   **speech.launch** - Launches soundplay_node.py of the
    [sound_play](sound_play) package and the speech_database node with
    the parameters mentioned above.

## Test Voice Output

By calling ```
rostopic pub /speech std_msgs/String "Hello World"
``` one can test the voice output.

## Use of self generated voice files

It is also possible to use self generated voice files (e.g. by recording
the own voice). In this case one has to copy the files into the folder
defined by the parameter 'audioPath' and edit the json file defined by
'jsonPath' by simply adding lines for every entry.
