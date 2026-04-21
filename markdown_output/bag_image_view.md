## Overview

The package allows to interactively browse the image content of a bag
file. It uses a bagserver to get information about the log file and the
content of the data. The package is intended as a useful tool and as an
example of how to access the bagserver.

-   Known limitations
-   Single image, single topic.
-   Positioning only within a second.
-   No type checking on the topic.

## Tutorials

Here's how to use it:

Make all: 

```
rosmake bagserver bag_image_view
```



Download test data 

```
roscd bagserver
make test
```



Run the bag server on the test_data/test_images2.index


```
roslaunch $(rospack find bagserver)/test/test_images2.launch
```



Run the bag_image_view tool: 

```
rosrun bag_image_view view.py
```



Drag the slider around.
