This package implements point cloud registration, using the Normal
Distributions Transform. Two basic classes are available - point to
distributiuon registration (NDTMatcherP2D) and distribution to
distribution registration (NDTMatcherD2D). The point to distribution
algorithm is described
[here](http://aass.oru.se/Research/mro/publications/Magnusson_etal_2007-JFR-3D_Scan_Registration_for_Autonomous_Mining_Vehicles.html)
and the distribution to distribution
[here](http://aass.oru.se/Research/mro/publications/Stoyanov_etal_2012-IJRR_Fast_and_Accurate_Scan_Registration_through_Minimization_of_the_Distance_between_Compact_3D_NDT_Representations.html).

## Documentation

Refer to CodeAPI for detailed description of the classes and interfaces.

## Example



```cplusplus
#include <ndt_matcher_d2d.h>
#include <pointcloud_utils.h>

int main() {
    double __res[] = {0.5, 1, 2, 4};
    std::vector<double> resolutions (__res, __res+sizeof(__res)/sizeof(double));
    lslgeneric::NDTMatcherD2D <pcl::PointXYZ,pcl::PointXYZ> matcherD2D (false,false,resolutions);
    Eigen::Transform<double,3,Eigen::Affine,Eigen::ColMajor> T;
    pcl::PointCloud<pcl::PointXYZ> cloud1,cloud2;
    //... load information into cloud1 and cloud2 ...
    bool ret = matcherD2D.match2D(cloud1,cloud2,T);
    //we now have T, which minimizes |cloud1 - cloud2*T| 
    lslgeneric::transformPointCloudInPlace<pcl::PointXYZ>(T,cloud2);
}
```



## Nodes
