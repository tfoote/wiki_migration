This package can also be used as an (advanced) example for using the C++
sql database interface. A simpler example is provided in the
[database interface tutorials](http://www.ros.org/wiki/database_interface/Tutorials).

This database is mainly used by our manipulation pipeline, which is
described in detail on the [object_manipulator](object_manipulator)
package page.

## Overview

The household_objects_database is a thin C++ and ROS wrapper for an SQL
database used for recognition and manipulation. Its main role is to

-   provide C++ data types for the data contained in the database;
-   provide easy to use C++ functions for the the most commonly used
    queries;
-   provide a ROS node wrapper for the most commonly used data queries
    so that they are accessible over ROS topics or services.

## The Database

For a detailed description of the database itself as a SQL entity, its
schema, the data that is contains and the design decisions behind it,
see the [household objects](household objects) page.

## ROS Node Wrapper and ROS API

The ROS node wrapper provides some of the most common database queries
as ROS services. It requires the following node parameters on startup to
establish a connection with the database server:

-   \`/household_objects_database/database_host\`: the address of the
    database server
-   \`/household_objects_database/database_port\`: the port to establish
    the connection on
-   \`/household_objects_database/database_user\`: the database username
-   \`/household_objects_database/database_password\`: the password for
    the database username
-   \`/household_objects_database/database_name\`: the name of the
    database to connect to

Once started, the wrapper node provides the following ROS services:

-   [GetModelList](http://www.ros.org/doc/api/household_objects_database_msgs/html/srv/GetModelList.html):
    retrieves a list of models available in the database
-   [GetModelMesh](http://www.ros.org/doc/api/household_objects_database_msgs/html/srv/GetModelMesh.html):
    gets the 3D mesh for a given model
-   [GetModelDescription](http://www.ros.org/doc/api/household_objects_database_msgs/html/srv/GetModelDescription.html):
    gets a set of descriptive meta-data for a given model
-   [GraspPlanning](http://www.ros.org/doc/api/object_manipulation_msgs/html/srv/GraspPlanning.html):
    retrieves a list of database grasps for the given model. In order to
    provide this service, the node will also look on the parameter
    server for a description of the arm being used. See the
    [pr2_object_manipulation_launch](pr2_object_manipulation_launch)
    package for an example of this description.

In general, information about database objects recognized in the
robot\'s environment are passed around the system in the form of
[DatabaseModelPose](http://www.ros.org/doc/api/household_objects_database_msgs/html/msg/DatabaseModelPose.html)
messages.

## Using the Database

### Install the database on your local machine

You can download a database backup file and install it on a local
database server. Has the advantage that the database is local and can be
modified. Here is how you can do it:

-   [install a PostgreSQL server](sql_database/Tutorials/Installing a PostgreSQL Server)
    on one of your machines
-   [install the household_objects database](household_objects_database/Tutorials/Install the household_objects database on your local database server)
    on your server.

### Remote ROS access to database hosted at Willow Garage

Note that remote read-only access to a server hosted at Willow Garage is
\'\'\'no longer officially supported\'\'\'. The infrastructure is still
available, but the overhead of keeping the ROS wrapper always up at
Willow ended up being too high.

If you\'d like to set up that service for yourself, the documentation
for the client side is still at
[tutorial for remote use of the database](household_objects_database/Tutorials/Use the household_objects_database remotely from a Willow Garage server).
