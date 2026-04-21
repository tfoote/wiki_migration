## Overview

This package implements the [access_point_control](access_point_control)
dynamic_reconfigure interface for controlling an access point for
Linksys access points.

### Compatible models

Tested compatible models are WRT610Nv2 and WRT310N. Any model that uses
the same web interface should work.

### Known issues

The following is a list of known issues with implementing the
access_point_control API for the Linksys web interface:

-   the Linksys models mentioned previously do not support automatic TX
    power control so the `txpower_auto` parameter should be set to
    `False`
-   the Linksys AP models do not support the WPA and WPA2 simultaneous
    security mode
-   after resetting the Linksys AP configuration (using the reset button
    on the AP), the `Manual` mode should be selected in the web
    interface under `Wireless/Basic Wireless Settings` (by default,
    the `Wi-Fi Protected Setup` mode is selected)
-   configuration updates are quite slow (5-10 seconds) due to the
    web-based interface
-   if a configuration parameter is rejected by the access point (e.g.
    an invalid channel) the AP reverts to the old setting; this is also
    reflected in the configuration returned by
    `update_configuration()`
-   the `wmm` parameter is shared between the 2.4 and 5GHz interface
    so setting it for one interface will cause it to be set for the
    other as well
-   the dynamic_reconfigure interface supports three modes, `a`, `b`
    and `g` and a boolean that specifies whether `n` mode should be
    enabled or not. These modes are mapped to those provided by the
    Linksys web interface as:
-   `a` <\-\--> `a-only`
-   `a` + `n` <\-\--> `mixed`
-   `b` <\-\--> `b-only`
-   `b` + `n` <\-\--> **should not be used** in order to keep the
    mapping bijective
-   `g` <\-\--> `g-only`
-   `g` + `n` <\-\--> `mixed`

## ROS API



```clearsilver
node.0 {
name=linksys_apcontrol_node.py
desc=`linksys_apcontrol_node.py` provides control of Linksys access point.
}
param {
group.0 {
name=Node parameters
desc=These are the startup parameters of the node.

0.name= ~interface
0.type= string
0.default= `wl0` (2.4GHz)
0.desc= The name of the interface that the node will control. Usually this is `wl0` for the 2.4GHz interface and `wl1` for the 5GHz. This parameter '''must''' be specified.

1.name= ~ip
1.type= string
1.default = `192.168.1.1`
1.desc= The IP address through which the AP web interface can be accessed.
 
2.name= ~user
2.type= string
2.default = empty string
2.desc= The admin user name. 

3.name= ~password
3.default= `admin`
3.type= string
3.desc= The admin password.
}
group.1 {
name=Dynamically Reconfigurable Parameters
desc=See the [[hostapd_access_point]] documentation for a full description. For a general discussion of dynamically reconfigurable parameters, see the [[dynamic_reconfigure]] package.
}
}
}
```


