## Install

Granted you have installed the ros-electric-desktop-full and the
ros-electric-ias-common debian packages: 

```
sudo apt-get install ros-electric-desktop-full ros-electric-ias-common
```

 you
have to install the following additional packages from the sources (make
sure you check them out into the directory contained in
ROS_PACKAGE_PATH): 

```
svn co https://code.ros.org/svn/ros-pkg/stacks/vslam/trunk vslam
svn co https://cmu-ros-pkg.svn.sourceforge.net/svnroot/cmu-ros-pkg/trunk/3rdparty/ann2 ann2
svn co https://jsk-ros-pkg.svn.sourceforge.net/svnroot/jsk-ros-pkg/trunk/3rdparty/libsiftfast libsiftfast
git clone https://github.com/dejanpan/objects_of_daily_use_finder
```

 Finally run:


```
rosmake objects_of_daily_use_finder
```



## Overview

In this package we report on the design and implementation of Objects of
Daily Use Finder **(ODUfinder)** perception system that can deal with
some aspects of this challenge. The system can detect and recognize
textured objects in typical kitchen scenes. The models for perceiving
the objects to be detected and recognized can be acquired autonomously
using the robot's camera as well as by loading large object catalogs
such as the one by [Germandeli](http://www.germandeli.com) into the
system. In the system configuration described in this package the robot
is equipped with an object model library containing about 3500 objects
from Germandeli and more than 40 objects from the
[Semantic3D](http://ias.cs.tum.edu/download/semantic-3d) database.
**ODUfinder** achieves an object detection rate of 10 FPS and recognizes
objects reliably with an accuracy over 90%. Object detection and
recognition is fast enough so that it does not cause delays in the
execution of the robot tasks.

![](attachment:teaser.png)

## Techniques

The ODUfinder system employs SIFT features for textured objects
recognition using vocabulary trees, which we extend in two important
ways. First, the comparison of object descriptions is done
probabilistically instead of relying on the more error-prone original
implementation with the accumulation of query sums. Second, ODUfinder
detects candidates for textured object parts by over-segmenting image
regions and then combines the evidence of the detected candidate parts
to infer the presence of the object.

## Usage

Please see tutorials on the right in order to learn about how to use
ODUFinder.

## Barcode Recognition

ODUFinder recently got extended with the plugin for the recognition of
various types of barcodes. The barcode decoding has been provided
through the Zbar library which we wrapped inside the
[ zbar](http://code.in.tum.de/indefero/index.php//p/ias-perception/source/tree/master/zbar )
package and for which we provide a rosnode example inside the
[ zbar_barcode_reader_node](http://code.in.tum.de/indefero/index.php//p/ias-perception/source/tree/master/zbar_barcode_reader_node )
package. We use this functionality in order to access the information
about the objects of daily use in the [ Barcoo](http://www.barcoo.com )
product information store. The latter you can test using the following
QT-based client
[ zbar_qt_ros](http://code.in.tum.de/indefero/index.php//p/ias-perception/source/tree/master/zbar_qt_ros )
(needs authorization from Barcoo GmbH).
