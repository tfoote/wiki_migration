## How to deploy your OROCOS application

Read the
[ OROCOS deployment manual](http://www.orocos.org/stable/documentation/ocl/v2.2.x/doc-xml/orocos-deployment.html )
for detailed information on how to use the deployer.

Run the orocos deployer using rosrun



```
rosrun ocl deployer-gnulinux -ldebug -s deploy.ops
```



Where you define your launch configuration in the deploy.ops script,
e.g.



```python
#import your OROCOS library (dependencies are automatically resolved)
import("my{Ros/OROCOS}Pkg")

#Load your OROCOS component (ComponentName as defined using the ORO_CREATE_* macro and Comp the name as you like the component to be known for the TaskBrowser)
loadComponent("Comp","ComponentName")

#Load properties
loadService("Comp","marshalling")
Comp.marshalling.loadProperties("cpf/myCompProp.cpf")

# Configure / Start components 
Comp.configure()
Comp.start()
```



The myCompProp.cpf file declares the Components properties using XML
syntax:



```
<?xml version="1.0" encoding="UTF-8"?>                                                                                                                            
  <!DOCTYPE properties SYSTEM "cpf.dtd">                                                                                                                            
    <properties>
     <simple name="init_file" type="string"><description>Name of the initialisation file</description><value>init.xml</value></simple>
    </properties>
```



## Roslaunch for OROCOS components

From orocos toolchain 2.2 and onwards, it is possible to start your
OROCOS component(s) using a roslaunch file. In that way you can also
give your component a more understandable name when using the
rtt_ros_integration.

E.g, a roslaunch file myComp.launch to start the ocl deployer in debug
mode and load the deploy.ops script in the myRosPkg package:



```
<launch>                                                                                                                                                 
   <node name="myNodeName" pkg="ocl" type="deployer-gnulinux" launch-prefix="konsole -e" args="-ldebug -s $(find myRosPkg)/deploy.ops --">
   </node>           
  </launch>
```



Important remarks:

-   The arguments you used to pass to the deployer on the command line,
    are now passed using the args attribute. You can use '\$(find
    myRosPkg)' syntax to avoid using absolute file paths.
-   The launch-prefix attribute makes the orocos deployer start in it's
    own terminal, which makes it possible to interact with it.
-   Always append the arguments with two dashes ("\--"). Your launch
    file will not work otherwise: the deployer will start but shutdown
    immediately. This has to do with ROS appending extra arguments to
    the args attribute. The 2 dashes are used to separate the deployer
    arguments from the additional ROS arguments.
-   The deployer might still fail in parsing your deploy.ops script if
    you use it to load additional properties. Nodes started with
    roslaunch are launched from within your HOME directory, which
    probably makes rtt not find the property file. Solution here is to
    either use an absolute path to point to the property file or use the
    [rtt_ros_param](rtt_ros_param) services.
