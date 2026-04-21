## Tutorials on Articulated Objects

## Model Classes and Model Parametrization

At the moment, the following model classes are implemented:

-   `rigid`: a rigid model, describes a static link (with Gaussian
    noise)
-   `prismatic`: a prismatic joint model, describes for example a
    drawer or a sliding cabinet door
-   `rotational`: a rotary joint model, describes for example a door
    or a door handle
-   `pca_gp`: a non-parametric model, capable of describing many other
    articulation models, like garage doors, or combinations of sliding
    and rotary motion.

All nodes in this package query the ROS parameter `filter_models`,
which names the model classes that will be considered during model
selection. The default is `rigid prismatic rotational`. Globally, all
model classes accept the parameters `sigma_position` and
`sigma_orientation`, that define the properties of the Gaussian noise
process.

### Model Parameters

The model estimators fit the models to the data, and store the found
parameters in the `ModelMsg::params` vector.

The parameters of the `rigid` model are:

-   `rigid_position\[3\]`, gives the estimated position of the rigid
    object.
-   `rigid_orientation\[4\]`, gives the estimated orientation of the
    rigid object.
-   `rigid_width`, gives the estimated width of the rigid object (only
    if a `width` channel is present in `ModelMsg::track.channels`).
-   `rigid_height`, gives the estimated height of the rigid object
    (only if a `height` channel is present in
    `ModelMsg::track.channels`).

The parameters of the `prismatic` model are:

-   `rigid_position\[3\]`, gives the average position of the
    articulated object (inherited from the `rigid` model)
-   `rigid_orientation\[4\]`, gives the average orientation of the
    articulated object (inherited from the `rigid` model)
-   `prismatic_dir\[3\]`, gives the line direction of the prismatic
    joint

The parameters of the `rotational` model are:

-   `rot_center\[3\]`, points to the rotational center of the
    rotational joint
-   `rot_axis\[4\]`, gives the rotational axis of the rotational joint
-   `rot_radius`, gives the radius of the rotational joint
-   `rot_orientation\[4\]`, gives the orientation of the articulated
    object

The `pca_gp` model is parameter-free, but requires the data points of
the trajectory to make predictions.

## Nodes

```clearsilver
name = model_learner_msg
desc = This node receives kinematic trajectories in form of <<MsgLink(articulation_msgs/TrackMsg)>> messages, fits the trajectories to all known model classes, selects the model with the lowest BIC (Bayesian Information Criterion), and publishes the result in form of a <<MsgLink(articulation_msgs/ModelMsg)>> message. The node operates in real-time i.e., it has a queue size of 1 and might drop messages if processing takes too long. 
sub {
  0.name = track
  0.type = articulation_msgs/TrackMsg
  0.desc = a kinematic trajectory of the articulated object, as observed by the robot
}
pub {
  0.name = model
  0.type = articulation_msgs/ModelMsg
  0.desc = the resulting articulation model, after model fitting and selection
}
param {
  0.name = ~sigma_position
  0.type = float
  0.desc = This parameter specifies the standard deviation of the assumed Gaussian noise in the Cartesian position of the observed trajectories. Unit: meters.
  0.default = 0.01
  1.name = ~sigma_orientation
  1.type = float
  1.desc = This parameter specifies the standard deviation of the assumed Gaussian noise in the orientation of the observed trajectories. Unit: radians.
  1.default = 4*PI (=ignore orientation)
  2.name = ~filter_models
  2.type = string
  2.desc = This parameter specifies which model classes are considered during model fitting and model selection. See the section on model classes for a complete list of available models. See the tutorial for how to add custom model classes.
  2.default = "rigid prismatic rotational"
}
```

```clearsilver
name = model_learner_srv
desc = This node provides ROS services for model fitting, selection and evaluation. This nodes provides high-level access to most of the functionality of `articulation_models` C++ library.
srv {
  0.name = model_fit
  0.type = articulation_msgs/TrackModelSrv
  0.desc = (Re-)fits the parameters of the model to the given trajectory. The model class needs to be set in the `request.model.name` field. The node then evaluates the model given these parameters and returns the resulting model. The model parameters, and the result of the evaluation, is stored in the `response.model.params` list. The projection of the trajectory, given the fitted model parameters, is stored in `response.model.track.pose_projected`.
  1.name = model_select
  1.type = articulation_msgs/TrackModelSrv
  1.desc = Selects the model class, given a noisy, unclassified trajectory of an articulated object. The node fits the given trajectory to all available model classes, evaluates the candidate models and selects the model with the lowest BIC (Bayesian Information Criterion). The resulting model is evaluated, and returned in `response.model`.
  2.name = model_eval
  2.type = articulation_msgs/TrackModelSrv
  2.desc = Evaluates a trajectory, given a model class and the model's parameters. In particular, the node computes the data likelihood, the BIC value, etc. Further, it projects the trajectory onto the model (`response.model.track.pose_projected`), 
}
param {
  0.name = ~sigma_position
  0.type = float
  0.desc = This parameter specifies the standard deviation of the assumed Gaussian noise in the Cartesian position of the observed trajectories. Unit: meters.
  0.default = 0.01
  1.name = ~sigma_orientation
  1.type = float
  1.desc = This parameter specifies the standard deviation of the assumed Gaussian noise in the orientation of the observed trajectories. Unit: radians.
  1.default = 4*PI (=ignore orientation)
  2.name = ~filter_models
  2.type = string
  2.desc = This parameter specifies which model classes are considered during model fitting and model selection. See the section on model classes for a complete list of available models. See the tutorial for how to add custom model classes.
  2.default = "rigid prismatic rotational"
}
```

```clearsilver
name = model_learner_prior
desc = This node is an extension of the `model_learner_srv` node. Next to providing ROS services for model fitting, selection and evaluation, and allows additionally to store, retrieve prior models and use them during model fitting and selection. Furthermore, it provides a service call for evaluating the model fitting/selection of partial trajectories, without the need for repeatedly calling the model selection service.
srv {
  0.name = model_select
  0.type = articulation_msgs/TrackModelSrv
  0.desc = Selects the model class, given a noisy, unclassified trajectory of an articulated object. The node fits the given trajectory to all available model classes, evaluates the candidate models and selects the model with the lowest BIC (Bayesian Information Criterion). The resulting model is evaluated, and returned in `response.model`. If a model class name is provided in `request.model.name`, only the parameters of this model are (re-)fitted. The model parameters, and the result of the evaluation, is stored in the `response.model.params` list. The projection of the trajectory, given the fitted model parameters, is stored in `response.model.track.pose_projected`.
  1.name = model_select_eval
  1.type = articulation_msgs/TrackModelSrv
  1.desc = Evaluates a trajectory, given a model class and the model's parameters. In particular, the node computes the data likelihood, the BIC value, etc. Further, it projects the trajectory onto the model (`response.model.track.pose_projected`).
  2.name = model_store
  2.type = articulation_msgs/TrackModelSrv
  2.desc = Store a model in the prior model database. The model is identified uniquely by its id (`request.model.id`), so repeated calls to `model_store` with the same `model.id` will overwrite the corresponding model. A special value of `model.id = -1` will automatically assign an unused `id` value to the field. This automatically assigned identifier can then be retrieved in `response.model.id`.
  3.name = model_prior_get
  3.type = articulation_msgs/GetModelPriorSrv
  3.desc = Retrieves the current list of prior models, stored in the `model_learner_prior` node. Useful for inspection, or saving the prior to disk (see `prior_save.py` for an example)
  4.name = model_prior_set
  4.type = articulation_msgs/SetModelPriorSrv
  4.desc = Sets the current list of prior models in the `model_learner_prior` node. This service can also be used to clear the list of known prior models, simply by calling it with an empty list. Useful for restoring the prior from disk (see `prior_load.py`).
}
param {
  0.name = ~sigma_position
  0.type = float
  0.desc = This parameter specifies the standard deviation of the assumed Gaussian noise in the Cartesian position of the observed trajectories. Unit: meters.
  0.default = 0.01
  1.name = ~sigma_orientation
  1.type = float
  1.desc = This parameter specifies the standard deviation of the assumed Gaussian noise in the orientation of the observed trajectories. Unit: radians.
  1.default = 4*PI (=ignore orientation)
  2.name = ~filter_models
  2.type = string
  2.desc = This parameter specifies which model classes are considered during model fitting and model selection. See the section on model classes for a complete list of available models. See the tutorial for how to add custom model classes.
  2.default = "rigid prismatic rotational"
  3.name = ~do_align
  3.type = boolean
  3.desc = When prior models are available, this parameter specifies whether the new data trajectory is aligned to the existing trajectory data of the prior model using the Iteratively Closest Point algorithm (see also <<TracLink(ros-pkg IPC)>>). 
  3.default = false
}
```

## Useful Scripts

```clearsilver
name = prior_publisher_atonce.py
desc = This node reads trajectories from multiple files, calls model fitting and selection, and stores the found model as a prior. For an example, run `roslaunch demo_fitting prior_iros_at_once.launch`.
pub {
  0.name = model
  0.type = articulation_msgs/TrackMsg
  0.desc = Resulting models, after model fitting and selection. Useful for visualization in RVIZ. 
}
srv_called {
  0.name = model_select
  0.type = articulation_msgs/TrackModelSrv
  0.desc = Select a suitable model for the trajectory. }
  1.name = model_store
  1.type = articulation_msgs/TrackModelSrv
  1.desc = Store the found model as a prior model, and use it as prior information during model fitting and selection for future trajectories.
}
```

```clearsilver
name = simple_publisher.py
desc = This node publishes a trajectory from a text file. Each line of the text file contains a single pose, with space-separated values. The format of a pose is "x y z [qw qx qy qz [width height]]", where x y z is the Cartesian position, qw qx qy qz is the (optional) orientation, and width and height is the (optional) dimensions of a door/drawer front. The script reads the complete file at once, then moves the trajectory to start at the origin. Then it incrementally sends out <<MsgLink(articulation_msgs/TrackMsg)>> messages, at 0.05 second intervals. For an example of this script, run `roslaunch demo_fitting fit_kitchen.launch`.
pub {
  0.name = track
  0.type = articulation_msgs/TrackMsg
  0.desc = Incrementally publishes kinematic trajectories that it reads from a text file. }
```

```clearsilver
name = prior_save.py
desc = This node retrieves the current prior models using the `model_prior_get` service and stores it in a file.
srv_called {
  3.name = model_prior_get
  3.type = articulation_msgs/GetModelPriorSrv
  3.desc = Retrieves the current list of prior models. }
```

```clearsilver
name = prior_load.py
desc = This node loads prior models from a file, and restores them using the `model_prior_set` service.
srv_called {
  3.name = model_prior_set
  3.type = articulation_msgs/SetModelPriorSrv
  3.desc = Sets the current list of prior models. }
```

## References

-   Jürgen Sturm, Cyrill Stachniss, Wolfram Burgard. A Probabilistic
    Framework for Learning Kinematic Models of Articulated Objects. In
    Journal on Artificial Intelligence Research (JAIR), volume 41, 2011.
    \[ [pdf](http://cvpr.in.tum.de/_media/spezial/bib/sturm11jair.pdf)
    \] \[
    [bibtex](http://cvpr.in.tum.de/members/sturmju/publications?key=sturm11jair)
    \]
-   Jürgen Sturm, Advait Jain, Cyrill Stachniss, Charlie Kemp, Wolfram
    Burgard. Operating Articulated Objects Based on Experience. In Proc.
    of the International Conference on Intelligent Robot Systems (IROS),
    Anchorage, USA, 2010. \[
    [pdf](http://www.informatik.uni-freiburg.de/~sturm/media/sturm10iros.pdf)
    \] \[
    [bibtex](http://www.informatik.uni-freiburg.de/~sturm/media/publications-sturm.bib)
    \]
-   Jürgen Sturm, Kurt Konolige, Cyrill Stachniss, Wolfram Burgard.
    Vision-based Detection for Learning Articulation Models of Cabinet
    Doors and Drawers in Household Environments. In Proc. of the IEEE
    International Conference on Robotics and Automation (ICRA),
    Anchorage, USA, 2010. \[
    [pdf](http://www.informatik.uni-freiburg.de/~sturm/media/sturm10icra.pdf)
    \] \[
    [bibtex](http://www.informatik.uni-freiburg.de/~sturm/media/publications-sturm.bib)
    \]
-   Jürgen Sturm, Cyrill Stachniss, Vijay Pradeep, Christian Plagemann,
    Kurt Konolige, Wolfram Burgard. Learning Kinematic Models for
    Articulated Objects. In Proc. of the International Joint Conference
    on Artificial Intelligence (IJCAI), Pasadena, USA, 2009. \[
    [pdf](http://www.informatik.uni-freiburg.de/~sturm/media/sturm09ijcai.pdf)
    \] \[
    [bibtex](http://www.informatik.uni-freiburg.de/~sturm/media/publications-sturm.bib)
    \]

## More Information

More information (including videos, papers, presentations) can be found
on the homepage of
[Juergen Sturm](http://vision.in.tum.de/members/sturmju).

## Report a Bug

If you run into any problems, please feel free to contact Juergen Sturm
<juergen.sturm@in.tum.de>.
