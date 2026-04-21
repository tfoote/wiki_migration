## Nodes



```clearsilver
node.0{
  name = mouse_click
  desc = Captures X click events and publishes them as clicks
  sub {
  }
  pub {
  
    0.name = click
    0.type = std_msgs/Empty
    0.desc = Published clicks. Note that click location is ignored.
  }
}


node.1 {
  name = world_intersect
  desc = Intersects a ray, represented as a pose with a point cloud.
  sub {
  
    0.name = cloud
    0.type = sensor_msgs/PointCloud2
    0.desc = The input pointcloud to be intersected with
  
    1.name = pose
    1.type = geometry_msgs/PoseStamped
    1.desc = A pose reprenting the pointing vector.
  }
  pub {
  
    0.name = intersected_points
    0.type = PointCloud
    0.desc = All points in the input cloud which are intersected by the pointing vector, as a PointCloud
  
    1.name = intersected_points
    1.type = sensor_msgs/PointCloud2
    1.desc = All points in the input cloud which are intersected by the pointing vector, as a PointCloud2
  
    2.name = intersected_point
    2.type = geometry_msgs/PointStamped
    2.desc = The single intersected point that is closest to the origin of the pointing vector.
  }
  param {
  
    0.name = vector_frame
    0.type = string
    0.desc = Defaults to std::string("intersected_vector")
  
    1.name = octree_resolution
    1.type = double
    1.desc = Defaults to 0.02
  
    2.name = min_dist
    2.type = string
    2.desc = Ignore points in the input cloud closer to the pointing vector origin than this.
  }
}

node.2 {
  name = intersect_plane
  desc = Find a ray-plane intersection.
  sub {
  
    0.name = pose
    0.type = geometry_msgs/PoseStamped
    0.desc = A pose reprenting the pointing vector.
  }
  pub {
  
    0.name = intersected_points
    0.type = sensor_msgs/PointCloud2
    0.desc = All points in the input cloud which are intersected by the pointing vector. This will only ever contain one point.
  }
  param {
  
    0.name = ~plane_frame
    0.type = string
    0.desc = The tf frame representing the plane to be intersected. The planes normal should be in the z direction.
  }
}
```


