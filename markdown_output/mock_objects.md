This package wraps Mock Objects for a service server, a message
subscriber and a actionlib server.

## Creating a Mock Object

First include the code dependencies and add to your code the following
include files

```
#include "ros/ros.h"
#include "gtest/gtest.h"
#include "mock_objects/MockSubscriber.h"
```

To create a mock subscriber

```
typedef controllersAndSensors_communications::irMsg ir;
MockSubscriber<ir> irSubscriber;
```

Creating a mock action server can be done as in this example:

```
#include "ros/ros.h"
#include "mock_objects/MockActionServer.h"
#include "RoboticArm_communications/moveArmAction.h"

MOCK_ACTION_SERVER(hello,RoboticArm_communications::moveArm)

int main() {
	MockhelloActionServer a("test");
}
```

## Range Checks using mock objects

You can use the mock objects for performing range checks, using the
build in google mock functions. For a message with the definition

```
Header header
int32[5] distance
```

the following range check can be defined:

```
EXPECT_CALL(irSubscriber, subscriberActualCallback(
  Pointee(Field(&ir::distance, ElementsAre(
   AnyOf(IsBetween(0, 800), Eq(-1)),
   AnyOf(IsBetween(0, 300), Eq(-1)),
   AnyOf(IsBetween(0, 300), Eq(-1)),
   AnyOf(IsBetween(0, 800), Eq(-1)),
   AnyOf(IsBetween(40, 300), Eq(-1))))
))).Times(AtLeast(0));
```

where the *IsBetween* is a matcher defined as follows:
```
MATCHER_P2(IsBetween, a, b, std::string(negation ? "isn't" : "is")
+ " between " + PrintToString(a) + " and " + PrintToString(b)) {
  return a <=arg;
}
```

Note that you need to add the following lines too
```
using ::testing::AtLeast;
using ::testing::Eq;
using ::testing::AllOf;
using ::testing::Field;
using ::testing::Pointee;
using ::testing::PrintToString;
using ::testing::ElementsAre;
using ::testing::Matcher;
using ::testing::AnyOf;
```

### Complex Logical Rules

Combining the Google Mock !AnyOf and !AllOf matchers can provide more
complex rules for range checks. For example:

```
EXPECT_CALL(soundExistenceSubscriber, subscriberActualCallback(
  AllOf(
    AnyOf(
      Pointee(Field(&existenceMsg::soundExists, Eq(0))),
      Pointee(Field(&existenceMsg::soundExists, Eq(1)))
    ),
    Pointee(Field(&existenceMsg::certainty, IsBetween(0,1)))
))).Times(AtLeast(0));
```

and a simple or-like statement

```
EXPECT_CALL(lineColorSubscriber, subscriberActualCallback(
   AnyOf(
     AllOf(
        Pointee(Field(&lineMsg::orientation, Eq(1))),
        Pointee(Field(&lineMsg::fromAngle, IsBetween(-XCAM,XCAM))),
        Pointee(Field(&lineMsg::toAngle, IsBetween(-XCAM, XCAM))),
        Pointee(Field(&lineMsg::color, IsBetween(1,4)))),

     AllOf(
        Pointee(Field(&lineMsg::orientation, Eq(2))),
        Pointee(Field(&lineMsg::fromAngle, IsBetween(-YCAM, YCAM))),
        Pointee(Field(&lineMsg::toAngle, IsBetween(-YCAM, YCAM))),
        Pointee(Field(&lineMsg::color, IsBetween(1,4))))

))).Times(AtLeast(0));
```

### Define New Matchers

You can define new matchers to simplify rules. For example, checking a
message that has x,y,z that all messages fall into a sphere of a
specific distance, we first define a matcher:

```
MATCHER_P(DistanceIsLess, distance, "") {
  return arg.x*arg.x+arg.y*arg.y+arg.z*arg.z < distance * distance;
}
```

and then use it.

### TF matcher

A matcher for the tf is as follows ```
typedef controllersAndSensors_communications::irMsg ir;
MockSubscriber<ir> irSubscriber;
```0

## More Examples

You can find more examples in the [RangeTests](RangeTests) package and
at the
[googlemock documentation](http://code.google.com/p/googlemock/w/list).
