## Overview

The topic_logger package provides a SimpleActionServer which allows
users to record bag-files. The topic_logger SimpleActionServer expects a
goal which consists of a command (string), an ID (string) and the topics
(vector of strings) that should be recorded. The SimpleActionServer
checks the goal whether a start or a stop of recording is required. If a
start is required he starts recording the topics specified in the goal
to a bag-file and replies periodically the current file size of the
bag-file as feedback. If a stop is required he stops recording data
uploads the bag-file to a web server, deletes the local copy of the
bag-file and replies the link to the uploaded bag-file as result. The
topic_logger SimpleActionServer is supposed to work with the
loggerwidget, which can be found in rosjs_remotelabwidgets, as the
accompanying SimpleActionClient.

![](attachment:architecture.jpg)

## Running the topic_logger node

Before launching the topic_logger node you have to make this package
using: ```
rosmake topic_logger
``` Afterwards you can launch the node
using: ```
roslaunch topic_logger topicLogger_server.launch
``` This launch-file launches the node and
sets several parameters on the ROS parameter server which are needed to
execute the node. The parameters are:

-   localWorkDirectory_topicLogger : defines the work directory for the
    node in which the local copy of the bag-file will be stored
    temporarily
-   keyfileDirectory_topicLogger : defines the directory in which the
    keyfile is stored. The keyfile is needed to connect to the web
    server
-   usernameWebserver_topicLogger : defines the user name with which the
    node connects to the web server
-   URLWebserver_topicLogger : defines the URL of the web server to
    which the bag-files will be uploaded
-   BaseURLWebserver_topicLogger : defines the base URL of the web
    server. This is needed to create the link for the result
