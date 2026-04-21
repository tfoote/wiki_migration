## Overview

This package allows you to store data easily in shared memory segments.
All variables stored in the shared memory are labeled and identified
with a name of your choice. You can also trigger signals for subscribed
processes on your shared variables instead of polling for changes.

### No Nodelets needed

Nodelets are not required and you have to rethink your communication.

### Interprocess communication

Using ak_shm also allows you to communicate with other
programs/processes on the same computer in a very efficient way.

### Tools

The package includes a program to simply access variables stored in the
shared memory

#### shmadmin

The program shmadmin is able to read and write variables and vectors of
common types. It is also able to set and release locks on variables
```shell
rosrun ak_shm shmadmin -h
Allowed Parameters:
  --help                get this help message
  -a [ --all ]          lists all shared variables
  -c [ --clear ]        clears shared memory
  -f [ --force ]        forces action write and ...
  -n [ --segment ] arg  shared memory segment
  -l [ --list ] arg     lists named variables
  -t [ --testlock ] arg tests locks
  -u [ --unlock ] arg   unlocks variables
  -k [ --lock ] arg     locks variables
  -s [ --signal ] arg   signals a change of a named variable
  -r [ --read ] arg     reads content of a named variable
  -w [ --write ] arg    [value] writes a value to shared variables
                        example:  -w Var "3:0 1.03  4 0 4, 4" writes a six 
                        channels vector/array six values at index 3
```

#### shmimageviewer

This program displays images stored in the shared memory
```shell
rosrun ak_shm shmimageview -h
Allowed Parameters:
  --help                 get this help message
  -s [ --simgleshot ]    shared rgb image
  -u [ --drawOnChange ]  updates only on change
  -n [ --segment ] arg   shared memory segment
  -g [ --gray ] arg      shared gray image
  -r [ --rgb ] arg       shared rgb image
  -b [ --bgr ] arg       shared bgr image
  -y [ --yuyv ] arg      shared yuyv image
```

## Examples

Various examples are provided to show how you can use the shared memory
for interprocess communication.

### usb_cam_to_shm.launch: copies a image into the shared memory and back

This example publishes images using the usb_cam package and copies the
image into the shared memory using the *image2shm* note. The
*shmimageviewer* is able to draw images stored in the shared memory and
the *shm2image* note pipes the image back to a rostopic.
```shell
rosmake usb_cam ak_shm 
rosrun ak_shm shmadmin -c # clears the shared memory
roslaunch ak_shm usb_cam_to_shm.launch
```

### Creating variables

This example shows you how you can create, read and write common shared
variables and how you can create a shared vector of your own type/class.
You should run the example multiple times to see the effect. You can
also see how to access variables on a secure concurrent way.
```shell
rosmake ak_shm
rosrun ak_shm shmadmin -c # clears the shared memory
rosrun ak_shm example00
```

### Locking variables, waiting for changes and signals

This example shows you how you lock variables and how you trigger
signals. ```shell
rosrun ak_shm shmadmin -c # clears the shared memory
rosrun ak_shm example01
``` After you run the example01 you can
use the **shmadmin** to view the variables. ```shell
rosrun ak_shm shmadmin -a # -a lists all shared variables
rosrun ak_shm shmadmin -u MyPoint3D # -a Unlocks variables
```

### Timed wait and signals

This example shows you how you lock variables and how you trigger
changes. ```shell
rosrun ak_shm shmadmin -c # clears the shared memory
rosrun ak_shm example02
```

### Shared images and opencv image processing

This example shows how you create a shared image and how you can view it
with the **shmimageviewer**. ```shell
rosrun ak_shm shmadmin -c # clears the shared memory
# opens a image and porcesses a canny image
rosrun ak_shm example03 [path to a color image] 
# shows the source image form the shm
rosrun ak_shm shmimageview --bgr ImgSrc 
# shows a gray image 
rosrun ak_shm shmimageview --gray ImgCanny  
# shows a multiple images in a false color format 
rosrun ak_shm shmimageview --rgb ImgSrc --gray ImgCanny
```

## System installation

If you want the library to be available outside of ros you can run *make
install* in your build folder ```shell
roscd ak_shm
cd build
make install # with sudo
```

### System uninstall

```shell
rm -rf /usr/include/akshm  # with sudo
rm $HOME/bin/shmimageview $HOME/bin/shmadmin
```

## Nodes

```shell
rosrun ak_shm shmimageview -h
Allowed Parameters:
  --help                 get this help message
  -s [ --simgleshot ]    shared rgb image
  -u [ --drawOnChange ]  updates only on change
  -n [ --segment ] arg   shared memory segment
  -g [ --gray ] arg      shared gray image
  -r [ --rgb ] arg       shared rgb image
  -b [ --bgr ] arg       shared bgr image
  -y [ --yuyv ] arg      shared yuyv image
```0
