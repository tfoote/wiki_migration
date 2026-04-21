## Overview

The database interface provides an easy way to access SQL databases from
C++ code. In particular, it allows the user to focus on the conceptual
"objects" stored in the database, rather than the database itself. A
C++ class definition is wrapped around an entry in a database table, and
a row of the table corresponds to an instance of the C++ class. For most
common functionality, the user never writes explicit SQL queries.

## Using the Interface

If you are not familiar with the database interface, it is recommended
you go through the following tutorials before proceeding:

-   [Introduction to using the database_interface](database_interface/Tutorials/Introduction to using the database_interface):
    step-by-step, hands-on introduction to using the interface
-   [The SQL database interface: advanced concepts](database_interface/Tutorials/The SQL database interface: advanced concepts):
    all the other details and advanced features of the interface

## Reference Guide

The most stable and commonly used interface methods are covered in the
above tutorials. For a complete reference to the interface functions,
look at the Code API for the
[PostgresqlDatabaseInterface](http://www.ros.org/doc/api/database_interface/html/classdatabase__interface_1_1PostgresqlDatabaseInterface.html)
class.

### Supported SQL databases

The current release provides an interface with PostgreSQL database.
However, most of the code is in place to support sqlite database as
well. This feature will probably be added in a future release

### Advanced Usage

If you are an advanced user requiring complex SQL capabilities, are
wondering why this interface has weird feature X instead of useful
feature Y, or are interested in contributing to this interface, please
see the [Code API](http://www.ros.org/doc/api/database_interface/html).
Most of the code is extensively documented, and discusses our design
choices, shortcomings, possible alternatives, etc.

Please note that this interface is still in a developmental stage. We
are hoping to add more feature to future releases, and your feedback
will be highly valuable.
