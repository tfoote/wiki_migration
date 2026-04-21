<http://jks-ros-pkg.googlecode.com/svn/trunk/pr2_coffee>

## Introduction

Multi-map navigation allows multiple 2D maps to be linked together with
"transitions" that allow the robot to travel between the two maps.
This approach solves the problem of having large maps that are too big
for the robot's memory or are too difficult to make in one SLAM
session. In addition, it allows for easy navigation of multi-floor
buildings. Each of the transitions can lead to the execution of a
separate program via "transition" actions as it is taken. This allows
the operation of door opening software or elevator management software.

## Map Creation

To create the maps used for multi-map navigation, you should use SLAM
software to create a number of 2D maps. You must engineer the maps in a
manner such that when the robot completes a transition from one map to
the next, it will be ready to navigate on the second map. These
requirements are dependent on your transition software. The default
transition simply dumps the robot right into the new map, so the two
maps should overlap at least enough for the robot to be able to navigate
on each transition.

After creating the maps, you must load them into the map_store. One way
to do this with the add_map script in the map_store package. Remember to
give them descriptive names so that they can be used appropriately in
defining transitions.

After loading the maps, you must define transitions between maps. This
revolves around creating a YAML file defining them. The YAML file has
two main parts - the first is a list of maps and the second a list of
transitions. The maps section is as follows: ```
start_map: willow-up
maps:
     - name: willow-up
       north_angle: 1.5707963267948966
```

The last two lines are repeated for however many maps there are. The
start_map: defines the initial map. The last two lines define a map
named willow-up. North_angle must be specified and is assumed to be the
angle towards north. It is always required, but it need not be accurate
unless the default transition is used. If all maps face the same
direction, it is safe to set all north_angle values to zero.

After defining your maps, you must define the transitions, which begin
with the wormholes tag: ```
wormholes:
     - name: hallway-door
       type: normal
       radius: 0.55
       locations:
            - map: willow-down
              position: [36.071, 19.45]
            - map: willow-up
              position: [5.65, 22.629]
```

The wormholes tag specifies the list of transitions. The -name: elements
may be repeated to define as many transitions as you wish. The name of
each transition (hallway-door) in this case, must be unique. The
"type:" tag describes the type of transition, which may be normal or
the name of a transition action (see below on creating your own
transition). The "radius:" tag defines the limits to the radius, a
circle which the robot must enter to travel through the transition - if
it is omitted, then the robot will attempt to get all the way to the
location before executing the transition. In addition to these
parameters, the location may contain other parameters that are fed to
the transition action, so long as they do not conflict with
"locations", "name", and "radius" at the will of the transition
action writer.

The "locations:" tag begins a list of locations, and each of the two
lines defines a location. Locations are the endpoints of a transition.
Most transitions (such as doors) have two locations, but some may have
more (e.g. an elevator in a four story building might have four
transitions). Each location must specify a map: which is the map in
which that location is placed and position: which is the x-y coordinate
in that map. To get these coordinates, open the map in such a way that
you can use rviz to place goals in that location, and then read from the
rviz console logs. Locations may additionally specify a direction: exit
or direction: entrance. This is needed for one-way transitions such as
pushing open a door. Locations without direction: are considered
bi-directional. Finally, the location may specify an angle: tag which
specifies an angle the robot must face when it reaches the location,
which ensures that the robot is facing the right way to perform the
action required. In addition to these parameters, the location may
contain other parameters that are fed to the transition action, so long
as they do not conflict with "map", "position", "angle", or
"direction", at the will of the transition action writer.

## Launching

You must first add map_store to your launch file. To start
multi_map_navigation, add this code to your launch file:
```
<node pkg="multi_map_navigation" type="multi_map_navigation" name="multi_map_navigation" output="screen">
  	<param name="definition_file" value="YAML" />
	<param name="transition_types" value="TYPES" />
  </node>
```

Where YAML is the absolute path to your configuration YAML and TYPES is
a list of transition actions that could be present in the map. TYPES can
be the empty string if you have no transitions outside of "normal"
transitions that do not trigger any actions.

You can also add lines to set the initial pose of the base:
```
<param name="/amcl/initial_pose_x" value="9.116" />
  <param name="/amcl/initial_pose_y" value="10.993" />
  <param name="/amcl/initial_pose_a" value="1.546" />
```

## Specifying Robot Position and Calling Multi-Map Navigation

Once multi-map navigation is launched, you must specify a position in
the maps. If you did not specify a proper initial position, then you
must use rviz to place the robot properly in the map. You must also
launch on the proper map, if you haven't, then you must properly set
the map from the command line: ```
rosservice call /multi_map_navigation/set_map <map-name>
``` Where
<map-name> is the target <map-name> which the robot is starting on.

Once multi-map navigation is launched, you can give the robot a goal. To
achieve this from the command line: ```
rosrun multi_map_navigation multi_map_navigation_test 12 10 willow-down
``` Where 12
and 10 are the floating point x-y coordinate of the target and
"willow-down" is the target map name.

## Calling Multi-Map Navigation Pragmatically

The example of multi_map_navigation_test shows how to do this
effectively. Basically, there is an action called
MultiMapNavigationAction that exists in multi_map_navigation/move. From
python:

```
self.action_client = actionlib.SimpleActionClient("multi_map_navigation/move", MultiMapNavigationAction)
        self.action_client.wait_for_server()
        goal = MultiMapNavigationGoal()
        goal.target_pose.header.stamp = rospy.get_rostime()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.pose.position.x = xp
        goal.target_pose.pose.position.y = yp
        goal.target_pose.pose.orientation.w = 1.0
        goal.goal_map = map
        self.action_client.send_goal(goal)
        self.action_client.wait_for_result()
```

## Writing Transition Actions

Transition actions are actions that get run on transition between maps
in the world. Examples include door and elevator operation software. The
transition is simply an action server implementing the
MultiMapNavigationTransitionAction. We recommend hard-coding the server
name so that map files can easily access it. The transition action feeds
data to your code that may be of use. The first is the string
"wormhole" which contains the entire YAML data as a string of the
transition from the YAML map configuration file. The second are
"start" and "end" which contain the numeric index of the starting
and ending wormholes, which is useful to determine, e.g. what floor an
elevator should exit on.

## Examples

Two examples of the use of multi-map navigation exist for your robot.
The first is in the stage_multi_map_navigation package, which serves as
a simulator-based regression test of the entire multi-map navigation
system. See
<http://jks-ros-pkg.googlecode.com/svn/trunk/pr2_coffee/stage_multi_map_navigation>.

A second example is the PR2 coffee run code which can be found in
<http://jks-ros-pkg.googlecode.com/svn/trunk/pr2_coffee/pr2_specific>.
This contains less re-usable software for the PR2 to perform a coffee
run through our office. It thus contains software such as a elevator
management and door openning software for dealing the doors in our
building. These may or may not work for your environment and are
unsupported - however they serve as advanced examples of multi-map
navigation's ablities.

## TODO

\- Develop a GUI (rviz plugin?) for drag and drop creation of maps -
Develop an rviz plugin for placing the initial position of the robot and
goals - Improve code quality
