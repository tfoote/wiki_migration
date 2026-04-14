## Overview

The \`cloudwatch_logger\` node enables logs generated in a ROS system to
get sent to Amazon Cloud\`\`Watch Logs. Out of the box, this node
provides the ability to subscribe to the \`/rosout_agg\` (rosout
aggregated) topic, which all logs using the ROS logging framework will
be published to, and sends logs to the Amazon Cloud\`\`Watch Logs
service. Logs can be sent to Amazon Cloud\`\`Watch Logs selectively
based on log severity. The \`cloudwatch_logger\` node can also subscribe
to other topics if logs are not sent to \`/rosout_agg\`, and it is able
to unsubscribe to the \`/rosout_agg\` topic for getting logs.

The \`cloudwatch_logger\` node wraps the
[aws-sdk-c++](https://github.com/aws/aws-sdk-cpp) in a ROS service API.

\`Amazon CloudWatch Logs Summary\`: Amazon Cloud\`\`Watch Logs can
monitor applications and systems using log data. You can create alarms
in Cloud\`\`Watch and receive notifications of particular API activity
as captured by Cloud\`\`Trail and use the notification to perform
troubleshooting. By default, logs are kept indefinitely and never
expire. You can adjust the retention policy for each log group, keeping
the indefinite retention, or choosing a retention periods between 10
years and one day. Amazon Cloud\`\`Watch Logs stores your log data in
highly durable storage.

\`Features in Active Development\`: - Offline caching: now, a batch of
logs will be dropped if the node fails to send them to AWS
Cloud\`\`Watch Logs. We will enable offline caching and try to save
logs. - Send logs to different log groups/streams: now, one node will
send logs to one log stream within one log group. We will enable a node
to send logs to different log groups/streams.

\`Keywords\`: ROS Application logs, System logs, Amazon Cloud\`\`Watch
Logs service

### License

The source code is released under an
[Apache 2.0](https://aws.amazon.com/apache-2-0/).

### Supported ROS Distributions

-   Kinetic
-   Lunar
-   Melodic
