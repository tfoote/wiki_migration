```wiki
Notice: This package is unsupported on recent versions of ROS. If you're writing a ROS driver which interfaces with serial hardware, consider using [[http://wjwwood.io/serial/|serial]].
```

## Documentation

This package was design to make life easier when developing drivers for
ROS. cereal_port includes various methods for reading data from a serial
port, including threaded streaming. To start using cereal_port check out
the [Code API.](http://www.ros.org/doc/api/cereal_port/html/)

## Example

The following example shows how to use the cereal_port library in your
ROS projects. This example in particular opens a serial port sends an
'R' and waits for a reply.

```cplusplus
#include <ros/ros.h>
#include <cereal_port/CerealPort.h>

#define REPLY_SIZE 8
#define TIMEOUT 1000

// This example opens the serial port and sends a request 'R' at 1Hz and waits for a reply.
int main(int argc, char** argv)
{
    ros::init(argc, argv, "example_node");
    ros::NodeHandle n;

    cereal::CerealPort device;
    char reply[REPLY_SIZE];

    // Change the next line according to your port name and baud rate
    try{ device.open("/dev/ttyUSB0", 9600); }
    catch(cereal::Exception& e)
    {
        ROS_FATAL("Failed to open the serial port!!!");
        ROS_BREAK();
    }
    ROS_INFO("The serial port is opened.");

    ros::Rate r(1);
    while(ros::ok())
    {
        // Send 'R' over the serial port
        device.write("R");

        // Get the reply, the last value is the timeout in ms
        try{ device.read(reply, REPLY_SIZE, TIMEOUT); }
        catch(cereal::TimeoutException& e)
        {
            ROS_ERROR("Timeout!");
        }
        ROS_INFO("Got this reply: %s", reply);

        ros::spinOnce();
        r.sleep();
    }
}
``` To compile this example.cpp file you should
make sure you have the serial_communication stack installed and don't
forget to add cereal_port as a dependency on your package manifest.xml:

```
...
  <depend package="cereal_port" />
``` Add the following lines to your pkg
CMakeList.txt in order to get your code to compile:

```
rosbuild_add_executable(example_node src/example.cpp)
target_link_libraries(example_node cereal_port)
```

## Current state

Although it is obsolete and not recommended for usage in new proejcts,
it might be required by legacy code and thus package.xml and
CMakeLists.txt were updated in a refreshed project to meet modern
requirements.

The refreshed projeect is available at
<https://github.com/NetBUG/cereal_port>

## Tutorials

Coming soon\...
