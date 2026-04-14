Imagine you whould never have to write a \'\'\'CMakeLists.txt\'\'\' file
again. Never forget to install everything, no need to update it whenever
you add a file, not time lost for figuring out how to call and use
find_package for your dependencies, etc.

Well, this is exactly what mrt_cmake_modules do for you! The only thing
you have to do is:

-   Keep your files in a fixed structure,
-   keep library and executable code in separate packages and
-   make sure the package.xml actually contains all the packages you
    depend on.

If you don\'t want to agree to this, there are ways to get this done as
well. This will require you to modify our template file a bit.

On the other hand, you get a lot of things for free:

-   Resolution of your dependencies in CMake based on your package.xml
-   Automatic generation of Nodes/Nodelets
-   Supports C++ and Python(2/3)
-   Python bindings for pybind11/boost-python
-   Automated unittest detection and execution (including ROS tests)
-   Automated code coverage generation
-   Support for sanitizers
-   Support for running clang-tidy
-   Automated install of your
    scripts/launchfiles/executables/libraries\... to the correct
    location

For more information, please refer to the documentation
[within the repository](https://github.com/KIT-MRT/mrt_cmake_modules)

\<\<GitHubIssues(KIT-MRT/mrt_cmake_modules)\>\>
