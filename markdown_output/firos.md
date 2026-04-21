## Overview

FIROS is a tool that helps connecting robots to the cloud. For this
purpose it uses the Robot Operating System (ROS, <http://www.ros.org/>)
and the FIWARE Context Broker
(<http://catalogue.fiware.org/enablers/publishsubscribe-context-broker-orion-context-broker>)
as a way to publish and listen robot's data.

FIROS works as a translator between the robotics field and the cloud
world, transforming ROS messages into NGSI to publish them in the cloud,
and vice versa.

Visit <https://github.com/Ikergune/firos/blob/master/README.md> to know
how to install and configure FIROS. To execute FIROS run:
```
$ rosrun firos core.py
```

Details can also be found in the following
[paper](http://fernandoherranz.com/wp-content/uploads/2015/07/HAIS62.pdf):

```
@incollection{herranz2015cloud,
  title={Cloud Robotics in FIWARE: A Proof of Concept},
  author={Herranz, F and Jaime, J and Gonz{\'a}lez, I and Hern{\'a}ndez, {\'A}},
  booktitle={Hybrid Artificial Intelligent Systems},
  pages={580--591},
  year={2015},
  publisher={Springer International Publishing}
}
```

## Report a Bug

<<GitHubIssues(Ikergune/firos)>>
