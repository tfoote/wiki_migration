![](attachment:acin-logo.png)![](attachment:TU-Logo.png)
![](attachment:pal_logo.png)![](attachment:elte_logo.jpg)

## Overview

BLORT - The Blocks World Robotic Vision Toolbox

The vision and robotics communities have developed a large number of
increasingly successful methods for tracking, recognizing and online
learning of objects, all of which have their particular strengths and
weaknesses. A researcher aiming to provide a robot with the ability to
handle objects will typically have to pick amongst these and engineer a
system that works for her particular setting. The toolbox is aimed at
robotics research and as such we have in mind objects typically of
interest for robotic manipulation scenarios, e.g. mugs, boxes and
packaging of various sorts. We are not aiming to cover articulated
objects (such as walking humans), highly irregular objects (such as
potted plants) or deformable objects (such as cables). The system does
not require specialized hardware and simply uses a single camera
allowing usage on about any robot. The toolbox integrates state-of-the
art methods for detection and learning of novel objects, and recognition
and tracking of learned models.

## Techniques

The system works with a CAD model of the object provided. The current
implementation of the BLORT detector module uses SIFT feature
descriptors to provide an approximate estimation of the object\'s pose
for the tracker module which will track the object using edge-based
methods.

More information: \[\'\'\'Mörwald, T.; Prankl, J.; Richtsfeld, A.;
Zillich, M.; Vincze, M. BLORT - The Blocks World Robotic Vision Toolbox
Best Practice in 3D Perception and Modeling for Mobile Manipulation (in
conjunction with ICRA 2010), 2010.\'\'\'\] or you can also visit the
[BLORT Homepage](http://www.acin.tuwien.ac.at/?id=290).
