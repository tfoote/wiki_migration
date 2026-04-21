**This package is not maintained any more and mainly provided as an
example how perception systems can be interfaced. Please contact the
stack maintainer if you plan to use it.**

## CopROSClient

Client that listens to CoP messages and asserts them in the KnowRob
knowledge base

There are two kinds of relevant messages: Database updates and object
detections. The first ones are important for the knowledge base to be
aware of which objects can currently be recognized, the second ones for
knowing which objects have been detected at which positions.

This node starts two threads that subscribe to the respective topics
/knowrob/cop_db (for DB updates) and /kipla/cop_reply (for object
detections, as triggered by kipla). Two separate worker threads read the
objects and create the respective structures in the knowledge base.

The following commands launch KnowRob and start the CoP listener. You
will get a list of models printed to the console (the current state of
the CoP database) after calling the cop_listener(_) predicate.
```
rosrun rosprolog rosprolog comp_cop
 comp_cop:cop_listener(_).
```

### Adding mappings from Cop to KnowRob identifiers

These mappings are defined in the file comp_cop/prolog/comp_cop.pl in
the form ```
cop_to_knowrob('placemat', 'http://ias.cs.tum.edu/kb/knowrob.owl#PlaceMat').
```

You can simply add new lines here and the system will know them after
restarting comp_cop.

## BarcodeWebLookup

The comp_cop package also provides a node for looking up a barcode on
the web, which is important to interpret the result of the CoP barcode
detection.

Given an EAN number (as string), the node queries upcdatabase.com for a
description of the object, parses the returned HTML and returns the
object class label as the result.

```
rosrun comp_cop BarcodeWebLookup
 rosservice call /barcode_web_lookup '!!str 40084015'
```
