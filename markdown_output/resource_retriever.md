## Code API

\`resource_retriever\` has an extremely simple C++ API, consisting of
two classes and one method.

The
[resource_retriever::Retriever](http://www.ros.org/doc/api/resource_retriever/html/classresource__retriever_1_1Retriever.html)
class is the gateway into downloading files. Its \`get()\` method
returns a
[resource_retriever::MemoryResource](http://www.ros.org/doc/api/resource_retriever/html/structresource__retriever_1_1MemoryResource.html)
which contains the file in memory.

The [Retrieving Files](resource_retriever/Tutorials/Retrieving Files)
tutorial details how to use both classes.

\`resource_retriever\` also has a very similar Python API.
