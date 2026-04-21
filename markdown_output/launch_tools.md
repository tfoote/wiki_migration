## launch_tools

### launchViz

![launchViz\|width=350](attachment:image.png)

Draws the relationship between launchfiles and nodes inside a folder or
a set of packages. Launchfiles inside the search are green boxes,
launchfiles outside the search are white ellipses and nodes are brown
rounded boxes.

-   Usage

Run: 

```
$ rosrun srv_tools launchViz
```

 launchViz will search for launchfiles in
the working directory 

```
$ rosrun srv_tools launchViz -pkg PKG_A [PKG_B ...]
```

 launchViz will search in
the specified packages
