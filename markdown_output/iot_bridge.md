## Overview

The IoT Bridge provides a bridge between ROS and the openHAB
Home-Automation system.

-   openHAB is an open source system that connects to virtually any
    intelligent device, such as smoke detectors, motion detectors,
    temperature sensors, Amazon Alexa, security systems, TV/audio,
    fingerprint scanners, lighting, 1-Wire, Wemo, CUPS, DMX, KNX,
    openpaths, Bluetooth, MQTT, Z-Wave, telephony, Insteon, weather
    sensors, and web services such as Twitter, etc. openHAB also
    provides a basic Web GUI and Iphone/Android app for setting and
    dynamically viewing values. [openhab](http://www.openhab)

\'\'\'Connect your robot to the wider world\'\'\'

-   A motion detector in openHAB triggers and ROS dispatches the robot
    to the location.
-   ROS facial recognition recognizes a face at the door and openHAB
    turns on the lights and unlocks the door.
-   A Washing Machine indicates to openHAB that the load is complete and
    ROS dispatches a robot to move the laundry to the dryer.
-   A user gives a voice smart home command to Alexa. Using the
    openHAB/Amazon Alexa integration this is forwarded to ROS via the
    iot_bridge.
-   The openHAB MQTT location binding indicates that Sarah will be home
    soon and a sensor indicates that the temperature is hot. ROS
    dispatches the robot to bring Sarah\'s favorite beer. openHAB turns
    on her favorite rock music and lowers the house temperature.
-   A user clicks on the openHAB GUI on an IPAD and selects a new room
    location for the robot. The message is forwarded by the iot_bridge
    to ROS and ROS dispatches the robot.

With the iot_bridge, any openHAB device can be easily setup to publish
updates to the iot_updates topic in ROS, giving a ROS robot knowledge of
any Home Automation device. ROS can publish to the iot_set topic (or
iot_command) and the device in openHAB will be set to the new value (or
act on the specified command).

\'\'\'Different access to REST APIs of openHAB 2 and openHAB 3\'\'\'

There is a different access to the REST APIs of
[openHAB 2](https://v2.openhab/docs/configuration/restdocs.html) and
[openHAB 3](https://www.openhab/docs/configuration/restdocs.html).
Specifically, this means that the header has changed.

The iot_bridge for openHAB 2 can be found at
<https://github.com/corb555/iot_bridge>. For openHAB 3 there is a fork
at <https://github.com/Michdo93/iot_bridge>.

## Installing

1\. Install openHAB from
[openhab](https://github.com/openHAB/openHAB/wiki/Quick-Setup-an-openHAB-Server)
2. Install [iot bridge](https://github.com/corb555/iot_bridge) for
openHAB 2 or [iot bridge](https://github.com/Michdo93/iot_bridge) for
openHAB 3 on the ROS system:

-   Go to [iot bridge](https://github.com/corb555/iot_bridge) for
    openHAB 2 or [iot bridge](https://github.com/Michdo93/iot_bridge)
    for openHAB 3 and find the GIT clone address
-   On your ROS system: ```
cd catkin_ws/src
        git clone address-from-above
        cd ..
        catkin_make
```

1\. Edit iot_bridge/config/items.yaml:

-   Update host address and port to match your openHAB server

2\. Edit openHAB\'s item file

-   Create the ROS group: Group ROS (All)
-   Add the (ROS) group to each item that should send status updates to
    ROS.

Note that the items must be directly in a (ROS) group, not in a
sub-group of the (ROS) group. Note, this is only needed for status
updates to go from openHAB to ROS - you can send commands from ROS to
any openHAB item regardless of what group it is in.

. \'\'add ROS_Status to openHAB\'s item file\'\'

Sample Open_HAB item definition:

NOTE: you must have two or more items defined in the ROS group.

```
Group ROS (All)
String ROS_Status "ROS [%s]"
Switch Light_GF_Corridor_Ceiling  "Ceiling"  (GF_Corridor, Lights, ROS)
Switch Light_GF_Bathroom (GF_Bathroom, Lights, ROS)
```

## Launch

1\. Launch . `roslaunch iot_bridge iot.launch`

2\. Test:

-   Test receiving from openHAB
-   In your browser, go to <http://localhost:8080/rest/items/ROS>
-   You should see an XML response with the state of the items you have
    put in the ROS group
-   In the console, type ```
rostopic echo /iot_updates
```
-   Bring up the openHAB demo site in your browser and change an item in
    the ROS group
-   You should see the new state in the rostopic echo console
-   Test sending to openHAB ```
cd catkin_ws/src/iot_bridge/scripts
    ./iot_test  item_name item_value
```

```{=html}
<!-- -->
```
-   You should see the message logged where you did the roslaunch.
-   If you have the openHAB demo site in your browser, you should see
    the item you named changed to your specified value.
-   The value must be valid for that device (number, or ON/OFF, or
    OPEN/CLOSED). See
    [openHAB/items](https://github.com/openHAB/openHAB/wiki/Explanation-of-items)
    for a summary of valid values.

1\. Statistics

-   You can place the ROS_Status item in your openHAB sitemap. It will
    display the
-   time of the last update (to nearest minute) and counts of messages
    and errors.
-   Place the following in demo.sitemap: . ```
Text item=ROS_Status label="ROS [%s]"
```

## Interfaces

### Send a Command to an openHAB item

. \'\'\'ROS topic subscribed by iot_bridge:\'\'\' . \'\'iot_command\'\'
(diagnostic_msgs/KeyValue)

When iot_bridge receives a name/value pair from the ROS
\'\'iot_command\'\' topic, it publishes those to openHAB and openHAB
sends that command to the device specified. The value must be valid for
that device. See
[openHAB/items](https://github.com/openHAB/openHAB/wiki/Explanation-of-items)
for a summary of valid values.

For Example:

A ROS program wants to turn on a ceiling light. It publishes the
following to the \'\'iot_command\'\' topic:

-   message type: diagnostic_msgs/KeyValue
-   key: Light_GF_Corridor_Ceiling - key must match openHAB\'s .items
    file
-   value: \"ON\" (string)

This will turn on the Ground Floor Corridor ceiling light. See sample
code in iot_test.

### Set Status for an openHAB Item

. \'\'\'ROS topic subscribed by iot_bridge:\'\'\' . \'\'iot_set\'\'
(diagnostic_msgs/KeyValue)

When the iot_bridge receives a name/value pair from the ROS
\'\'iot_set\'\' topic, it publishes those to openHAB and openHAB updates
the status for the item specified (e.g. indicate that a switch is now
ON).

For Example:

A ROS program running Facial Detection detects that Sarah is present. It
publishes the following to the \'\'iot_set\'\' topic:

-   message type: diagnostic_msgs/KeyValue
-   key: \"facedetection\" - key must match openHAB\'s .items file
-   value: \"Sarah\" (string)

This will set the facedetection item in openHAB to Sarah, indicating
Sarah has been detected. See sample code in iot_test.

### Receive item updates from openHAB

. \'\'\'ROS topic published by iot_bridge:\'\'\' . \'\'iot_updates\'\'
(diagnostic_msgs/KeyValue)

The IoT bridge receives updates from openHAB and publishes those as
name/value pairs to the \'\'iot_updates\'\' ROS topic.

To see updates from the command line, type:

rostopic echo iot_updates

For example: A motion detector is triggered in openHAB. The openHAB
bridge will publish the following to the \'\'iot_updates\'\' topic in
ROS

-   message type: diagnostic_msgs/KeyValue
-   key: \"office_motion\" - key matches openHAB\'s .items file
-   value: \"1\" (string) . \'\'\'NOTE - device states are ONLY
    published to ROS when they change (or when iot_bridge is started).
    If you need the current state for ALL items in the ROS group, use
    the Request Refresh interface.\'\'\'

### Request Refresh of all Item states

\'\'\'ROS topic subscribed by iot_bridge:\'\'\'

. \'\'iot_command\'\' (diagnostic_msgs/KeyValue)

For Example:

A ROS program publishes the following to the \'\'iot_command\'\' topic:

-   message type: diagnostic_msgs/KeyValue
-   key: \"ROS_COMMAND\" - key must be added to openHAB\'s .items file
-   value: \"REFRESH\" (string)

openHAB will send the current status of every item in the (ROS) group to
the iot_updates topic. Subsequent status will continue to send only when
they change.

## An example for each item type

If you want to test e.g. ROS and openHAB, but have not yet installed the
corresponding devices and items, you can try the
[Static Examples](https://github.com/Michdo93/openhab_static_examples).
These are so-called
[unbound items](https://community.openhab.org/t/design-pattern-unbound-item-aka-virtual-item/15993)
for each
[item type](https://www.openhab.org/docs/configuration/items.html#type)
of openHAB.

## Bug Reports & Feature Requests

Use !GitHub to
[report bugs or submit feature requests.](https://github.com/corb555/iot_bridge/issues)

We appreciate the time and effort spent submitting bug reports.
