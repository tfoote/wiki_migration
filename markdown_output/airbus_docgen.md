The airbus_docgen package can be used for the auto generation of HTML
documentation of a complete workspace, this package will create a
graphical tree of your workspace, metapackages and packages, a tree of
dependencies between packages and an API of executable files, services,
messages and actions.

## Execution

The launch file airbus_docgen.launch can be used to call the tool:



```
roslaunch airbus_docgen airbus_docgen.launch output_path:="/tmp/docu" ros_pkg:="/home/user/my_workspace"
```

 or: 

```
roslaunch airbus_docgen airbus_docgen.launch output_path:="/tmp/docu" ros_pkg:="package_name"
```



Input parameters of this launch file are:

-   output_path: the path where should be saved the generated
    documentation (optional, by default /tmp/docu)
-   ros_pkg: the name of the package that has to be documented or the
    name of the workspace that contains all the packages to be
    documented

In case you want to document your current workspace and save the
documentation in the /tmp/docu directory, you can just call the index.py
node:



```
rosrun airbus_docgen index.py
```



The index.html of your workspace will look like the following image:

![\|width=100%](attachment:docgen1.png)

Choosing one of the package of the menu a direct link to each package
description will show the following graphic:

![\|width=100%](attachment:docgen2.png)
