\'\'\'rve_properties\'\'\' provides a way to store configuration data in
a node similar to how the parameter server works. It differs from the
parameter server in that:

-   It does not require any network lookups, so it\'s much faster
-   It can store arbitrary data in an efficient manner \-- no
    serialization/deserialization required if the type remains the same
-   It can store extra metadata about a property (to, for example,
    notify a UI that it should display a slider with min/max/step
    values)
-   Multiple disconnected trees are allowed
-   It supports callbacks for when properties are modified (technically
    supported by the parameter server, but no client currently supports
    it)

A simple example of using properties: ```cplusplus
PropertyNodePtr pn(new PropertyNode);
uint32_t val = 5;
pn->set("foo/bar/baz", val);
val = pn->get<uint32_t>("foo/bar/baz");
```
