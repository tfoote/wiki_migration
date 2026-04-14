![\|height=\"200\",width=\"333\"](attachment:Logo-white-medium.jpg)

## Description

Includes the mild.launch file which starts the
[asr_mild_base_laserscanner](asr_mild_base_laserscanner) node and the
[asr_mild_base_driving](asr_mild_base_driving) node.

## Functionality

Our MILD Robot:

![Our MILD Robot\|height=\"402\",width=\"218\",class=\"external_image\"](attachment:Mild-Photo.jpg)

This package is only used to start the asr_mild_base_laserscanner node
of a robot with a SICK PLS 101-312 laserscanner and the
asr_mild_base_driving node.

Also here you can adapt the parameters for the laserscanner and the
speed up of the velocity (look at the
[asr_mild_base_laserscanner](asr_mild_base_launch_files) and
[asr_mild_base_driving](asr_mild_base_driving) documentation).

To adapt the parameters take a look at the mild.launch file:

```
<launch>
    <env name="ROSCONSOLE_CONFIG_FILE" value="$(find asr_mild_base_launch_files)/log/rosconsole.config" />

    <node name="sick" pkg="asr_mild_base_laserscanner" type="asr_mild_base_laserscanner" output="screen" required="true"/>
    <param name="topic" value="scan" />
    <!-- Laserscanner baudrate. Only four values: 9600, 19200, 38400, 500000. 38400 means 4 complete measurements in 1 sec. -->
    <param name="baudrate" value="500000" />
    <param name="serial" value="/dev/rs422b" />
    <param name="init_attempts" value="10" />

    <node name="can" pkg="asr_mild_base_driving" type="asr_mild_base_driving" output="screen" required="true"/>
    <!-- Speedup of the mild. 1 = normal velocity. 2 = double velocity. Float value. --> <param name="velocity" value="1" />
</launch>
```

## Usage

### Needed packages

asr_mild_base_driving

asr_mild_base_laserscanner

### Start system

Execute the following command on the computer which is connected to the
motors and the laserscanner (start driving and laserscanner):

```
roslaunch asr_mild_base_launch_files mild.launch
```
