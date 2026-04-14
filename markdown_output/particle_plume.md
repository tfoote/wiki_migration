## Overview

Particle Plume is a 3D odor mapping algorithm. It intends to tackle the
problems of plume intermittence, gas sensor noise and chemical data
sharing between robots when applicable.

Particle Plume represents plumes as point clouds using [PCL](PCL). A
grid of visited cells us also generated, allowing to distinguish between
visited locations with no odor present and locations which were not yet
visited.

## ROS API

```clearsilver
node.0 {
name=particle_plume_node
desc=`particle_plume_node` is a 3D odor mapping algorithm.
sub{
0.name= nose
0.type= lse_sensor_msgs/Nostril
0.desc= Gas sensor messages.
}
pub{
0.name= plume
0.type= sensor_msgs/PointCloud2
0.desc= The odor plume.

1.name= /visited_cells
1.type= nav_msgs/GridCells
1.desc= Visited cells.
}
param {
0.name= ~global_frame_id
0.default= map
0.type= string
0.desc= The global frame id.

1.name= ~bubble_radius
1.default= 0.10
1.type= double
1.desc= The radius of the bubble in meters inside which particles are generated for any given gas sensor reading.

2.name= ~max_particles_per_bubble
2.default= 1000
2.type= int
2.desc= The maximum number of particles generated inside a bubble, represents the maximum value given by the gas sensor.

3.name= ~particle_life_time
3.default= 0
3.type= int
3.desc= The time before each particle is removed after creation in minutes. 0 means the particle is never removed.

4.name= ~publish_frequency
4.default= 2.0
4.type= double
4.desc= The frequency at which the plume and the visited cells are published in Hz.

5.name= ~cell_size
5.default= 0.05
5.type= double
5.desc= Visited cell size. Should be equal to the navigation map cell size.

6.name= ~sensor_model
6.default= Figaro 2620
6.type= string
6.desc= The sensor model being used to generate the plume.
}
}
```

## Tutorials

Coming soon\...
