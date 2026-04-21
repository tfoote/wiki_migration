## Overview

This package broadcasts
[BVH files (a motion capture data format)](https://research.cs.wisc.edu/graphics/Courses/cs-838-1999/Jeff/BVH.html)
as [tf transfromations](http://wiki.ros.org/rviz/DisplayTypes/TF).

**GitHub repository**: <https://github.com/mingfeisun/bvh_broadcaster>

## Data input

Input contains two string parameters:

-   A path to BVH file, e.g.,
    [example.bvh](https://research.cs.wisc.edu/graphics/Courses/cs-838-1999/Jeff/Example1.bvh)
-   A name of frame for motion capture to be loaded on, e.g., "world"
    frame, or "odom" frame.

You can find relevant BVH-formatted CMU MoCap from
[this post](https://github.com/mingfeisun/bvh_broadcaster/blob/master/cmu_mocap_bvh.md).
Get BVH-formatted motion capture data from
[here](http://www.cgspeed.com/).

## Usage

```shell
python bvh_broadcaster.py [-h] [-n NAME] [-l] bvh_file base_frame

positional arguments:
  bvh_file              A path to bvh file that you want to broadcast
  base_frame            An existing frame in rviz on which the skeleton will
                        be loaded

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Node name, default: BVHBroadcaster
  -l, --loop            Loop broadcasting
```

For example: ```shell
# add execution access
chmod +x scripts/bvh_broadcaster.py
# loop broadcasting bvh to world frame
python scripts/bvh_broadcaster.py example/13_14.bvh world -l
``` Now, you can view the result in
rviz:

![](https://raw.githubusercontent.com/mingfeisun/bvh_broadcaster/master/example/example_bvh.gif)

The original actor and BVH file are as follows:

![](https://github.com/mingfeisun/bvh_broadcaster/blob/master/example/example_actor.gif?raw=true)![](https://github.com/mingfeisun/bvh_broadcaster/blob/master/example/example_animator.gif?raw=true)

## BVH resources for Motion Capture

CMU provides a lot of useful motion capture data, see
[CMU MoCap](http://mocap.cs.cmu.edu/). Nevertheless, these data are not
presented in BVH format. You can find relevant BVH-formatted CMU MoCap
from
[this post](https://github.com/mingfeisun/bvh_broadcaster/blob/master/cmu_mocap_bvh.md).
