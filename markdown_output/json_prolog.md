This package provides methods for querying the KnowRob ontology via ROS.

# Command-Line Parameters

json_prolog can load the `init.pl` file of a ros package at startup.
Just pass the corresponding ros package name as first parameter.
```
rosrun json_prolog json_prolog comp_germandeli
```

# Client Libraries

Examples on how to use the different client libraries can be found in
the `examples` subdirectory.

## Python

For interfacing json_prolog, the python client library provides the
class Prolog as an interface for making queries and the class
!PrologQuery to encapsulate results.

Solutions are python dictionaries that map variables to their bindings.
Prolog lists are represented as lists. Atoms are represented as strings.
More complex terms are represented as dictionaries with the sole mapping
from `term` to a list of values. The first value is always an atom,
i.e. a python string. The other values can be of any valid result type,
i.e. again a dictionary containing a `term`, a string, a list or a
number.

The class Prolog provides two methods:

-   `query(query_str, incremental=False)`: Performs a query and
    returns a an instance of type !PrologQuery. The `incremental`
    parameter indicates if the query should be processed "at-once",
    i.e. all solutions are generated, or if solutions should be
    generated incrementally. Incrementally generated solutions allow to
    handle queries with an infinite number of solutions. The
    !PrologQuery object provides the following methods:
-   `solutions()`: returns a generator for the solutions of the query.
-   `finish()`: Finishes the query.
-   `once(query_str`: Query for exactly one solution. This returns the
    dictionary of the first solution.

## C++

The main interface class of the C++ client is `json_prolog::Prolog`.
It provides the methods:

-   `query(const std::string &query_str, bool incremental=false)`:
    Performs a query and returns a !PrologQueryProxy object.
-   `once(const std::string &query_str)`: Performs a query and returns
    the first solution.

The class `json_prolog::!Prolog` provides a very simplistic container
like interface to a sequence of bindings. In particular, it provides the
methods `begin()` that returns an iterator to the beginning of the
prolog result, `end()` that returns a past-end iterator and the method
`finish()` to close the query.

Dereferencing a !PrologQueryProxy::Iterator returns an instance of type
`json_prolog::!PrologBindings`. This class essentially is a
std::map<std::string, json_prolog::!PrologValue> that maps variables
to their actual values. The !PrologValue class is a wrapper around
boost::any with support for the types

-   double
-   int
-   string
-   list
-   term
-   empty

To check if a !PrologValue contains a specific type, it provides the
methods

-   `type()`: returns the contained type.
-   `isValid()`: returns true if it contains a valid type (i.e.
    non-empty)
-   `isDouble()`
-   `isInt()`
-   `isString()`
-   `isTerm()`
-   `isList()`

To get the value as a specific type, the casting operator to the desired
type and the method as<type>() are implemented.

Lists are represented as std::vector<!PrologValue>. Terms are
represented by the special class !PrologTerm which provides the
following method:

-   `name()`: Returns the name of the term
-   `arity()`: Returns the arity
-   `values()`: Returns a std::vector<!PrologValue> containing the
    "parameters" of the term
-   `operator\[\]`: Returns the !PrologValue at a specific index

The method `toString` returns a pretty printed representation of the
contained value.

## Java

An example client can be found in the examples directory.

# Communication format

Communication between a json_prolog server and its clients is performed
through 4 services:

## Node API

```clearsilver
srv{
0.name=~query
0.type=json_prolog/PrologQuery
0.desc=Starts a query. The slot `query` has to be a valid JSON encoded query. The format is specified below.

1.name=~simple_query
1.type=jsonProlog/PrologQuery
1.desc=Starts a query. The slot `query` has to be a valid expression of the underlying prolog implementation. It doesn't have a special encoding.

2.name=~next_solution
2.type=json_prolog/PrologNextSolution
2.desc=Request the next solution for a query. Automatically finishes the query when there are no more solutions. The format of the result is explained below.

3.name=~finish
3.type=json_prolog/PrologFinish
3.desc=Finishes a query and frees all acquired resources.
}
```

## JSON Format

Prolog expressions are either *terms*, *atoms*, *numbers*, *lists* or
*variables*. All types apart from terms, lists and variables are
represented by their native JSON format. Terms, lists and variables are
represented as dictionaries with exactly one mapping. For terms, they
contain a mapping from `term` to a list with the name of the term as
first element and the parameters as the rest of the list. For lists,
they contain a mapping from `list` to the (JSON) list of the members.
For variables, they contain a mapping from `variable` to the name of
the variable. Strings should always be enclosed by \\" to prevent the
JSON parser from doing something stupid. The following example shows how
a the Prolog query ```
member(X, [1, 2, 3]), Y = foo(X)
``` should be encoded:
```
{\"term\":[\",\",{\"term\":[\"MEMBER\",{\"variable\":\"X\"},{\"list\":[1,2,3]}]},{\"term\":[\"=\",{\"variable\":\"Y\"},{\"term\":[\"foo\",{\"variable\":\"X\"}]}]}]}
```

Please note that for calling the service `query`, the outer map has to
be omitted, i.e. only the list corresponding to the outer `term` must
be passed to the service.

Results are maps of variables to values in the format specified above.
For instance, a Prolog query ```
X = 1, Y = 2
``` results in one
solution of the form ```
{\"X\":1, \"Y\":2}
```
