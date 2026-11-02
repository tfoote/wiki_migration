## Realtime Publisher

The `realtime_tools::RealtimePublisher` allows users that write C++
[realtime controllers](https://index.ros.org/p/pr2_controller_manager)
to publish messages on a ROS topic from a hard realtime loop. The normal
ROS publisher is not realtime safe, and should not be used from within
the update loop of a realtime controller. The realtime publisher is a
wrapper around the ROS publisher; the wrapper creates an extra
non-realtime thread that publishes messages on a ROS topic. The example
below shows a typical usage of the realtime publisher in the `init()`
and `update()` methods of a realtime controller:


```cplusplus
#include <realtime_tools/realtime_publisher.h>

bool MyController::init(pr2_mechanism_model::RobotState *robot,
                        ros::NodeHandle &n)
{
  ...

  realtime_pub = new 
    realtime_tools::RealtimePublisher<mgs_type>(n, "topic", 4);
  return true;
}


void MyController::update()
{
  if (realtime_pub->trylock()){
    realtime_pub->msg_.a_field = "hallo";
    realtime_pub->msg_.header.stamp = ros::Time::now();
    realtime_pub->unlockAndPublish();
  }
  ...
}
```
