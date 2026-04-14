<http://rtc-us-ros-pkg.svn.sourceforge.net/viewvc/rtc-us-ros-pkg/trunk/rtcus_mobile_robots/rtcus_compositions/>

## Description

This package contains a c++ generic template library to make geometrical
transformations: compositions and inverse compositions between different
kinds of geometric datatypes.

## Precedents

The [tf](tf) package provides a good set of type transformations of
different kinds of datastructures but it is strictly focused on poses:
Pose, StampedPose, etc. The MRPT software provides as well many features
for compositions and inverse compositions of different datatypes. This
package try to unify all these transformations in a generic template
library. Because of this, this package is absolutely open to accept new
kinds of transformation software.

Example of Cpp code of composition MRPT: ```
CPose2D original, new_local_frame, result;
original.x(3);
original.phi(0.1);
new_local_frame.y(30);

result= original - new_local_frame;
```

## Composing not only poses

But not only poses can be composed. All data with geometrical and
spetial information can be composed: a point cloud, a laser scan, etc.
The packages [laser_geometry](laser_geometry) or [pcl_ros](pcl_ros)
provides software to do these transformations but they are not given
toghether.

Moreover, complex poses like not deterministic poses can be composed.
Poses with uncertainty (see [pose_cov_ops](pose_cov_ops)) or with
dynamic information like speed or acceleration can be theoretically
composed.

See the next example: consider a frame moving and while dynamic
information is available (PoseWithTwist)a possible composition would be
```
(pcl::PointCloud<PointXYPhi>) - (PoseWithTwist) ->  (pcl::PointCloud<PointXYdXdYdPhi>)
```

For now there is no a convey about how to tackle this problem. Because
of this the rtcus_compositios is needed. This package provide a cpp
library with this functionality:

```
class StateComposer
{
public:

  template<typename targetType, typename localStateFrame>
    static void compose(const targetType& src, const localStateFrame& delta_transform, targetType& dst);

  template<typename t_target, typename t_local_frame>
    static void inverse_compose(const t_target& initial_state, const t_local_frame& local_frame_state, t_target& dst,
                                const std::string& new_frame_name = ANONYMOUS_LOCAL_FRAME_NAME);

};
```

If the composition is available it would be detected at linking time.

This package is designed to be extensible and this use is recommendable
to design generic type algorithms with geometrical transformations.

## Note

This package is still in development and it should be analyzed if the
the goal of the package is similar to [tf2](tf2). In such case the
developed code will be converted to several tf2 plugins.
