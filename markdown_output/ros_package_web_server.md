## Overview

A webserver that serves ROS package resources. This is useful with
[Robot Web Tools](http://robotwebtools.org/) for serving resources that
would normally be found with rospack. For example when displaying a URDF
using [ros3djs](http://wiki.ros.org/ros3djs) the robot model files must
be served from somewhere. This package allows for these models to be
served directly from the install location instead of having to copy
resources to a separate web root. Resources are served with CORS enabled
to allow for easy interop with resources served elsewhere. Navigating to
the root path will display a list of all installed packages. Resources
can then be loaded using by prefixing the path of the resource relative
to the share location of the package. For installed packages this is in
the share folder in the install location and for non-installed packages
this is the package root.

## Nodes



```clearsilver
node.0 {
  name = server.py
  desc = Host ROS resources on a webserver
  sub {
  }
  pub {
  }
  param {
    0.name = ~port
    0.type = int
    0.default = 8888
    0.desc = The port to host resources at
  }
}
```


