

## Tutorials

- [The Ecl CMake Library](#the-ecl-cmake-library):
  Lists ecl's cmake library api and demos its usage.
- [Link as Needed](#link-as-needed):
  Remove unused library dependencies from being automatically linked by
  ros.

## The Ecl CMake Library

- **Description:** Lists ecl's cmake library api and demos its usage.
- **Keywords:** ecl cmake
- **Tutorial Level:** INTERMEDIATE
- **Next Tutorial:**
  [Link as Needed](#link-as-needed)

### Overview

These are modules which can be included by cmake in the regular way with
a macro/function api to call upon (think regular c-style library).

One nice feature of this is that you don't waste time processing macros
you don't use (unlike a usual cmake module).

### Usage

- Ensure ecl_build is listed as a dependency in your manifest.xml
- Simply rosbuild_include any of the macro libraries you wish to use:



```
# Include the macro libraries you wish to use...e.g.
rosbuild_include(ecl_build ecl_build_utilities)
rosbuild_include(ecl_build ecl_platform_detection)
rosbuild_include(ecl_build ecl_ros_utilities)

# Call the macros
ecl_detect_platform() # a general purpose platform sniffer
ecl_ros_get_dependency_list() # get the dependency list for this project

# Finally use some of the variables it sets (this one the dependency 
message(STATUS "Dependencies: ${${PROJECT_NAME}_DEPENDENCIES}")
```



### The Library

See the code api in ecl_build (i.e. the .cmake
files) for more detailed usage notes and examples.

#### Platform Detection

- **File**: ecl_platform_detection.cmake



```
ecl_detect_distro() - returns distro version details )currently ubuntu only).
ecl_detect_posix() - returns variables confirming the level of posix available.
ecl_detect_threads() - detects the thread model.
ecl_detect_timers() - detects the timers model.
ecl_detect_sizes() - determines the size of the fundamental types.
ecl_detect_char_type() - detects the typedef of char.
ecl_detect_endianness() - detects endianness of the platform.
ecl_set_platform_cflags() - sets platform flags based on various input variables.
ecl_detect_compiler_version() - returns the version of the compiler (msvc and gnu).
ecl_check_cxx_flags() - general version of CheckCXXCompilerFlags can be used for linker flags.
ecl_link_as_needed() - cross platform application of --link-as-needed.
ecl_link_no_as_needed() - cross platform application of the opposite.
ecl_detect_platform() - brings most of the above scripts together.
ecl_summary_platform() - prints results of the platform detection script.
```



#### Build Utilities

- **File**: ecl_build_utilities.cmake



```
ecl_download_url()
ecl_extract_tarball()
ecl_extract_bzip2()
ecl_autotools_compile()
ecl_add_uninstall()
```



#### Ros Utilities

- **File**: ecl_ros_utilities.cmake



```
ecl_ros_manifest_brief() - parses the package's manifest for the short description.
ecl_ros_get_dependency_list() - returns the list of all dependencies for a package.
ecl_ros_output_paths() - sets standard output paths for ros builds.
```

## Link as Needed

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [The Ecl CMake Library](#the-ecl-cmake-library).
- **Description:** Remove unused library dependencies from being
  automatically linked by ros.
- **Keywords:** ecl linking
- **Tutorial Level:** INTERMEDIATE

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     <#FFFF00> This tutorial is no longer relevant for most platforms supporting ros hydro and beyond since gcc has switched its internal behaviour to link as needed.   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

### Problem

The ros framework automatic dependency management will often bring in
far more libraries as a dependency to your library/app than it actually
uses. Actually, linux build frameworks used to have this issue as well.
For us this often means we're pulling in ros dependencies when ecl is
actually not depending on any ros code (just the build environment). It
also means we string together too many dependencies within the ecl as
well, which creates a size problem for embedded builds.

To get around this, most distros have moved to using the
\--link-as-needed flag with gcc to automatically prune these redundant
dependencies. This flag is different on different platforms though (e.g.
macosx use a different flag), so ecl provides a cmake macro which can be
used to set this for your package. In your CMakeLists.txt:

### Solution

- Include ecl_build as a dependency in your package's manifest.xml
  (this allows you to rosbuild_include).
- Set up your CMakeLists.txt to bring in ecl's cmake macro libraries as
  follows:



```
cmake_minimum_required(VERSION 2.4.6)

include($ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake)
rosbuild_init()
rosbuild_include(ecl_build ecl_platform_detection)

ecl_link_as_needed(ECL_LINK_AS_NEEDED_FLAG)
set(ROS_LINK_FLAGS "${ROS_LINK_FLAGS} ${ECL_LINK_AS_NEEDED_FLAG}")

# Actual build stuff here
```
