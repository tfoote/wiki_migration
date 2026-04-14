: filters is now a separate stack. In previous releases, it was part of
[common](common).

## Pre-requisite: Pluginlib

Filters are closely linked to [pluginlib](pluginlib). Please make sure
that you are familiar with the [pluginlib documentation](pluginlib)
before continuing.

## Using Filters

It is recommended to use a \`filters::FilterChain\` whenever using more
than one instances of \`filters::Filter\`. However, you need to
understand the base Filter C++ API first before using the Filter Chain
API.

### Filter

The core of the \`filters\` Package is a templated base class
\`filters::FilterBase\<TemplateType\>\` which defines the external API
to any filter. The methods are \`configure()\` and \`update()\`. It also
provides helper methods for a Filter implementation. To use a Filter
simply instantiate it in your code.

Filters are configured from parameters on the
[Parameter Server](Parameter Server). The configure method passes in the
parameter namespace to read from of the Parameter Server.

#### Currently Implemented Filters

-   [MeanFilter](/MeanFilter)
-   [MedianFilter](/MedianFilter)
-   [IncrementFilter](/IncrementFilter)
-   [TransferFunctionFilter](/TransferFunctionFilter)

#### Filter ROS Parameters

A Filter expects to find a map with three elements: \`name\`, \`type\`
and \`params\`.

\`name\` (\`string\`) a unique name for debugging purposes within the
chain being used. \`type\` (\`string\`) the Filter\'s typename as
declared in it\'s [pluginlib](pluginlib) registration. \`params\`
(\`map\`) data to present to the Filter implementation.

#### Example configuration

```yaml
parameter_namespace_passed_to_configure:
  name: unique_name
  type: FilterName
  params: { param1: a, param2: b}
```

### Filter Chain

The \`filters::FilterChain\` class has been designed to facilitate
dynamically loading a sequence of Filters based on runtime parameters.
The Filter Chain is configured from the
[Parameter Server](Parameter Server) just like Filters. Based on the
parameters the Filter Chain will dynamically load the Filters by their
name.

The public API looks just like the Filter API with \`configure()\` and
\`update()\` methods.

#### Filter Chain ROS Parameters

\`filter_chain\` (list(Filters)) Parameter containing properly formatted
Filters. See [Filter ROS Parameters](#FilterParameters).

#### Example configuration

```
param_namespace_passed_to_configure:
  filter_chain:
    -
      name: median_test_unique
      type: MultiChannelMedianFilterDouble
      params: {number_of_observations: 5}
    - 
      name: median_test2
      type: MultiChannelMedianFilterDouble
      params: {number_of_observations: 5}
```

#### Using a Filter Chain

Here\'s an example of a multi-channel filter chain for doubles. To do a
non-vector style use a \`filters::FilterChain\<double\>\` and change
\`in\` and \`out\` to type \`double\`.

Initialization: ```
filters::MultiChannelFilterChain<double> chain("double"); //Node template type and argument must match
chain.configure("param_namespace_passed_to_configure");
std::vector<double> in, out;
```

Process data: assuming in is populated ```
chain.update(in, out);
```

## Implementing a Filter

Implementing a \`Filter\` is simply a specific form of a dynamically
loaded class for [pluginlib](pluginlib).

### Steps to create a filter

1\. Create a class which inherits from \`FilterBase\<T\>\` a. Implement
\`configure()\` method a. Implement \`update()\` method 1. In the source
for the class call ```
PLUGINLIB_REGISTER_PLUGIN(UniqueFullClassNameSoSpecialCharacters, my_package::ClassName, filters::FilterBase<Type>)
```: A new simpler plugin macro
is now recommended: ```
PLUGINLIB_EXPORT_PLUGIN(my_package::ClassName, filters::FilterBase<Type>)
``` 1. Create a plugin
description file, see [pluginlib](pluginlib) 1. Add an export to your
[manifest.xml](Manifest) pointing to the plugin description file, see
[pluginlib](pluginlib) 1. Make sure you depend on the \`filters\`
package in your [manifest.xml](Manifest).

## MultiChannelFilterBase and MultiChannelFilterChain

This whole document refers simply to \`filters::FilterBase\` and
\`filters::FilterChain\`. However there are \`MultiChannel\` versions of
both. Instead of the templated data type, \`T\`, they expect
\`std::vector\<T\>\` on the update calls. And the configure method has
one extra argument which is the number of channels expected(aka how many
elements are expected in the \`vector\`).
