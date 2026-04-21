

```wiki
/!\ Work in progress.
```



## Downloading

The tabletop_for_cabinet package is a part of the
[mit-ros-pkg](mit-ros-pkg) repository. To download the most recent
version of the stack without downloading the whole repository use



```
$ svn co `roslocate svn tabletop_for_cabinet`
```



## Overview

The tabletop_for_cabinet package uses tabletop detection to find the
cabinet door. It fits the plane of the table to the cabinet door.

![](attachment:Screenshot-RViz.png)

It uses cluster detection to find all of the clusters in front of the
tabletop and finds those clusters' bounding boxes.

![](attachment:Screenshot-RViz-2.png)

It then selects the cluster most likely to be the handle based on the
size of the bounding box and its relative location of the door. It
chooses the bounding box which is most centered.

![](attachment:Screenshot-RViz-4.png)

## Usage

Tutorials can be found at
[tabletop_for_cabinet/Tutorials/tabletop_for_cabinet](tabletop_for_cabinet/Tutorials/tabletop_for_cabinet)

## ToDo

The current selection of the handle bounding box needs to be refined. If
possible, it should return multiple poses of all the possible handles
(in case the first choice is not correct). The orientation of the handle
should be a parameter
