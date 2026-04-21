## tf_tools

### tf_logger

tf_logger will record the changes of frames published through [tf](tf)
each with respect to a given reference frame.

#### Usage

```
$ rosrun tf_tools tf_logger FREQUENCY REF_FRAME LOG_FRAME [REF_FRAME LOG_FRAME ...]
``` E.g. if you want to log both the transforms
/world -> /odom and /odom -> /base_link at a frequency of 5 Hz, run

```
$ rosrun tf_tools tf_logger 5 /world /odom /odom /base_link
``` You can log as many transformations as you
wish.
