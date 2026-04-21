## Overview

Roslisp is a client library for writing ROS nodes in idiomatic Common
Lisp. The library is written to support ease of use, quick scripting of
nodes, and interactive debugging of a running ROS system.

See the [roslisp overview](/Overview) for a guide to roslisp's
features.

## Status

Roslisp is part of the stable ROS core distribution, and follows the
[ROS versioning policy](StackVersionPolicy).

Roslisp has been tested fairly extensively on Ubuntu (Jaunty or later),
and to some degree on OS X 10.5.

See the [roslip roadmap](/Roadmap) for future changes.

## Dependencies

### SBCL

Roslisp is based on the [SBCL](http://www.sbcl.org/) version of Common
Lisp. It is defined as a system dependency in the roslisp ROS package.

## See also

-   [ros_emacs_utils](ros_emacs_utils) metapackage contains
    [slime_ros](slime_ros), which integrates roslisp with the popular
    [SLIME IDE](http://common-lisp.net/project/slime/) for lisp. This is
    the recommended way of using roslisp.
-   [roslisp_common](roslisp_common) contains standard libraries for
    using roslisp within ros.
