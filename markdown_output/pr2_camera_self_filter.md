Contains launch files and scripts to run the camera_self_filter nodes on
a PR2 robot with an Nvidia graphics card in c2. This is highly
experimental! You may have to play around with the xorg.conf file once
the X-server is installed.

Instructions:

-   make /etc/ read-writeable on c2 by changing in /usr/sbin/c2init
    \'\'unionmount_ro etc\'\' to \'\'unionmount etc\'\'
-   install Xorg X-server: \'\'sudo apt-get install xserver-xorg\'\'
-   install NVidia-drivers
-   shutdown and plug in an
    [VGA-dummy adapter ](http://www.xtremesystems.org/forums/showthread.php?t=200444)
    to simulate a monitor
-   reboot, start robot and \'\'roslaunch pr2_camera_self_filter
    camera_self_filter.launch\'\'
