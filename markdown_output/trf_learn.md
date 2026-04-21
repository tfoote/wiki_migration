## Process Overview

This package uses visual feature learning to create detectors for
operating the behaviors included (drawer opening, flip style light
switches, and rocker style light switches). Before using the included
behaviors on real world mechanisms, you'll first need to perform an
initialization and a data collection step to create a visual classifier
for your specific mechanism. After these two steps, you'll be able to
run the included behaviors with your new learned visual detector using
the execute launch script (execute.launch).

Specifically, the steps that you'll need to perform are:

-   launch navigation and manipulation nodes required (trf_learn.launch)
    

```
roslaunch trf_learn trf_learn.launch
```


-   Localize the robot with rviz.
-   Position your robot in front of the mechanism to operate.
-   Initialize the learning procedure. 

```
roslaunch trf_learn init.launch
```


    -   after this completes the collected data will be saved in
        /.ros/locations_narrow_v11.pkl
-   Launch the learning procedure. 

```
roslaunch trf_learn practice.launch
```



Finally to execute your learned behavior use: 

```
roslaunch trf_learn execute.launch
```



When initialization finishes, you'll progress to the second stage and
set the robot to gather additional data autonomously for its classifier
(using practice.launch). Due to the experimental nature of the code,
currently this data collection process takes a few hours but once it's
done use the task execution script (execute.launch) to activate the
behavior with its trained detector.
