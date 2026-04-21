## Documentation

The simple_robot_control library provides a simple interface to move the
PR2s arms, grippers, base, head and torso. C++ and Python API available.
Arm, Gripper, Head, Base and Torso objects can be instantiated and
calling their functions will move the robot. For moving the arms in
cartesian space the arm planners need to be launched by calling:



```
launch/simple_robot_control_without_collision_checking.launch
```



or to enable planning with obstacle avoidance 

```
launch/simple_robot_control.launch
```



C++ interface:



```
#include <ros/ros.h>

#include <simple_robot_control/robot_control.h>


int main(int argc, char** argv){



	ros::init(argc, argv, "robot_control_test_app");
	ros::NodeHandle nh;

	//Create robot controller interface
	simple_robot_control::Robot robot;

	//look straight
	robot.head.lookat("torso_lift_link", tf::Vector3(0.1, 0.0, 0.0));

	//do stuff with arms
	robot.left_arm.tuck();
	robot.right_arm.stretch();

        //specify joint angles for two waypoints
	double tuck_pos_right[] 
           = { -0.4,0.0,0.0,-2.25,0.0,0.0,0.0,
               -0.01, 1.35, -1.92, -1.68, 1.35, -0.18,0.31};
	std::vector<double> tuck_pos_vec(tuck_pos_right, tuck_pos_right+14);
	robot.right_arm.goToJointPos(tuck_pos_vec);

	robot.right_arm.stretch();

        //grab position from above
	robot.right_arm.moveGripperToPosition(tf::Vector3(0.6,-0.1, 0.0),    
                 "torso_lift_link", simple_robot_control::Arm::FROM_ABOVE);
        
        //grab position frontal
	robot.right_arm.moveGripperToPosition(tf::Vector3(0.8,-0.1, 0.1), 
                    "torso_lift_link", simple_robot_control::Arm::FRONTAL);

        //specify grab pose with postion and orientation as StampedTransform
	tf::StampedTransform tf_l (tf::Transform(tf::Quaternion(0,0,0,1), 
           tf::Vector3(0.8,0.1,0.0)),
           ros::Time::now(),"torso_lift_link","doesnt_matter");
	robot.left_arm.moveGrippertoPose(tf_l);

	//look at left gripper
	robot.head.lookat("l_gripper_tool_frame");

	//drive 0.5m forward
	robot.base.driveForward(0.5);

	//raise torso to 10cm above lowest position
	robot.torso.move(0.1);

	return 0;

}
```


