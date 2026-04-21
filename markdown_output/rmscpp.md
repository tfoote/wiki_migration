## About

The `rmscpp` package is a client library, written in C++, for the
[rms](rms) (Robot Management System) [REST API](rms/rest). This library
allows for external programs to interact with the RMS MySQL database. By
doing so, we are able to do things like parse log data from user studies
externally, or write ROS nodes which retrieve, add, or modify data
within the RMS system itself.

## Installation

To install the `librms` stack, you can choose to either install from
source, or from the Ubuntu package:

### Source

To install from source, execute the following: 

```shell
cd /path/to/your/ros/stacks
git clone https://github.com/WPI-RAIL/librms.git
roscd librms
rosdep install librms
rosmake librms
```



### Ubuntu Package

To install the Ubuntu package, execute the following:


```
sudo apt-get install ros-fuerte-librms
```



## Library Example

In the following example, we will make both an unauthenticated call, and
an authenticated call to the RMS API. This tutorial assumes that you
have [installed the RMS](rms/Tutorials/InstallTheRMS) locally; however,
it can be easily adapted to access a remote server.

### The C++ Code



```cplusplus
/*
 * A simple example that utilizes the RMS library from the rmscpp package.
 *
 * Author: Russell Toris - rctoris@wpi.edu
 *
 * Version: November 15, 2012
 */

#include <iostream>
#include <rmscpp/rms.h>

using namespace std;
using namespace rms;

int main(int argc, char **argv)
{
  // create a connection to the RMS
  rms_client client("localhost");

  // first, let's count the number of articles per page
  vector<content_page> pages = client.get_content_pages();
  for (uint i = 0; i < pages.size(); i++)
  {
    // grab the articles for this page
    int pageid = pages.at(i).get_pageid();
    vector<article> articles = client.get_articles_by_pageid(pageid);

    // notify us of how many articles we found
    string title = pages.at(i).get_title();
    cout << "Content Page \"" << title << "\" has " 
           << articles.size() << " article(s)." << endl;
  }

  // now let's try and make a call we do not have permission to make yet
  try
  {
    client.get_user_accounts();
  }
  catch (string &error)
  {
    cerr << endl << "ERROR: " << error << endl;
  }

  // if we authenticate, we will be able to make the call successfully
  client.set_authorization("admin", "myremotelab");
  vector<user_account> users = client.get_user_accounts();
  cout << endl << "There are " << users.size() << " user(s)." << endl;
}
```



### Code Explanation

Now that we have a running example, let's look at each piece.

In order to utilize the RMS library, we must import the single client
header file. We also include the `iostream` header to allow for
terminal printing.

We start by creating a client object that will connect to `localhost`
using the default parameters (i.e., port `80`, and using HTTP).

First, we will make a call that requires no authentication. This basic
example will grab a list of all content pages in the RMS, and then count
the number of articles that were found for that given page. This
information is printed to the terminal.

Next, we attempt to grab a list of all of the user accounts. This call
requires an admin to be authenticated. To illustrate what will happen if
you do not authenticate, we surround the call in a `try-catch` block.
The error string that is reported is the one that comes from the
[API](rms/rest).

Finally, we authenticate (using the default admin password supplied with
the base install of RMS), and make the call again. We then report the
number of users found in the system.

## Support

Please send bug reports to the
[GitHub Issue Tracker](https://github.com/WPI-RAIL/librms/issues). Feel
free to contact me at any point with questions and comments.

-   [Russell Toris](Russell Toris)
-   <rctoris@wpi.edu>
-   [Academic Website](http://users.wpi.edu/~rctoris/)

------------------------------------------------------------------------

  -- ------------------------------------------------- -- ---------- -- -------------------------- --
     <tablewidth="100%"> ![](attachment:wpi.png)      <:99%>      ![](attachment:rail.png)   
  -- ------------------------------------------------- -- ---------- -- -------------------------- --
