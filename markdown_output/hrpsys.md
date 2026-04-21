[Included page Industrial/Software_Status/Developmental not found](Included page Industrial/Software_Status/Developmental not found)

## Robots compatible to hrpsys

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ------------------------------------------------------------------------------------- --
     [![HRP2\|height=175](https://unit.aist.go.jp/is/humanoid/m_projects/img/HRP-2_Pose2.jpg)](https://unit.aist.go.jp/is/humanoid/m_projects/img/HRP-2_Pose2.jpg)                                                         [HRP2](http://global.kawada.jp/mechatronics/hrp2.html), (DRC2015 contender. ROS package not disclosed)                                                                                            [![HRP4 Miim\|height=175](http://www.pinktentacle.com/images/hrp_4c_4.jpg)](http://www.pinktentacle.com/images/hrp_4c_4.jpg)                                                                 [HRP4](http://global.kawada.jp/mechatronics/hrp4.html), (ROS package not disclosed)   
     [![NEXTAGE OPEN\|height=125](http://i.i.cbsi.com/cnwk.1d/i/tim/2011/11/09/Nextage1.JPG)](http://i.i.cbsi.com/cnwk.1d/i/tim/2011/11/09/Nextage1.JPG)                                                                   [NEXTAGE OPEN](http://nextage.kawada.jp/en/) ([ROS pkg](rtmros_nextage)                                                                                                                           [![Schaft\|height=125](http://spectrum.ieee.org/img/SCHAFT-robot-japan-humanoid-620-1365622921766.png)](http://spectrum.ieee.org/img/SCHAFT-robot-japan-humanoid-620-1365622921766.png)      [Schaft](http://schaft-inc.jp/?lang=en), (DRC Trial 2013 winner)                      
     [![Atlas on Gazebo\|height=125](http://wiki.ros.org/gazebo_ros_pkgs?action=AttachFile&do=get&target=VRC_Hose_Atlas.jpg)](http://wiki.ros.org/gazebo_ros_pkgs?action=AttachFile&do=get&target=VRC_Hose_Atlas.jpg)      [Atlas](http://www.bostondynamics.com/robot_Atlas.html) on [gazebo](gazebo), [Gazebo pkg](https://code.google.com/p/rtm-ros-robotics/source/browse/trunk/rtmros_gazebo/hrpsys_gazebo_atlas/)      [![JAXON\|height=125](http://www.theroboticschallenge.org/sites/default/files/NEDO-JSK_JAXON.png)](http://www.theroboticschallenge.org/sites/default/files/NEDO-JSK_JAXON.png)               [JAXON](http://www.theroboticschallenge.org/finalist/nedo) (DRC2015 contender)        
     [![AERO\|height=125](http://www.theroboticschallenge.org/sites/default/files/AeroDRC_main.png)](http://www.theroboticschallenge.org/sites/default/files/AeroDRC_main.png)                                             [AERO](http://www.theroboticschallenge.org/finalist/aero) (DRC2015 contender)                                                                                                                                                                                                                                                                                                                                                                                                        
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ------------------------------------------------------------------------------------- --

## Documentation

-   API documentation is
    [available on github](http://fkanehiro.github.io/hrpsys-base/).
-   For writing application, you can use some existing resource from one
    of the client packages of \`hrpsys\`,
    [rtmros_hironx](http://wiki.ros.org/rtmros_nextage/Tutorials/Programming)

### Notable features

-   Real-time capable utilizing OS feature
-   Rich interface for kinematic operation
-   Manipulator operation by the pose of end-effector (EEF linear
    interpolation)
-   Manipulation by passing the set of joint angles (joint angle
    interpolation)
-   2 interpolation options; linear / minimum jerk
-   Preemptive kinematic operation (canceleable and modifyable)
-   Preemption can be disabled
-   Plugins
-   EEF compliance control plugin (using on force-torque sensor)
-   EEF virtual force computation plugin (using joint torque values)
-   Joint protection plugin
-   Self interference detection plugin
-   Servo module hand plugin
-   Proven operational history
-   Development has been active over years at institutes such as the
    original developer [AIST](http://aist.go.jp/) (National Institute of
    Advanced Industrial Science and Technology in Japan),
    [JSK Lab at U-Tokyo](http://jsk.t.u-tokyo.ac.jp/).
-   Dozens of thousands of operational time
-   Number of robots are running atop
-   Include 5 DRC contender robots (2013 and 2015)
-   See above for the incomplete list of the hrpsys-based robots
-   Active development status; 73 commits during month of June 2015 made
    by 5 authors

## Community

-   Mailing list: <http://groups.google.com/d/forum/rtm-ros-robotics>
-   [Issues, feature  requests](https://github.com/start-jsk/hrpsys/issues?direction=desc&sort=updated&state=open).

## For developer

### Steps to release a new version

As a 3rd party package to ROS we need some extra chores to release.
Discussed
[here](https://github.com/start-jsk/hrpsys/pull/99#issuecomment-49831482).
NOTE for 2 different repositories are involved:

-   [Upstream source repository (fkanehiro/hrpsys-base)](https://github.com/fkanehiro/hrpsys-base/issues)
-   [ROS repository (start-jsk/hrpsys)](https://github.com/start-jsk/hrpsys/blob/master/CHANGELOG.rst)

Steps:

1\. Send a pull request to
[fkanehiro/hrpsys-base](https://github.com/fkanehiro/hrpsys-base/issues)
to update a tag in
[CMakeLists.txt](https://github.com/fkanehiro/hrpsys-base/blob/master/CMakeLists.txt).
[Example](https://github.com/fkanehiro/hrpsys-base/pull/231). This way
community will decide if we\'re ready for the next release. 2. Send a
pull request to update
[start-jsk/hrpsys/Makefile.hrpsys-base](https://github.com/start-jsk/hrpsys/blob/master/Makefile.hrpsys-base).
[Example](https://github.com/start-jsk/hrpsys/pull/88/files). 3. Send a
pull request to update
[start-jsk/hrpsys/CHANGELOG.rst](https://github.com/start-jsk/hrpsys/blob/master/CHANGELOG.rst).

3-1. Use [this script](https://github.com/start-jsk/hrpsys/pull/96) to
copy commit messages from upstream \`fkanehiro/hrpsys-base\`.

3-2. Summarize commit messages into user-meaningful content
([discussion](https://github.com/start-jsk/hrpsys/pull/99#issuecomment-49596002)).

3-3. (Rare) If there\'s an update in
[ROS repository (start-jsk/hrpsys)](https://github.com/start-jsk/hrpsys/blob/master/CHANGELOG.rst),
add change logs into the one created in 3-2. Maybe use
\`catkin_generate_changelog\` command to auto-generate it, and manually
merge.

4\. After here follow the normal release manner: Update tags and
\`package.xml\` by using \`catkin_prepare_release\`.

Notice that we\'re sending pull requests to two different repositories;
one is the source upstream repository that isn\'t ROS-dependent, another
repository is used to release a DEB using ROS infrastructure.
