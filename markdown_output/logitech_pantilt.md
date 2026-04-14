## Camera Initialization

The camera must be initialized before pan/tilt can be used.
mjpg_streamer (available from
<http://sourceforge.net/projects/mjpg-streamer>) can perform this
initialization. Create a shell script containing the following:
```/usr/bin/env
#init_camera.sh
export MJPG_ROOT=/usr/local
export LD_LIBRARY_PATH=$MJPG_ROOT/lib
$MJPG_ROOT/bin/mjpg_streamer -i "input_control.so -d /dev/video0" -o "output_http.so -w /usr/local/www -p 8081"&
sleep 2
killall mjpg_streamer
``` Add execute permissions:
```
chmod +x init_camera.sh
``` Run the script as root ```
sudo ./init_camera.sh
```
You can perform this initialization at boot-time by adding a link to
init_cam.sh in /etc/rc.local.
