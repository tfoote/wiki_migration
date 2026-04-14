## Introduction

This package implements the perceptual pipeline for the
[worldmodel](http://www.ros.org/wiki/worldmodel) stack; you should start
at that page to get a general overview of the system.

## Perceptual Model

The segmentation pipeline tries to makes two assumptions about your
robot, and one assumption about your environment. It assumes that your
robot mounts a Microsoft Kinect (in general, any RGB-D sensor) fairly
far off the floor, and has a localized mobile base. It also assumes that
your environments contains \"interesting\" objects atop large flat
surfaces like tables, counters, or shelves. This planarity assumption is
helpful in indoor environments, as many objects of human interest are
kept on such surfaces.

Data collection, therefore, consists of storing Kinect RGB-D point
clouds (and localization tf frames); processing the data requires
segmenting out horizontal planes and the objects atop them.

## Collecting Data

To ease the computational load on your robot, the common case for this
code is to do a pure data-collection run and then to generate the object
database offline. Here, we discuss how to gather data; see below for
generating a database. \'\'If you\'d like, you can run the database
generation online; however, this is computation- and
bandwidth-intensive.\'\' To reduce data usage, the common case saves the
raw Kinect images at 5fps; see \`throttles.launch\` to change this rate.
During database generation, these raw images are reprojected (see
\`openni_record_player.launch\`) into RGB-D point clouds for processing.

To collect data, you want the \`gather_data.launch\` launchfile. (If
you\'re not using a PR2, you should set the \`headpointer\` argument to
false.) The comments in that launchfile are detailed, and should get you
started. Once this is up and running, use the \`record_data.sh\` script
to record a bagfile (\`record_data.sh\` automatically collects all
necessary ROS topics). Drive your robot around as you see fit (we
recommend a an automated tour using the navigation tools;
[worldmodel_ops](http://www.ros.org/wiki/worldmodel_ops) shows how this
can be done using continuous operations, but could be straightforwardly
adapted to waypoint navigation or teleoperation.

## Generating a Database

Once you have a bagfile containing Kinect data for your localized robot,
you should run \`playbag-local.launch\` to start up the data-processing
pipeline, and then run the \`playbag.sh\` script to start playback.
(Just using \`rosbag play\` will fail to set some important parameters;
hence \`playbag.sh\`.)

## Visualizing a Running Process

While collecting data, the plane-extraction process will be running
(this is used to perform active head pointing, if you are on a PR2);
these planes, and various other things, can be visualized in rviz (there
are several point cloud topics; the convex hulls of the planes are also
published to the marker topics).

During database generation, the point clouds of the segmented objects
will also be visible.

## Viewing and Querying the Database

The code for doing this has been broken out into the
[semantic_model_web_interface](http://www.ros.org/wiki/semantic_model_web_interface)
package; see that page.

## Implementation Details

The heavy lifting of the segmentation pipeline is done in the Segmenter
class; see \`segmenter.hh\` and \`segmenter.cc\` for details of the
interface and implementation. The segmenter has a wide variety of
\`dynamic_reconfigure\` parameters, the most-important of which are
detailed here.

-   \`min_z\` and \`max_z\` truncate the point cloud (which is
    transformed into the /map frame, where +z is \"up\"); this limits
    processing to tabletops; the tighter this limitation, the faster the
    code will run, but you run the risk of chopping the tops off of tall
    objects. The default values are tuned for a PR2 with a head-mounted
    Kinect.

```{=html}
<!-- -->
```
-   \`voxel_size\` describes the size of the voxels for pointcloud
    downsampling (RANSAC for plane extraction is run in a downsampled
    cloud, for speed\'s sake).

```{=html}
<!-- -->
```
-   \`plane_distance\` defines how far \'\'above\'\' the plane points
    must be to be object candidates; this keeps points that are actually
    part of the table from being accidentally treated as candidate
    object points.

```{=html}
<!-- -->
```
-   \`filter_lag_cutoff\` lets you drop input frames that are too old;
    even at 5Hz, the perceptual pipeline can sometimes fall behind.
    While this is not a problem during playback, it is an issue when
    performing active head pointing; this parameter allows you to give
    up on frames that are taking too long. (In our experiments, with the
    default value, only a single-digit percentage of the total frames
    were dropped during a standard data-collection run.)
