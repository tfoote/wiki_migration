![](attachment:rosruby_logo.png)

## Overview

rosruby is ruby ROS client. This is experimental stack and supports
hydro, groovy and fuerte (v0.2.1).

## See also

-   [rosruby_common](rosruby_common) metapackage contains
    [rosruby_actionlib](rosruby_actionlib), and
    [rosruby_tutorials](rosruby_tutorials).
-   [rosruby_tf](https://github.com/OTL/rosruby_tf) is highly under
    development.
-   [rosruby GitHub repository](https://github.com/OTL/rosruby) for more
    information.

## Installation

You can install rosruby using apt.

```
sudo apt-get install ros-hydro-rosruby ros-hydro-rosruby-common ros-hydro-rosruby-messages
```

rosruby_messages contains pre-compiled ruby message files. Then you have
to source setup file for update your environmental variables for
rosruby.

```
source ~/.bashrc
```

or

```
source /opt/ros/hydro/setup.bash
```

## Tutorials

Please refer to the [rosruby_tutorials](rosruby_tutorials) package and
read the [rosruby/Tutorials](rosruby/Tutorials) page.

## API Reference

For a more detailed reference, please consult the
[code API documentation](http://otl.github.com/rosruby/doc/).

## Generate message files

After you installed rosruby, ruby message file will be compiled if you
generate msg/srv from source. If you want to know more, read
[this](https://github.com/OTL/rosruby#message-generation).
