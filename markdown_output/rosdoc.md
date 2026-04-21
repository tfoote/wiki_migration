**DEPRECATION NOTICE: `rosdoc` is now deprecated in favor of
[rosdoc_lite](rosdoc_lite)**

See also: [Doxygen](Doxygen), [Sphinx](Sphinx), and [Epydoc](Epydoc)

## What is rosdoc?

`rosdoc` is simply a tool that runs an external documentation tool,
like [Doxygen](Doxygen), [Epydoc](Epydoc), or [Sphinx](Sphinx), on one
or more ROS [packages](Packages). We recommend trying `rosdoc` instead
of attempting to setup those tools manually, as it provides shortcuts
for configuring those tools and can also import additional ROS
information.

`rosdoc` makes a best effort at providing good default settings to
these tools, and in some cases allows these settings to be customized
further. The documentation is generated on a package-by-package basis
\-- `rosdoc` does not run on ROS [stacks](Stacks).

In general, tools like Doxygen search all of the source code in a code
tree for structured comments, and then use these comments as well as the
API of the code to generate HTML files documenting the package. Doxygen
and Sphinx also provide additional tools for authoring documentation
that is not tied to code API.

By default, `rosdoc` will use Doxygen to generate the documentation
for a package. If you wish to use another tool, like Epydoc or Sphinx,
you must use a rosdoc configuration file. This is described below. For
C/C++, only Doxygen is advised.

The documentation that is generated will depend on which tool is used,
as each tool behaves differently. For example, Doxygen will extract API
details from all source files found in the package (see
[Doxygen](Doxygen) for more).

`rosdoc` is used as part of an automated process for updating
documentation on ros.org. It is frequently run on packages in
`ros-pkg` and `wg-ros-pkg`, with the resulting documentation linked
to in the "Code API" link of many packages.

`rosdoc` contains some additional functionality for generating
machine-readable documentation files, as well as `msg`/`srv`
documentation, that are used by the ros.org wiki system and elsewhere.
This functionality is mainly only of use to those maintaining
documentation Web sites.

## Usage

You can use `rosdoc` to generate local copies of documentation. When
you run the `rosdoc` command, it will generate documentation into the
'doc' folder of the local directory.



```
Usage: rosdoc [options] [packages...]

Options:
  -h, --help            show this help message and exit
  -n NAME, --name=NAME  Name for documentation set
  --paths=PATHS         package paths to document
  -o OUTPUT_DIRECTORY   directory to write documentation to
```



*Generate documentation for specific packages*:



```
roscd rosdoc
./rosdoc <package-names>
```

 or simply 

```
rosrun rosdoc rosdoc <package-names>
```



This will generate the documentation in `rosdoc/doc`. It's easiest if
you point your Web browser to open
`rosdoc/doc/<package-name>/html/index.html`. Note that you need
`doxygen` installed on your machine (e.g., `sudo apt-get install
doxygen`). You may also need to install sphinx for certain Python
packages.

*Generate documentation for all packages*:



```
roscd rosdoc
./rosdoc
```



`rosdoc` will find all packages on your package path and generate
documentation for them in the 'doc' folder.

*Generate documentation in your home directory*:

Sometimes, the `rosdoc` package directory may not be writable, perhaps
it was installed as a binary package. In that case, use the `-o`
option to specify a different output directory. 

```
roscd rosdoc -o ~/doc
./rosdoc <package-names>
```


(Again rosrun combination works here too.)

## Automatically Generated Online Documentation

`rosdoc` is automatically run for packages in `ros-pkg`,
`wg-ros-pkg`, and others. The resulting documentation is uploaded to
`ros.org` and is linked in the "Code API" links that you see on
various package pages, like [rospy](rospy).

Even if `rosdoc` is automatically generated for your package, we
recommend regularly running `rosdoc` on your own computer to verify
what your documentation looks like before checking it in.

## rosdoc configuration files (Epydoc, Sphinx)

rosdoc supports a YAML-based configuration file that lets you:

-   use Epydoc or Sphinx instead of Doxygen
-   configure multiple documentation builds per package
-   do advance configuration of documentation builds

### Enabling via manifest.xml

In order to enable the rosdoc configuration file, you must place the
following tag in the `<export>\...</export>` section of the
[manifest.xml](Manifest) file:



```
<export>
  <rosdoc config="rosdoc.yaml" />
</export>
```



`rosdoc.yaml` should be the path to the configuration file you wish to
use.

### Basic Syntax

The YAML configuration file should contain a list of dictionaries, where
each dictionary has the following standard keys:

-   **builder**: name of documentation builder (`doxygen`, `epydoc`,
    or `sphinx`)
-   **output_dir**: (optional) name of sub-directory to write
    documentation to. If you have multiple builders, you must specify
    this property to avoid builders writing to the same directory.
-   **name**: (optional) name of documentation set (e.g. "Python API")

Each builder may specify additional configuration keys.

Here is an example from the [roslib](roslib) package, which performs
both C++ and Python API documentation:



```
- builder: epydoc
   output_dir: python
 - builder: doxygen
   name: C++ API
   output_dir: c++
   file_patterns: '*.c *.cpp *.h *.cc *.hh *.dox'
```



#### Builder: Doxygen

The "doxygen" builder will enable running [Doxygen](Doxygen) on a
package. As Doxygen is the default builder for any package, it is only
necessary to configure this option if:

-   you wish to run multiple builders in a package
-   you wish to enable additional Doxygen configuration options, which
    are described below

The "doxygen" builder may specify the following additional keys:

-   **file_patterns**: (optional) override the Doxygen `FILE_PATTERNS`
    property
-   **excludes**: (optional) override the Doxygen `EXCLUDE` property
-   **homepage**: (optional) link to project home page
-   **exclude_patterns**: **ROS C-Turtle** (optional) override Doxygen
    `EXCLUDE_PATTERNS` property.
-   **javadoc_autobrief**: (optional) override Doxygen
    `JAVADOC_AUTOBRIEF` property. Default `NO`.
-   **multiline_cpp_is_brief**: (optional) override Doxygen property
    `MULTILINE_CPP_IS_BRIEF`. Default `NO`.
-   **tab_size**: (optional) override Doxygen property `TAB_SIZE`.
    Default `8`.
-   **aliases**: (optional) override Doxygen property `ALIASES`.
    Default ""
-   **example_patterns**: (optional) override Doxygen property
    `EXAMPLE_PATTERNS`. Default ""
-   **image_path**: (optional) override Doxygen property `IMAGE_PATH`.
-   **exclude_symbols**: (optional) override Doxygen property
    `EXCLUDE_SYMBOLS`. Default ""

#### Builder: Epydoc

The "epydoc" builder will enable running [Epydoc](Epydoc) on a
package.

**Note**: Epydoc's "introspection" capability currently breaks when
trying to process some ros python modules, so this feature should not be
enabled in a custom epydoc config file.

The "epydoc" builder may specify the following additional keys:

-   **exclude**: (optional) override the Epydoc `\--exclude` option
-   **config**: (optional) override the Epydoc `\--config` option,
    which passes in a separate Epydoc configuration file.

#### Builder: Sphinx

The "sphinx" builder will enable running [Sphinx](Sphinx) on a
package.

The "sphinx" builder may specify the following additional keys:

-   **sphinx_root_dir**: (optional) root directory of Sphinx documents,
    i.e. the location of `index.rst` and `conf.py`. If not
    specified, it will look for an `index.rst` file in the root of the
    ROS package.

#### Builder: external

The "external" builder specifies that you wish to link to externally
generated documentation. `rosdoc` will generate a landing page with
the link to the specified URL.

The "external" builder takes in the following additional keys:

-   **external_url**: URL of external documentation
-   **external_label**: (optional) link text

#### Builder: rosmake

**Removed in ROS Fuerte**: this builder has been removed as it has
problematic side-effects.

The "rosmake" builder specifies that `rosdoc` must run
[rosmake](rosmake) on the package before generating documentation. This
is most frequently used in packages with auto-generated code, such as
swig-wrappers.

The "rosmake" builder takes no additional configuration. The "name"
and "output_dir" options are ignored.

## Linking to External Third Party Documentation

*NOTE: starting with C Turtle, you can also use the 'external' builder
specified above*

For third party packages, rosdoc can automatically create a doxygen main
page for the package, that includes a link to the third party
documentation. To do so, you must add a line to your
manifest.xml

```
<export>
  <doxymaker external="http://link.to.external/page.html"/>
</export>
```



## rosdoc on ros.org

rosdoc is used automatically generate documentation on the ros.org web
server. Frequent updates are made to:

-   <http://ros.org/doc/api>

It is also used to generate the data for the `PackageHeader`,
`StackHeader` and `MsgSrvDoc` wiki macros that you see on many of
the ros.org wiki pages.

## Roadmap/Stability

The `rosdoc` tool itself is stable, though it has many internal
features and functionality that are changed to support the documentation
needs of `ros.org`. In the future, the `rosdoc` tool will hopefully
be evolved to better support the configuration requirements of the
documentation tools it invokes (i.e. Doxygen), and it will also better
support documenting specific stacks.

The code API of `rosdoc` should **not** be used as it is an internal
library that is frequently changed.
