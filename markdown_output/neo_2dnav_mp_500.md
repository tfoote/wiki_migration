The package neo_2dnav_mp_500 includes config files for running
[move_base](move_base) with an mp-500 robot.

## Usage/Example

first export the robot type in a shell (for example):


```
export ROBOT=mp_500_2_1
```

 then launch 2dnav in this shell:


```
roslaunch neo_2dnav_mp_500 2dnav.launch env_map:=/full/path/to/your_map.yaml
```


