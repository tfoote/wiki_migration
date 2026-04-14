## Overview

ground_station is a GUI based on GTK+ allowing to display/update data
provided by some ROS topics. Given that the CityFlyer platform is a
quadrotor (i.e. Pelican built by Ascending Technologies GmbH -
<http://www.asctec.de>) we have developed several GTK+ widgets capable
of display telemetry data. These widgets are made to look like to real
flight instruments in order to allow easy feedbacks for the user/pilot.

For more details about these widgets and how to use them, check out the
doxygen documentation available in the Code API section.

## Usage

The ground station GUI can be started by running:
```shell
roslaunch ground_station ground_station.launch
```

The telemetry demo can be started by running: ```shell
roslaunch ground_station telemetry.launch
```

## Nodes

```clearsilver
node.0 {
name = groundstation
desc = The is the first version of the CityFlyer ground station. In this version, the GUI is devided into 3 tabs. The first one showing the telemtry widgets needed. The second tab is quite the same as [[gpsd_viewer]]. And the third tab provide an easy way to record bags.{{attachment:ground_station_telemetry.png}}{{attachment:ground_station_gps.png}}{{attachment:ground_station_rec.png}}
sub {
0{
name = /asctec/GPS_DATA
type = asctec_msgs/GPSData
desc = Basic GPS Data
}
1{
name = /asctec/IMU_CALCDATA
type = asctec_msgs/IMUCalcData
desc = Fused IMU Data, in asctec format
}
2{
name = /asctec/LL_STATUS
type = asctec_msgs/LLStatus
desc = Low Level Status including battery voltage
}
3{
name = /mav/imu
type = sensor_msgs/IMU
desc = IMU data
}
4{
name = /mav/pressure_height_filtered
type = mav_msgs/Height
desc = The height reported by the pressure sensor
}
5{
name = /fix
type = gps_common/GPSFix
desc = This topic is advertised by [[gpsd_client]].
}
}
param {
0.name = window_grayscale_color
0.type = bool
0.desc = Puts all widgets in grayscale color mode (e.g. outdoor use).
0.default = false
1.name = window_radial_color
1.type = bool
1.desc = Enable/Disable radial color layer on widgets; increases drawing performance.
1.default = true
2.name = altimeter_unit_is_feet
2.type = bool
2.desc = Sets the altimeter in meter or feet.
2.default = true
3.name = altimeter_step_value
3.type = int
3.desc = Define the step of the altimeter (e.g. 1,10 or 100 feet/meter).
3.default = 100
4.name = variometer_step_value
4.type = int
4.desc = Define the step of the variometer (e.g. 1,10 or 100 feet/meter).
4.default = 100
5.name = bg_widget_name
5.type = string
5.desc = Indicates the name of the bar gauge widget.
6.name = bg_bar_number
6.type = int
6.desc = Number of bag gauge you want in the widget.
6.default = 1
7.name = bg_name_bar_gauge1
7.type = string
7.desc = Indicates the name of bar 1.
8.name = bg_unit_bar_gauge1
8.type = string
8.desc = Indicates the unit of bar 1.
9.name = bg_start_value_bar_1
9.type = int
9.desc = Indicates the start value of bar 1.
9.default = 0
10.name = bg_end_value_bar_1
10.type = int
10.desc = Indicates the end value of bar 1.
10.default = 100
11.name = bg_name_bar_gauge2
11.type = string
11.desc = Indicates the name of bar 2.
12.name = bg_unit_bar_gauge2
12.type = string
12.desc = Indicates the unit of bar 2.
13.name = bg_start_value_bar_2
13.type = int
13.desc = Indicates the start value of bar 2.
13.default = 0
14.name = bg_end_value_bar_2
14.type = int
14.desc = Indicates the end value of bar 2.
14.default = 100
15.name = bg_name_bar_gauge3
15.type = string
15.desc = Indicates the name of bar 3.
16.name = bg_unit_bar_gauge3
16.type = string
16.desc = Indicates the unit of bar 3.
17.name = bg_start_value_bar_3
17.type = int
17.desc = Indicates the start value of bar 3.
17.default = 0
18.name = bg_end_value_bar_3
18.type = int
18.desc = Indicates the end value of bar 3.
18.default = 100
19.name = bg_name_bar_gauge4
19.type = string
19.desc = Indicates the name of bar 4.
20.name = bg_unit_bar_gauge4
20.type = string
20.desc = Indicates the unit of bar 4.
21.name = bg_start_value_bar_4
21.type = int
21.desc = Indicates the start value of bar 4.
21.default = 0
22.name = bg_end_value_bar_4
22.type = int
22.desc = Indicates the end value of bar 4.
22.default = 100
}
}
node.1 {
name = telemetry_demo
desc = This node show all the telemetry widgets in a simple GTK window and suscribe to an altitude message. It was only made for widgets demonstration. The widgets available are: altimeter, variometer, compass, gauge, bar gauges, artificial horizon and turn coordinator. {{attachment:telemetry_widgets.png}}
sub {
0.name = /fake_alti
0.type = geometry_msgs/Pose
0.desc = Suscribes to this topic for a testing purpose, altitude only (pose.z).
}
param {
0.name = window_grayscale_color
0.type = bool
0.desc = Puts all widgets in grayscale color mode (e.g. outdoor use).
0.default = false
1.name = window_radial_color
1.type = bool
1.desc = Enable/Disable radial color layer on widgets; increases drawing performance.
1.default = true
2.name = altimeter_unit_is_feet
2.type = bool
2.desc = Sets the altimeter in meter or feet.
2.default = true
3.name = altimeter_step_value
3.type = int
3.desc = Define the step of the altimeter (e.g. 1,10 or 100 feet/meter).
3.default = 100
4.name = variometer_step_value
4.type = int
4.desc = Define the step of the variometer (e.g. 1,10 or 100 feet/meter).
4.default = 100
5.name = gauge1_name
5.type = string
5.desc = Provide the name of gauge 1 (support pango text attribute).
6.name = gauge1_unit
6.type = string
6.desc = Provide the unit of gauge 1 (support pango text attribute).
7.name = gauge1_start_value
7.type = int
7.desc = Indicates the start value of the gauge 1.
7.default = 0
8.name = gauge1_end_value
8.type = string
8.desc = Indicates the end value of the gauge 1.
8.default = 100
9.name = gauge1_initial_step
9.type = int
9.desc = Fisrt step, divides the gauge 1 range into steps.
9.default = 10
10.name = gauge1_sub_step
10.type = string
10.desc = Sub step, divides the gauge 1 range into steps.
10.default = 1
11.name = gauge1_drawing_step
11.type = int
11.desc = Indicates the step where numbers will be drawn for gauge 1.
11.default = 10
12.name = gauge1_color_strip_order
12.type = string
12.desc = Allows to change the color strip order in gauge 1. By default it's YOR (Yellow Orange Red) - possible: GYR,RYG,ROY.
12.default = `"YOR"`
13.name = gauge1_green_strip_start
13.type = int
13.desc = Indicates the start of the green strip for gauge 1.
14.name = gauge1_yellow_strip_start
14.type = int
14.desc = Indicates the start of the yellow strip for gauge 1.
15.name = gauge1_red_strip_start
15.type = int
15.desc = Indicates the start of the red strip for gauge 1.
16.name = gauge1_green_strip_start
16.type = int
16.desc = Indicates the start of the green strip for gauge 1.
17.name = gauge2_name
17.type = string
17.desc = Provide the name of gauge 2 (support pango text attribute).
18.name = gauge2_unit
18.type = string
18.desc = Provide the unit of gauge 2 (support pango text attribute).
19.name = gauge2_start_value
19.type = int
19.desc = Indicates the start value of the gauge 2.
19.default = 0
20.name = gauge2_end_value
20.type = string
20.desc = Indicates the end value of the gauge 2.
20.default = 100
21.name = gauge2_initial_step
21.type = int
21.desc = Fisrt step, divides the gauge 2 range into steps.
21.default = 10
22.name = gauge2_sub_step
22.type = string
22.desc = Sub step, divides the gauge 2 range into steps.
22.default = 1
23.name = gauge2_drawing_step
23.type = int
23.desc = Indicates the step where numbers will be drawn for gauge 2.
23.default = 10
24.name = gauge2_color_strip_order
24.type = string
24.desc = Allows to change the color strip order in gauge 2. By default it's YOR (Yellow Orange Red) - possible: GYR,RYG,ROY.
24.default = `"YOR"`
25.name = gauge2_green_strip_start
25.type = int
25.desc = Indicates the start of the green strip for gauge 2.
26.name = gauge2_yellow_strip_start
26.type = int
26.desc = Indicates the start of the yellow strip for gauge 2.
27.name = gauge2_red_strip_start
27.type = int
27.desc = Indicates the start of the red strip for gauge 2.
28.name = gauge2_green_strip_start
28.type = int
28.desc = Indicates the start of the green strip for gauge 2.
29.name = bg_widget_name
29.type = string
29.desc = Indicates the name of the bar gauge widget.
30.name = bg_bar_number
30.type = int
30.desc = Number of bag gauge you want in the widget.
30.default = 1
31.name = bg_name_bar_gauge1
31.type = string
31.desc = Indicates the name of bar 1.
32.name = bg_unit_bar_gauge1
32.type = string
32.desc = Indicates the unit of bar 1.
33.name = bg_start_value_bar_1
33.type = int
33.desc = Indicates the start value of bar 1.
33.default = 0
34.name = bg_end_value_bar_1
34.type = int
34.desc = Indicates the end value of bar 1.
34.default = 100
35.name = bg_name_bar_gauge2
35.type = string
35.desc = Indicates the name of bar 2.
36.name = bg_unit_bar_gauge2
36.type = string
36.desc = Indicates the unit of bar 2.
37.name = bg_start_value_bar_2
37.type = int
37.desc = Indicates the start value of bar 2.
37.default = 0
38.name = bg_end_value_bar_2
38.type = int
38.desc = Indicates the end value of bar 2.
38.default = 100
39.name = bg_name_bar_gauge3
39.type = string
39.desc = Indicates the name of bar 3.
40.name = bg_unit_bar_gauge3
40.type = string
40.desc = Indicates the unit of bar 3.
41.name = bg_start_value_bar_3
41.type = int
41.desc = Indicates the start value of bar 3.
41.default = 0
42.name = bg_end_value_bar_3
42.type = int
42.desc = Indicates the end value of bar 3.
42.default = 100
43.name = bg_name_bar_gauge4
43.type = string
43.desc = Indicates the name of bar 4.
44.name = bg_unit_bar_gauge4
44.type = string
44.desc = Indicates the unit of bar 4.
45.name = bg_start_value_bar_4
45.type = int
45.desc = Indicates the start value of bar 4.
45.default = 0
46.name = bg_end_value_bar_4
46.type = int
46.desc = Indicates the end value of bar 4.
46.default = 100
```

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports.

Please use our [Trac](http://robotics.ccny.cuny.edu/trac/) to
[report bugs](http://robotics.ccny.cuny.edu/trac/newticket?component=asctec_drivers/asctec_autopilot&type=defect)
or
[request features](http://robotics.ccny.cuny.edu/trac/newticket?component=asctec_drivers/asctec_autopilot&type=enhancement).
