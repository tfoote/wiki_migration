## About

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------------------------- --
     <tablewidth="100%" tablestyle="text-align:left">The `rms_rovio_environment` package contains launch files that can launch an example RMS environment for use with the [rms](rms). These files will launch the appropriate nodes to control and query the Rovio and start appropriate server nodes (e.g., [rosbridge_server](rosbridge_server)).      ![](attachment:rovio.png)   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------------------------- --

## Installation

To install the `rms_rovio_environment` stack, you can choose to either
install from source, or from the Ubuntu package:

### Source

To install from source, execute the following: ```shell
cd /path/to/your/ros/stacks
git clone https://github.com/WPI-RAIL/rms_rovio_environment.git
roscd rms_rovio_environment
rosdep install rms_rovio_environment
rosmake rms_rovio_environment
```

### Ubuntu Package

To install the Ubuntu package, execute the following:
```
sudo apt-get install ros-fuerte-rms-rovio-environment
```

### Startup

A launch file is included to launch the appropriate nodes to control the
Rovio and accept remote client connections. In order to run this server,
the launch files in the [rovio_ctrl](rovio_ctrl) and
[rovio_av](rovio_av) packages must be configured to work with your
Rovio. Refer to the documentation provided on the their respective wiki
pages to do so. When finished, you can launch the RMS environment server
with the following command:

```
roslaunch rms_rovio_environment rms_rovio_environment.launch
```

## Tutorials

More detailed instructions are provided for installing, setting up, and
running an instance of the Rovio RMS Environment server. For more
information, start with the following tutorial:

A full list of all RMS related tutorials is provided on the [rms](rms)
stack page.

## Support

Please send bug reports to the
[GitHub Issue Tracker](https://github.com/WPI-RAIL/rms_rovio_environment/issues).
Feel free to contact me at any point with questions and comments.

-   [Russell Toris](Russell Toris)
-   <rctoris@wpi.edu>
-   [Academic Website](http://users.wpi.edu/~rctoris/)

------------------------------------------------------------------------

  -- ------------------------------------------------- -- ---------- -- -------------------------- --
     <tablewidth="100%"> ![](attachment:wpi.png)      <:99%>      ![](attachment:rail.png)   
  -- ------------------------------------------------- -- ---------- -- -------------------------- --
