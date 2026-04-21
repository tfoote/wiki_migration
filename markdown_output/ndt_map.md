This package implements the NDT data structure. Several options for
constructing an NDT map are available.

## Documentation

For detailed documentation of the API, please refer to the doxygen
generated documentation. The main class of interest is NDTMap, which
provides several methods of constructing an NDT, given a point cloud of
the environment. A sample node that generates and saves NDT maps is also
provided.

### Spatial Indexing

NDT maps can be created either using a regular grid data structure
(LazyGrid) or using an irregular grid (OcTree). The recommended mode is
to use LazyGrid, as most of the subsequent algorithms have been
optimized for that data structure.

### NDT Cell

Each cell in the NDT map is stored as an NDTCell object, which stores
the mean and covariance of the point distribution in the cell. Points
used for computing the distribution are deleted after the cell is
created. Several update methods are available for adapting to new
measurements in the cell.

### Class API and usage

An example of how to create an NDT map from a point cloud:


```cplusplus
#include <ndt_map.h>
#include <lazy_grid.h>
#include <pcl/point_cloud.h>

int main() {
    //creates an empty grid with a resolution of 0.2 meters
    lslgeneric::LazyGrid<pcl::PointXYZ> grid(0.2);
    //the grid is only used as a prototype by the map
    //which will allocate a new empty grid
    lslgeneric::NDTMap<pcl::PointXYZ> nd(&grid);
    //create a pcl point cloud (and load data)
    pcl::PointCloud<pcl::PointXYZ> cloud;
    //load the point cloud in the ndt map, allocates memory for the grid 
    nd.loadPointCloud(cloud);
    //computes the distributions in each cell and deletes the points
    nd.computeNDTCells();
    //do something with the map ...
}
```



## Nodes
