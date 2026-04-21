## Nodes



```clearsilver

node.0 {
  name = nao_alife
  desc = ROS node to interface with Naoqi Autonomous Life modules. See the [[http://doc.aldebaran.com/2-1/naoqi/core/autonomouslife_advanced.html#autonomouslife-states|Nao documentation]] for a description of the individual states.
  srv {
    0.name = nao_alife/disabled
    0.desc = Set the robot's state to ''disabled''.
    0.type = std_srvs/Empty
    1.name = nao_alife/interactive
    1.desc = Set the robot's state to ''interactive''.
    1.type = std_srvs/Empty
    2.name = nao_alife/safeguard
    2.desc = Set the robot's state to ''safeguard''.
    2.type = std_srvs/Empty
    3.name = nao_alife/solitary
    3.desc = Set the robot's state to ''solitary''.
    3.type = std_srvs/Empty
  }
}

node.1 {
 name = nao_behaviors
 desc = `nao_behaviors` allows you to query and execute pre-recorded actions on the NAO. Note a node may only execute one behaviour at a time. You can use choregraphe to generate behaviors (Box libraries->Templates->Animation).
 goal {
  0.name = run_behavior
  0.type = naoqi_msgs/RunBehaviorGoal
  0.desc = Executes an already installed behavior
 }
 srv {
  0.name = get_installed_behaviors
  0.type = naoqi_msgs/GetInstalledBehaviors
  0.desc = Returns a list of the installed behaviors on the robot
 }
}

node.3 {
 name = nao_diagnostic_updater
 desc = This script collects diagnostic information on a Nao robot and publishes the information as !DiagnosticArray messages (last tested with NaoQI 1.10.52). CPU temperature and network status will only be available if the script runs directly on the robot.
 pub{
  0.name = diagnostics
  0.type = diagnostic_msgs/DiagnosticArray
  0.desc = Dignostic messages
 }
}

node.4 {
 name = nao_footsteps
 desc = `nao_footsteps` handles footsteps meant to be executed on the NAO robot. It offers a topic and a service to execute footsteps on the NAO robot, as well as a service to clip footsteps which can be afterwards performed by the NAO robot.
 sub {
  0.name = footstep
  0.type = humanoid_nav_msgs/StepTarget
  0.desc = Sends a footstep command to the NAO robot.
 }

 srv {
  0.name = footstep_srv
  0.type = humanoid_nav_msgs/StepTargetService
  0.desc = Sends a footstep command to the NAO robot. The service blocks until the footstep has been executed.

  1.name = clip_footstep_srv
  1.type = humanoid_nav_msgs/ClipFootstep
  1.desc = Clips a footstep into the range executable by the NAO robot.
 }

 param {
  0.name = ~init_stiffness
  0.type = float
  0.desc = initial stiffness (defaults to 0 so it doesn't strain the robot when no teleoperation is running), set to 1.0 if you want to control the robot immediately
  0.default = 0.0
 }
}

node.5 {
 name = nao_leds
 desc = `nao_leds` can control all the LEDs on the NAO. It also allows to activate a customazible blinking behavior.
 goal {
  0.name = blink
  0.type = naoqi_msgs/BlinkGoal
  0.desc = NAO will blink with a color chosen at random from `colors`, the duration of the actual blink is determined by `blink_duration` and the blinking rate is assumed to be normal with mean `blink_rate_mean` and standard deviation `blink_rate_sd`. The background color while the robot is not blinking is set to `bg_color`. This behavior runs until either a new !BlinkGoal is sent or the current goal is cancelled.
 }
 sub {
  0.name = fade_rgb
  0.type = naoqi_msgs/FadeRGB
  0.desc = Set the leds represented by `led_name` to `color`. Transisition lasts for `fade_duration`. For more information about valid names refer to [[http://www.aldebaran-robotics.com/documentation/naoqi/sensors/alleds.html|the NAOqi documentation]].
 } 
}
node.6 {
 name = nao_speech
 desc = Node leverages both !NaoQi's text-to-speech and speech recognition engines and exposes them to ROS. It is possible to have several concurrent nodes of this type, each one configured with different parameters.
 sub {
  0.name = speech
  0.type = std_msgs/String
  0.desc = Text to be said over Nao's speech synthesis.
 }
 pub {
  0.name = word_recognized
  0.type = naoqi_msgs/WordRecognized
  0.desc = Words and confidence levels detected with Nao's speech recognition system.
 }
 srv {
  0.name = reconfigure
  0.type = std_srvs/Empty
  0.desc = Call to reconfigure node using ROS parameters, useful if parameters have been updated since node start-up.
  1.name = start_recognition
  1.type = std_srvs/Empty
  1.desc = Start Nao's speech recognition system. The vocabulary parameters needs to be set for the call to succeed. Only one node can use the speech recognition at any given time.
  2.name = stop_recognition
  2.type = std_srvs/Empty
  2.desc = Stop speech recognition. Useful to allow other nao_speech nodes to start the speech recognition system.
 }
 param{
  0.name = ~voice
  0.type = string
  0.default = current voice
  0.desc = Set NAO's voice
  
 1.name = ~language
 1.type = string
 1.default = current language
 1.desc = Set NAO's language (both text-to-speech and speech recognition)
 
 2.name = ~volume
 2.type = float
 2.default = current volume
 2.desc = Set NAO's voice volume

 3.name = ~vocabulary
 3.type = list of strings
 3.default = empty list
 3.desc = List of words to be recognized by NAO. Must not be empty for speech recognizer to work.
 
 4.name = ~enable_audio_expression
 4.type = boolean
 4.default = current value
 4.desc = Enable speech recognizer's audio expression

 5.name = ~enable_visual_expression
 5.type = boolean
 5.default = current value
 5.desc = Enable speech recognizer's visual expression

 6.name = ~word_spotting
 6.type = boolean
 6.default = false
 6.desc = Enable word spotting (recognizing words in the middle of a speech) only if your NAO supports it (>v4)
}

goal {
  0.name = speech_action/goal
  0.type = naoqi_msgs/SpeechWithFeedback
  0.desc = Text to be spoken by Nao's speech synthesis
  1.name = /speech_vocabulary_action/goal
  1.type = naoqi_msgs/SetSpeechVocabulary
  1.desc = List of words to be recognized by NAO. Must not be empty for speech recognizer to work. 
}

}

node.7 {
 name = nao_tactile
 desc = Publishes sensor data of Nao's tactile sensors and bumpers. A message is sent whenever the state of the touch sensors or bumpers change, and the full state (pressed / touched or not) is sent.
 pub{
  0.name = tactile_touch
  0.type = naoqi_msgs/TactileTouch
  0.desc = Contains information about which tactile button on Nao's head was touched
  1.name = bumper
  1.type = naoqi_msgs/Bumper
  1.desc = Contains information about which bumper (left or right) was triggered.
  2.name = foot_contact
  2.type = std_msgs/Bool
  2.desc = Indicates whether at least one of the feet touches the ground.
 }
}

node.8 {
 name = nao_walker
 desc = `nao_walker` provides teleoperation with an omnidirectional walk by wrapping the Aldebaran Python NaoQI API. Accessing Nao's speech synthesis is also possible with the topic `speech`.
 sub{
  0.name = cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = Omnidirectional velocity (x, y, and theta) for the walking engine
  1.name = cmd_pose
  1.desc = Send a goal in cartesian coordinates to the walking engine
  1.type = geometry_msgs/Pose2D
  2.name = cmd_step
  2.desc = Send footsteps to the walking engine
  2.type = humanoid_nav_msgs/StepTarget
 }

 param {
  0.name = ~step_frequency
  0.type = double
  0.desc = Maximum fraction of Nao's step frequency to be used when walking (between 0 and 1). This controls how fast (and stable) Nao is walking.
  0.default = 0.5

  2.name = ~use_walk_pose
  2.type = boolean
  2.desc = Slowly move from init pose to walk pose before walking to avoid toppling over backwards (might improve stability for naoqi versions >= 1.10.10, not tested for other versions)
  2.default = False

  3.name = ~enable_foot_contact_protection
  3.type = boolean
  3.desc = Enable or disable foot contact protection in robot's motion configuration. If this parameter is not specified, the current setting will not be changed.

  4.name = ~use_foot_gait_config
  4.type = boolean
  4.desc = Enable or disable using a foot gait configuration for all walk commands. Disabling will use the Default gait configuration saved on the Nao.
  4.default = False

  5.name = ~foot_gait_config
  5.type = ALValue/Tupel
  5.desc = A list of the gait config parameters, see the NAOqi API for more information.

  6.name = ~init_stiffness
  6.desc = initial stiffness (defaults to 0 so it doesn't strain the robot when no teleoperation is running), set to 1.0 if you want to control the robot immediately
  6.type = float
 }
 srv{
  0.name = read_foot_gait_config_srv
  0.type = std_srvs/Empty
  0.desc = Reads the values from ~use_foot_gait_config and ~foot_gait_config and sets them. This can be used to change the current foot gait config during runtime.
    1.name = cmd_vel_srv
    1.desc = Send a velocity to the walking engine
    1.type = naoqi_msgs/CmdVelService

    2.name = cmd_step_srv
    2.desc = Send a footstep target to the walking engine
    2.type = humanoid_nav_msgs/StepTargetService

    3.name = cmd_pose_srv
    3.desc = Send a pose in cartesian coordinates to the walking engine
    3.type = naoqi_msgs/CmdPoseService

    4.name = stop_walk_srv
    4.desc = Stop walking immediately
    4.type = std_srvs/Empty

    5.name = needs_start_walk_pose_srv
    5.desc = Sets a flag indicating whether the robot should go to a posture suitable for walking first before starting to walk
    5.type = std_srvs/Empty
    6.name = enable_arms_walking_srv
    6.desc = Enable or disable swinging the arms while walking
    6.type = naoqi_msgs/SetArmsEnabled
  }


 }
}
```


