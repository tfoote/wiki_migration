You might also check [catkin_lint](catkin_lint) for checking package
configuration.

## Usage

Add a **build** dependency on roslint to your package's
`package.xml`:



```
<build_depend>roslint</build_depend>
```



In your package's `CMakeLists.txt` file, include roslint as one of
your catkin component dependencies:



```
find_package(catkin REQUIRED COMPONENTS roslint ...)
```



Then, invoke the roslint functions from your `CMakeLists.txt`, eg:



```
roslint_cpp()
```



If you'd like more control over what gets linted, you can specify the
exact files:



```
roslint_cpp(src/foo.cpp src/bar.cpp src/baz.cpp)
```



To run roslint against your package you must invoke catkin_make with
your package's roslint target. For example, for a package named
`my_fancy_package` you would run:



```
catkin_make roslint_my_fancy_package
```



To use roslint with catkin_tools (aka catkin build), use the following
command:



```
catkin build my_fancy_package --make-args roslint
```



You can also manually invoke roslint from the build directory with the
follow commands: 

```
cd ~/catkin_ws
catkin build
cd build/my_fancy_package
make roslint
```



See the following section for all available functions.

## Reference

Each `roslint_\*` function create a catkin build target called
`roslint_*pkgname*`, which runs all specified lint operations for the
package. Each additionally creates (if it does not yet exist) a master
`roslint` target, which depends on all other `roslint_\*` targets.

Each function can be called multiple times, if that's more convenient.

`roslint_cpp(\[files \...\])` . Lint the specified files using a
modified cpplint. If none are specified, default to a glob of all
`cpp` and `h` files contained in the package.

`roslint_python(\[files \...\])` . Lint the specified files using
pep8. If none are specified, default to a glob of all `py` files
contained in the package. This will not catch extensionless executables
living in the scripts directory.

`roslint_custom(linter linter_opts file \[\...\])` . Lint the
specified files using a custom lint executable.

`roslint_add_test()` . Create a dependency between the package's
run_tests target and lint target, so that linter fails are able to break
the build.

## Tips

To fix basic whitespace issues in C++, try using
[astyle](http://astyle.sourceforge.net/). Example invocation within your
package:



```
sudo apt-get install astyle
find -regextype egrep -regex '.*\.[ch](pp)?$' -exec astyle '{}' --style=allman --indent=spaces=2 --pad-oper --unpad-paren --pad-header --convert-tabs \;
```



For similar fixes in Python, try
[pep8ify](https://github.com/spulec/pep8ify). Example:



```
sudo pip install pep8ify
pep8ify -nw .
```



When using automated tools to manipulate source code, it's best to push
changes made by the tool as their own commit, distinct from any manual
changes made afterward. Since an automated change can be large and
difficult to review, this ensures that everyone can reproduce the change
locally, including on other branches if necessary for a merge.

Should you have the need to disable specific warnings, the linter filter
can be modified. You will need to update your CMakeLists.txt. Example:



```
set(ROSLINT_CPP_OPTS "--filter=-runtime/references,-runtime/int")
roslint_cpp()
set(ROSLINT_PYTHON_OPTS "--max-line-length=180")
roslint_python()
```



You can also disable cpplint for a particular line only:



```
// There's just no other way; I don't control the location of this header.
#include "my_silly_header.h"  // NOLINT(build/include)
```
