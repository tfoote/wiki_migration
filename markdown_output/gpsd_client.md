

## Tutorials

- [Configuring a Trimble AgGPS Receiver](#configuring-a-trimble-aggps-receiver):
  Trimble AgGPS configuration requirements for interoperability with
  gpsd_client
- [Getting Started with gpsd_client (C++)](#getting-started-with-gpsd_client-c):
  Detailed tutorial for running gpsd_client in ROS
- [Writing a Subscriber for gpsd_client (C++)](#writing-a-subscriber-for-gpsd_client-c):
  This tutorial illustrates a sample code in C++ to get gps data using
  gpsd_client. We use class methods to bring the gps data to the main
  function.

## Configuring a Trimble AgGPS Receiver

- **Description:** Trimble AgGPS configuration requirements for
  interoperability with gpsd_client
- **Keywords:** Trimble, Trimble AgGPS, AgGPS, GPS, gpsd, gpsd_client,
  gps

In order for a Trimble AgGPS262 or similar AgGPS receiver to operate
correctly with gpsd_client the receiver has to be configured properly.

STEP 1: Connect the proprietary serial cable to a windows system and
launch AG Remote software. If you need this software you can find it
here:
<http://www.trimble.com/support_trl.asp?pt=AgRemote&Nav=Collection-1545>

STEP 2: Once you are connected to the receiver you need to modify the
list of active NMEA sentences to match the following list. Active NMEA
senstences are indicated by being displayed with ALL CAPITAL LETTERS
whereas inactive NMEA sentences are displayed in all lowercase letters.

List of NMEA sentences that need to be active on the port (either PORTA
or PORTB) that is connected to the ROS system:

Note: Instructions on navigating the menu structure and setting these
modes properly can be found in the applicable AgGPS user manual for your
specific receiver.

1\. RMC 2. GGA 3. GSA 4. GSV 5. GST 6. MSS

Aside from the specific NMEA sentence settings, I would recommend that
the GPS receiver port (Either PORTA or PORTB) be configured as follows,

Input Protocol: TSIP Baud: 38400 Output Protocol: NMEA Baud: 38400

Note: Your success may vary. After hours of playing with various
settings on the receiver I was finally able to receive valid result via
"rostopic echo /gps" after setting up my receiver as above.

## Getting Started with gpsd_client (C++)

- **Description:** Detailed tutorial for running gpsd_client in ROS
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Writing a Subscriber for gpsd_client (C++)](#writing-a-subscriber-for-gpsd_client-c)

### Hardware Requirements

This tutorial has been tested with the following devices:

- Garmin 18-18x, 1-5hz LVC (serial connection)

### Installation

Start by installing the [gpsd](http://gpsd.berlios.de/) package.



```
$ sudo apt-get install gpsd
```

 Now, in order to install the gpsd_client for
ROS you should install the revision control tool git,



```
$ sudo apt-get install git-core
```

 To install the stack containing gpsd_client we
suggest the path given by */opt/ros/boxturtle/stacks*, but this is left
to the preferences of the user. Once you are located in your chosen
folder type,



```
$ sudo git clone git://ram.umd.edu/ros/gps_umd.git
```

 It will download all the stack to the
designated folder. Once this is done move to the directory where the
gpsd_client package is located,



```
$ roscd gpsd_client
```

 If for some reason this does not work, move to
the gpsd_client folder through the following path:

*/\[your_chosen folder\]/umd-ros-pkg/gps_umd/gpsd_client*

and proceed to compile the package



```
$ sudo rosmake --rosdep-install
```

 Now, the gpsd_client node should be ready to
use. If you get some error messages while compiling the package be sure
that the dependencies were compiled before, specially the
[gps_common](https://index.ros.org/p/gps_common) package.

#### Optional Packages

As an option we can install the gpsd-clients and python-gps packages
which provide tools (*e.g.* gpscat, cgps, xgps) to test the
communication with the GPS through the serial port as explained in the
optional section 1.4.



```
$ sudo apt-get install gpsd-clients python-gps
```



### Physical Connections

Be sure that your Garmin 18-18x GPS is correctly attached to a serial
port and powered on.

### Optional: Testing the GPS with gpscat

If you want to check the actual data transmitted by the GPS you can use
[gpscat](http://gpsd.berlios.de/gpscat.html).



```
$ gpscat -s [baudrate] [serial_port]
```

 The baud rate changes depending on the GPS
model you are using, so we suggest to try different values (*e.g.* 1200,
4800, 9600, 19200).

Using a Garmin 18 (5 hz) GPS we should receive
[NMEA](http://www.gpsinformation.org/dale/nmea.htm) data typing the
following command,



```
$ gpscat -s 19200 /dev/ttyS1
```

 The
[NMEA](http://www.gpsinformation.org/dale/nmea.htm) messages should
appear on the terminal as follows,



```
$GPRMC,002454,A,3553.5295,N,13938.6570,E,0.0,43.1,180700,7.1,W,A*3F
$GPRMB,A,,,,,,,,,,,,A,A*0B
$GPGGA,002454,3553.5295,N,13938.6570,E,1,05,2.2,18.3,M,39.0,M,,*7F
$GPGSA,A,3,01,04,07,16,20,,,,,,,,3.6,2.2,2.7*35
$GPGSV,3,1,09,01,38,103,37,02,23,215,00,04,38,297,37,05,00,328,00*70
$GPGSV,3,2,09,07,77,299,47,11,07,087,00,16,74,041,47,20,38,044,43*73
$GPGSV,3,3,09,24,12,282,00*4D
$GPGLL,3553.5295,N,13938.6570,E,002454,A,A*4F
$GPBOD,,T,,M,,*47
$PGRME,8.6,M,9.6,M,12.9,M*15
$PGRMZ,51,f*30
$HCHDG,101.1,,,7.1,W*3C
$GPRTE,1,1,c,*37
$GPRMC,002456,A,3553.5295,N,13938.6570,E,0.0,43.1,180700,7.1,W,A*3D
```

 You should receive NMEA data from the GPS even
if it has not got any signal from the satellites.

### Using gpsd_client for ROS

As mentioned at the gpsd_client web site,
the [gpsd](http://gpsd.berlios.de/) daemon should be running before the
gpsd_client node is running. To run the [gpsd](http://gpsd.berlios.de/)
daemon type,



```
$ gpsd -S [TCP_port] [serial_port]
```

 The default TCP port is 2947.

In this tutorial we will use the TCP port 4000 and the serial port
*/dev/ttyS1* as before.



```
$ gpsd -S 4000 /dev/ttyS1
```

 We can check that the data from the GPS is now
going through the TCP port 4000 by typing



```
$ telnet localhost 4000
```

 Afterwards press any key and you should start
visualizing NMEA data on the screen.

Now, we are ready to run the MASTER node,



```
$ roscore
```

 and the gpsd_client node,



```
$ rosrun gpsd_client gpsd_client _host:=localhost _port:=4000
```



### Testing the Node

Now, we are ready to test the node



```
$ rostopic echo /fix
```

 We should be able to see the actual ROS
messages from the GPS on the terminal.

## Writing a Subscriber for gpsd_client (C++)

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Getting Started with gpsd_client (C++)](#getting-started-with-gpsd_client-c),
  [Beginner Level Tutorials](ROS/Tutorials) and
  [Publishers and Subscribers](https://index.ros.org/p/roscpp).
- **Description:** This tutorial illustrates a sample code in C++ to get
  gps data using gpsd_client. We use class methods to bring the gps data
  to the main function.
- **Tutorial Level:** INTERMEDIATE

### Hardware Requirements

This tutorial has been tested with the following devices:

- Garmin 18-18x, 1-5hz LVC (serial connection)

### Preliminary Set-Up

Be sure that your GPS is properly connected and working.

Please follow the steps indicated in section 1.5 of
[Getting Started with gpsd_client (C++)](#getting-started-with-gpsd_client-c).

### Creating the Package

Let us start creating a new package for our application called
*gps_test_pkg* which should depend on the package *gpsd_client*,



```
$ sudo roscreate-pkg gps_test_pkg gpsd_client
```



### The Code

Now, go to the main folder of the gps_test-pkg package,



```
$ roscd gps_test_pkg
```



and create the *src* folder,



```
$ mkdir src
```



Use your favorite text editor to create a file named *gpsTest.cpp* and
copy and paste the following C++ code on it.



```
// Originally located at:
// http://controls.ece.unm.edu/documents/gpsTest.cpp
#include <iostream>
#include <ros/ros.h>
#include <gps_common/GPSFix.h>

class GpsTest
{
public:
  // Type for GPS messages
  gps_common::GPSFix gpsMsg;

  // Constructor
  GpsTest(ros::NodeHandle nh_) : n(nh_)
  {
    // Subscribing to the topic /fix
    gps_sub = n.subscribe("/fix", 100, &GpsTest::gpsCallback, this);
  }

  // Callback Function for the GPS
  void gpsCallback(const gps_common::GPSFixConstPtr &msg)
  {
    gpsMsg = *msg;
  }

private:
  // Nodehandle
  ros::NodeHandle n;

  // Subscriber
  ros::Subscriber gps_sub;
};

int main(int argc, char** argv)
{
  // Variables to store the Latitude and Longitude from the GPS respectively
  double gpsLat = 0;
  double gpsLong = 0;

  // Initializing the node for the GPS
  ros::init(argc, argv, "gps_Subscriber");
  ros::NodeHandle nh_;

  GpsTest *p = new GpsTest(nh_);

  // Getting the data from the GPS
  gpsLong = p->gpsMsg.longitude;
  gpsLat = p->gpsMsg.latitude;

  std::cout << "Current Latitude: " << gpsLat << std::endl;
  std::cout << "Current Longitude " << gpsLong << std::endl;

  ros::spin();
  return 0;
}
```



### Compiling the Package

Now, go to the main folder of the package and use your favorite text
editor to add the following line to the *CMakeList.txt* file,



```
rosbuild_add_executable(gpsTest src/gpsTest.cpp)
```



Now, proceed to compile the package



```
$ sudo rosmake --rosdep-install
```



### Running the Node

Now, you should be able to run the node



```
$ rosrun gps_test_pkg gpsTest
```



and visualize the latitude and longitude given by the GPS on the
terminal.

### The Code Explained

Let us put the code in pieces to make it clear.

This section is for including the necessary C++ libraries and packages.



```
#include <iostream>
#include <ros/ros.h>
#include <gps_common/GPSFix.h>
```



In this part of the code we are declaring a class containing all the
functions and variables we need to subscribe to the topic containing the
GPS data.



```
class GpsTest
{
```



Here we start declaring the public attributes of the class. The variable
*gpsMsg* stores the GPS data so we can access it from the main function.



```
public:
  // Type for GPS messages
  gps_common::GPSFix gpsMsg;
```



In this case the constructor of the class is the function which allows
us to encapsulate the subscriber *gps_sub*. We subscribe the node to the
/fix topic using a callback of type *class method* (check section 2.3.2
at [Publishers and Subscribers](https://index.ros.org/p/roscpp)). Since
we are encapsulating the node handle *n* we pass the nodehandle *nh_*
from the main function via member initializers to the constructor. The
colon (:) in the header separates the input parameter from the member
initializer.



```
// Constructor
GpsTest(ros::NodeHandle nh_) : n(nh_)
{
  // Subscribing to the topic /fix
  gps_sub = n.subscribe("/fix", 100, &GpsTest::gpsCallback, this);
}
```



This is the callback signature (check section 2.2 at
[Publishers and Subscribers](https://index.ros.org/p/roscpp)) for the
callback associated to the GPS. Notice that this callback puts the
information data from the GPS in the public variable *gpsMsg*.



```
// Callback Function for the GPS
void gpsCallback(const gps_common::GPSFixConstPtr &msg)
{
  gpsMsg = *msg;
}
```



We encapsulate the nodehandle n and the subscriber gps_sub by declaring
them *private* variables in the class.



```
private:
  // Nodehandle
  ros::NodeHandle n;

  // Subscriber
  ros::Subscriber gps_sub;
};
```



Here is where the main function starts.



```
int main(int argc, char** argv)
{
```



This section initializes the node with the label *gps_Subscriber* and
declares the nodehandle nh_.



```
// Initializing the node for the GPS
ros::init(argc, argv, "gps_Subscriber");
ros::NodeHandle nh_;
```



the **new** operator assigns a storage of the proper size for the object
*p* of type GpsTest by calling the constructor to initialize the object
and returning a pointer to the type GpsTest.



```
GpsTest *p = new GpsTest(nh_);
```



We use the arrow (*->*) operator to access the member *gpsMsg* of the
class *GpsTest* to get the latitude and longitude values from the GPS.
We proceed to show the data on the terminal by using the conventional
*std::cout* commands in lines 59 and 60. Finally the ros::spin command
waits for new messages from the GPS to run the callback.



```
// Getting the data from the GPS
gpsLong = p->gpsMsg.longitude;
gpsLat = p->gpsMsg.latitude;

std::cout << "Current Latitude: " << gpsLat << std::endl;
std::cout << "Current Longitude " << gpsLong << std::endl;

ros::spin();
return 0;
}
```



For a list of the available data given by the gps_common/GPSFix messages
besides latitude and longitude, check
[gps_common/GPSFix](http://www.ros.org/doc/api/gps_common/html/msg/GPSFix.html).
