## Overview

The \`lj_costmap\` package is a localizing jockey for the Large Maps
Framework ([LaMa](Large Maps Framework)) that computes place
dissimilarities based on a local cost map, such as those obtained from
the [local_map](local_map) package.

The role of this jockey is to get the dissimilarity of the
\<\<MsgLink(lama_msgs/PlaceProfile)\>\> descriptors of all vertices with
the current place profile. The action is done when the dissimilarities
are computed. Implemented actions:

-   \`GET_VERTEX_DESCRIPTOR\`: return the PlaceProfile and the computed
    Crossing
-   \`GET_SIMILARITY\`: return the dissimilarity based on PlaceProfile

## Usage

### ROS API

#### Interaction with the map (created by this jockey)

  -- --------------------------- -- ----------------------------------------- -- ----------------------------------- --
     \[Getter\]\[/\]\[Setter\]      message type                                 interface default name              
     Getter/Setter                  \<\<MsgLink(lama_msgs/PlaceProfile)\>\>      jockey_name + \"\_place_profile\"   
     Setter                         \<\<MsgLink(lama_msgs/Crossing)\>\>          jockey_name + \"\_crossing\"        
  -- --------------------------- -- ----------------------------------------- -- ----------------------------------- --

```clearsilver
sub {
   0.name=~<name>/local_costmap
   0.type= nav_msgs/OccupancyGrid
   0.desc= local cost map which orientation is global, cf. [[local_map]].
}
srv {
  0.name= ~<name>/dissimilarity_server
  0.type= polygon_matcher/PolygonDissimilarity
  0.desc= used to compare all known places (as polygons) with the current place.
}
param {
  0.name= ~<name>/costmap_interface_name
  0.default= jockey_name + "_place_profile"
  0.type= String
  0.desc= Name of the map interface for place profiles.
  1.name= ~<name>/crossing_interface_name
  1.default= jockey_name + "_crossing"
  1.type= String
  1.desc= Name of the map interface for crossings.
  2.name= ~<name>/dissimilarity_server_name
  2.default= "dissimilarity_server"
  2.type= String
  2.desc= Name of the dissimilarity server.
}
```
