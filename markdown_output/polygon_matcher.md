The `polygon_matcher` package provides messages and a simple
implementation for polygon matching for the Large Maps Framework
([LaMa](Large Maps Framework)).

## Overview

The `polygon_matcher` package provides messages and a simple
implementation for polygon matching for the Large Maps Framework.
Polygon matching is used in the !LaMa Framework to recognize already
visited places (map vertices).

## ROS API

<<MsgSrvDoc(polygon_matcher)>>

### Services

```clearsilver
srv {
  0.name= ~<name>/simple_polygon_dissimilarity
  0.type= polygon_matcher/PolygonDissimilarity
  0.desc= Compute the distance of each point in polygon 1 to each point in polygon 2
}
```
