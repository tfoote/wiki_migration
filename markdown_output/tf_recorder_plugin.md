## Plug-in Description

### Functionality

This plug-in records [tf](tf) transforms to an sqlite3 database. It
stores the transformations in a table in order to allow for indexing
over the transforms. The plug-in exposes its functionality as C++
methods an a service call. Spatial indexing requires the tf frames to be
relative to a common frame. Thus, the plug-in transforms all frames into
a reference frame before storing them in the database.

The performance of the sqlite database is not high enough to record tf
frames at their full rate in most cases. Therefore, the plug-in has
support for recording only transforms at a maximal rate.



```clearsilver
 param {
   group.1{
     name = Parameters
     desc = Parameters used to configure tf_recorder_plugin
     0.name = reference_frame
     0.type = string
     0.default = /map
     0.desc = The reference frame all messages are transformed to before storing them in the database.
     1.name = tf_topic
     1.type = string
     1.default = /tf
     1.desc = The topic to record.
     2.name = record
     2.type = bool
     2.default = true
     2.desc = Enable recording of frames. If `false`, the database is unchanged.
     3.name = record_frequency
     3.type = double
     3.default = 0.0
     3.desc = The maximal frequency of tf frames to record. If 0.0, the plug-in records as fast as possible.
          }
       }
     
 srv{
  group.2{
    name = Services
    desc = These are the services that tf_recorder_plugin exposes.
    0.name = lookup_transform
    0.type = tf_recorder_plugin/LookupRecordedTransform
    0.desc = This service allows to lookup a recorded transformation.
        }
     }
```


