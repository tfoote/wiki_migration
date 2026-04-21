The body_msgs messages are used many of the
[ MIT Kinect Demos](mit-ros-pkg/KinectDemos).

# Messages

## Hands

A Hands message is just two Hand messages with the header of the point
cloud it came from.

### Hand Field descriptions:

-   **thumb**: index of which finger was determined to be the thumb. a
    negative number means no thumb was detected, (does not mean no
    fingers)
-   **arm**:
-   in **detecthands**: points near, but not in the hand are clustered
    and marked as the arm. It is pretty accurate in giving the direction
    that the arm is facing.
-   in **detectskelhands**: arm represents the skeleton\'s elbow.
-   **palm**: 6D pose of the palm (orientation may not be fully
    functional yet)
-   **fingers**: for each finger detected, the centroid is given.
    Because of how finger segmentation is done, this point will not
    always be the center of the finger, at least in the direction away
    from the palm.
-   **state**: Currently unused. Soon, when pointing is implemented,
    this will indicate what type of gesture is being made (ie: fist,
    peace, openpalm, etc.)

## Skeletons

A Skeletons message is a list of Skeleton messages with a header.

### Skeleton Field descriptions:

-   **joints** The joints are pretty self explanatory. They are the 3d
    position of that joint, plus a confidence. Generally the joints are
    trusted if the confidence is \> .5
-   **id** The id of the user.
