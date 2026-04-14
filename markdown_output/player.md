## Overview

Player is a networked robot device interface. We use it for its library
of drivers (e.g., in [amcl_player](amcl_player) and
[wavefront_player](wavefront_player)).

We include it in 3rdparty because:

-   We use almost the latest version from SVN, which is not yet
    available in OS package managers (older version are available). We
    need the latest version because it has numerous fixes to amcl and
    wavefront.

Two paths to minimizing the cost of building Player:

-   Extract the driver code that we\'re using and put it in the ROS
    packages where needed. That is, don\'t build Player at all.
-   Only build those parts of Player that we actually use.
    \'\'\'Done\'\'\': the build is now approx 25 seconds, including the
    initial download.
