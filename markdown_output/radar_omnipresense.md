## Documentation

Please see the individual packages within this stack for documentation.
OPS241/OPS242 radar sensors can be purchased from
[OmniPreSense](https://www.omnipresense.com/shop/). The full API
Interface documentation (AN-10) is available at
<https://omnipresense.com/applications/>.

radar_omnipresense , a ROS module for the OmniPreSense radar sensor

## Devices Supported

The packages supports the OPS241, OPS242, and OPS243 radar sensors. The
OPS241 is a development kit with more flexible firmware operation while
the OPS242 (Doppler) and OPS243-A (Doppler) carry full FCC/CE modular
regulatory approval. The OPS243-C provides both range and speed
information and is also supported.

## Installation

The radar_omipresense driver is built automatically by the ROS build
farm. Subsequently, the standard way of installing drivers works for the
radar omnipresense driver. Namely, apt install
ros-\'\'distro\'\'-radar-omnipresense. So, for example, if you are
running with ROS \"melodic\" and are not logged in as root, you could
issue the command; ```
sudo apt install ros-melodic-radar-omnipresense
``` You can also download the
driver as source code and build it yourself. All external dependencies
have been removed, so a beginner should be able to accomplish it without
too many complications. The instructions on the wiki are very thorough
on walking a developer through the steps. A good place to start is
[wiki.ros.org/ROS/Tutorials/BuildingPackages](ROS/Tutorials/BuildingPackages)

## Support

For application support, please contact customerservice@omnipresense.com
.
