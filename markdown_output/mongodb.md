This package pulls in Mongo DB 1.8 as a 3rd party dependency. Run the db
server using `wrapper.py` in this package.

## ROS Parameters

Private parameters of `wrapper.py`

-   `database_path`: where the db is stored. Defaults to `/tmp/db`.
-   `overwrite`: whether to overwrite existing db. Defaults to false.

There are also some parameters in the parent namespace. These are used
both by `wrapper.py` and client libraries.

-   `warehouse_host`: The hostname of the machine on which the db
    runs. Currently defaults to `localhost` (a smarter default will
    eventually be used).
-   `warehouse_port`: The port on which the db server listens for
    connections. Defaults to 27017.

## Notes

-   MongoDB on a 32 bit system has a max DB size of about 2GB. The
    server should be run on a 64 bit system if possible.
