## Usage

```
cd src/pan_tilt_robotis
 python pan_tilt.py -h
``` The output will be: ```
Usage: pan_tilt.py [options]

Options:
  -h, --help         show this help message and exit
  -d SERVO_DEV_NAME  servo device string. [default= /dev/robot/pan_tilt0]
  --pan_id=PAN_ID    id of the pan servo
  --tilt_id=TILT_ID  id of the tilt servo
  --pan=PAN          pan angle (degrees).
  --tilt=TILT        tilt angle (degrees).
```

The `pan_id` and `tilt_id` are the servo ids of the pan and tilt
Robotis servos.
