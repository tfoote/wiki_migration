## How to

The corobot_launch package provide several launch file to customize what
you want to launch. The corobot_software.launch is the main launch file,
the one you should call to launch the necessary nodes to use your robot.
To do so, just do: ```
{
roslaunch corobot_launch corobot_software.launch
```}

In the launch_included folder you will see several launch files like
camera.launch or motor.launch, which you can open and customize. Several
parameters are present for you to modify, some are so select the nodes
that will start, other for important values necessary to make some
hardware work.
