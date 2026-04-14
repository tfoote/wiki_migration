This stack is an extension of the popular [move_base](move_base)
navigation stack enhancing a robotic platform to recover its expected
performance after a fault happened, as collisions.

This navigation stack extension provides interfaces for handling faults
over a navigation task, like collisions or faulty sensors. By default we
provide some plugins for collision detection. However, new approaches
for fault detection are highly encouraged.

\'\'\' Important Information \'\'\'

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------- --
     \<#cce0ff\>\'\'\'Note:\'\'\' This package is the result for a master thesis project. Additional information, write a mail to jocamaba1989@gmail.com   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------- --

## Components List

1\. Collisions Detector and Diagnoser. a. Simple Sensor Fusion Detector.
a. Simple Sensor Fusion Detector and Diagnoser. a. Sensor Fusion Method
Detector and Diagnoser.

1\. Collisions Recovery Behavior. a. Mislocalization. a. Major
Collision. a. Minor Collision. a. Unknown Collision.

## Collision Detection Sources

-   RGB Camera. vision_utils_ros
-   Accelerometer. raspberry_ros
-   IMU. other_sources

## Launching Nodes

### fault_tolerant_move_base (complete implementation)

a\. roslaunch collisions_launch 2dnav.launch a. rosrun

### collision detection and diagnosis (without recovery)

a\. roslaunch a. rosrun collision_detector_diagnoser
collision_detector_diagnoser_node

## Package Configuration

### Parameters

-   fault_detector:
    collision_detector_diagnoser/CollisionDetectorDiagnoser

```{=html}
<!-- -->
```
-   sensor_fusion: sensor_number: 4

```{=html}
<!-- -->
```
-   fault_recovery_behaviors: - name: \'simple_collision_recovery\'
    type: \'simple_collision_recovery/SimpleCollisionRecovery\' - name:
    \'mislocalization_collision_recovery\' type:
    \'mislocalization_collision_recovery/MisLocalizationCollisionRecovery\'

## Main Dependencies

-   [move_base](move_base)
-   [vision_opencv](vision_opencv)
-   [pcl_ros](pcl_ros)

Related repositories available on:

<https://github.com/jcmayoral/collision_stuff>
<https://github.com/jcmayoral/collision_detector_observers>
<https://github.com/jcmayoral/vision_collision_detector>
<https://github.com/jcmayoral/collision_detector_functions>
<https://github.com/jcmayoral/VisionUtils>
