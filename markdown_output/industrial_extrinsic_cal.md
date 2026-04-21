## Overview

The `industrial_extrinsic_cal` package provides a generic tool for
calibrating sensors to a known reference frame. It is relevant to anyone
using a system in which the relative position(extrinsics) of multiple
pieces of equipment must be determined. Common equipment examples
include positioning systems(i.e. robots, cartesian gantries),
measurement/sensor systems (i.e. camera(s), laser scanner/trackers,
radio) and fixturing(accurately produced parts for referencing objects
of interest).

[Youtube](https://www.youtube.com/watch?v=MRvExKMOH1g&rel=0)

The calibration uses Google's Ceres solver to perform bundle adjustment
or minimize the reprojection error of the camera to the known points.
The Ceres software problem and solver are generic and the cost functions
contain the definition of the error to minimize.

## Installation

```wiki
'''UPDATE 20170922''' For ROS [[indigo]], the following `ceres` installation is now not necessary now that [[https://github.com/ros-industrial/industrial_calibration/pull/109|this pull request]] is merged. Please report if you see any issue regarding this.
```

The industrial extrinsic calibration package depends on the google
[Ceres Solver](http://ceres-solver.org/). The steps below walk through a
minimal installation of Ceres on Ubuntu 14.04 as required for this
package, more detailed instructions or different Ubuntu versions can be
found [here](http://ceres-solver.org/installation.html). **NOTE:** These
instructions download and install dependencies from your home directory.
Once installed, these tarballs and directories can be deleted.

1\. Install gflags ```
cd
wget https://github.com/gflags/gflags/archive/v2.1.2.zip
unzip v2.1.2.zip && rm v2.1.2.zip
cd gflags-2.1.2 && mkdir build && cd build
cmake .. -DBUILD_SHARED_LIBS=ON
make
sudo make install
``` 1. Install glog
```
cd
wget https://github.com/google/glog/archive/v0.3.4.zip
unzip v0.3.4.zip && rm v0.3.4.zip
cd glog-0.3.4/
./configure --with-gflags=/usr/local/
make
sudo make install
``` 1. Install Ceres ```
cd
wget https://github.com/ceres-solver/ceres-solver/archive/1.11.0.zip
unzip 1.11.0.zip && rm 1.11.0.zip
cd ceres-solver-1.11.0
mkdir build && cd build
cmake ..
make
sudo make install
``` 1.
Install `industrial_extrinisc_cal` from
[source](https://github.com/ros-industrial/industrial_calibration.git).

## Tutorials

. Examples can be found in the
[tutorials](industrial_extrinsic_cal/Tutorials).

## Design

Detailed design info can be found in this
[presentation](http://roscon.ros.org/2014/wp-content/uploads/2014/07/LewisPresentation.pdf)
presented at ROSCon 2014. <<Vimeo(106994711)>>
