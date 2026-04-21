

```wiki
(!) '''[[rqt]] is a replacement for the [[rx]] stack since [[fuerte]].'''
```



Please see [rqt_common_plugins](rqt_common_plugins) for more information
on rxtool replacements.

## GUI Tools

-   [rxconsole](rxconsole): Display logging messages published to
    [rosout](rosout). For more information, please see the
    [rxconsole User's Guide](rxconsole).
-   [rxplot](rxplot): Plot data from ROS messages published to topics.
    For more information, please see the [rxplot User's Guide](rxplot)
    for more information.

## rxtools libraries

For documentation on the libraries that `rxtools` provides, please see
the [Code API](http://www.ros.org/doc/api/rxtools/html/).

## Roadmap/Stability

`rxconsole` and `rxplot` are **stable** tools. For future
development, the hope is to add other forms of plotting to `rxplot`,
such as plotting distributions. `rxplot` may also get a plugin API
that would enable it to plot common message types with default settings.

In future versions of ROS, the `rxplot` command-line format may be
changed to reflect updates in ROS name syntax.
