## Provides

-   `cameras`
-   `actions`

### actions

`actions` provides an index of all [actionlib](actionlib) actions in a
running ROS graph. The API is currently very simple right now and only
supports display action goal arguments and synchronous invocation.

`actions.action_name` Prints action goal arguments.

`actions.action_name(args)` Invoke action synchronously and return
result.

### cameras

`cameras` provides an index of cameras that support the general ROS
camera interface, which is commonly used in
[camera_drivers](camera_drivers). With the `cameras` object, you can
easily inspect which cameras are available, retrieve their camera info,
and show camera images.

`show(cameras.camera)` Opens camera viewer using `rviz/image_view`.
Accepts both single and stereo camera objects. NOTE: this requires
loading the [rosh_visualization](rosh_visualization) plugin.

## Advanced

### Plugin API

`rosh_common.PLUGIN_CAMERA_SHOW` Register `show()` handler for
`cameras`. Used by [rosh_visualization](rosh_visualization).
