## Overview

This package implements the next best view estimation for the needs of
the mobile 3D semantic mapping. As the mobile robot enters the room, it
turns and scans repeatedly to get as much information as possible about
its surroundings. Then it estimates the next best view poses and drives
to a selected reachable location in the provided 2D map that would
increase the coverage of the scans further. It repeats the process until
it is deemed that the remaining occlusions are either too small or not
scannable by the sensor setup.

## Techniques

In greater detail, to obtain a list of suggested new scanning poses, we
make the following steps:

-   mark each voxel in the volume of the room as free, ocupied or
    unknown (the remaning ones) based on a\
    raytracing approach;
-   select those unknown voxels which have at least one free neighbor
    (meaning that they could be scanned in the next steps);
-   estimate the normals in some of the points of this boundary surface;
-   mark the connected components that have similar surface normals and
    filter those that are either too high or too low, as they are
    outside of the sensor's reach;
-   assume that the biggest surface patches cover bigger unknown
    volumes. Multiple scan poses that are directed towards the unknown
    space are then generated.

The following figures depict 3D point cloud of a household enviroment at
[IAS](http://ias.cs.tum.edu) and the estimated surfaces covering unknown
volumes after first scan: ![](attachment:firstshot.png)

After second scan:

![](attachment:second_shot.png)

After the third, final scan:

![](attachment:third_shot.png)

## Usage:

Please see tutorials on the right in order to learn about how to use
ODUFinder.
