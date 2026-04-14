Contains code for working with a wrist-mounted NetFT force/torque
sensor.

## Usage

netft_zeroing.py processes the Wrench messages broadcast by the
[netft_rdt_driver](netft_rdt_driver) package to remove the forces due to
gravity. The calibration procedure is automated on a wrist mounted PR2
netft sensor by incrementally sampling forces with various orientations
of the gripper. A parameter file is fed to the utility (examples in the
params folder) and output parameters are written back to it.

Show help options: ```
rosrun hrl_netft netft_zeroing.py --help
# describes the options available for the script
```

### Quick Start

#### Training a Tool

```
roslaunch hrl_phri_2011 phri_netft_tracking.launch
roscd hrl_phri_2011
cp params/ft_zero_params_scratcher_tool.yaml params/ft_zero_params_$tool$_tool.yaml
vim params/ft_zero_params_$tool$_tool.yaml
# Edit wrench_location_frame to be "/$tool$"
roslaunch hrl_netft netft_zero_train.launch tool:=$tool$
# Hit enter to collect sample (stay still)
# Type "d" and hit enter to finish
# Collect at least 20 samples
```

#### Running the Zeroing Node

```
roslaunch hrl_phri_2011 phri_netft_tracking.launch
roslaunch hrl_netft netft_zero_run.launch tool:=$tool$
```
