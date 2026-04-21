## Overview

`rfnserver` is a child class of
[actionlib's SimpleActionServer](actionlib#Python_SimpleActionServer)
which requires a special type of action \-- namely,
`FilledSemanticFrame.action` in
[roboframenet_msgs](roboframenet_msgs).

A relatively stable version of `RFNServer` is working in Python.

[Initializing an RFNServer](#Initializing an RFNServer) requires a three
lines of code \-- one each for importing, initializing, and starting.

[Adding semantic frames](#Adding Semantic Frames), and
[adding lexical units](#Adding Lexical Units) each require one line of
code. (For adding semantic frames and lexical units, a corresponding
yaml file is also needed. See:
[yaml files for lexical units](semantic_framer#Creating Lexical Units),
[yaml files for semantic frames](frame_registrar#Creating Semantic Frames).)

[Registration with a semantic frame](#Registering with a Semantic Frame)
requires one line of code for registration plus a function to handle the
callback.

## Initializing an RFNServer

```
from rfnserver import RFNServer

[...]

server = RFNServer("moo", moo)
# Add semantic frames and lexical units here.
# Register with semantic frames here.
server.start()
```

The first argument is the topic where you want the `RFNServer`
(behind-the-scenes: `SimpleActionServer`) to publish goal, feedback,
and preemption messages.

The second argument is a callback function which takes one argument \--
namely, a filled semantic frame. (The message type is of type
[roboframenet_msgs](roboframenet_msgs)/FilledSemanticFrame .) The frame
passed into this callback will be from one of the semantic frames with
which the `RFNServer` has
[registered](#Registering with a Semantic Frame).

To get arguments for a specific frame element of the semantic frame, the
helper function `frame_argument` is provided:

```
def callback(filled_semantic_frame):
  [...]
  arg_str = RFNServer.frame_argument(filled_semantic_frame, "parameter")
  [...]
```

## Adding Semantic Frames

```
server.add_frame("../frames/mooing.yaml")
```

The filepath is relative to the directory from which the program was
launched. Typically, this means that before running, you'll want to
either move to the node's directory, or you'll want to add the
attribute [cwd="node"](roslaunch/XML/node#Attributes) to the node's
tag in its roslaunch file.

## Adding Lexical Units

```
server.add_lexical_unit("../lu/mooing.yaml")
```

The filepath is relative to the directory from which the program was
launched. Typically, this means that before running, you'll want to
either move to the node's directory, or you'll want to add the
attribute [cwd="node"](roslaunch/XML/node#Attributes) to the node's
tag in its roslaunch file.

## Registering with a Semantic Frame

```
server.register_with_frame("mooing")
```

Upon registration, the callback specified in the
[initialization](#Initializing an RFNServer) of the RFNServer may
receive a filled semantic frame of the specified type.
