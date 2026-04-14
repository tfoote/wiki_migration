## Overview

A component of the world canvas framework, a ROS stack for storing and
accessing semantic information about the world, with an initial emphasis
on needs and use cases for mobile robots.

World canvas server is a storage manager for semantic maps. Initial
version replicates map_store behavior for semantic maps.

### ROS APIs

```clearsilver
name = world canvas server
desc = world canvas server apis
srv {
  0.name = get_annotations
  0.type = world_canvas_msgs/GetAnnotations
  0.desc = queries annotations from database
  1.name = get_annotations_data
  1.type = world_canvas_msgs/GetAnnotationsData
  1.desc = queries annotations from database
  2.name = pub_annotations_data
  2.type = world_canvas_msgs/PubAnnotationsData
  2.desc = publishes annotations data
  3.name = delete_annotations
  3.type = world_canvas_msgs/DeleteAnnotations
  3.desc = removes annotations from database
  4.name = save_annotations_data
  4.type = world_canvas_msgs/SaveAnnotationsData
  4.desc = saves annotations data into database
  5.name = list_worlds
  5.type = world_canvas_msgs/ListWorlds
  5.desc = queries list of available worlds from database
  6.name = set_keyword
  6.type = world_canvas_msgs/SetKeyword
  6.desc = configure keyword for given annotation id
  7.name = set_relationship
  7.type = world_canvas_msgs/SetRelationship
  7.desc = configure relationship for given annotation id
  8.name = reset_database
  8.type = world_canvas_msgs/ResetDatabase
  8.desc = clear all information in database
  9.name = yaml_import
  9.type = world_canvas_msgs/YAMLImport
  9.desc = import data from yaml file into database
  10.name = yaml_export
  10.type = world_canvas_msgs/YAMLExport
  10.desc = export data in database as yaml file

  11.name = list_maps
  11.type = world_canvas_msgs/ListMaps
  11.desc = (LEGACY API from map store)
  12.name = publish_map
  12.type = world_canvas_msgs/PublishMap
  12.desc = (LEGACY API from map store)
  13.name = delete_map
  13.type = world_canvas_msgs/DeleteMap
  13.desc = (LEGACY API from map store)
  14.name = rename_map
  14.type = world_canvas_msgs/rename_map
  14.desc = (LEGACY API from map store)
  15.name = save_map
  15.desc = (LEGACY API from map store)
  15.type = world_canvas_msgs/SaveMap
  16.name = dynamic_map
  16.type = world_canvas_msgs/GetMap
  16.desc = (LEGACY API from map store)
}
param {
  0.name = ~start_map_manager
  0.default = False
  0.desc = enable Legacy api from map store
  1.name = ~last_map_id
  1.desc = param for map manager
  2.name = ~last_map_id
  2.desc = param for map manager
  3.name = ~auto_save_map
  3.default = False
  3.desc = param for map manager
}
```
