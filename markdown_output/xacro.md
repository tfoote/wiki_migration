\'\'\'Modern wiki: <https://github.com/ros/xacro/wiki>\'\'\'

------------------------------------------------------------------------

This package is most useful when working with large XML documents such
as robot descriptions. It is heavily used in packages such as the
[urdf](urdf). See for example,
[this tutorial](urdf/Tutorials/Using Xacro to Clean Up a URDF File) for
how xacro is used to simplify urdf files. See
[here](https://github.com/ubi-agni/human_hand/blob/master/model/human_hand.urdf.xacro),
for an example showing the use of the advanced features (python
evaluation, yaml integration) introduced in Jade.

## Use of new features on Indigo

Many of the features highlighted as \"New in Jade\" below are also
accessible from Indigo. To use them, the \`\--inorder\` flag is
required. This flag is discussed [below](#Processing_Order), and for
some background information see this
[pull request](https://github.com/ros/xacro/issues/110#issuecomment-144589000).
Put simply, this flag is used to trigger Jade-enabled xacro processing
on Indigo.

## Example

Consider the following Xacro XML snippet:

```
<xacro:macro name="pr2_arm" params="suffix parent reflect">
  <pr2_upperarm suffix="${suffix}" reflect="${reflect}" parent="${parent}" />
  <pr2_forearm suffix="${suffix}" reflect="${reflect}" parent="elbow_flex_${suffix}" />
</xacro:macro>

<xacro:pr2_arm suffix="left" reflect="1" parent="torso" />
<xacro:pr2_arm suffix="right" reflect="-1" parent="torso" />
``` This snippet expands to:

```
<pr2_upperarm suffix="left" reflect="1" parent="torso" />
<pr2_forearm suffix="left" reflect="1" parent="elbow_flex_left" />
<pr2_upperarm suffix="right" reflect="-1" parent="torso" />
<pr2_forearm suffix="right" reflect="-1" parent="elbow_flex_right" />
``` If we also define macros for pr2_upperarm and
pr2_forearm, then this snippet could expand to describe an entire
robotic arm.

The remainder of this document describes the features of xacro.

## Property and Property Blocks

Properties are named values that can be inserted anywhere into the XML
document. Property blocks are named snippets of XML that can be inserted
anywhere that XML is allowed. Both use the property tag to define
values.: Properties are local if defined inside of a \`xacro:macro\`.
See [Local properties](#Local_properties).

The following example shows how to declare and use a property:

```
<xacro:property name="the_radius" value="2.1" />
<xacro:property name="the_length" value="4.5" />

<geometry type="cylinder" radius="${the_radius}" length="${the_length}" />
``` The two properties are inserted into the
geometry expression by placing the names inside dollared-braces (\${}).
If you want a literal \"\${\", you should escape it as \"\$\${\".

Here\'s an example of using a property block:

```
<xacro:property name="front_left_origin">
  <origin xyz="0.3 0 0" rpy="0 0 0" />
</xacro:property>

<pr2_wheel name="front_left_wheel">
  <xacro:insert_block name="front_left_origin" />
</pr2_wheel>
```

## Math expressions

Within dollared-braces (\${}), you can also write simple math
expressions. Currently, basic arithmetic and variable substitution is
supported. Here\'s an example:

```
<xacro:property name="radius" value="4.3" />
<circle diameter="${2 * radius}" />
```:

Since ROS Jade, Xacro employs \`python\` to evaluate expressions
enclosed in dollared-braces, \`\${}\`. This allows for more complex
arithmetic expressions. Functions and constants from the \`python\` math
module (e.g. \`pi\` and trigonometric functions) are available for use.
Examples:

```
<xacro:property name="R" value="2" />
<xacro:property name="alpha" value="${30/180*pi}" />
<circle circumference="${2 * pi * R}" pos="${sin(alpha)} ${cos(alpha)}" />
<limit lower="${radians(-90)}" upper="${radians(90)}" effort="0" velocity="${radians(75)}" />
```

## Conditional Blocks

Xacro has conditional blocks similar to roslaunch. This is useful for
things like configurable robots or loading different Gazebo plugins. It
follows this syntax:

```
<xacro:if value="<expression>">
  <... some xml code here ...>
</xacro:if>
<xacro:unless value="<expression>">
  <... some xml code here ...>
</xacro:unless>
``` The expression needs to evaluate to \"0\",
\"1\", \"true\", or \"false\", otherwise an error will be thrown.: The
more powerful evaluation capabilities in ROS Jade allow for much more
complex expression. Virtually any python expression that evaluates to a
Boolean is feasible:

```
<xacro:property name="var" value="useit"/>
<xacro:if value="${var == 'useit'}"/>
<xacro:if value="${var.startswith('use') and var.endswith('it')}"/>

<xacro:property name="allowed" value="${[1,2,3]}"/>
<xacro:if value="${1 in allowed}"/>
```

## Rospack commands

Xacro allows you to use certain rospack commands with
dollared-parentheses (\`\$()\`).

```
<foo value="$(find xacro)" />
<foo value="$(arg myvar)" />
``` Xacro currently supports most of the rospack
commands that roslaunch supports using
[substitution args](roslaunch/XML#substitution_args) (with the exception
of \`eval\`, see
[here](https://github.com/ros/xacro/issues/225#issuecomment-543311376)).
Arguments need to be specified on the command line using the
\`myvar:=true\` syntax.: Since ROS Indigo, it is also possible to define
defaults like so:

```
<xacro:arg name="myvar" default="false"/>
``` Using this you can run xacro like:

```
<pr2_upperarm suffix="left" reflect="1" parent="torso" />
<pr2_forearm suffix="left" reflect="1" parent="elbow_flex_left" />
<pr2_upperarm suffix="right" reflect="-1" parent="torso" />
<pr2_forearm suffix="right" reflect="-1" parent="elbow_flex_right" />
```0 In xacro files, \`args\` is a \_global\_
dictionary accessible from within any included file or macro.

## Macros

The main feature of xacro is its support for macros. Define macros with
the macro tag, and specify the macro name and the list of parameters.
The list of parameters should be whitespace separated. They become
macro-local properties.

```
<pr2_upperarm suffix="left" reflect="1" parent="torso" />
<pr2_forearm suffix="left" reflect="1" parent="elbow_flex_left" />
<pr2_upperarm suffix="right" reflect="-1" parent="torso" />
<pr2_forearm suffix="right" reflect="-1" parent="elbow_flex_right" />
```1 The example declares a macro \"pr2_caster\",
which takes two parameters: suffix and origin. Note that \"origin\" is
starred. This indicates that origin is a block parameter instead of a
simple text parameter. Look ahead to the use of pr2_caster. The suffix
property is defined in the pr2_caster tag as an attribute, but no origin
property is defined. Instead, origin refers to the first element inside
(the \"pose\" block, in this case). The double-starred version
(\"content\", \"anothercontent\") allows to insert an arbitrary number
of elements that are passed within elements subsequently available
(\"container\", \"another\" respectively in the example above). This
example expands to the following:

```
<pr2_upperarm suffix="left" reflect="1" parent="torso" />
<pr2_forearm suffix="left" reflect="1" parent="elbow_flex_left" />
<pr2_upperarm suffix="right" reflect="-1" parent="torso" />
<pr2_forearm suffix="right" reflect="-1" parent="elbow_flex_right" />
```2 Multiple block parameters will be processed in
the specified order:

```
<pr2_upperarm suffix="left" reflect="1" parent="torso" />
<pr2_forearm suffix="left" reflect="1" parent="elbow_flex_left" />
<pr2_upperarm suffix="right" reflect="-1" parent="torso" />
<pr2_forearm suffix="right" reflect="-1" parent="elbow_flex_right" />
```3 Macros may contain other macros. The outer
macro will be expanded first, and then the inner macro will be expanded.
For example:

```
<pr2_upperarm suffix="left" reflect="1" parent="torso" />
<pr2_forearm suffix="left" reflect="1" parent="elbow_flex_left" />
<pr2_upperarm suffix="right" reflect="-1" parent="torso" />
<pr2_forearm suffix="right" reflect="-1" parent="elbow_flex_right" />
```4 becomes:

```
<pr2_upperarm suffix="left" reflect="1" parent="torso" />
<pr2_forearm suffix="left" reflect="1" parent="elbow_flex_left" />
<pr2_upperarm suffix="right" reflect="-1" parent="torso" />
<pr2_forearm suffix="right" reflect="-1" parent="elbow_flex_right" />
```5Comments in front of macros will be removed
during processing. They are considered to be related to the macro (e.g.
explaining the macro). If you want to keep a comment in the final
document, separate it with an empty line from the macro.

### Default parameters === Macro parameters can have default values:

```
<pr2_upperarm suffix="left" reflect="1" parent="torso" />
<pr2_forearm suffix="left" reflect="1" parent="elbow_flex_left" />
<pr2_upperarm suffix="right" reflect="-1" parent="torso" />
<pr2_forearm suffix="right" reflect="-1" parent="elbow_flex_right" />
```6 If the defaults contain evaluation
expressions, they will be evaluated at instantiation time.Often, you
need to pass external variables into local macro params (as above for
x). To ease this task, you can employ the \^ syntax:

```
<pr2_upperarm suffix="left" reflect="1" parent="torso" />
<pr2_forearm suffix="left" reflect="1" parent="elbow_flex_left" />
<pr2_upperarm suffix="right" reflect="-1" parent="torso" />
<pr2_forearm suffix="right" reflect="-1" parent="elbow_flex_right" />
```7 The caret \^ indicates to use the outer-scope
property (with same name). The pipe \| indicates to use the given
fallback if the property is not defined in outer scope.

### Local properties ===Properties and macros defined within a macro are local to this macro, i.e. not visible outside. Using the optional attribute \`scope=\"parent \| global\"\`, a property definition can be exported to the parent scope of a macro (or the global scope).

## Including other xacro files

You can include other xacro files using the \`xacro:include\` tag:

```
<pr2_upperarm suffix="left" reflect="1" parent="torso" />
<pr2_forearm suffix="left" reflect="1" parent="elbow_flex_left" />
<pr2_upperarm suffix="right" reflect="-1" parent="torso" />
<pr2_forearm suffix="right" reflect="-1" parent="elbow_flex_right" />
```8 The file \"other_file.xacro\", will be
included and expanded by xacro.: Relative filenames are interpreted
relative to the currently processed file. \'\'\'Note\'\'\': When
including files within a macro, not the macro-defining but the
macro-calling file is the one that processes the include! \$(cwd)
explicitly allows to access files in the current working directory.

To avoid name clashes between properties and macros of various included
files, you can specify a namespace for the included file - providing the
attribute ns:

```
<pr2_upperarm suffix="left" reflect="1" parent="torso" />
<pr2_forearm suffix="left" reflect="1" parent="elbow_flex_left" />
<pr2_upperarm suffix="right" reflect="-1" parent="torso" />
<pr2_forearm suffix="right" reflect="-1" parent="elbow_flex_right" />
```9 Access to namespaced macros and properties is
achieved by prepending the namespace, separated by a dot:

```
<xacro:property name="the_radius" value="2.1" />
<xacro:property name="the_length" value="4.5" />

<geometry type="cylinder" radius="${the_radius}" length="${the_length}" />
```0

## YAML support == Properties can be dictionaries or lists too - manually declared with python syntax, like so:

```
<xacro:property name="the_radius" value="2.1" />
<xacro:property name="the_length" value="4.5" />

<geometry type="cylinder" radius="${the_radius}" length="${the_length}" />
```1 or loaded from [YAML](YAML%20Overview) files
like so:

```
<xacro:property name="the_radius" value="2.1" />
<xacro:property name="the_length" value="4.5" />

<geometry type="cylinder" radius="${the_radius}" length="${the_length}" />
```2 Note, the evaluation brackets \${}
distinguishing evaluation from plain text definition. Calibration data
is an ideal candidate to be loaded from YAML.

The xacro property loaded from a YAML file is treated as dictionary. So
if `props.yaml` is loaded into the `props` xacro property (as above) and
contains ```
<xacro:property name="the_radius" value="2.1" />
<xacro:property name="the_length" value="4.5" />

<geometry type="cylinder" radius="${the_radius}" length="${the_length}" />
```3 you can access `val1` using

```
<xacro:property name="the_radius" value="2.1" />
<xacro:property name="the_length" value="4.5" />

<geometry type="cylinder" radius="${the_radius}" length="${the_length}" />
```4

## Building from CMakeLists.txt

The following snippet shows how to use xacro during a package\'s make
call:

```
<xacro:property name="the_radius" value="2.1" />
<xacro:property name="the_length" value="4.5" />

<geometry type="cylinder" radius="${the_radius}" length="${the_length}" />
```5: While this cmake code provides full control
over the target name and build order, there is a conveniency macro too:

```
<xacro:property name="the_radius" value="2.1" />
<xacro:property name="the_length" value="4.5" />

<geometry type="cylinder" radius="${the_radius}" length="${the_length}" />
```6 If you want the generated files to have a
\`.urdf\` extension it is possible to provide input files terminating
with \`.urdf.xacro\`, the \`.xacro\` suffix will be removed by the CMake
function. This results in files with a \`.urdf\` extension.

## Elements and Attributes ==: In order to add elements or attributes with a dynamically defined name, you can use the special xacro tags \`\<xacro:element\>\` and \`\<xacro:attribute\>\`:

```
<xacro:property name="the_radius" value="2.1" />
<xacro:property name="the_length" value="4.5" />

<geometry type="cylinder" radius="${the_radius}" length="${the_length}" />
```7 Usage example for \`\<xacro:attribute\>\`:

```
<xacro:property name="the_radius" value="2.1" />
<xacro:property name="the_length" value="4.5" />

<geometry type="cylinder" radius="${the_radius}" length="${the_length}" />
```8 gives:

```
<xacro:property name="the_radius" value="2.1" />
<xacro:property name="the_length" value="4.5" />

<geometry type="cylinder" radius="${the_radius}" length="${the_length}" />
```9

## Processing Order

Classicly, xacro first loads all includes, then processes all property
and macro definitions and finally instantiates macros and evaluates
expressions. Thus, \'\'\'later property or macro definitions will
override previous ones\'\'\'. Additionally, the conditional tags, \<if\>
and \<unless\>, have no effect on macro or property definitions nor the
inclusion of additional files.:

Since ROS Jade, xacro provides the command-line option \`\--inorder\`,
that allows to process the whole document in read order. Hence the
latest definition of a property or macro \'\'\'seen so far\'\'\', will
be used. This is a much more intuitive evaluation process that allows
for some nice new features as well:

-   Inclusion of files can be postponed or completely suppressed if the
    \<include\> tag is placed within a macro or within conditional tags
    respectively.

```{=html}
<!-- -->
```
-   Include filenames can be specified via properties or macro
    parameters.
-   By changing properties at the global scope, the instantiation of a
    macro can yield different results if these properties are used in
    the macro.
-   Property definitions can be conditional.
-   Macros can define properties within a local scope without affecting
    outside stuff.

Because \--inorder processing is much more powerful, in future versions
beyond Jade, the new processing style will become default and you should
check the compatibility of your xacro files. Usually, both processing
styles should give identical results. You can easily check this like so:

```
<xacro:property name="front_left_origin">
  <origin xyz="0.3 0 0" rpy="0 0 0" />
</xacro:property>

<pr2_wheel name="front_left_wheel">
  <xacro:insert_block name="front_left_origin" />
</pr2_wheel>
```0 If there are any differences shown, you should
check and adapt your xacro file. A common reason will be the late
loading of calibration data (as properties). In this case, simply move
them up front, i.e. before usage. To facilitate search for wrongly
placed property definitions, you can run xacro with option
\`\--check-order\`. If there are any problematic properties, they will
be listed on stderr:

```
<xacro:property name="front_left_origin">
  <origin xyz="0.3 0 0" rpy="0 0 0" />
</xacro:property>

<pr2_wheel name="front_left_wheel">
  <xacro:insert_block name="front_left_origin" />
</pr2_wheel>
```1 Using the command-line option \`-vv\` or
\`-vvv\` one can increase verbosity level to log all defintions of
properties.

## Unrolling loops

By recursively calling a macro, it is also possible to unroll a loop and
generate multiple similar XML snippets for a list of \`items\`:
```
<xacro:property name="front_left_origin">
  <origin xyz="0.3 0 0" rpy="0 0 0" />
</xacro:property>

<pr2_wheel name="front_left_wheel">
  <xacro:insert_block name="front_left_origin" />
</pr2_wheel>
```2

## Deprecated Syntax ==:

While in previous versions, xacro tags without the namespace prefix were
accepted, this sloppy syntax is strongly discouraged as it prevents the
use of those tags in the final XML. Since Jade, this syntax is
deprecated and you should update your files accordingly. The following
script will update your files for you:

```
<xacro:property name="front_left_origin">
  <origin xyz="0.3 0 0" rpy="0 0 0" />
</xacro:property>

<pr2_wheel name="front_left_wheel">
  <xacro:insert_block name="front_left_origin" />
</pr2_wheel>
```3 To suppress the legacy interpretation of
sloppy xacro tags and allow their usage in the target XML, you can use
the command line option \`\--xacro-ns\`.

## Debugging Syntax Errors

To get more verbose syntax error output run following command which
generates urdf from xacro and checks for errors in syntax:

```
<xacro:property name="front_left_origin">
  <origin xyz="0.3 0 0" rpy="0 0 0" />
</xacro:property>

<pr2_wheel name="front_left_wheel">
  <xacro:insert_block name="front_left_origin" />
</pr2_wheel>
```4 Or: ```
<xacro:property name="front_left_origin">
  <origin xyz="0.3 0 0" rpy="0 0 0" />
</xacro:property>

<pr2_wheel name="front_left_wheel">
  <xacro:insert_block name="front_left_origin" />
</pr2_wheel>
```5
