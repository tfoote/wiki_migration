## About

The \`rovio_av\` package contains nodes and launch files that can be
used to stream video and play sounds on the Rovio. Additionally,
included in the \`rovio_av\` package is a selection of \`.wav\` files
that have been converted to 8000 Hz 16 bit PCM (the native format for
the Rovio). These files are conversions from Willow Garage\'s
[Robot Sound Libraries](http://hri.willowgarage.com/sounds/). These
sounds can then be sent to the Rovio via a service call and played on
its internal speakers.

## Nodes

```clearsilver
node.0 {
  name = rovio_audio
  desc = `rovio_audio` can be used to play 8000 Hz 16 bit PCM `.wav` files on the Rovio. Additionally, included in the [[rovio_av]] package is a selection of `.wav` files (located in the `wav` directory) that have been converted to 8000 Hz 16 bit PCM (the native format for the Rovio). These files are conversions from Willow Garage's [[http://hri.willowgarage.com/sounds/|Robot Sound Libraries]].
  srv {
    0.name = wav_play
    0.type = rovio_shared/wav_play
    0.desc = Send the given file (given as the absolute file name) to the Rovio to play.
  }
  param {
    0.name = /rovio_shared/host
    0.type = `string`
    0.desc = Hostname used to communicate with the Rovio.
    1.name = /rovio_shared/user
    1.type = `string`
    1.desc = Username used to authenticate with the Rovio.
    2.name = /rovio_shared/pass
    2.type = `string`
    2.desc = Password used to authenticate with the Rovio.
  }
}
```

## Installation

To install the \`rovio\` stack, you can choose to either install from
source, or from the Ubuntu package:

### Source

To install from source, execute the following: ```shell
cd /path/to/your/ros/stacks
git clone https://github.com/WPI-RAIL/rovio.git
roscd rovio
rosdep install rovio
rosmake rovio
```

### Ubuntu Package

To install the Ubuntu package, execute the following:
```
sudo apt-get install ros-fuerte-rovio
```

### Startup

The \`rovio_av\` package contains a \`rovio_av.launch\` file which
should be edited with the hostname, username and password to login to
your Rovio. Additionally, the username, password, and host should be
changed in the \`GSCAM_CONFIG\` variable in order to stream video using
[gscam](gscam). This file launches an instance of the \`rovio_audio\`
and \`gscam\` nodes. To launch these nodes, the following command can be
used:

```
roslaunch rovio_av rovio_av.launch
```

With the above nodes running, you can test video streaming with the
[image_view](image_view) package using the following command:

```
rosrun image_view image_view image:=/gscam/image_raw
```

Additionally, an example to test the audio service is the following
command:

```
rosservice call /wav_play /path/to/rovio/rovio_av/wav/G22.wav
```

## Support

Please send bug reports to the
[GitHub Issue Tracker](https://github.com/WPI-RAIL/rovio/issues). Feel
free to contact me at any point with questions and comments.

-   [Russell Toris](Russell Toris)
-   <rctoris@wpi.edu>
-   [Academic Website](http://users.wpi.edu/~rctoris/)

------------------------------------------------------------------------

  -- ------------------------------------------------- -- ---------- -- -------------------------- --
     \<tablewidth=\"100%\"\> ![](attachment:wpi.png)      \<:99%\>      ![](attachment:rail.png)   
  -- ------------------------------------------------- -- ---------- -- -------------------------- --
