**`rqt_bag` supersedes [rxbag](rxbag)**, which is deprecated since
`ROS` [groovy](groovy).

## Overview

`rqt_bag` is an application for recording and managing bag files.
Primary features:

- show bag message contents
- display image messages (optionally as thumbnails on a timeline)
- plot configurable time-series of message values
- publish/record messages on selected topics to/from ROS
- export messages in a time range to a new bag

`rqt_bag` can be extended via a plugin mechanism. Core plugins are
contained in the [rqt_bag_plugins](rqt_bag_plugins) package available in
the [rqt_common_plugins](rqt_common_plugins) metapackage.

![rqt_bag window\|width="750"](attachment:rqt_bag.png)

## Usage

### To run



```
$ rqt
```



and select from `Plugins` \--> `Logging` \--> `Bag`.

Or simply the following (with this you can't open `rqt_bag` with
other rqt tools).



```
$ rqt_bag
```



The main window shows a timeline representing the stream of messages
contained in the bag file, listed by topic.

### Publish ROS topics while playing back from the recorded bag file

Right-click on the name of the topic you want to publish, then select
`Publish` (as in the image below).

![publish a topic in rqt_bag\|width="700"](attachment:publish_grab.png)

**Note:** Don't forget to use simulation time when republishing from a
bag file:
[Using Sim Time](Clock#Using_Simulation_Time_from_the_.2BAC8-clock_Topic)

### To stop recording

You can stop recording by re-clicking the red circle button.

## Description for GUI components

### Timeline

The messages are shown at the timestamp stored in the bag file. This
timestamp may differ from the message's `Header` timestamp (if any),
e.g. `rosbag record` stores the time the message was received.

Right-clicking on the timeline opens a menu with options for opening
detailed message views, choosing which topics to display thumbnails for,
managing re-publishing of messages, and exporting a time range of
messages to another bag.

A subset of the data can be selected by dragging the cursor over a range
of time at the top of the timeline. This selection is used in any
message view, such as plot view.

![rqt_bag time selection\|width="700"](attachment:rqt_bag_time_selection.png)

### Toolbar

At the top of the timeline window is a toolbar for controlling the
playhead and zooming the display:

![](attachment:rqt_bag_toolbar.png)

From left to right, the buttons on the toolbars allow you to:

- record mode
- load file
- save currently selected region to a bag file
- move playhead to start of timeline
- rewind or slow playback
- play/pause
- fastforward or slow rewind
- move playhead to end of timeline
- zoom in
- zoom out
- reset zoom level to full bag
- toggle thumbnail display

### Status Bar

At the bottom of the window is a status bar:

From left to right, these indicators display:

- progress for background tasks
- timestamp of playhead
- time in human readable form
- elapsed time in seconds from start of timeline
- current playback speed

### Message Views

Message views display information about the message immediately
preceding the position of the timeline playhead (the vertical red line.)
The message datatype determines which message views are available.

![rqt_bag message views\|width="700"](attachment:rqt_bag_views.png)

For details on common message views such as images and plotting, see
[rqt_bag_plugins](rqt_bag_plugins).

Every message view has a toolbar for stepping the playhead forward to
the next message on the topic, back to the previous message, or to the
first and last messages in the bag.

#### raw

Every topic has an option of displaying a raw view of the message. This
displays the fields of the message in a tree view:

Also, the following keyboard shortcuts can be used:

  -- ---------- -- ----------------------------------- --
     *Ctrl-A*      Select all fields in message        
     *Ctrl-C*      Copy selected fields to clipboard   
  -- ---------- -- ----------------------------------- --

## Plugin API

`rqt_bag` currently has a proof-of-concept plugin API, which is used
in the [rqt_bag_plugins](rqt_bag_plugins) package.
