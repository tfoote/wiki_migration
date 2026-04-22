## Hardware Requirements

This package was created to be used with Care-O-bot but is not limited
to one specific robot. It can be used for a real robot as well as for a
simulated one (see [cob_bringup](cob_bringup)).

## Python API

This package provides all methods as a python API (see
[Tutorials](cob_script_server/Tutorials)). The table below shows a
summary of the most important commands and their parameters.

  -- ------------------ -- -------------------- ------- ---------------------------------------------- ----- ------------------------------------------ ---------------------------------- ----------------------------------- ------------------------------------------------------------------------------- ----------------------- -------------------------------------------------- ----------------------------------------- --
     **command**           **component name**           **parameter name**                                   **example**                                                                   **explanation**                                                                                                                                                                                                                          
     `init()`              base                 torso   tray                                           arm   sdh                                                                           \--                                                                                                                 `sss.init("base")`                                                         initializes component                     
     `recover`             base                 torso   tray                                           arm   sdh                                                                           \--                                                                                                                 `sss.recover("base")`                                                      recovers component after emergency stop   
     `stop`                base                 torso   tray                                           arm   sdh                                                                           \--                                                                                                                 `sss.stop("base")`                                                         stops current goal of component           
     `move`                torso                tray    arm                                            sdh                                              string of parameter                                                    `sss.move("torso","front")`                                                                             move component to predefined joint configuration                                             
     `move`                torso                tray    arm                                            sdh                                              list of points with joint values                                       `sss.move("torso",` `  [[0, 0, 0, 0],` `  [0.1, 0, 0.2, 0],` `  [...], ...])`                           move component to joint configuration                                                        
     `move`                base                         string of parameter                                  `sss.move("base","home")`                                                     move component to predefined pose                                                                                                                                                                                                        
     `move`                base                         \[x,y,th\] in map coordinates                        `sss.move("base",[0, 0, 0])`                                                  move component to pose                                                                                                                                                                                                                   
     `move_base_rel`       base                         \[x,y,th\] in base_link relative coordinates         `sss.move_base_rel("base",[0, 0, 1.57])`                                      move relative pose base                                                                                                                                                                                                                  
     `sleep`               \--                          time in seconds                                      `sss.sleep(2.0)`                                                              sleeps                                                                                                                                                                                                                                   
     `wait_for_input`      \--                          \--                                                  `ret = sss.wait_for_input()`                                                  wait for a keyboard input                                                                                                                                                                                                                
     `say`                 \--                          string of parameter                                  `sss.say("sentence1")`                                                        says a predefined string                                                                                                                                                                                                                 
     `say`                 \--                          list of strings                                      `sss.say(["Hello."])`                                                         says a string                                                                                                                                                                                                                            
     `set_light`           \--                          string                                               `sss.set_light("red")`                                                        sets LEDs to a predefined color                                                                                                                                                                                                          
     `set_light`           \--                          \[r,b,g\]                                            `sss.set_light([0.5,0.5,0.5])`                                                sets LEDs to a rgb color                                                                                                                                                                                                                 
  -- ------------------ -- -------------------- ------- ---------------------------------------------- ----- ------------------------------------------ ---------------------------------- ----------------------------------- ------------------------------------------------------------------------------- ----------------------- -------------------------------------------------- ----------------------------------------- --

Each of the above function (except `wait_for_input`, which returns the
keyboard input) returns a handle which offers the following commands.

  -- ----------------- -- ---------------------- -- ----------------------------------------------------------------------------------------------------------------------------------------------------- --
     **command**          **example**               **explanation**                                                                                                                                       
     `wait()`             `handle.wait()`           waits forever until the command is finished                                                                                                           
     `wait(timeout)`      `handle.wait(2.0)`        waits until the command is finished, but max. for `timeout` seconds                                                                                   
     `get_state()`        `handle.get_state()`      gets the state of the current execution (see [actionlib_msgs/msg/GoalStatus](https://docs.ros.org/en/rolling/p/actionlib_msgs/msg/GoalStatus.html))   
  -- ----------------- -- ---------------------- -- ----------------------------------------------------------------------------------------------------------------------------------------------------- --

## Terminal API

By running 

```
rosrun cob_script_server cob_console
```

 you can access all script_server
commands in an ipython terminal with the prefix `sss`, e.g.


```
sss.move("head","front")
```



## Actionlib API

All functions from the python API are also available as
[actionlib](actionlib) calls.



```clearsilver
 name = script_server
 desc = The script server node takes in <<MsgLink(cob_script_server/ScriptAction)>> messages and send this to the robot to be executed.

goal{
 0.name=script_server/goal
 0.type=cob_script_server/ScriptActionGoal
 0.desc=The goal describes the script action command the robot has to execute
}

result{
 2.name=script_server/result
 2.type=cobscript_server/ScriptActionResult
 2.desc=Returns an error code
}

feedback{
 0.name=script_server/feedback
 0.type=cob_script_server/ScriptActionFeedback
 0.desc=empty
}

sub{
}

pub{
}

srv{
}

param{
}

req_tf{
}

prov_tf{
}
```



## Usage/Examples

For starting the script server and upload parameters


```
roslaunch cob_script_server script_server.launch
```

 For running a test script


```
rosrun cob_script_server test_script.py
```

 For running the script viewer


```
rosrun cob_script_server script_viewer.py
```



All the parameters that are loaded in the name space /script_server are
defined in .yaml files in the package
[cob_default_robot_config](cob_default_robot_config).

## Tutorials

Tutorials can be found on the
[Tutorials page](cob_script_server/Tutorials).
