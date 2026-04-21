## Overview

This package contains no ROS nodes or utility commands.

It provides C++ and Python classes and functions for working with
geodetic coordinate systems.

## C++ API

All C++ symbols defined by this package reside in the
[geodesy](http://ros.org/doc/api/geodesy/html/c++/namespacegeodesy.html)
namespace.

These coordinate types are currently supported, each with its own C++
header file:

### WGS 84

-   [<geodesy/wgs84.h>](http://docs.ros.org/hydro/api/geodesy/html/c++/wgs84_8h.html)

This is the base type for communicating geodetic information between ROS
nodes, using <<MsgLink(geographic_msgs/GeoPoint)>> and
<<MsgLink(geographic_msgs/GeoPose)>> messages.

### UTM

-   [<geodesy/utm.h>](http://docs.ros.org/hydro/api/geodesy/html/c++/utm_8h.html)

This is a slight generalization of the Universal Transverse Mercator
projection. It includes grid information from the Military Grid
Reference System, and can be extended to support Universal Polar
Stereographic zones at the poles, which are outside and supplementary to
the UTM scheme.

Being a Mercator projection, these coordinates permit local navigation
using a close approximation of Euclidean geometry, much simpler than the
ellipsoidal geometry of latitude and longitude.

## Python API

All Python modules defined by this package reside in the
[geodesy](http://ros.org/doc/api/geodesy/html/python/index.html)
namespace.

## Links

-   Geodesy
-   <http://en.wikipedia.org/wiki/Geographic_Information_System>
-   <http://en.wikipedia.org/wiki/Geodesy>
-   <http://en.wikipedia.org/wiki/World_Geodetic_System>

```{=html}
<!-- -->
```
-   UTM
-   <http://en.wikipedia.org/wiki/Universal_Transverse_Mercator>
-   <http://en.wikipedia.org/wiki/Military_grid_reference_system>
-   [UTM tutorial](http://www.uwgb.edu/dutchs/fieldmethods/utmsystem.htm)

```{=html}
<!-- -->
```
-   External software
-   [PROJ.4 Cartographic Projections Library](http://trac.osgeo.org/proj/wiki)
