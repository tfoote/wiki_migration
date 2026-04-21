## Deprecated

(!) **[rx](rx) packages are replaced by [rqt](rqt), which is available
for fuerte and later.**

[../rqt_bag](../rqt_bag) succeeds \`rxbag\`.

## Overview

\`rxbag\` is an application for recording and managing bag files. Its
primary features are:

-   show tree-view of bag message contents
-   display image messages (optionally as thumbnails on a timeline)
-   plot configurable time-series of message values
-   publish/record messages on selected topics to/from ROS
-   export messages in a time range to a new bag
-   export message contents to comma-separated value (CSV) files

\`rxbag\` can be extended via a plugin mechanism. Core plugins are
contained in the [rxbag_plugins](rxbag_plugins) package in the
[visualization](visualization) stack.

## Usage

To run, pass the filename of a bag file, e.g. ```
$ rxbag teleop.bag
```

Additional [command-line options](rxbag/Commandline) are available.

The main window shows a timeline representing the stream of messages
contained in the bag file, listed by topic.

![](attachment:rxbag-1.png)

## Timeline

The messages are shown at the timestamp stored in the bag file. This
timestamp may differ from the message\'s \`Header\` timestamp (if any),
e.g. \`rosbag record\` stores the time the message was received.

Right-clicking on the timeline opens a menu with options for opening
detailed message views, choosing which topics to display thumbnails for,
managing re-publishing of messages, and exporting a time range of
messages to another bag.

When using the \`\--record\` option, you can sync the timeline to the
latest message by left-clicking to the far right (to the right of the
latest message), which will make it \"stick\" to real-time.

### Toolbar

At the top of the timeline window is a toolbar for controlling the
playhead and zooming the display:

![](attachment:rxbag-menu.png)

From left to right, the buttons on the toolbars allow you to:

-   move playhead to start of timeline (Keyboard shortcut: *Home*)
-   rewind or slow playback (*Numpad -*)
-   play (*Space*)
-   fastforward or slow rewind (*Numpad +*)
-   move playhead to end of timeline (*End*)
-   zoom in (*Page Up*)
-   zoom out (*Page Down*)
-   reset zoom level
-   toggle thumbnail display

Also, the timeline can be shifted later or earlier using the arrow keys
(*Left* and *Right* respectively.)

### Status Bar

At the bottom of the window is a status bar:

![](attachment:rxbag-status.png)

From left to right, these indicators display:

-   status text
-   progress for background tasks
-   timestamp of playhead
-   time in human readable form
-   elapsed time in seconds from start of timeline
-   playback speed

## Message Views

Message views display information about the message immediately
preceding the position of the timeline playhead (the vertical red line.)
The message datatype determines which message views are available.

For details on common message views such as images and plotting, see
[rxbag_plugins](rxbag_plugins).

Every message view has a toolbar for stepping the playhead forward to
the next message on the topic, back to the previous message, or to the
first and last messages in the bag.

### raw

Every topic has an option of displaying a raw view of the message. This
displays the fields of the message in a tree view:

![](attachment:rxbag_battery_raw.png)

Also, the following keyboard shortcuts can be used:

  -- ---------- -- ----------------------------------- --
     *Ctrl-A*      Select all fields in message        
     *Ctrl-C*      Copy selected fields to clipboard   
  -- ---------- -- ----------------------------------- --

String representations of message fields are truncated to 50 characters.

## Plugin API

\`rxbag\` currently has a proof-of-concept plugin API, which is used in
the [rxbag_plugins](rxbag_plugins) package. Future versions of ROS will
have a more stable API to more broadly support plugins.
