Simple example of using boost python to wrap c++ code.

# run the sample

```
roscd foo_boost_python
rosmake
rosrun foo_boost_python doit.py
```

Very cool.

# rosh

```
rosrun rosh rosh
``` Try some tab completion.
```rosh
In [2]: roslib.load_manifest('foo_boost_python')
In [3]: import foo_boost_python as fbp
In [4]: fbp.myfunction(5)
void myfunction(int) 5

In [5]: help(fbp.myfunction)
Help on built-in function myfunction:

myfunction(...)
    myfunction( (int)arg1) -> None :
    
        C++ signature :
            void myfunction(int)
```
