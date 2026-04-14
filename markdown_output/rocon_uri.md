## Overview

Various entities in the rocon framework require a specification for
describing the kind of resource it is, or the kind of resource it is
compatible with. In particular, such a specification must describe
entities like robots, define compatibility strings for apps (i.e. what
robots/platforms can run this app) and shape robot requests (give me a
robot with this specification and able to run this robot app). It is the
glue which will ultimately enable us to run a diverse mix of robots and
applications together to provide useful robotic solutions.

A typical rocon uri string is of the form:

```
rocon://concert_name/hardware_platform/name/application_framework/operating_system#rocon_app
```

You will see these flung around a rocon concert frequently at the ros
api level. Examples:

-   \`rocon:/turtlebot2/cybernetic_pirate#rocon_apps/im_here_to_make_you_lazy\`
-   \`rocon:/pr2/bob#rocon_apps/look_menacing\`

## Command Line Tools

There is a command line tool for introspecting and testing rocon uri
strings:

```
Utility for introspecting on rocon uri strings.

Commands:
        rocon_uri parse URI     parse and attempt to validate a rocon URI.
        rocon_uri fields        print a full list of permitted fields in a rocon uri string.
        rocon_uri rules         print a full list of the ebnf rules for a rocon uri string.
```

## Python Module

A detailed specification, the ebnf rules table and examples for parsing
and compatibility checking with the python module can be found in the
sphinx documentation.

-   [Indigo](http://docs.ros.org/indigo/api/rocon_uri/html)
