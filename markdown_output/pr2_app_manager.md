Scripts for running the app_manager on the PR2.

## Software Installation

All of the following commands will be performed as SSH on the PR2 as PR2
admin. First, update and install all the requisite debs:



```
sudo apt-get update
sudo apt-get install ros-electric-pr2-apps ros-electric-wg-common ros-electric-multimaster-experimental ros-electric-pr2-props-stack
```



Second, make sure there is no existing applications user or related
stale files. Delete the user, group, and any existing home directory:



```
sudo userdel applications
sudo groupdel applications
sudo rm -rf /u/applications
sudo rm -rf /home/applications
```



Third, we are ready to install applications. Run:



```
roscd pr2_app_manager/scripts/
sudo ./install_applications.sh
```



During the install process, you will be prompted for the name of the
robot: 

```
Enter the robot name (e.g. pri):
```



The robot name refers to the identity of the robot. It is important that
it be the same as the robot's host name.

Note: version 0.4.5 and earlier had a bug causing the ssh keys of the
new "applications" user to not get set up correctly. If you are using
that version, or just want to be sure, run this:



```
sudo su applications
```



If you have the old version, you will be asked if you want to set up
your SSH keys. Answer "Y" for yes. You should see a random ASCII art
square. Then type `exit` to log back out of the "applications" user
account.

If you have the new version, you will not be asked anything, you will
just get a regular shell prompt. Type `exit` to log out of the
"applications" account.

Finally, after the script runs and completes successfully, run a test:


```
robot claim
robot start
roslaunch pr2_app_manager pr2_app_manager.launch
```



This should run without complaint. If there are error messages, it means
that something has likely gone wrong in the installation process. If
there are no error messages, you are ready to use the platform. You
probably wish to create a QR code first, however.

## Creating a QR Code

The QR codes for the PR2s are specified with a variety of attributes
stored in YAML to help connect to them. They are generated using
[the Zebra Crossing QR Code Generator](http://zxing.appspot.com/generator/).
To create the QR codes, use the "Text" mode, type in the text
(examples below) and click generate. When you are finished, you can
right click and save or print the QR code image. To avoid the hassle of
printing, many devices can read the QR code directly off of your PC
screen.

Most robot wifis are unsecured and can be run with a QR code similar to
the following one:



```
URL: http://pri1:11311/
CURL: http://pri1/cgi-bin/control.py
WIFI: priLAN
```



Obviously, the three instances of "pri" will have to be changed for
your specific robot.

Some robots have secured networks. They need an extra line:


```
WIFIPW: <then the wifi password>
```
