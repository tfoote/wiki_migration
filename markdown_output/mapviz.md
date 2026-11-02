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

#### Disparity

Overlays a
[sensor_msgs/msg/DisparityImage](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/DisparityImage.html)
onto the display using the "jet" color map.

##### Parameters

- `Topic` (`string`): disparity topic name
- `Anchor` (`enum`): position in display (options: top left \| top
  center \| top right \| center left \| center \| center right \| bottom
  left \| bottom center \| bottom right)
- `Offset X` (`float`): display offset from the left
- `Offset Y` (`float`): display offset from the top
- `Width` (`int`): display width
- `Height` (`int`): display height
- `Units` (`pixels | percent of window`): units for offsets, width, and
  height

#### GPS

Projects
[gps_common/msg/GPSFix](https://docs.ros.org/en/rolling/p/gps_common/msg/GPSFix.html)
message data into the scene.

##### Parameters

- `Topic` (`string`): GPS topic name
- `Color` (`color`): color of the GPS data
- `Draw Style` (`lines | points | arrows`): display style of GPS data
- `Position Tolerance` (`float`): distance threshold for adding new GPS
  points to visualization
- `Buffer Size` (`int`): size of circular buffer of GPS points

#### Grid

Projects a 2D grid into the scene.

##### Parameters

- `Frame` (`string`): coordinate frame of the grid
- `Color` (`color`): color of the grid
- `Alpha` (`float`): alpha transparency of the grid
- `X` (`float`): x-offset of the grid from origin of coordinate frame
- `Y` (`float`): y-offset of the grid from origin of coordinate frame
- `Size` (`int`): size of each grid cell
- `Rows` (`int`): number of grid rows
- `Columns` (`int`): number of grid columns

#### Image

Overlays a
[sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)
onto the display

##### Parameters

- `Topic` (`string`): image topic name
- `Anchor` (`enum`): position in display (options: top left \| top
  center \| top right \| center left \| center \| center right \| bottom
  left \| bottom center \| bottom right)
- `Offset X` (`float`): display offset from the left
- `Offset Y` (`float`): display offset from the top
- `Width` (`int`): display width
- `Height` (`int`): display height
- `Units` (`pixels | percent of window`): units for offsets, width, and
  height

#### LaserScan

Projects a
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
message into the scene

##### Parameters

- `Topic` (`string`): laser scan topic name
- `Min Color` (`color`): color associated with minimum return intensity
- `Max Color` (`color`): color associated with maximum return intensity
- `Min Intensity` (`float`): minimum intensity value
- `Max Intensity` (`float`): maximum intensity value
- `Point Size` (`int`): display size of laser scan points in pixels
- `Buffer Size` (`int`): size of circular buffer of laser scan messages

#### Marker

Projects a
[visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)
or
[visualization_msgs/msg/MarkerArray](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/MarkerArray.html)
into the scene. [Markers](https://index.ros.org/p/rviz) are the most
flexible display type; they more or less mirror the
[OpenGL primitives](https://www.opengl.org/wiki/Primitive).

##### Parameters

- `Topic` (`string`): marker topic name

#### Multi-res Image

Projects a geo-referenced multi-resolution image tile map into the
scene. The concept is the same as the Google Maps-style pan/zoom
satellite imagery.

##### Parameters

- `Geo File` (`string`): Path to the geo-referenced map tiles; see
  [GeoFile](#geofile) for format

#### Odometry

Projects
[nav_msgs/msg/Odometry](https://docs.ros.org/en/rolling/p/nav_msgs/msg/Odometry.html)
message data into the scene.

##### Parameters

- `Topic` (`string`): odometry topic name
- `Color` (`color`): color of the odometry data
- `Draw Style` (`lines | points | arrows`): display style of odometry
  data
- `Show Covariance` (`bool`): draw covariance ellipse around latest data
- `Position Tolerance` (`float`): distance threshold for adding new
  odometry points to visualization
- `Buffer Size` (`int`): size of circular buffer of odometry points

#### Path

Projects
[nav_msgs/msg/Path](https://docs.ros.org/en/rolling/p/nav_msgs/msg/Path.html)
message data into the scene

##### Parameters

- `Topic` (`string`): path topic

#### Robot Image

Projects an image loaded from a file into the scene to represent the
robot platform

##### Parameters

- `Image File` (`string`): path to image file
- `Frame` (`string`): frame to which to tie the image
- `Width` (`float`): physical width represented by the image
- `Height` (`float`): physical height represented by the image

#### Textured Marker

Projects
[marti_visualization_msgs/msg/TexturedMarker](https://docs.ros.org/en/rolling/p/marti_visualization_msgs/msg/TexturedMarker.html)
and
[marti_visualization_msgs/msg/TexturedMarkerArray](https://docs.ros.org/en/rolling/p/marti_visualization_msgs/msg/TexturedMarkerArray.html)
message data into the scene. Textured markers follow the same general
approach as traditional markers, but can be used to texture dense image
data onto a [quad](https://www.opengl.org/wiki/Primitive#Quads) which is
projected into the scene.

##### Parameters

- `Topic` (`string`): textured marker topic

#### Tile Map

Projects a geo-referenced multi-resolution image tile map into the
scene. Data is automatically streamed from
[OpenMapQuest](http://open.mapquest.com/) (satellite and road data) or
[Stamen Design](http://maps.stamen.com/) (terrain, watercolor, and
toner). Custom or local map servers can also be specified. Map data is
cached to disk, which enables some limited use when completely offline.

##### Parameters

- `Source` (`string`): source of the tile data

#### TF Frame

Projects [tf](https://index.ros.org/p/tf) frames into the scene, similar
to the [Odometry](#odometry) plugin

##### Parameters

- `Frame` (`string`): tf frame
- `Color` (`color`): color of the tf data
- `Draw Style` (`lines | points | arrows`): display style of tf data
- `Position Tolerance` (`float`): distance threshold for adding new tf
  points to visualization
- `Buffer Size` (`int`): size of circular buffer of tf points

## GeoFile

Mapviz can display a geo-referenced
multi-resolution image tile map using its
[Multi-Res Image](#multi-res-image) plugin. The
concept is the same as the Google Maps-style pan/zoom satellite imagery.

![Multi-res satellite imagery](doc/mapviz_multires_image.png)

### File Format

The tile data is specified via a custom file format:



```
image_path: "."        # The relative path to the map tiles
image_width: 29184     # The full pixel width of the map
image_height: 15872    # The full pixel height of the map
tile_size: 512         # The pixel size of the individual tiles

datum: "wgs84"         # Datum is currently ignored
projection: "utm"      # (utm|wgs84)

                       # At least 2 tie points are required for 
                       # scale, and 3 for orientation.
tiepoints:             #   [pixel x, pixel y, geo x, geo y]
 - point: [4799, 209, 535674.5, 3258382.5]
 - point: [2336, 15596, 535329.5, 3256198.5]
 - point: [26925, 15457, 538837.5, 3256233.5]
 - point: [29133, 84, 539142.5, 3258416.5]
```



The plugin transforms the tiles to best match the tie point pixel
locations with the corresponding geographic locations in the scene.

### Tile Storage

Map tiles are stored in directories for each resolution starting
`layer0`, the full (highest) resolution. In subsequent layers, the
resolution is halved until the entire map fits within a single tile.

Tiles are named using the following format:



```
tile%05dx%05d.png% (row, column)
```



For example, the top-left tile in any layer will be called
tile00000x00000.png.
