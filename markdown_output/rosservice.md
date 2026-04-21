## See also

The [rossrv](rossrv) tool provides information about [srv](srv) files.

## rosservice command-line tool

The \`rosservice\` command implements a variety of commands that let you
discover which services are currently online from which nodes and
further drill down to get specific information about a service, such as
its type, URI, and arguments. You can also call a service directly from
the command line.

The currently supported commands are: ```
rosservice call	call the service with the provided args
rosservice find	find services by service type
rosservice info	print information about service
rosservice list	list active services
rosservice type	print service type
rosservice uri	print service ROSRPC uri
```

### rosservice args

\`args \<service-name\>\` Print the arguments to a
service.```
$ rosservice args /service_name
```

### rosservice call

\`call \<service-name\> \[service-args\]\` Call a service from the
command line.```
$ rosservice call /service_name service-args
```

e.g.```
$ rosservice call /add_two_ints 1 2
```

\`\--wait\` (*New in ROS 1.1*) Wait until service is advertised before
calling.

#### YAML syntax

Please see [YAML command line](ROS/YAMLCommandLine) for a detailed
description and examples of how to specify service arguments to
\`call\`.

#### Negative numbers

Please see [YAML command line](ROS/YAMLCommandLine) for a detailed
description and examples of how to call \`rosservice\` with
negative-number arguments.

### rosservice find

\`find \<service-type\>\` Display all services of a particular
type.```
$ rosservice find rospy_tutorials/AddTwoInts
```

### rosservice list

\`list\` List all the services that are currently
available.```
$ rosservice list
```

\`list \<namespace\>\` (ROS 0.11) List all services in the specified
namespace.```
$ rosservice list /rosout
```

\`-n\` Include the name of the node that implements the
service.```
$ rosservice list -n
```

### rosservice info (ROS 0.11)

\`info \<service-name\>\` Print information about specified
service.```
$ rosservice info /rosout
```

### rosservice node

\`node \<service-name\>\` Display the name of the node that provides a
particular service.```
$ rosservice node /service_name
```

### rosservice type

\`type \<service-name\>\` Display the type of a
service.```
$ rosservice args /service_name
```0

This is useful in combination with [rossrv](rossrv). For example, to
show the [srv](srv) file that defines a
<service:```
$ rosservice args /service_name
```1>

or with a shell pipe:```
$ rosservice args /service_name
```2

### rosservice uri

\`uri \<service-name\>\` Display the URI of a service. This is useful,
for example, if you wish to know what address a service is
using.```
$ rosservice args /service_name
```3

## Roadmap

\`rosservice\` is a stable command-line tool within the ROS core
toolchain. It\'s currently feature set is not expected expand much.
Currently, the only major feature planned is the ability to use YAML
text files as well as piped YAML input with the \`rosservice call\`
command. This feature is currently not scheduled.
