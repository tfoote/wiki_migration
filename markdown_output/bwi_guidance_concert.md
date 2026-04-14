This package wraps a Human-Robot Interaction Experiment conducted at the
Univesity of Texas At Austin. The results from this experiment were
reported in the following symposium paper: Piyush Khandelwal and Peter
Stone. Multi-robot Human Guidance using Topological Graphs. In AAAI
Spring 2014 Symposium on Qualitative Representations for Robots
(AAAI-SSS), March 2014.
([pdf](http://www.aaai.org/ocs/index.php/SSS/SSS14/paper/viewFile/7726/7699))

The \`bwi_guidance_concert\` package wraps this experiment to use the
[Robotics in Concert](rocon) framework.

## Overview

The goal of the multi-robot guidance project is to allow an automated
system to efficiently guide a person unfamiliar with the environment to
their goal using multiple robots. In the experiment available through
this package, a single controller decides where to position robots in
the environment and what direction should be displayed on each robot\'s
screen to guide the person.

This package currently wraps preliminary work on this project, where a
central positioner node teleports each robot to a desired location using
Gazebo\'s \`set_model_state\` service. Additionally, each robot
subscribes to an image stream which is displayed on its simulated robot
screen (ex. \'/robot1/image\'), and these images are also published by
the positioner.

Apart from the positioner node, an experiment controller node decides
which exact problem the user is facing, and a server node keeps track of
which user is interfacing with the system. A user controls a human
avatar inside the simulator using a web based GUI that talks to the rest
of the system using [rosbridge_suite](rosbridge_suite).

The workflow of the system is as follows:

-   Initially, we start a concert with the server node which accepts new
    users using the web interface.
-   When a new user arrives and locks the server (preventing other users
    from connecting to the experiment until this lock is relinquished),
    the server internally starts gazebo, the positioner node and the
    experiment controller node within the service. In order to spawn all
    the robots, a wrapper around
    [concert_service_segbot_gazebo](concert_service_segbot_gazebo) is
    used, although all of these modules are loaded using
    [roslaunch](roslaunch).
-   10 concert clients are loaded (1 for each robot). No topics are
    flipped to these concerts since these topics eventually need to be
    used locally, and without topic remapping and subscribers behaving
    poorly when subscribed to multiple masters
    ([#127](https://github.com/robotics-in-concert/rocon_multimaster/issues/127)),
    it is typically a bad idea to flip these topics. Please note that
    when we move to the next version of the research, where robots use
    the standard navigation stack to navigate into place, none of the
    topics flipped will be required locally and the system can work as
    intended.
-   A dummy app is run on each concert (empty launch and interface
    file), just to demonstrate how robots will be used in the next stage
    of research.
-   At this time, the user runs through a series of experiments, data is
    collected and compiled into results.

## Installation

-   Follow the instructions at
    [segbot_gazebo_concert#Installation](segbot_gazebo_concert#Installation)
    to install all the base code required by this package.
-   Additionally, you\'ll need to install a web server. This package has
    only been tested using the apache web server:
    ```
sudo apt-get install apache2
```
-   Next, install the following rosinstall entry. You may already have
    some of these packages if you\'ve already installed the
    [segbot_gazebo_concert](segbot_gazebo_concert) demo. A patched
    version of rosbridge is used here
    ([#104](https://github.com/RobotWebTools/rosbridge_suite/issues/104))
    ```
- git: {local-name: segbot_rocon, uri: 'https://github.com/utexas-bwi/segbot_rocon.git', version: master}
- git: {local-name: bwi_guidance, uri: 'https://github.com/utexas-bwi/bwi_guidance.git', version: master}
- git: {local-name: rl_pursuit, uri: 'https://github.com/utexas-bwi/rl_pursuit.git', version: master}
- git: {local-name: rosbridge_suite, uri: 'https://github.com/piyushk/rosbridge_suite.git', version: patch-1}
```
-   You\'ll need to copy/symlink the necessary files so that they can be
    displayed by the webserver. If you\'ve got home directory encryption
    enabled, then the following command won\'t work and you\'ll have to
    copy the files. The following command also assumes standard
    installation with the web home directory being \`/var/www\`.
    ```
sudo ln -sf `rospack find bwi_guidance`/www /var/www/exp1
```
-   Finally, you\'ll need to copy some data files to the bwi_guidance
    package which are required by the experiment:
    ```
roscd bwi_guidance_solver/data/exp2/cache
wget http://cs.utexas.edu/~piyushk/share/vi.tar.gz
tar xvzf vi.tar.gz
rm vi.tar.gz
```

## Running the code

### Command Line Execution

The following commands need to be run on a reasonably powerful machine
(Recommended: Quad Core i7 Processor) that can also run Gazebo.

#### Non-Concert Version

```
roslaunch bwi_guidance_solver server.launch --screen
```

#### Concert Version

```
rocon_launch bwi_guidance_concert guidance.concert --screen
```

### Running the User Interface

The user interface can be run on any browser that can connect to the
machine on which the software was run. The connection is made using the
rosbridge library over websockets.

Typically, you\'ll have to type the following link into the web-browser
to launch the user side GUI. This link will only work on the machine
from where you ran the command line application.
```
http://localhost/exp1/index.html
```

If you want to run on a different machine, you\'ll have to supply the
hostname/IP of the machine where the command line application ran, so
that your browser knows to connect to it: ```
http://robot-devil.csres.utexas.edu/exp1/index.html?host=robot-devil.csres.utexas.edu
```

Additionally, if you\'re running the concert version of the demo,
you\'ll have to supply an additional parameters:
```
http://robot-devil.csres.utexas.edu/exp1/index.html?host=robot-devil.csres.utexas.edu&concert=true
```

A convenience webpage where you can enter this information and get
redirected to the correct link is available at: ```
http://robot-devil.csres.utexas.edu/exp1/link.html
```

Once you get to the \`index.html\` page, follow the instructions to run
through the experiment!
