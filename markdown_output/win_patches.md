## Patch List

The code api link always contains a list of the currently floated
patches in win_ros.

## Usage

### Msvc

This following batch file makes one assumption: you must have all source
stacks one level below your root. For example, `C:\\work\\src` should
include directories for `ros`, `ros_comm`, `rospkg`, `win_ros`
etc\...



```
> cd win_ros/win_patches
> apply_msvc_patches
```



### Mingw



```
> cd win_ros/win_patches
> apply_mingw_patches
```


