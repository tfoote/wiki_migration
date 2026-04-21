## Algorithms

Many of the algorithms and their parameters are well-described in the
book Probabilistic Robotics, by Thrun, Burgard, and Fox. The user is
advised to check there for more detail. In particular, we use the
following algorithms from that book:
**\`sample_motion_model_odometry\`**, **\`beam_range_finder_model\`**,
**\`likelihood_field_range_finder_model\`**, **\`Augmented_MCL\`**, and
**\`KLD_Sampling_MCL\`**.

As currently implemented, this node works only with laser scans and
laser maps. It could be extended to work with other sensor data.

## Example

To localize using laser data on the \`base_scan\` topic:
```
amcl scan:=base_scan
```

## Nodes

```clearsilver
node.0 {
  name=amcl
  desc=`amcl` takes in a laser-based map, laser scans, and transform messages, and outputs pose estimates. On startup, `amcl` initializes its particle filter according to the parameters provided.  Note that, because of the defaults, if no parameters are set, the initial filter state will be a moderately sized particle cloud centered about (0,0,0).
  sub{
    0.name= scan
    0.type= sensor_msgs/LaserScan
    0.desc= Laser scans.
    1.name= tf
    1.type= tf/tfMessage
    1.desc= Transforms.
    2.name= initialpose
    2.type= geometry_msgs/PoseWithCovarianceStamped
    2.desc= Mean and covariance with which to (re-)initialize the particle filter.
    3.name= map
    3.type= nav_msgs/OccupancyGrid
    3.desc= When the `use_map_topic` parameter is set, AMCL subscribes to this topic to retrieve the map used for laser-based localization. '''New in navigation 1.4.2.'''
  }
  pub{
    0.name= amcl_pose
    0.type= geometry_msgs/PoseWithCovarianceStamped
    0.desc= Robot's estimated pose in the map, with covariance.
    1.name= particlecloud
    1.type= geometry_msgs/PoseArray
    1.desc= The set of pose estimates being maintained by the filter.
    2.name= tf
    2.type= tf/tfMessage
    2.desc= Publishes the transform from `odom` (which can be remapped via the ~odom_frame_id parameter) to `map`.
  }
  srv{
    0.name=global_localization 
    0.type= std_srvs/Empty
    0.desc= Initiate global localization, wherein all particles are dispersed randomly through the free space in the map.
    1.name=request_nomotion_update 
    1.type= std_srvs/Empty
    1.desc= Service to manually perform update and publish updated particles.
    2.name=set_map 
    2.type= nav_msgs/SetMap
    2.desc= Service to manually set a new map and pose.
}
  srv_called{
    0.name=static_map 
    0.type= nav_msgs/GetMap
    0.desc= amcl calls this service to retrieve the map that is used for laser-based localization; startup blocks on getting the map from this service.
  }
```

#### Parameters

There are three categories of ROS [Parameters](Parameters) that can be
used to configure the \`amcl\` node: overall filter, laser model, and
odometery model.

##### Overall filter parameters

```clearsilver
param {
  no_header=True
  0.name= ~min_particles
  0.default=100
  0.type= int
  0.desc= Minimum allowed number of particles.
  1.name= ~max_particles
  1.default=5000
  1.type= int
  1.desc= Maximum allowed number of particles.
  2.name= ~kld_err
  2.default=0.01
  2.type= double
  2.desc= Maximum error between the true distribution and the estimated distribution.
  3.name= ~kld_z
  3.default=0.99
  3.type= double
  3.desc= Upper standard normal quantile for (1 - p), where p is the probability that the error on the estimated distrubition will be less than `kld_err`.
  4.name= ~update_min_d
  4.default=0.2 meters
  4.type= double
  4.desc= Translational movement required before performing a filter update.
  5.name= ~update_min_a
  5.default=&pi;/6.0 radians
  5.type= double
  5.desc= Rotational movement required before performing a filter update.
  6.name= ~resample_interval
  6.default=2
  6.type= int
  6.desc= Number of filter updates required before resampling.
  7.name= ~transform_tolerance
  7.default=0.1 seconds
  7.type= double
  7.desc= Time with which to post-date the transform that is published, to indicate that this transform is valid into the future.
  8.name= ~recovery_alpha_slow
  8.default= 0.0 (`disabled`)
  8.type= double
  8.desc=Exponential decay rate for the slow average weight filter, used in deciding when to recover by adding random poses. A good value might be 0.001.
  9.name= ~recovery_alpha_fast
  9.default=0.0 (`disabled`)
  9.type= double
  9.desc= Exponential decay rate for the fast average weight filter, used in deciding when to recover by adding random poses. A good value might be 0.1.
  10.name= ~initial_pose_x
  10.default=0.0 meters
  10.type= double
  10.desc= Initial pose mean (x), used to initialize filter with Gaussian distribution.
  11.name= ~initial_pose_y
  11.default=0.0 meters
  11.type= double
  11.desc= Initial pose mean (y), used to initialize filter with Gaussian distribution.
  12.name= ~initial_pose_a
  12.default=0.0 radians
  12.type= double
  12.desc= Initial pose mean (yaw), used to initialize filter with Gaussian distribution.
  13.name= ~initial_cov_xx
  13.default=0.5*0.5 meters
  13.type= double
  13.desc= Initial pose covariance (x*x), used to initialize filter with Gaussian distribution.
  14.name= ~initial_cov_yy
  14.default=  0.5*0.5 meters
  14.type= double
  14.desc= Initial pose covariance (y*y), used to initialize filter with Gaussian distribution.
  15.name= ~initial_cov_aa
  15.default=(&pi;/12)*(&pi;/12) radian
  15.type= double
  15.desc=  Initial pose covariance (yaw*yaw), used to initialize filter with Gaussian distribution.
  16.name= ~gui_publish_rate
  16.default=-1.0 Hz
  16.type= double
  16.desc=  Maximum rate (Hz) at which scans and paths are published for visualization, -1.0 to disable.
  17.name= ~save_pose_rate
  17.default= 0.5 Hz
  17.type= double
  17.desc=  Maximum rate (Hz) at which to store the last estimated pose and covariance to the parameter server, in the variables ~initial_pose_* and ~initial_cov_*. This saved pose will be used on subsequent runs to initialize the filter. -1.0 to disable.
  18.name= ~use_map_topic
  18.type= bool
  18.default= false
  18.desc= When set to true, AMCL will subscribe to the `map` topic rather than making a service call to receive its map. '''New in navigation 1.4.2'''
  19.name= ~first_map_only
  19.type= bool
  19.default= false
  19.desc= When set to true, AMCL will only use the first map it subscribes to, rather than updating each time a new one is received. '''New in navigation 1.4.2'''
  20.name= ~selective_resampling
  20.type= bool
  20.default= false
  20.desc= When set to true, will reduce the resampling rate when not needed and help avoid particle deprivation. The resampling will only happen if the effective number of particles (''N_eff = 1/(sum(k_i^2))'') is lower than half the current number of particles. Reference: ''Grisetti, Giorgio, Cyrill Stachniss, and Wolfram Burgard. "Improved techniques for grid mapping with rao-blackwellized particle filters." IEEE transactions on Robotics 23.1 (2007): 34.''
}
```

##### Laser model parameters

Note that whichever mixture weights are in use should sum to 1. The beam
model uses all 4: z_hit, z_short, z_max, and z_rand. The
likelihood_field model uses only 2: z_hit and z_rand.

```clearsilver
param {
  no_header=True
  0.name= ~laser_min_range
  0.default=-1.0
  0.type= double
  0.desc= Minimum scan range to be considered; -1.0 will cause the laser's reported minimum range to be used. 
  1.name= ~laser_max_range
  1.default=-1.0
  1.type= double
  1.desc= Maximum scan range to be considered; -1.0 will cause the laser's reported maximum range to be used.
  2.name= ~laser_max_beams
  2.default= 30
  2.type= int
  2.desc=  How many evenly-spaced beams in each scan to be used when updating the filter.
  3.name= ~laser_z_hit
  3.default=0.95
  3.type= double
  3.desc=  Mixture weight for the z_hit part of the model.
  4.name= ~laser_z_short
  4.default=0.1
  4.type= double
  4.desc=  Mixture weight for the z_short part of the model.
  5.name= ~laser_z_max
  5.default=0.05
  5.type= double
  5.desc= Mixture weight for the z_max part of the model.
  6.name= ~laser_z_rand
  6.default=0.05
  6.type= double
  6.desc=   Mixture weight for the z_rand part of the model.
  7.name= ~laser_sigma_hit
  7.default=0.2 meters
  7.type= double
  7.desc= Standard deviation for Gaussian model used in z_hit part of the model.
  8.name= ~laser_lambda_short
  8.default=0.1
  8.type= double
  8.desc=Exponential decay parameter for z_short part of model.
  9.name= ~laser_likelihood_max_dist
  9.default=2.0 meters
  9.type= double
  9.desc= Maximum distance to do obstacle inflation on map, for use in likelihood_field model.
  10.name= ~laser_model_type
  10.default=`"likelihood_field"`
  10.type= string
  10.desc= Which model to use, either `beam`, `likelihood_field`, or `likelihood_field_prob` (same as `likelihood_field` but incorporates the beamskip feature, if enabled).
}
```

##### Odometry model parameters

If \`odom_model_type\` is \`\"diff\"\` then we use the
\`sample_motion_model_odometry algorithm\` from Probabilistic Robotics,
p136; this model uses the noise parameters \`odom_alpha1\` through
\`odom_alpha4\`, as defined in the book.

If \`odom_model_type\` is \`\"omni\"\` then we use a custom model for an
omni-directional base, which uses \`odom_alpha1\` through
\`odom_alpha5\`. The meaning of the first four parameters is similar to
that for the \`\"diff\"\` model. The fifth parameter capture the
tendency of the robot to translate (without rotating) perpendicular to
the observed direction of travel.

A [bug](https://github.com/ros-planning/navigation/issues/20) was found
and fixed. But fixing the old models would have changed or broken the
localisation of already tuned robot systems, so the new fixed odometry
models were added as new types \`\"diff-corrected\"\` and
\`\"omni-corrected\"\`. The default settings of the \`odom_alpha\`
parameters only fit the old models, for the new model these values
probably need to be a lot smaller, see
<http://answers.ros.org/question/227811/tuning-amcls-diff-corrected-and-omni-corrected-odom-models/>.

Also, another
[bug](https://github.com/ros-planning/navigation/issues/499) was found
but only fixed after Navigation 1.16, while the current release for
Kinetic is Navigation 1.14.1. This bug only affects robot with type
\`\"omni\"\` and \`\"omni-corrected\"\`, where \`odom_alpha1\` and
\`odom_alpha4\` are actually reversed. I.e. \`odom_alpha1\` is for the
translation odometry noise from robot translation-al motion, and
\`odom_alpha4\` represents the odometry rotation noise from robot\'s
rotation motion.

```clearsilver
param {
  no_header=True
  0.name= ~odom_model_type
  0.default=`"diff"`
  0.type= string
  0.desc= Which model to use, either `"diff"`, `"omni"`, `"diff-corrected"` or `"omni-corrected"`.
  1.name= ~odom_alpha1
  1.default=0.2
  1.type= double
  1.desc=  Specifies the expected noise in odometry's rotation estimate from the rotational component of the robot's motion.
  2.name= ~odom_alpha2
  2.default=0.2
  2.type= double
  2.desc= Specifies the expected noise in odometry's rotation estimate from translational component of the robot's motion.
  3.name= ~odom_alpha3
  3.default=0.2
  3.type= double
  3.desc= Specifies the expected noise in odometry's translation estimate from the translational component of the robot's motion.
  4.name= ~odom_alpha4
  4.default=0.2
  4.type= double
  4.desc= Specifies the expected noise in odometry's translation estimate from the rotational component of the robot's motion.
  5.name= ~odom_alpha5
  5.default=0.2
  5.type= double
  5.desc= Translation-related noise parameter (only used if model is `"omni"`).
  6.name= ~odom_frame_id
  6.default=`"odom"`
  6.type= string
  6.desc= Which frame to use for odometry.
  7.name= ~base_frame_id
  7.default= `"base_link"`
  7.type= string
  7.desc= Which frame to use for the robot base
  8.name = ~global_frame_id
  8.default = `"map"`
  8.type = string
  8.desc = The name of the coordinate frame published by the localization system
  9.name = ~tf_broadcast
  9.default= true
  9.type= bool
  9.desc = Set this to `false` to prevent amcl from publishing the transform between the global frame and the odometry frame.
}
```

#### Transforms

\`amcl\` transforms incoming laser scans to the odometry frame
(\`odom_frame_id\`). So there must exist a path through the [tf](tf)
tree from the frame in which the laser scans are published to the
odometry frame.

An implementation detail: on receipt of the first laser scan, \`amcl\`
looks up the transform between the laser\'s frame and the base frame
(base_frame_id), and latches it forever. So \`amcl\` cannot handle a
laser that moves with respect to the base.

The drawing below shows the difference between localization using
odometry and \`amcl\`. During operation \`amcl\` estimates the
transformation of the base frame (base_frame_id) in respect to the
global frame (\`global_frame_id\`) but it only publishes the transform
between the global frame and the odometry frame (\`odom_frame_id\`).
Essentially, this transform accounts for the drift that occurs using
Dead Reckoning. The published transforms are
[future dated](tf/FAQ#Why_do_I_see_negative_average_delay_in_tf_monitor.3F).

![\|width=\"750px\"](attachment:amcl_localization.png)
