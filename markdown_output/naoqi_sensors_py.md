## Nodes



```clearsilver
node.0 {
 name = camera
 desc = `camera` publishes Nao's camera image by wrapping the Aldebaran Python NaoQI API. Note that there is a Python and a C++ version of this node. The camera node provides a camera info manager and is compatible with the [[camera_calibration]] package. Use [[rqt_reconfigure]] to select the camera and to change the camera parameters on the fly.
 pub {
  0.name = image_raw
  0.type = sensor_msgs/Image
  0.desc = Image stream (by default bgr8 encoding)
  1.name = camera_info
  1.type = sensor_msgs/CameraInfo
  1.desc = Camera info providing the camera calibration data if available.
 }
}
node.1 {
    name = microphone
    desc = Publish audio buffers from microphones
    pub {
        0.name = ~audio_raw
        0.type = naoqi_msgs/AudioBuffer
        0.desc = Raw audio buffers
    }
    param {
        0.name = ~use_ros_time
        0.desc = Timestamp audio buffers using ros::Time::now() instead of NAOqi timestamps
        0.type = boolean
        0.default = True
        1.name = ~frequency
        1.desc = Audio sampling frequency
        1.type = integer
        1.default = 16000
    }
}
node.2 {
    name = sonar
    desc = Node that publishes readings from the robot's sonar sensors in its chest.
    pub {
        0.name = sonar
        0.type = sensor_msgs/Range
        0.desc = Sonar readings
    }
    param {
        0.name = ~memory_key
        0.type = string
        0.desc = ALMemory key for the sensor readings. For Nao robots the keys are `Device/SubDeviceList/US/Left/Sensor/Value` or `Device/SubDeviceList/US/Right/Sensor/Value`.
        1.name = ~frame_id
        1.type = string
        1.desc = TF frame for the sensor readings. For Nao robots the frames are `LSonar_frame` or `RSonar_frame`.
        2.name = ~sonar_rate   
        2.default = 10.0
        2.type = float
        2.desc = Rate for publishing the sonar readings in Hz.
    }
}
```


