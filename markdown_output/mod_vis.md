## Visualization canvas

Instances in the knowledge base can be pushed to the visualization
canvas, are then drawn, and can be further inspected. Currently
supported: Action sequences, linked to the resp. human pose sequence, as
well as most objects that are relevant in the IAS kitchen.

The visualization is written in [Processing](http://processing.org) and
Java.

You can navigate the display with the following commands:

-   press & drag left mouse button: rotate display
-   press & drag right mouse button: shift display
-   press & drag center mouse button: zoom
-   left/right arrow keys: scroll through a pose sequence
-   page up/page down: quick scrolling through a pose sequence

## Communication visualization applet

This is a small applet for visualizing communication that is being
performed. There are two images for the sending and receiving entity
that can be changed on-line plus two text fields where the query and
response strings can be visualized.

The applet offers four services for changing these four fields, all of
which accept a string that is either visualized or used as a file name
to load an image.

```
comm_vis_set_left_img
comm_vis_set_right_img
comm_vis_set_req_text
comm_vis_set_res_text
```

Launch with ```
rosrun mod_vis communication_vis
```

You can either call the services directly or, from within Java, use the
wrapper function in the CommunicationVisApplet class:
```
CommunicationVisApplet.visualizeCommunication("Retrieving model...", "", null, "cop.png");
```

## Visualization of task descriptions

See here for documentation:
<http://www.knowrob.org/doc/plan_visualization>
