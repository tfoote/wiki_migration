roscs integrates C#-written programs into ROS. It only provides support
for mono under linux. A Windows extension is not planned.

# Setup

C# programs running under mono dynamically load assemblies (i.e., \*.dll
files) from one of three locations:

-   The current path
-   A path listed in the environment variable \$MONO_PATH
-   The global assembly cache (gac)

In the following, we assume that \$MONO_PATH is set to a common library
path. All C#-assemblies should be built into that path.

# Building

In order to build your own C# assemblies and executables the following x
simple steps are needed:

-   Let your package depend on roscs, by editing the manifest.xml
-   Include the roscs cmake file into your CMakeLists.txt:
    `rosbuild_include(roscs cncs)`
-   Use the following macros for building:

  -- --------------------------------------------- -- -------------------------------------------------------------------------------------------------- --
     `CSHARP_ADD_TARGET_DEPENDENCY(target deps)`      adds the dependencies deps to target. Only use target names or assembly names without extension.   
  -- --------------------------------------------- -- -------------------------------------------------------------------------------------------------- --

Example: ```
CSHARP_ADD_TARGET_DEPENDENCY(myExecutable myLibrary Mono.C5 otherLibrary)
```

  -- --------------------------------- -- --------------------- --
     `CSHARP_ADD_LIBRARY(lib files)`      build a C# assembly   
  -- --------------------------------- -- --------------------- --

Example: ```
CSHARP_ADD_LIBRARY(myLibrary src/mycode.cs src/myclass.cs)
```

  -- ----------------------------- -- ----------------------- --
     `CSHARP_ADD_EXE(exe files)`      build a C# executable   
  -- ----------------------------- -- ----------------------- --

Example: ```
CSHARP_ADD_EXE(myExe src/mymain.cs src/myclass.cs)
```

  -- ----------------------------------------- -- ----------------------------------- --
     `CSHARP_ADD_PKG_DEPENDENCY(target dep)`      add a dependency using pkg-config   
  -- ----------------------------------------- -- ----------------------------------- --

Example: ```
CSHARP_ADD_PKG_DEPENDENCY(myLibrary gtk-sharp-2.0)
```

  -- ----------------------------------- -- ---------------------------------------------------------------- --
     `CSHARP_ADD_RESOURCE(target res)`      add a resource to the target (similar to `dmcs -resource:res`)   
  -- ----------------------------------- -- ---------------------------------------------------------------- --

-   In order to generate wrapper code for ROS functionality such as
    publishing and subscription, add the following line to your
    CMakeLists.txt: `rosbuild_gen_cs_msg()`

This command, similar to rosbuild_genmsg() will generate and compile all
neccessary code. The major difference to rosbuild_genmsg() is that code
for **all** messages that occur in packages your package depends on will
be generated and built. In other words, all messages stemming from the
complete dependency graph, starting from your package will be wrapped.

-   If you want to use service or define services, additionally call
    `rosbuild_gensrv()` from within the CMakeLists.txt

# Using the wrapped API

Your targets will automatically be linked against the generated message
libraries. The root namespace for all generated code is RosCS and each
package defines its own sub-namespace, i.e., RosCS.std_msgs.

API documentation for the main functionality is available here:
<https://cn-roscs-ros-pkg.googlecode.com/git/roscs/apidoc/index.html>.

The following example illustrates the wrapped API:
```
using System;
using System.Threading;
using RosCS;
using RosCS.std_msgs;

namespace Example
{
	public class RosCsExample
	{
		Node node;
		Publisher pub;
		public RosCsExample()
		{
			this.node = Node.MainNode;
			this.pub = new Publisher(this.node,"DummyTopic",RosCS.std_msgs.String.TypeId,1);
			this.node.Subscribe("DummyTopic",OnMessage,6);
			
		}
		public void OnMessage(RosCS.std_msgs.String msg) {
			Console.WriteLine("Got message: "+msg.Data);
		}
		public void Run() {
			int i = 0;
			while(RosSharp.Ok()) {
				RosCS.std_msgs.String msg = new RosCS.std_msgs.String();
				msg.Data ="Hello "+i;
				this.pub.Send(msg);
				i++;
				Thread.Sleep(1000);
			}			
		}		
		public static void Main(string[] args) {			
			RosSharp.Init("NodeName",args);			
			RosCsExample rce = new RosCsExample();
			rce.Run();
		}
	}
}
``` Note that only asynchronous message handling is
supported.

# Known Issues and Limitations

-   Due to the fact that all messages that a package can possibly use
    given its dependency graph are wrapped, compilation takes a rather
    long time. In the future, this will probably be eliviated using
    proxy packages for non-c# packages.
-   There is a rare race-condition in the build chain, when multiple
    packages depend on the same package are built at the same time. If
    this happens, recompile or recompile with only one thread. Proxy
    packages as above will fix this issue.
