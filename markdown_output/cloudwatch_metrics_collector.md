## Overview

The ` cloudwatch_metrics_collector ` ROS Node publishes your robot's
metrics to the cloud to enable you to easily track the health of a fleet
with the use of automated monitoring and actions for when a robot's
metrics show abnormalities. You can easily track historic trends and
profile behavior such as resource usage. Out of the box it provides a
ROS interface to take a ROS message defining a metric and publish it to
Amazon Cloud``Watch Metrics. The only configuration required to get
started is setting up AWS Credentials and Permissions for your robot.The
Cloud``Watch Metrics Node can be used with existing ROS Nodes that
publish metric messages or with your own nodes if you instrument them to
publish your own custom metrics.

```Amazon CloudWatch Metrics Summary```: Amazon Cloud``Watch is
a monitoring and management service built for developers, system
operators, site reliability engineers (SRE), and IT managers.
Cloud``Watch provides you with data and actionable insights to monitor
your applications, understand and respond to system-wide performance
changes, optimize resource utilization, and get a unified view of
operational health. Cloud``Watch collects monitoring and operational
data in the form of logs, metrics, and events, providing you with a
unified view of AWS resources, applications and services that run on
AWS, and on-premises servers. You can use Cloud``Watch to set high
resolution alarms, visualize logs and metrics side by side, take
automated actions, troubleshoot issues, and discover insights to
optimize your applications, and ensure they are running smoothly.

```Keywords```: ROS, AWS, Cloud``Watch, Metrics

### License

The source code is released under an
[Apache 2.0](https://aws.amazon.com/apache-2-0/).

### Supported ROS Distributions

-   Kinetic
-   Lunar
-   Melodic
