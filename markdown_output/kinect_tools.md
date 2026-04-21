#### Current status:

-   **1/23/2011:**
-   The Kinect tools package is obsolete. The content of kinect_tools
    has been split between:
-   [body_msgs](body_msgs)
-   [hand_interaction](hand_interaction)
-   [impromptu_buttons](impromptu_buttons)

[Youtube](https://www.youtube.com/watch?v=5nZSVjY_gNo)

## Hand Detector

This program detects hands. It is still very much under development, so
don't expect a whole lot of stability here! A stable version may appear
under the cturtle branch of mit-ros-pkg soon.

### Topics

#### Input

-   **/kinect/cloud** *PointCloud2* the kinect point cloud.
    **detecthands** will assume that the cloud is in the kinect frame.

#### Output

-   **/finger_norms** *PolygonalMap* gives the vectors of the fingers,
    as well as the direction of the arm
-   **/hand0_cloud** *PointCloud2* the fingers on the nearest hand
-   **/hand0_cloud2** *PointCloud2* the palm on the nearest hand
-   **/hand1_cloud** *PointCloud2* the fingers on the farthest hand
-   **/hand1_cloud2** *PointCloud2* the palm on the farthest hand
-   **hands** *Hands* the hands message, see below.

Hands are made available through the Hand/Hands message. A Hands message
is just two Hand messages with the header of the point cloud it came
from.

### Hand Field descriptions:

-   **thumb**: index of which finger was determined to be the thumb. a
    negative number means no thumb was detected, (does not mean no
    fingers)
-   **arm**: points near, bot not in the hand are clustered and marked
    as the arm. It is pretty accurate in giving the direction that the
    arm is facing.
-   **palm**: 6D pose of the palm (orientation may not be fully
    functional yet)
-   **fingers**: for each finger detected, the centroid is given.
    Because of how finger segmentation is done, this point will not
    always be the center of the finger, at least in the direction away
    from the palm.
-   **state**: Currently unused. Soon, when pointing is implemented,
    this will indicate what type of gesture is being made (ie: fist,
    peace, openpalm, etc.)

### Getting good detections

first off, this is still unstable! Work is being done to make detections
more reliable, while still maintaining 30fps. In the meanwhile, here are
some tips:

-   present your hand with fingers spread, palm facing the kinect
-   tilting currently hampers the finger segmentation
-   if your fingers are pointing toward the kinect, it often will not
    see them
-   your palm must be within 1m of the sensor. This is an arbitrary
    limit imposed by the clutter of my desk while I was developing the
    detector.
-   moving quickly presents motion blur, which is not compensated for.
    ![Effects of motion blur](attachment:motionblursmall.png)

### Current packages using Hand Detector

**Piano/pianist**

-   This is a (fairly finicky, for ppl not myself) program to play five
    notes.
-   when it detect five fingers, it will first say: "Hold still"
    indicating that it is waiting for your hand to remain at a fixed
    position, so it can set up a baseline.
-   When it says: fingers: <some numbers> you are ready to go!
-   if you dip your finger too much, it will lose sight of it, and it
    will do nothing if it does not see five fingers.
-   I set the distance threshold low, so you should not have to move
    much. [Youtube](https://www.youtube.com/watch?v=kf3G-DXqt6Y)
