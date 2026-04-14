This page contains notes on using visual place recognition on the PR2
for localization, solving the kidnapped / wake-up robot problem.

At a high level, there will be a node that continuously gathers data for
performing place recognition as an already localized robot moves around
in the world. It may actively engage with the [navigation](navigation)
stack to stop and collect data when needed. This data is stored
persistently so we have it on robot wake-up.

It will have a ROS interface (action?) to attempt to localize using
place recognition when the robot is poorly localized (kidnapped or just
woken up).

## Gathering place data

Global pose estimates come from [amcl](amcl):

-   Can listen on \`/tf\` for \`odom\` to \`map\` transform.
-   And/or listen to \`/amcl_pose\` and only collect data for pose
    estimates with low covariance. We want AMCL to be well-localized
    when gathering data.

### Place database

At least for now, keep two separate databases. One in memory for doing
the place recognition prefilter. Another containing other associated
data (poses, keypoints, descriptors) for doing the geometric check and
pose estimation. Both are keyed on the \"document id\" for that image
(pair, for stereo).

An extension once basic system is working: replace old data when we
revisit a place to give some robustness to changing environment.

Place recognition database:

-   Already implemented as
    [vt::Database](http://www.ros.org/doc/api/vocabulary_tree/html/classvt_1_1Database.html).
-   Need to flush to disk periodically.
-   Or consider storing each \`DocumentVector\` in appropriate row of
    SQLite DB to keep everything in one place.
-   For replacing old data: will need to add methods to remove / replace
    a document.

Associated data for pose estimation:

-   Shove into a simple SQLite database.
-   Indexed on document id.
-   Each row contains:
-   Time stamp.
-   Pose in map frame from AMCL.
-   Transform from camera frame to \`odom\` as head will be moving.
-   Keypoints and descriptors (binary BLOB).
-   Spatial queries
-   Can start with simple \"sort on X, filter on Y\" scheme.
-   Drop in [SQLite R\*Tree module](http://www.sqlite.org/rtree.html)
    if/when we need better scalability.

### Getting sufficient coverage of building

When some distance (say \>2m) from any place already in database:

-   Check AMCL well localized.
-   Halt base movement - need to interact with [move_base](move_base)
    action. Talk to Eitan about most sensible way to do that.
-   Rotate head to get 4-8 frames of 360 degree surroundings.
-   For each frame, compute keypoints & descriptors, store with other
    metadata in SQLite. Quantize descriptors and add document to
    vocabulary tree database.
-   Allow robot to continue on.

Can publish markers of where we took samples to rviz to see where we
have coverage.

Would be nice to teleop robot around and have it just stop and collect
data when appropriate. Maybe simplest to hack up
[pr2_teleop](pr2_teleop) to allow place rec node to temporarily disable
responding to the joystick. Skip 180 degrees backwards view (?) since
someone will always be standing there.

Nicest would be for the robot to traverse the whole building
autonomously to gather / refresh its data, but that can be implemented
later.

## Localizing by place recognition

When action / service invoked:

-   Halt base movement if necessary.
-   Rotate head to get 4-8 frames.
-   Do place recognition against known places in database, with
    geometric check.
-   If we get a good match, publish to AMCL\'s \`initialpose\` topic to
    (re-)initialize the particle filter.
