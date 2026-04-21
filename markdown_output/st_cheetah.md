# SynTouch Cheetah Package

------------------------------------------------------------------------

**`'This page is currently under development, please check back in the future for updates`**'

------------------------------------------------------------------------

Welcome to SynTouch's new ROS package **st_cheetah**. SynTouch is
currently developing this package to collect !BioTac data from the
Cheetah SPI/USB controller. Collected data can be processed using the
package [st_biotac](st_biotac).

For more information visit:
[SynTouch Website](http://www.syntouchllc.com)

------------------------------------------------------------------------

# st_cheetah

This package contains ROS Drivers for collecting !BioTac sensor data
from the Cheetah SPI Host controller
([Total Phase](http://www.totalphase.com/products/cheetah_spi/)) and
multi-!BioTac board. The contained node publishes raw data from the
attached !BioTacs and writes their properties to the parameter server.

-   Authors: Abhishek Pawar, Gary Lin, and Jeremy Fishel, contact:
    ros@syntouchllc.com
-   Maintained by: Abhishek Pawar / abhishek.pawar@syntouchllc.com
-   License: GPL
-   External Website: <http://www.syntouchllc.com>
-   Source: (software currently under development)

## Overview

```html
This package provides a ROS interface for the !BioTac sensors through the Cheetah SPI Port. The Cheetah device samples the connected !BioTacs according to the specified <a href="#Sampling Parameters">sampling parameters</a>. The !BioTac C library is included in this package to communicate with the sensors and decode the data. Each sample is then published as a new message that contains the channel identifier, sample data for each attached !BioTac, and a timestamp.
```

![hardware interface\|width=600](attachment:cheetah_hardware_interface.png)

**NOTE:** Do **not** Download the latest library from Total Phase. Our
software is only compatible with the version that is included in this
package.

```html
<a name="working"></a>
```

### BioTac Communication and Batch Structure

One or more BioTac sensors can be connected to the multi-BioTac board
and Cheetah SPI Host which is in turn connected to the computer via a
USB cable.

![software interface\|width=600](attachment:cheetah_software_interface.png)

The Cheetah SPI Host is capable of queueing *batches* of !BioTac SPI
sampling commands that execute asynchronously and are transmitted over
USB to the host computer when they become available. The !BioTac C
Library takes advantage of these asynchronous shifts to ensure
continuous sampling of !BioTac data even if USB communication is
delayed. During initialization, 16 batches of data are shifted to the
host adapter's queue as a buffer to ensure continuously sampled data.
Each time a batch is collected an identical batch of sampling commands
is added at the end of the queue. For this reason the minimum batch size
is one complete sampling sequence, or a *frame*. An integral multiple of
frames can be structured into a batch. Using more frames per batch is
efficient and reduces the USB bandwidth of the computer, which may be
necessary for slower computers; fewer frames per batch allows for faster
access to data, but may cause discontinuous sampling if the computer is
not fast enough to keep up. When this happens and the computer cannot
shift batches to the Cheetah SPI host faster than they are acquired it
is referred to as *buffer underrun* and indicates that the collected
!BioTac data is not continuous. When this happens, increasing the batch
length can solve the problem. Setting this value generally requires some
tuning, it is recommended that you start with a batch length of 30ms and
adjust either higher or lower depending on computer performance. Program
behavior in response to buffer underrun can be configured as indicated
below.

## ROS API

Rosgraph containing the nodes and topics

```clearsilver
node.0 {
  name=BioTac_Cheetah_Pub
  desc=This node finds all available Cheetah devices and references the configuration file to determine which device to communicate with (specified by serial number). Then it checks for available !BioTacs and retrieves their device information. After this configuration is complete it begins sampling and publishing a continuous stream of data.

pub {
  0.name = /biotacs/<port_name>
  0.type = st_biotac/BioTac_Port_Data
  0.desc = This topic contains !BioTac Data from all !BioTacs connected to the Cheetah port. The name of the topic depends on the parameter (~cheetah_port_name) as specified in the configuration file (default value is PORT0). For data structure refer to [[http://www.ros.org/wiki/st_biotac#msgs|BioTac Messages]].
}
```

#### Parameters

##### Cheetah Hardware Configuration parameters

![serial no\|width=300](attachment:cheetah_serial_no.png)

```clearsilver
param {
  no_header=True
  0.name = ~cheetah_serial_num
  0.default =`"0"`
  0.type = string
  0.desc = Serial number of the Cheetah device connected to the !BioTacs (with dashes). It can be found on the cheetah device as shown in the image above. If this value is set to 0 the first available Cheetah device is used. If this value is set to the particular device connected then connection to that device is established if it is found. For systems using more than one Cheetah this must be configured to avoid problems.
 
  1.name = ~cheetah_port_name
  1.default = `"PORT0"`
  1.type = string
  1.desc = The identifier of the cheetah device(i.e. left_hand). This parameter is used to specify the topic associated with this Cheetah.

}
```

```html
<a name="Sampling Parameters"></a>
```

##### Sampling Parameters

```clearsilver
param {
  no_header=True
  0.name = ~bt_sample_rate_hz
  0.default = 4400
  0.type = int
  0.desc = Sampling rate of the !BioTacs in Hz (maximum recommended rate is 20kHz). This is the overall sampling rate, sampling rate of each channel depends on frame structure (for the default frame structure, PAC sampling rate is 1/2 of the overall sampling rate, and all other channels are sampled at 1/44 of the overall sampling rate).

  1.name = ~bt_frame_type
  1.default = 0
  1.type = int
  1.desc = The sampling pattern for the !BioTac. They are hard coded in the program and can be identified by numbers as listed below:
}
``` ```html
<a name="frame types"></a>
```

-   0 - *Default Sampling Sequence* - Vibrations (P,,AC,,) signals are
    sampled at high frequency and interleaved with all other
    measurements. This is the recommended sampling sequence for most
    applications and is recommended to have an overall sampling rate of
    4400Hz.
-   Sequence (*44 Samples/frame*): P,,AC,,, E,,1,,, P,,AC,,, E,,2,,,
    \... P,,AC,,, E,,18,,, P,,AC,,, E,,19,,, P,,AC,,, P,,DC,,, P,,AC,,,
    T,,AC,,, P,,AC,,, T,,DC,,,

```{=html}
<!-- -->
```
-   1 - *Default with Hall* - This sampling sequence is for !BioTacs
    versions 2.3 and later with integrated Hall Sensor that require the
    sensing of this channel. The recommended sampling rate for this
    sequence is 4600Hz.
-   Sequence (*46 Samples/frame*): P,,AC,,, E,,1,,, P,,AC,,, E,,2,,,
    \... P,,AC,,, E,,18,,, P,,AC,,, E,,19,,, P,,AC,,, P,,DC,,, P,,AC,,,
    T,,AC,,, P,,AC,,, T,,DC,,, P,,AC,,, Hall

```{=html}
<!-- -->
```
-   2 - *All Channels* - This sampling sequence is recommended when high
    bandwidth vibration data is not necessary. It reduces the sampling
    rate of P,,AC,, to conserve bandwidth. Recommended sampling rate is
    2400Hz, however lower sampling rates can be used if desired. NOTE:
    when using this sampling sequence P,,AC,, is vulnerable to aliasing.
-   Sequence (*24 Samples/frame*): P,,AC,,, P,,DC,,, T,,AC,,, T,,DC,,,
    Hall, E,,1,,, E,,2,,, \... E,,18,,, E,,19,,,

```{=html}
<!-- -->
```
-   3 - *Electrodes Only* - This sampling sequence is recommended for
    force extraction algorithms that make use of the !BioTac electrodes,
    preferably for light forces. The recommended sampling rate is
    1900Hz.
-   Sequence (*19 Samples/frame*): E,,1,,, E,,2,,, \... E,,18,,,
    E,,19,,,

```{=html}
<!-- -->
```
-   4 - *AC/DC Pressure* - This sampling sequence is recommended for
    high-resolution sampling of vibration signals and contact, it
    alternates between the P,,AC,, and P,,DC,, channels. The recommended
    sampling rate is 4400Hz.
-   Sequence (*2 Samples/frame*): P,,AC,,, P,,DC,,,

```{=html}
<!-- -->
```
-   5 - *AC Pressure Only* - This sampling sequence is recommended for
    extremely low-noise vibration measurements. The recommended sampling
    rate is 2200Hz.
-   Sequence (*2 Samples/frame*): P,,AC,,, P,,DC,,,

##### Batch Parameters

```clearsilver
param {
  no_header=True
  0.name = ~bt_batch_ms
  0.default = 30
  0.type = int
  0.desc = The Cheetah SPI device asynchronously collects data and transmits multiple frames of data in batches over USB protocol to the host computer. Shorter batches allow for faster response by the host but can result in excessive USB traffic. In slower computers, this can result in breaks in the asynchronous sampling. If these problems are encountered, increasing the batch length (so more frames are transmitted in each batch communication) usually fixes the problem. The recommended batch length for most systems is 30ms.

  1.name = ~bt_buffer_underrun_option
  1.default = 0
  1.type = int
  1.desc = This parameter specifies how the !BioTac_Cheetah_Pub node will behave if the buffer in the Cheetah has underrun. The following parameters can be set:
}
```

-   0 - display warning and continue sampling
-   1 - display warning and reset sampling sequence before continuing
-   2 - Display error and terminate program (recommended for
    time-critical applications)```html
<p>For more details go <a href="#working">here</a>.
</p>
```

##### BioTac Properties

```clearsilver
param {
  no_header=True
  0.name = ~bt_status
  0.default = NULL
  0.type = bool[]
  0.desc = An array of boolean variables that indicate which connectors have !BioTacs attached (1=connected, 0=disconnected).

  1.name = ~bt_serial_num
  1.default = NULL
  1.type = string[]
  1.desc = An array containing the serial numbers of attached !BioTacs.

  2.name = ~bt_flex_ver
  2.default = NULL
  2.type = string[]
  2.desc = An array containing the flex circuit version of attached !BioTacs.

  3.name = ~bt_firmware_ver
  3.default = NULL
  3.type = string[]
  3.desc = An array containing the firmware version of attached !BioTacs.

  4.name = ~bt_cpu_speed
  4.default = NULL
  4.type = double[]
  4.desc = An array containing the CPU speed of attached !BioTacs in MHz.
}
```

##### Other Parameteres

```html
<a name="working"></a>
```0

## Documentation

The !BioTac_Cheetah_Pub node performs a number of error checking
operations to ensure hardware is properly configured and newly attached
or disconnected !BioTacs are identified. On each execution the node does
the following: 1. Checks if the specified Cheetah device is connected to
the host computer and displays warnings if not. 2. Checks if any
!BioTacs are connected and displays warnings if there are none. The
!BioTac information for each attached !BioTac is stored in global
parameters. 3. The publisher configures the Cheetah for asynchronous
sampling. 4. The publisher collects a batch from cheetah and publishes
samples. 5. If a !BioTac is disconnected or reconnected it updates the
parameters. If a new !BioTac is connected sampling is stopped to query
the !BioTac properties before restarting sampling.

## Installation Instructions

Download the SynTouch stack from (link). Unpack the package in a working
ROS directory. ```html
<a name="working"></a>
```1

Configure the launch file parameters. The minimum configuration is
specified below: ```html
<a name="working"></a>
```2

Or the extended configuration:

```html
<a name="working"></a>
```3

Run the launch file with: ```html
<a name="working"></a>
```4

## Contributing

If you are interested in contributing to the development of this stack
or would like to add or help us add new function to a package please
contact us at ros@syntouchllc.com

## Support

If you encounter a problem or need support please contact us at
ros@syntouchllc.com

------------------------------------------------------------------------
