## Overview

This package provides a C++ API for working with road map and coordinate
representations. These classes are exported in an \`artmap\` library.

There is also a ROS node that publishes a road map for the ART
autonomous vehicle to follow, plus some related test utilities.

## ROS Nodes

```clearsilver
node.0 {
 name = maplanes
 desc = Publish local and global road map for the ART vehicle.
 sub {  
  2.name = odom
  2.type = nav_msgs/Odometry
  2.desc = estimate of vehicle position and velocity
 }
 pub {
  3.name = roadmap_global
  3.type = art_msgs/ArtLanes
  3.desc = global road map lanes (latched topic)
  4.name = roadmap_local
  4.type = art_msgs/ArtLanes
  4.desc = local area road map lanes
 }
param {
0.name= ~poly_size
0.default= 2.5
0.type= double
0.desc=Minimum polygon size for road map lanes (m).
1.name= ~range
1.default= 80.0
1.type= double
1.desc=Publish local road map polygons within this radius (m).
2.name= ~rndf
2.default= ""
2.type= str
2.desc=Road Network Definition File name (required).
}
}
```

#### Examples

Run the ART map server, publishing \`roadmap_global\` and
\`roadmap_local\` messages using the RNDF from the 2007 DARPA site visit
at Southwest Research Institute.

```
$ roscd art_map
 $ rosrun art_map maplanes _rndf:=rndf/swri/site_visit.rndf
```

```clearsilver
node.0 {
 name = getpoints
 desc = Write out GPS data from the Applanix POS-LV to waypoint file. This file can then be used to generate RNDFs.
 sub {  
  2.name = gps
  2.type = art_msgs/GpsInfo
  2.desc = GPS data from Applanix POS-LV
 }
}
```

#### Usage

Run the getpoints node to collect waypoints. ```
$ rosrun art_map getpoints
```

Enter waypoints for lanes, zones or parking spots by pressing the
corresponding letter and \<Enter\>. ```
Valid instructions are:
 L record lane point
 P record zone perimeter point
 S record parking spot point
 E end the current lane or zone point list
 Q quit
```

Use the following command to convert waypoint file to RNDF
```
$ `rospack find art_map`/src/node/pointsToRNDF.rb waypoints.txt out.rndf
```

```clearsilver
node.0 {
 name = test_lanes
 desc = Road map test utility for ART RNDF.
}
```

#### Usage

```
$ rosrun art_map test_lanes --help
usage: test_lanes [options] RNDF_name

    Display RNDF lane information.  Possible options:
	-h, --help	print this message
	-i, --image	make .pgm image of polygons
	-y, --latitude	initial pose latitude
	-x, --longitude	initial pose longitude
	-s, --size	max polygon size
	-p, --print	print polygons to stdout
	-o, --output-points	print polygon points to polys.points
	-v, --verbose	print verbose messages
```
