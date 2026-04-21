## ROS API

### Published Topics

This node publishes [sensor_msgs](sensor_msgs)/jointState messages on
two topics for the raw and calibrated values. The two topics are
**/cyberglove/raw/joint_states** and
**/cyberglove/calibrated/joint_states**

### Services

You have access to 2 different services to control the glove node.

-   **/cyberglove/start**: With the
    [start / stop](http://www.ros.org/doc/api/cyberglove/html/srv/Start.html)
    service you can start or stop publishing the glove data. Please note
    that it's a lot more convenient for you to simply push on the glove
    wrist button: if the light is on the data will be published, if
    it's off, the data won't be published.
    ![The Cyberglove, with the wrist button highlighted\|width=400](attachment:glove_btn.png)

```{=html}
<!-- -->
```
-   **/cyberglove/calibration**: A
    [calibration](http://www.ros.org/doc/api/cyberglove/html/srv/Calibration.html)
    service is also available if you want to load a different
    calibration file for the glove.

### Parameters

-   **publish_frequency**: The frequency at which the data are polled
    from the Cyberglove.
-   **path_to_glove**: In the cyberglove.launch file, you can also edit
    on which port you want to listen to, by modifying the
    **path_to_glove** parameter. By default it's set to be
    **dev/ttyS0**, but this can vary depending on your configuration.
-   **path_to_calibration**: You can modify here the default path to the
    calibration file used for the glove.

## Calibration

The calibration file is loaded from the
[sr_control_gui](sr_control_gui)/param/cyberglove.cal file. To change
which file you want to use, you can simply edit the parameter
**path_to_calibration** of the **cyberglove.launch** file.


```
<node pkg="cyberglove" name="cyberglove" type="cyberglove">
    <param name="cyberglove_prefix" type="string" value="/cyberglove" />
    <param name="publish_frequency" type="double" value="20.0" />
    <param name="path_to_glove" type="string" value="/dev/ttyS0" />
    <param name="path_to_calibration" type="string" value="$(find
    sr_control_gui)/param/cyberglove.cal" />
</node>
```



A calibration process is available in the **cyberglove calibrator**
plugin of the [sr_control_gui](sr_control_gui).

## Which Versions of the Cyberglove have been tested

The standard Cyberglove connected to the serial port has been tested, as
well as the bluetooth version of the cyberglove. To use the bluetooth
version, you need to pair it with your computer. A good howto is
available on the
[Gentoo wiki](http://www.gentoo.org/doc/en/bluetooth-guide.xml).
