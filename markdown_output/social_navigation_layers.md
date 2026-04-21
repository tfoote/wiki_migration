## Social Navigation Layers

There are currently two social navigation layers. However, they both
share functionality in that they both subscribe to where people are and
alter the costmaps with a Gaussian distribution around those people.
Both classes derive from the general !SocialLayer class.

They can be used in
[costmap configurations](http://wiki.ros.org/costmap_2d/Tutorials/Configuring%20Layered%20Costmaps)
with the following types:

-   `social_navigation_layers::ProxemicLayer`
-   `social_navigation_layers::PassingLayer`

```clearsilver
name = ProxemicLayer/PassingLayer
desc = The interface for both layers is the same. 
sub {
  0.name = /people
  0.type = people_msgs/People
  0.desc = People to navigate around
}
param {
  0.name = enabled
  0.type = bool
  0.desc = Whether to apply this plugin or not
  0.default = True
  1.name = cutoff
  1.type = double
  1.desc = Smallest value to publish on costmap adjustments
  1.default = 10.0
  2.name = amplitude
  2.type = double
  2.desc = Amplitude of adjustments at peak
  2.default = 77.0
  3.name = covariance
  3.type = double
  3.desc = Covariance of adjustments
  3.default = 0.25
  4.name = factor
  4.type = double
  4.desc = Factor with which to scale the velocity
  4.default = 5.0
  5.name = keep_time
  5.type = double
  5.desc = Pause before clearing leg list
  5.default = 0.75
}
```

## How the Costmap Changes

![](attachment:person.png)

### Proxemic Layer

The proxemic layer adds gaussian costs all around the detected person,
with the parameters specified above. If the person is stationary, the
gaussian is perfectly round. However, if the person is moving, then the
costs will be increased in the direction of their motion. How far in
front of the person the costs are increased is proportional to the
`factor` parameter.

#### Stationary Person

![](attachment:prox.png)

#### Moving Person

![](attachment:proxscale.png)

### Passing Layer

This layer is intended to cause the robot to always pass on the left
side of a person and will hence only increase the cost on one side of
the person.

![](attachment:passing.png)
