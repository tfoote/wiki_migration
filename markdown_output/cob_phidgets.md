## Hardware Check

After installation of the phidgets board execute following steps: 1.
login on the PC which is connected to the phidgets board 2. run
\"\'\'lsusb\'\'\" in the console 3. if you find something with phidgets
in the printed list follow step 6. 4. if not unplug and plug in the
phidgets board 5. run \"\'\'dmesg\'\'\" and look at the last lines (end)
6. start \'\'roscore\'\' 7. run \"\'\'relaunch cob_bringup
tray_sensors.launch\'\'\" 8. check output with \"\'\'rostopic echo
/tray_sensors/range_1\'\'\"

## Error Handling

If you get a message like \"operation not permitted\" you have probably
not the right to open the USB device. Therefore, add an udev rule with:

```
sudo echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="06c2", MODE="0666", GROUP="dialout"' >>  /etc/udev/rules.d/10-persistent-usb.rules && sudo chmod a+r /etc/udev/rules.d/10-persistent-usb.rules && sudo udevadm control --reload-rules
```

Make sure your user is in the group \"dialout\" with `groups`.
