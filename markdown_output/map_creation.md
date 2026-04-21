[cyphy_people_mapping](cyphy_people_mapping):[people_tracker](people_tracker)/[trajectory_clustering](trajectory_clustering)/map_creation

## Installation

In order for the nodes to render properly you must have a version of
rviz where the map_display plugin supports continuous values. Later
versions of rviz have this.

Otherwise, you'll need to edit the file map_display.cpp in
\.../rviz/src/rviz/default_plugin directory. Scroll down to
approximately line 314 and look for the code

```
for( unsigned int pixel_index = 0; pixel_index < num_pixels_to_copy; pixel_index++ )
  {
    unsigned char val;
    if(msg->data[ pixel_index ] == 100)
        val = 0;
    else if(msg->data[ pixel_index ] == 0)
        val = 255;
    else
        pixels[ pixel_index ] = val;
  }
```

create an overlay of rviz in your own workspace, and replace the above
code with

```
for( unsigned int pixel_index = 0; pixel_index < num_pixels_to_copy; pixel_index++ )
  {
    unsigned char val;

    if(msg->data[ pixel_index] == -1)
        val = 127;
    else
        val = (100 - msg->data[ pixel_index ])/100*255 ;

    pixels[ pixel_index ] = val;
  }
```

## Running the node

```
rosrun map_creation map_creation
```
