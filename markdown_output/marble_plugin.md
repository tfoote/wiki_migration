![width=100\|alt This is an image of the plugin](attachment:2013-01-14-screenshot.png)

## Features

This plugin takes advantage of the Marble Widget, provided with the
libmarble-dev package of ubuntu. The main features are:

-   Show two geo positions
    ([sensor_msgs::NavSatFix\|target=\"\_blank\"](http://ros.org/doc/api/sensor_msgs/html/msg/NavSatFix.html)
    message) on the map. This is helpful if you have a \"sensor signal\"
    originating from the sensor and a \"map matching position\"
    originating from your map matching algorithm.
-   Show content of several
    [KML Files\|target=\"\_blank\"](http://en.wikipedia.org/wiki/Keyhole_Markup_Language)
-   Load specific map themes as Open Street Map theme, Historic theme,
    Sattelite View theme, World by Night theme, \...

## Installation

You might need to satisfy dependency by: ```
$ rosdep install marble_plugin
```

## Further Reading

-   <http://techbase.kde.org/Projects/Marble/MarbleCPlusPlus>
-   <http://edu.kde.org/marble/>

## 
