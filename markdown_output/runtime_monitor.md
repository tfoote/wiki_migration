```wiki
Deprecated: `runtime_monitor` is superseded by [[rqt_runtime_monitor]].
```

## Overview

The \`runtime_monitor\` package allows robot operators to view raw
diagnostics data for a robot. Using the [diagnostics](diagnostics)
toolchain, the Runtime Monitor will display the raw data on the
\`/diagnostics\` topic, of type
\<\<MsgLink(diagnostic_msgs/DiagnosticArray)\>\>.

For robots with a [diagnostic_aggregator](diagnostic_aggregator), users
should use the [robot_monitor](robot_monitor) for viewing diagnostics.
The \`runtime_monitor\` is only useful for simple systems, or for users
who need the raw data.

![](attachment:runtime_monitor.png)

## Viewing Diagnostics

To start the \`runtime_monitor\`, point to the ROS [Master](Master) for
your robot, e.g. ```
export ROS_MASTER_URI=http://my_robot:11311
```

In the same terminal, type: ```
rosrun runtime_monitor monitor
```

For the complete tutorial, see
[Starting the Runtime Monitor](diagnostics/Tutorials/Starting the Runtime Monitor)

### Rxbag Plugin

The \`runtime_monitor\` can view messages of type
\<\<MsgLink(diagnostic_msgs/DiagnosticArray)\>\> as an [rxbag](rxbag)
plugin. This features is experimental.

## Embedding a Monitor Panel in WX Application

The \`MonitorPanel\` class of the \`runtime_monitor\` can be embedded in
a WX application. To embed the monitor inside a WX notebook panel:

```python
from runtime_monitor.monitor_panel import MonitorPanel

# ... code above ...
  def create_monitor(self):
    self._monitor_panel = MonitorPanel(self._notebook)

    # Set size to make it pretty
    self._monitor_panel.SetSize(wx.Size(400, 500))
    # Notebook is wxNotebook
    self._notebook.AddPage(self._monitor_panel, "Diagnostics")

  def on_change_topic(self, new_topic):
    """
    Must be of type diagnostic_msgs/DiagnosticArray
    """
    self._monitor_panel.change_diagnostic_topic(new_topic)

  def on_reset(self):
    self._monitor_panel.reset_monitor()
 
  def close(self):
    """
    Safely unregister from diagnostics topic
    """
    self._monitor_panel.shutdown()
```

Only the above functions are supported when embedded into a WX
application.

## ROS API

```clearsilver
name = monitor
desc = Displays diagnostics in GUI
sub {
  0.name = /diagnostics
  0.type = diagnostic_msgs/DiagnosticArray
  0.desc = Raw diagnostics data from robot
}
```
