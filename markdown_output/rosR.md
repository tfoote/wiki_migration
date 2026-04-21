![](http://svn.code.sf.net/p/ivs-ros-pkg/code/trunk/rosR/misc/rosR.png)

# Overview

This package provides an simple interface of standard
ros-functionalities for the programming language R. We hope that it
might be useful to make the R capabilities for statistical analyses and
visualization also usable for the robotic community. In contrast to
other language implementations, such as rospy, rosjava, etc. this is not
a pure R implementation, it is a mixture of pure R, SWIG generated
functions, and system commands. This combination was required to
overcome some limitations of R, such as single threaded, lacking support
for sockets and handling of raw streams. Nevertheless, this package can
be used to define and use typical ROS publishers and subscribers in R,
messages are automatically and online generated from the definition
files, and it integrates the possibility to read and therefore analyse
bag-files in R. We will explain this in more detail within the next
sections.

See also [rosR_demos](rosR_demos).

# Introduction

video \... comming soon

# Installation

We divided this section into two parts. For those who come from the ROS
side, it will be probably easy to install and to use this packet (of
course they will probably have to cope with the R-code). Coming from the
R side with no experience about ROS, it will be hard to install and run
this package.

## ROS-Side

If you have already some expertise on working with ROS, then you can
install rosR just like any ordinary ros-package. Three additional
dependencies are required before you can compile it:

-   Swig3.0 is required for interfacing C code, and only swig3.0 can
    generate appropriate code for R.

```bash
$ sudo apt-get install swig3.0
```

-   The second part is an R base installation

```bash
$ sudo apt-get install r-base
```

-   r-cran-rcpp includes all required C source to develop R packages

```bash
$ sudo apt-get install r-cran-rcpp
``` Then simply download the rosR package via git
from the repository and run catkin_make.

That's all folks!

## R-Side

Within this subsection we will describe all steps that are required to
install ros-groovy under an Ubuntu 12.04 32-bit (with long time support)
and then our extension for the R-programming language (especially for
users with totally no ROS experience). The first steps were taken from
the manual (<http://www.ros.org/wiki/groovy/Installation/Ubuntu>) and we
guess, you already have installed Ubuntu on your PC.

### Preparation

First of all we will have to add the required ros-repositories.
Therefore simply copy and execute the following command in your
terminal:

```bash
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu precise main" > /etc/apt/sources.list.d/ros-latest.list'
``` And afterwards set up the keys with:

```bash
$ wget http://packages.ros.org/ros.key -O - | sudo apt-key add -
```

### Installing all Requirements

While the ROS-base installation should be sufficient enough to build and
run rosR, we strongly recommend to use the desktop-install:

```bash
$ sudo apt-get install ros-groovy-desktop
``` There are also some other things necessary:

```bash
$ sudo apt-get install r-base      # R base system
$ sudo apt-get install r-cran-rcpp # the R-development package
$ sudo apt-get install swig2.0     # to generate the ros-wrapper for R
$ sudo apt-get install subversion  # svn, to be able to download our package
```

### Environment Setup

To be able to run ROS commands and to build our package, you now will
have to set some environment parameters. So choose your preferred editor
(in our case vim) to edit the .bashrc. Insert at the end of the .bashrc
the following statements:

```bash
# to set all required variables
source /opt/ros/groovy/setup.bash
export ROS_MASTER_URI=http://localhost:11311/
# this is the path where we will install and run our local packages
export ROS_PACKAGE_PATH=$HOME/ros-projects:$ROS_PACKAGE_PATH
``` To instantiate all required variables, simply
run (this happens only once, afterwards all stuff is initialized
automatically, due to the .bashrc)

```bash
$ source ~/.bashrc
``` For sake of completeness also run the following
commands:

```bash
$ sudo rosdep init
$ rosdep update
```

### Install rosR

Now we will have to create a local directory, where we will put in all
of our local ros-packages. We already defined it within the .bashrc but
now we will have to create it:

```bash
$ sudo apt-get install r-base
```0 and step into the your newly created package
path:

```bash
$ sudo apt-get install r-base
```1 Download the rosR language extension from our
repository via svn:

```bash
$ sudo apt-get install r-base
```2 go into:

```bash
$ sudo apt-get install r-base
```3 and finaly run

```bash
$ sudo apt-get install r-base
```4 If the compilation process is finished (and
hopefully everything was okay, as in our case) you will be able to run
the first examples with

```bash
$ sudo apt-get install r-base
```5 and if you had previously installed
ros-desktop, then also the following example should work:

```bash
$ sudo apt-get install r-base
```6

# Publish Subscribe

## R--Publisher

Defining a publisher in R is nearly as simple as in Python. First of all
you will have to load this package into your R environment, what can be
done with the following command:

```bash
$ sudo apt-get install r-base
```7 This looks a bit complex, but have trust, this
is the only complex command that is required. We did not develop a
package that can be directly installed in R but more a ros package and
therefore it can be somewhere on your systems, as ros packages do it
normaly. Therefore the commandline program rospack is involved to find
the location of your rosR installation. But thats all, now you can use
all of our ros-functions in R.

As in most programs you start with the initialization of your new ros
node and so we do:

```bash
$ sudo apt-get install r-base
```8 And the new node appears\... Let us now
generate the publisher:

```bash
$ sudo apt-get install r-base
```9 Simply call ros.Publisher with the new topic,
in our case "chatter", and the message type that is transmitted
"std_msgs/String". In the same way it is also possible to define a new
message:

```bash
$ sudo apt-get install r-cran-rcpp
```0 Messages in our case are always defined as
list, that may include further list. So it is possible to set and get
messages values in a similar war, as you know you know it from other ros
language implementations:

```bash
$ sudo apt-get install r-cran-rcpp
```1 Now we can pass this message to the publisher
as follows:

```bash
$ sudo apt-get install r-cran-rcpp
```2 And that was all ... cange the content of your
message and republish it:

```bash
$ sudo apt-get install r-cran-rcpp
```3 Have look at some complete examples in folder
nodes/test/publisher.R

## R-Subscriber

Creating a subscriber is as simple creating a publisher. At first you
have to load the package, initialize the node and then create the
subscriber:

```bash
$ sudo apt-get install r-cran-rcpp
```4 As mentioned before, R is single threaded, and
calling callback functions is nearly not possible. To circumvent this
tiny drawback, you have to poll, if a new messages was received or not.
Therefore, you have to call:

```bash
$ sudo apt-get install r-cran-rcpp
```5 to fill the subscriber with possibly new
messages. The receipt of a new message can than be identified by calling
the following method:

```bash
$ sudo apt-get install r-cran-rcpp
```6 This function call will return TRUE if a new
message was received otherwise FALSE. If a new message was received,
this can simply be read with:

```bash
$ sudo apt-get install r-cran-rcpp
```7 Check out the examples in folder rosR/nodes.

## Messages

The subscriber generates automatically the correct message format. If
you publish a message it is recommended to use function:

```bash
$ sudo apt-get install r-cran-rcpp
```8 If you want to get a message of another
format, like for example a laserscan, you wil get the following result:

```bash
$ sudo apt-get install r-cran-rcpp
```9 A message in this case is always a composition
of lists, therefor single elements are accessed with "\$". Thus, the
structure of a message is quite similar to the structures in other
languages, but instead of a point, you have to use a dollar. Changing
and reading the header sequence would than be done as follows:

```bash
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu precise main" > /etc/apt/sources.list.d/ros-latest.list'
```0 The handling of arrays is a bit tricky,
because in the background these are handled as C structures std::vector.
Thus, the size of our new LaserScan is currently 0:

```bash
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu precise main" > /etc/apt/sources.list.d/ros-latest.list'
```1 and you can add new elements and read these
values in the normal manner:

```bash
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu precise main" > /etc/apt/sources.list.d/ros-latest.list'
```2 But calling functions like sum(msg\$ranges) or
median(msg\$ranges) will not work, unless you define it in file
lib/std_vector.R, or you call:

```bash
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu precise main" > /etc/apt/sources.list.d/ros-latest.list'
```3 This generates a copy of the structures within
the std::vector and returns a R vector:

```bash
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu precise main" > /etc/apt/sources.list.d/ros-latest.list'
```4 Otherwise it would slow down the conversion of
messages, just think of a camera image with 800x600 pixels with 24bits
... The handling of std::vectors in R is defined in lib/std_vector.R you
are free to add new functionality \...

# Other Functions

## Bag-Files

At the moment it is only possible to load bagfiles into R. Use therefore
the following function:

```bash
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu precise main" > /etc/apt/sources.list.d/ros-latest.list'
```5 You will receive a list, containing the
messages, the timestamps, topics, and datatypes of every message:

```bash
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu precise main" > /etc/apt/sources.list.d/ros-latest.list'
```6

## Misc

There is also other functionality defined in src/ros.cpp and lib/ros.R
like:

```bash
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu precise main" > /etc/apt/sources.list.d/ros-latest.list'
```7/
