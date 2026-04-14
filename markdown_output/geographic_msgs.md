Geographic information messages.

\<\<MsgSrvDoc(geographic_msgs)\>\>

## Unique Identifiers

Map points, features and segments all have universally unique identifier
names
([UUID](http://en.wikipedia.org/wiki/Universally_unique_identifier)),
using \<\<MsgLink(uuid_msgs/UniqueID)\>\> messages.

Each UUID is stored as an array of unsigned bytes. UUID generation is up
to the programmer, but the intent is for matching features within a
domain such as Open Street Map to yield the same UUID. The
[unique_id](unique_id) package provides C++ and Python interfaces for
generating them: use the \`fromURL()\` method on a URL constructed from
the map source.

For example, the Open Street Map URL scheme is:

-   \`http:*openstreetmap.org/node/999999\` \*
    \`http:*openstreetmap.org/way/999999\`
-   \`http:*openstreetmap.org/relation/999999\`*

Here, \`999999\` is the decimal representation of the integer OSM node,
way, or relation ID without leading zeros.

Other map sources should use similar conventions.

## Cartography

The \<\<SrvLink(geographic_msgs/GetGeographicMap)\>\> service takes a
map URL and optional \<\<MsgLink(geographic_msgs/BoundingBox)\>\>,
returning a \<\<MsgLink(geographic_msgs/GeographicMap)\>\>,

The map contains a \<\<MsgLink(geographic_msgs/WayPoint)\>\> vector and
a \<\<MsgLink(geographic_msgs/MapFeature)\>\> vector. Each point or
feature is identified by a \<\<MsgLink(geographic_msgs/UniqueID)\>\>,
and optional \<\<MsgLink(geographic_msgs/KeyValue)\>\> properties
describing their roles.

Features represent any interesting collection of map points: hiking
trails, bicycle paths, streets, highways, tunnels, bridges, rivers,
buildings, property boundaries, etc. They contain a sequence of
component unique identifiers, which may name points or other features. A
feature may not directly or indirectly contain itself, so its
subordinate points and features must form a tree structure. But, a
feature may belong to more than one higher-level feature.

## Route Network

Not all way points in a map are drivable by any particular vehicle. Some
delimit buildings, rivers, or property boundaries. The
\<\<MsgLink(geographic_msgs/RouteNetwork)\>\> message represents
drivable paths as a directed graph using a
\<\<MsgLink(geographic_msgs/WayPoint)\>\> vector and a
\<\<MsgLink(geographic_msgs/RouteSegment)\>\> vector. Each segment
represents an edge from one point to another. Unless the path is
one-way, another segment will point in the opposite direction.
