## Overview

This package is a collection of extensions that go above and beyond what
the family of core ros modules (rospy, rosmaster, rostopic, rosnode,
rosservice\...) do for enabling the ros middleware with python.

## Reference

Full details and usage examples are in the sphinx documentation
([indigo](http://docs.ros.org/hydro/api/rocon_python_comms/html/)), the
following is just a brief reference of what is available.

-   `find_xxx` : helpers for finding nodes, topics and services.
-   `SubscriberProxy` : similar to a service proxy (client), but works
    with a latched topic.
-   `ServicePairs` : use pub-sub pairs for blocking/non-blocking
    request-response behaviour (c.f. [actionlib](actionlib)).

## Tutorials
