## Usage

Any [rxbag](rxbag) plugin in the `ROS_PACKAGE_PATH` is detected
automatically by `rxbag` on start-up.

To access these plugins, launch the `rxbag` GUI tool (see
[rxbag](rxbag) for details), right-click on the timeline and select a
topic and view type from the context menu.

## Plugins

The following plugins are currently provided for `rxbag`:

### Image

The image view displays raw image data for
[sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)
and
[sensor_msgs/msg/CompressedImage](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CompressedImage.html)
messages:

![](attachment:rxbag_prosilica.png)

The view is initially opened at the recorded resolution of the raw
image. Resizing the window scales the image.

Right-clicking on the image opens a context menu which allows you to
resize the window to the original resolution, or save the image to a
`.png` file.

### Plot

The plot view displays a customizable time series plot of numeric fields
in a ROS message.

When initially opened, the plot view is empty:

![](attachment:rxbag_plot_view_empty.png)

Clicking on the configure button in the toolbar
(![](attachment:rxbag_plot_view_configure_button.png)) opens a new
window for selecting which fields in the message to plot. Message fields
are displayed in the left tree, and the current plot configuration is
shown in the right tree.

![](attachment:rxbag_plot_view_configure.png)

To plot a message field, first select a plot
(![](attachment:rxbag_plot_view_plot.png)) in the right tree. Then,
either double-click a field in the left tree, or select it and click the
add series button (![](attachment:rxbag_plot_view_add_series.png)).

New plots are created by clicking the add plot button
(![](attachment:rxbag_plot_view_add_plot.png)), and are deleted with the
remove plot button (![](attachment:rxbag_plot_view_remove_plot.png)).

Series can be moved between plots by clicking and dragging, and are
deleted either with the remove series button
(![](attachment:rxbag_plot_view_remove_series.png)) or by
double-clicking on the series.

Any change to the plot configuration automatically reloads data from the
[bag](Bags) file, updating the plot view display:

![](attachment:rxbag_plot_view.png)

Each plot in the display shares the same X axis, which shows the number
of seconds since the start of the bag file. The axis is centered on the
timeline's current playhead position. The range can be configured under
the `Interval` submenu in the context-menu accessible by clicking the
right mouse button on the plot window.

To zoom/pan the plot, use mouse middle click or shift-click. Vertical
movement zooms, horizontal movement pans.

## Roadmap

The plugin API for `rxbag` is experimental and under development.
Please see [rxbag](rxbag) for roadmap information.
