## An Example

See <http://worldmodel.willowgarage.com> for an example of this package
in action.

## Getting Started

You should read the
[worldmodel stack page](http://www.ros.org/wiki/worldmodel) for a
high-level description of what this package does; after that, read the
[semanticmodel](http://www.ros.org/wiki/semanticmodel) page to learn how
to gather a database file. (This package is concerned with visualizing a
database).

## Bringing up a database server

Assuming you've created the database in some location such as
`/path/to/db`, run the db server using something like `rosrun mongodb
wrapper.py_database_path:=/path/to/db`. See the [mongodb](mongodb)
package for details. If you're running multiple instances of the db
server on the same machine, you can set the `warehouse_port` ros
parameter to use different ports.

## Bringing up the web server

The web interface uses the [Flask](http://flask.pocoo.org/) web
framework. It can either be run using a production web server such as
Apache or Flask's own debug server. To use Apache, you just need to set
up a wsgi file that imports the application from this package: see the
Flask documentation for details. Simpler (but not recommended for public
networks or heavy use) is to run Flask's own server. This is done with:

```
rosrun semantic_model_web_interface run_server.py
```

The above command brings up the site on port 5000 of the local machine.
You can use a different port by passing it as the single argument to
`run_server.py`. The server will look at the `warehouse_port` ros
parameter to decide which port to look for the db on (defaults to
27017).
