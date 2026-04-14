\<\<Include(Industrial/Software_Status/Developmental)\>\>

Dependency graph (that\'s yielded by [rqt_dep](rqt_dep)) of
\`hironx_ros_bridge\`.
[![ launch top window \| width=90%](attachment:rosdep_hironx_ros_bridge.png )](http://wiki.ros.org/hironx_ros_bridge?action=AttachFile&do=view&target=rosdep_hironx_ros_bridge.png)

## Tutorials

Tutorial for \`Hironx\` is integrated into
[NEXTAGE OPEN](rtmros_nextage/Tutorials)\'s page.

## Available Robot Client Methods

\`hironx_ros_bridge\` is supported by the opensource community per
best-effort basis. If you find anything wrong, or would like to add more
documentation, please consider opening a ticket and providing patches
[at the issue tracker](http://code.google.com/p/rtm-ros-robotics/issues/list).

### Methods\' API Doc

User can get a the most control of the \`Hironx\` robot through the
Python class \`hironx_ros_bridge.hironx_client.HIRONX\`, where the large
part of methods are derived from
[hrpsys.HrpsysConfigurator](http://fkanehiro.github.io/hrpsys-base/df/d98/classpython_1_1hrpsys__config_1_1HrpsysConfigurator.html).
Some of their methods are overridden specifically for Hironx at
[the Python class \`HIRONX\`](http://docs.ros.org/hydro/api/hironx_ros_bridge/html/classhironx__ros__bridge_1_1hironx__client_1_1HIRONX.html)
(that is a derived class of \`hrpsys.HrpsysConfigurator\`).

### Unit Testing

For some of those methods derived from [hrpsys](hrpsys), unit test cases
are available in
[nextage_ros_bridge/test/test_hironx_derivedmethods_rostest.py](https://github.com/tork-a/rtmros_nextage/blob/groovy-devel/nextage_ros_bridge/test/test_hironx_derivedmethods_rostest.py).
Download it and run: ```
$ mv test_hironx_derivedmethods_rostest.py `rospack find nextage_ros_bridge`/test
$ chmod 755 test_hironx_derivedmethods_rostest.py
$ rosrun nextage_ros_bridge test_hironx_derivedmethods_rostest.py
```

As of today (Jan 31, 2014), you might want to modify the file to adjust
to your environment. Open the file with the editor, replace
[rtm.nshost](https://github.com/tork-a/rtmros_nextage/blob/b53fdb3adffe3a4d3f90a7ba9435e786b05f8db7/nextage_ros_bridge/test/test_hironx_derivedmethods_rostest.py#L78)
with the QNX hostname of your robot.

This will be improved so that you can specify the hostname in easier
way.
