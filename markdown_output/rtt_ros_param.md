## Loading the rosparam service

### Using an Orocos program script at deployment

/!\\ Make sure you have a roscore running before you start the deployer.

An example script *test.ops*: ```python
import(your_component_package)
import("rtt_ros_param")
loadComponent("YourComponentName","your_component_package::YourComponent")
loadService("YourComponentName","rosparam")
#Store all properties on the ROS parameter server
YourComponentName.rosparam.storeProperties()
#Refresh all properties with the values on the ROS parameter server if available
YourComponentName.rosparam.refreshProperties()
#Store a single property on the ROS parameter server, in the global namespace
YourComponentName.rosparam.storeProperty("PropertyName",false,false)
#Refresh a single property from the ROS parameter server, from the private and relative namespace
YourComponentName.rosparam.refreshProperty("PropertyName",true,true)
```

Which you can run using: ```
rosrun ocl deployer-gnulinux -s test.ops
```

The meaning of the rosparam functions are explained in the next section.

## Available rosparam functions

### Storing Properties on the ROS parameter server

#### Storing a single property

```cplusplus
bool storeProperty(string PropertyName, bool private_namespace, bool relative_component_name)
```

The **storeProperty** function takes 3 arguments: 1. **propertyName**:
this is the name of the Property you want to store 2.
**private_namespace**: a boolean indicating if you want to store the
Property in the private namespace of the deployer 3.
**relative_component_name**: a boolean indicating if you want to store
the Property in the namespace of the component

storeProperty will return *false* if RTT does not know how to store the
Property, this can happen if you do not have a RTT typekit for the
Property type.

This results in 4 possibilities of storing the Property on the parameter
server:

  -- --------------------------------------------- -- -------------- -- -------------------------------------- --
     storeProperty("propertyName",true,true)        *stores in *      /nodeName/componentName/propertyName   
     storeProperty("propertyName",false,true)                         /componentName/propertyName            
     storeProperty("propertyName",true,false)                         /nodeName/propertyName                 
     storeProperty("propertyName",false,false)                        /propertyName                          
  -- --------------------------------------------- -- -------------- -- -------------------------------------- --

#### Storing all properties

```cplusplus
bool storeProperties()
```

This will **always** store all the components properties **in the
private and relative component namespace**:

  -- --------------------------------------- --
     /nodeName/componentName/propertyName1   
     /nodeName/componentName/propertyName2   
     \...                                    
     /nodeName/componentName/propertyNameN   
  -- --------------------------------------- --

### Refreshing Property values from the ROS parameter server

#### Refresh a single properties

```cplusplus
bool refreshProperty(string PropertyName, bool private_namespace, bool relative_component_name)
```

The **refreshProperty** function takes 3 arguments: 1. **propertyName**:
this is the name of the Property you want to refresh 2.
**private_namespace**: a boolean indicating if you want to refresh the
Property from the private namespace of the deployer 3.
**relative_component_name**: a boolean indicating if you want to refresh
the Property from the namespace of the component

refreshProperty will return *false* if the parameter is not found on the
parameter server or if RTT does not know how to compose the Property
value from the paramter value, this can happen if you do not have a RTT
typekit for the Property type.

This results in 4 possibilities of refreshing the Property from the
parameter server:

  -- ----------------------------------------------- -- ------------------- -- -------------------------------------- --
     refreshProperty("propertyName",true,true)        *refreshes from *      /nodeName/componentName/propertyName   
     refreshProperty("propertyName",false,true)                              /componentName/propertyName            
     refreshProperty("propertyName",true,false)                              /nodeName/propertyName                 
     refreshProperty("propertyName",false,false)                             /propertyName                          
  -- ----------------------------------------------- -- ------------------- -- -------------------------------------- --

#### Refresh all properties

```cplusplus
bool refreshProperties()
```

This will **always** refresh all the components properties **from the
private and relative component namespace** if they are availabe, if one
of the properties in not found, refreshProperties will silently go on.
