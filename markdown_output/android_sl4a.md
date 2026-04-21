## Introduction

This package allows creating ROS nodes for Android phones. At the
current stage only Python is supported, i.e. rospy is fully working on
the phone. By running the ROS nodes in the
[SL4A](http://code.google.com/p/android-scripting/) (Scripting Layer for
Android) environment, one can access the most important Android
functions and sensor datas without great effort.

## Pre-Requirements

In order to run ROS on Android, you have to install
[Python for Android](http://code.google.com/p/python-for-android/) and
for easy API access
[Scripting Layer for Android](http://code.google.com/p/android-scripting/).

This can be done either by running our Makefile or manually:

-   **Automatic way:**\
    Please set ADB variable to your adb executable or make sure that adb
    executable is in your PATH.\
    Connect your Android device to your PC. ```
$ export ADB=~/android/android-sdk-linux_86/platform-tools/adb
 $ make python
```
    This will automatically download and install latest stable SL4A and
    Python for Android on your phone.

```{=html}
<!-- -->
```
-   **Manual way:**\
-   **Scripting Layer for Android (SL4A)**\
    In order to access Android API, we suggest installing SL4A on the
    Android phone: a. Download
    [latest stable SL4A APK](http://android-scripting.googlecode.com/files/sl4a_r3.apk)
    from <http://code.google.com/p/android-scripting/downloads/list>\
    ![1&choe=UTF-8](https://chart.googleapis.com/chart?chs=150x150&cht=qr&chl=http://android-scripting.googlecode.com/files/sl4a_r3.apk&chld=L) a.
    Install SL4A on your Android phone either by opening the APK on your
    phone using a file explorer or by installing it from the PC via
    adb:```
adb install sl4a_r3.apk
```
-   **Python for Android (Py4A)**\
    This will install Python executable, library and its most common
    modules on your Android device:\
    a. Download
    [latest stable PythonForAndroid APK](http://python-for-android.googlecode.com/files/PythonForAndroid_r5.apk)
    from <http://code.google.com/p/python-for-android/downloads/list>\
    ![1&choe=UTF-8](https://chart.googleapis.com/chart?chs=150x150&cht=qr&chl=http://python-for-android.googlecode.com/files/PythonForAndroid_r5.apk&chld=L) a.
    Install Py4A on your Android phone either by opening the APK on your
    phone using a file explorer or by installing it from the PC via
    adb:```
adb install PythonForAndroid_r5.apk
``` a. Launch *Python for Android* on your
    device and press *Install*. This will download and extract Python,
    most common Python modules and the SL4A API on the phone.\

### Verify correct installation

After the setup, Python should be ready to run on your device. You can
verify the successfull installation either by starting *SL4A* and
executing one of the Python example files or by starting Python on your
device via adb shell:\
Open up a terminal on your PC, have your Android device connected to
it.```
$ sudo adb start-server
 $ adb shell
``` Now you can work on the device's shell from
the PC and try to execute Python on it:```
PYTHONPATH=/data/data/com.googlecode.pythonforandroid/files/python/lib/python2.6/lib-dynload
PYTHONPATH=${PYTHONPATH}:/mnt/sdcard/com.googlecode.pythonforandroid/extras/python
export PYTHONPATH
export PYTHONHOME=/data/data/com.googlecode.pythonforandroid/files/python
export LD_LIBRARY_PATH=/data/data/com.googlecode.pythonforandroid/files/python/lib
/data/data/com.googlecode.pythonforandroid/files/python/bin/python
``` This
should show something like this:```
Python 2.6.2 (r262:71600, Feb 14 2011, 10:32:30) 
 [GCC 4.4.3] on linux-armv7l
 Type "help", "copyright", "credits" or "license" for more information.
 >>>
```\
\

## Get ROScore running on Android

At the moment a simple Makefile invoking adb commands takes over the
installation. In the near future, we will provide an installer that
takes over the installation of the basic ROS environment and the
depended Python modules.

Please set ADB variable to your adb executable or make sure that adb is
in your PATH. We can distinguish the installation

-   **Un-rooted Android devices** (default)\
    On unrooted phones you have to carry out the OpenCV Module Import
    manually. First install the files on your phone by running e.
    g.:```
$ export ADB=~/android/android-sdk-linux_86/platform-tools/adb
 $ make install_no_root
``` After the process has finished, you have
    to execute *Python for Android* on your mobile device and press
    *Import Module*. There you should be able to select **cv.egg**.
    After the *Success* message, you are able to run our sample ROS node
    or you can start developing your own Android ROS Nodes.\
-   **Rooted Android devices**\
    Installation on rooted phones (Hint: you will know if you have one.)
    is easier, as we can install all the files to their correct location
    automatically. You can simply run, e. g.:```
$ export ADB=~/android/android-sdk-linux_86/platform-tools/adb
 $ make install
```\
    \

## Currently supported ROS packages and Python modules

### ROS packages

The following packages are supported and automatically installed at the
moment:

-   **rospy**
-   **roslib**: Manifests are not working yet, so don't add
    *roslib.load_manifest(\...)* at the moment.
-   **std_msgs**
-   **sensor_msgs**: especially the *Image* msg
-   **geometry_msgs**
-   **cv_bridge**

Currently we only push the ROS package's Python code and messages to
the phone. But in the next few releases we will add support for
Manifest.xml and thus the installation of ROS Packages on Android will
be similar to the normal installation on the PC.\
\

### Python modules

Almost all common Python modules are now shipped directly with *Python
for Android*. We additionally install:

-   **yaml**
-   **OpenCV** (simply do *import cv*)

Attention: Some OpenCV functions may be corrupt or missing. But up to
now everything worked fine for us.

To get an impression how an Android ROS node could look like, simply
take a look at our sample ROS node (ros.py).\
\

## Run our sample ROS node (ros.py)

If no errors occurred during the installation, our provided sample ROS
node can be started.

-   Launch *SL4A*
-   Execute *ros.py*
-   Enter *ROS_MASTER_URI* (be sure to be at the same network)
    **manually**, scan a **QR-code** holding the *ROS_MASTER_URI* or
    chose an address from the history (if available). Using QR-code
    needs
    \[<https://market.android.com/details?id=com.google.zxing.client.android>
    Barcode Scanner\] installed on the Android device.\
    For generating the QR-code automatically, you can use the
    *start_roscore.sh* script in *testing*/ folder. This script depends
    on [pyqrcode](http://pyqrcode.sourceforge.net/) Python module.\
    You can also generate your own QR-code using
    [Google's Chart API](http://code.google.com/intl/de-DE/apis/chart/):```
https://chart.googleapis.com/chart?chs=150x150&cht=qr&chl=ROS_MASTER_URI&chld=L|1&choe=UTF-8
```
    replace *ROS_MASTER_URI* with your full URI e.
    g.:```
https://chart.googleapis.com/chart?chs=150x150&cht=qr&chl=http://192.168.1.100:11311&chld=L|1&choe=UTF-8
```\
    Now */android* ROS node should exists. Feel free to test the
    following topics:

**Publishers:** ```
adb install sl4a_r3.apk
```0

**Subscribers:** ```
adb install sl4a_r3.apk
```1

The image on */mobile/image* is only published after a request on
*/mobile/request_images* (std_msgs/Int16), which holds the number of
requested images.\
\

### Screenshots of the GUI

![alt ROS_MASTER_URI selection dialog at startup.\|width=200](https://vmi.lmt.ei.tum.de/projects/ros/raw-attachment/wiki/Androidinstall/ros_master_uri.png)
![alt Console output of the running ROS node.\|width=200](https://vmi.lmt.ei.tum.de/projects/ros/raw-attachment/wiki/Androidinstall/ros_py_say.png)

## Create your own ROS node

Simply develop your ROS node using *rospy* and the provided packages and
push it to SL4A's script directory on the Android device:

```
adb install sl4a_r3.apk
```2

After pushing it to the device, you can execute it directly from *SL4A*.

For interacting with the Android API, you can use the provided API from
*SL4A*:

-   SL4A API Overview:
    <http://code.google.com/p/android-scripting/wiki/AndroidFacadeAPI>
-   SL4A API Reference:
    <http://code.google.com/p/android-scripting/wiki/ApiReference>\

## Tested devices

-   HTC Desire HD with Android 2.2.1
-   Samsung Galaxy S I9000 with Android 2.2.2 and 2.3.3
-   Nexus S with Android 2.3
-   Nexus One with Android 2.2.1
-   Samsung Galaxy Tab with Android 2.2
