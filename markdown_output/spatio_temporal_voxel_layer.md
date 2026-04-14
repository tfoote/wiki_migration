## Overview

The spatio-temporal voxel layer incorporates information from the
sensors in the form of PointClouds or LaserScans. This information is
converted into 3D and populated into an efficient voxel grid for each
sensor cycle.

ROS drop in replacement to the voxel layer which uses OpenVDB\'s
lightening fast voxel representation originally created for Dreamworks\'
animations. It runs at significantly less CPU than the existing
voxel_layer plugin using the voxel_grid structure.

Created in response to need for a more efficient voxel grid to process
10+ high resolution depth sensors in parallel and reduce the CPU load of
the move_base process.

It also introduces the concept of global and local voxel decay, which
temporally and spatially decays voxels rather than raycasting. We find
major improvements in performance and usability in highly dynamic
spaces. OpenVDB\'s efficient iterators and speed allow for this new
technique and is suitable for outdoor environments as well as indoor. It
also allows for more complex inputs to costmap_2d in the form of
clustered or tracked depth blobs.

More information, ROS API, demos, and resources are given in the
[GitHub](https://github.com/SteveMacenski/spatio_temporal_voxel_layer)
page.

You can find this work
<https://journals.sagepub.com/doi/10.1177/1729881420910530>.

\@article{<doi:10.1177/1729881420910530>, author = {Steve Macenski and
David Tsai and Max Feinberg}, title ={Spatio-temporal voxel layer: A
view on robot perception for the dynamic world}, journal =
{International Journal of Advanced Robotic Systems}, volume = {17},
number = {2}, year = {2020}, doi = {10.1177/1729881420910530}, URL =
{<https://doi.org/10.1177/1729881420910530>} }
