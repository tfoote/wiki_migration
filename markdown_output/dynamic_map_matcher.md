## Algorithms

dynamic_map_matcher is a package for cooperative robots SLAM. It is
based on a regularized particle filter and the technical details will be
published once our paper "Dynamic map matching using particle
filtering" is published.

The main contribution of this package is its capability to work with any
SLAM algorithm that produces an occupancy grid based map. The provided
demo uses two hector_slam mappers.

## Example

[Youtube](https://www.youtube.com/watch?v=iqKVjtpLI8w)

## Nodes

```clearsilver
node.0 {
  name=map_matcher_node
  desc=`map_matcher_node` takes in two occupancy grid based map and outputs a global matched map. On startup, `map_matcher_node` initializes its particle filter according to the parameters provided.
  sub{
    0.name= origin_map
    0.type= nav_msgs/OccupancyGrid
    0.desc= Map of the first robot to be matched with the target map.
    1.name= target_map
    1.type= nav_msgs/OccupancyGrid
    1.desc= Target map to be matched.
  }

pub{
    0.name= global_map
    0.type= nav_msgs/OccupancyGrid
    0.desc= The estimated global map.
  }
}

}
```

```clearsilver
param {
  no_header=True
  0.name= /sequential_map_matcher/origin_map
  0.default=origin_map
  0.type= string
  0.desc= Topic name for the origin map.
  1.name= /sequential_map_matcher/target_map
  1.default=target_map
  1.type= string
  1.desc= Topic name for the target map.
  2.name= /sequential_map_matcher/n_particles
  2.default= 500
  2.type= int
  2.desc=  Number of particles to use, has an effect on the computation time.
  3.name= /sequential_map_matcher/n_observation
  3.default=500
  3.type= int
  3.desc=  Number of observation to use from the maps, has an effect on the computation time.
  4.name= /sequential_map_matcher/n_history
  4.default=5
  4.type= int
  4.desc=  Convolution history, how many time steps to affect weighting the particles. A good value is 5-10.
  5.name= /sequential_map_matcher/n_theta
  5.default=50
  5.type= int
  5.desc= Initialization count for the transformation angle.
  6.name= /sequential_map_matcher/n_x
  6.default=20
  6.type= int
  6.desc= Initialization count for the transition on the x axis.
  7.name= /sequential_map_matcher/n_y
  7.default=20
  7.type= int
  7.desc= Initialization count for the transition on the y axis.
  8.name= /sequential_map_matcher/R_var
  8.default=0.1
  8.type= double
  8.desc= Weighting coefficient for the particle filter likelihood function.
}
```

## References

This work is summarized in a yet to be published paper - "Dynamic map
matching using particle filtering".
