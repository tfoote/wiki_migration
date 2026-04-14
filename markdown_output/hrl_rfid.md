If you decide to use UHF RFID in \'\'your\'\' project, we kindly suggest
taking a look at our lab\'s
[RFID in Robotics project page](http://www.hsi.gatech.edu/hrl/project_rfid.shtml)
or the Pervasive Computing article:
\"[RFID-Guided Robots for Pervasive Automation](http://www.computer.org/portal/web/csdl/doi/10.1109/MPRV.2010.17)\"
(registration-free
[pdf](http://www.hsi.gatech.edu/hrl/pdf/pervasive_computing_2010.pdf)).

## Hardware Overview:

My UHF RFID reader of choice is the
[ThingMagic Mercury5e (M5e)](http://www.thingmagic.com/embedded-rfid-readers/mercury5e/1-embedded-rfid-readers/3-mercury5e)
and/or
[Mercury5e-Compact (M5e-C)](http://www.thingmagic.com/embedded-rfid-readers/m5e-compact/1-embedded-rfid-readers/1-m5e-compact),
pictured below left. I have personally verified these readers\'
operation with over 32 different UHF RFID tag variants, pictured below
right (not to scale). Generally, I prefer Alien Squiggle tags; they are
available for roughly \$0.29-0.59 ea. in quantities of 500-1000 from
places like [BuyRFID](http://www.buyrfid.com/catalog/) or
[AtlasRFIDstore](http://www.atlasrfidstore.com/default.asp). Other tags,
such as specialty tags designed to operate on / near metal, are more
expensive; AtlasRFIDstore as a nice set of
[sample packs](http://www.atlasrfidstore.com/RFID_Tag_Sample_Pack_UHF_Passive_p/rfid_tag_sample_pack.htm)
that give you the opportunity to explore different variants.

![\|height=\"200\"](attachment:ThingMagicMercury5e.jpg)
![\|height=\"200/\"](attachment:UHF_RFID_Tags.jpg)

ThingMagic Mercury5e:

-   EPCglobal Gen 2 (ISO 18000-6C) tag protocol with anti-collision
-   Two antenna connectors
-   Adjustable read/write power from 5 dBm to 30 dBm (1W)
-   860 to 960 MHz UHF RFID carrier frequency range
-   FCC certifiable
-   TTL serial interface
-   Maximum tag read rate of over 170 tags per second
-   30 feet (9 m) max. read range with 6 dBi antenna
-   4 general purpose I/O lines
-   \'\'\'Approx Cost: \$500.00\'\'\'

ThingMagic Mercury5e-Compact:

-   EPCglobal Gen 2 (ISO 18000-6C) tag protocol with anti-collision

```{=html}
<!-- -->
```
-   One antenna connector
-   Adjustable read/write power from 10 dBm to 23 dBm
-   860 to 960 MHz UHF RFID carrier frequency range
-   FCC certifiable
-   TTL serial interface
-   Maximum tag read rate of over 160 tags per second
-   20 feet (6 m) max. read range with 6 dBi antenna
-   4 general purpose I/O lines
-   \'\'\'Approx Cost: \$400.00\'\'\'

Generally speaking, I prefer the extra RF output power afforded by the
M5e (full), as it translates into greater read ranges; the added antenna
port is particularly useful for servoing applications. The M5e-C is also
useful, as it can be powered solely off of USB (a hardware design I
\'\'might\'\' elaborate on at a later date). Anyway, ThingMagic has
[dev-kits](http://www.thingmagic.com/store/) available for \$1,500 that
include the cabling, power regulation, an antenna, and some tags \-- not
a bad deal if you\'re starting fresh. However, for roughly \$60, you can
build your own carrier board with TTL RS232→USB (FTDI) already built in.
My PCB design ([Eagle CAD](http://cadsoft.de/)) can be found her
(<attachment:Design.zip>); it can be fabricated by
[Advanced Circuits](http://4pcb.com/) for \$33 each.

One of the \'\'\'\'\'most important\'\'\'\'\' considerations when
designing your UHF RFID system is the selection of reader antennas (the
same considerations apply to tag antennas, but specifications are
generally unpublished). This topic is too deep to fully explore here;
most critically, you\'ll want to pay attention to:

-   \'\'\'Physical size:\'\'\' Drastically affects robot integration.
    High-gain / directionality antennas are generally much larger and
    unwieldy.

```{=html}
<!-- -->
```
-   \'\'\'Radiation pattern:\'\'\' A specification of gain /
    directionality versus bearing-azimuth (polar) angles will
    essentially determine how far tags can be read at various angles.

```{=html}
<!-- -->
```
-   \'\'\'Gain:\'\'\' Simply put, higher gain equates to longer read
    range.

```{=html}
<!-- -->
```
-   \'\'\'Beamwidth:\'\'\' Determines the \'\'sharpness\'\' (width) of
    the high-gain region. Larger beamwidths will have more angle / area
    coverage, but are less discriminative in angle (for determining
    direction of tag) and generally suffer from more multipath signal
    interference.

```{=html}
<!-- -->
```
-   \'\'\'Polarization:\'\'\' Circularly-polarized antennas tend to have
    less mismatch when exciting tags at off-angles.

![\|height=\"250\"](attachment:RFID_antennas.jpg)
![\|height=\"250\"](attachment:ELE_large_antennas.jpg)
![\|height=\"250\"](attachment:ELE_Small_Antennas.jpg)

Over the last several years, I have experimented with \'\'numerous\'\'
antennas, both purchased and constructed: whips, dipoles, patches,
loaded-microstrips, etc. Ultimately, I\'ve settled on these two patch
antennas (articulated using
[Robotis Dynamixel servos](http://www.hizook.com/blog/2010/03/14/robotis-dynamixel-servos-overview-applications-tear-down-and-open-source-software));
generally choosing the largest antenna possible given robot integration
size constraints (see EL-E photos above):

-   \'\'\'Laird Technologies S9028PC12NF\'\'\': Circularly polarized, 25
    x 25 cm, 65° beamwidth, 7.5 dB gain. Available from
    [Hutton Communications](http://www.hol4g.com/ac/product.aspx?number=CCS-S9028PC12NF&p=163850&sc=3572)
    for \$215.
    ([Datasheet](hrl_rfid/sites/default/files/users/Travis%20Deyle/Laird_S9028PC12NF.pdf))

```{=html}
<!-- -->
```
-   \'\'\'Laird Technologies S9025P:\'\'\' Circularly polarized, 13.5 x
    13.5 cm, 100° beamwidth, 5.5 dB gain. Available from
    [Arcadian Inc](http://www.arcadianinc.com/part/S9025PLNF/88239/LAIRDTechnologiesAntenexCenturionCushcraftandPacificWireless/)
    for \$100.
    ([Datasheet](hrl_rfid/sites/default/files/users/Travis%20Deyle/Laird_S9025P_Antenna.pdf))

## Software Overview:

The communication / software API for ThingMagic\'s module is obtained
upon purchase; I do not believe I am at liberty to distribute my
personal copy. However, my open source Python library (depending only on
[Pyserial](http://pyserial.sourceforge.net/)) implements a sufficiently
rich subset of the API and functions on Windows, Linux, and Mac OS. The
stand-alone M5e library is contained in \'\'lib_M5e.py\'\'. Now for a
demonstration, assuming a Linux machine and a M5e (full) reader
operating at 30dBm (1Watt) output power:

```
import lib_M5e as M5e

r = M5e.M5e( '/dev/ttyUSB0', readPwr = 3000 )
r.ChangeAntennaPorts( 1, 1 )
r.QueryEnvironment()

r.TrackSingleTag( 'test_tag_id_' )
r.ChangeTagID( 'test_tag_id_' )
r.QueryEnvironment()
r.TrackSingleTag( 'test_tag_id_' )

r.ChangeAntennaPorts( 2, 2 )
r.QueryEnvironment()
``` Basically, this code sets up the reader,
selects antenna port 1 for both transmit and receive, and queries for
all tags in the environment for 50 ms (returns a list of tuples: \[(ID,
RSSI), \... \] ). Subsequently, the reader checks for the presence of a
specific 96-bit tag ID (returns RSSI if read was successful, -1
otherwise). Then the \'\'ChangeTagID\'\' function changes the ID of the
nearest tag (the one read first), and then queries the environment and
tracks the tag again. Finally, the last two statements query the
environment using the other antenna port.

There is also a \'\'M5e_Poller\'\' class that can run in a thread and
continuously either query the environment or track a tag \-- issuing
callbacks with argument \'\'\[antenna_name, ID, RSSI\] \'\'after each
read / read attempt:

```
import lib_M5e as M5e

def P1(r):
    r.ChangeAntennaPorts(1,1)
    return 'AntPort1'

def P2(r):
    r.ChangeAntennaPorts(2,2)
    return 'AntPort2'

def PrintDatum(data):
    ant, ids, rssi = data
    print data

r = M5e.M5e( '/dev/ttyUSB0', readPwr = 3000 )
q = M5e.M5e_Poller(r, antfuncs=[P1, P2], callbacks=[PrintDatum])
q.query_mode()

t0 = time.time()
while time.time() - t0 < 3.0:
    time.sleep( 0.1 )

q.track_mode( 'test_tag_id_' )

t0 = time.time()
while time.time() - t0 < 3.0:
    time.sleep( 0.1 )

q.stop()
``` That sums up the stand-alone library. The Robot
Operating System (ROS) wrappers act in pretty much the same fashion as
the \'\'M5e_Poller \'\'and can be found in \'\'ros_M5e.py \'\'(server
node) and \'\'ros_M5e_client.py\'\' (client nodes). Only one
\'\'server\'\' node can connect to the M5e module\'s serial port at once
due to strict device handshaking protocols; any number of client nodes
can control / query the server. The server code looks like this:

```
import ros_M5e as rm

def P1(r):
    r.ChangeAntennaPorts(1,1)
    return 'AntPort1'

def P2(r):
    r.ChangeAntennaPorts(2,2)
    return 'AntPort2'

ros_rfid = rm.ROS_M5e( name = 'my_rfid_server',
                       readPwr = 3000,
                       portStr = '/dev/ttyUSB0',
                       antFuncs = [P1, P2],
                       callbacks = [] )

rospy.spin()
ros_rfid.stop()
``` By default, the server does nothing (standby to
save power). A client node must put the server into either
\'\'QUERY_MODE \'\'or \'\'TRACK_MODE\'\'. This can be accomplished using
any client. For example, using \'\'rosservice\'\':

```
>  rosservice call /rfid/my_rfid_server_mode "['query']"
>  rostopic echo  -c /rfid/my_rfid_server_reader
[OUTPUT HERE]
>  rosservice call /rfid/my_rfid_server_mode "['track', 'test_tag_id_']"
>  rostopic echo  -c /rfid/my_rfid_server_reader
[OUTPUT HERE]
>  rosservice call /rfid/my_rfid_server_mode "['stop']"
``` The last call puts the reader back into standby
mode (any argument other than \'query\' or \'track\'). The
\'\'ros_M5e_client.py\'\' file implements a rudimentary RFID client that
can perform the same operations.

```
import ros_M5e_client as rmc

r = rmc.ROS_M5e_Client( name = 'my_rfid_client' )
r.query_mode()
r.read( antenna = 'AntPort1' )

r.track_mode( 'test_tag_id' )
r.read( antenna = 'AntPort1' )

r.stop()
``` The \'\'read\'\' method for
\'\'ROS_M5e_Client\'\' returns the latest RFID read on the desired
antenna as a ROS RFIDread message.
