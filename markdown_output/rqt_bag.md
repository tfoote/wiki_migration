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
contained in the
[rqt_bag_plugins](https://index.ros.org/p/rqt_bag_plugins) package
available in the
[rqt_common_plugins](https://index.ros.org/p/rqt_common_plugins)
metapackage.

![rqt_bag window](doc/rqt_bag.png)

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

![publish a topic in rqt_bag](doc/publish_grab.png)

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

![rqt_bag time selection](doc/rqt_bag_time_selection.png)

### Toolbar

At the top of the timeline window is a toolbar for controlling the
playhead and zooming the display:

![attachment:rqt_bag_toolbar.png](doc/rqt_bag_toolbar.png)

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

![rqt_bag message views](doc/rqt_bag_views.png)

For details on common message views such as images and plotting, see
[rqt_bag_plugins](https://index.ros.org/p/rqt_bag_plugins).

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
in the [rqt_bag_plugins](https://index.ros.org/p/rqt_bag_plugins)
package.

## Tutorials

- [Create an rqt_bag Plugin](#create-an-rqt_bag-plugin):
  Create a custom visualization for rqt_bag

## Create an rqt_bag Plugin

- **Description:** Create a custom visualization for rqt_bag
- **Keywords:** rqt_bag bag data rqt
- **Tutorial Level:** INTERMEDIATE

Let's say you have bags of data and you want to be able to visualize
them. `rqt_bag` gives you the ability to scroll through the recorded
messages and visualize the raw message values. However, often may want
something more visual, or to do some post-processing on the raw message.
For that, you can write an rqt_bag plugin, using the proof-of-concept
Python plugin system. That way you can go from a simple visualization of
the messages\...

![width=100%](doc/base.png)

to something like this:

![width=100%](doc/full.png)

### Package Setup

We're going to create a package called `rqt_bag_diagnostics_demo`.
Insert the following into your `package.xml`. 

```xml
    <depend>diagnostic_msgs</depend>
    <depend>rqt_bag</depend>
    <export>
      <rqt_bag plugin="${prefix}/plugins.xml"/>
    </export>
```


Since we'll be making a python library, we'll need the standard Python
setup. In your CMake 

```
catkin_python_setup()
```

 In `setup.py`


```/usr/bin/env

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

package_info = generate_distutils_setup(
    packages=['rqt_bag_diagnostics_demo'],
    package_dir={'': 'src'}
)

setup(**package_info)
```



Finally, we're going to define the plugin in an xml file called
`plugins.xml` (as referenced in the `package.xml`)



```xml
<library path="src">
  <class name="DiagnosticBagPlugin"
         type="rqt_bag_diagnostics_demo.the_plugin.DiagnosticBagPlugin"
         base_class_type="rqt_bag::Plugin">
    <description>
    </description>
  </class>
</library>
```



The name is the name of the class we'll create. The type is the way we
would import the class in Python, i.e.
`package_name.name_of_file.class_name`

### Defining the Plugin

As with all Python libraries, we'll make sure a (blank)
`src/package_name/__init__.py` file exists. As referenced in the
`plugins.xml`, all the code that follows will be in
`src/rqt_bag_diagnostics_demo/the_plugin.py`.

First, the core Plugin class.



```python
from rqt_bag.plugins.plugin import Plugin
from python_qt_binding.QtCore import Qt
from diagnostic_msgs.msg import DiagnosticStatus


def get_color(diagnostic):
    if diagnostic.level == DiagnosticStatus.OK:
        return Qt.green
    elif diagnostic.level == DiagnosticStatus.WARN:
        return Qt.yellow
    else:  # ERROR or STALE
        return Qt.red


class DiagnosticBagPlugin(Plugin):
    def __init__(self):
        pass

    def get_view_class(self):
        return None

    def get_renderer_class(self):
        return None

    def get_message_types(self):
        return ['diagnostic_msgs/DiagnosticStatus']
```



Here we have some basic imports, and helper function that we'll use
later, and a class that defines the three parts of an `rqt_bag`
plugin. 1. `view_class` - a.k.a. `TopicMessageView` - A separate
panel that can be used for viewing individual messages. 2.
`renderer_class` - a.k.a. `TimelineView` - A tool for drawing onto
the timeline view of the bag data. 3. `message_types` - An array of
strings that define what message types this plugin can be used for. You
can return `\['\*'\]` for it to apply to all messages.

Since we return None for the first two methods, this plugin won't do
anything. We'll tackle each of these separately.

### TopicMessageView

#### Version 1

We're going to create a class that extends the `TopicMessageView`
class.



```python
class DiagnosticPanel(TopicMessageView):
    name = 'Awesome Diagnostic'

    def message_viewed(self, bag, msg_details):
        super(DiagnosticPanel, self).message_viewed(bag, msg_details)
        t, msg, topic = msg_details
        print msg
```



Here we define two things. The name string defines what we'll see in
the menu of `rqt_bag`. The `message_viewed` method defines what to
do when the message is selected. So here, we'll just print the message
to terminal for now.

We need to hook this class we've created into the plugin
infrastructure, and for that, we return the class object itself in the
`get_view_class` method.



```python
    def get_view_class(self):
        return DiagnosticPanel
```



To see this in action, open up the
[provided bag file](doc/some_diagnostics.bag), and right click on the
diagnostic track. It will give you three options under the "View":
Raw, Plot and our "Awesome Diagnostic." Clicking this should open a
panel and you can scroll through the messages and watch them print.
![width=100%](doc/panel.png)

#### Version 2

`TopicMessageView` is itself an extension of a `QObject`. There's
lots of things you could do with this using all the might and power of
Qt. This is not a python Qt tutorial sadly. So we're going to just add
a simple QWidget and draw on it.



```python
class DiagnosticPanel(TopicMessageView):
    name = 'Awesome Diagnostic'

    def __init__(self, timeline, parent, topic):
        super(DiagnosticPanel, self).__init__(timeline, parent, topic)
        self.widget = QWidget()
        parent.layout().addWidget(self.widget)
        self.msg = None
        self.widget.paintEvent = self.paintEvent

    def message_viewed(self, bag, msg_details):
        super(DiagnosticPanel, self).message_viewed(bag, msg_details)
        _, self.msg, _ = msg_details
        self.widget.update()

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self.widget)

        rect = event.rect()

        if self.msg is None:
            self.qp.fillRect(0, 0, rect.width(), rect.height(), Qt.white)
        else:
            color = get_color(self.msg)
            self.qp.setBrush(QBrush(color))
            self.qp.drawEllipse(0, 0, rect.width(), rect.height())
```



In the constructor, we create a `QWidget` and override its
`paintEvent` method. Now when we get a message with
`message_viewed`, we save it, and update the widget, which will in
turn call our `paintEvent`. Before a message is selected, we'll just
paint a white rectangle. Otherwise, we'll draw a circle, using our
handy helper method to relate the color to what level the diagnostic is
at. ![width=100%](doc/circle.png)

### TimelineRenderer

#### Version 1

To draw on the timeline, we extend the `TimelineRenderer` class.


```python
class DiagnosticTimeline(TimelineRenderer):
    def __init__(self, timeline, height=80):
        TimelineRenderer.__init__(self, timeline, msg_combine_px=height)

    def draw_timeline_segment(self, painter, topic, start, end, x, y, width, height):
        painter.setBrush(QBrush(Qt.blue))
        painter.drawRect(x, y, width, height)
```

 You can customize how tall the message's
portion of the timeline is with the `msg_combine_px` parameter. The
key method to override is the `draw_timeline_segment` method which
gives you potions of the timeline to draw. For now we'll just draw blue
rectangles on each segment.

Just like the message view, you also have to edit the plugin to return
your class.



```python
    def get_renderer_class(self):
        return DiagnosticTimeline
```



To view this, you have to enable "Thumbnails" (a misleading name) in
the rqt_bag gui.

![width=100%](doc/blue.png)

#### Version 2

Okay, now we actually want to customize how the messages are drawn in
the timeline based on the messages themselves. For that, there's a
wonky bunch of magical incantations you need to read the messages out of
the bag files.



```python
    def draw_timeline_segment(self, painter, topic, start, end, x, y, width, height):
        bag_timeline = self.timeline.scene()
        for bag, entry in bag_timeline.get_entries_with_bags([topic], rospy.Time(start), rospy.Time(end)):
            topic, msg, t = bag_timeline.read_message(bag, entry.position)
            color = get_color(msg)
            painter.setBrush(QBrush(color))
            painter.setPen(QPen(color, 5))

            p_x = self.timeline.map_stamp_to_x(t.to_sec())
            painter.drawLine(p_x, y, p_x, y+height)
```

 Using the topic, start and end parameters of
the method, we can get the bag entries that correspond with this segment
of the timeline. We can then get the actual message and use it to draw.
Here we are drawing a line based on the level of the diagnostic message.
We can automatically figure out where to draw the message horizontally
using the `map_stamp_to_x` method.

![width=100%](doc/timeline.png)

The alternative to this weird way of accessing the messages is to
[Timeline Cache](https://github.com/ros-visualization/rqt_bag/blob/master/rqt_bag/src/rqt_bag/timeline_cache.py)
like the
[ImageTimelineViewer](https://github.com/ros-visualization/rqt_bag/blob/master/rqt_bag_plugins/src/rqt_bag_plugins/image_timeline_renderer.py)
does, but figuring that out is left as an exercise to the reader.
