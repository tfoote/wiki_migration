## Overview

The ROS Anomaly Detector Module (ADM) is designed to execute alongside
industrial robotic arm tasks to detect unintended deviations at the
application level. The ADM utilizes a learning based technique to
achieve this. The process has been made efficient by building the ADM as
a ROS package that aptly fits in the ROS ecosystem. While this module is
specific to anomaly detection for an industrial arm, it is extensible to
other projects with similar goals. This is meant to be a starting point
for other such projects.

The crux of anomaly detection within this module relies on a three step
process. The steps includes creating datasets out of the published
messages within ROS, training learning models from those datasets, and
deploying it in production. Appropriately, the three modes that the ROS
ADM can be executed in are Collect, Learn, and Operate. The following
image presents the workflow.

![High Level ADM Workflow\|](attachment:adm_flow.png)
