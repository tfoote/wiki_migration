## Video

[Youtube](https://www.youtube.com/watch?v=J8NiCoO38Gc)

## Nodes

### rf_detector

rf_detector is a categorical object detector using Random Forests. It
runs a ROS node that expects stereo input data (with textured light)
input from the [texture_light_on_off](texture_light_on_off) node.

#### Subscribed topics

rf_detector subscribes to three ROS topics:

-   **/t_on_off/image**
-   **/t_on_off/caminfo**
-   **/t_on_off/dense_cloud**

After the \`rf_detector\` node receive all three topics, it will start
detecting objects in the image.

## launch files

\`rf_pcd_hogshape_detector_3Class.launch\` will start the rf_detector
with some default parameter settings. There are five groups of
parameters which need to be set.

1\. table-top object related parameters :

-   !PrineTableFlag \-- if true, do table-top object candidate
    reasoning.
-   max_depth \-- the maximum depth that the system will search for
    objects.
-   min_depth \-- the minimum depth that the system will search for
    objects.
-   plane_axis_x \-- the x component of the surface number orientation
    of the table in the image_frame.
-   plane_axis_y \-- the y component of the surface number orientation
    of the table in the image_frame.
-   plane_axis_z \-- the z component of the surface number orientation
    of the table in the image_frame.
-   eps_angle \-- the tolerance of the different between the estimated
    surface norm direction and the one set by plane_axis.

2\. patch sample related parameters

-   Radius \-- Radius of corresponding the 3d sphere to be sampled.
-   !SampleStep \-- The step size (in pixel) between two nearby sampled
    patches .
-   winStep \-- The incremental step of the patch size in pixel.
-   numCellPerWin \-- the number of cells in each patch for both
    vertical and horizontal direction.
-   numCellPerBlock \-- the number of cells in each Block for both
    vertical and horizontal direction.
-   padding \-- The padding in pixel for both top-left and bottom-right
    corner.
-   ObjHeight2winHeightRatio \-- Object height / Patch height

3\. model related parameters

-   !RFmodel_filename \-- the file describing the trained random forest.
-   !FgBgProb_filename \-- the Foreground/Background probability of each
    lead nodes in the random forest.
-   !ClassIdBinary_filename \-- the Class Id of each trained Foreground
    patch.
-   !NormVotesBinary_filename \--The normalized voting direction, the
    relative object height to patch height, the aspect ratio of the
    object.
-   !MaxClassId \-- the Maximum Class Id.
-   ClassId2ViewObjClassMapFile \-- the file which map each Class Id
    into object Class index and Viewpoint index.

4\. voting related parameters

-   hitThreshold \-- The minimum Foreground/Background ratio of a node
    to cast votes.
-   !MeanShiftMaxIter \-- The maximum mean-shift iteration to search for
    local mode.
-   !ObjHeightStep \-- The incremental step of the object height in
    pixel.
-   !ObjASStep \-- The incremental step of the object aspect ratio.

5\. detection post processing related parameters

-   !RectOverlapRatio \-- The threshold to decide if two bounding boxes
    are overlapping each other.
-   !ConfThre \-- It defines the minimum score for a object detector
    could return.
