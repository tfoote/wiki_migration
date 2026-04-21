For instructions on setting up the build on hudson, refer to the
doxygen.

## Links

-   *Hudson Node Url:* <http://build.willowgarage.com/computer/win7-64/>
-   *Hudson Project Url:* <http://build.willowgarage.com/job/roswin/>
-   *Hudson Manual Trigger Url:*
    <http://build.willowgarage.com/job/roswin/build?token=yujin>
-   *Java for Windows Url:*
    <http://java.com/en/download/help/windows_manual_download.xml>

## Machine Setup

-   Install [java](http://www.java.com/en/download/index.jsp)
-   Create a user `rosbuild`.

This is an *ugly*, but necessary constraint of the script on the hudson
server. It also needs a specific directory in which to operate (i.e.
look for the script that needs to be run).

-   Create the working directory and download a few scripts.



```
> mkdir %USERPROFILE%/hudson/workspace/roswin
> cd %USERPROFILE%/hudson/workspace/roswin
> wget --no-check-certificate https://raw.github.com/stonier/win_ros/master/win_sdk/scripts/schebang.bat
> wget --no-check-certificate https://raw.github.com/stonier/win_ros/master/win_hudson/resources/hudson.bat
> wget --no-check-certificate https://raw.github.com/stonier/win_ros/master/win_hudson/resources/slave.jar
```



## Execution

Open the trigger url in a browser:



```
http://build.willowgarage.com/job/roswin/build?token=yujin
```


