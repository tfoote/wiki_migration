![Bosch\|align="right",width=200](attachment:Bosch_SL-en_4C_S.png)\
\
\
\

![](attachment:bmp085_photo.jpg)

The BMP085 is a high-precision, ultra-low power barometric pressure
sensor for use in advanced mobile applications. With a range of 300 hPa
to 1100 hPa, an absolute accuracy of 2.5 hPa, and a noise level of down
to 0.03 hPa (which is equivalent to an altitude change of merely 0.25 m)
the BMP085 offers superior performance.

## Supported Hardware

This package supports
[BMP085 and SMD500](http://www.bosch-sensortec.com/content/language1/html/3477.htm)
pressure sensors from Bosch Sensortec.

## Hardware Setup

The BMP085 comes as a fully-calibrated, ready-to-use sensor module
without the need for additional external circuitry. Pressure and
temperature data are provided as 16-bit values via the I\^2\^C
interface, together with calibration data for temperature compensation.
Details on device pinout and electrical characteristics can be found in
the
[BMP085 datasheet](http://www.bosch-sensortec.com/content/language1/downloads/BST-BMP085-DS000-06.pdf)

ROS communication with the BMP085 is achieved through an external
hardware interface. This package includes example code demonstrating how
the sensor can be used with hardware interfaces such as the
[Xdimax SUB-20](http://www.xdimax.com/sub20/sub20.html),
[Arduino Uno](http://arduino.cc/en/Main/ArduinoBoardUno), and
[gumstix Overo](http://www.gumstix.com/). Please see
[HardwareInterface](HardwareInterface) for instructions on setting up
the hardware interfaces to work with this ROS package.

## ROS API/Nodes

The ROS API is currently undergoing additional development.



```clearsilver
node.0{
name = bmp085_w_sub20
desc = The `bmp085_w_sub20` interfaces with Bosch Sensortec BMP085 barometric pressure sensor. The driver requires a [[http://www.xdimax.com/sub20/sub20.html|Sub20]] to communicate with the I^2^C interface of the BMP085. 

param {
  0.name = max_acc_g 
  0.default = `16`
  0.type = double
  0.desc = maximum measurable acceleration in g 
  1.name = bandwidth_Hz
  1.default =`300`
  1.type = double
  1.desc = sensor filter bandwidth 
}
pub {
  0.name = bmp085_measurement
  0.type = bmp085/bmp085_measurement
  0.desc = time, connection status, temperature data [C], and air pressure [kPa]
}
```



## Tools

## External Links

-   [BMP085 Flyer](http://www.bosch-sensortec.com/content/language1/downloads/BMP085_Flyer_Rev.0.2_March2008.pdf)
-   [BMP085 datasheet](http://www.bosch-sensortec.com/content/language1/downloads/BST-BMP085-DS000-06.pdf)
-   [Bosch Sensortec MEMS pressure sensors](http://www.bosch-sensortec.com/content/language1/html/3477.htm)
-   [Xdimax SUB-20 Device](http://www.xdimax.com/sub20/sub20.html)
-   [Arduino Uno](http://arduino.cc/en/Main/ArduinoBoardUno)
-   [gumstix](http://www.gumstix.com/)
