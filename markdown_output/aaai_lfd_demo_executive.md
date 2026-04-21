## Description

This package contains the node that controls the demo by telling the
robot where to navigate using rl_2dnav and where to pick up the objects
using openloop_object_manipulation. It uses the param server for the
object locations and for the "executive_script" which is the order the
objects should be picked up and put down.



```
self.object_locations = rospy.get_param('aaai_lfd_demo_object_locations', {})
 self.executive_script = rospy.get_param('aaai_lfd_demo_executive_script', {})
```



execute.py essentially performs the functionality described in the
tutorials of
[ rl_2dnav](http://www.ros.org/wiki/rl_2dnav/Tutorials/Using%20rl_2dnav%20action%20server )
and
[openloop_object_manipulation ]( http://www.ros.org/wiki/openloop_object_manipulation/Tutorials/Using%20the%20open_loop_object_manipulation%20actionserver )
using the config files found in aaai_lfd_demo_launch.
