## Deprecated

(!) [rx](rx) packages are replaced by [rqt](rqt), which is available for
fuerte and later. [rqt_graph](rqt_graph) succeeds \`rxgraph\`.

## Command-line tools

### rxgraph

\`rxgraph\` display a visualization of a ROS
[Computation Graph](ROS/Concepts), i.e. the ROS [nodes](Nodes) that are
currently running, as well as the ROS [topics](Topics) that connect
them.

[![](attachment:Screenshot-rxgraph.png)](attachment:Screenshot-rxgraph.png)

*NOTE: Screenshot is of rxgraph in ROS 1.1. Older version does not have
right-hand pane or filter bar.*

#### Usage

```
Usage: rxgraph [options]

Options:
  -h, --help            show this help message and exit
  -o DOTFILE, --dot=DOTFILE
                        ouput graph as graphviz dot file
```

\`-o DOTFILE\`, \`\--dot=DOTFILE\` \`rxgraph\` can save a
[GraphViz](http://www.graphviz.org/) \"dot\" file of the ROS graph. This
is useful for producing documentation of your online system.

**New in ROS 1.1**

\`\--nodens=NAMESPACE\` Only display nodes in specified namespace.

\`\--topicns=NAMESPACE\` Only display topics in specified namespace.

**Removed in ROS 1.1**

The \`-q\` and \`-t\` options were removed from the command-line and
replaced with \'quiet\' and \'All topics\' check-boxes in the toolbar.

The quiet option removes the following nodes: ```
['/diag_agg', '/runtime_logger', '/pr2_dashboard', '/rviz', 
'/rosout', '/cpu_monitor', '/monitor','/hd_monitor', '/rxloggerlevel', '/clock']
```

Usually, topics are marked with edges and nodes by ellipses. The \'All
topics\' option makes the topics appear as rectangles. It also makes
those topics visible which have either no publishers or no subscribers.
