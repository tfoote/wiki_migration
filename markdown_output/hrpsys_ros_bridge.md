## Usage

Other than API documentation being available
[here](http://ros.org/doc/api/hrpsys_ros_bridge/html/index.html), this
package is missing document and your contribution is appreciated. Please
contact through
[this ticket](https://github.com/start-jsk/rtmros_common/issues/302).

### Model config file generation

In its downstream package, you might see a folder for conf files (e.g.
[hironx_ros_bridge/conf](https://github.com/start-jsk/rtmros_hironx/tree/groovy-devel/hironx_ros_bridge/conf))
where only template files with suffix `.in` are stored. Once you build
the package the concrete files are generated into the same folder. There
are 3 types of conf files of which the distinction may not be very clear
([related discussion](https://github.com/start-jsk/rtmros_hironx/issues/92)):

-   `_nosim`: simulation without dynamics
-   (no suffix or any other indicatior): simulation with dynamics
-   `_real`/`_realrobot`: Real robot (not simulation)

## For Maintainers

### Tweak to release into Groovy

While in current design the package depends on
[pr2_controllers_msgs](pr2_controllers_msgs) that's catkinized from
[hydro](hydro) onward and not available in [groovy](groovy), some hacks
allow the package not to separate `branches` (regardless it's good or
not, doing so is the decision as of March 2014). This requires another
hack during release process using `bloom` as follows:

1\. Run [bloom](bloom) as normal. E.g. `\$ bloom-release \--rosdistro
groovy \--track groovy rtmros_common`. 2. Once `bloom` halts and its
command prompt starts waiting on the same terminal (the output might
look as following), edit `package.xml` to comment out lines for
declaring build and run depend on `pr2-controllers`.

```
$ bloom-release --rosdistro groovy --track groovy rtmros_common
:
>>> Resolve any conflicts and when you have resolved this problem run 'git am --resolved' and then exit the shell using 'exit 0'. <<<
    To abort use 'exit 1'
(bloom)emacs package.xml
```

Modify `package.xml` as: ```
:  
<!-- <build_depend>pr2_controllers</build_depend> -->
:
<!-- <run_depend>pr2_controllers</run_depend> -->
:
```

3\. Run `git add`, `\$ git am \--skip`, `git commit` like below,
and `exit 0` respectively. If all succeeds then `bloom` resumes.
```
(bloom)git add package.xml
(bloom)git am --skip
Resolve operation not in progress, we are not resuming.
(bloom)git commit -m "3rd trial commentout pr2 pkg" -a
[release/groovy/hrpsys_ros_bridge 1c05bbc] 3rd trial commentout pr2 pkg
 1 file changed, 1 insertion(+), 1 deletion(-)
(bloom)git status
# On branch release/groovy/hrpsys_ros_bridge
# Your branch is ahead of 'origin/release/groovy/hrpsys_ros_bridge' by 8 commits.
#
nothing to commit (working directory clean)
(bloom)exit 0
exit
 [git-bloom-patch import]: User reports that conflicts have been resolved, continuing.
 [git-bloom-patch import]: Applied 2 patches
:
(bloom continues)
```
