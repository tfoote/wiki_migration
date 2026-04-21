/!\\ The following doc might be significantly outdated. Please consider
contributing to update it.

## Installation

First build the library with 

```
rosdep install libphidgets
rosmake libphidgets
```

 Afternwards
install the module with 

```
roscd libphidgets
sudo ./install_phidgets.sh
```



After this procedure the driver is installed for your system (and your
kernel so you have to repeat the procedure once your kernel has
changed). After restart the driver will be activated automatically.
