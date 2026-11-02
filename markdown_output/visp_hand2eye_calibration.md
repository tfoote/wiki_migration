## Overview

<a id="Overview"></a> visp_hand2eye_calibration
is a ROS package that computes extrinsic camera parameters : the
constant transformation from the hand to the camera coordinates.

Let's consider a camera attached to a robotic hand, as shown in the
following diagram: ![attachment:calibrations.png](doc/calibrations.png)

The interest of this package is to perform the hand to eye calibration
part.

To do so, two sets of transformations are fed to the `calibrator`
node.

- a list of camera-to-object transformations
- a list of world to hand transformations

Once the node has enough transformations, it can estimate the
camera-to-hand transformation which is the goal of the calibration.

The package consists of a `calibrator` node and an experimental client
doing a sample calibration from a few poses.

The experimental client is merely there for a quick demonstration of the
package abilities.

## Installation

visp_hand2eye_calibration is
part of [vision_visp](https://index.ros.org/p/vision_visp) stack.

- To install
  visp_hand2eye_calibration
  package run 

```
sudo apt-get install ros-$ROS_DISTRO-visp-hand2eye-calibration
```



<!-- -->

- Or to install the complete stack run 

```
sudo apt-get install ros-$ROS_DISTRO-vision-visp
```



## Usage

To run the `calibrator` node: 

```
rosrun visp_hand2eye_calibration visp_hand2eye_calibration_calibrator
```



## Example

<a id="Example"></a> An example client is shipped
with this package. It feeds different transformations (camera->object
and world->hand) to the calibrator which computes the relative
transformation between the the camera and the hand.

To try this example, run roscore first. 

```
roscore
```



Then, run the client:



```
rosrun visp_hand2eye_calibration visp_hand2eye_calibration_client
```



Finally, run the calibrator:



```
rosrun visp_hand2eye_calibration visp_hand2eye_calibration_calibrator
```



The output displayed in the terminal running your client should look
like this:



```
[ INFO] [1329226083.184531090]: Waiting for topics...
[ INFO] [1329226084.186233704]: 1) GROUND TRUTH:
[ INFO] [1329226084.186327570]: hand to eye transformation: 
translation: 
  x: 0.1
  y: 0.2
  z: 0.3
rotation: 
  x: 0.96875
  y: 0.0863555
  z: -0.0863555
  w: 0.215889


[ INFO] [1329226085.186682976]: 2) QUICK SERVICE:
[ INFO] [1329226085.188853282]: hand_camera: 
translation: 
  x: 0.1
  y: 0.2
  z: 0.3
rotation: 
  x: 0.96875
  y: 0.0863555
  z: -0.0863555
  w: 0.215889

[ INFO] [1329226085.188915366]: 3) TOPIC STREAM:
[ INFO] [1329226085.190303537]: hand_camera: 
translation: 
  x: 0.1
  y: 0.2
  z: 0.3
rotation: 
  x: 0.96875
  y: 0.0863555
  z: -0.0863555
  w: 0.215889
```



## Nodes

<a id="NodeApi"></a>

### calibrator

#### Subscribed Topics

- `world_effector`
  ([visp_hand2eye_calibration/msg/TransformArray](https://docs.ros.org/en/rolling/p/visp_hand2eye_calibration/msg/TransformArray.html)):
  transformation between the world and the hand frame. The node expects
  to receive several of those transformations.
- `camera_object`
  ([visp_hand2eye_calibration/msg/TransformArray](https://docs.ros.org/en/rolling/p/visp_hand2eye_calibration/msg/TransformArray.html)):
  transformation between the camera and the object frame. The node
  expects to receive several of those transformations.

#### Services Called

- `compute_effector_camera`
  ([visp_hand2eye_calibration/srv/compute_effector_camera](https://docs.ros.org/en/rolling/p/visp_hand2eye_calibration/srv/compute_effector_camera.html)):
  Returns the hand to camera transformation result after calibration
  based on the data published on the subscribed topics.
- `compute_effector_camera_quick`
  ([visp_hand2eye_calibration/srv/compute_effector_camera_quick](https://docs.ros.org/en/rolling/p/visp_hand2eye_calibration/srv/compute_effector_camera_quick.html)):
  Returns the hand to camera transformation result after calibration.
  This service is not based on the data published on the subscribed
  topics. Instead, the transformation are passed as service parameters.
- `reset`
  ([visp_hand2eye_calibration/srv/reset](https://docs.ros.org/en/rolling/p/visp_hand2eye_calibration/srv/reset.html)):
  Reset all the data published on the subscribed topics. Only new
  publications (transformations) will be taken into account.
