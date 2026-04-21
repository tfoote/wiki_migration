## Usage

### Setup

Add the eros python tools to your PATH. The easiest way to do this is
simply to add the command to your setup.sh.



```
echo "export PATH=`rospack find eros_python_tools`/scripts:\${PATH}" >> setup.sh
```



### Tool List

-   [rostoolchain](eros_python_tools/rostoolchain) - create, delete or
    select from existing toolchain configurations.
-   [rosplatform](eros_python_tools/rosplatform) - create, delete or
    select from existing platform configurations.
-   [rosbuild](eros_python_tools/rosbuild) - setting/viewing the current
    global build mode (debug, release etc).
-   [rosprefix](eros_python_tools/rosprefix) - setting/viewing the
    current install prefix.
-   [rosprotect](eros_python_tools/rosprotect) - clean, build and
    protect parts of your ros install.
-   [roscreate-qt-pkg](eros_python_tools/roscreate_qt_pkg) - creates a
    simple layout for a qt based package.
-   [roscreate-qt-ros-pkg](eros_python_tools/roscreate_qt_ros_pkg) -
    creates a simple layout for a qt based ros package.
