# GRAVEYARD

This package is currently in the graveyard until it is ported to work
with the new visual odometry libraries. It and its dependencies can be
checked out from:

<https://code.ros.org/svn/wg-ros-pkg/graveyard/>

## Data files

The [place_recognition](place_recognition) and visual_odometry packages
are research code; apologies if they are difficult to work with in their
current form.

To use this package you will need a vocabulary tree trained on a large
dataset of images. We have one here:
<http://vault.willowgarage.com/wgdata1/vol1/jbowman/holidays.tree>

This tree was trained on the C-descriptors devised by Michael Calonder
([calonder_descriptor](calonder_descriptor)). This descriptor has its
own training stage which produces a random forest classifier. The
classifier used to generate the above tree is available in two ways:

-   Do \`roscd calonder_descriptor && make test\`. This will
    automatically download the classifier \`current.rtc\` to the
    \`calonder_descriptor\` package directory.
-   Download it directly from
    <http://pr.willowgarage.com/data/calonder_descriptor/current.rtc>

## Tutorials

Links to relevant tutorials
