The `pm_mcc` package provides an implementation for polygon matching
for the Large Maps Framework ([LaMa](Large Maps Framework)). The
implementation is based on the Multi-scale Convexity Concavity Method:
Adamek, T. and O'Connor, N.E., "A multiscale representation method for
nonrigid shapes with a single closed contour", IEEE Transactions on
Circuits and Systems for Video Technology, 2004.

## Overview

The `pm_mcc` package provides an implementation for polygon matching
for the Large Maps Framework (LaMa). The implementation is based on the
Multi-scale Convexity Concavity Method: Adamek, T. and O'Connor, N.E.,
"A multiscale representation method for nonrigid shapes with a single
closed contour", IEEE Transactions on Circuits and Systems for Video
Technology, 2004.

## ROS API

### Services



```clearsilver
srv {
  0.name= ~<name>/compute_dissimilarity
  0.type= polygon_matcher/PolygonDissimilarity
  0.desc= Compute the dissimilarity between two polygons
}
```


