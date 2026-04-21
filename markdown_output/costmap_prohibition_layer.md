# Overview

This package includes a plugin to add prohibited areas to the
costmap-2D. The user is able to define those areas in a YAML file in
world coordinates. Prohibited ares can have three different forms:

  -- ----- -- -- -- ------------------------ -- -- -- ------------ --
     1\.            only a single point               1\*\[x,y\]   
     2\.            a line                            2\*\[x,y\]   
     3\.            a polygon with n edges            n\*\[x,y\]   
  -- ----- -- -- -- ------------------------ -- -- -- ------------ --

The plugin reads at initializing the costmap all the parameters from the
ROS-parameter server and set the costs of this areas to LETHAL.

**Warning:** If used in combination with a local costmap, make sure that
the global-frame parameter of the local costmap coincides with global
costmap's parameter. Furthermore, the global-frame should be fixed
(e.g. /map and not /odom), since currently no coordinate transformations
are performed internally.

# Configuration

## Declare the prohibition areas

To declare your prohibition areas you need to detect the coordinates in
the map (e.g. with Rviz). This coordinates you can fill into a YAML file
with the following structre:



```
prohibition_areas:
 # your first prohibited area is only a point
 - [17.09, -6.388]
 # now we define a line
 # it will become the thickness of the costmap resolution
 - [[8.33, 2.11],
    [8.26, 5.11]]
 # and last but not least a polygon with an individual number of points
 - [[-11.15, -15.614],
    [-12.35, -13.89],
    [-10.05, -12.218]]
```



## configure your global costmap plugin

The costmap2D from ros is able to add plugins (see
[Costmap2D Tutorial](http://wiki.ros.org/costmap_2d/Tutorials/Configuring%20Layered%20Costmaps)).
In step two you see how to add the YAML file to the parameters. If
you're doing this in the launch file of the move base, you should load
them into the namespace *global_costmap/costmap_prohibition_layer*. The
underlayed namespace (*costmap_prohibition_layer* should accord with the
plugin name, defined in the next step: In step three it is described how
to add the plugin itself. For this plugin you have to add:


```
plugins:
     # ... your own plugins     
     - {name: costmap_prohibition_layer,       type: costmap_prohibition_layer_namespace::CostmapProhibitionLayer"}
```



  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     <tablewidth="90%" #E0E0FF> **NOTE:** If you're using the inflation_layer and want, that your prohibitions get also inflated you have to add the costmap_prohibition_layer plugin above the inflation_layer plugin.   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
