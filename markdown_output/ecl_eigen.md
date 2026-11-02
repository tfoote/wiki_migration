This provides an internal implementation of Eigen. This was necessary
while eigen was fairly volatile and transitioning from Eigen 2 to Eigen
3. Eventually this will disappear and be replaced as a system
dependency.

Currently either the internal or system implementation can be used - see
[ecl_linear_algebra](https://index.ros.org/p/ecl_linear_algebra) for
more information.
