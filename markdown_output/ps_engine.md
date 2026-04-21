## Installation

Please see the [ni](ni) page for installation instructions.

## Documentation

This package tracks the
[PrimeSense Sensor project](https://github.com/PrimeSense/Sensor) on
!GitHub, which is an OpenNI-compliant driver for the !PrimeSense RGB-D
sensor. Our version includes patches to support the Kinect.

Please see [OpenNI.org](http://openni.org) for more information about
OpenNI.

## Kinect compatibility

This wrapper is intended to be compatible with both the
[PSDK5.0 device](http://www.primesense.com/?p=1132) and Kinect, though
this is a work in progress. In order to use `ps_engine` with the
Kinect, you will need to set two environment variables. We recommend
adding the following to your `.bashrc`:



```
export XN_SENSOR_VENDOR_ID=0x045E 
export XN_SENSOR_PRODUCT_ID=0x02AE
export XN_HOST_PROTOCOL_ALGORITHM_REGISTRATION=0x40
```


