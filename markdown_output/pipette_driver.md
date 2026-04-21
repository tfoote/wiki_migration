# Introduction

The pipette_driver package allows control and communication with Viaflo
Vision Pipette over a bluetooth link. The package contains:

-   The `pipette` python package (library) that allows access to
    pipette.
-   `pipette_node` provide a ROS service interface to pipette and
    diagnostics.
-   `purge`, `aspirate`, and `dispense` scripts that make simple service
    calls to `pipette_node`

# Tutorial: using the pipette with a PR2

This tutorial describes how to use the ViaFlo Vision pipette with a PR2,
but should be instructive for other setups as well.

## Put Pipette in Bluetooth mode

1\. Use back `<-` button on pipette to get into \'Main Menu\'. 1. Scroll
to bottom of menu and select \'Toolbox\' option 1. In \'Toolbox\' menu,
select \'Communications\' option 1. In \'Communications\' menu, scroll
to \'Bluetooth\' and select to enter bluetooth mode.

### Local computer setup

Get bluetooth tools ```
sudo apt-get install bluez
```

Plugin bluetooth adapter\...

### PR2 setup

The PR2 already has a bluetooth adapter. However, the adapter is
connected to the second computer (c2). For the rest of the tutorial you
should run commands from c2.

Log into second computer on PRI: ```
ssh pri2
```

## Determine bluetooth address of pipette

Make sure bluetooth adapter was found and is running:
```
hciconfig
``` You should see something like
```
hci0:	Type: USB
	BD Address: 00:1B:DC:00:04:81 ACL MTU: 310:10 SCO MTU: 64:8
	UP RUNNING PSCAN 
	RX bytes:367492 acl:10576 sco:0 events:9367 errors:0
	TX bytes:124782 acl:6401 sco:0 commands:1120 errors:0
``` If **UP** is not present then run:
```
sudo hciconfig hci0 up
```

Now scan for bluetooth devices (this may take 30+ seconds):
```
hcitool scan
``` The output might look like something like
```
Scanning ...
	00:80:98:E6:2B:30	Ezurio blu2i E62B30
	00:80:98:EB:96:BA	WINXPHOME-DK
```

The **Ezurio blu2i E62B30** is the pipette. You will want to remember
the bluetooth device address **00:80:98:EB:96:BA** for later.

## Starting pipette_node

Compile ```
rosmake pipette_driver
```

The pipette node need to be told what the address for the bluetooth
pipette that was determined in the previous step.
```
rosrun pipette_driver pipette_node.py -a 00:80:98:E6:2B:30
```

## Run make service calls using scripts

Once the pipette node is running, there are some scripts that can be use
to make service calls.

Flush contents of pipette ```
rosrun pipette_driver purge
```

Suck up 200uL of fluid ```
ssh pri2
```0

Spit out 100uL of fluid ```
ssh pri2
```1

## Using diagnostics

The pipette node provide some output to the diagnosics topic. You can
use the the runtime monitor (or pr2_dashboard on robot) to view this
data. ```
ssh pri2
```2

![](attachment:pipette-diagnostics.png)

When using the PR2 and dashboard, the pipette diagnostics will be put in
the \"Other\" category

![](attachment:pipette-diagnostics-dashboard.png)
