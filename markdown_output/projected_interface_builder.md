## Usage

```
rosrun projected_interface_builder interface_builder.py -h
usage: interface_builder.py [-h] [-s] [savefile]

positional arguments:
  savefile          path to saved interface file

optional arguments:
  -h, --help        show this help message and exit
  -s, --standalone  standalone mode (startup fake service servers)
```

![](attachment:interface_builder.png)

Clicking anywhere in the main section starts drawing a polygon.
Successive clicks add vertices, and a polygon can be closed by double
clicking. While drawing a polygon, hovering near a point on the current
polygon or any other polygon in the interface will cause the cursor to
snap to that vertex.

Vertices can be modified after drawing a polygon by selecting the
polygon from the list and typing in values for x and y coordinates.The
polygon\'s name specifies text that is drawn in the interface, and the
ID is a unique ID used for referring to the polygon in code.

### Visualization

Pressing the \`Send Polygons\` button causes the interface to make a
service call to display the polygons, and also publishes a MarkerArray
for visualization in rviz. An example visualization is shown below.

![](attachment:interface_builder_viz.png)

### Units

All units are in meters. By default, the interface displays a grid with
\`5cm\` spacing. The x and y coordinates of the cursor are displayed in
meters in the status bar. When drawing a polygon, the line connecting
the last vertex and the cursor displays the length of the edge.

### Modifier Keys

-   **Shift**: snap to grid
-   **Ctrl+Shift**: axis-align
-   **Esc**: Cancels polygon drawing

## Nodes

```clearsilver

node.0 {
  name = interface_builder
  desc = GUI for building interfaces for use with [[projector_interface]].
  pub {  
    0.name = /polygon_viz
    0.type = visualization_msgs/MarkerArray
    0.desc = Visualization of the interface for use with rviz.
  }
```
