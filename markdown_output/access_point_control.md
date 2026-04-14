## ROS API

The following dynamic_reconfigure API must be implemented by packages
specific to access point model such as
[hostapd_access_point](hostapd_access_point),
[linksys_access_point](linksys_access_point),
[ddwrt_access_point](ddwrt_access_point).

```clearsilver

param {

name=Dynamically Reconfigurable Parameters
desc=  See the [[dynamic_reconfigure]] package for details on dynamically reconfigurable parameters.
0.name= ~enabled
0.default= False
0.type= bool
0.desc= Access point running status. Set to `True` to start access point and to `False` to stop it. Note that this is also an output parameter (the current running status of the AP will be reflected here).
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
```
