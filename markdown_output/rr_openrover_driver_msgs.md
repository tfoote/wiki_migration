## Overview

This package contains the messages used to publish hardware data from
the OpenRover.

## RawRrOpenroverDriverFastRateData.msg



```
std_msgs/Header header
std_msgs/int32 left_motor
std_msgs/int32 right_motor
std_msgs/int32 flipper_motor
```



## RawRrOpenroverDriverMedRateData.msg



```
std_msgs/Header header
std_msgs/int32 reg_pwr_total_current
std_msgs/int32 reg_motor_fb_rpm_left
std_msgs/int32 reg_motor_fb_rpm_right
std_msgs/int32 reg_flipper_fb_position_pot1
std_msgs/int32 reg_flipper_fb_position_pot2
std_msgs/int32 reg_motor_fb_current_left
std_msgs/int32 reg_motor_fb_current_right
std_msgs/int32 reg_motor_charger_state
std_msgs/int32 reg_power_a_current
std_msgs/int32 reg_power_b_current
std_msgs/int32 reg_motor_flipper_angle
std_msgs/int16 battery_current_a
std_msgs/int16 battery_current_b
```



## RawRrOpenroverDriverMedRateData.msg



```
std_msgs/Header header
std_msgs/int32 reg_motor_fault_flag_left
std_msgs/int32 reg_motor_temp_left
std_msgs/int32 reg_motor_temp_right
std_msgs/int32 reg_power_bat_voltage_a
std_msgs/int32 reg_power_bat_voltage_b
std_msgs/int32 reg_robot_rel_soc_a
std_msgs/int32 reg_robot_rel_soc_b
std_msgs/uint16 battery_mode_a
std_msgs/uint16 battery_mode_b
std_msgs/uint16 battery_temp_a
std_msgs/uint16 battery_temp_b
std_msgs/uint16 battery_voltage_a
std_msgs/uint16 battery_voltage_b
std_msgs/int32 buildno
```



## RawRrOpenroverDriverMedRateData.msg



```
std_msgs/Header header

std_msgs/bool over_charged_alarm
std_msgs/bool terminate_charge_alarm
std_msgs/bool over_temp_alarm
std_msgs/bool terminate_discharge_alarm
std_msgs/bool remaining_capacity_alarm
std_msgs/bool remaining_time_alarm

std_msgs/bool initialized
std_msgs/bool discharging
std_msgs/bool fully_charged
std_msgs/bool fully_discharged
```


