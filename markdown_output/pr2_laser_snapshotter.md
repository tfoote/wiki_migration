**Note:** in electric, this node can be found in the
[pr2_arm_navigation_perception](pr2_arm_navigation_perception) package.

## Nodes

```clearsilver
node.0 {
  name=pr2_laser_snapshotter
  desc=`pr2_laser_snapshotter` is a node that assembles a set of scans from a single sweep of the PR2's tilting laser into a point cloud, which is then published.
  pub{
    0.name= full_cloud
    0.type= sensor_msgs/PointCloud
    0.desc= The assembled point cloud from one sweep of the tilt laser is published here.
  }
  sub{
    0.name= laser_scanner_signal
    0.type= pr2_msgs/LaserScannerSignal
    0.desc= On receipt of this signal from the tilt laser controller, a cloud is assembled by calling the `assemble_scans` service.
  }
  srv_called{
    0.name= assemble_scans
    0.type= laser_assembler/AssembleScans
    0.desc= This service is called to acquire a point cloud from the set of scans that were published in between publications to `laser_scanner_signal`.  The service is usually implemented by [[laser_assembler]]/point_cloud_assembler.
  }
  param{
    0.name= ~num_skips
    0.type= int
    0.default= 0
    0.desc=  If set to N>0, then the snapshotter will skip N signals before requesting a new snapshot. This will make the snapshots be N times larger. N=0 - no skipping.
  }
``` ```clearsilver
node.0 {
  name=point_cloud_srv
  desc=`point_cloud_srv` is a node that assembles a set of scans from a single sweep of the PR2's tilting laser into a point cloud, which is then published.  It is similar to the `pr2_laser_snapshotter` node, with the difference that `point_cloud_srv`'s interface is a service through which the user can specify parameters for the tilt profile.
  srv{
    0.name= point_cloud_srv/single_sweep_cloud
    0.type= pr2_laser_snapshotter/BuildCloudAngle
    0.desc= Call this service to request a point cloud assembled from a single, customized sweep of the tilting laser.  The cloud is returned after the laser has executed one iteration of the requested sweep.
  }
  sub{
    0.name= laser_tilt_controller/laser_scanner_signal
    0.type= pr2_msgs/LaserScannerSignal
    0.desc= On receipt of this signal from the tilt laser controller, a cloud is assembled by calling the `build_cloud` service.
  }
  srv_called{
    0.name= build_cloud
    0.type= laser_assembler/AssembleScans
    0.desc= This service is called to acquire a point cloud from the set of scans that were published in between publications to `laser_scanner_signal`.  The service is usually implemented by [[laser_assembler]]/point_cloud_assembler.
    1.name= laser_tilt_controller/set_periodic_cmd
    1.type= pr2_msgs/SetPeriodicCmd
    1.desc= This service is called to configure the tilt laser with the sweep parameters that were received via the `point_cloud_srv/single_sweep_cloud` service.
  }
```

## Example

If you wanted to assemble point clouds on the PR2, you could launch
something like this:

```
<launch>
  <node pkg="pr2_mechanism_controllers" type="send_periodic_cmd_srv.py"
        name="laser_cmd"
        args="laser_tilt_controller linear 10 1 .35" />

  <node type="laser_scan_assembler" pkg="laser_assembler"
        name="tilt_scan_assembler">
    <remap from="scan" to="tilt_scan"/>
    <param name="max_scans" type="int" value="400" />
    <param name="fixed_frame" type="string" value="base_link" />
    <param name="ignore_laser_skew" type="bool" value="true" />
  </node>

  <node pkg="pr2_laser_snapshotter" type="pr2_laser_snapshotter" output="screen"
        name="snapshotter">
    <remap from="laser_scanner_signal"
           to="/laser_tilt_controller/laser_scanner_signal"/>
    <remap from="full_cloud" to="tilt_laser_cloud" />
  </node>
</launch>
```
