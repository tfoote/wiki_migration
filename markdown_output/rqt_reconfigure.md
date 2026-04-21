## Usage

To launch reconfigure_gui in Groovy, run: ```
rosrun rqt_reconfigure rqt_reconfigure
```

You will be presented with an interface like this:

![ Node List](attachment:reconfigure_gui1.png )

From here you can select any of the left hand nodes to reconfigure it:

![ Reconfiguring single node](attachment:reconfigure_gui2.png )

You can select multiple nodes.

![ Reconfiguring multiple nodes](attachment:reconfigure_gui3.png )

You can also launch the `reconfigure_gui` via [rqt_gui](rqt_gui):
```
rosrun rqt_gui rqt_gui
```

### Limitation

-   [Incompatible with nodes running on ROS that's older than `Groovy`](https://github.com/ros-visualization/rqt_common_plugins/issues/40)
    (won't fix)
-   Parameters are only picked up when this tool boots. Workaroud:
    Refresh plugin (by blue "whirling arrow"(?)) button on each
    plugin's toolbar
    ([ticket](https://github.com/ros-visualization/rqt_common_plugins/issues/154))

## Troubleshoot

Generally speaking, try isolating GUI and non-GUI issue.
`dynamic_reconfigure`'s
[command line tools](http://wiki.ros.org/dynamic_reconfigure/#dynamic_reconfigure.2BAC8-groovy.dynparam_command-line_tool)
are helpful for doing that.

### No parameter listed on GUI

([Related ticket](https://github.com/ros-visualization/rqt_reconfigure/issues/4#issuecomment-361952689))

Run the following command to make sure dynamic reconfigure parameters
are returned:

```
rosrun dynamic_reconfigure dynparam list
```

If nothing returned then the issue is your `dynamic_reconfigure`
itself, not `rqt-reconfigure`.

## Internal design

### Sequence diagrams

Some diagrams about key sequences. Click to magnify images.

Sequence; Node tree building and connecting each node once user chooses.

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     [![ Node tree building and connecting each node once user chooses \| width=800 ](attachment:seq-1_msg_arrval.png )](http://ros.org/wiki/rqt_reconfigure?action=AttachFile&do=view&target=seq-1_msg_arrval.png)   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Sequence; Filtering nodes tree by input text

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     [![ Filtering nodes tree by input text \| width=800 ](attachment:seq-2_Filtering_with_timer.png )](http://ros.org/wiki/rqt_reconfigure?action=AttachFile&do=view&target=seq-2_Filtering_with_timer.png)   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     [ {{attachment:seq-5_Connect_nodes_multithread.png \| Sequence; Connecting nodes by multi thread \| width=800 }}](http://ros.org/wiki/rqt_reconfigure?action=AttachFile&do=view&target=seq-5_Connect_nodes_multithread.png )   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
