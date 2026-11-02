## Overview

Mapviz is a ROS-based visualization tool with a plug-in system similar
to [rviz](https://index.ros.org/p/rviz) focused on visualization 2D
data.

![Screenshot of mapviz with several plugins active](doc/mapviz.png)

[Youtube](https://www.youtube.com/watch?v=3yy1J1Ci98c&rel=0)

## Plug-ins

See [Plugins](#plugins) for a list of existing
plugins.

## Plugins

### Overview

Mapviz is extensible, like
[rviz](https://index.ros.org/p/rviz), by writing plugins to display
different kinds of data. This page describes existing plugin types.

### Plugin Types



```clearsilver
name = Disparity
desc = Overlays a <<MsgLink(sensor_msgs/DisparityImage)>> onto the display using the "jet" color map.
param {
  0.name = Topic
  0.desc = disparity topic name
  0.type = string

  1.name = Anchor
  1.desc = position in display (options: top left | top center | top right | center left | center | center right | bottom left | bottom center | bottom right)
  1.type = enum

  2.name = Offset X
  2.desc = display offset from the left
  2.type = float

  3.name = Offset Y
  3.desc = display offset from the top
  3.type = float

  4.name = Width
  4.desc = display width
  4.type = int

  5.name = Height
  5.desc = display height
  5.type = int

  6.name = Units
  6.desc = units for offsets, width, and height
  6.type = pixels | percent of window
}
```





```clearsilver
name = GPS
desc = Projects <<MsgLink(gps_common/GPSFix)>> message data into the scene.
param {
  0.name = Topic
  0.desc = GPS topic name
  0.type = string

  1.name = Color
  1.desc = color of the GPS data
  1.type = color

  2.name = Draw Style
  2.desc = display style of GPS data
  2.type = lines | points | arrows

  3.name = Position Tolerance
  3.desc = distance threshold for adding new GPS points to visualization
  3.type = float

  4.name = Buffer Size
  4.desc = size of circular buffer of GPS points
  4.type = int
}
```





```clearsilver
name = Grid
desc = Projects a 2D grid into the scene.
param {
  0.name = Frame
  0.desc = coordinate frame of the grid
  0.type = string

  1.name = Color
  1.desc = color of the grid
  1.type = color

  2.name = Alpha
  2.desc = alpha transparency of the grid
  2.type = float

  3.name = X
  3.desc = x-offset of the grid from origin of coordinate frame
  3.type = float

  4.name = Y
  4.desc = y-offset of the grid from origin of coordinate frame
  4.type = float

  5.name = Size
  5.desc = size of each grid cell
  5.type = int

  6.name = Rows
  6.desc = number of grid rows
  6.type = int

  7.name = Columns
  7.desc = number of grid columns
  7.type = int
}
```





```clearsilver
name = Image
desc = Overlays a <<MsgLink(sensor_msgs/Image)>> onto the display
param {
  0.name = Topic
  0.desc = image topic name
  0.type = string

  1.name = Anchor
  1.desc = position in display (options: top left | top center | top right | center left | center | center right | bottom left | bottom center | bottom right)
  1.type = enum

  2.name = Offset X
  2.desc = display offset from the left
  2.type = float

  3.name = Offset Y
  3.desc = display offset from the top
  3.type = float

  4.name = Width
  4.desc = display width
  4.type = int

  5.name = Height
  5.desc = display height
  5.type = int

  6.name = Units
  6.desc = units for offsets, width, and height
  6.type = pixels | percent of window
}
```





```clearsilver
name = LaserScan
desc = Projects a <<MsgLink(sensor_msgs/LaserScan)>> message into the scene
param {
  0.name = Topic
  0.desc = laser scan topic name
  0.type = string

  1.name = Min Color
  1.desc = color associated with minimum return intensity
  1.type = color

  2.name = Max Color
  2.desc = color associated with maximum return intensity
  2.type = color

  3.name = Min Intensity
  3.desc = minimum intensity value
  3.type = float

  4.name = Max Intensity
  4.desc = maximum intensity value
  4.type = float

  5.name = Point Size
  5.desc = display size of laser scan points in pixels
  5.type = int

  6.name = Buffer Size
  6.desc = size of circular buffer of laser scan messages
  6.type = int
}
```





```clearsilver
name = Marker
desc = Projects a <<MsgLink(visualization_msgs/Marker)>> or <<MsgLink(visualization_msgs/MarkerArray)>> into the scene. [[rviz/DisplayTypes/Marker|Markers]] are the most flexible display type; they more or less mirror the [[https://www.opengl.org/wiki/Primitive|OpenGL primitives]].
param {
  0.name = Topic
  0.desc = marker topic name
  0.type = string
}
```





```clearsilver
name = Multi-res Image
desc = Projects a geo-referenced multi-resolution image tile map into the scene. The concept is the same as the Google Maps-style pan/zoom satellite imagery.
param {
  0.name = Geo File
  0.desc = Path to the geo-referenced map tiles; see [[mapviz/GeoFile]] for format
  0.type = string
}
```





```clearsilver
name = Odometry
desc = Projects <<MsgLink(nav_msgs/Odometry)>> message data into the scene.
param {
  0.name = Topic
  0.desc = odometry topic name
  0.type = string

  1.name = Color
  1.desc = color of the odometry data
  1.type = color

  2.name = Draw Style
  2.desc = display style of odometry data
  2.type = lines | points | arrows

  3.name = Show Covariance
  3.desc = draw covariance ellipse around latest data
  3.type = bool

  4.name = Position Tolerance
  4.desc = distance threshold for adding new odometry points to visualization
  4.type = float

  5.name = Buffer Size
  5.desc = size of circular buffer of odometry points
  5.type = int
}
```





```clearsilver
name = Path
desc = Projects <<MsgLink(nav_msgs/Path)>> message data into the scene
param {
  0.name = Topic
  0.desc = path topic
  0.type = string
}
```





```clearsilver
name = Robot Image
desc = Projects an image loaded from a file into the scene to represent the robot platform
param {
  0.name = Image File
  0.desc = path to image file
  0.type = string

  1.name = Frame
  1.desc = frame to which to tie the image
  1.type = string

  2.name = Width
  2.desc = physical width represented by the image
  2.type = float

  3.name = Height
  3.desc = physical height represented by the image
  3.type = float
}
```





```clearsilver
name = Textured Marker
desc = Projects <<MsgLink(marti_visualization_msgs/TexturedMarker)>> and <<MsgLink(marti_visualization_msgs/TexturedMarkerArray)>> message data into the scene. Textured markers follow the same general approach as traditional markers, but can be used to texture dense image data onto a [[https://www.opengl.org/wiki/Primitive#Quads|quad]] which is projected into the scene.
param {
  0.name = Topic
  0.desc = textured marker topic
  0.type = string
}
```





```clearsilver
name = Tile Map
desc = Projects a geo-referenced multi-resolution image tile map into the scene. Data is automatically streamed from [[http://open.mapquest.com/|OpenMapQuest]] (satellite and road data) or [[http://maps.stamen.com/|Stamen Design]] (terrain, watercolor, and toner). Custom or local map servers can also be specified. Map data is cached to disk, which enables some limited use when completely offline.
param {
  0.name = Source
  0.desc = source of the tile data
  0.type = string
}
```





```clearsilver
name = TF Frame
desc = Projects [[tf]] frames into the scene, similar to the [[mapviz#Odometry|Odometry]] plugin
param {
  0.name = Frame
  0.desc = tf frame
  0.type = string

  1.name = Color
  1.desc = color of the tf data
  1.type = color

  2.name = Draw Style
  2.desc = display style of tf data
  2.type = lines | points | arrows

  3.name = Position Tolerance
  3.desc = distance threshold for adding new tf points to visualization
  3.type = float

  4.name = Buffer Size
  4.desc = size of circular buffer of tf points
  4.type = int
}
```
