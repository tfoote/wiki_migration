## Usage

```
rosrun manifest_cleaner stats.py (some/directory/containing/packages) [-web]
```

The script will walk the entire directory structure of the specified
path. The optional -web flag checks the status of the URL specified in
manifest tags (see below)

## Example Report

[A report of all the Debian packages I have installed on my machine](http://www.cse.wustl.edu/~dvl1/stuff/ros/WillowStats.html)

## Statistics Report

### Stack Overview

The first section lists all of the specific properties of any stacks
that were crawled. Example: ```
name                     description brief    license url       review       author                     
======================== =========== ======== ======= ========= ============ ===========================
pr2_common               detailed    detailed BSD     specified Doc reviewed Maintained by John Hsu
```

### Package Overview

The second section lists all the properties for the stacks that were
crawled. Example: ```
name                     description brief    license url       review       author                     
======================== =========== ======== ======= ========= ============ ===========================
pr2_msgs                 detailed    detailed BSD     specified Doc reviewed Eric Berger and many others
```

### Descriptions Summary

Total number of packages that have detailed descriptions and those that
have just the package name.

### Brief Descriptions Summary

Total number of packages that have detailed brief descriptions and those
that have just the package name.

### Review Summary

Total number of contents of the review tag\'s attribute status. Case
sensitive.

### License Summary

Totals for all the licenses listed. Minor parsing is done to separate
out comma separated lists.

### URL Summary

If the \`-web\` tag is not used, the summary will contain whether the
URL tag is specified or not.

If the \`-web\` tag is used, the summary will contain the HTTP response
numbers obtained when the given URL is downloaded. Note that this option
will take a bit longer to run.

### Author Summary

A list of all the authors and the number and list of all the
stacks/packages they maintain. Minor parsing is done to separate comma
delineated lists and email addresses when they are of the form \'My
name/myemail@gmail.com\'.
