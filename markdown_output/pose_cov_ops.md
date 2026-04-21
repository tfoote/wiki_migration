## Provided functionality

See the C++ API documentation for the namespace
[ pose_cov_ops](http://docs.ros.org/kinetic/api/pose_cov_ops/html/namespacepose__cov__ops.html).

This module provides implementations for the **four main operations**
between poses (**p**,**p1**,**p2**) and points (**a**), which are the
following (using the \"o plus\" and \"o minus\" notation):

1\. **p1** &oplus; **p2** : Composition of two poses **p1** and **p2**:
the resulting pose is **p2** \"as if\" **p1** was the new origin of
coordinates for **p2**.

2\. **p2** &ominus; **p1** : Inverse composition of two poses **p1** and
**p2**: the resulting pose is **p2** \"as seen from\" **p1**.

3\. **p** &oplus; **a** : Composition of a pose **p** and a point **a**:
the resulting point is **a** \"as if\" **p** was the new origin of
coordinates of **a**.

4\. **a** &ominus; **p** : Inverse composition of a pose **p** and a
point **a**: the resulting point is **a** \"as seen from\" **p**.

Is better to illustrate these operations graphically:

  -- ------------------------------------------------------------ --
     \<:99%\> ![](attachment:mrpt_geometry_poses_explained.png)   
  -- ------------------------------------------------------------ --

## Examples of usage

```cplusplus
#include <mrpt_cov_ops/mrpt_cov_ops.h>

...
geometry_msgs::PoseWithCovariance p1, p2, p;

// p = p1 (+) p2
// Pose composition, including uncertainty in both p1 and p2:
pose_cov_ops::compose(p1,p2,  p);

...
geometry_msgs::Pose p1;
geometry_msgs::PoseWithCovariance p2, p;

// p = p1 (+) p2
// Pose composition, including uncertainty only in p2 (and in the output, obviously!):
pose_cov_ops::compose(p1,p2,  p);
```

## References

Further references on the geometry and the maths behind these functions:

-   <https://www.mrpt.org/tutorials/programming/maths-and-geometry/2d_3d_geometry/>

```{=html}
<!-- -->
```
-   *A tutorial on SE(3) transformation parameterizations and
    on-manifold optimization*, J.L. Blanco, Technical report, 2010
    [ PDF](https://ingmec.ual.es/~jlblanco/papers/jlblanco2010geometry3D_techrep.pdf ).
