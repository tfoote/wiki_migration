## How This Package Should Work

### Summary

  -- -- -- ------------------------------------------------------------------------- -- -- --
           <style="text-align: center;"> ![](attachment:laser_milk_carton.png)         
           <style="text-align: center;">Laser point detected on milk carton            
  -- -- -- ------------------------------------------------------------------------- -- -- --

Stereo images comes and are filtered using intensity thresholding and
image differencing to select bright parts of the image that are moving.
The resulting connected components are then tracked (large connected
components are thrown out). After having been tracked for a couple of
frames, the resulting connected components are then fed to a random
forest classifier. The first positive classification is then
triangulated resulting in a 3D point.

At this time, if the user has also left clicked a PC mouse, then the 3D
point will be published. If there is not mouse input then all the
positive classifications will be saved by the system to use as negative
training examples. These false positives will be incorporated into the
classifier whenever the system receives the string `rebuild` on the
`laser_mode` topic. The rationale for this step is that if the user
has not turned on the laser pointer then any detections can be safely be
marked as false positives (with some caveats).

### More Details

The main node in this package is the `laser_pointer_detector_node.py`.
When it launches it will subscribe to the rectified images produced by
the specified stereo pair
(`/CAMERA_NAME/(left\|right)/image_color_rect`), and calibration
parameter on `/CAMERA_NAME/(left\|right)/camera_info`.

After getting a pair of images, the detector will run two filters. The
first is a motion filter that uses simple image differencing to select
regions that have recently moved that are smaller than a threshold size
(`max_blob_area`). The second is an intensity filter that tries to
select locally bright areas in the image. It is controlled by two
parameters: `intensity_threshold_low`, and
`intensity_threshold_high`. This filter is composed of the results of
two filters based on thresholding the intensity in a specified color
channel (`color_channel`) with two different numbers and ORing the
resulting image.

  -- ------------------------------------------------------ ----- -- ---------------------------------------------------------------------------- -- --------------------------------------------------------- ----- --
     <style="text-align: center; vertical-align: top;"   3>      <99% style="text-align: center;"> ![](attachment:hypotheses_panel.png)      <style="text-align: center; vertical-align: bottom;"   3>   
  -- ------------------------------------------------------ ----- -- ---------------------------------------------------------------------------- -- --------------------------------------------------------- ----- --

The detector will then OR the results of the intensity and motion filter
together and feed the remaining connected components in the image to a
tracker. The tracker, on each time step will associate each of its track
with the closest connected component within a threshold distance
(`tracker_max_pix_treshold`). Tracks that have not been associated for
components for a number seconds (`tracker_max_time_threshold`) will be
deleted. Tracks that have been around for a certain minimum time
(`min_age`) are then sent to the random forest classifier.

  -- -- -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -- -- --
           <99% style="text-align: center;"> ![](attachment:hypotheses.png)                                                                                                                                                                       
           <99% style="text-align: center;">Hypotheses resulting from the above motion and intensity masks. In the above the PR2's head is slowly panning to the right resulting in bright scene points appearing as if they are moving.         
  -- -- -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -- -- --

On start up, the classifier projects its training set into a lower
dimensional space using PCA keep just enough dimensions to preserve a
certain percentage of variance in the original data
(`pca_variance_retain`). With this dimensionality reduced set, the
detector constructs a number of random trees (`number_of_learners`)
for use during classification.

The detector repeats the process above for both images in the stereo
pair independently. Then it selects the largest connected component from
the processed results for each image and triangulates the components'
two centroids into a 3D point using the camera parameters.

At this time, if the user has also left clicked a PC mouse (`True` on
topic `mouse_click`), then the 3D point will be published (on the
topic `cursor3d`). If there is not mouse input then all the positive
classifications will be saved by the system to use as negative training
examples. These false positives will be incorporated into the classifier
whenever the system receives the string `rebuild` on the
`laser_mode` topic. The rationale for this step is that if the user
has not turned on the laser pointer then any detections can be safely be
marked as false positives (with some caveats).

## Setting up and Running the Laser Detector

### What This Package Assumes

  -- -- -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -- --
           <style="text-align: center;"> ![](attachment:handheld_laser_mouse.jpg)                                                                                                 
           <style="text-align: center;">A hand held laser pointer coupled with the clicker switch of a mouse (construction instructions for this will be posted shortly).         
  -- -- -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -- --

-   A camera system setup in a similar manner to the PR2 with
    compatibility with dynamic_reconfigure (this assumption can be
    removed if you manage your own exposure settings).
-   There is a mouse device whose left click button is somehow coupled
    to the on switch of a laser pointer. A more integrated solution such
    as the above is preferred but this will still work with a regular
    wireless mouse and laser pointer.

### Tuning Camera Exposures and Intensity Thresholds

Prior to running, it's best to check the camera exposure and intensity
threshold settings. If you are running this in an office with
fluorescent lights (and no windows) then this step is not strictly
necessary. Unfortunately, setting these parameters is still a manual
process. Maybe there will be a spiffy automated way to do this in the
future.

On the first terminal run:



```
roslaunch laser_detector_office_local.launch 2> /dev/null
```

 The piping to `/dev/null` is due to some
OpenCV weirdness. Leave it out if you're willing to put up with lots of
annoying printouts.

On the second terminal run:



```
rosrun laser_interface user_interface_node.py
```

 In the display that appears, press `d`
(another window showing video images should pop up) then `g` (a whole
bunch of new windows should pop up).

On the third terminal:



```
rosrun dynamic_reconfigure reconfigure_gui
```

 After the reconfigure_gui pops up we will
select `/wide_stereo_both`. Uncheck everything that looks like it'll
try do do things automatically (`auto_gain`, `auto_black_level`, and
`auto_exposure`).

Now we will play a little not so fun game with the camera exposure and
intensity thresholds. Shine your laser pointer in the scene on both
bright and dark objects using the `video` window to make sure that the
laser point is visible in the image in both cases using the `exposure`
setting in the `reconfigure_gui` (set the `gain`, `brightness`,
and `black_level to some reasonable value and forget about them). Next
we adjust the intensity threshold through the command line:



```
rosparam set laser_pointer_detector/intensity_threshold_low 20
rosparam set laser_pointer_detector/intensity_threshold_high 215
```

 Replace 20 and 215 with values that will allow
the laser point to show up as a white region in the `intensity`
window. Adjust `intensity_threshold_low` such that the laser point
will show up when shone on dark objects (dark brown tables, blue jeans,
etc), and `intensity_threshold_high` so that it will show up on bright
objects (whiteboards, bright walls, etc). Reduce the `exposure` as
needed. When moving the the laser point around you should be able to see
that it's marked by a blue square in the image.

When satisfied with the results, save your camera settings (replace the
node name and file name if needed):



```
rosrun save_dynamic_config /wide_stereo_both my_awesome_exposure_settings.yaml
```

 Now place your new yaml file into some safe
package, for now we'll move it to the laser_interface package:



```
mv my_awesome_exposure_settings.yaml `rospack find laser_interface`/
```

 For the intensity thresholds we'll, open your
favorite text editor and type the following (replace these numbers with
yours):



```
intensity_threshold_low   : 72
intensity_threshold_high  : 146
```

 Let's call this file
`intensity_threshold.yaml`.

Open `laser_detector_office_local.launch` and replace office.yaml with
`intensity_threshold.yaml`, and `office_exposure.yaml` with
`my_awesome_exposure_settings.yaml` (or some less verbose equivalent,
you can also just overwrite the default yaml files with yours).

### Making an Initial Training Set

Now we'll give the detector some positive examples to work with. First,
close the running detector node (Ctrl-C
laser_detector_office_local.launch) from the last step and launch a
fresh copy:



```
roslaunch laser_detector_office_local.launch 2> /dev/null
```

 It should now be using your new settings. Point
the stereo pair to a static scene (no people, no moving objects, no
trees blowing in the wind, etc). In the GUI (user_interface_node.py),
press `p`, left click on the GUI window (and hold down the mouse
button) then start shining the laser point in this static scene. Make
sure that the laser point is the only moving thing. You should see the
following messages in your console:



```
LaserPointerDetector.mode_handler: gather_positive_examples True
LaserPointerDetector.click_handler: click!
EmbodiedLaserDetector.record: expected 1 got 1, 96
...
EmbodiedLaserDetector.record: expected 1 got 1, 97
...
EmbodiedLaserDetector.record: expected 1 got 1, 118
```

 Do this until you've gathered a sufficiently
representative number of examples (couple of hundreds, more is better
but not of the same stuff). This step can be repeated if need be.

Now we gather negative examples by pointing the cameras at a scene full
of shiny moving things. The goal is to get the laser detector to
misclassify and print out messages similar to the following:



```
EmbodiedLaserDetector.record: expected 0 (no laser detections) but got 1 (laser detection), 122 instances
EmbodiedLaserDetector.record: expected 0 (no laser detections) but got 1 (laser detection), 123 instances
EmbodiedLaserDetector.record: expected 0 (no laser detections) but got 1 (laser detection), 124 instances
EmbodiedLaserDetector.record: expected 0 (no laser detections) but got 1 (laser detection), 125 instances
...
```

 After a couple of hundreds of these, press
space bar in the GUI to rebuild the classifier and write our dataset to
disk. You should see something like the following (but with more
examples hopefully):



```
rosrun laser_interface user_interface_node.py
```

0 You should now see a file called
`PatchClassifier.dataset.pickle`.

### Running on a Robot

Check out this code on the robot first. Then edit the file
`laser_detector_sunny_pr2c1.launch` on the robot and replace the yaml
files with your appropriate settings. Copy over the file
PatchClassifier.dataset.pickle to the package `laser_interface`.
Launch your new file on the robot:



```
rosrun laser_interface user_interface_node.py
```

1 If nothing happens, then try it without the
redirection to see if there are any errors (besides from OpenCV
complaining).

Then on a computer with an X server run:



```
rosrun laser_interface user_interface_node.py
```

2 To use, give focus to the GUI and turn on the
laser point after left clicking. When there are detections you should
see them on the `cursor3d` topic:



```
rosrun laser_interface user_interface_node.py
```

3

### Maintenance

Periodically (or often? sorry!), you will see false positives detected
on the console. Pressing space bar in the GUI will rebuild the
classifier. Usually this will get rid of them.

## Command Line Usage



```
rosrun laser_interface user_interface_node.py
```

4

## ROS API



```
rosrun laser_interface user_interface_node.py
```

5



```
rosrun laser_interface user_interface_node.py
```

6
