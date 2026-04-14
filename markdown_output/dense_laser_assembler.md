## Stability

This package is still unstable, and does not have a released API.

## Overview

\'\'\'Terminology\'\'\'\
- \'\'\'Ray\'\'\' - A single range/intensity reading from a laser
scanner. Takes approx 17 &#965;s to acquire\
- \'\'\'Scan\'\'\' - Data collected during a single revolution of a
laser scanner. Takes approx 25 ms to acquire, and consists of 100\'s of
rays\
- \'\'\'Sweep\'\'\' - Data collected during monotonic motion of the
tilting_stage on the PR2. Usually takes 2-10 seconds to acquire, and
consists of 100\'s of scans\

Intensity and Range data from a single sweep are each stored in their
own Float32 multiarray. Each row of the multiarray stores data from a
single scan, and these rows are stacked (sorted by the tilting angle) to
form the \'rasterized\' dense representation. Note that we are not doing
any sort of perspective projection or interpolation or \'filling in\' of
the data. It is simply a set of stacked scans.

The assembler will also store timing and joint information. The
positions of requested joints are stored in another multiarray, with the
same number of rows as the range-data and intensity-data multiarrays.
Depending on what fidelity we need, we could either store a joint
position for the start of each scan, or a joint_position for each ray.

A \'typical\' Laser\`\`Scan message will also be published, providing
config information for each scan. This includes info like min-angle,
max-angle, angle-increment, time-increment, etc. Currently, we assume
that the config information is consistent across all scans in a dense
laser scan.

![](attachment:all_data_multiarrays.png)

These multiarrays are convenient, since they look very similar to
images. This makes it very easy to run openCV algorithms, such as
checkerboard detection, on the intensity data.

![](attachment:cb_image_corners.png)

## Dense Point Clouds

Assuming a client receives the published data and also knows the
pertinent parts of the robot\'s kinematics, the client can transform the
laser data into a \'dense point cloud\'. Ideally, this datatype will be
used for both dense laser data and stereo data. The first 3 32-Bit
fields will hold XYZ position data. The last 32-Bit field can hold
auxiliary data, such as intensity. This aux data could hopefully also
indicate whether the reading is valid. (eg. an intensity of 0 could
imply an invalid range reading). Note that the indexing isn\'t changed
between the dense_point_cloud and the original data, so both datasets
can still easily be correlated.

![](attachment:dense_point_cloud.png)

It is likely that the Dense\`\`Point\`\`Cloud could end up using
BinaryMultiArray as the underlying data structure.

If that is the case, then the scan stride can be chosen to be 16 bytes
regardless of whether or not 3 channels (X,Y,Z) or 4 channels (X,Y,Z,
validity) are used.
