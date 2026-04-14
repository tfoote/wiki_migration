## Overview

A ROS node for starting and controlling a hostapd-based access point.
This node works with wifi adapters that have
[nl80211](http://linuxwireless.org/en/developers/Documentation/nl80211)-compatible
drivers which support master mode (see
[here](http://linuxwireless.org/en/users/Drivers) for more information).

## ROS API

```clearsilver
node.0 {
name=ap_hostapd_node.py
desc=`ap_hostapd_node.py` provides control of a hostapd-based access point running on a Linux network interface in master mode.

param {
group.0 {
name=Node parameters
desc=These are the startup parameters of the node.

0.name= ~interface
0.type= string
0.desc= The name of the interface that hostapd will run on (e.g. `wlan0`, `wlan1`). This parameter '''must''' be specified.

1.name= ~ip
1.type= string
1.desc= The IP address of the AP interface. If this parameter is present, then the node will also bring the interface up and assign it this IP address.
 
2.name= ~netmask
2.type= string
2.desc= The netmask to use when setting the IP of this node. 

3.name= ~hostapd_path
3.type= string
3.default= `hostapd`
3.desc= The path to the hostapd executable. This might be particulary useful, for using a non-default (i.e. newer than the one shipping with the Linux distribution) hostapd as currently only the latest versions support WMM (Wireless Multimedia Extensions).
}
group.1 {
name=Dynamically Reconfigurable Parameters
desc= Implements the dynamic_reconfigure interface defined in [[access_point_control]]. See the [[dynamic_reconfigure]] package for details on dynamically reconfigurable parameters.
0.name= ~enabled
0.default= False
0.type= bool
0.desc= Access point (i.e. hostapd) running status. Set to `True` to start access point and to `False` to stop it. Note that this is also an output parameter (the current running status of the AP - i.e. whether hostapd is currently running - will be reflected here).
1.name= ~ssid
1.default= `test`
1.type= str
1.desc=Access point essid (network name) 
2.name= ~wmm
2.default= False
2.type= bool
2.desc=Wireless multimedia extensions support 
3.name= ~mode
3.default= `b`
3.type= str
3.desc= IEEE 802.11 mode. Possible values are: `a`: 802.11a mode, `b`: 802.11b mode, `g`: 802.11g mode
4.name= ~freq
4.default= 2412000000.0
4.type= double
4.desc=Access point frequency in Hz. This needs to be both a legal IEEE 802.11 channel frequency and the channel must belog to the current mode (e.g. if setting a 5GHz frequency, the current mode has to be `a`)
5.name= ~ieee80211n
5.default= False
5.type= bool
5.desc=IEEE 802.11n support.
6.name= ~encryption_mode
6.default= open
6.type= string
6.desc=Security mode. Possible values are: `open`: no security, `wep`: WEP security, `wpa`: WPA security, `wpa2`: WPA2 security, `wpa_wpa2`: WPA or WPA2 security.
7.name= ~encryption_pass
7.type= string
7.desc=Encryption key (i.e. 10 or 26 hexadecimal digits) for WEP or passphrase for WPA. 
8.name= ~txpower_auto
8.default= True
8.type= bool
8.desc=Automatic TX power control 
9.name= ~txpower
9.default= 0
9.type= int
9.desc=TX power (dBm). Must first set `txpower_auto` to `False`.
10.name= ~bitrate
10.default= 0
10.type= int
10.desc=TX bitrate (bps). This should be a legal bitrate for the current 802.11 mode (e.g. `1000000` for `b` mode or `24000000` for `g` or `a` modes)  
11.name= ~status
11.default= OK
11.type= string
11.desc=Status of last parameter update. Possible values are: `OK`: operation successfully completed or `FAIL`: last operation failed (see `errmsg` for the reason). This parameter is '''read-only'''.
12.name= ~errmsg
12.default= 
12.type= string
12.desc=Error message if last update was not successful. This parameter is '''read-only'''.
}
}
}
```

## Usage examples

### Manual control

This is an example that shows how to set up an access point and control
its parameters using the \`reconfigure_gui\` interface.

The following launch file starts an AP node on the \`wlan0\` interface
and the \`reconfigure_gui\`:

```
<launch>
    <node name="ap_wlan0" pkg="hostapd_access_point" type="ap_hostapd_node.py">
        <param name="interface" value="wlan0"/>
        <param name="ip" value="192.168.68.1"/>
        <param name="netmask" value="255.255.255.0"/>
    </node>
    <node name="reconfigure_node" pkg="dynamic_reconfigure" type="reconfigure_gui"/>
</launch>
```

The following window will appear showing that initially the AP is not
running (the enable checkbox is unchecked):

![](attachment:reconfigure1.png)

The desired configuration is selected: mode \`a\`, channel 44, WPA
security with the chosen password, a TX power level of 8 dBm and a TX
bitrate of 24Mbit/s. Next the \`enabled\` checkbox is checked at the AP
is started:

![](attachment:reconfigure2.png)

Next, a channel in the 2.4GHz band is selected, which is illegal in
802.11a mode, thus an error message is displayed and the AP is stopped:

![](attachment:reconfigure3.png)

### AP control from Python

The hostapd access point can be controlled programatically via the
dynamic_reconfigure interface described above. The following snippet
reproduces the manual interaction from the previous section.

```
import dynamic_reconfigure.client

ap = dynamic_reconfigure.client.Client("ap_wlan0")

freq = IEEE80211_Channels.get_freq(44, IEEE80211_Channels.BAND_5000_MHz)
config = ap.update_configuration({"enabled": True, "mode": 'a', "freq": freq, "encryption_mode": "wpa", "encryption_pass": "sample_password", "txpower_auto": False, "txpower": 8, "bitrate": 24*10**6})

if config['status'] != "OK":
    raise Exception("AP failed to start: " + config['errmsg'])

freq = IEEE80211_Channels.get_freq(1, IEEE80211_Channels.BAND_2400_MHz)
config = ap.update_configuration({"freq": freq})

if config['status'] != "OK":
    raise Exception("AP failed to start: " + config['errmsg'])
```

## Command-line tools

### find_hwsim_iface.py

This script is useful for setting up a \`mac80211_hwsim\`-based setup.
mac80211_hwsim is a 802.11 radio simulator. The script takes two
parameters:

-   \`radio index\`
-   \`total number of radios\`

If the mac80211_hwsim is not loaded or if the number of radios it has
currently spawned is smaller than \`total number of radios\` then it is
re-loaded with the proper radio count. The script prints to its output
the name of the \`radio index\`-th interface.

For example (this is taken from a real setup), suppose that the system
has a real wireless interface with name \`wlan1\` and we need to spawn
three virtual interfaces. Their names will be \`wlan0\`, \`wlan1\` and
\`wlan2\`.

Using \`find_hwsim_iface.py\`:

```
$ echo `rosrun hostapd_access_point find_hwsim_iface.py 1 3`
wlan0
$ echo `rosrun hostapd_access_point find_hwsim_iface.py 2 3`
wlan1
$ echo `rosrun hostapd_access_point find_hwsim_iface.py 3 3`
wlan1
```

The script can be used to launch nodes on the \'\'n-th virtual
interface\'\' with roslaunch. The following example, launches two nodes
on the first and second mac80211_hwsim interfaces while ensuring that
there are at least three total interfaces:

```
<launch>
    <node name="ap1" pkg="hostapd_access_point" type="ap_hostapd_node.py">
        <param name="interface" command="$(find hostapd_access_point)/scripts/find_hwsim_iface.py 1 3"/>
    </node>

    <node name="ap2" pkg="hostapd_access_point" type="ap_hostapd_node.py">
        <param name="interface" command="$(find hostapd_access_point)/scripts/find_hwsim_iface.py 2 3"/>
    </node>
</launch>
```

### hwsim_nat_setup.sh

This script sets up NAT routes and ARP entries so that packets can be
sent \"over-the-air\" between two interfaces connected to the same host.
By default, packets addressed to the IP of a local interface get sent
over the local route.

The script takes six parameters:

-   first interface name (e.g. \`wlan0\`)
-   first interface real IP address
-   first interface fake IP address (pinging this address will send
    packets over-the-air with the second interface as the source and the
    first interface as the destination)
-   second interface name
-   second interface real IP
-   second interface fake IP

An example:

```
# rosrun hostapd_access_point hwsim_nat_setup.sh wlan0 192.168.68.1 192.168.69.1 wlan1 192.168.69.2 192.168.68.2

# ifconfig wlan0
wlan0     Link encap:Ethernet  HWaddr 02:00:00:00:00:00  
          inet addr:192.168.68.1  Bcast:192.168.68.255  Mask:255.255.255.0

# ifconfig wlan1
wlan1     Link encap:Ethernet  HWaddr 02:00:00:00:01:00  
          inet addr:192.168.69.2  Bcast:192.168.69.255  Mask:255.255.255.0
```

A packet with destination IP 192.168.69.1 will travel \"over-the-air\"
from wlan1 to wlan0, while packets with destination IP 192.168.68.2 will
travel from wlan0 to wlan1.

\'\'\'Known problems\'\'\':

-   starting hostapd on an interface flushes the ARP entries so the
    \`hwsim_nat_setup.sh\` needs to be run again each time hostapd is
    restarted
-   care should be taken if ifb-devices are present on the system (most
    likely these would be the result of using ingress traffic control
    with \`network_traffic_control\`) as these seem to steal the ARP
    entries

## Tips and known bugs

-   The \`ap_hostapd_node.py\` as well as the scripts in this package
    need super-user privileges. It\'s probably easiest if everything is
    ran as root.
-   Note that if a change in configuration fails, hostapd will be
    stopped and remain stopped, until restarted with a good
    configuration. Each time the configuration of the AP is updated the
    success status should be checked.
-   WEP mode does not work with mac80211_hwsim interfaces (open and
    WPA/WPA2 do)
-   Upon exit, the node sends a SIGTERM signal to hostapd and waits for
    10 seconds for the daemon to exit after which it sends it a SIGKILL
    signal. This should never happen as 10 seconds is plenty of time.
    However should this happen, SIGKILL-ing hostapd seems to render the
    monitor interface in a strange state so reload of the driver module
    is needed.
