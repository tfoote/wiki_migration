## Basic Example

Timing some code: ```
rtcus_timing::Timer timer;
  //anonymous chunk
  timer.start();
  ros::Duration(1.0).sleep();
  timer.stop();

  timer.start("second_chunk");
  ros::Duration(2.0).sleep();
  ros::Duration duration = timer.stop("second_chunk");
  ROS_INFO("duration of the second chunk: %lf",duration.toSec());

  timer.start("third_chunk");
  ros::Duration(3.0).sleep();
  timer.stop("third_chunk");

  timer.publish_data();
  ros::Duration(5.0).sleep();
```

See the console output result: ```
[ INFO] [1340637966.153541042]: duration of the second chunk: 2.000209
```

Watch the timing topic messages ```
$ rostopic echo timing

event_name: default
start_time: 
  secs: 1340637963
  nsecs: 152958238
end_time: 
  secs: 1340637964
  nsecs: 153118715
duration: 
  secs: 1
  nsecs: 160477
---
event_name: second_chunk
start_time: 
  secs: 1340637964
  nsecs: 153136043
end_time: 
  secs: 1340637966
  nsecs: 153345372
duration: 
  secs: 2
  nsecs: 209329
---
event_name: third_chunk
start_time: 
  secs: 1340637966
  nsecs: 153664930
end_time: 
  secs: 1340637969
  nsecs: 153811438
duration: 
  secs: 3
  nsecs: 146508
---
```
