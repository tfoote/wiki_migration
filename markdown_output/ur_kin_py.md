# Installation

-   Clone ur_kin_py: <https://github.com/gt-ros-pkg/ur_kin_py>
-   Clone boost_numpy: <https://github.com/gt-ros-pkg/Boost.NumPy>
-   catkin_make



```
from ur_kin_py.kin import Kinematics
kin = Kinematics('ur5') # or ur10
print kin.forward([0.1]*6)
```


