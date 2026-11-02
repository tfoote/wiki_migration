## Overview

Provides a templatised c++ parser for handling command line arguments.
The templates provide a very flexible manner for handling any type of
input argument.

The code for the command line parser is a simple wrapper around another
template header library called [TCLAP](http://tclap.sourceforge.net/).
Since it is relatively small, its bundled here in the command_line
subdirectory and namespaced in a convenient manner.

### Alternatives

A more complicated, but more flexible alternative (it allows argument
parsing from both command line and configuration file simultaneously) is
the `boost::program_options` library.

## Compiling & Linking

Include the following at the top of any translation unit:



```cplusplus
#include <ecl/command_line.hpp>

// Interface classes
using ecl::CmdLine;
using ecl::ArgException
// Argument classes
using ecl::SwitchArg;
using ecl::ValueArg;
using ecl::MultiArg;
using ecl::UnlabeledValueArg;
using ecl::UnlabeledMultiArg; // there are more - see tclap docs
```



## Tutorials

- [Command Line Parsing with TCLAP](#command-line-parsing-with-tclap)

## Examples

- `src/examples/command_line.cpp`.

## Command Line Parsing with TCLAP

For a more detailed tutorial, visit the
[TCLAP documentation](http://tclap.sourceforge.net/). Some common use
cases are outlined below.

### Initialisation

A single object is used to parse the command line. Initialise it with a
few default properties. These will be used to automatically generate a
\--help argument.



```cplusplus
// Supply a program description, argument separator (optional) and version number (optional).
CmdLine cmd("This is a test program to test the command line parsing facilities provided by TCLAP.");
// CmdLine cmd("This is a test program to test the command line parsing facilities provided by TCLAP.", ' ', "0.01");
```



### Adding Arguments

Valid argument types include:

- `ecl::SwitchArg` : simple boolean.
- `ecl::ValueArg` : expect some value on the command line.
- `ecl::MultiArg` : permit multiple values for an argument which get
  stored in a vector.
- `ecl::MultiSwitchArg` : as above, but for booleans
- `ecl::UnlabeledValueArg` : does not use a flag (like the arguments
  for copy), order is important!
- `ecl::UnlabeledMultiArg` : reads in all remaining unlabelled args
  (like rm file1.txt file2.txt etc.)

#### Toggles/Switches



```cplusplus
// Add a boolean (flag, name, description, default)
SwitchArg debug("d","debug","Enable debugging.", false);
cmd.add(debug);
```



You would call the above program (supposing it has name `foo`):



```
> foo -d false
```



#### Labelled



```cplusplus
// Add a boolean (flag, name, description, default)
SwitchArg debug("d","debug","Enable debugging.", false);
cmd.add(debug);

// Add an integer 
// (flag,name,description,compulsory flag,default value,type hint")
ValueArg<int> intArg("t","test","An integer argument for testing.",false,5,"integer");

cmd.add(intArg);
```



Custom ValueArg types can be used so long as they implement the >>
operator.



```
> foo --test 3
```



#### Unlabelled

These are unlabelled (like what you do with `cp my_file_here
my_file_there`).



```cplusplus
// Not a regular option (name,description,compulsory flag,default value,type hint")
UnlabeledValueArg<std::string> outputDirArg("output_dir","Output directory for rectified images.",true,"./rectified","string");
cmd.add(outputDirArg);
```





```
> foo /home/snorri/images
```



### Parsing the Arguments



```cplusplus
cmd.parse(argc,argv);
bool debug = debugSwitch.getValue();
int test = testArg.getValue();
std::String output_dir = outputDirArg.getValue();
```



### Allowing ROS to Pass

If you want to add your command line parsing program to a roslaunch,
you'll need to let it know what it needs to parse and what it needs to
pass\... This can be achieved by the `\--` argument (literally means,
'ignore the rest'). An example:



```highlight
    <node name="service_relay" pkg="foo" type="service_relay" args="-r 2 --">
        <remap from="service_relay/foo" to="/bar"/>
    </node>
```



Alternatively you can prune the ros args before they get to the command
line parser in the code itself:



```highlight

#include <ros/init.h>

// ....

std::vector<std::string> myargs;
ros::removeROSArgs(argc, argv, myargs);
char** myargv = new char*[myargs.size()]; //array to emulate argv.
for(int i = 0, ie = myargs.size(); i < ie; ++i)
{
  myargv[i] = const_cast<char*>(myargs[i].data());
}
cmd.parse(myargs.size(), myargv);
```

## Tutorials

- [Command Line Parsing with TCLAP](#command-line-parsing-with-tclap):
  Introduction to command line parsing with TCLAP.
