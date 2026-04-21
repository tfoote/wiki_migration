## Upgrading your code from Eigen2 to Eigen3

To prevent conflicts with `Eigen2` in packages that depend on both
`Eigen2` and `Eigen3`, the ROS version of `Eigen3` uses a
different namespace, `Eigen3`. In addition, all header files are in
the subdirectory `Eigen3` instead of `Eigen` now. eigen3 contains a
script that performs the necessary renaming automatically. You can run
it like this: ```
rosrun eigen3 rename_eigen_namespace `rospack find your_awesome_package`
```

If you still have problems, read
[this page](http://eigen.tuxfamily.org/dox-devel/Eigen2ToEigen3.html) to
understand what changed. If that doesn't help, continue reading.

While upgrading PCL 0.2.9 to `Eigen3`, we found the following issues:

### EIGEN_ALIGN_128

`EIGEN_ALIGN_128` doesn't seem to exist anymore in `Eigen3`. Use
`EIGEN_ALIGN16` instead, which is defined as: ```
#define EIGEN_ALIGN16 EIGEN_ALIGN_TO_BOUNDARY(16)
```
in Macros.h

### Eigen::ForceAligned

`Eigen2` had `Eigen::ForceAligned` defined in
`Core/util/Constants.h`, and its behavior seemed to be confusing. In
`Eigen3`, `ForceAligned` was dropped, and we should use
`Eigen::Aligned` instead. Check
[this thread](http://thread.gmane.org/gmane.comp.lib.eigen/551) for more
information. So your our expressions will change from:
```
typedef Eigen::Map<Eigen::Vector4f, Eigen::ForceAligned> Vector4fMap;
``` to ```
typedef Eigen3::Map<Eigen3::Vector4f, Eigen3::Aligned> Vector4fMap;
```

### VectorXx ().cwise ()

`Eigen3` introduces a new storage concept called
[Array](http://eigen.tuxfamily.org/dox-devel/TutorialArrayClass.html).
All the `cwise ()` operations that were previously defined on
`VectorXx` (`MatrixBase`), are no longer valid. Here's an example:
```
Eigen::Vector4i xyz_offset (fields[x_idx].offset, fields[y_idx].offset, fields[z_idx].offset, 0);

xyz_offset.cwise () += input_->point_step;
``` needs to change to: ```
Eigen::Array4i xyz_offset (fields[x_idx].offset, fields[y_idx].offset, fields[z_idx].offset, 0);

xyz_offset += input_->point_step;
```

### VectorXx ().start () / .end ()

`VectorXx ().start ()` changed to `VectorXx ().head ()`, and
`VectorXx.end ()` changed to `VectorXx ().tail ()`. See
[\|this](http://eigen.tuxfamily.org/dox-devel/Eigen2ToEigen3.html) for
more information.

### MatriXx ().corner ()

Check
[this](http://eigen.tuxfamily.org/dox-devel/Eigen2ToEigen3.html#Corners).

### Transfom3f

The `Transform3f` typedef is deprecated starting with eigen3.0-beta2.
To make your old code work, change all instances of
```
Eigen3::Transfom3f
``` to ```
Eigen3::Affine3f
```

### PCL (Point Cloud Library) specific changes

To make sure that our Point Cloud data is always aligned, both on 32bit
architectures as well as on 64bit, we have changed the
`pcl::PointCloud<T>` data type internally as follows. Instead of
providing a: ```
std::vector <T> points;
``` we now use:
```
std::vector<T, Eigen3::aligned_allocator<T> > points;
```

This requires changes in your code wherever you use vectors of points
manually. Example: ```
#define EIGEN_ALIGN16 EIGEN_ALIGN_TO_BOUNDARY(16)
```0 should now be
```
#define EIGEN_ALIGN16 EIGEN_ALIGN_TO_BOUNDARY(16)
```1
