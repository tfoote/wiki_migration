This package provides version 2.1 of
[Google Perftools](https://code.google.com/p/gperftools/) as a catkin
package for ROS Hydro (Indigo coming).

# Usage:

Unlike most catkin packages, using gperftools is a three-step process.
You must declare a dependency on gperftools in your package.xml and in
your CMakeLists, and your must specify which gperftools features you
want to use.

## Declaring a dependency on gperftools

Add build and run dependencies to your package.xml:



```
<build_depend>gperftools_21</build_depend>
<run_depend>gperftools_21</run_depend>
```



Add gperftools_21 to the list of catkin conponents in your
CMakeLists.txt:



```
find_package(catkin REQUIRED COMPONENTS
   gperftools_21
   # other catkin components ...
)
```



## Choosing which gperftools features you want

You can choose to use tcmalloc, the gperftools profiler, or both.

**tcmalloc:** 

```
target_link_libraries(your_target ${GPERFTOOLS_TCMALLOC})
```



**profiler:** 

```
target_link_libraries(your_target ${GPERFTOOLS_PROFILER})
```



**both:** 

```
target_link_libraries(your_target ${GPERFTOOLS_TCMALLOC_AND_PROFILER})
```


