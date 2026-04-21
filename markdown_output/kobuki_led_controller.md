## Overview

Python library to control [kobuki](kobuki) LEDs.

## Usage

This is example script to demonstrate usage.



```highlight
import kobuki_led_controller

rospy.init_node('Hello')

blinker = kobuki_led_controller.LedBlinker()
rospy.loginfo("Blinker : blinker start")
blinker.start() # Starts Led blinker thread.

rospy.loginfo("Blinker : blinks red")
blinker.set_on_error() # Blinks Red LED
rospy.sleep(3.0)

rospy.loginfo("Blinker : blinks Green")
blinker.set_on_ok()    # blinks Green LED
rospy.sleep(3.0)

rospy.loginfo("Blinker : stop blinking")
blinker.set_on_off()   # stop blinking

rospy.loginfo("Blinker : blinker stops")
blinker.stop()         # stops led blinkder thread.
```


