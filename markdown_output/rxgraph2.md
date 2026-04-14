\'\'\'Invoking rxgraph2: \'\'\'

You will need to have roscore running on a machine somewhere that you
can access over the network before rxgraph2 will be able to do anything
interesting.

Currently you just have to launch rxgraph2 as an Eclipse project. Later
it should be possible to launch it using rosrun after we have figured
out how to package the necessary jar files. It should also be possible
to launch it from a browser using Java Web Start.

\'\'\'Possibly setting the ROS_MASTER_URI:\'\'\' On startup, rxgraph2
may prompt you to enter the ROS_MASTER_URI if it can\'t access your
environment variables or ROS_MASTER_URI is not defined in your
environment variables.

\'\'\'The default view, topics=vertices:\'\'\'

Typically, this step shouldn\'t be necessary, and rxgraph2 should
immediately make two windows, one containing a graph and one containing
a variety of controls.

By default, the graph window shows ROS nodes as circular blue graph
vertices and topics as square orange graph vertices. To avoid confusion,
we always use the term \"vertex\" and not \"node\" when talking about a
vertex of the graph. We always use the term \"node\" when talking about
a ROS node. In this default graph view, an arrow going from a node
vertex to a topic vertex indicates that the node publishes the topic,
and an arrow going from a topic vertex to a node vertex indicates that
the node subscribes to the topic. Each vertex has its name displayed.

\'\'\'Navigating in the graph view:\'\'\'

Drag: move camera

Mouse scroll wheel: zoom in and out (zooming in will not make the vertex
icons appear bigger, so it is a good way to make the graph more legible
if the text labels are overlapping)

Ctrl-drag: Shear transformation of view

Shift-drag: Rotates the view

Option-drag: Moves whole window (probably won\'t do this if you aren\'t
running Gnome; it is part of Gnome \"look and feel\")

\'\'\'The topics=edges view:\'\'\'

It is also possible to draw topics as edges. This shows node-to-node
connectivity more explicity and reduces graph clutter. However, some
information is lost because any topic with no publshers or no
subscribers is not drawn at all.

You can switch between the topics=edges view and the topics=nodes view
using the radio button pair in the \"Draw topics as\...\" panel of the
\"rxgraph controls\" window.

By default, the names of topics are not displayed in topics=edges mode
because the text gets too cluttered. However, the \"\...with labels\"
checkbox may be used to turn them on.

\'\'\'The magnifying glass:\'\'\'

To read the labels on tightly packed vertices without losing your camera
position, check the \"Use magnifying glass\" checkbox. This displays a
grey oval that magnifies the items underneath it. You can move the
magnifying glass by dragging the small circle at its center, and change
its magnification power using ctrl+the scroll wheel of the mouse. You
can resize the magnifying glass by dragging on its border.

\'\'\'The filter manager:\'\'\'

In the \"rxgraph controls\" window there is a panel labeled \"Filters
(applied top to bottom)\". This box controls both which vertices and
edge are displayed, as well as how the vertices and edges are colored.

The filter manager contains several filters that have been pre-loaded
for your convenience, but you can also define your own.

Each filter is defined by a row in the filter manager. On the leftmost
side of the filter is a checkbox that determines whether the filter is
active. Try checking the box next to the filter that reads \"exclude
nodes+topics with any property\". The entire graph should go blank.
Checking that box made the filter active, and it excluded all nodes and
topics.

Now click the \"add new filter\" button at the bottom of the filter
manager. A new filter, enabled by default, should appear. It should read
\"include nodes+topics with no subscribers\". If you are in
topics=vertices mode, this may make some vertices appear (depending on
what is running on your core). Click on the drop-down menu in the new
filter that reads \"no subscribers\" and change it to \"name\". A new
field reading \"contains\" should appear followed by a textbox. Type
\"rosout\" into the textbox. You have just created a new filter that
reads \"include nodes+topics with name contains rosout\" and you should
see at least one node called rosout and at least one topic called rosout
on the graph. (These are always brought up when you bring up roscore).
This example illlustrates the principle that filters are applied in top
to bottom order. First, \"exclude nodes+topics with any property\" at
the top of the filter manager excludes everything. Then \"include
nodes+topics with name contains rosout\" displays them again.It is
possible to add filters at any point in the chain by using either the
\"add new filter\" button to add a filter that will be applied after all
filters, or if you want to add a filter that will be applied right
before an existing filter, click the \"+\" button on the right side of
the existing filter. Clicking the \"-\" button will delete a filter (but
don\'t forget you can also turn them off without deleting them just by
unchecking their check boxes)

Uncheck the box next to each of the two filters you have running. Now
make sure you are in topics=vertices mode and click the checkbox for the
preloaded filter reading \"warn about topics with no publishers\". You
will probably see a few vertices such as \"/time\" turn red. The warning
system allows you to write filters to highlight conditions that you are
interested in. You can change the \"no publishers\" variable to \"name\"
to search for nodes or topics with a given name and highlight it red,
for instance.

As of this writing, all of the filters available to rxgraph can always
run with certainty. Later, there might be new filters that could fail to
evaluate immediately, for example if they depend on getting data over
the network. If someone has added such features since this writing, you
may see topics or nodes turn green. A green topic or node indicates that
one or more of your filters that is needed to determine rxgraph should
warn about a node can\'t be run at the current moment. Note: if one
filter has already turned warnings on for a node/topic, but another
filter is unable to run, the display color will be red, not green.

\'\'\'The preloaded filters\'\'\'

The preloaded filters each serve a particular purpose.

Exclude nodes+topics with any property: this lets you clear the graph,
and then add new filters to show just the few pieces you are interested
in.

Exclude nodes and exclude topics with any property are similar.

Warn about topics with no publishers: This often indicates a naming
problem, where a node doesn\'t receive a topic it wants because it has
subscribed to the wrong topic name.

Warn about topics with no subscribers: This shows what topics are not
actually being used. It can be useful for tracking down naming problems.

Exclude topics with no subscribers: This excludes unused topics and can
reduce graph clutter considerably in the topics=vertices view.

\'\'\'Changing the ROS_MASTER_URI:\'\'\'

If the ROS core goes down or becomes uncontactable while rxgraph2 is
running, it will prompt you to enter a new ROS_MASTER_URI. You can wait
as long as you want to enter the new URI, so you can always bring up the
old core and enter the same URI again. You can also click \"cancel\" to
quit rxgraph2.

\'\'\'Quitting rxgraph2:\'\'\'

To quit at any time, close the graph display window.
