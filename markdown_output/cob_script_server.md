## Hardware Requirements

This package was created to be used with Care-O-bot but is not limited
to one specific robot. It can be used for a real robot as well as for a
simulated one (see [cob_bringup](https://index.ros.org/p/cob_bringup)).

## Python API

This package provides all methods as a python API (see
[Tutorials](#tutorials-1)). The table
below shows a summary of the most important commands and their
parameters.

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
[actionlib](https://index.ros.org/p/actionlib) calls.

### script_server

The script server node takes in
[cob_script_server/msg/ScriptAction](https://docs.ros.org/en/rolling/p/cob_script_server/msg/ScriptAction.html)
messages and send this to the robot to be executed.

#### Action Goal

- `script_server/goal`
  ([cob_script_server/msg/ScriptActionGoal](https://docs.ros.org/en/rolling/p/cob_script_server/msg/ScriptActionGoal.html)):
  The goal describes the script action command the robot has to execute

#### Action Result

- `script_server/result`
  ([cobscript_server/msg/ScriptActionResult](https://docs.ros.org/en/rolling/p/cobscript_server/msg/ScriptActionResult.html)):
  Returns an error code

#### Action Feedback

- `script_server/feedback`
  ([cob_script_server/msg/ScriptActionFeedback](https://docs.ros.org/en/rolling/p/cob_script_server/msg/ScriptActionFeedback.html)):
  empty

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
[cob_default_robot_config](https://index.ros.org/p/cob_default_robot_config).

## Tutorials

Tutorials can be found on the
[Tutorials page](#tutorials-1).

## Tutorials

### Script Server Tutorials

#### Running a Script

- [Running a simple grasp script](#running-a-simple-grasp-script):
  This tutorial teaches you how to run a script.

#### Writing a Script

- [Modifying parameter files](#modifying-parameter-files):
  This tutorial teaches you how to modify parameter files, e.g. for
  teaching new positions.
- [Preparing a new script (python)](#preparing-a-new-script-python):
  This tutorial shows how to write a simple script for grasping and
  handing over an object using cob_script_server.
- [Specify execution behaviour (python)](#specify-execution-behaviour-python):
  This tutorial shows how to execute synchronous and asynchronous
  behaviour.
- [Using other commands (python)](#using-other-commands-python):
  This tutorial teaches you how to use other commands beside the `move`
  command.
- [Using the move command (python)](#using-the-move-command-python):
  This tutorial teaches you how to use the move function.

#### Using Script Server Tools

- [Generate a graph from a script](#generate-a-graph-from-a-script):
  This tutorial teaches you how to generate a graph from a script and
  save it as a `*.png` file.
- [Live visualization of a script](#live-visualization-of-a-script):
  This tutorial teaches you how to visualize a running script.

#### All Tutorials

- [Generate a graph from a script](#generate-a-graph-from-a-script):
  This tutorial teaches you how to generate a graph from a script and
  save it as a `*.png` file.
- [Live visualization of a script](#live-visualization-of-a-script):
  This tutorial teaches you how to visualize a running script.
- [Modifying parameter files](#modifying-parameter-files):
  This tutorial teaches you how to modify parameter files, e.g. for
  teaching new positions.
- [Preparing a new script (python)](#preparing-a-new-script-python):
  This tutorial shows how to write a simple script for grasping and
  handing over an object using cob_script_server.
- [Running a simple grasp script](#running-a-simple-grasp-script):
  This tutorial teaches you how to run a script.
- [Specify execution behaviour (python)](#specify-execution-behaviour-python):
  This tutorial shows how to execute synchronous and asynchronous
  behaviour.
- [Using other commands (python)](#using-other-commands-python):
  This tutorial teaches you how to use other commands beside the `move`
  command.
- [Using the move command (python)](#using-the-move-command-python):
  This tutorial teaches you how to use the move function.

## Running a simple grasp script

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Bringing up Care-O-bot](https://index.ros.org/p/cob_bringup).
- **Description:** This tutorial teaches you how to run a script.
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Live visualization of a script](#live-visualization-of-a-script)
  [Preparing a new script (python)](#preparing-a-new-script-python)

### Software Requirements

You will need [cob_tutorials](cob_tutorials). Install it following the
instructions on [Robots/Care-O-bot/git](Robots/Care-O-bot/git).

### Bringing up the robot

First, bringup either a real Care-O-bot or a simulated one (see
[cob_bringup_sim](https://index.ros.org/p/cob_bringup_sim)). To bringup
a simulated Care-O-bot 

```
export ROBOT=cob3-3
export ROBOT_ENV=ipa-kitchen
roslaunch cob_bringup_sim robot.launch
```

 You should see gazebo
starting with a Care-O-bot in the IPA kitchen environment.

Launch the specific launch file for this tutorial, navigation,
kdl_solver and parameters 

```
roslaunch cob_script_server_tutorial script_server_tutorial.launch
```



### Running a simple grasp script

Afterwards we can run a script and watch the robot moving either in the
[gazebo](gazebo) window or with [rviz](https://index.ros.org/p/rviz).


```
rosrun cob_script_server_tutorial simple_grasp.py
```

 You should open rviz to localise the robot in
order to the robot can reach the correct positions.


```
rosrun rviz rviz
```

## Modifying parameter files

- **Description:** This tutorial teaches you how to modify parameter
  files, e.g. for teaching new positions.
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Specify execution behaviour (python)](#specify-execution-behaviour-python)

### Script Server Parameters

The cob_script_server uses the ROS
[parameter server](Parameter Server) for making parameters available to
different nodes. The parameters are added to the namespace of their
component within the `/script_server` namespace, e.g.
`/script_server/tray` for tray positions.

To check if a parameter is loaded type 

```
rosparam list | grep script_server
```



If you already started a script_server (see
[Running a simple grasp script](#running-a-simple-grasp-script))
you should see something like 

```
/script_server/arm/folded
/script_server/arm/home
/script_server/arm/pregrasp
/script_server/arm/tablet
/script_server/base/home
/script_server/base/kitchen
/script_server/sdh/cylclosed
/script_server/sdh/cylopen
/script_server/sdh/home
...
```



### Parameter files

The script server uses `.yaml`-files to load parameters to the ROS
[parameter server](Parameter Server).

The default `.yaml`-files can be found in the
[cob_default_robot_config](https://index.ros.org/p/cob_default_robot_config)
package 

```
roscd cob_default_robot_config/cob3-3
```



The `tray_joint_configurations.yaml`-file could look similar to this:



```python
joint_names: ["torso_tray_joint"]

up: [[0.0]]
down: [[-3.1415926]]
```



Each entry is defined as a list of lists. The inner list contains all
joint positions for a certain point. The outer list contains all points
belonging to a certain trajectory. All commands are trajectories with
one or more points.

Here you can see an example of a `arm_joint_configurations.yaml` file
with points and trajectories: 

```python
joint_names: ["arm_1_joint","arm_2_joint","arm_3_joint","arm_4_joint","arm_5_joint","arm_6_joint","arm_7_joint"]

# single positions
home: [[0,0,0,0,0,0,0]]
folded: [[-1.16, -1.91, -2.53, -1.78, -2.84, -0.97, 1.76]]
pregrasp: [[-1.3813, -1.9312, -1.7251, -1.4565, 0.7169, 1.0560, -2.1230]]
wavein: [[1.5, 0.5, 0.0, -0.5, 0.0, 0.5, 0.0]]
waveout: [[1.5, 0.5, 0.0, 0.5, 0.0, -0.5, 0.0]]

# trajectories
wave: [waveout, wavein, waveout, wavein]
```



The `base.yaml`-file for the base looks slightly different. Here you
specify a 2D pose with in a 2D map, this means `x`- and `y`-position as
well as the `theta` orientation around the z-axis.



```python
#[x,y,theta]
home: [0, 0, 0]
order: [0.5, -1, 0]
kitchen: [-2.05, -1.36, 1.0]
```



You can upload your own configurations by creating a `.yaml`-file and
uploading it to the `/script_server`-namespace at the ROS
[parameter server](Parameter Server).

## Preparing a new script (python)

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Bringing up Care-O-bot](https://index.ros.org/p/cob_bringup),
  [Running a simple grasp script](#running-a-simple-grasp-script).
- **Description:** This tutorial shows how to write a simple script for
  grasping and handing over an object using cob_script_server.
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Using the move command (python)](#using-the-move-command-python)
  [Using other commands (python)](#using-other-commands-python)

### Including cob_script_server

`cob_script_server` provides basic functions to make simple movements
with Care-O-bot's arms, grippers, torso and base. `cob_script_server`
provides a Python interface which can be included in any other script.
To do so, prepare the following script structure:



```python
#!/usr/bin/python

import roslib
roslib.load_manifest('cob_script_server')
import rospy

from simple_script_server import script

class MyScript(script):
    def Initialize(self):
        rospy.loginfo("Initializing all components...")

    def Run(self):
        rospy.loginfo("Running script...")

if __name__ == "__main__":
    SCRIPT = MyScript()
    SCRIPT.Start()
```

 As you can see you have declared a new class
`MyScript` with two functions `Initialize` and `Run`. The class
`MyScript` inherits from the `script` class which provides the
functionalities of the
cob_script_server as a python API. The
`Initialze`-function will later be used to send an init-command to all
components and move them to initial positions so that the script can be
started. The `Run`-function will later contain the main script.

Save your file in a ROS package. For testing you should save the file as
`my_script.py` in the folder `<cob_script_server_tutorial>/scripts/`.

### Initializing Components

If you want to run your script on a real robot all components need to be
initialized before they can be moved. For doing this, the routine
`Init("<component_name>")` is provided. In order to initialize all
components, add an Init-command for each component to your
`Initialize`-function:



```python
    def Initialize(self):
        rospy.loginfo("Initializing all components...")
        self.sss.init("base")
        self.sss.init("torso")
        self.sss.init("arm_left")
        self.sss.init("arm_right")
        self.sss.init("gripper_left")
        self.sss.init("gripper_right")
```

 For simulation this step is not neccessary.

Furthermore before the script can be started all components should move
to their initial positions:



```python
    def Initialize(self):
        rospy.loginfo("Initializing all components...")
        self.sss.init("base")
        self.sss.init("torso")
        self.sss.init("arm_left")
        self.sss.init("arm_right")
        self.sss.init("gripper_left")
        self.sss.init("gripper_right")

        # move to initial positions
        self.sss.move("torso","home")
        self.sss.move("arm_left","side")
        self.sss.move("arm_right","side")
        self.sss.move("gripper_left","close")
        self.sss.move("gripper_right","close")
```



### Running your script for the first time

Although the script does nothing really useful yet, it is a good idea to
run it now for the first time. Doing so allows you to check if
everything is set up correctly and if all packages you need are there.
To run your script you have to

1\. Make your script executable by typing in a shell


```
chmod 755 my_script.py
```

 2. Bringup a robot. For starting Care-O-bot in
simulation type 

```
export ROBOT=cob4-3
 roslaunch cob_bringup_sim robot.launch
```

 For detailed instructions about
this package have a look at
[cob_bringup_sim](https://index.ros.org/p/cob_bringup_sim). 3. Start
`cob_script_server` by typing 

```
roslaunch cob_script_server_tutorial script_server_tutorial.launch
```

 For detailed
instructions about this package have a look at
cob_script_server.

Note that you have to start `cob_script_server` although you include it
directly in your script and do not want to send messages to it. This is
necessary because the package also sets up all parameters, e.g. joint
angles for certain positions. 4. Start your script. If you have saved
your script as `my_script.py` in `<cob_script_server_tutorial>/scripts/`
you need to issue the command 

```
rosrun cob_script_server_tutorial my_script.py
```



If you have done everything right, you will see some messages saying
that Care-O-bot's components are initializing (For simulation this will
fail, but you don't have to care about this). As step 1-3 only have to
be done once you can now start your script anytime you like by repeating
step 4.

## Specify execution behaviour (python)

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Preparing a new script (python)](#preparing-a-new-script-python),
  [Using the move command (python)](#using-the-move-command-python).
- **Description:** This tutorial shows how to execute synchronous and
  asynchronous behaviour.
- **Tutorial Level:** INTERMEDIATE
- **Next Tutorial:**
  [Using other commands (python)](#using-other-commands-python)

### Synchronizing motion

Wouldn't it be nice if you could start opening the hand for grasping
while the arm is still moving? To do that you need to call functions
non-blocking so that they run in the background. To make a function
non-blocking set the optional third parameter of `move` to `False`.



```python
        # move arm while opening gripper
        self.sss.move("arm_left","arm_to_tray",False)
        self.sss.move("gripper_left","open")
```

 Now the gripper will start to move right after
the arm has begun to move. As the arm trajectory is rather long, the
gripper will reach its target position even before the arm.

### Waiting for motion to finish

In the example above the components move at the same time. But how will
you know, that the arm has finally arrived? You need to know that
because otherwise you might open the hand to early and the object will
drop! The solution is to assign a handle to the non-blocking function.
You can call `<handle>.wait()` afterwards to ensure that the function
call is finished.

So you should modify the code above and add the `<handle>.wait()`
functionality to the arm movement.



```python
        # move arm while opening gripper
        handle01 = self.sss.move("arm_left","arm_to_tray",False)
        self.sss.move("gripper","open")

        #wait for arm movement to be finished
        handle01.wait()
```



The `wait` function provides even more functionality. You can set a
timeout, after which you stop waiting and go on with your script. Note
that this timeout doesn't terminate the action running in the
background. The `wait` function also returns the status code or exit
code of the associated `Move` function, which allows you to check if the
action had any errors.

### Getting current state and error_code

If you assigned a handle to a move action you can ask for the current
state and get an error_code, which indictes what kind of failure
occoured. So let's modify the code above again to



```python
        # move arm while opening gripper
        handle01 = self.sss.move("arm_left","arm_to_tray",False)
        self.sss.move("gripper","open")

        # print current state
        print handle01.get_state()

        #wait for arm movement to be finished
        handle01.wait()

        # print again current state and error_code
        print handle01.get_state()
        handle01.get_error_code()
```



If the movements are executed without error you should get state `1` for
the first `get_state()` which means active. For the second `get_state()`
the action should be finished so you get the state `2` for `failed` or
`3` for `succeeded`. The return states of the `get_state()` function are
the same as the return codes of the actionlib, see
<http://www.ros.org/doc/api/actionlib_msgs/html/msg/GoalStatus.html>.

To know what went wrong you can have a look at the error_code from
`get_error_code()`. The error_code is `0` if all was successfully or
otherwise an integer value indicating the reason for the failure.

## Using other commands (python)

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Preparing a new script (python)](#preparing-a-new-script-python).
- **Description:** This tutorial teaches you how to use other commands
  beside the `move` command.
- **Tutorial Level:** BEGINNER

Apart from the `Move` command,
cob_script_server provides some basic
functionality for other subsystems of the robot, e.g.: You can play a
wave file or say text using a text to speech system, you can also change
the color of the LEDs in Care-O-bot's torso, get some user input, etc.
\...

### Speech

cob_script_server provides two
functions for producing sound:



```
Speak(<parameter_name>,<mode (optional)>)
SpeakStr(<text_to_be_spoken>,<mode>)
```



#### The Speak function

The first function allows you to produce a sound specified by
`<parameter_name>` in an output mode specified by `<mode>`. Possible
modes are:

- `"DEFAULT"` - use the default mode set by the global parameter
  `speech_mode`. The global parameter is set in
  `<cob_script_server>/launch/sound.yaml` and has to be one of the other
  possible modes.
- `"WAV_DE"` - play wav-Files with German text. The directory for the
  wave file is set in global parameter `wav_de_path`.
- `"WAV_EN"` - play wav-FIles with English text. The directory for the
  wave file is set in a global parameter `wav_en_path`.
- `"FEST_EN"` - use free text-to-speech system Festival. It should
  already be installed on your computer as some other ROS packages
  depend on it.
- `"CEPS_EN"` - use commercial text-to-speech Cepstral with the English
  voice David. Of course this only works if you have bought and
  installed the voice on your computer.
- `"CEPS_DE"` - use commercial text-to-speech Cepstral with the German
  voice Matthias. Of cause this only works if you have bought and
  installed the voice on your computer.
- `"MUTE"` - play no sound at all but show a message each time a sound
  would be played. This is a good option for not beeing annoyed while
  testing your script.

The basic idea behind these different modes is that you can change the
mode any time you want. For example you could have a presentation for
English-speaking people one day and for German-speaking people another
day. Say that for the English version you would like to use Festival
text-to-speech but having no German voice installed you would like to
use wave files for the German presentation. Here is what you have to do:

- Set up all sentences for the English presentation in
  `<cob_script_server>/launch/sound.yaml`. For our grasp script the file
  might look like this: 

```python
 speech_en/grasp_tutorial_01: "Hello, my name is Care-O-bot!"
 speech_en/grasp_tutorial_02: "I will get you something to drink."
 speech_en/grasp_tutorial_03: "Here is your drink!"
```

 Note that all english
  sentences are are in a seperate namespace called `speech_en`
- For the German presentation, record your wave files, name them in the
  same way as your parameters an put them in the folder specified by the
  paramter `wav_de_path`. For our grasp script the directory might look
  like this: 

```
$ ls
     grasp_tutorial_01.wav
     grasp_tutorial_02.wav
     grasp_tutorial_03.wav
```

 For this tutorial the wav files
  are already provided in folder
  `<cob_script_server>/common_files/wav_de/`. Please ensure that the
  absolute(!) path to this directory is available as `wav_de_path` in
  `sound.yaml`.

Now go on and add some speech commands to your grasp script. For example
you could add a greeting message in the beginning. When the drink is
ready you speak another sentence saying that the user can now take the
drink. Find out how it works best! - or try this solution:



```python
    def GraspObject(self):
        rospy.loginfo("Grasping an object from table...")
        # speak greeting
        self.sss.Speak("grasp_tutorial_01")
        self.sss.Speak("grasp_tutorial_02")

        # prepare for grasping
        myhandle = self.sss.Move("arm","pregrasp",False)
        self.sss.Move("sdh","cylopen")
        myhandle.wait()
        # grasp the object
        self.sss.Move("arm","grasp")
        self.sss.Move("sdh","cylclosed")
        # put object on tray
        myhandle = self.sss.Move("arm","grasp-to-tablet",False)
        self.sss.Move("tray","up")
        myhandle.wait()
        self.sss.Move("sdh","cylopen")
        # draw arm back to folded position
        myhandle = self.sss.Move("arm","tablet-to-folded",False)
        self.sss.Move("sdh","cylclosed")
        myhandle.wait()

        # inform user that he may take the drink
        self.sss.Speak("grasp_tutorial_03")
```



#### The SpeakStr function

The `Speak` function requires that you have a parameter for every text
you want to speak. If you just want add some spoken words to your script
very quickly or if you want to change your messages dynamically during
runtime, you can use `SpeakStr` function. The difference to the `Speak`
function is, that you hand over the string to be spoken directly as a
parameter. Of cause this only works for text-to-speech systems (not for
wave files). Therefore the `<mode>` parameter is required for this
function. Possible modes are:

- `"FEST_EN"` - use free text-to-speech system Festival. It should
  already be installed on your computer as some other ROS packages
  depend on it.
- `"CEPS_EN"` - use commercial text-to-speech Cepstral with the English
  voice David. Of cause this only works if you have bought and installed
  the voice on your computer.
- `"CEPS_DE"` - use commercial text-to-speech Cepstral with the German
  voice Matthias. Of cause this only works if you have bought and
  installed the voice on your computer.

If you like, make a few tests with `SpeakStr` function. Add some funny
texts to your grasp script!

### Setting LED color

cob_script_server also allows you to
change the color of the LEDs in Care-O-bot's torso. The command is



```
SetLight(<color_parameter>)
```

 Once again the parameters for the different
colors are set in a seperate file,
`<cob_script_server>/launch/light.yaml` this time. Each LED parameter
consists of three numbers which are more or less an RGB notation.
Unfortunately the brightness of the different colors is not the same, so
a nice white light is `[250,999,300]`.

You can use the LEDs to give a visual feedback of the robot's status or
task. For example you could set the LEDs to yellow everytime the arm is
moving (signals "attention!") and back to green when the arm stopps.
Another idea would be to use a certain color (e.g. blue) to indicate
that user interaction (e.g. taking the bottle) is allowed or required.

### Waiting for input or confirmation

Sometimes it is helpful to suspend a script until the user confirms by
pressing a key. Of cause a real autonomous robot wouldn't need
something like that but for testing it's nice to have.
cob_script_server provides a function



```
input_string = wait_for_input()
```



to wait for confirmation. The function is blocking until the `Return`
key is hit. If the user enters a string and hits `Return` afterwards,
you can read out the input from variable `input_string`. Note that the
`Return` key itself produces a linefeed character (`\n`). This is
important if you want to compare strings afterwards.

Say you want to lower the tray once the drink has been taken by the
user. As you do not know when this will happen you could wait for some
helpful guy to press a button to indicate that the drink is gone. In
order to do so, add the following lines to the end of the grasp script



```python
        # wait for signal that the drink has been taken
        self.sss.wait_for_input()
        self.sss.Move("tray","down")
```

 **Congratulations! You have written your first
grasp script using
cob_script_server!**

## Using the move command (python)

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Preparing a new script (python)](#preparing-a-new-script-python).
- **Description:** This tutorial teaches you how to use the move
  function.
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Modifying parameter files](#modifying-parameter-files)

### The Move command

By using the `move` command you can command any motion for components
such as arm, gripper, torso and base. By combining these commands you
write a first script.

Components are moved by using the `move` command:



```
Move(<component_name>,<parameter_name>,<blocking (optional)>)
```



1\. The first parameter specifies the component which shall be moved.
Possible components are `"arm_left"`, `"arm_right"`, `"gripper_left"`,
`"gripper_right"`, `"torso"` and `"base"`.

2\. The second parameter is the name of a parameter on the ROS
[parameter server](Parameter Server) which specifies a target position
or trajectory. These parameters are specified in several `.yaml`-files
in the `<cob_script_server>/launch/` directory. More about modifying and
adding new positions in the next tutorial
[Modifying parameter files](#modifying-parameter-files).
It is also possible to specify directly a position or trajectory instead
of a name.

3\. The third parameter is optional and specifies the execution behavior
to be blocking or non-blocking. More on the execution behaviour in the
[Specify execution behaviour](https://index.ros.org/p/cob_script_server).
Possible values are `True` and `False`, default is `True`.

### First moves

Back to your first script. Add some `move`-commands for some of the
positions you find in the `.yaml` files to the `Run`-function and see
what happens. For grasping an object, a sequence like this might be
suitable:



```python
    def Run(self):
        rospy.loginfo("Grasping an object...")

        # prepare for grasping
        self.sss.move("gripper_left","open")
        self.sss.move("arm_left","arm_to_tray")

        # grasp the object that is given to the robot
        self.sss.move("gripper_left","close")

        # move arm to torso for navigation
        self.sss.move("arm_left","side")
```



Experiment a little bit with these commands. You could for example try
to grasp something from a table.

You might also want to add some commands for the torso:



```python
        self.sss.move("torso","front")
        self.sss.move("torso","back")
```



or make Care-O-bot nodding and shaking its head



```python
        self.sss.move("torso","front_down")
        self.sss.move("torso","shake")
```



or move the base



```python
        self.sss.move("base","home")
        self.sss.move("base","kitchen")
```



Please note that for executing base movements you need to launch another
`.launch`-file besides the script_server. To do this, open a new
terminal and enter the following: 

```
roslaunch cob_navigation_global 2dnav_ros_dwa.launch
```

## Generate a graph from a script

- **Description:** This tutorial teaches you how to generate a graph
  from a script and save it as a `*.png` file.
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Running a simple grasp script](#running-a-simple-grasp-script)

### Generating a graph

## Live visualization of a script

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Running a simple grasp script](#running-a-simple-grasp-script).
- **Description:** This tutorial teaches you how to visualize a running
  script.
- **Tutorial Level:** BEGINNER

### Start the Script Viewer

To start the script viewer type 

```
rosrun cob_script_server script_viewer.py
```

 You should see
a new window saying "no graph available"

![no graph available](doc/no_graph.png)\

or if you already executed a script showing the graph of the last
script.

![clear graph of a test_script](doc/test_script_clear.png)\

### Run a Script and follow the status in the Script Viewer

Now you can run a script as described in the
[running a simple script](#running-a-simple-grasp-script)
tutorial and use to script viever to monitor the execution state of the
script. The colors in the block represent the different states according
to the following table.

  -- ----------- -- ------------ --
     **color**      **state**    
     white          not active   
     yellow         active       
     red            failed       
     green          succeeded    
  -- ----------- -- ------------ --

![graph of a test_script](doc/test_script.png)\
