Note: this package doesn't seem to have been updated in several years.
For a Catkinized Groovy-compatible fork, see
<https://github.com/danepowell/phantom_omni>

## Requirements

-   Phantom Omni device.
-   Open``Haptics SDK (download [here](http://dsc.sensable.com/))

## Running

### Installing the OpenHaptics SDK

The script install_open_haptics.sh is provided as a convenient way to
install the SDK. However, as of Ubuntu 10.10, this script no longer
works (see notes below), so it's recommended that you install the SDK
manually.

If you want to use the script anyway, place the downloaded SDK into the
`phantom_omni` package: 

```
mv OpenHapticsAE_Linux_v3_0.zip `rospack find phantom_omni`/
```

 Launch the
installation script: 

```
roscd phantom_omni
./install_open_haptics.sh
```



### Compiling and Starting

Make and run the `omni` node with: 

```
rosmake phantom_omni
rosrun phantom_omni omni
```



## Troubleshooting

-   **64-bit installation**: you will need to edit
    install_open_haptics.sh and replace instances of '32-bit' with
    '64-bit' and 'i386' with 'amd64' (someone should update this
    script so that the platform architecture is detected automatically).
    Additionally, you may get an error about missing libHD libraries
    when trying to run the omni node. I think this is because
    Open``Haptics oddly installs libraries to /usr/lib64. I think the
    best way to solve this is to create a file
    /etc/ld.so.conf.d/openhaptics.conf with the line '/usr/lib64' and
    then run ldconfig.
-   **Ubuntu versions 11.04 and later**: Ubuntu no longer uses raw1394,
    so you cannot use the Open``Haptics v3.0 drivers out of the box.
    Until v3.1 is released, you have two options: 1. (recommended)
    Replace the drivers with the unstable "JUJU" drivers that are
    available in the DSC forums. 2. Create a "dummy" raw1394 module
    according to this
    [HowTo article](https://wiki.sofa-framework.org/tdev/wiki/HowTo/SensableWithoutRaw1394).
    One consequence of this is that the set_permissions_1394.sh script
    will fail. Instead of using this script, follow the instructions at
    <http://superuser.com/a/239692> to permanently set permissions.

```{=html}
<!-- -->
```
-   **Drift**: the Omni's pose will drift from time to time, to correct
    for this restart the node with the stylus outside the calibration
    well, then place the stylus in when prompted.

```{=html}
<!-- -->
```
-   **Device not found **errors
-   This can happen if your Omni is not paired with your computer fix by
    running /usr/sbin/PHANToMConfiguration again.
-   You might not have access to /dev/raw1394 to fix execute
    set_permissions_1394.sh.

```{=html}
<!-- -->
```
-   **Using more than one device** on one Linux machine: currently, the
    Linux Omni driver is restricted to operating on only one device at a
    time. To use two devices (i.e. for controller a humanoid robot), you
    will need two different machines. It's a good thing that ROS is
    around : )

## ROS API



```clearsilver
name=omni
desc= In the below, replace OMNI_NAME with the appropriate value set for the parameter `~omni_name` (defaults to `omni1`)
pub {
   0.name = tf
   0.type = tf/tfMessage
   0.desc = `OMNI_NAME_link0`, `OMNI_NAME_link6`, and `OMNI_NAME_sensable` 

   1.name= OMNI_NAME_button
   1.type= phantom_omni/PhantomButtonEvent
   1.desc= State of the Phantom Omni's buttons.

   2.name= OMNI_NAME_pose
   2.type= geometry_msgs/PoseStamped
   2.desc= A static point representing the tip of the Omni end-effector.  Note that this point is being published in the frame defined by link6 so a TF will be needed to get the end-effector pose wrt to link0.
}
sub {
   0.name = OMNI_NAME_force_feedback
   0.type = geometry_msgs/Wrench
   0.desc = A wrench in the `OMNI_NAME_sensable` frame to play back on the Omni.
}
param {
   0.name=~omni_name
   0.type=string
   0.default=omni1
   0.desc=Name for this omni device.
```


