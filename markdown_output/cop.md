# Configuring cop

The package
[cognitive_perception](http://www.ros.org/doc/api/cognitive_perception/html/index.html)
build a library called cop and a service called cop_srv.

The package cop contains examples of configurations for this service.

The configuration is a XML-file that is passed as the first command line
parameter to the cop_srv and starts a set of rosservices in the node
named by the second command line parameter (careful with ros launch
files here).

. A cop config is a xml file. it contains a \<config\> node with the
following sub elements:

. . \<[VisualFinder](cop/VisualFinder)/\>: Configures algorithms used
for localizing special objects or concepts.

. . \<[VisLearner](cop/VisLearner)/\>: Configures algorithms used to
learn new Descriptors or to classify existing objects

. . \<[ImageInputSystem](cop/ImageInputSystem)/\>: Configures the sensor
setup loaded on start up

. . \<[SignatureDB](cop/SignatureDB)/\> Configures the available
Descriptors on start up

. . \<[AttentionManager](cop/AttentionManager)/\>:

An example might look like:

```
<?xml version="1.0" encoding="ISO-8859-1"?>
  <config>
    <VisualFinder>
      ...
    </VisualFinder>
    <VisLearner>
      ...
    </VisLearner>
    <ImageInputSystem>
     ...
    </ImageInputSystem>
    <SignatureDB>
     ...
    </SignatureDB>
    <AttentionManager />
  </config>
```

# Using the /cop/in Service

The main functionality of cop can be used by calling the service at
/\[cop\]/in It is of type vision_srvs/cop_call which looks like this
(rossrv show cop_call): ```
string outputtopic
string[] object_classes
uint64[] object_ids
uint64 action_type
uint64 number_of_objects
vision_msgs/apriori_position[] list_of_poses
  float64 probability
  uint64 positionId
---
uint64 perception_primitive
```

The parameter \'\'outputtopic\'\' specifies the topic on which the
answers are expected. This topic will be advertised by cop, and cop will
wait a while for the caller of this service to subscribe to it, before
publishing the first result.

The parameter \'\'object_class\'\' can take a list of semantic classes
that selects the models that may be used for the specified action. If
one of the given names is not yet registered as a class, it is
considered as a new annotation for all given ids.

The parameter \'\'object_ids\'\' can take a list of objects that selects
the models and signatures that can be used for the requested action.

The parameter \'\'action_type\'\' specifies whether this action is
thought to Localize an object, Track it, Refine (= Learning new
properties and classifying it) it, or just Look it up.

The parameter \'\'number_of_objects\'\' specifies the maximum numbers of
objects that is returned by a the action.

The parameter \'\'list_of_poses\'\' contains at least one position where
the object has to expected. If this value is empty, all actions will
fail, but the Locate action that will try to create candidate regions by
a geometric segmentation, if available.

# Using the /cop/save Service

Next to the default service cop_call cop provides an additional service:
/cop/save

This service is thought to provide a possibility to share some learned
models with other robots. It allows to send an ObjectID (see
\<[SignatureDB](cop/SignatureDB)/\>) and the result will be a local path
of XML-file saving the necessary parameters. Additionally there is a
list of relative paths returned which contains all files referred in the
XML-file that are necessary to create the model.

There exist a test client: Given a running instance of cop: rosrun
test_client save_cop 2

will return something like: Called cop XMLFilename:
/work/klank/src/tumros-internal/perception/cop/resource/signature1280824708.xml
Additional filename 0: plate_brownrings.DXF
