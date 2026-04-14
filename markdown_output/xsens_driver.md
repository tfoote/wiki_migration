## Introduction

This package provides a driver for the third and fourth generation of
Xsens IMU devices. The driver is in two parts, a small implementation of
most of the MT protocol in Python and a [ROS node](#mtnode). It works
both on serial and USB interfaces.

These MT\* devices can store their configuration and will retrieve it at
each boot and then stream data according to this configuration. The node
only forwards the data streamed onto ROS topics. In order to configure
your device, you can use the [mtdevice.py](#mtdevice) script (or the
vendor tool on Windows).

Compared to the other MTi drivers ([lse_xsens_mti](lse_xsens_mti) and
[xsens_mti](xsens_mti)), this one can handle other configurations than
the default and the GPS module of the MTi-G. It is also a clean rewrite
of the communication protocol easier to maintain (and possibly extend)
than the old vendor based multi-layered architecture.

## mtnode.py

The ROS node is a wrapper around the \`mtdevice::MTDevice\` class to
publish the data that the IMU streams. It can publish the following
topics, depending on the configuration of the device (topics are only
advertised when there is data to publish): ```clearsilver
pub {
  0.name = imu/data
  0.type = sensor_msgs/Imu
  0.desc = orientation, angular velocity, and linear acceleration.
  1.name = fix
  1.type = sensor_msgs/NavSatFix
  1.desc = longitude, latitude, and altitude (from GPS, only for MTi-G)
  2.name = velocity
  2.type = geometry_msgs/TwistStamped
  2.desc = velocity information (linear only from GPS)
  3.name = imu/mag
  3.type = sensor_msgs/MagneticField
  3.desc = magnetic field information
  4.name = temperature
  4.type = sensor_msgs/Temperature
  4.desc = temperature of the sensor
  5.name = pressure
  5.type = sensor_msgs/FluidPressure
  5.desc = pressure information
  6.name = analog_in1
  6.type = std_msgs/UInt16
  6.desc = first analog input
  7.name = analog_in2
  7.type = std_msgs/UInt16
  7.desc = second analog input
  8.name = ecef
  8.type = geometry_msgs/PointStamped
  8.desc = ECEF position (only for device with GPS)
  9.name = time_reference
  9.type = sensor_msgs/TimeReference
  9.desc = time information form the device
  10.name = imu_data_str
  10.type = std_msgs/String
  10.desc = string version of all the data parsed from the IMU.
}
```

It also publishes [diagnostics](http://www.ros.org/wiki/diagnostics)
information.

If the IMU is set to raw mode, the values in of the \`/imu/data\`,
\`/velocity\` and \`/magnetic\` topics are the 16 bits output of the AD
converters.

The covariance information in the
[sensor_msgs::Imu](http://www.ros.org/doc/api/sensor_msgs/html/msg/Imu.html)
message are filled with default values from the MTx/MTi/MTi-G
documentation but may not be exact; it also does not correspond to the
covariance of the internal XKF.

```clearsilver
param {
  0.name = ~device
  0.type = string
  0.default = auto
  0.desc = the path of the device file to connect to the imu; `"auto"` will look through all serial devices to find the first one.
  1.name = ~baudrate
  1.type = int
  1.default = 0
  1.desc = the baudrate of the IMU (unused for `"auto"` device); `0` will try to auto-detect baudrate.
  2.name = ~timeout
  2.type = float
  2.default = 0.002
  2.desc = the timeout for the serial communication.
  3.name = ~frame_id
  3.type = string
  3.default = /base_imu
  3.desc = the frame id of the IMU.
  4.name = ~frame_local
  4.type = string
  4.default = ENU
  4.desc = the desired orientation of the `~frame_id` reference frame
}
```

## mtdevice.py

\`mtdevice.py\` is a Python module that is both a library to communicate
to devices through the \`MTDevice\` class, and a standalone script to
configure such a device. Note that you can use the module in an
interactive session to diagnose or configure the device with a bit more
flexibility.

/!\\ Changing the baudrate to values other than 115200 might not work
for some devices (despite mentioned in the vendor documentation) and
might require the emergency procedure to recover communication with the
device.

### Usage

```
Usage:
    ./mtdevice.py [commands] [opts]

Commands:
    -h, --help
        Print this help and quit.
    -r, --reset
        Reset device to factory defaults.
    -a, --change-baudrate=NEW_BAUD
        Change baudrate from BAUD (see below) to NEW_BAUD.
    -c, --configure=OUTPUT
        Configure the device (see OUTPUT description below).
    -e, --echo
        Print MTData. It is the default if no other command is supplied.
    -i, --inspect
        Print current MT device configuration.
    -x, --xkf-scenario=ID
        Change the current XKF scenario.
    -l, --legacy-configure
        Configure the device in legacy mode (needs MODE and SETTINGS arguments
        below).
    -v, --verbose
        Verbose output.

Generic options:
    -d, --device=DEV
        Serial interface of the device (default: /dev/ttyUSB0). If 'auto', then
        all serial ports are tested at all baudrates and the first
        suitable device is used.
    -b, --baudrate=BAUD
        Baudrate of serial interface (default: 115200). If 0, then all
        rates are tried until a suitable one is found.

Configuration option:
    OUTPUT
        The format is a sequence of "<group><type><frequency>?<format>?"
        separated by commas.
        The frequency and format are optional.
        The groups and types can be:
            t  temperature (max frequency: 1 Hz):
                tt  temperature
            i  timestamp (max frequency: 2000 Hz):
                iu  UTC time
                ip  packet counter
                ii  Integer Time of the Week (ITOW)
                if  sample time fine
                ic  sample time coarse
                ir  frame range
            o  orientation data (max frequency: 400 Hz):
                oq  quaternion
                om  rotation matrix
                oe  Euler angles
            b  pressure (max frequency: 50 Hz):
                bp  baro pressure
            a  acceleration (max frequency: 2000 Hz (see documentation)):
                ad  delta v
                aa  acceleration
                af  free acceleration
                ah  acceleration HR (max frequency 1000 Hz)
            p  position (max frequency: 400 Hz):
                pa  altitude ellipsoid
                pp  position ECEF
                pl  latitude longitude
            n  GNSS (max frequency: 4 Hz):
                np  GNSS PVT data
                ns  GNSS satellites info
            w  angular velocity (max frequency: 2000 Hz (see documentation)):
                wr  rate of turn
                wd  delta q
                wh  rate of turn HR (max frequency 1000 Hz)
            g  GPS (max frequency: 4 Hz):
                gd  DOP
                gs  SOL
                gu  time UTC
                gi  SV info
            r  Sensor Component Readout (max frequency: 2000 Hz):
                rr  ACC, GYR, MAG, temperature
                rt  Gyro temperatures
            m  Magnetic (max frequency: 100 Hz):
                mf  magnetic Field
            v  Velocity (max frequency: 400 Hz):
                vv  velocity XYZ
            s  Status (max frequency: 2000 Hz):
                sb  status byte
                sw  status word
        Frequency is specified in decimal and is assumed to be the maximum
        frequency if it is omitted.
        Format is a combination of the precision for real valued numbers and
        coordinate system:
            precision:
                f  single precision floating point number (32-bit) (default)
                d  double precision floating point number (64-bit)
            coordinate system:
                e  East-North-Up (default)
                n  North-East-Down
                w  North-West-Up
        Examples:
            The default configuration for the MTi-1/10/100 IMUs can be
            specified either as:
                "wd,ad,mf,ip,if,sw"
            or
                "wd2000fe,ad2000fe,mf100fe,ip2000,if2000,sw2000"
            For getting quaternion orientation in float with sample time:
                "oq400fw,if2000"
            For longitude, latitude, altitude and orientation (on MTi-G-700):
                "pl400fe,pa400fe,oq400fe"

Legacy options:
    -m, --output-mode=MODE
        Legacy mode of the device to select the information to output.
        This is required for 'legacy-configure' command.
        MODE can be either the mode value in hexadecimal, decimal or
        binary form, or a string composed of the following characters
        (in any order):
            t  temperature, [0x0001]
            c  calibrated data, [0x0002]
            o  orientation data, [0x0004]
            a  auxiliary data, [0x0008]
            p  position data (requires MTi-G), [0x0010]
            v  velocity data (requires MTi-G), [0x0020]
            s  status data, [0x0800]
            g  raw GPS mode (requires MTi-G), [0x1000]
            r  raw (incompatible with others except raw GPS), [0x4000]
        For example, use "--output-mode=so" to have status and
        orientation data.
    -s, --output-settings=SETTINGS
        Legacy settings of the device. This is required for 'legacy-configure'
        command.
        SETTINGS can be either the settings value in hexadecimal,
        decimal or binary form, or a string composed of the following
        characters (in any order):
            t  sample count (excludes 'n')
            n  no sample count (excludes 't')
            u  UTC time
            q  orientation in quaternion (excludes 'e' and 'm')
            e  orientation in Euler angles (excludes 'm' and 'q')
            m  orientation in matrix (excludes 'q' and 'e')
            A  acceleration in calibrated data
            G  rate of turn in calibrated data
            M  magnetic field in calibrated data
            i  only analog input 1 (excludes 'j')
            j  only analog input 2 (excludes 'i')
            N  North-East-Down instead of default: X North Z up
        For example, use "--output-settings=tqMAG" for all calibrated
        data, sample counter and orientation in quaternion.
    -p, --period=PERIOD
        Sampling period in (1/115200) seconds (default: 1152).
        Minimum is 225 (1.95 ms, 512 Hz), maximum is 1152
        (10.0 ms, 100 Hz).
        Note that for legacy devices it is the period at which sampling occurs,
        not the period at which messages are sent (see below).

Deprecated options:
    -f, --deprecated-skip-factor=SKIPFACTOR
        Only for mark III devices.
        Number of samples to skip before sending MTData message
        (default: 0).
        The frequency at which MTData message is send is:
            115200/(PERIOD * (SKIPFACTOR + 1))
        If the value is 0xffff, no data is send unless a ReqData request
        is made.
```

## Permissions

It might be necessary to add the user to the \`dialout\` group so that
the node can communicate with the device.
