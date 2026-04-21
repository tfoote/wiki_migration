## Prerelease

### Web interface

<http://prerelease.ros.org/>

### Command line

Usage: 

```
rosrun job_generation generate_prerelease.py --rosdistro diamondback --email name@foo.bar --stack stackname1 --stack stackname2
```



Extra options:

-   **\--source-only**: Build all the stack dependencies from source
    instead of from Debians. This is useful when the Debian pipeline is
    delayed. Builds using this option can easily take an extra hour to
    complete.
-   **\--repeat n**: Run the regression tests of the stack n times. This
    option helps you to catch spurious test failures.
-   **\--arch x**: Only generate tests for this specific architecture.
    Options are i386 and amd64. It is allowed to specify multiple
    \--arch x blocks
-   **\--ubuntu x**: Only generate tests for this specific Ubuntu
    distribution (e.g. lucid, maverick, \...). It is allowed to specify
    multiple \--ubuntu x blocks
-   **\--delete**: If there is an old (running) job with the same name,
    don't wait for that old job to finish, but instead just delete the
    old job.

## Devel

### Command line

Usage: 

```
rosrun job_generation generate_devel.py --rosdistro diamondback --stack stackname1
```



Extra options:

-   **\--os**: Specify the operating system. 'ubuntu' and 'osx' are
    supported, default is 'ubuntu'.
-   **\--delete**: Delete the corresponding job(s)
