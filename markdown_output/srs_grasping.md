## ROS API

This API is for grasp tasks with the SDH (Schunk Dextrous Hand). It
provides tools to generate/simulate different grasping solutions.

## Resources

To obtain the grasping solutions there are 2 services. The get_pregrasps
service is exclusive for the [srs_ui_but](srs_ui_but).

### Services

get_db_grasps (
[srs_grasping/GetDBGrasps](https://github.com/mrodriguez-robotnik/srs_public/blob/master/srs_grasping/srv/GetDBGrasps.srv))
Reads the grasping configurations from the database. If the info is not
stored, it tries to generate it. get_feasible_grasps (
[srs_grasping/GetFeasibleGrasps](https://github.com/mrodriguez-robotnik/srs_public/blob/master/srs_grasping/srv/GetFeasibleGrasps.srv))
Returns the feasible grasping configurations (in **/base_link**
coordinates system) for a given object ID and object pose.

get_pregrasps (
[srs_grasping/GetPreGrasp](https://github.com/mrodriguez-robotnik/srs_public/blob/master/srs_grasping/srv/GetPreGrasp.srv))
Return pregrasp configurations for a given position.

## Files

Simulate the generated grasp configurations in the OpenRAVE simulator.
```
scripts/test_simulation.py
``` A grasp task example. ```
scripts/test_simplegrasp.py
```
Obtains grasp configurations for a given object.
```
script/test_generator.py
```

This files contains all the methods used in the grasping tools.
```
src/databaseutils.py
src/operaveutils.py
src/graspingutils.py
``` This one contains an instance of each one:
```
src/grasping_functions.py
``` The services. ```
src/get_db_grasps.py
src/get_feasible_grasps.py
src/get_pregrasps.py
``` This
file launch all the services. ```
launch/grasping_services.py
```

This file contains the mesh of the hand. It\'s needed to calculate
grasps and other tasks. ```
robos/care-o-bot3.zae
```

## Installation

This ppackage depends on OpenRAVE. The faster option is to install
OpenRAVE from its repository: ```
sudo add-apt-repository ppa:openrave/release
sudo apt-get update
sudo apt-get install openrave
``` Another option is
to install the [openrave_planning](openrave_planning) package.

We recommend the first option to avoid configuration problems with
environment variables.

## Usage/Examples

The grasping tools calls the generator when the goal has not a grasping
info in the database. Internally, these tools needs to call some
[srs_object_database](srs_object_database) services. For that reason,
before use these tools you must launch the srs_db.launch file. More
details about the configuration and content of this file can be found in
the [srs_object_database](srs_object_database) wiki.
```
roslaunch srs_object_database srs_db.launch
``` After launch this file, you must launch:
```
scripts/test_simplegrasp.py
```0

At this point, you can use different grasp tools like the generator, the
simulator or the grasp_machine: ```
scripts/test_simplegrasp.py
```1
