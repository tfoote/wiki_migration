![Bosch\|align="right",width=200](attachment:Bosch_SL-en_4C_S.png)\
\
\
\

## Install Arduino Firmware

Before using this package, the firmware of the Arduino must be updated.
The necessary code and a Makefile are included in the
`arduino_firmare` directory of the package.

### Install Arduino Development Environment

The Arduino development environment 1.0.1 or greater must be installed
before the firmware can be built. The `apt-get` package name is
"`arduino`". Note that for Ubuntu 12.04, the 1.0.1 version must be
installed from the backports repository.

### Building the Firmware

```
{#!wiki caution
'''I^2^C with External Pull-up Resistors'''

If you are using the I^2^C interface on the Arduino with external pull-up resistors, you must deactivate the Arduino's internal pull-ups on the SDA and SCL lines. By default, these pullups are enabled. To deactivate them, open the `Wire` library in the Arduino libraries folder (nominally `/usr/share/arduino/libraries`). In the `utilities` sub-folder, open the file `twi.c`, and comment out lines 70 and 71:
{{{
69 // activate internal pullups for twi.
70 // digitalWrite(SDA, 1);
71 // digitalWrite(SCL, 1);
``` }}}}

Open a terminal and change to the `arduino_firmware` directory. Set
the Arduino board type by setting an environment variable:
```
$ export BOARD=uno
``` Alternatively, the `Makefile` defualt on line
281 can be changed. To see supported boards type `make boards`.

Build the firmware by typing ```
$ make
``` There should be a
fair number of warnings, but no errors. The warnings are all in the
Arduino-supplied code.

### Uploading the Firmware

After the firmware is successfully built, upload it to the Arduino using
```
$ make upload
``` The Arduino is now ready for use with the
`arduino_interface` package.

The Makefile supports additional options, as described in the table
below:

  -- ------------------- -- ----------------------------------------------------------- --
     **Command**            **Description**                                             
     `make`               Build the firmware and display the size of the code         
     `make target`        Build the firmware                                          
     `make libs`          Build the Arduino libraries                                 
     `make clean`         Remove all build files and libraries                        
     `make size`          Determine the size of the copiled code                      
     `make upload`        Upload the firmware (`\*.hex`) to the Arduino             
     `make download`      Download the firmware from the Arduino to a `.hex` file   
     `make erase`         Erase the firmware on the Arduino                           
     `make boards`        List the different Arduino boards this makefile supports    
     `make monitor`       Run the serial monitor for talking to the Arduino           
  -- ------------------- -- ----------------------------------------------------------- --

## Using the Package
