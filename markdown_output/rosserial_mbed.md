This package contains Mbed-specific extensions required to run
[rosserial_client](https://index.ros.org/p/rosserial_client) on an
[Mbed compatible platform](https://developer.mbed.org/platforms/). It is
meant to demonstrate how easy it is to integrate custom hardware and
cheap sensors into your ROS project using an
[Mbed](https://www.mbed.com/en/). The Tutorials of this package will
walk you through a setting up your Mbed environment, creating a few
example programs and explain where to purchase the additional hardware.

## Tutorials

- [Blink (example subscriber)](#blink-example-subscriber):
  This tutorial shows step by step how to use rosserial with
  subscribers.
- [Buzzer Module](#buzzer-module):
  This tutorial will cover the use of an Mbed with a Buzzer Module.
- [Collision Sensor](#collision-sensor):
  In this tutorial, we will use a Mbed and a Collision Sensor Module.
- [DHT Humidity and Temperature Sensor](#dht-humidity-and-temperature-sensor):
  In this tutorial, we will use a Mbed and a DHT Humidity and
  Temperature Sensor.
- [Hello World (example publisher)](#hello-world-example-publisher):
  This tutorial shows step by step how to create a publisher using
  rosserial.
- [IR Ranger Tutorial](#ir-ranger-tutorial):
  Using an IR Ranger with rosserial and an MBED
- [MBED Oscilloscope](#mbed-oscilloscope):
  In this tutorial, we will be making a poor man's oscilloscope using
  the MBED's ADC (analog to digital converter) and rqt_plot.
- [Maxbotix Ultrasonic Ranger](#maxbotix-ultrasonic-ranger):
  In this tutorial, we will use an MBED and a Maxbotix Ultrasonic Range
  Finder.
- [Temperature Sensor](#temperature-sensor):
  Measuring Temperature using the TMP102
- [Motor Shield Example](#motor-shield-example):
  In this tutorial, we will use a Mbed and a Motor Controller Shield
- [PIR Motion Sensor](#pir-motion-sensor):
  This tutorial shows an example for using an Mbed with a PIR Motion
  Sensor.
- [Push Button](#push-button):
  Monitor a push button and publish its state in ROS
- [SRF08 Ultrasonic Ranger](#srf08-ultrasonic-ranger):
  In this tutorial, we will use a Mbed and a
  [SRF08 Ultrasonic Ranger](http://www.acroname.com/robotics/parts/R145-SRF08.html)
  as a Range Finder.The SRF08 communicates with the Mbed over SPI/I2C.
- [Servo Controller Example](#servo-controller-example):
  Tutorial for controlling an R/C servo with rosserial and an MBED
- [Using Time and TF](#using-time-and-tf):
  This tutorial shows how to use ros::Time and TF to create a tf
  publisher on MBED.
- [Using rosserial with Inforce MBED PAC Shield](#using-rosserial-with-inforce-mbed-pac-shield):
  This tutorial show how to use rosserial_mbed with the Inforce 6410
  plus + PAC Shield
- [rosserial MBED Setup](#rosserial-mbed-setup):
  This tutorial shows how to configure a basic development environment
  to use rosserial_mbed with an enabled MBED board

## Blink (example subscriber)

- **Description:** This tutorial shows step by step how to use rosserial
  with subscribers.
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Using Time and TF](#using-time-and-tf)

### Blink: Creating a Subscriber

#### The Code

Now that we've created a ROS publisher in the
[previous tutorial](#hello-world-example-publisher),
we'll create a subscriber.

Open the Blink example placed on your previously downloaded
rosserial/rosserial_mbed/examples directory, and open the `Blink.cpp`
file in your favorite text editor:



```cplusplus
/*
 * rosserial Subscriber Example
 * Blinks an LED on callback
 */
#include "mbed.h"
#include <ros.h>
#include <std_msgs/Empty.h>

ros::NodeHandle nh;
DigitalOut myled(LED1);

void messageCb(const std_msgs::Empty& toggle_msg){
    myled = !myled;   // blink the led
}

ros::Subscriber<std_msgs::Empty> sub("toggle_led", &messageCb);

int main() {
    nh.initNode();
    nh.subscribe(sub);

    while (1) {
        nh.spinOnce();
        wait_ms(1);
    }
}
```



#### The Code Explained

Now, let's break the code down. We need to include the `mbed.h` for
every MBED program. As before, we need to include the `ros.h` as with
any other ROS MBED program. We also include the header files for
messages, in this case, the `Empty` message. Next, we need to
instantiate the node handle, which allows our program to create
publishers and subscribers. The node handle also takes care of serial
port communications. We then create the callback function for our
subscriber. The call back function must take a constant reference of a
message as its argument. In our callback `messageCb`, the type of
message is `std_msgs::Empty` and the message name will be
`toggle_msg`.

Inside our callback, we could reference `toggle_msg`, but since it is
empty, there is no need to. We just blink the LED on the MBED board
every time we receive a message. We need to instantiate the publishers
and subscribers that we will be using. Here we instantiate a Subscriber
with a topic name of "toggle_led" and type `std_msgs::Empty`. With
Subscribers, you must remember to template the subscriber upon the
message. Its two arguments are the topic it will be subscribing to and
the callback function it will be using. In the main function you need to
initialize your ROS node handle, advertise any topics being published,
and subscribe to any topics you wish to listen to. Finally, inside the
main function there's a loop in which we call ros::spinOnce() where all
of the ROS communication callbacks are handled. We don't need to do any
additional processing in the `loop()`, since ros::spinOnce() will
handle passing messages to the subscriber callback.

### Compiling and uploading the Code

As seen on the previous tutorial, you must compile the source code by
using the makefile in order to generate the .bin file that will be
uploaded later to your MBED board. This is no different from uploading
any other mbed binary.

#### Running the Code

Now, launch the [roscore](roscore) in a new terminal window:



```
roscore
```

 Next, run the rosserial client application that
forwards your MBED messages to the rest of ROS. Make sure to use the
correct serial port:



```
rosrun rosserial_python serial_node.py /dev/ttyACM0
```

 Finally, you can toggle the LED using
[rostopic](https://index.ros.org/p/rostopic):



```
rostopic pub toggle_led std_msgs/Empty --once
```



### Further Reading

Please see [rosserial/Overview](https://index.ros.org/p/rosserial) for
more information on publishers and subscribers. Also see
[limitations](https://index.ros.org/p/rosserial) for information about
more complex data types.

## Buzzer Module

- **Description:** This tutorial will cover the use of an Mbed with a
  Buzzer Module.
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Collision Sensor](#collision-sensor)

[rosserial](https://index.ros.org/p/rosserial) allows you to easily
integrate Mbed-based hardware with ROS. This tutorial will explain how
to use a Buzzer Module with a Mbed.

You will need an [Mbed](https://developer.mbed.org/platforms), a
[Buzzer](http://www.seeedstudio.com/depot/Grove-Buzzer-p-768.html), and
a way to connect your Buzzer to your Mbed such as a breadboard,
protoboard or
[Grove Base Shield](http://www.seeedstudio.com/depot/base-shield-v13-p-1378.html?cPath=132_134).

### The Code

Open the Buzzer example placed on your previously downloaded
rosserial/rosserial_mbed/examples directory, and open the Buzzer.cpp
file in your favorite text editor:



```cplusplus
/*
 * rosserial Buzzer Module Example
 *
 * This tutorial demonstrates the usage of the
 * Seeedstudio Buzzer Grove module
 * http://www.seeedstudio.com/depot/Grove-Buzzer-p-768.html
 *
 * Source Code Based off of:
 * https://developer.mbed.org/teams/Seeed/code/Seeed_Grove_Buzzer/
 */

#include "mbed.h"
#include <ros.h>
#include <std_msgs/Float32MultiArray.h>

ros::NodeHandle  nh;

#ifdef TARGET_LPC1768
PwmOut buzzer(p21);
#elif defined(TARGET_KL25Z) || defined(TARGET_NUCLEO_F401RE)
PwmOut buzzer(D2);
#else
#error "You need to specify a pin for the sensor"
#endif

Timeout toff;
bool playing = false;
DigitalOut led(LED1);

void nobeep() {
    buzzer.write(0.0);
    led = 1;
    playing = false;
}
void beep(float freq, float time) {
    buzzer.period(1.0/freq);
    buzzer.write(0.5);
    toff.attach(nobeep, time);
    led = 0;
}

void messageCb(const std_msgs::Float32MultiArray& msg){
    if(!playing){
        playing = true;
        // msg.data[0] - Note
        // msg.data[1] - duration in seconds
        beep(msg.data[0], msg.data[1]);
    }
}

ros::Subscriber<std_msgs::Float32MultiArray> sub("buzzer", &messageCb);

int main() {
    buzzer = 0;
    led = 1;
    nh.initNode();
    nh.subscribe(sub);
    while (1) {
        nh.spinOnce();
        wait_ms(1);
    }
}
```



### Compiling and uploading the Code

As seen on the previous tutorial, you must compile the source code by
using the makefile in order to generate the .bin file that will be
uploaded later to your MBED board. This is no different from uploading
any other mbed binary.

### Launching the App

Launch roscore 

```
roscore
```



Run the serial node with the right serial port corresponding to your
MBED board 

```

```

}}} 

```

```

}}}

Finally, you must publish the pitches by following this
[Reference pitches](https://www.arduino.cc/en/Tutorial/ToneMelody?action=sourceblock&num=2)
and duration (in seconds). 

```
$ rostopic pub /buzzer std_msgs/Float32MultiArray "{46, 2}"
```

## Collision Sensor

- **Description:** In this tutorial, we will use a Mbed and a Collision
  Sensor Module.
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [PIR Motion Sensor](#pir-motion-sensor)

[rosserial](https://index.ros.org/p/rosserial) allows you to easily
integrate Mbed-based hardware with ROS. This tutorial will explain how
to use a Collision Sensor Module with a Mbed.

You will need an [Mbed](https://developer.mbed.org/platforms), a
[Collision Sensor](http://www.seeedstudio.com/depot/Grove-Collision-Sensor-p-1132.html),
and a way to connect your Sensor to your Mbed to your Mbed such as a
breadboard, protoboard or
[Grove Base Shield](http://www.seeedstudio.com/depot/base-shield-v13-p-1378.html?cPath=132_134).

### The Code

Open the Collision Sensor example placed on your previously downloaded
rosserial/rosserial_mbed/examples directory, and open the
GroveCollision.cpp file in your favorite text editor:



```cplusplus
/*
 * rosserial collision sensor
 *
 * This tutorial demonstrates the usage of the
 * Seeedstudio Collision Grove Sensor
 * http://www.seeedstudio.com/wiki/Grove_-_Collision_Sensor
 */

#include "mbed.h"
#include <ros.h>
#include <std_msgs/Bool.h>

ros::NodeHandle  nh;

std_msgs::Bool collision_msg;
ros::Publisher pub_collision("collision", &collision_msg);


Timer t;
#ifdef TARGET_LPC1768
DigitalIn sig1(p9);
#elif defined(TARGET_KL25Z) || defined(TARGET_NUCLEO_F401RE)
DigitalIn sig1(D6);
#else
#error "You need to specify a pin for the sensor"
#endif

int main() {
    t.start();

    nh.initNode();
    nh.advertise(pub_collision);

    long publisher_timer = 0;

    while (1) {

        if (t.read_ms() > publisher_timer) {
            collision_msg.data = !sig1;
            pub_collision.publish(&collision_msg);
            publisher_timer = t.read_ms() + 1000;
        }
        nh.spinOnce();
    }
}
```



### Compiling and uploading the Code

As seen on the previous tutorial, you must compile the source code by
using the makefile in order to generate the .bin file that will be
uploaded later to your MBED board. This is no different from uploading
any other mbed binary.

### Launching the App

Launch roscore 

```
$ roscore
```



Run the serial node with the right serial port corresponding to your
MBED board 

```

```

}}} 

```

```

}}}

Now watch the sensor's value on the pushed topic



```
$ rostopic echo collision
```

## DHT Humidity and Temperature Sensor

- **Description:** In this tutorial, we will use a Mbed and a DHT
  Humidity and Temperature Sensor.
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Motor Shield Example](#motor-shield-example)

[rosserial](https://index.ros.org/p/rosserial) allows you to easily
integrate Mbed-based hardware with ROS. This tutorial will explain how
to use a DHT Humidity and Temperature Sensor with an Mbed.

You will need an [Mbed](https://developer.mbed.org/platforms), a
[Humidity and Temperature Sensor](http://www.seeedstudio.com/depot/Grove-TempHumi-Sensor-p-745.html),
and a way to connect your Sensor to your Mbed to your Mbed such as a
breadboard, protoboard or
[Grove Base Shield](http://www.seeedstudio.com/depot/base-shield-v13-p-1378.html?cPath=132_134).

### The Code

Open the Humidity and Temperature Sensor example placed on your
previously downloaded rosserial/rosserial_mbed/examples directory, and
open the GrovePIRMotionSensor.cpp file in your favorite text editor:



```cplusplus
/*
 * rosserial Temperature and Humidity Sensor Example
 *
 * This tutorial demonstrates the usage of the
 * Seeedstudio Temperature and Humidity Grove module
 * http://www.seeedstudio.com/wiki/Grove_-_Temperature_and_Humidity_Sensor
 *
 * Source Code Based of:
 * https://developer.mbed.org/teams/Seeed/code/Seeed_Grove_Temp_Humidity_Example/
 */

#include "mbed.h"
#include "DHT.h"
#include <ros.h>
#include <sensor_msgs/Temperature.h>
#include <sensor_msgs/RelativeHumidity.h>

ros::NodeHandle  nh;

sensor_msgs::Temperature temp_msg;
sensor_msgs::RelativeHumidity humidity_msg;
ros::Publisher pub_temp("temperature", &temp_msg);
ros::Publisher pub_humidity("humidity", &humidity_msg);

Timer t;
#ifdef TARGET_LPC1768
DHT sensor(p9, AM2302);
#elif defined(TARGET_KL25Z) || defined(TARGET_NUCLEO_F401RE)
DHT sensor(D6, AM2302);
#elif defined(TARGET_NUCLEO_F401RE)
DHT sensor(A6, AM2302);
#else
#error "You need to specify a pin for the sensor"
#endif

int main()
{
  int error = 0;
  t.start();

  nh.initNode();
  nh.advertise(pub_temp);
  nh.advertise(pub_humidity);

  long publisher_timer = 0;
  temp_msg.header.frame_id = "/base_link";
  humidity_msg.header.frame_id = "/base_link";

  while (1)
  {

    if (t.read_ms() > publisher_timer)
    {
      error = sensor.readData();
      if (0 == error)
      {
        temp_msg.temperature = sensor.ReadTemperature(CELCIUS);
        temp_msg.header.stamp = nh.now();
        pub_temp.publish(&temp_msg);

        humidity_msg.relative_humidity = sensor.ReadHumidity();
        humidity_msg.header.stamp = nh.now();
        pub_humidity.publish(&humidity_msg);
      }
      publisher_timer = t.read_ms() + 1000;
    }
    nh.spinOnce();
  }
}
```



### Compiling and uploading the Code

As seen on the previous tutorial, you must compile the source code by
using the makefile in order to generate the .bin file that will be
uploaded later to your MBED board. This is no different from uploading
any other mbed binary.

### Launching the App

Launch roscore 

```
$ roscore
```



Run the serial node with the right serial port corresponding to your
MBED board 

```

```

}}} 

```

```

}}}

Now watch the sensor's value on the pushed topic



```
$ rostopic echo /temperature
```

 or 

```
$ rostopic echo /humidity
```

## Hello World (example publisher)

- **Description:** This tutorial shows step by step how to create a
  publisher using rosserial.
- **Keywords:** MBED, rosserial, serial
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Blink (example subscriber)](#blink-example-subscriber)

### Hello World: Creating a Publisher

#### The Code

We'll start our exploration into rosserial by creating a "hello
world" program for our MBED. It is included as part of the examples for
the MBED plataform of the rosserial repository.

Open the Hello World example placed on your previously downloaded
rosserial/rosserial_mbed/examples directory, and open the
`HelloWorld.cpp` file in your favorite text editor:



```cplusplus
/*
 * rosserial Publisher Example
 * Prints "hello world!"
 */

#include"mbed.h"
#include <ros.h>
#include <std_msgs/String.h>

ros::NodeHandle  nh;

std_msgs::String str_msg;
ros::Publisher chatter("chatter", &str_msg);

char hello[13] = "hello world!";

DigitalOut led = LED1;

int main() {
    nh.initNode();
    nh.advertise(chatter);

    while (1) {
        led = !led;
        str_msg.data = hello;
        chatter.publish( &str_msg );
        nh.spinOnce();
        wait_ms(1000);
    }
}
```





```wiki
If you're using the official online compiler you can import this program using this [[https://developer.mbed.org/users/garyservin/code/rosserial_mbed_hello_world_publisher/|link]].
```



#### The Code Explained

Now, let's break the code down. As a part of every ROS MBED program,
you need to include the ros.h header file and header files for any
messages that you will be using. Next, we need to instantiate the node
handle, which allows our program to create publishers and subscribers.
The node handle also takes care of serial port communications. We need
to instantiate the publishers and subscribers that we will be using.
Here we instantiate a Publisher with a topic name of "chatter". The
second parameter to Publisher is a reference to the message instance to
be used for publishing. We need to initialize your ROS node handle,
advertise any topics being published, and subscribe to any topics you
wish to listen to. Finally, inside the main function there's a loop,
the node publishes "Hello World" and calls ros::spinOnce() where all
of the ROS communication callbacks are handled, also there's a LED
switching its state for every loop cycle.

#### Compiling and uploading the Code

As seen on the previous tutorial, you must compile the source code by
using the makefile in order to generate the .bin file that will be
uploaded later to your MBED board. This is no different from uploading
any other mbed binary.

#### Running the Code

Now, launch the roscore in a new terminal window:

. 

```
$ roscore
```



Next, run the rosserial client application that forwards your MBED
messages to the rest of ROS. Make sure to use the correct serial port:

. 

```
$ rosrun rosserial_python serial_node.py /dev/ttyACM0
```



Finally, watch the greetings come in from your MBED by launching a new
terminal window and entering :

. 

```
$ rostopic echo chatter
```



#### Further Reading

Please see [rosserial/Overview](https://index.ros.org/p/rosserial) for
more information on publishers and subscribers. Also see
[limitations](https://index.ros.org/p/rosserial) for information about
more complex data types.

## IR Ranger Tutorial

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [rosserial mbed Setup](#rosserial-mbed-setup).
- **Description:** Using an IR Ranger with rosserial and an MBED
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [SRF08 Ultrasonic Range Finder](#srf08-ultrasonic-ranger)

[rosserial](https://index.ros.org/p/rosserial) allows you to easily
integrate mbed-based hardware with ROS. This tutorial will explain how
to use a sharp IR ranger with an mbed.

You will need an MBED board. Additionally, you will need a
[Sharp IR Ranger, Model# GP2D120XJ00F](http://www.sparkfun.com/products/8959),
and a way to connect your IR Ranger to your MBED such as a breadboard or
protoboard.

### Hardware Setup

To get started, connect your ranger to one of your MBED's "analog"
(pwm) pins, the VCC and GND to its respective pins. In the code you can
appreciate the different PIN numbers for three different MBED boards.

### Software Setup

#### The Code

Next, open up your favorite plain text editor and copy in the code
below.



```cplusplus
/*
 * rosserial IR Ranger Example
 *
 * This example is calibrated for the Sharp GP2D120XJ00F.
 */

#include <ros.h>
#include <ros/time.h>
#include <sensor_msgs/Range.h>

ros::NodeHandle  nh;


sensor_msgs::Range range_msg;
ros::Publisher pub_range( "range_data", &range_msg);

#if defined(TARGET_LPC1768)
PinName analog_pin = p20;
#elif defined(TARGET_KL25Z) || defined(TARGET_NUCLEO_F401RE)
PinName analog_pin = A0;
#else
#error "You need to specify a pin for the mic"
#endif

unsigned long range_timer;

/*
 * getRange() - samples the analog input from the ranger
 * and converts it into meters.
 */
float getRange(PinName pin_num) {
    int sample;
    // Get data
    sample = AnalogIn(pin_num).read_u16()/4;
    // if the ADC reading is too low,
    //   then we are really far away from anything
    if(sample < 10)
        return 254;     // max range
    // Magic numbers to get cm
    sample= 1309/(sample-3);
    return (sample - 1)/100; //convert to meters
}

char frameid[] = "/ir_ranger";

Timer t;
int main() {
    t.start();
    nh.initNode();
    nh.advertise(pub_range);

    range_msg.radiation_type = sensor_msgs::Range::INFRARED;
    range_msg.header.frame_id =  frameid;
    range_msg.field_of_view = 0.01;
    range_msg.min_range = 0.03;
    range_msg.max_range = 0.4;

    while (1) {
        // publish the range value every 50 milliseconds
        //   since it takes that long for the sensor to stabilize
        if ( (t.read_ms()-range_timer) > 50) {
            range_msg.range = getRange(analog_pin);
            range_msg.header.stamp = nh.now();
            pub_range.publish(&range_msg);
            range_timer =  t.read_ms() + 50;
        }
        nh.spinOnce();
    }
}
```



#### The Code Explained

Now let's break down the code. As always, the code begins by including
the appropriate message headers and `ros.h` from the rosserial library
and then instantiating the publisher. There are some preprocessor
directives for selecting the correct analog pin on three different MBED
boards. Here we define a function that converts the analog signal to a
corresponding distance reading in meters. Here, the code creates a
global variable for the sensors frame id string. It is important to make
this string global so it will be alive for as long as the message will
be in use. In the mbed's main function, the code initializes the node
handle and then fills in the descriptor fields for `range_msg`.
Finally, in the main loop, the MBED samples the ranger once every 50
milliseconds and publishes the range data.

### Launching the App

After you program your mbed, its time to visualize the sensors
measurements using rxplot.



```
roscore
```





```

```

}}} 

```

```

}}}



```
rxplot range_data/range
```

## MBED Oscilloscope

- **Description:** In this tutorial, we will be making a poor man's
  oscilloscope using the MBED's ADC (analog to digital converter) and
  rqt_plot.
- **Keywords:** MBED, rosserial, serial, ADC
- **Tutorial Level:** BEGINNER

In this tutorial, we will be making a poor man's oscilloscope using the
MBED's ADC (analog to digital converter) and rqt_plot. We will set up a
publisher which will forward the analog values from each of the mbed's
6 ADC pins to ROS using rosserial. This will be a relatively bad
oscilloscope (very low sampling frequency and resolution), but it will
be perfect for many quick and dirty setups.

### Custom Message

This code uses a custom message type, the `ADC.msg`. This message has
`uint16` field for each of the analog input pins on the standard mbed.



```
uint16 adc0
uint16 adc1
uint16 adc2
uint16 adc3
uint16 adc4
uint16 adc5
```



This message is a part of the rosserial_mbed package and has been added
to your ros_lib library.

### The Code

The code for this tutorial is fairly straight forward. The code
registers a `Adc` msg publisher, initializes the node handle, and then
tries to publish as many `Adc` messages as possible.



```cplusplus
/*
 * rosserial ADC Example
 *
 * This is a poor man's Oscilloscope.  It does not have the sampling
 * rate or accuracy of a commerical scope, but it is great to get
 * an analog value into ROS in a pinch.
 */

#include "mbed.h"
#include <ros.h>
#include <rosserial_mbed/Adc.h>

#if defined(TARGET_LPC1768)
PinName adc0 = p15;
PinName adc1 = p16;
PinName adc2 = p17;
PinName adc3 = p18;
PinName adc4 = p19;
PinName adc5 = p20;
#elif defined(TARGET_KL25Z) || defined(TARGET_NUCLEO_F401RE)
PinName adc0 = A0;
PinName adc1 = A1;
PinName adc2 = A2;
PinName adc3 = A3;
PinName adc4 = A4;
PinName adc5 = A5;
#else
#error "You need to specify the pins for the adcs"
#endif

ros::NodeHandle nh;

rosserial_mbed::Adc adc_msg;
ros::Publisher p("adc", &adc_msg);


//We average the analog reading to elminate some of the noise
int averageAnalog(PinName pin) {
    int v=0;
    for (int i=0; i<4; i++) v+= AnalogIn(pin).read_u16();
    return v/4;
}

long adc_timer;

int main() {
    nh.initNode();

    nh.advertise(p);

    while (1) {
        adc_msg.adc0 = averageAnalog(adc0);
        adc_msg.adc1 = averageAnalog(adc1);
        adc_msg.adc2 = averageAnalog(adc2);
        adc_msg.adc3 = averageAnalog(adc3);
        adc_msg.adc4 = averageAnalog(adc4);
        adc_msg.adc5 = averageAnalog(adc5);

        p.publish(&adc_msg);

        nh.spinOnce();
    }
}
```



### Running the Oscilloscope



```
roscore
```





```

```

}}} 

```

```

}}}



```
rqt_plot adc/adc0
```



Now, you should see the raw analog value on adc0 displayed in
[rqt_plot](https://index.ros.org/p/rqt_plot). Try connecting ADC0 to
ground, 5V, and 3.3V on your MBED and observing the value. Also notice
that when you don't have anything connected to the ADC, it is a
floating analog input and its value will oscillate randomly.

For example, look at the below output where the ADC0 input is switched
between 5V and gnd. There are wild oscillations during the transition.

![attachment:RXPlot.jpg](doc/RXPlot.jpg)

## Maxbotix Ultrasonic Ranger

- **Description:** In this tutorial, we will use an MBED and a Maxbotix
  Ultrasonic Range Finder.
- **Tutorial Level:** BEGINNER

[rosserial](https://index.ros.org/p/rosserial) allows you to easily
integrate MBED-based hardware with ROS. This tutorial will explain how
to use a Maxbotix Ultrasonic Ranger along with an MBED.

You will need an MBED board, a
[Maxbotix Ultrasonic Ranger](http://maxbotix.com/ultrasonic-sensor-used-in-robot-operating-system-157.htm),
and a way to connect your Ranger to your MBED such as a breadboard or
protoboard.

### The Code

Next, open up your favorite plain text editor and copy in the code
below.



```cplusplus
/*
 * rosserial Ultrasound Example
 *
 * This example is for the Maxbotix Ultrasound rangers.
 */

#include "mbed.h"
#include <ros.h>
#include <ros/time.h>
#include <sensor_msgs/Range.h>

ros::NodeHandle  nh;

sensor_msgs::Range range_msg;
ros::Publisher pub_range( "/ultrasound", &range_msg);

#if defined(TARGET_LPC1768)
const PinName adc_pin = p20;
#elif defined(TARGET_KL25Z) || defined(TARGET_NUCLEO_F401RE)
const PinName adc_pin = A0;
#else
#error "You need to specify a pin for the sensor"
#endif

char frameid[] = "/ultrasound";

float getRange_Ultrasound(PinName pin_num) {
    int val = 0;
    for (int i=0; i<4; i++) val += AnalogIn(pin_num).read_u16();
    float range =  val;
    return range /322.519685;   // (0.0124023437 /4) ; //cvt to meters
}

Timer t;
int main() {
    t.start();
    nh.initNode();
    nh.advertise(pub_range);

    range_msg.radiation_type = sensor_msgs::Range::ULTRASOUND;
    range_msg.header.frame_id =  frameid;
    range_msg.field_of_view = 0.1;  // fake
    range_msg.min_range = 0.0;
    range_msg.max_range = 6.47;

    //pinMode(8,OUTPUT);
    //digitalWrite(8, LOW);

    long range_time=0;

    while (1) {

        //publish the adc value every 50 milliseconds
        //since it takes that long for the sensor to stablize
        if ( t.read_ms() >= range_time ) {
            range_msg.range = getRange_Ultrasound(adc_pin);
            range_msg.header.stamp = nh.now();
            pub_range.publish(&range_msg);
            range_time =  t.read_ms() + 50;
        }

        nh.spinOnce();
    }
}
```



### Compiling and uploading the Code

As seen on the previous tutorial, you must compile the source code by
using the makefile in order to generate the .bin file that will be
uploaded later to your MBED board. This is no different from uploading
any other mbed binary.

### Running the Code

Now, launch the roscore in a new terminal window:



```
roscore
```

 Next, run the rosserial client application that
forwards your mbed messages to the rest of ROS. Make sure to use the
correct serial port:

{ }}}} { }}}} Finally, echo the topic to see the lectures from the
sensor:



```
rostopic echo /ultrasound
```

## Temperature Sensor

- **Description:** Measuring Temperature using the TMP102
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Push Button](#push-button)

In this tutorial, we will use an MBED and a
[TMP102 temperature sensor](http://focus.ti.com/docs/prod/folders/print/tmp102.html)
to measure the ambient temperature in a room. The tutorial's goals are
two fold. The first is to show an example temperature sensing node. The
second is to demonstrate the mbed as an I2C interface for ROS. The
TMP102 is one of many pieces of hardware that use I2C to communicate.
You can now interface SPI/I2C to ROS with ease using an MBED.

### Hardware

For this tutorial, you will need an MBED and a
[TMP102 Breakout board from Sparkfun](http://www.sparkfun.com/products/9418).
This board is a great little temperature sensor that can measure
temperature with a 0.625 degree C resolution. Connecting it to an MBED
is very straightforward. It is a 3.3V sensor communication over I2C so
it connects to the MBED's 3.3V output, GND, SDA, SCL pins. SDA and SCL
are the I2C data line and I2C clock line respectively. They are exposed
on the MBED board as analog pins 4 and 5.

![\|width="500 height=300"](attachment:tmp102.png)

Diagram from [here](http://bildr.org/2011/01/tmp102-mbed)

### Code



```cplusplus
/*
 * rosserial Temperature Sensor Example
 *
 * This tutorial demonstrates the usage of the
 * Sparkfun TMP102 Digital Temperature Breakout board
 * http://www.sparkfun.com/products/9418
 *
 * Source Code Based off of:
 * http://wiring.org.co/learning/libraries/tmp102sparkfun.html
 */

#include "mbed.h"
#include <ros.h>
#include <std_msgs/Float32.h>

ros::NodeHandle  nh;

std_msgs::Float32 temp_msg;
ros::Publisher pub_temp("temperature", &temp_msg);


// From the datasheet the BMP module address LSB distinguishes
// between read (1) and write (0) operations, corresponding to
// address 0x91 (read) and 0x90 (write).
// shift the address 1 bit right (0x91 or 0x90), the Wire library only needs the 7
// most significant bits for the address 0x91 >> 1 = 0x48
// 0x90 >> 1 = 0x48 (72)

int sensorAddress = 0x91 >>1;  // From datasheet sensor address is 0x91
                               // shift the address 1 bit right, the Wire library only needs the 7
                               // most significant bits for the address

Timer t;
#ifdef TARGET_LPC1768
I2C i2c(p9, p10);        // sda, scl
#elif defined(TARGET_KL25Z) || defined(TARGET_NUCLEO_F401RE)
I2C i2c(D14, D15);       // sda, scl
#else
#error "You need to specify a pin for the sensor"
#endif

int main() {
    t.start();

    nh.initNode();
    nh.advertise(pub_temp);

    long publisher_timer =0;

    while (1) {

        if (t.read_ms() > publisher_timer) {
            // step 1: request reading from sensor
            //Wire.requestFrom(sensorAddress,2);
            char cmd = 2;
            i2c.write(sensorAddress, &cmd, 1);

            wait_ms(50);

            char msb;
            char lsb;
            int temperature;
            i2c.read(sensorAddress, &msb, 1); // receive high byte (full degrees)
            i2c.read(sensorAddress, &lsb, 1); // receive low byte (fraction degrees)

            temperature = ((msb) << 4);  // MSB
            temperature |= (lsb >> 4);   // LSB

            temp_msg.data = temperature*0.0625;
            pub_temp.publish(&temp_msg);

            publisher_timer = t.read_ms() + 1000;
        }

        nh.spinOnce();
    }
}
```



### Testing



```
roscore
```





```

```

}}} 

```

```

}}}



```
rostopic echo temperature
```

## Motor Shield Example

- **Description:** In this tutorial, we will use a Mbed and a Motor
  Controller Shield
- **Tutorial Level:** BEGINNER

[rosserial](https://index.ros.org/p/rosserial) allows you to easily
integrate Mbed-based hardware with ROS. This tutorial will explain how
to use a Motor Controller Shield with an Mbed.

You will need an [Mbed](https://developer.mbed.org/platforms), a
[Motor Control Shield](http://www.seeedstudio.com/depot/motor-shield-v20-p-1377.html),
and a way to connect your Sensor to your Mbed such as a breadboard or
protoboard.

### The Code

Open the Motor Shield example placed on your previously downloaded
rosserial/rosserial_mbed/examples directory, and open the
MotorShield.cpp file in your favorite text editor:



```cplusplus
/*
 * rosserial Motor Shield Example
 *
 * This tutorial demonstrates the usage of the
 * Seeedstudio Motor Shield
 * http://www.seeedstudio.com/depot/motor-shield-v20-p-1377.html
 *
 * Source Code Based on:
 * https://developer.mbed.org/teams/shields/code/Seeed_Motor_Shield/
 */

#include "mbed.h"
#include "MotorDriver.h"
#include <ros.h>
#include <geometry_msgs/Twist.h>

#ifdef TARGET_LPC1768
#define MOTORSHIELD_IN1     p21
#define MOTORSHIELD_IN2     p22
#define MOTORSHIELD_IN3     p23
#define MOTORSHIELD_IN4     p24
#define SPEEDPIN_A          p25
#define SPEEDPIN_B          p26
#elif defined(TARGET_KL25Z) || defined(TARGET_NUCLEO_F401RE)
#define MOTORSHIELD_IN1     D8
#define MOTORSHIELD_IN2     D11
#define MOTORSHIELD_IN3     D12
#define MOTORSHIELD_IN4     D13
#define SPEEDPIN_A          D9
#define SPEEDPIN_B          D10
#else
#error "You need to specify a pin for the sensor"
#endif

MotorDriver motorDriver(MOTORSHIELD_IN1, MOTORSHIELD_IN2, MOTORSHIELD_IN3, MOTORSHIELD_IN4, SPEEDPIN_A, SPEEDPIN_B);
ros::NodeHandle nh;

void messageCb(const geometry_msgs::Twist& msg)
{
  if (msg.angular.z == 0 && msg.linear.x == 0)
  {
    motorDriver.stop();
  }
  else
  {
    if (msg.angular.z < 0)
    {
      int speed = (int)(msg.angular.z * -100);
      motorDriver.setSpeed(speed, MOTORA);
      motorDriver.setSpeed(speed, MOTORB);
      motorDriver.goRight();
    }
    else if (msg.angular.z > 0)
    {
      int speed = (int)(msg.angular.z * 100);
      motorDriver.setSpeed(speed, MOTORA);
      motorDriver.setSpeed(speed, MOTORB);
      motorDriver.goLeft();
    }
    else if (msg.linear.x < 0)
    {
      int speed = (int)(msg.linear.x * -100);
      motorDriver.setSpeed(speed, MOTORA);
      motorDriver.setSpeed(speed, MOTORB);
      motorDriver.goBackward();
    }
    else if (msg.linear.x > 0)
    {
      int speed = (int)(msg.linear.x * 100);
      motorDriver.setSpeed(speed, MOTORA);
      motorDriver.setSpeed(speed, MOTORB);
      motorDriver.goForward();
    }
  }
}

ros::Subscriber<geometry_msgs::Twist> sub("cmd_vel", &messageCb);
Timer t;

int main()
{
  t.start();
  long vel_timer = 0;
  nh.initNode();
  nh.subscribe(sub);
  motorDriver.init();
  motorDriver.setSpeed(90, MOTORB);
  motorDriver.setSpeed(90, MOTORA);
  while (1)
  {
    if (t.read_ms() > vel_timer)
    {
      motorDriver.stop();
      vel_timer = t.read_ms() + 500;
    }
    nh.spinOnce();
    wait_ms(1);
  }
}
```



### Compiling and uploading the Code

As seen on the previous tutorial, you must compile the source code by
using the makefile in order to generate the .bin file that will be
uploaded later to your MBED board. This is no different from uploading
any other mbed binary.

### Launching the App

Launch roscore 

```
$ roscore
```



Run the serial node with the right serial port corresponding to your
MBED board 

```

```

}}} 

```

```

}}}

And last, start publishing messages into the cmd_vel topic


```
$ rostopic pub /cmd_vel geometry_msgs/Twist '[1.0, 0.0, 0.0]' '[0.0, 0.0, 0.0]'
```

## PIR Motion Sensor

- **Description:** This tutorial shows an example for using an Mbed with
  a PIR Motion Sensor.
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [DHT Humidity and Temperature Sensor](#dht-humidity-and-temperature-sensor)

[rosserial](https://index.ros.org/p/rosserial) allows you to easily
integrate Mbed-based hardware with ROS. This tutorial will explain how
to use a PIR Motion Sensor with an Mbed.

You will need an [Mbed](https://developer.mbed.org/platforms), a
[PIR Motion Sensor](http://www.seeedstudio.com/depot/Grove-PIR-Motion-Sensor-p-802.html),
and a way to connect your Sensor to your Mbed to your Mbed such as a
breadboard, protoboard or
[Grove Base Shield](http://www.seeedstudio.com/depot/base-shield-v13-p-1378.html?cPath=132_134).

### The Code

Open the PIR Motion Sensor example placed on your previously downloaded
rosserial/rosserial_mbed/examples directory, and open the
GrovePIRMotionSensor.cpp file in your favorite text editor:



```cplusplus
/*
 * rosserial PIR Motion Sensor Example
 *
 * This tutorial demonstrates the usage of the
 * Seeedstudio PIR Motion Sensor Grove module
 * http://www.seeedstudio.com/depot/Grove-PIR-Motion-Sensor-p-802.html
 *
 * Source Code Based on:
 * https://developer.mbed.org/teams/Seeed/code/Seeed_Grove_PIR_Motion_Sensor_Example/
 */

#include "mbed.h"
#include <ros.h>
#include <std_msgs/Bool.h>

ros::NodeHandle  nh;

std_msgs::Bool motion_msg;
ros::Publisher pub_motion("motion", &motion_msg);

Timer t;
#ifdef TARGET_LPC1768
DigitalIn sig1(p9);
#elif defined(TARGET_KL25Z) || defined(TARGET_NUCLEO_F401RE)
DigitalIn sig1(D6);
#else
#error "You need to specify a pin for the sensor"
#endif

int main() {
    t.start();

    nh.initNode();
    nh.advertise(pub_motion);

    long publisher_timer = 0;

    while (1) {

        if (t.read_ms() > publisher_timer) {
            motion_msg.data = sig1;
            pub_motion.publish(&motion_msg);
            publisher_timer = t.read_ms() + 1000;
        }
        nh.spinOnce();
    }
}
```



### Compiling and uploading the Code

As seen on the previous tutorial, you must compile the source code by
using the makefile in order to generate the .bin file that will be
uploaded later to your MBED board. This is no different from uploading
any other mbed binary.

### Launching the App

Launch roscore 

```
$ roscore
```



Run the serial node with the right serial port corresponding to your
MBED board 

```

```

}}} 

```

```

}}}

Now watch the sensor's value on the pushed topic



```
$ rostopic echo /motion
```

## Push Button

- **Description:** Monitor a push button and publish its state in ROS
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Servo Controller](#servo-controller-example)

This tutorial describes one of the simplest and most common pieces of
hardware you might want to integrate into your ROS system: a push
button. A button and be an input device to command your robot to do its
next task, a sensor to detect of a box is opened, or an important safety
feature to stop a motor from moving past a joints limits.

In this tutorial, we will write a rosserial_mbed node that will monitor
the state of a normally off button. It will publish a boolean message to
the topic "pushed" everytime the button's state changes.

### Hardware

For this tutorial, you need an MBED board and some sort of normally off
momentary switch or push button.

For those of you who are used to hardware design, you will notice that
there is no pull-up resistor on switch input. This is because the mbed
has built in pullup resistors. Pin 7 is pulled high until the button is
pressed and connected to ground.

### Code

The code for this program is below. To use the code, copy it directly
into a fresh sketch in the mbed IDE.



```cplusplus
/*
 * Button Example for Rosserial
 */

#include "mbed.h"
#include <ros.h>
#include <std_msgs/Bool.h>

#ifdef TARGET_LPC1768
PinName button = p20;
#elif defined(TARGET_KL25Z)
PinName button = D10;
#elif defined(TARGET_NUCLEO_F401RE)
PinName button = USER_BUTTON;
#else
#error "You need to specify a pin for the button"
#endif

ros::NodeHandle nh;

std_msgs::Bool pushed_msg;
ros::Publisher pub_button("pushed", &pushed_msg);

DigitalIn button_pin(button);
DigitalOut led_pin(LED1);

bool last_reading;
long last_debounce_time=0;
long debounce_delay=50;
bool published = true;

Timer t;
int main() {
    t.start();
    nh.initNode();
    nh.advertise(pub_button);

    //Enable the pullup resistor on the button
    button_pin.mode(PullUp);

    //The button is a normally button
    last_reading = ! button_pin;

    while (1) {
        bool reading = ! button_pin;

        if (last_reading!= reading) {
            last_debounce_time = t.read_ms();
            published = false;
        }

        //if the button value has not changed for the debounce delay, we know its stable
        if ( !published && (t.read_ms() - last_debounce_time)  > debounce_delay) {
            led_pin = reading;
            pushed_msg.data = reading;
            pub_button.publish(&pushed_msg);
            published = true;
        }

        last_reading = reading;

        nh.spinOnce();
    }
}
```

 This code is a typical example of how
rosserial_mbed is used. The rosserial objects are globally declared.
Some preprocessor directives for defining the GPIOs used by the program,
depending on which MBED board are you using

#### Monitoring the Button

This sensor should not spam messages about button's state but should
publish an update only when the button is pressed or released. To
monitor this change we need to remember the button's last state and
know how long this state has been valid. Then once the state has
changed, the sensor should debounce the button. It should wait "long
enough" so we know that the button value has settled and is not
oscillating around. This is because the voltage at the input pin will
bounce around (as shown in the diagram below) as the mechanical contacts
bounce back and forth during contact and release.

![attachment:debounce.png](doc/debounce.png) Debouncing variables, this
approach is used for avoiding false lectures from the push buttons.
Creates a timer "t" Set pin mode as `PullUp`, which means it
connects a weak resistor in between the pin and VCC, so you don't need
to connect a resistor from outside. Stores the actual state of the input
on a variable and compares it with the last reading before that and
reset the published variable to false. Finally the code reads the button
at every loop, checks to see if the button state has changed, and then
checks to see if the button state is stable and has been published.
Updates the value of the last_reading variable with the actual reading
value.

### Testing

Startup roscore



```
roscore
```

 In a new terminal window, run the
rosserial_python serial_node.py. Make sure to use the correct serial
port.

{ }}}} { }}}} Now watch the button's value on the pushed topic



```
rostopic echo pushed
```

## SRF08 Ultrasonic Ranger

- **Description:** In this tutorial, we will use a Mbed and a
  [SRF08 Ultrasonic Ranger](http://www.acroname.com/robotics/parts/R145-SRF08.html)
  as a Range Finder.The SRF08 communicates with the Mbed over SPI/I2C.
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Buzzer Module](#buzzer-module)

[rosserial](https://index.ros.org/p/rosserial) allows you to easily
integrate Mbed-based hardware with ROS. This tutorial will explain how
to use a SRF08 Ultrasonic ranger with a Mbed.

You will need an [Mbed](https://developer.mbed.org/platforms), a
[SRF08 Ultrasonic Ranger](http://www.acroname.com/robotics/parts/R145-SRF08.html),
and a way to connect your Ranger to your Mbed such as a breadboard or
protoboard.The SRF08 Mbed library can be downloaded from
[here](https://developer.mbed.org/cookbook/SRF08-Ultrasonic-Ranger)

### The Code



```cplusplus
/*
 * rosserial SRF08 Ultrasonic Ranger Example
 *
 * This tutorial demonstrates the usage of SRF08 ultrasonic module
 *
 * Source Code Based on:
 * http://wiki.ros.org/rosserial_arduino/Tutorials/SRF08%20Ultrasonic%20Range%20Finder
 */

#include "mbed.h"
#include "SRF08.h"

#include <ros.h>
#include <ros/time.h>
#include <sensor_msgs/Range.h>

ros::NodeHandle  nh;

sensor_msgs::Range range_msg;
ros::Publisher pub_range("/ultrasound", &range_msg);

char frameid[] = "/ultrasound";

#ifdef TARGET_LPC1768
SRF08 srf08(p9, p10, 0xE0);             // Define SDA, SCL pin and I2C address
#elif defined(TARGET_KL25Z) || defined(TARGET_NUCLEO_F401RE)
SRF08 srf08(I2C_SDA, I2C_SCL, 0xE0);    // Define SDA, SCL pin and I2C address
#else
#error "You need to specify a pin for the sensor"
#endif

Timer t;
int main()
{
  t.start();
  nh.initNode();
  nh.advertise(pub_range);

  range_msg.radiation_type = sensor_msgs::Range::ULTRASOUND;
  range_msg.header.frame_id =  frameid;
  range_msg.field_of_view = 0.1;  // fake
  range_msg.min_range = 0.0;
  range_msg.max_range = 6.47;

  long range_time = 0;

  while (1)
  {
    //publish the adc value every 50 milliseconds
    //since it takes that long for the sensor to stablize
    if (t.read_ms() >= range_time)
    {
      range_msg.range = srf08.read() / 100.0;
      range_msg.header.stamp = nh.now();
      pub_range.publish(&range_msg);
      range_time =  t.read_ms() + 50;
    }

    nh.spinOnce();
  }
}
```



### Launching the App



```
$ roscore
```



Run the serial node with the right serial port corresponding to your
MBED board 

```

```

}}} 

```

```

}}}

Now watch the sensor's value on the pushed topic



```
$ rostopic echo /ultrasound
```

## Servo Controller Example

- **Description:** Tutorial for controlling an R/C servo with rosserial
  and an MBED
- **Next Tutorial:**
  [IR Ranger](#ir-ranger-tutorial)

This tutorial explains how to control an R/C servo through ROS by using
an MBED and rosserial. This can be used to control a release mechanism,
a cheap robot arm, ROS powered biped, or anything where you need a cheap
actuator. The code provided is a very basic example and shows the
control of a single hobby servo.

### Hardware

This example assumes that you have an MBED and a hobby r/c servo. The
r/c servo can be purchased from your local hobby shop,
[Towerhobbies](http://www3.towerhobbies.com/cgi-bin/wti0001p?&I=LXUK84&P=ML),
[Sparkfun](http://www.sparkfun.com/products/9064), etc.

The hobby servo r/c are great little actuators because they are
relatively cheap (as low as \$10) but contain a gear box and motor
control electronics. They are controlled by sending a squarewave pulse
of 1-2 milliseconds in width every 20 milliseconds. This typically moves
the servo arm from 0-180 degrees. Hobby servo's come in a huge variety
of sizes, torques, and angular precision.

### Code

The code for this tutorial is made extremely simple through the use of
the MBED Servo library. It handles all of the low level control to
generate and maintain the servo pulses. All your code needs to do is
specify the pin the servo is attached to and then write the angle to the
servo object. Underneath, the Servo library uses the MBED's built in
timer interrupts to generate the correct pulses.



```cplusplus
/*
 * rosserial Servo Control Example
 *
 * This sketch demonstrates the control of hobby R/C servos
 * using ROS and an MBED board
 *
 */

#include "mbed.h"
#include "Servo.h"
#include <ros.h>
#include <std_msgs/UInt16.h>

ros::NodeHandle  nh;

#ifdef TARGET_LPC1768
Servo servo(p21);
#elif defined(TARGET_KL25Z) || defined(TARGET_NUCLEO_F401RE)
Servo servo(D8);
#else
#error "You need to specify a pin for the Servo"
#endif

DigitalOut myled(LED1);

void servo_cb( const std_msgs::UInt16& cmd_msg) {
    servo.position(cmd_msg.data); //set servo angle, should be from 0-180
    myled = !myled;  //toggle led
}


ros::Subscriber<std_msgs::UInt16> sub("servo", servo_cb);

int main() {

    nh.initNode();
    nh.subscribe(sub);

    while (1) {
        nh.spinOnce();
        wait_ms(1);
    }
}
```



The key servo specific areas here are the fact that we made a global
Servo object, attached to the correct MBED pin, and then on every servo
topic call back, we write the servos new angle to the servo object.

### Testing

First, startup your roscore and the rosserial python node in their own
terminal windows. 

```
roscore
```





```

```

}}} 

```

```

}}}

Now, in a new terminal window, use rostopic pub to control your servo!
Simply specify the angle from 0-180 and watch it move.



```
rostopic pub servo std_msgs/UInt16  <angle>
```

## Using Time and TF

- **Description:** This tutorial shows how to use ros::Time and TF to
  create a tf publisher on MBED.
- **Keywords:** MBED, rosserial, serial
- **Tutorial Level:** INTERMEDIATE
- **Next Tutorial:**
  [Measuring Temperature](#temperature-sensor)

### Using Time and TF on MBED

The `rosserial_mbed` package contains libraries for generating
timestamps on MBED which are synchronized with the computer on which the
roscore instance is running. This tutorial shows how to access time,
using an example of publishing a `tf` transform.

#### The Code

Open the Time and TF example placed on your previously downloaded
rosserial/rosserial_mbed/examples directory, and open the TimeTF.cpp
file in your favorite text editor:



```cplusplus
/*
 * rosserial Time and TF Example
 * Publishes a transform at current time
 */

#include "mbed.h"
#include <ros.h>
#include <ros/time.h>
#include <tf/transform_broadcaster.h>

ros::NodeHandle  nh;

geometry_msgs::TransformStamped t;
tf::TransformBroadcaster broadcaster;

char base_link[] = "/base_link";
char odom[] = "/odom";

int main() {
    nh.initNode();
    broadcaster.init(nh);


    while (1) {
        t.header.frame_id = odom;
        t.child_frame_id = base_link;
        t.transform.translation.x = 1.0;
        t.transform.rotation.x = 0.0;
        t.transform.rotation.y = 0.0;
        t.transform.rotation.z = 0.0;
        t.transform.rotation.w = 1.0;
        t.header.stamp = nh.now();
        broadcaster.sendTransform(t);
        nh.spinOnce();
        wait_ms(10);
    }
}
```



#### The Code Explained

Now, let's break the code down. We need to include the `mbed.h` for
every MBED program. We need to include our typical ROS stuff. Next, we
instantiate a `TransformStamped` message to use, and a broadcaster. We
also need to specify the names of the frames we are publishing a
transform for, and the transform broadcaster. Inside the main function,
we have to call `init()` on the !TransformBroadcaster with the node
handle as a parameter. Without doing this, the broadcaster will not
publish correctly. Then, inside the main function there's a loop in
which we fill in the fields of our transform. The frame IDs are set to
the correct string names, and the values of the translation and rotation
are set. Calling `nh.now()` returns the current time, as a
`ros::Time` instance, just like when using
[roscpp's ros::Time::now()](https://index.ros.org/p/roscpp). Finally,
we publish the transform, and then `spinOnce` and wait a bit before
doing it again. Transforms should always be published at a regular rate,
although usually the data fields will be filled in from real data.

### Compiling and uploading the Code

As seen on the previous tutorial, you must compile the source code by
using the makefile in order to generate the .bin file that will be
uploaded later to your MBED board. This is no different from uploading
any other mbed binary.

#### Running the Code

Now, launch the [roscore](roscore) in a new terminal window:


```
roscore
```



Next, run the rosserial client application that forwards your mbed
messages to the rest of ROS. Make sure to use the correct serial port:


```

```

}}} 

```

```

}}}

Finally, you can check the transform using: 

```
rosrun tf tf_echo odom base_link
```

 Or,
by running: 

```
rosrun tf view_frames
```



### Further Reading

Please see [rosserial/Overview](https://index.ros.org/p/rosserial) for
more information using Time instances.

## Using rosserial with Inforce MBED PAC Shield

- **Description:** This tutorial show how to use rosserial_mbed with the
  Inforce 6410 plus + PAC Shield
- **Keywords:** Inforce PAC MBED serial rosserial
- **Tutorial Level:** BEGINNER

### Using rosserial with Inforce MBED PAC Shield

#### Downloading the required files

Login to Inforce's website and download the BSP package: at the time
this wiki was written it was: SYS6410P_Ubuntu_Linux_BSP_880411_V1.zip
unzip it and place it somewhere on your home directory, e.g.:

. 

```
$ unzip SYS6410P_Ubuntu_Linux_BSP_880411_V1.zip -d ~/SYS6410P_BSP
```



Download an install PPA for your specific Ubuntu version form here:
<https://launchpad.net/~terry.guo/+archive/ubuntu/gcc-arm-embedded>

#### Generating ros_lib

Create a new empty workspace for rosserial:

. 

```
$ cd ~/SYS6410P_BSP
```

 

```
$ mkdir -p rosserial_ws/src
```




```
$ cd rosserial_ws/src
```



Clone the rosserial repo from github and checkout to the jade-devel
branch:

. 

```
$ git clone https://github.com/ros-drivers/rosserial -b jade-devel
```



Move to the root of your new workspace:

. 

```
$ cd ..
```



and from there execute:

. 

```
$ catkin_make
```



and then:

. 

```
$ source devel/setup.bash
```



From that same terminal, generate the libraries that we will need later
for your mbed project, e.g.:

. 

```
$ rosrun rosserial_mbed make_libraries.py ~/SYS6410P_BSP/
```



That should create a new directory called ros_libs with all the involved
libraries, on the path you wrote inside the brackets

#### Download and run the demo project

You can clone this demo that make use of some of the capabilities of the
MBED PAC Shield for the Inforce 6410 plus board.

Clone this Github repo into your prefered directory:

. 

```
$ git clone https://github.com/creativa77/ifc6410p_mbed_ros_demo ros_demo
```



You can access the instructions of this demo from its
[Github](https://github.com/creativa77/ifc6410p_mbed_ros_demo) main page
or by reading the README.md file on your downloaded ros_demo directory.

#### Importing your project into the custom build system

Copy your project directory into mbed-master/libraries/tests/ros/ for
example:

. 

```
$ cp -r ~/ros_demo ~/SYS6410P/mbed-master/libraries/tests/ros/
```



Open the tests.py script from
/SYS6410P/mbed-master/workspace_tools/tests.py and search for a series
of braces with something similar to this:

. 

```
{
    "id": "ROSSERIAL_MBED_PAC", "description": "Example of rosserial_mbed on PAC board",
    "source_dir": join(TEST_DIR, "ros", "ros_demo"),
    "dependencies": [MBED_LIBRARIES, TEST_MBED_LIB, CPPUTEST_LIBRARY],
    "automated": False,
    "mcu": ["PAC_F401RB"],
},
```



You should make a copy of one of those and edit it with your own
project's description and dependencies and place it at the end of the
existing list to make things easier for the next step.

from the \~ /SYS6410P/mbed-master/workspace_tools/ directory, do:

. 

```
$ python make.py
```



it will answer with an error and will show you some instructions about
the usage and an enumerated list with all the available projects. Your
project should appear at the end of this list with a number. Example:

. 

```
[ERROR] You have to specify one of the following tests:
[  0] MBED_A1: Basic
[  1] MBED_A2: Semihost file system
[  2] MBED_A3: C++ STL
[  3] MBED_A4: I2C TMP102
[  4] MBED_A5: DigitalIn DigitalOut
[  5] MBED_A6: DigitalInOut
[  6] MBED_A7: InterruptIn
[  7] MBED_A8: Analog
[  8] MBED_A9: Serial Echo at 115200
...
[135] ROSSERIAL_MBED_PAC: Example of rosserial_mbed on PAC board
```



Execute again the script but this time as shown on the next line and
replace the last number with your project's number as shown on the
command from above.

. 

```
$ sudo python make.py -m PAC_F401RB -t GCC_ARM -d ~/SYS6410P_BSP/ -p 135
```



It will compile the project and create a .bin file ready to be burned
into the board

#### Downloading the code into the MBED PAC shield

Now, depending on where you are doing the work, you must copy the .bin
into the stm32 flash: If you are working on a remote computer, say, a
laptop. One way would be copying the file through ssh, example:

. 

```
$ scp ~/SYS6410P_BSP/rosserial_mbed_pac.bin linaro@192.168.1.101:
```



You must have correctly installed and configured SSH in your own board
and use their use their corresponding user and IP.

Once the .bin is placed into your board's memory, and assuming the .bin
is placed on your home directory, run this command in order to burn it
into the stm32 microcontroller of the PAC board:

. 

```
stm32flash -w ~/rosserial_mbed_pac.bin -v -g 0x0 /dev/ttyHS2 -R
```



where:

. 

```
[-w filename] write the file
[-v] verify writes
[-g address] start execution at specified address
[-R] restart device at exit
```



#### Video of the demo running

Here's a demo video of the Inforce 6410P with rosserial_mbed in action:

[Youtube](https://www.youtube.com/watch?v=_Fw67s5DVuc&rel=0)

## rosserial MBED Setup

- **Description:** This tutorial shows how to configure a basic
  development environment to use rosserial_mbed with an enabled MBED
  board
- **Keywords:** MBED serial rosserial
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Hello World (example publisher)](https://index.ros.org/p/rosserial_mbed)

### Introduction

MBED is a platform and operating system for devices based on 32-bit ARM
Cortex-M microcontrollers. It is a great tool for quickly and easily
programming hardware. Using the
rosserial_mbed package, you can use ROS
directly with your MBED enabled board.
[rosserial](https://index.ros.org/p/rosserial) provides a ROS
communication protocol that works over your MBED's UART. It allows your
MBED to be a full fledged ROS node which can directly publish and
subscribe to ROS messages, publish TF transforms, and get the ROS system
time.

In order to use the rosserial libraries in your own code, you must first
put

. 

```
#include <ros.h>
```



prior to including any other header files, e.g.

. 

```
#include <std_msgs/String.h>
```



otherwise the compiler will not be able to locate them.

### Using the official online compiler



```
{#!wiki version indigo_and_newer

You just need to import the rosserial_mbed library to your online compiler account using the following link:
   {{{
$ https://developer.mbed.org/users/garyservin/code/ros_lib_$ROS_DISTRO/
```

 }}}}

### Using the offline compiler

#### Install gcc4mbed

You need to install [gcc4mbed](https://github.com/adamgreen/gcc4mbed) by
following the "Quick start" instructions on the Readme.

Let's assume that you've installed gcc4mbed to `~/gcc4mbed`.

#### Cloning the rosserial repo

Clone the [rosserial](https://github.com/ros-drivers/rosserial.git) repo
on your ros workspace src directory, e.g.: `~/catkin_ws/src/`

#### Generating the ros_lib library

Go to the root of your workspace and execute:

. 

```
$ catkin_make
```



And then:

. 

```
source devel/setup.bash
```



Now you are able to generate the `ros_lib` library, needed to compile
every project using rosserial_mbed:

. 

```
rosrun rosserial_mbed make_libraries.py ~/ros/lib
```



where the last parameter is the output path for the generated `ros_lib`
directory to reside in. You should modify it according to your directory
structure.

#### Exporting path variables

Now, move to your mbed project's directory and set the environment
variables for the gcc4mbed and the ros-lib paths: Example:

. 

```
$ export GCC4MBED_DIR=~/gcc4mbed
```

 

```
$ export ROS_LIB_DIR=~/ros/lib/ros_lib
```



Make sure to point to the `ros_lib` directory, which is inside the
directory specified in the above `rosrun`. It is important that you
DON'T put trailing slashes (especially for the `ROS_LIB_DIR`). If you
do, you might end up getting a "missing header" error when compiling
your project.

You can export these two variables in your `.bashrc` or modify your MBED
project's makefile with the desired path for both variables (we are
going to cover that later on in this tutorial).

#### Compiling and deploying an mbed project

Once you've finished all the above tasks you must be able to compile
and deploy your mbed project into the board:

We are going to base this part of the tutorial on the 'Blink' project
that came with the rosserial_mbed repo you've downloaded earlier, you
can find it in the following relative path:

. 

```
rosserial/rosserial_mbed/src/examples/Blink/
```



There you should find a typical source for an mbed project: a C++ source
file (`Blink.cpp`) and a `makefile` file, which you can use as a base
for other projects by modifying the things according to your needs.

Then, from your makefile path directory do:

. 

```
$ make
```



This will generate a compiled binary file, and now you're able to copy
it into your mbed device for testing. Or, simply run:

. 

```
$ make deploy
```



to do the compilation and deployment in one step.
