## Overview

t2obj stand for table-top object. It is a library for segmenting out
objects on top of a table using 3d point-clouds. Part of its codes are
extracted from recognition_lambertian pkg. It allow you fit a
table-plane with a prior knowledge of the plane orientation and segment
out the object candidate locations.

## Examples

It is used by rf_detector to generate object candidates before applying
the detector. Please look into RFPcdHogShapeDetector.cpp for more
details.
