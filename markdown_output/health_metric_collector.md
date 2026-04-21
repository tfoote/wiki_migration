## Overview

This `health_metric_collector` ROS node collects system metrics and
publishes them to `/metrics` topic. The
`cloudwatch_metrics_collector` node is subscribed to this topic and
will publish the metrics to Amazon Cloud``Watch when it is
instantiated.

```Keywords```: ROS, AWS, Cloud``Watch, Metrics

### License

The source code is released under an
[Apache 2.0](https://aws.amazon.com/apache-2-0/).

### Supported ROS Distributions

-   Kinetic
-   Lunar
-   Melodic
