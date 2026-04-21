## Code

The source code for segmenting floor plans and the dataset of 20 floor
maps with and without furniture can be found here:
<https://github.com/ipa320/ipa_coverage_planning> .

The floor maps lie in .png format under common/files/test_maps
(<https://github.com/ipa320/ipa_coverage_planning/tree/noetic_dev/ipa_room_segmentation/common/files/test_maps>).
The relevant are the ones which are existing in several versions, shown
by following name extensions:

-   \_furnitures : The original map with furnitures drawn in
-   \_trashbins : The original map with trashbins as blue pixels drawn
    in

And the combinations of these extensions, resulting in 4 versions for
each map.

Additionally there are ground-truth maps, that show how a human might
intersect these maps, shown by the name extension \_gt. If you want to
colour these ground-truth maps, to show the different segments, you can
use a flood-fill algorithm for the white pixels to collect each pixel
that belong to one segment, because the drawn lines seperates the white
spaces from each other. Then you can colour each of this found pixels
with a color that is unique for this segment. This is done in the
computePrecisionRecall() function of the EvaluationSegmentation class
(common/src/evaluation_segmentation.cpp) if you want it.

## General Procedure

1\. Change the algorithm parameters in
ros/launch/room_segmentation_action_server_params.yaml in ros/launch to
the wanted algorithms and settings.

-   room_segmentation_algorithm: Choose which segmentation algorithm
    should be used.
-   display_segmented_map: Specify if you want a window to pop up after
    the given map has been segmented, showing the results. To continue
    the program press any button in the window.
-   train_semantic, train_vrf: Booleans that show, if the feature-based
    or voronoi random field segmentation should be trained. For details
    of this training method see the further document.
-   Every algorithm has its own specific range of allowed room areas.
    Segments that are out of this range will not be drawn and are going
    to be filled by the surrounding valid rooms. **Remark:** The upper
    border in the feature-based segmentation method has a little
    addition. If found segments are too big they become separated by
    randomly putting centers in the segment and splitting it by using a
    wavefront algorithm. It\'s better to turn this off by setting the
    allowed maximal area very high.
-   Some algorithms have specific parameters that change some
    functionalities of it, which is described in detail in the .yaml
    file.

2\. Start the action server using the launch file
/ros/launch/room_segmentation_action_server.launch, which executes the
/ros/src/room_segmentation_server.cpp file. If the server crashes for
some reason (e.g. no valid map given by the client) it respawns with a
little delay.

3\. Start an action client, which sends a goal to the segmentation
action server, corresponding to the MapSegmentation.action message,
which lies in ipa_building_msgs/action. The goal consists of the
following parts

-   input_map: The map that should be segmented, as sensor_msgs/Image.
    **Has to be a 8-Bit single channel image, with 0 as occupied space
    and 255 as free space**.
-   map_resolution: The resolution the map has been sampled with
    \[meter/cell\].
-   map_origin: The origin of the map in \[meter\] to bring the provided
    map coordinates in absolute coordinates, if wanted.
-   return_format_in_pixel: Boolean to indicate if the results should be
    returned in pixel-coordinates.
-   return_format_in_meter: Boolean to indicate if the results should be
    returned in absolute coordinates.
-   robot_radius: The radius of your robot. If this is set to a value
    greater than 0 the room centers are chosen at locally reachable
    areas. 4. The action server returns a result, that has the following
    parts
-   segmented_map: The map with the N found segments drawn in. The value
    of a pixel indicates its ID, which can be used to find pixels
    belonging to one room. The IDs start at 1 and go up to N, the
    **return format is 32-Bit single channel**, because it allows to
    have more rooms than the 8-Bit format.
-   RoomInformation: For each found room the min/max x/y coordinate of
    points belonging to this room and the center is provided. See
    ipa_building_msgs/msg/RoomInformation.msg for details. This can be
    in pixel coordinates or absolute coordinates, depending on the
    booleans defined above.
-   doorway_points: The fifth algorithm (voronoi random field
    segmentation) is capable of predicting doorways. If this algorithm
    is chosen, central points on a computed voronoi graph are returned
    that were labeled as doorways.

A client also can change the parameters of the server by using
dynamic_reconfigure. This can be done using the
dynamic_reconfigure_client.h file that provides a client for this
purpose. With client.setConfig(\"param_name\", value) one specific
parameter can be changed from the client, see
ros/src/room_segmentation_client.cpp for an example. Of course
rqt_reconfigure can also be used to change specific parameters.

The algorithms are implemented in common/src, using the headers in
common/include/ipa_room_segmentation. Each algorithm has its own class,
so if you want to use it alone you have to include the header for the
algorithm you want to use and make a new object. Then you have to
execute the segmentMap() function, which segments the map.

For large maps the algorithms can take a few minutes to complete the
segmentation, especially the feature-based and voronoi random field
segmentation. If you want fast results, the morphological and distance
segmentation are the fastest, but they might return not the best results
if you have wide open spaces. To see results on different maps, see the
chapter **6. Segmentation results**.

## Available algorithms

1\. Morphological segmentation: Given the map as binary image, a binary
erosion is iteratively applied. After each step, the algorithm searches
for separate regions that have an area in the defined range. If it finds
one, this region is saved and drawn black such that it doesn\'t need to
be looked at any further. After all white regions are black, the
algorithm stops and draws the segments in an image, then applies a
wavefront algorithm to fill remaining white spaces.

2\. Distance segmentation: Out of the given image a distance-map is
computed that stores for each white pixel its distance to the nearest
black pixel. On this distance-map a threshold operator is applied
iteratively that makes every pixel above a certain threshold black and
everything beneath it white. After each step the algorithm searches for
segments in the given area range and stores them, then increases the
threshold. After all possible thresholds have been looked at, the
algorithm chooses the segmentation with the most valid segments as
segmentation. After that it also draws the segments in an image and
applies a wavefront algorithm.

3\. Voronoi segmentation: For the given map a pruned voronoi graph is
computed. The points belonging to this graph are then separated into
different neighborhoods and searching in this neighborhood for the point
with the smallest distance to the black pixels, called a critical point.
This critical point is connected with the two closest black pixels,
creating a separation of two segments.

4\. Feature-based/semantic segmentation: For each white pixel a 360
degree laserscan is simulated, resulting in different distances to
obstacles around this point. These laserscans are then used to compute
different features, which are put into two AdaBoost algorithms. These
compute the probability that the current point is a room or hallway.
Depending on the probabilities a label is given to that point. The same
procedure is then repeated for each white pixel in the given map,
resulting in different separated regions for rooms/hallways that are
treated as segments.

5\. Voronoi Random Field Segmentation: First a pruned voronoi graph is
computed for the given map, on that a neighborhood gets concentrated
into one central point. After all points are found, neighboring
relations are obtained, meaning which node is next to another depending
on the voronoi graph. This gives several cliques, resulting in a
conditional random field. The features for this CRF are then the weak
responses of the AdaBoost classifiers for rooms, doorways and hallways.
These AdaBoost classifiers use the same features as the feature-based
segmentation. On this CRF then a loopy belief propagation is done,
resulting in several intersected segments.

## Training

In this package two algorithms are implemented that use machine-learning
techniques, which of course need pre-labeled examples for training.
These algorithms are the feature-based segmentation and the voronoi
random field segmentation. The training procedure starts as soon, as you
start the action server.

**Important**: The algorithms assume that the maps are given as 8-Bit
single channel image, with 0 as occupied space and 255 as free space.

1\. The feature-based segmentation uses two AdaBoost classifiers, one to
detect hallways and one to detect rooms, based on simulated
laserscannner-data. For the training of this algorithm hand-labelled
data showing where rooms and where hallways are. To do so see the given
files in common/files/training_maps. You can see that for different maps
some regions are grey and not white or black. These grey regions show
where a hallway/room is, the colour itself is not important. After you
have created some training files yourself you have to specify where they
lay on your file-system in the room_segmentation_action_server.launch
file. When you set the train boolean to true these given maps are read
in and given to the training routine.

2\. The voronoi random field segmentation also uses AdaBoost algorithms
to check for rooms/hallways/doorways. Additionally the weak classifier
results from these algorithms are used as Features in a conditional
random field, resulting in two different algorithms that need to be
trained. Examples for training data for this algorithm can be seen in
common/files/training_maps/voronoi_random_field_training. The data
consist of the original maps, with only white and black regions and the
labeled maps (training_maps) with colours showing the class of the
current point. Optionally one can also provide additional data to save
computation time, the precomputed maps with a voronoi graph drawn in
(colour 127) and maps that show where nodes are in the given voronoi
graph. If you provide one of it you also need to provide the other.
After you created your personal training files you also have to specify
the path to them in room_segmentation_action_server.launch. The colours
provided in the training maps have the meaning

-   77: room
-   115: hallway
-   179: doorway

## References

If you use this work please cite our ICRA 2016 paper,
<attachment:article.pdf> :

R. Bormann, F. Jordan, W. Li, J. Hampp, and M. Hägele. Room
Segmentation: Survey, Implementation, and Analysis. In *Proceedings of
the IEEE International Conference on Robotics and Automation (ICRA)*,
2016.

## Segmentation results

without furniture

  -- ----------------------------------------------------------------------------------------------------------------------- -- ---------------------------- -- ----------------------------- -- ---------------------------------- -- --------------------------------- -- ----------------------------------- --
     \<tablewidth=\"870px\" tableheight=\"58px\" tablestyle=\"text-align:left; ;text-align:center\"\>ground truth labeling      morphological segmentation      distance-based segmentation      Voronoi graph-based segmentation      feature-based room segmentation      voronoi random field segmentation   
  -- ----------------------------------------------------------------------------------------------------------------------- -- ---------------------------- -- ----------------------------- -- ---------------------------------- -- --------------------------------- -- ----------------------------------- --

![\|width=\"850\"](attachment:without_furniture.png)

with furniture

![\|width=\"850\"](attachment:with_furniture.png)

## Optimization of Work Order

The comprehensive results discussed on optimizing work order using
<https://github.com/ipa320/ipa_coverage_planning/tree/noetic_dev/ipa_building_navigation>
in our ICRA 2016 paper is available from here:
<attachment:Wagenpositionierung.xlsx>
