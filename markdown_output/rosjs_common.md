# Overview

This is a package that provides libraries of functionality that is often
required for users using Javascript and [rosjs](rosjs) with the robot.
To include the functionality common.js should be added as a script to
the HTML.

# Provided Functionality

-   actionlib Javascript actionlib interface. Allows programmers to
    create action clients to interface with action servers running on
    the robot. This includes goal managing.
-   core Core functionality to simplify dealing with ROS.
-   Node Handle - allows programmers to handle a ROS node. Including but
    not limited to functions to advertise, publish, subscribe,
    unsubscribe, get topics, and get Services.
-   Publisher - allows programmers to publish ROS messages through
    publish funciton
-   Service Client - allows programmers to interact with ROS service
    through call and wait_for_service functions.
-   math Frequently used math functionality: quaternion, rotation,
    transform and 3-d vector operations
-   pcl Basic functionality to handle point cloud messages
-   roslib
-   Header handles ROS headers for messages
-   system provides interfaces for map, time and tree
-   tf provides code to easily work with TFs in Javascript.
-   urdf provides code to easily work with urdfs in Javascript.
-   widgets provides code to create and handle widgets with ROS
    functionality. Widgets are the recommended means of creating
    portable ROS web applications

# Code API Documentation

A documentation of the code can be found here:
<http://www.pr2-remotelab.com/jsdoc/rosjs_common/html/js/index.html>
