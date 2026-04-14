## ROS API

```clearsilver
node.0 {
name=virtualplume_node
desc=`virtualplume_node` is a wrapper for the !VirtualPlume library. Robots can access odor readings over a service and visualization of the plume is possible on [[rviz]] over the plumesim_markers topic.
srv{
0.name= ~read_virtualplume
0.type= virtualplume/ReadVirtualPlume
0.desc= Read the chemical value on the robot's current position.
}
pub{
0.name= ~virtualplume_markers
0.type= visualization_msgs/Marker
0.desc= Plume particles for visualization purposes.
}
param {
group.0 {
name=General Parameters
desc=The following parameters affect !VirtualPlume no matter the plume type.
0.name= ~type
0.default= 
0.type= string
0.desc= Type of plume. Accepted values are meadering, gaussian, fluent and pslog. Keep in mind that !VirtualPlume provides Gaussian and Meandering plumes as a quick and easy way to get started. These will not take obstacles into account, neither do they provide realistic chemical plume simulations. For that you should use [[http://en.wikipedia.org/wiki/Computational_fluid_dynamics | CFD]] software such as [[http://www.ansys.com/ | ANSYS]] Fluent. !PlumeSim accepts Fluent log files and plays them back in ROS. You can also use a pslog file containing data from your choice of [[http://en.wikipedia.org/wiki/Computational_fluid_dynamics | CFD]] software, your own plume generation algorithms or even from a recorded plume using a chemical sensor network.
1.name= ~global_frame_id
1.default= /map
1.type= string
1.desc= The frame_id in which odor readings and markers will be returned.
2.name= ~color/r
2.default= 1.0
2.type= float
2.desc= Red component of the RGB plume color.
3.name= ~color/g
3.default= 0.0
3.type= float
3.desc= Green component of the RGB plume color.
4.name= ~color/b
4.default= 0.0
4.type= float
4.desc= Blue component of the RGB plume color.
5.name= ~color/a
5.default= 0.9
5.type= float
5.desc= Alpha component of the color.
6.name= ~ns
6.default= plume
6.type= string
6.desc= Plume namespace.
7.name= ~id
7.default= 0
7.type= int
7.desc= Plume id.
8.name= ~frequency
8.default= 1.0
8.type= float
8.desc= Plume update frequency.
}
group.1 {
name=Meadering
desc=Parameters for the case of type=meadering.
0.name= ~releasepoint/x
0.default= 0.0
0.type= float
0.desc= Release point x.
1.name= ~releasepoint/y
1.default= 0.0
1.type= float
1.desc= Release point y.
2.name= ~releasepoint/z
2.default= 0.0
2.type= float
2.desc= Release point z.
3.name= ~arena/start/x
3.default= 0.0
3.type= float
3.desc= Arena start corner x.
4.name= ~arena/start/y
4.default= 0.0
4.type= float
4.desc= Arena start corner y.
5.name= ~arena/end/x
5.default= 0.0
5.type= float
5.desc= Arena send corner x.
6.name= ~number_of_points
6.default= 100
6.type= int
6.desc= Number of points to represent the plume.
7.name= ~release_rate
7.default= 10
7.type= float
7.desc= Plume release rate.
8.name= ~dispersion_coeficient
8.default= 0.06
8.type= float
8.desc= Plume dispersion coeficient.
9.name= ~radius
9.default= 0.1
9.type= float
9.desc= Plume reading bubble radius.
}
group.2 {
name=Gaussian
desc=Parameters for the case of type=gaussian.
0.name= ~releasepoint/x
0.default= 0.0
0.type= float
0.desc= Release point x.
1.name= ~releasepoint/y
1.default= 0.0
1.type= float
1.desc= Release point y.
2.name= ~releasepoint/z
2.default= 0.0
2.type= float
2.desc= Release point z.
3.name= ~arena/start/x
3.default= 0.0
3.type= float
3.desc= Arena start corner x.
4.name= ~arena/start/y
4.default= 0.0
4.type= float
4.desc= Arena start corner y.
5.name= ~arena/end/x
5.default= 0.0
5.type= float
5.desc= Arena send corner x.
6.name= ~cell_size
6.default= 0.01
6.type= float
6.desc= Cell size.
7.name= ~diffx
7.default= 0.0
7.type= float
7.desc= Something x.
8.name= ~diffy
8.default= 0.0
8.type= float
8.desc= Something y.
9.name= ~radius
9.default= 0.1
9.type= float
9.desc= Plume reading bubble radius.
10.name= ~max_points_per_cell
10.default= 10
10.type= int
10.desc= Maximum number of particles per cell.
}
group.3 {
name=Fluent
desc=Parameters for the case of type=fluent.
0.name= ~file_name
0.default= 
0.type= string
0.desc= Fluent log file name.
1.name= ~num_of_frames
1.default= 0
1.type= int
1.desc= Number of frames to read from the log file.
2.name= ~max_concentration
2.default= 1.0
2.type= float
2.desc= Maximum chemical concentration found on the log file.
3.name= ~max_points_per_cell
3.default= 10
3.type= int
3.desc= Maximum number of particles per cell.
4.name= ~cell_size
4.default= 0.01
4.type= float
4.desc= Cell size.
}
group.4 {
name=PSlog
desc=Parameters for the case of type=pslog.
0.name= ~file_name
0.default= 
0.type= string
0.desc= PSlog file name.
1.name= ~max_points_per_cell
1.default= 10
1.type= int
1.desc= Maximum number of particles per cell.
}
}
}
```

## PSLog

!PlumeSim allows you to run simulated plumes in ROS from a !VirtualPlume
log file called PSLog. These are merely .txt files with the following
structure: ```
Coming soon...
```

## Tutorials
