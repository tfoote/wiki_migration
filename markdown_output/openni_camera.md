## Use Kinect on Ubuntu with OpenNI

Note: This is the \'\'\'prerequisite\'\'\' for your usage of
openni_camera / openni_launch for Kinect in ROS. You have to firstly
install the Driver for Kinect on Ubuntu and make sure your kinect can
work properly on ubuntu.

To get started, please Refer
[this blog](http://www.20papercups.net/programming/kinect-on-ubuntu-with-openni/)
and you may meet some incompatible contents, do not worry, the thought
and path is correct.

The very important doc you should read carefully is that on
[OpenNI\'s GitHub site](https://github.com/OpenNI/OpenNI/blob/master/README)
and that on
[SensorKinect GitHub site](https://github.com/avin2/SensorKinect/blob/unstable/README).

-   The Core thing for this is Installing Driver for Kinect on Ubuntu.
    The two important packages you should install are: The OpenNI
    UNSTABLE version The SensorKinect package

```{=html}
<!-- -->
```
-   Here, I want to say that: after you have installed the OpenNI, and
    be ready to clone the git files for SensorKinect,DO NOT change
    directory!Otherwise you cannot generate the Redist directory for
    installation of SensorKinect.

```{=html}
<!-- -->
```
-   The Cloning process could be very slow, you can checkout the files
    from here: <http://yunpan.cn/cmTPmvr2D29Yj> keycode: 32e4

```{=html}
<!-- -->
```
-   There existed a Readme.txt file which is wriiten in Chinese. Don\'t
    worry, you can ignore it after you suffer this Installation for
    longer than 1 week cuz you will be the expert on this field at that
    time. ;-)

```{=html}
<!-- -->
```
-   When you succeded in using Kinect_for_Windows on Ubuntu, the using
    of Kinect_for_Xbox is just \'unplug and plugin\'.

```{=html}
<!-- -->
```
-   It\'s really easier if you use Kinect_for_XBox with OpenKinect.
    unfortunately, OpenKinect does not support Kinect4Windows.

```{=html}
<!-- -->
```
-   If you\'re using Virtual Machine launching Ubuntu on it, I don\'t
    recommend you continue. I failed too many times in trying to do it
    on VMs. And finally I succeded in real machine.

```{=html}
<!-- -->
```
-   Read Carefully about This Blog:
    [this blog](http://www.20papercups.net/programming/kinect-on-ubuntu-with-openni/).
    and follow it. Good luck!
