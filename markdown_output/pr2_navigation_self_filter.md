## Overview

The pr2_navigation_self_filter package provides a node that filters hits
on the robot\'s body out of
\<\<MsgLink(geometry_msgs/PointCloud.msg)\>\> messages and republishes
them.

## API Stability

Due to the fact that \<\<MsgLink(geometry_msgs/PointCloud.msg)\>\>
messages will soon be deprecated, the pr2_navigation_self_filter has no
stable API. A new version of the node will be written and supported long
term with the new !PointCloud structure, but until the
[navigation](navigation) stack moves to support the new !PointCloud\'s
this package will remain in [pr2_navigation](pr2_navigation). Overall,
you can use this package, but its at your own risk.

## New In Indigo:

The pr2_navigation_self_filter package has been moved to the
robot_self_filter package as it is no longer PR2 specific. It is hosted
at <https://github.com/pr2/robot_self_filter>. This change will not
fully go into affect until ROS Jade which the pr2_navigation_self_filter
package will then be removed from the pr2_navigation metapackage. This
means in Indigo, we will support both packages. In Hydro, there will be
no relaese of robot_self_filter. Please see
[this link](https://github.com/PR2/pr2_navigation/pull/20) for
discussion on the matter.
