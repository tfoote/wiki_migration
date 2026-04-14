This package provides basic functions for testing ROS interfaces.

## Testing Node Existence

For example a Google Test can check if a node named
\"/navigation/plannerNode\" exists as follows:

```
TEST(NAVIGATIONtest, plannerNode) {
     EXPECT_TRUE(InterfaceTester::checkForNode("/navigation/plannerNode"));
}
```

The same test can be performed in a simple if structure (e.g. for a
diagnostic)

```
if (!InterfaceTester::checkForNode("/navigation/plannerNode")){
    stat.add("/navigation/plannerNode","Down");
}
```

## Testing Topics & Services

Similar to testing node existence there exist a few other functions

### Testing for Services

```
TEST(NAVIGATIONtest, navigationMapDataSrvTest)
{
  EXPECT_TRUE(InterfaceTester::checkForService("/navigation/navigationMapSrv"));
  EXPECT_TRUE(InterfaceTester::checkForNodeService("/navigation/navigationMapSrv","/navigation/"));
}
``` This test if the Service
/navigation/navigationMapSrv has been advertised and if the a node in
the /navigation/ namespace provides that service.

### Testing for Topic Subscription

We can test if a node is subscribed to a specific topic

```
TEST(NAVIGATIONtest, sensorsIrSubscriberTest)
{
  EXPECT_TRUE(InterfaceTester::checkForSubscribed("/sensors/ir"));
  EXPECT_TRUE(InterfaceTester::checkForSubscribedNode("/sensors/ir","/navigation/"));
}
```

The first EXPECT_TRUE tests if the topic /sensors/ir has been advertised
(either by a subscriber or a publisher). The second EXPECT_TRUE tests
that a node in the /navigation namespace is subscribed at the
/sensors/ir topic.

We could also test for a specific node like this:
```
EXPECT_TRUE(InterfaceTester::checkForSubscribedNode("/sensors/ir","/navigation/planner"));
```

### Testing for Topic Publishing

Similar to the previous section, we can test if a topic has been
published:

```
TEST(CONTROLLERSANDSENSORStest, sensorsIrPublisherTest)
{
  EXPECT_TRUE(InterfaceTester::checkForTopicPublishing("/sensors/ir","controllersAndSensors_communications/irMsg"));
  EXPECT_TRUE(InterfaceTester::checkForNodePublishing("/sensors/ir","/sensors/"));
}
```

The first line of code checks if the topic /sensors/ir that has been
advertised is of type controllersAndSensors_communications/irMsg The
second line checks if a node in the /sensors/ namespace is actually
publishing to the /sensors/ir topic. By publishing, we mean that a
Publisher has been created on that node (and no actual message sending)

## More Examples

You can find more examples in the
[interface_tester](http://www.ros.org/wiki/interface_tester) package.
