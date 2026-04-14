See also: [Doxygen](Doxygen), [Sphinx](Sphinx), and [Epydoc](Epydoc)

## What is rosdoc_lite?

\`rosdoc_lite\` is a simple program that runs an external documentation
tool, like [Doxygen](Doxygen), [Epydoc](Epydoc), or [Sphinx](Sphinx), on
a single ROS [package](Packages). It was built as a light-weight
replacement to the [rosdoc](rosdoc) tool and uses the same
\`rosdoc.yaml\` file format to assist in porting. We recommend trying
\`rosdoc_lite\` instead of attempting to setup those tools manually, as
it provides shortcuts for configuring those tools and can also import
additional ROS information. Configuring your package to be documented by
\`rosdoc_lite\` also has the additional benefit of allowing your package
to be indexed for inclusion on the ROS wiki.

\`rosdoc_lite\` makes a best effort at providing good default settings
to these tools, and in some cases allows these settings to be customized
further.

In general, tools like Doxygen search all of the source code in a code
tree for structured comments, and then use these comments as well as the
API of the code to generate HTML files documenting the package. Doxygen
and Sphinx also provide additional tools for authoring documentation
that is not tied to code API.

By default, \`rosdoc_lite\` will use [Doxygen](Doxygen) to generate the
documentation for a package. If you wish to use another tool, like
[Epydoc](Epydoc) or [Sphinx](Sphinx), you must use a rosdoc
configuration file. This is described below. For C/C++, only Doxygen is
advised.

The documentation that is generated will depend on which tool is used,
as each tool behaves differently. For example, Doxygen will extract API
details from all source files found in the package (see
[Doxygen](Doxygen) for more).

\`rosdoc_lite\` is used as part of an automated process for updating
documentation on ros.org. It is frequently run on repositories that have
[rosinstall](rosinstall) files listed in the
[rosdistro](https://github.com/ros/rosdistro) repository, with the
resulting documentation linked to in the \"Code API\" link of many
packages\' on \`wiki.ros.org\`.

\`rosdoc_lite\` contains some additional functionality for generating
machine-readable documentation files, as well as \`msg\`/\`srv\`
documentation, that are used by the ros.org wiki system and elsewhere.
This functionality is mainly only of use to those maintaining
documentation Web sites.

## Usage

### Installation

```
apt-get install ros-$ROS_DISTRO-rosdoc-lite
```

### Generate document locally

You can use \`rosdoc_lite\` to generate local copies of documentation.
When you run the \`rosdoc_lite\` command, it will generate documentation
into the \'doc\' folder of the local directory.

```
Usage: rosdoc_lite [options] [package_path]

Options:
  -h, --help            show this help message and exit
  -q, --quiet           Suppress doxygen errors.
  -o OUTPUT_DIRECTORY   The directory to write documentation to.
  -t TAGFILE, --tagfile=TAGFILE
                        Path to tag configuration file for Doxygen cross
                        referencing support. Ex: /home/user/tagfiles_list.yaml
  -g GENERATE_TAGFILE, --generate_tagfile=GENERATE_TAGFILE
                        If specified, will generate a doxygen tagfile in this
                        location. Ex: /home/user/tags/package.tag
``` \'\'Generate documentation for a package\'\':

```
rosdoc_lite <path_of_package>
``` . This will generate the documentation in
\`doc\`. It\'s easiest if you point your Web browser to open
\`doc/html/index.html\`. Note that you need \`doxygen\` installed on
your machine (e.g., \`sudo apt-get install doxygen\`). You may also need
to install sphinx or epydoc for certain Python packages.

### Create rosdoc configuration files (to use Epydoc, Sphinx)

rosdoc supports a YAML-based configuration file that lets you:

-   use Epydoc or Sphinx instead of Doxygen
-   configure multiple documentation builds per package
-   do advanced configuration of documentation builds

For more details, please see one of these pages:

-   [Epydoc](Epydoc)
-   [Sphinx](Sphinx)

#### Enabling via package.xml

In order to enable the rosdoc configuration file, simply have a
\`rosdoc.yaml\` file in the root of your package. If you wish to name it
something else, you must place the following tag in the
\`\<export\>\...\</export\>\` section of the \`package.xml\`, but this
behavior is old:

```
<export>
  <rosdoc config="rosdoc.yaml" />
</export>
```

#### Basic Syntax

The YAML configuration file should contain a list of dictionaries, where
each dictionary has the following standard keys:

-   \'\'\'builder\'\'\': name of documentation builder (\`doxygen\`,
    \`epydoc\`, or \`sphinx\`)
-   \'\'\'output_dir\'\'\': (optional) name of sub-directory to write
    documentation to. If you have multiple builders, you must specify
    this property to avoid builders writing to the same directory.
-   \'\'\'name\'\'\': (optional) name of documentation set (e.g.
    \"Python API\")
-   \'\'\'required\'\'\': (optional) if set to True, the build will fail
    if any documentation builder fails. The default behavior is to
    ignore builder errors.

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

The \"doxygen\" builder will enable running [Doxygen](Doxygen) on a
package. As Doxygen is the default builder for any package, it is only
necessary to configure this option if:

-   you wish to run multiple builders in a package
-   you wish to enable additional Doxygen configuration options, which
    are described below

The \"doxygen\" builder may specify the following additional keys:

-   \'\'\'file_patterns\'\'\': (optional) override the Doxygen
    \`FILE_PATTERNS\` property
-   \'\'\'excludes\'\'\': (optional) override the Doxygen \`EXCLUDE\`
    property
-   \'\'\'homepage\'\'\': (optional) link to project home page
-   \'\'\'exclude_patterns\'\'\': \'\'\'ROS C-Turtle\'\'\' (optional)
    override Doxygen \`EXCLUDE_PATTERNS\` property.
-   \'\'\'javadoc_autobrief\'\'\': (optional) override Doxygen
    \`JAVADOC_AUTOBRIEF\` property. Default \`NO\`.
-   \'\'\'multiline_cpp_is_brief\'\'\': (optional) override Doxygen
    property \`MULTILINE_CPP_IS_BRIEF\`. Default \`NO\`.
-   \'\'\'tab_size\'\'\': (optional) override Doxygen property
    \`TAB_SIZE\`. Default \`8\`.
-   \'\'\'aliases\'\'\': (optional) override Doxygen property
    \`ALIASES\`. Default \"\"
-   \'\'\'example_patterns\'\'\': (optional) override Doxygen property
    \`EXAMPLE_PATTERNS\`. Default \"\"
-   \'\'\'image_path\'\'\': (optional) override Doxygen property
    \`IMAGE_PATH\`.
-   \'\'\'exclude_symbols\'\'\': (optional) override Doxygen property
    \`EXCLUDE_SYMBOLS\`. Default \"\"
-   \'\'\'predefined\'\'\': (optional) override Doxygen property
    \`PREDEFINED\`. Default \"\"
-   \'\'\'use_mdfile_as_mainpage\'\'\': (optional) override Doxygen
    property USE_MDFILE_AS_MAINPAGE. Default \"\"
-   \'\'\'generate_treeview\'\'\': (optional) override Doxygen property
    GENERATE_TREEVIEW to specify whether a treeview side panel should be
    generated. Default \"NO\"
-   \'\'\'input_filter\'\'\': (optional) override Doxygen property
    INPUT_FILTER to specify a script to transform the source files with
    before being passed to Doxygen. Default \"\"
-   \'\'\'include_path\'\'\': (optional) override Doxygen property
    INCLUDE_PATH. Default \"\"

Simple example:

. From
[ardrone_autonomy](https://github.com/tum-vision/ardrone_autonomy/blob/master/rosdoc.yaml)
```
- builder: doxygen
  name: C++ API
  output_dir: c++
  file_patterns: '*.c *.cpp *.h *.cc *.hh *.dox'
  exclude_patterns: '*/ARDroneLib/*'
```

. Or using the README.md as mainpage: ```
- builder: doxygen
  file_patterns: '*.c *.cpp *.h *.cc *.hh *.dox *.md'
  use_mdfile_as_mainpage: README.md
```

#### Builder: Epydoc

The \"epydoc\" builder will enable running [Epydoc](Epydoc) on a
package.

\'\'\'Note\'\'\': Epydoc\'s \"introspection\" capability currently
breaks when trying to process some ros python modules, so this feature
should not be enabled in a custom epydoc config file.

The \"epydoc\" builder may specify the following additional keys:

-   \'\'\'exclude\'\'\': (optional) override the Epydoc \`\--exclude\`
    option
-   \'\'\'config\'\'\': (optional) override the Epydoc \`\--config\`
    option, which passes in a separate Epydoc configuration file.

Simple example:

. From
[dynamic_reconfigure](https://github.com/ros/dynamic_reconfigure/blob/master/rosdoc.yaml)
```
- builder: epydoc
  config: epydoc.config
```

#### Builder: Sphinx

The \"sphinx\" builder will enable running [Sphinx](Sphinx) on a
package.

The \"sphinx\" builder may specify the following additional keys:

-   \'\'\'sphinx_root_dir\'\'\': (optional) root directory of Sphinx
    documents, i.e. the location of \`index.rst\` and \`conf.py\`. If
    not specified, it will look for an \`index.rst\` file in the root of
    the ROS package.

Simple example:

. From
[rocon_uri/rosdoc.yaml](https://github.com/robotics-in-concert/rocon_tools/blob/7900b9aaa9242c8c91b42f96c820afe78b84363a/rocon_uri/rosdoc.yaml)
```
- builder: sphinx           # specify document generator. e.g) doxygen, epidoc, sphinx
  sphinx_root_dir: doc      # document directory
```

#### Builder: external

The \"external\" builder specifies that you wish to link to externally
generated documentation. \`rosdoc_lite\` will generate a landing page
with the link to the specified URL.

The \"external\" builder takes in the following additional keys:

-   \'\'\'external_url\'\'\': URL of external documentation
-   \'\'\'external_label\'\'\': (optional) link text

### (Option) Using Doxygen Tag Files

\`rosdoc_lite\` provides support for cross-referencing with external
[Doxygen](Doxygen) documentation using tag files. For more information
on using tag files with [Doxygen](Doxygen) to link to external
documentation, see this
[page](http://www.doxygen.nl/manual/external.html).

#### Generating a Tag File

To generate a tag file during a documentation run, simply pass the
\`-g\` option to rosdoc lite with a path to the desired location of the
tagfile. For example:

```
rosdoc_lite -o doc -g doc/tags/my_package.tag /path/to/my/package
```

### (Option) Using External Tag Files

\`rosdoc_lite\` can be passed a yaml file containing a list of tagfiles
with the \`-t\` option. This yaml file should contain a list of
dictionaries, where each dictionary has the following standard keys:

-   \'\'\'docs_url\'\'\': The URL that corresponds to the entry point of
    the documentation associated with the tag file.
-   \'\'\'location\'\'\': The location of the tag file to pass to
    Doxygen. This can be on the local file system (use <file://>) or a
    URL (use <http://>).

An example tags (example_tags.yaml) file is shown below:

```
Usage: rosdoc_lite [options] [package_path]

Options:
  -h, --help            show this help message and exit
  -q, --quiet           Suppress doxygen errors.
  -o OUTPUT_DIRECTORY   The directory to write documentation to.
  -t TAGFILE, --tagfile=TAGFILE
                        Path to tag configuration file for Doxygen cross
                        referencing support. Ex: /home/user/tagfiles_list.yaml
  -g GENERATE_TAGFILE, --generate_tagfile=GENERATE_TAGFILE
                        If specified, will generate a doxygen tagfile in this
                        location. Ex: /home/user/tags/package.tag
```0 Running \`rosdoc_lite\` with this file to get
cross references might look something like this:

```
Usage: rosdoc_lite [options] [package_path]

Options:
  -h, --help            show this help message and exit
  -q, --quiet           Suppress doxygen errors.
  -o OUTPUT_DIRECTORY   The directory to write documentation to.
  -t TAGFILE, --tagfile=TAGFILE
                        Path to tag configuration file for Doxygen cross
                        referencing support. Ex: /home/user/tagfiles_list.yaml
  -g GENERATE_TAGFILE, --generate_tagfile=GENERATE_TAGFILE
                        If specified, will generate a doxygen tagfile in this
                        location. Ex: /home/user/tags/package.tag
```1

### Linking to External Third Party Documentation

For third party packages, rosdoc_lite can automatically create a doxygen
main page for the package, that includes a link to the third party
documentation. To do so, you must add a line to your manifest.xml

```
Usage: rosdoc_lite [options] [package_path]

Options:
  -h, --help            show this help message and exit
  -q, --quiet           Suppress doxygen errors.
  -o OUTPUT_DIRECTORY   The directory to write documentation to.
  -t TAGFILE, --tagfile=TAGFILE
                        Path to tag configuration file for Doxygen cross
                        referencing support. Ex: /home/user/tagfiles_list.yaml
  -g GENERATE_TAGFILE, --generate_tagfile=GENERATE_TAGFILE
                        If specified, will generate a doxygen tagfile in this
                        location. Ex: /home/user/tags/package.tag
```2

## Automatically Generated Online Documentation on ros.org

\`rosdoc_lite\` is automatically run for packages in repositories that
have rosinstall files listed in the
[rosdistro](https://github.com/ros/rosdistro) repository. The resulting
documentation is uploaded to \`ros.org\` and is linked in the \"Code
API\" links that you see on various package pages, like [rospy](rospy).

Even if \`rosdoc_lite\` is automatically generated for your package, we
recommend regularly running \`rosdoc_lite\` on your own computer to
verify what your documentation looks like before checking it in.

rosdoc_lite is used automatically generate documentation on the ros.org
web server. Frequent updates are made to:

-   <http://docs.ros.org/api/>

It is also used to generate the data for the \`PackageHeader\`,
\`StackHeader\` and \`MsgSrvDoc\` wiki macros that you see on many of
the ros.org wiki pages.

## Roadmap/Stability

The \`rosdoc_lite\` tool itself is stable, though it has many internal
features and functionality that are changed to support the documentation
needs of \`ros.org\`. In the future, the \`rosdoc_lite\` tool will
hopefully be evolved to better support the configuration requirements of
the documentation tools it invokes (i.e. Doxygen).

The code API of \`rosdoc_lite\` should \'\'\'not\'\'\' be used as it is
an internal library that is frequently changed.
