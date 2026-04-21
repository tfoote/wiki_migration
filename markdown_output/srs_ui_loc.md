## INSTALL

This shows how to install srs ui loc (srs_ui_loc). 1. Allow installing
apps from unknown sources: Settings-\>Applications-\>Unknown
sources-\>check 2. Copy srs_ui_loc.apk onto the device (Samsung Galaxy
SII) 3. Install it by opening it

## CONFIGURATION

After installing the apk file, you will find a new app called \"SRS\" in
your apps list. Start the app and follow these instructions to configure
it correctly:

-   Touch the \"Settings\" button
-   Type in the hostname of the computer running the ROS server (e.g.
    \"cob3-3-pc1\")
-   Type in the apartment name (e.g. \"ipa-kitchen\")
-   Type in the skype user name for the UI_LOC user
-   Type in the skype user password for the UI_LOC user
-   Type in the skype user name used for emergency calls
-   Touch the \"Edit etc/hosts file\" button
-   add/change entries as necessary (format for each line: \"ip-address
    hostname\", e.g. \"192.168.0.101 cob3-3-pc1\")
-   Touch \"Save\" button
-   Touch \"Save Settings\" button

Note1: You need to scroll on the Settings screen in order to reach all
parts of it.\
Note2: Type in all necessary configuration data without quotes.

## Usage/Examples

1\. Start [srs_scenarios](srs_scenarios) on the computer with the
hostname you have configured in Settings 2. On the same computer, start
[srs_mixed_reality_server](srs_mixed_reality_server) 2. Start SRS app on
device 3. Change settings if needed as described above 4. Touch \"SRS\"
button to start UI_LOC 5. Use buttons provided by UI_LOC to navigate
through UI_LOC (soft phone buttons are deactivated)

Note1: The first time you start UI_LOC, there won\'t be any contacts to
call. To change that, you need to restart UI_LOC: in the Main menu (two
grey, one red button) open the android menu, choose \"Exit\" and then
touch the \"SRS\" button again.\

Note2: A contact photo is transmitted during the first call to that
contact. However, it won\'t be displayed before restarting UI_LOC.
Therefore, in order to have all contact photos, one needs to call all
contacts (only ringing them does not work) and then restart UI_LOC. The
contact photos will be saved permanently.

## Other

To read the phone log or to debug the application (with adb or eclipse),
one needs to activate USB debugging:
Settings-\>Applications-\>Development-\>USB debugging-\>check.\

UI_LOC has been tested on several devices:

  -- ---------------------- -- ------------------- -- ---------- -- ------------------------------------------- --
     *Device name*             *Android version*      *rooted*      *supported*                                 
     Samsung Galaxy SII        2.3.5                  yes           full support                                
     easypix Easypad 1370      2.3.1                  no            full support                                
     HTC Sense 3.0             2.3.5                  no            full support                                
     Huawei G300               2.3.6                  no            no support at all                           
     HTC Sense 3.6             4.0                    yes           skype and editing etc/hosts does not work   
  -- ---------------------- -- ------------------- -- ---------- -- ------------------------------------------- --
