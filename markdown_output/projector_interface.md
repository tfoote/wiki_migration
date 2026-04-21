## Running

The easiest way to run the interface is alongside the
[projector calibration node](projector_calibration#grid). This can be
done with 

```bash
roslaunch projector_interface calibrate_and_circle.launch
```



This will start both the calibration node and interface node. The
interface node will wait to display anything until a homography is
available on the /homography parameter. After calibration, the
calibration node will exit.

At this point the interface node is ready to display the cursor, object
circles, and any polygons sent to it using the
<<SrvLink(projector_interface/DrawPolygon)>> service.

## Nodes



```clearsilver
node.0 {
  name = object_circler
  desc = Responsible for drawing the interface and dispatching click notifications if any objects in the interface have been clicked
  sub {
  
    0.name = object_cloud
    0.type = sensor_msgs/PointCloud2
    0.desc = A point cloud containing the centers of detected objects to be circled
  
    1.name = click
    1.type = std_msgs/Empty
    1.desc = Indicates that a click has been received
  
    2.name = intersected_points
    2.type = sensor_msgs/PointCloud2
    2.desc = A point cloud containing point intersections. These points are used to determine which object (if any) is being selected. This enables using multiple world models for object selection. If multiple models are not being used, this should be the same as intersected_points_cursor.
  
    3.name = intersected_points_cursor
    3.type = sensor_msgs/PointCloud2
    3.desc = A point cloud containing point intersections used to determine the current cursor location in the interface.
  
    4.name = camera_info
    4.type = sensor_msgs/CameraInfo
    4.desc = The camera calibration for the camera whose camera-projector homography is being used.
  }
  pub {
  
    0.name = selected_point
    0.type = geometry_msgs/PointStamped
    0.desc = After a click, this is the point that was clicked on.
  
    1.name = rate
    1.type = std_msgs/Empty
    1.desc = Published each time the interface is finished redrawing

    2.name = click_stats
    2.type = sensor_msgs/PointCloud2
    2.desc = Published the cursor history every time a click is received.
  
    3.name = clicked_object
    3.type = std_msgs/String
    3.desc = The object id for the object that was just clicked
  }
  srv {
  
    0.name = hilight_object
    0.type = projector_interface/HilightObject
    0.desc = Tells the interface to hilight a specific object
  
    1.name = clear_hilights
    1.type = projector_interface/ClearHilights
    1.desc = Clears all hilights
  
    2.name = get_cursor_stats
    2.type = projector_interface/GetCursorStats
    2.desc = Requests the current cursor history
  
    3.name = set_selection_method
    3.type = projector_interface/SetSelectionMethod
    3.desc = Enables changing the selection method for selecting circled objects.
  
    4.name = draw_polygon
    4.type = projector_interface/DrawPolygon
    4.desc = Adds a polygon for the interface to draw
  
    5.name = clear_polygons
    5.type = projector_interface/ClearPolygons
    5.desc = Clears all polygons
  }
  param {
  
    0.name = /homography
    0.type = string
    0.desc = The camear-projector homography
  
    1.name = ~flip
    1.type = string
    1.desc = Sets the top right of the display to be (0,0) rather than bottom left. Defaults to false.
  
    2.name = ~window_size
    2.type = string
    2.desc = Sets how much cursor history to use. Defaults to 10.
    
    3.name = ~circle_objects
    3.type = string
    3.desc = Sets whether or not to draw circles around detected objects (from object_cloud)
  }
}


node.1 {
  name = point_to_click
  desc = Takes a button press from a joystick and publishes a click. After a button press has been detected, won't publish another click for 1 second.
  sub {
  
    0.name = joy
    0.type = sensor_msgs/Joy
    0.desc = The joystick topic
  }
  pub {
  
    0.name = click
    0.type = std_msgs/Empty
    0.desc = Topic where clicks should be published.
  }
}


node.2 {
  name = find_objects
  desc = Calls the tabletop object detector and publishes a cloud of detected object centers.

  pub {
  
    0.name = object_cloud
    0.type = sensor_msgs/PointCloud2
    0.desc = Object center cloud topic
  
    1.name = table
    1.type = tabletop_object_detector/Table
    1.desc = Table information
  }

  param {
  
    0.name = ~detect_rate
    0.type = float
    0.desc = How frequently to call the detector. Defaults to once every 2 seconds (0.5).
  }
}


node.3 {
  name = manipulator
  desc = Goes between object_circler and PR2's object manipulation capabilities.
  sub {
  
    0.name = click
    0.type = std_msgs/Empty
    0.desc = Receives clicks when objects are clicked on
  
    1.name = intersected_points
    1.type = sensor_msgs/PointCloud2
    1.desc = Intersected points when there was a click
  }
  pub {
  
    0.name = place_pose
    0.type = geometry_msgs/PoseStamped
    0.desc = Publishes a pose where the object should be placed
  }
```


