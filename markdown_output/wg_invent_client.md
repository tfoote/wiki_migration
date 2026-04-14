## WG Inventory System

The Willow Garage Inventory System, known as \"Invent\", stores as
device history record (DHR) for components of the PR2 and other Willow
Garage products. The inventory system is located at
<http://invent.willowgarage.com>.

A separate, \"debug\", system exists at <http://cmi.willowgarage.com>.
This system contains a mirror of the real Invent database for debugging
and testing.

### Invent Overview

The device history record contains data for individual parts and
products used at Willow Garage.

### Invent vocabulary

-   \'\'\'Product/Part\'\'\' - Type of component. Ex: Hokuyo laser
    scanner
-   \'\'\'Item\'\'\' - Serialized component. Ex: Prosilica camera
    #109104
-   \'\'\'Reference\'\'\' - Unique identifier that can be attached to an
    individual part. This is usually a manufacturer\'s serial number or
    MAC address.
-   \'\'\'Sub-items/Children\'\'\' - Any items that are assembled into
    the current item.
-   \'\'\'Location/Parent\'\'\' - Location a part can be stored or moved
    to.
-   \'\'\'Key-Value\'\'\' - Items can have arbitrary keys, stored with
    designated values. All qualification tests set the \"Test Status\"
    key to \"PASS\".
-   \'\'\'Attachment\'\'\' - Attachment files of any binary type can be
    linked to an item or part.

#### Serial Numbers

Invent serial numbers are of the form: ```
68-0XXXX-0YYYY
``` The
first values, \`XXXX\`, are the part number. All Hokuyo laser scanners
have the part number \"3134\". The second, \`YYYY\`, is the serial
number of the device. Serial numbers are increasing from \"0000\" for
each device.

#### Users

Invent allows users to:

-   Lookup items by serial number or \"reference\"
-   Assemble components together
-   Move items to a new location
-   Print barcode labels
-   Add or edit notes for items or products
-   View testing data for different products
-   Add new part numbers to Invent

Administrators can:

-   Add or edit users
-   Delete or edit key-value of an item or product
-   Delete notes or testing data

Invent also has a client API, which this package provides an interface
to. Users can use the client API to query and modify the Invent
database.

## WG Inventory Client

This package contains the client API for using the WG Inventory System.
The client can be used from any computer, even outside of Willow Garage,
as long as the user has the correct permissions.

### Client Example

```python
from wg_invent_client import Invent

# Initialize client
iv = Invent(username, password)
iv.login() 

# Check that component is valid
if not iv.check_serial_valid(serial) or not iv.check_assembled(serial):
    raise InvalidItemException("The item %s is not properly assembled or is invalid" % serial)

# Pull all attachments
attachs = iv.list_attachments(serial)

# Check that we've pass qualification tests
if iv.get_test_status(serial):
    iv.setNote(serial, "Item has finished with all testing")
```

Client functions will log in automatically. Calling the \`login()\`
method can be useful to check a username and password.

### Analyzing Test Data

Test data is analyzed using the
[wgtest_data_analysis](wgtest_data_analysis) package.

## Device History Record (DHR) API

The following is a summary of the functions currently needed for the
Device History Record API.

Below is the unfinished API for the WG inventory system.

### Device History

When processing diagnostic logs, it is important to be able to recall
the history of moves of every part of the robot to compute use.

1\. User can get a list of historical changes to the composition or
membership of a serialized component. 1. pseudo-code:
```
get_history(serial_number)
``` 1. returns a list of changes 1. Each change is
a list comprising the datetime of the change followed by a string for
the type of change, either `Parent` or `Children`

This will allow a precise record of move. The goal is to process .bag
files of diagnostics by MCB serial numbers, and associate them with the
correct assemblies, and other components (slip rings, etc).
