## About

The `rovio_shared` package contains a library that is used to
communicate with the Rovio. This package and library are intended to be
used with the packages provided in the [rovio](rovio) stack; however, it
is possible to compile and use the library in your own packages as well.

<<MsgSrvDoc(rovio_shared)>>

## Installation

To install the `rovio` stack, you can choose to either install from
source, or from the Ubuntu package:

### Source

To install from source, execute the following: 

```shell
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



## Library Example

While the `rovio_http` library was constructed primarily for use
within the `rovio` stack's packages, it is possible to utilize its
functionality in any ROS node.

The example below has the Rovio drive forwards until the user issues a
`ctrl-c` command. Other information on the `rovio_http` library can
be found in the [API](http://www.ros.org/doc/api/rovio_shared/html/).

### The C++ Code



```cplusplus
/*
 * A simple example that utilizes the rovio_http library from the
 * rovio_shared package.
 *
 * Author: Russell Toris - rctoris@wpi.edu
 *
 * Version: September 1, 2011
 */

#include <ros/ros.h>
#include <rovio_shared/rovio_http.h>

int main(int argc, char **argv)
{
  // initialize ROS and the node
  ros::init(argc, argv, "rovio_http_example");
  ros::NodeHandle node;

  // create the rovio_http object to talk to Rovio
  rovio_http rovio("admin", "your_password");

  // update at 5 Hz
  ros::Rate loop_rate(5);
  // continue until a ctrl-c has occurred
  while (ros::ok())
  {
    // always good practice to spin in a loop
    ros::spinOnce();

    // send a command to move forwards
    rovio_response *resp = rovio.send(
        "http://192.168.1.110/rev.cgi?Cmd=nav&action=18&drive=1&speed=5");
    // print out the response
    ROS_INFO("%s", resp->data);
    // always free the response once we are done with it
    free(resp);

    // wait for the timer
    loop_rate.sleep();
  }
}
```



### Code Explanation

Now that we have a running example, let's look at each piece.

In order to utilize the rovio_http library in ROS, we must import the
both the standard ROS and rovio_http library headers.

Create and initialize your ROS node as with any other ROS node.

Create a `rovio_http` object by supplying it with the username and
password to your Rovio. This object with use `libcurl` to communicate
to the Rovio's HTTP server.

In this example we enter a loop that runs at 5 Hz.

Even though we do not have any topics or services, it is still good
practice to spin inside of the main loop in a node.

Here we construct and send an HTTP command based on the
[Rovio API](http://www.wowwee.com/static/support/rovio/manuals/Rovio_API_Specifications_v1.2.pdf).
In this example we will tell to Rovio to drive forwards at speed 5. This
function will return a pointer to a 'rovio_response' struct containing
the response from the Rovio. Even if this information is not need it is
important to always free this struct once you are finished to prevent a
memory leak.

Once the command has been sent we wait for the ROS timer to go off
before continuing.

## Support

Please send bug reports to the
[GitHub Issue Tracker](https://github.com/WPI-RAIL/rovio/issues). Feel
free to contact me at any point with questions and comments.

-   [Russell Toris](Russell Toris)
-   <rctoris@wpi.edu>
-   [Academic Website](http://users.wpi.edu/~rctoris/)

------------------------------------------------------------------------

  -- ------------------------------------------------- -- ---------- -- -------------------------- --
     <tablewidth="100%"> ![](attachment:wpi.png)      <:99%>      ![](attachment:rail.png)   
  -- ------------------------------------------------- -- ---------- -- -------------------------- --
