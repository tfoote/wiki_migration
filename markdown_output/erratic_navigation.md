The erratic_navigation package contains configuration and launch files
for running the navigation stack on an Erratic robot. Currently there
are three sets of configuration options:

-   navigation_global - this set contains configuration files for the
    [move_base](move_base) and [amcl](amcl) nodes meant to be run in an
    application that requires global navigation with a pre-specified
    static map.

```{=html}
<!-- -->
```
-   navigation_local - this set contains configuration files for the
    [move_base](move_base) node meant to be run in an application that
    requires navigation in an odometric frame.

```{=html}
<!-- -->
```
-   navigation_slam - this set contains configuration files for the
    [move_base](move_base) and [gmapping](gmapping) nodes meant to be
    run in an application that requires SLAM-based global navigation.
