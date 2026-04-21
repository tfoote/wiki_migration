## Overview

This package defines an actionlib interface for controlling PTUs. This
interface allows PTUs to be controlled by specifing either absolute
pan/tilt angles, or pan/tilt velocities (if supported in hardware).

An actionlib server using this interface is also provided for
controlling and tracking the Logitech Orbit AF camera.

## Python Action Client Example

The following code reads pan and tilt angles from the command line,
starts an action client, sends the desired pan/tilt angles, and waits
for any feedback. 

```python
#!/usr/env/bin python
import roslib; roslib.load_manifest('ptu_control')
import rospy
import ptu_control.msg
import actionlib
import sys
 
def ptu_action_test():
    client = actionlib.SimpleActionClient('SetPTUState', ptu_control.msg.PtuGotoAction)
    client.wait_for_server()
    goal = ptu_control.msg.PtuGotoGoal(pan=float(sys.argv[1]), tilt=float(sys.argv[2]))
    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()
     
if __name__ == '__main__':
    rospy.init_node('action_test')
    result = ptu_action_test()
    print result
```


