ISOGenerator is a set of scripts for the creation of ROS live cds, live
USB keys, and related installers. The scripts are used by the Hudson job
[ros-live-iso-generator](http://build.willowgarage.com/job/ros-live-iso-generator/)
to create ISO files. These ISO files are then stored where they can be
downloaded or published. These ISO files must be installed on media with
the Ubuntu startup disk creator.

## Customization Process

The system customizes an ISO in a set of steps: 1. Unpacking the Linux
ISO 1. Running a customization script chrooted to the ISO 1. Removing
temporary files on the ISO 1. Adding a hook so that ubiquity will run
the clean up script 1. Packing the ISO 1. Deleting temporary files

The scripts that perform these steps are found in
isogenerator/livecd_scripts. The extract_and_patch.sh script automates
the entire process.

The customization scripts generally perform the following steps: 1.
Adding the ROS repos and updating apt 1. Installing the desired ROS
packages 1. Adding the desktop shortcut 1. Adding the post-install
script to clean up files 1. Adding special drivers and configuration
files

The scripts that perform these steps are found in
isogenerator/livecd_modification_scripts.

## Using the ros-live-iso-generator Hudson Job

The ros-live-iso-generator Hudson Job is used to automatically create a
desired USB key with the appropriate files. 1. Go to the
[hudson page](http://build.willowgarage.com/job/ros-live-iso-generator/build?delay=0sec)
and log in 1. Choose the desired CUSTOMIZATION_SCRIPT 1. Choose the
desired architecture. Note that currently, only amd64 is supported 1.
Click the \"Build\" button 1. Click the first item in the list of builds
(it should be flashing) 1. Wait until the build finishes (approximately
10 minutes) 1. Click the \"Console Output\" link 1. Find the line that
says \"Storing at:\". It should be near the end of the output 1. Use
either ssh or http to copy the file to your computer. If using http, the
url is in the form of
pub1.willowgarage.com/hudson_logs/\[SCRIPT_NAME\]-\[ARCHITECTURE\].iso 1.
You are now ready to install the generated ISO

## Customizing an ISO Locally

In general you, should use the hudson job for customizing ISO files.
However, if you are testing or creating a livecd modification script,
customizing locally can be easier then using hudson.

First, extract the cd: 1. Do a local checkout of the isogenerator
stack 1. Add the isogenerator/livecd_scripts directory to your PATH 1.
Download the desired linux ISO. The isogenerator has only been tested
with Ubuntu ISOs, so use others at your own risk 1. Create a working
directory for the extracted ISO 1. cd to the working directory 1. Run
extract_cd.sh with the linux ISO file as its argument

To run a modification script: 1. Ensure you are in the working
directory 1. Run sudo \`which edit_cd.sh\` with the modification script
as its argument

To open a terminal inside the cd: 1. Ensure you are in the working
directory 1. Run sudo \`which edit_cd.sh\` without any arguments 1. You
are now in a terminal chrooted to the livecd and can begin typing
commands 1. Exit the terminal by typing control-D or exit. Do not close
the terminal window or kill the process through other means

To create a new ISO: 1. Ensure you are in the working directory 1. Run
create_iso.sh with the file name for the new ISO as its argument 1. Run
sudo \`which clean_cd.sh\` to clean up the temporary directories. You
will need to add \"yes\" as its argument 1. You are now ready to install
the generated ISO

## Creating a Customization Script

Creating a customization script is the best way to edit the livecd. The
scripts run a set of commands on the livecd inside the chroot. This
requires commit access to the rosrelease repository and the ability to
edit jobs in hudson

1\. Do a local checkout of the isogenerator stack 1. Create a new script
inside of isogenerator/livecd_modification_scripts called
\[your-script\].sh where \[your-script\] is the script name. You may
want to copy ros_live.sh as a template 1. Edit the script as desired 1.
Run the script locally as described above for testing purposes 1. Check
in the script 1. Log in to the
[hudson configuration page](http://build.willowgarage.com/job/ros-live-iso-generator/configure) 1.
Add \[your-script\] to the list of choices for CUSTOMIZATION_SCRIPT. Add
it as a new line in the list 1. Scroll down and click save 1. You are
now ready to run the hudson job

## Using a Generated ISO

To use a generated ISO, you will need a USB key that is bigger than the
file and a computer running Ubuntu. All files on the USB key will be
erased.

1\. Locate the ISO on your computer 1. Plug the USB key into the
computer 1. Open the Ubuntu Startup Disk Creator by choosing System -\>
Administration -\> Startup Disk Creator 1. Choose the disk in the lower
list and click \"Erase Disk\" 1. Wait for the disk to be erased 1.
Ensure that the disk is still clicked in the lower list 1. Click
\"Other\...\" below the list of ISO files 1. Choose your ISO file in the
file chooser 1. Click \"Make Startup Disk\" 1. Wait until the copying
process is finished 1. Close the Startup Disk Creator 1. Eject the USB
Disk by right clicking it on the desktop and choosing Eject 1. Remove
the USB Disk from the computer

\'\'\'If you are asked for your root password:\'\'\' sometimes Ubuntu
will ask for your root password instead of doing a \"sudo\" when you
launch Startup Disk Creator from the GUI. If you have this problem,
close the Startup Disk Creator and start a terminal (Applications -\>
Accessories -\> Terminal). Type the following in the terminal and go
back to step 5:

```
sudo usb-creator-gtk
```
