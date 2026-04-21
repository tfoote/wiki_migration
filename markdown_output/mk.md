/!\\ **`'NOTE:`**' when using `rospack` to find the `mk`-package,
the `ROS_PACKAGE_PATH` needs to be set accordingly. Thus, you should
have a dependency to `roslib` in your `package.xml`, as this
provides the respective
[environment hooks](https://github.com/ros/ros/blob/jade-devel/core/roslib/env-hooks/10.ros.sh.em)
that set this.

## CMake-driven builds

Most packages, and all stacks, use CMake to build. But every package
must provide a `Makefile` if it does any building. The following files
are provided to simplify the `Makefile` in most packages, and all
stacks:

-   `cmake.mk`
-   `cmake_stack.mk` Use these files by including them, as explained
    in the [rosbuild documentation](rosbuild) and
    [stack-building documentation](StackBuildFiles).

## 3rdparty code, from tarball

For a 3rdparty package that pulls code from an tarball (or equivalent
downloadable file), you should use `download_unpack_build.mk`, like
so: 

```
all: paramiko

TARBALL = build/paramiko-1.7.5.tar.gz
TARBALL_URL = http://pr.willowgarage.com/downloads/paramiko-1.7.5.tar.gz
SOURCE_DIR = build/paramiko-1.7.5
MD5SUM_FILE = paramiko-1.7.5.tar.gz.md5sum
UNPACK_CMD = tar xzf
include $(shell rospack find mk)/download_unpack_build.mk

paramiko: $(SOURCE_DIR)/unpacked
        mkdir -p src
        cd $(SOURCE_DIR) && python setup.py build 
        rm -rf src
        mv `python find_pylib.py paramiko $(SOURCE_DIR)/build/` src
        touch paramiko
clean:
        -rm -rf src $(SOURCE_DIR) paramiko
wipe: clean
        -rm -rf build
```

 The following variables should be defined
prior to including `download_unpack_build.mk`:

-   `TARBALL`: local path to which the tarball should be downloaded;
    it **must** start with `build/`
-   `TARBALL_URL`: fully-qualified URL from which to retrieve the
    tarball
-   `SOURCE_DIR`: source directory that you want the tarball unpacked
    into; it **must** start with `build/`
-   `INITIAL_DIR` (optional): the name that the tarball will naturally
    unpack into, if different from `SOURCE_DIR`; it **must** start
    with `build/`
-   `UNPACK_CMD` (optional): the command to apply to the tarball to
    unpack it (default: `tar xzf`)
-   `MD5SUM_FILE` (optional, but highly recommended): The name of a
    file containing the md5 hash of the tarball, in the format produced
    by the UNIX command `md5sum`
-   `TARBALL_PATCH` (optional): a list of patch files to apply to the
    tarball after unpacking (e.g. 'TARBALL_PATCH = patch1.patch
    patch2.patch')

After including `download_unpack_build.mk`, you can make targets
depend on the `\$(SOURCE_DIR)/unpacked` file; it will be created (and
updated) after the tarball has been downloaded, unpacked, and
(optionally) patched.

### Examples

Some packages that use `download_unpack_build.mk`:

-   [pycrypto](pycrypto)
-   [gtest](gtest)
-   [prosilica_gige_sdk](prosilica_gige_sdk)
-   [sicktoolbox](sicktoolbox)

## 3rdparty code, from SVN

For a 3rdparty package that pulls code from an SVN repository, you
should use `svn_checkout.mk`, like so: 

```
all: installed

SVN_DIR = build/stage-svn
SVN_URL = https://playerstage.svn.sourceforge.net/svnroot/playerstage/code/stage/branches/stage-ros
SVN_REVISION = -r 8262
include $(shell rospack find mk)/svn_checkout.mk

installed: $(SVN_DIR) patched Makefile.stage
        cd $(SVN_DIR) && autoreconf -i -s
        cd $(SVN_DIR) && ./configure --prefix=`pwd`/../..
        cd $(SVN_DIR) && make install
        touch installed

clean:
        -cd $(SVN_DIR) && make clean
        rm -rf stage installed patched

wipe: clean
        rm -rf $(SVN_DIR)
```

 The
following variables should be defined prior to including
`svn_checkout.mk`:

-   `SVN_DIR`: the name of the local working copy to be created
-   `SVN_URL`: the URL of the repository to check out from
-   `SVN_REVISION` (optional, but highly recommended): the revision to
    check out at, including the `-r` flag (e.g., `-r 8262`)
-   `SVN_CMDLINE` (optional): how to invoke `svn` (useful if you
    want to pass extra arguments, e.g. `svn \--non-interactive`)
-   `SVN_PATCH`: list of patch files to apply to the working copy
    after checkout

After including `svn_checkout.mk`, you can make your targets depend on
the `patched` file; it will be created after the working copy is
checked out and (optionally) patched.

### Examples

Some packages that use `svn_checkout.mk`:

-   [kdl](kdl)
-   [gazebo](gazebo)
-   [opencv2](opencv2)
-   [cwiid](cwiid)

## 3rdparty code, from Git, Mercurial, Bazaar

Similar to `svn_checkout.mk`, there are also:

-   `git_checkout.mk`
-   `hg_checkout.mk`
-   `bzr_checkout.mk`

These are based on `svn_checkout.mk`, so you can generally use them by
substituting the appropriate three-letter abbreviation for `SVN`.

## Optimizing SVN

svn checkouts are both slow and more prone to downtime. A hybrid
approach using the tarball for distribution, and a fancy makefile can be
done with a script like the [bullet](bullet) package
<https://code.ros.org/svn/ros-pkg/stacks/geometry/tags/geometry-1.0.0/bullet/Makefile.bullet>
This uses the svn_checkout script to build the tarball when developing,
but most users simply use the tarball.
