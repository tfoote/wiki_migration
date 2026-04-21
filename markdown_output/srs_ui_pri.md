## INSTALL

This shows how to install srs ui pri (srs_ui_pri). 1. Add srs.ipa to
iTunes

2\. Sync your iPad with iTunes.

## CONFIGURATION

Go to Settings app and select SRS

1\. In Remote Host enter 

```
ws://IP:9090
```

 where IP is the IP
address of the machine you are running rosbridge and
[srs_decision_making](srs_decision_making)

2\. In the Video feed 1 enter 

```
http://IP:8080/stream?topic=/stereo/left/image_raw
```

 3. In the Video
feed 2 enter 

```
http://IP:8080/stream?topic=/stereo/right/image_raw
```



4\. Dynamic joysticks means whether the joystick can be moved around by
touching longer on the place where you want to move the joystic to

5\. Auto hide means whether joystick will fade out after it is released.

6\. Hand manipulation means whether hand controls will show up in the
Manual Control view

7\. In the Map Server enter the following 

```
http://IP:8080/snapshot?topic=/map
```



## Usage/Examples

1\. Start [srs_scenarios](srs_scenarios)

2\. Start the topics for UI_PRI error handling (mendatory)
[srs_scenarios](srs_scenarios)

3\. Start [srs_mixed_reality_server](srs_mixed_reality_server)

4\. Start rosbridge



```
rosrun rosbridge rosbridge.py
```



4\. Start the app on your iPad
