## Overview

To annotate data on Mechanical Turk, we need to store it on our task
management server. The annotations are structured in sessions and work
units. Each work unit belongs to a session and produces one or more
submission.

This package provides tools for sending the data to the annotation
server and receiving the data from it. The communication happens over
XML-RPC and some transfers occur over plain HTTP.

The mech_turk package has no semantic information about the data being
transfered. As such, no conversions is done by this package. It provides
only raw data.

## Authentication and server names

Much of the server API requires authenticated user. To avoid typing the
passwords all the time, the mech_turk package uses a config file
(\"/.ros/.mech_turk/auth.txt\") to keep the user credentials. The file
has very simple format: ```
server_alias:{
  server: server_name[:port],
  user:   user_name,
  pwd:    user_password
}
...
``` e.g.
```
test: {
  server: vm6.willowgarage.com,
  user: mt_tester,
  pwd: some-not-important-password
}
default: {
  server: mech_turk.willowgarage.com,
  user: mt_worker,
  pwd: some-not-important-password
}
```

After a server alias is declared in the `auth.txt`, it can be used in
all mech turk commands using \"\--server=ALIAS\". For convenience,
\"\--server=default\" is assumed as a default value.

## Using command line tools

To submit raw data to the session, we can use submit_work_units.py:
```
rosrun mech_turk submit_work_units.py --session=test_session data/work_unit_*.xml
```

Once the work is completed, we can download the submissions and the
original work units through get_raw_session_results.py:
```
rosrun mech_turk get_raw_session_results.py --session=test_session --saveto=results/all_results --filter=none
```

If we have Q/A enabled, we can restrict the download to only good
results: ```
rosrun mech_turk get_raw_session_results.py --session=test_session --saveto=results/all_results --filter=none
```
