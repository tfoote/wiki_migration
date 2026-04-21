# Description

The notion of Capabilities in ROS is that there exists a higher level
interface for most "capabilities" that robots possess. An example of
this is the organic evolution of interfaces for things like the
Navigation Stack and the tf frame names. These sane defaults were used
on robots like the PR2 and have become defacto standards over time, and
some have even been solidified in REP's. But there has never been a
system in place to define these higher level interfaces (which consist
of other ROS concepts such as topics, services, and parameters) and to
manage their runtime in a way that makes interacting with an unknown or
abstracted robot easier.

One of the main goals of the capabilities is to make writing robot
agnostic "apps" easier. If a robot can declare that it implements the
standardized interface for the navigation capability, then an app can
rely on the ROS interface used to utilize that capability. Making it
easier for app developers to work independently of the robot developers
and making it easier to integrate onto new robots. This is analogous to
the use of Messages in topics and services, and that has proven to be
very effective at easing integration of disparate parts of the system.

# Documentation

## Tutorials

There are tutorials located here:
[capabilities/Tutorials](capabilities/Tutorials)

## API Documentation

There is fairly extensive API documentation for this package in the
CodeAPI link on the right side of this page.

The provided (Python) API can be used to discover local packages which
define one or more of the spec files defined by this package, load them,
and interact with them. It also provides an API to discover what
capabilities are provided by a `capability_server` running on a remote
machine, which is useful for tools like the
[rqt_capabilities](rqt_capabilities) plugin.

## capability_server

This package provides the `capability_server` ROS node which loads all
capability spec files from packages on the `ROS_PACKAGE_PATH` and
provides a ROS interface for querying and running those capabilities.

The `capability_server` is documented in the CodeAPI (linked to on the
right).

## Design Documents

There is no organized design documentation, but there are a few
documents used during the design process that might be useful for anyone
wanting to understand the existing work:

-   <https://docs.google.com/presentation/d/1sq28YcKFI8pE8WpvZUnk_jFHzbe72pgsNdwypuND7q8/edit?usp=sharing>
-   <https://docs.google.com/document/d/18kAOYxSmVE1ZEQ5P1nbrJalR8vSynuqu9QFaFzxxeqY/edit?usp=sharing>
-   <https://docs.google.com/document/d/1GVQ1wbrYymwp_8alyqZKRZjw0cTJ6PZAO-q1aYJBVVQ/edit?usp=sharing>

There was also an article in IEEE Spectrum (ROS Topics):

-   <http://ieeexplore.ieee.org/xpl/articleDetails.jsp?reload=true&arnumber=6990859>
