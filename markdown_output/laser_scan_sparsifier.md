## Details

The [laser_scan_sparsifier](laser_scan_sparsifier) package is used to
downsample \<\<MsgLink(sensor_msgs/LaserScan)\>\> messages.

## Nodes & Nodelets

Two drivers are available: \`laser_scan_sparsifier_nodelet\` and
\`laser_scan_sparsifier_node\`. Their parameters and topics are
identical.

```clearsilver
 name = laser_scan_sparsifier_node / laser_scan_sparsifier_nodelet
 desc = The `laser_scan_sparsifier` takes in <<MsgLink(sensor_msgs/LaserScan)>> messages, and downsamples it by a given step size.
sub {
   0{
    name = scan
    type = sensor_msgs/LaserScan
    desc = Input scan
    }
  }
pub {
   0{
    name = scan_sparse
    type = sensor_msgs/LaserScan
    desc = Output scan
   }
  }
param{
    0.name = ~step
    0.type = int
    0.default = 2
    0.desc = Step size for decimation (must be > 0). A step size of 1 means the output scan will be the same as the input scan. A step size of 2 means the output scan will be half the input scan, etc.
}
```

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports and
feature requests.

Please submit your tickets through
[github](https://github.com/ccny-ros-pkg/scan_tools/issues/) (requires
github account) or by emailing the maintainers.
