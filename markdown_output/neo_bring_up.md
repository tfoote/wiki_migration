## Description

In this package you can find bringup scripts.

## Usage/Example

### mpo 500

To start your mpo-500, type the following commands in a shell:


```
export ROBOT=mpo_500_1_0
```





```
roslaunch neo_bring_up mpo_500.launch
```



### mp 500

If you are using a mp-500 from year 6/2009 and later you should set:


```
export ROBOT=mp_500_2_1
```

 For older mp-500s use the following setting:


```
export ROBOT=mp_500_0_9
```

 After that you can launch the bring_up script:


```
roslaunch neo_bring_up mp_500.launch
```


