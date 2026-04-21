## Package Summary

This package is a ROS wrapper for the open-source project
[OpenFABMAP](http://code.google.com/p/openfabmap/), an implementation of
the Fast Appearance-based Mapping algorithm (FAB-MAP) originally
developed by Mark Cummins and Paul Newman.

FAB-MAP performs location matching between places that have been visited
within the world as well as providing a measure of the probability of
being at a new, previously unvisited location. Camera images form the
sole input to the system, from which bag-of-words models are formed
through the extraction of appearance-based (e.g. SURF) features.

## Usage

OpenFABMAP can be used in two modes, training or testing. Examples of
training and testing are provided in the launch files **`learn`** and
**`run`** respectively.

Datasets are available at the
[CyPhy Lab](https://wiki.qut.edu.au/display/cyphy/Datasets), with
[QUT Level 7](https://wiki.qut.edu.au/display/cyphy/Indoor+Level+7+S-Block+Dataset)
available in [rosbag](http://www.ros.org/wiki/rosbag) format.

## Example

Below are examples of training and testing on the garden_loop.bag file.
In practice you do not train your codebook on the test-set but for
simplicity we use a single bag file, available
[here](https://wiki.qut.edu.au/display/cyphy/Datasets). The included
codebook's are trained on various indoor and outdoor datasets, details
and downloads available on the same page.

### Training

The learning of a codebook is typically completed 'offline' although a
case can be made for the creation of incremental 'online' codebooks.
In any case it can be useful to train a codebook on data gathered in
various conditions and locations stored in multiple
[rosbag](http://www.ros.org/wiki/rosbag) files.

```
roscore

rosparam set use_sim_time true

roslaunch openfabmap2 learn.launch image:=/stereo/left/image_raw path:=/codebook_path

rosbag play garden_loop.bag --clock
```

This will process images on the supplied topic for a number of frame and
then save the codebook and descriptor files to the 'path' location.

Default parameters used within the **`learn`** launch file are provided
below:

-   Detector Type: SURF
-   Sample Rate: 0.5Hz
-   Max Images: 100
-   Cluster Size: 0.5
-   Visualise: true

#### Example Visualisation

![](attachment:garden_key_points.png)

### Testing

While testing, the node describes the stream of images by words in the
provided codebook and publishes candidate matches to previous images
observed in the test-set. This process is typically run 'online', the
following example is provided.

```
roscore

rosparam set use_sim_time true

roslaunch openfabmap2 run.launch image:=/stereo/left/image_raw path:=/codebook_path

rosbag play garden_loop.bag --clock
```

This example will will visualise the matches between images as a
confusion matrix. Time along the vertical axis and frame ID on the
horizontal (origin top left), white representing the matches found.

Default parameters used within the **`run`** launch file are provided
below:

-   Detector Type: SURF
-   FABMAP Version: FABMAP2
-   New Place Method: Sampled
-   Sample Rate: 12.5Hz
-   Visualise: true
-   Min Match Value: 0.98
-   Max Matches: 3
-   Disable Self Match: false
-   Disable Unknown Match: false
-   Add Only New Places: false

#### Example Visualisation

![](attachment:garden_confusion_matrix_R02.png)

## Bug Reports & Feature Requests
