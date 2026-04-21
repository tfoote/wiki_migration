![](attachment:asctec_mon.jpg)

## Usage

This package provides a curses based console groundstation for use with
the
[AscTec AutoPilot](http://www.asctec.de/asctec-hummingbird-autopilot/)

## Details

Pressing 'q' will quit the program and pressing 'r' will begin
recording a bag file. Pressing 'r' again will cause recording to stop.

## Known Bugs

The terminal needs to be a little larger than 80x24 to display correctly
Requires a /ros/bags directory to record bags.

This code is a stopgap solution while our
[ground station](ccny_ground_station) is under development. It should
not be considered production quality or even usable.

## Example

The monitor can be started by running:

```shell
roslaunch asctec_mon monitor.launch
```

## Nodes

To be added\...

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports.

Please use our [Trac](http://robotics.ccny.cuny.edu/trac/) to
[report bugs](http://robotics.ccny.cuny.edu/trac/newticket?component=asctec_drivers/asctec_autopilot&type=defect)
or
[request features](http://robotics.ccny.cuny.edu/trac/newticket?component=asctec_drivers/asctec_autopilot&type=enhancement).
