## Prerequisites

This package requires the [kdl_acc_solver](kdl_acc_solver) package to be
installed.

## Example code for PR2

An example C++ code for doing inverse kinematics with the PR2 is given
under **src/pr2_kdl_wrapper_example.cpp** :

```cplusplus

#include <ros/ros.h>
#include <ros/console.h>
#include <iostream>
#include <kdl_wrapper/kdl_wrapper.h>


int main(int argc, char *argv[])
{
    /// initialize ROS, specify name of node
    ros::init(argc, argv, "pr2_kdl_wrapper_example");


    KDLWrapper pr2_kdl_wrapper;

    if(!pr2_kdl_wrapper.init("torso_lift_link", "r_gripper_tool_frame"))
    {
        ROS_ERROR("Error initiliazing pr2_kdl_wrapper");
    }

    KDL::JntArray q_in(7);
    q_in(0) = 0.0;
    q_in(1) = M_PI/2;
    q_in(2) = 0.0;
    q_in(3) = M_PI/4;
    q_in(4) = 0.0;
    q_in(5) = 0.0;
    q_in(6) = M_PI/3;


    KDL::Twist v_in;
    v_in.vel = KDL::Vector(0.0, 0.2, 0.2);
    v_in.rot = KDL::Vector(0.0, 0.0, 0.0);

    KDL::JntArray q_dot_out;
    ROS_INFO("Calculating inverse kinematics");
    pr2_kdl_wrapper.ik_solver_vel->setLambda(0.3);
    pr2_kdl_wrapper.ik_solver_vel->CartToJnt(q_in, v_in, q_dot_out);

    ROS_INFO("Output q_dot: (%f, %f, %f, %f, %f, %f, %f)",
             q_dot_out(0),
             q_dot_out(1),
             q_dot_out(2),
             q_dot_out(3),
             q_dot_out(4),
             q_dot_out(5),
             q_dot_out(6));

    return 0;
}
```

You can run the example code by doing the following:

1\. Make sure you have the pr2_common metapackage:
```
sudo apt-get install ros-<rosdistro>-pr2-common
``` 2. Upload the PR2 URDF:
```
roslaunch pr2_description upload_pr2.launch kinect:=TRUE
``` 3. Compile the \`kdl_wrapper\` package.

4\. Run the pr2_kdl_wrapper_example : ```
rosrun kdl_wrapper pr2_kdl_wrapper_example
```

## Report a Bug

\<\<GitHubIssues(kth-ros-pkg/kdl_wrapper)\>\>
