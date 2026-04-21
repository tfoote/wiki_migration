This package enables fully immersive control of a PR2 robot using the
Oculus Rift and Razer Hydra.

# What it does

-   Render the Kinect point cloud and robot model to the Oculus Rift
-   Use the Oculus head tracking to control the PR2 head
-   Connect the Hydra to the PR2 joystick teleop (base motion, torso
    lift & gripper control)
-   Track the Hydra motion with the PR2 grippers

# How to run

-   Make sure your desktop computer and the PR2 are time-synchronized
    (e.g. using \`ntpdate\`)
-   Connect your Hydra and Oculus Rift
-   On the robot: \`robot start\`, then \`roslaunch pr2_surrogate
    robot.launch\`
-   On the desktop: \`roslaunch pr2_surrogate desktop.launch\`

# Joystick button

The button assignment is similar to one used for the PS3 joystick in
[pr2_teleop](pr2_teleop).

## Left Paddle

  -- ------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------ --
     **Button**             **Control Action**                                                                                                                                     
     **LB**                 The \"deadman\" control allows the joystick to send commands to the robot; the robot will only respond to the joystick when this button is held down   
     **LT**                 The \"head\" button allows the sticks to control the head instead of the base                                                                          
     **Joystick**           Rotate (yaw) the base                                                                                                                                  
     **1**                  Open left gripper                                                                                                                                      
     **3**                  Close left gripper                                                                                                                                     
     **Center Button**      \"deadman\" switch for controlling the left arm. While pressed, the left PR2 gripper will mimic the movements of the paddle.                           
  -- ------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------ --

## Right Paddle

  -- ------------------- -- -------------------------------------------------------------------------------------------------------------------------------- --
     **Button**             **Control Action**                                                                                                               
     **R1**                 The \"run\" button commands the base to drive faster and enables the texture projector.                                          
     **1**                  Open right gripper                                                                                                               
     **3**                  Close right gripper                                                                                                              
     **4**                  Move the torso up                                                                                                                
     **2**                  Move the torso down                                                                                                              
     **Joystick**           Move (translate) the base                                                                                                        
     **Center Button**      \"deadman\" switch for controlling the right arm. While pressed, the right PR2 gripper will mimic the movements of the paddle.   
  -- ------------------- -- -------------------------------------------------------------------------------------------------------------------------------- --

# Parameters

## desktop.launch

-   **start_hydra:** If true (default), will launch the Razer Hydra
    node.
-   **razer_pos:** Position of the Razer Hydra frame relative to
    torso_lift_link (default: \"1.2 0 -0.3\"). Adjust this e.g. if the
    virtual arms appear to high/low for your setup and body size.

## desktop.launch / robot.launch

-   **audio:** If true, will launch nodes to transmit sound from and to
    the PR2 (default: false).
