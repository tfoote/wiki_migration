## Collision Map Processing

This stack has two main roles:

-   add the results of the
    [tabletop_object_detector](tabletop_object_detector) to the
    collision environment
-   once added to the collision environment, an object gets a collision
    name which can be used later to reason about collision with that
    particular object.
-   recognized objects (from the database of models) get added to the
    collision environment as triangular meshes
-   unknown objects (segmented point clouds) get added to the collision
    map as bounding boxes
-   (optional) the table gets added to the collision map as a box
-   once added to the collision environment, an object (known or
    unknown) also gets repackaged as a
    [GraspableObject](http://www.ros.org/doc/api/object_manipulation_msgs/html/msg/GraspableObject.html),
    which can be provided as input to a Pickup or Place request sent to
    the [object_manipulator](object_manipulator).
-   acquire static collision maps using the tilting laser
-   the tilting laser is used to build an image of the environment
    beyond what is seen by the narrow stereo cameras
-   a complete laser scan is used to build a static collision map of the
    environment, which can be used for motion planning and collision
    avoidance
-   any objects present in the collision environment (such as the robot
    itself, or detected objects added in the previous step) are filtered
    out of the static collision map.
-   the static collision map can the thought of as containing the
    obstacles in the environment that we have no information on, except
    that they should not be collided with.

![](attachment:coll_map1.png)

\'\'Image of the Collision Map. Note the points from the tilting laser
(in cyan) and the explicitly recognized objects (in green)\'\'

![](attachment:coll_map2.png)

\'\'Detail of the Collision Map. Note that the recognized objects have
been added as triangle meshes, while the unrecognized object has been
added as a bounding box.\'\'

## ROS API

This package provides a single service,
[TabletopCollisionMapProcessing](http://www.ros.org/doc/api/tabletop_collision_map_processing/html/srv/TabletopCollisionMapProcessing.html),
which performs all of the above tasks.

## Running the Manipulation Pipeline

To launch the manipulation pipeline, complete with the sensor processing
provided here, and execute pickup and place tasks using the PR2 robot,
tutorials and launch files are provided in
[pr2_tabletop_manipulation_apps](pr2_tabletop_manipulation_apps).
