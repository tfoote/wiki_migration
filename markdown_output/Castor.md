Castor is mainly used to read in write robot specific configuration
files.

# Requirements

Castor, as well as all packages that use it require that the environment
variable ES_ROOT is set to a valid directory. Robots are identified by
the environment variable ROBOT, or, if that is not set, by the hostname
of the system.

Castor will therefore look for configuration files in: 1.
ES_ROOT/etc/ROBOT 2. ES_ROOT/etc/hostname 3. ES_ROOT/etc If it cannot
find the requested file, an exception will be thrown. Castor aklso
allows to read the configuration files of other robots, such that some
reasoning with respect to their parameters can be done.
