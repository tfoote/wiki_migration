NOTE: Package is deprecated. Only works with ROS Diamondback and below
with Ubuntu 12.04 and below

[Youtube](https://www.youtube.com/watch?v=lIZVWqixcL8)

NOTE: Those interested in the ROAR training/testing dataset can find it
[here](ftp://hapticsnas.seas.upenn.edu/permanent/roar_tests.zip).

![center](attachment:roar_spec.png)

## Overview

The ROAR package contains a set of GUI and command line tools to allow
you to easily create simple models of audio events, and then attempt to
detect these events later in your own software.

Currently ROAR uses popular techniques (spectral analysis and noise
reduction, PLP coefficients, One-Class SVMs) for categorizing short-time
audio clips. As such, ROAR is good at learning and detecting unique
sound samples that last roughly 100 milliseconds. For example, the ring
of a doorbell or the click of a button. ROAR was not designed to
distinguish between long-time audio clips, such as two different songs
or different words of human speech. However, most longer audio segments
contain smaller distinct clips, and it is possible to train on these
events.

It is written using python interfaces to the
[ ALSA sound library](http://www.alsa-project.org/main/index.php/Main_Page)
(the default sound standard in most Linux distributions), so, if your
microphone works in Linux chances are it will work with ROAR.

## Hardware

The first step in using ROAR is to obtain a proper microphone and ensure
it is functioning properly.

### Recommended Microphones

All [ALSA](http://www.alsa-project.org/main/index.php/Main_Page)
compatible microphones work with ROAR. When doing precise audio
detection it is best to pick a microphone that has a clear crisp
response. Directional microphones work very well, but tend to perform
poorly if you move away from their \"sweet spot\". A few microphones we
have personally tested include the
[Samson C01U](http://www.samsontech.com/products/productpage.cfm?prodid=1810),
the [ Roland UA-25ex](http://www.roland.com/products/en/UA-25EX/ ), and
the
[MXL AC-404](http://www.mxlmics.com/products/web_conferencing/AC-404/AC-404.html).
We recommend the AC-404 as a good starter microphone, since it has a
nice crisp response for almost 180 degrees in front of the mic.

### Creating PR2 Ears

We used the
[MXL AC-404](http://www.mxlmics.com/products/web_conferencing/AC-404/AC-404.html)
microphone to create two ears for our PR2 robot. Details for reproducing
our hardware/software setup can be found on the
[ PR2 Hardware Modifications page ](Robots/PR2/HardwareMods).

You should also change roar/launch/audio_parameters.yaml audio_card line
to read: ```
audio_card: plug:left_ear
```

### ALSA Configuration

None of the ROAR software will work properly unless you enable your
computers microphone input (duh). Each microphone is a little different,
so it is hard to give generic instructions,but here are a few tips:

-   **The microphone input channel used by ROAR can be configured in the
    launch/audio_parameters.yaml file. It\'s default setting is
    \'default\', your computers default microphone channel input**. To
    find out what other options you have on your computer try typing
    \'aplay -l\' on the command line.
-   For USB microphones:
    <http://wiki.audacityteam.org/index.php?title=USB_mic_on_Linux>
-   Generic ALSA configuration info:
    <http://www.volkerschatz.com/noise/alsa.html>
-   Here are some tips on setting up a asound.conf file:
    <http://alsa.opensrc.org/.asoundrc> Generally, when you can record
    using gnome-sound-recorder, then you\'ve got the microphone setup
    properly. You may want to store these settings or load some settings
    you previously stored with. ```
alsactl -f ~/roar_microphone.state store
alsactl -f ~/roar_microphone.state restore
```

## Software

For the smoothest programming experience it is highly recommended you
use Ubuntu 10.04 or greater. ROAR depends on several external packages
that can be found in the [roar_stack](roar_stack) rosdep.yaml file. If
these dependencies are satisfied ROAR should run fine on any
distribution, but they currently remain untested.

### Downloading ROAR

The proper way to aquire the ROAR software is to download the entire
stack to the folder of your choosing (below we download to /ros):
```
svn co https://mediabox.grasp.upenn.edu/svn/penn-ros-pkgs/roar_stack/trunk ~/ros/roar_stack
``` If /ros isn\'t already on your ROS_PACKAGE_PATH
you will need to add it by typing the following before continuing with
the installation: ```
export ROS_PACKAGE_PATH=~/ros:${ROS_PACKAGE_PATH}
```

### Compiling ROAR

To compile the ROAR stack you should build the roar package. Make sure
to use the \--rosdep-install flag, which will install the external
dependencies for Ubuntu (NOTE: You will need super-user permissions to
install packages to the system properly!): ```
rosmake roar --rosdep-install
```

### Running ROAR

There are two different parts to running ROAR. The trainer and the
detector. You will use the trainer when you want to make a model of a
new sound. You will use the detector when you want to detect that sound
later in real-time. You can get detailed instructions on each step by
following the tutorials below:

[ Trainer Tutorial](roar/Tutorials/Trainer )

[ Detector Tutorial](roar/Tutorials/Detector )
