## Tools

\`ectools\` contains a utility for recording dropped packers over a
loopback link.

```clearsilver
name = ecstats
desc = Counts dropped packets over loopback link
pub {
  0.name = ecstats
  0.type = ectools/ecstats
  0.desc = Link status
}
```

#### Command Line Usage

```
usage: bin/ecstats [-i <interface>] [-s <size>] [-d <delay>] [-l <preload>] [-v]
Measures Ethernet bandwidth and packet loss.  Also, counts number of EtherCAT devices.
Publishes results on 'ecstats' topic.
  -i : network interface to use when communicating with EtherCAT MCBs
  -s : <size> of packet to send.  Defaults to 1400
  -j : number of threads to run.  Defaults to 8
  -v : increase verbosity
  -h : display this help
```

This node generates data that is listened by the
[pr2_hardware_test_monitor](pr2_hardware_test_monitor). It is used in
the WG hardware test system to monitor slip rings.
