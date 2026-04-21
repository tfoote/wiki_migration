## Associated Hardware

-   Ocean Server: <http://www.ocean-server.com/overview.html>
-   IBPS specific documentation
    [IBPS Protocol](http://pr.willowgarage.com/wiki/IBPSBatteryInterface/IBPS_Protocol)
-   The Smart Battery Standard <attachment:sbdat110.pdf>

## Nodes

### ocean_server

`ocean_server` controls an array of battery controllers. The API below
is for informational purposes only; it is not intended for use by
anything other than [power_monitor](power_monitor), which is where you
should look for power data.

The `ocean_server` node will report the status of the batteries to
diagnostics. It will warn on the diagnostics if a battery does not
update within a timeout.

#### Advertised topics

```clearsilver
pub {
  no_header= True
  0.name= /diagnostics
  0.type= diagnostics_msgs/DiagnosticArray
  0.desc= Diagnostic information
  1.name= /battery/server2
  1.type= pr2_msgs/BatteryServer2
  1.desc= Battery data
  2.name= /battery/server
  2.type= pr2_msgs/BatteryServer
  2.desc= Battery data (DEPRECATED)
}
```

#### Parameters

```clearsilver
param {
  no_header= True
  0.name= ~number_of_ports
  0.type= int
  0.default= if no value specified on command-line, 4
  0.desc= Number of ports to monitor
  1.name= ~debug_level
  1.type= int
  1.default= if no value specified on command-line, 0
  1.desc= Debug level
  2.name= ~port<ID>
  2.type= string
  2.default= `"/dev/ttyUSB<ID>"`
  2.desc= Which device file is associated with the battery on port <ID>
  3.name= ~lag_timeout
  3.type= int
  3.default= `60`
  3.desc= Maximum time between battery messages before a battery reports a warning. Set to <0 to disable
  4.name= ~stale_timeout
  4.type= int
  4.default= `120`
  4.desc= Maximum time between battery messages before a battery reports an error. Set to <0 to disable
}
```
