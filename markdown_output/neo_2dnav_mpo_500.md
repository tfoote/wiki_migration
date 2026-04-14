The package neo_2dnav_mpo_500 includes config files for running
[move_base](move_base).

## Usage/Example

first export your robot version in a shell (for example):
```
export ROBOT=mpo_500_1_0
``` then launch 2dnav in this shell:
```
roslaunch neo_2dnav_mpo_500 2dnav.launch env_map:=/full/path/to/your_map.yaml
```
