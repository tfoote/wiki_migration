## What is rostweet for?

Rostweet is a [twitter](http://www.twitter.com) client for ROS. It
allows your robots to send tweets to its followers, and to receive
tweets from its following contacts. Rostweet can be applied in many
different ways, these are some examples:

-   Communicating progress. Robots running ROS can use rostweet for
    reporting feedback: task progress, failure detection, etc.
-   Sharing new knowledge. After acquiring new information, a robot can
    use rostweet in order to share it with its followers, e.g. how to
    grasp an object, a new environment map, a learnt task, etc.
-   Acquiring new knowledge. By listening to the others' tweets, a new
    source of incoming information is created and can be used for
    enlarging the robot knowledge.
-   Just fun! Let your robot read your tweets, send you a picture, etc.

In general, rostweet can be useful for instantaneous and decentralized
robot-robot, robot-human and human-robot sharing of information. Just
create a twitter account for your robot and start following other robots
(or humans!).

## Installation and usage

Rostweet is delivered as a ROS stack. It can be downloaded from the
uji-ros-pkg google code project repository:

```
$ svn co http://uji-ros-pkg.googlecode.com/svn/trunk/rostweet
```

After downloading and placing it in a folder inside your
`ROS_PACKAGE_PATH`, it should compile with:

```
$ rosmake rostweet
```

and run with:

```
$ rosrun rostweet rostweet
```

This will ask for a twitter username and password and start the node
afterwards (by running the node for the first time, you implicitly
accept rostweet as a twitter application in your account, and allow it
to read your timeline and publish tweets). Once the node is running,
other nodes can subscribe to incoming tweets at
`/rostweet/incomingTweet` (of type `rostweet_msgs/IncomingTweet`),
and publish tweets by calling to the service `/rostweet/postTweet` (of
type `rostweet_msgs/postTweet`). There is an example node for posting
e.g.:

View incoming tweets:

```
$ rostopic echo /rostweet/incomingTweet/tweet
```

Send a tweet:

```
$ rosrun rostweet post "Hello world from rostweet"
```

With rostweet your robots can also share pictures. Use the `post`
executable for an example:

```
$ rosrun rostweet post "Hello world from rostweet" <path_to_picture>
```

For now, rostweet only supports the image media type, although support
for other types of media can be easily added.

## Create a launch file

Without any parameters, each time rostweet is executed, it will ask for
username, password, and will get the OAuth tokens. If you want to skip
some of these steps, you can set them with the following parameters via
[rosparam](rosparam):

-   rostweet/user
-   rostweet/password
-   rostweet/tokenKey
-   rostweet/tokenSecret

After the first execution, the username and token keys are stored in a
file inside the launch/ folder in [YAML](YAML Overview) format. With it
you can easily write a launch file in order to set the parameters
automatically:

```
<launch>
 <node name="rostweet" pkg="rostweet" type="rostweet" output="screen">
 <rosparam command="load" file="$(find rostweet)/launch/paramFile.yaml" />
 </node>
 </launch>
```
