## Usage

The transmission of audio data takes place outside of the ROS
communication system. Knowledge of hostnames and ports is provided to
the server and client scripts via parameters. The server and client
scripts both require a `client_host` and `client_port`. If both
scripts are run on the same machine `client_host` can be set to
`localhost`.

Example launch file for the server: 

```
<launch>

  <node name="gstream_server" pkg="compressed_audio_streaming" type="gstream_server.py" output="screen">
    <param name="client_host" value="localhost"/>
    <param name="client_port" value="3000"/>
  </node>

</launch>
```



Example launch file for the client: 

```
<launch>

  <node name="gstream_client" pkg="compressed_audio_streaming" type="gstream_client.py" output="screen">
    <param name="client_host" value="localhost"/>
    <param name="client_port" value="3000"/>
  </node>

</launch>
```



Once the launch files are created, start the server on the machine which
has the microphones 

```
roslaunch compressed_audio_streaming server.launch
```



Finally, start the client on the machine which is to receive the audio
stream 

```
roslaunch compressed_audio_streaming client.launch
```



## Audio Devices

The server records from the default audio input, and the client plays to
the default audio output.
