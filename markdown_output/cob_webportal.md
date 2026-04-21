# Description

The main goal of the cob_webportal package is extensive support of
distributed development and in particular distributed integration and
test on hardware platforms. It offers

-   Remote access to a hardware platform
-   Remote operation of single software components on the hardware
    platform
-   Debugging and tracing via log files
-   VNC-based forwarding of component visualizations The webportal is
    embedded into a trac environment, such that an integration with
    standard software engineering tools like version control,
    bugtracking, continuos integration and online documentation for the
    hardware platform in form of a wiki is available.

Currently it is configured for the Care-O-bot platform. As the
architecture of the webportal does not rely on a a special hardware or
software framework, it can be easily used for other hardware platforms.

The webportal consists of a control plugin for the remote access and
will be anhanced by a deployment plugin, that allows to choose special
repository versions or releases of the components to be deployed on the
robot hardware for remote tests.

## Access Rights

General access to the hardware is managed by a resource management
plugin to prevent the concurrent operation of two remote users. By a
hierarchical definition of different user rights, multiple users can
participate at remote tests. While one user is operating the components,
the others can e.g. track the component logs or view the visualizations.

The webportal control plugin offers the following user rights:

-   CONTROL_VIEW: View component log windows and visualisations
-   CONTROL_USER: Reserve the hardware for operation
-   CONTROL_OPERATOR: Configuration of existing components, addition of
    new components
-   CONTROL_ADMIN: Administrator rights to configure the plugin itself.

Unless a user with CONTROL_USER or CONTROL_OPERATOR rights has not
reserved the current time slot, he is restricted to the CONTROL_VIEW
rights.

## Available Webportal Services

Shortly web access to a full-fledged gazebo simulation environment of
Care-O-bot 3 including all driver components will be available. The
robot can be controlled in multiple ways, e.g.:

-   via a cob_dashboard instantiation over the webportal
-   by a cob_teleop intantiation on your local pc
-   by new developed controllers to be tested

In a second step, access will also be granted to real hardware.

# Why should I use it?

Cob_webportal offers the possibility to remotely test new developed ROS
packages for complex service robots, e.g.

-   a new manipulator controller
-   a new script
-   a new application The tester doesn't have to care about the
    installation of the simulation environment or a running robot
    hardware, respectively.

# Getting Started

If you are interested, please send a mail to
webportal-account(at)ipa.fraunhofer.de to get an account for the
webportal.

## Prerequisites

Before getting started, install the following packages required for
cob_webportal: ```
$ sudo apt-get install python-setuptools python-paramiko screen python2.*-dev
```

## Installing Trac

If you don't have trac installed already, grab a copy of the latest
version from the
[Trac Download Page](http://trac.edgewall.org/wiki/TracDownload). We use
version 1.0 in this scenario. When your download finished install trac
via setup_tools, pip or the python installation script. More information
can be found on the
[Trac Installation Guide](http://trac.edgewall.org/wiki/TracInstall). We
use the following basic installation: ```
$ mkdir ~/trac && cd ~/trac
$ wget http://download.edgewall.org/trac/Trac-1.0.tar.gz
$ tar -xzvf Trac-1.0.tar.gz
$ cd Trac-1.0
$ sudo easy_install Trac==1.0
``` In case
you don't get any error you can check whether the installation was
successful via the python interactive shell: ```
$ python
>>> import trac
>>> trac.__version__
'1.0'
``` If
you get the output '1.0' as well, then trac is installed correctly.

## Creating a Trac environment

In order to use trac, you have to set up an environment. You can use the
helper tool trac-admin for that purpose. See
[TracEnvironment Wiki Page](http://trac.edgewall.org/wiki/TracEnvironment)
for more Information. We use a basic setup under the directory
/usr/local/trac/webportal ```
$ sudo mkdir -p /usr/local/trac/webportal
$ sudo trac-admin /usr/local/trac/webportal initenv
Follow instructions
```

## Setting up Apache

After you set up a trac environment, it's time to make it accessible
from your browser. You can use trac with many different web servers,
including the standalone version tracd. For a complete list see
[DeployingTrac](http://trac.edgewall.org/wiki/TracInstall#DeployingTrac).
However, in this example, we are going to use the widely spread
webserver from [Apache](http://httpd.apache.org/). For Apache to work
with trac we need a new module called mod_wsgi. It can be downloaded
from the [mod_wsgi project page](http://code.google.com/p/modwsgi/). On
the project page you can find the
[Installation Instructions](http://code.google.com/p/modwsgi/wiki/InstallationInstructions)
as well. We install mod_wsgi the following way: ```
$ cd ~/trac
$ wget http://modwsgi.googlecode.com/files/mod_wsgi-3.4.tar.gz
$ tar -xzvf mod_wsgi-3.4.tar.gz
$ cd mod_wsgi-3.4
$ ./configure
```
If your configure script prints the following error message at the end:
```
config.status: error: cannot find input file: Makefile.in
``` You have to install the package apache2-dev or
apache2-threaded-dev, depending on your system ```
$ sudo apt-get install apache2-dev || sudo apt-get install apache2-threaded-dev
```

The next steps include compiling, installing and configuring apache to
load the module: ```
$ make
$ sudo make install
$ echo 'LoadModule wsgi_module /usr/lib/apache2/modules/mod_wsgi.so' | sudo tee /etc/apache2/mods-available/wsgi.load
$ sudo a2enmod wsgi
$ sudo service apache2 restart
```

If you experience the following error during the restart process:
` No apache MPM package installed" ` then you have to install the
apache2-mpm-prefork package
` $ sudo apt-get install apache2-mpm-prefork `

Your apache web server is now almost ready to serve your trac
environment. However, we need to make a few more configurations first.
In a first step, we need to deploy the trac configuration to play nicely
with apache and wsgi. An elaborate guide can be found on the Trac's
[ModWSGI Wiki Page](http://trac.edgewall.org/wiki/TracModWSGI). We
deploy our environment like this: ```
$ sudo trac-admin /usr/local/trac/webportal deploy /usr/local/trac/webportal
``` The previous
command creates the folders cgi-bin and htdocs under the
/usr/local/trac/webportal directory. Next we need to map a url to our
cgi scripts. Create a new site for apache: ```
$ sudo vim /etc/apache2/sites-available/webportal
``` and
paste the following content: ```
$ mkdir ~/trac && cd ~/trac
$ wget http://download.edgewall.org/trac/Trac-1.0.tar.gz
$ tar -xzvf Trac-1.0.tar.gz
$ cd Trac-1.0
$ sudo easy_install Trac==1.0
```0 Enable the site
via the command: ```
$ mkdir ~/trac && cd ~/trac
$ wget http://download.edgewall.org/trac/Trac-1.0.tar.gz
$ tar -xzvf Trac-1.0.tar.gz
$ cd Trac-1.0
$ sudo easy_install Trac==1.0
```1 You need to give the apache
user read and write access to your trac.ini and db files. Moreover you
are going to need a .egg-cache directory to which the apache user
requires read/write access as well. You can do that with the commands:
```
$ mkdir ~/trac && cd ~/trac
$ wget http://download.edgewall.org/trac/Trac-1.0.tar.gz
$ tar -xzvf Trac-1.0.tar.gz
$ cd Trac-1.0
$ sudo easy_install Trac==1.0
```2

Now you should be able to view your trac environment in the browser.
Browse the following location <http://localhost/webportal>. You should
see trac's default landing page with the following header **Welcome to
Trac 1.0**.

In a next step we configure an access authentication. The robotcontrol
server only works with the basic access authentication at the moment.
First we need an httpasswd file. To do that run the following command
which creates an password file called **htpasswd** under the directory
*/usr/local/trac/webportal* with an initial user *admin*.
```
$ mkdir ~/trac && cd ~/trac
$ wget http://download.edgewall.org/trac/Trac-1.0.tar.gz
$ tar -xzvf Trac-1.0.tar.gz
$ cd Trac-1.0
$ sudo easy_install Trac==1.0
```3 Next open your configuration file
*/etc/apache2/sites-available/webportal* and paste the following lines
at the top of the file: ```
$ mkdir ~/trac && cd ~/trac
$ wget http://download.edgewall.org/trac/Trac-1.0.tar.gz
$ tar -xzvf Trac-1.0.tar.gz
$ cd Trac-1.0
$ sudo easy_install Trac==1.0
```4

We also need to enable apache's mod_rewrite module and as usual you
need to restart apache afterwards: ```
$ mkdir ~/trac && cd ~/trac
$ wget http://download.edgewall.org/trac/Trac-1.0.tar.gz
$ tar -xzvf Trac-1.0.tar.gz
$ cd Trac-1.0
$ sudo easy_install Trac==1.0
```5

When you browse to your location <http://localhost/webportal> again, you
should be prompted a dialog requiring you to enter your user
credentials. If your browser does not require you to login, you can take
a look at our final apache configuration
[#final_apache_configuration](#final_apache_configuration) and compare
it to yours. Make sure you restarted the server correctly and it didn't
producte any errors. In the browser's login box use *admin* as the
username and enter your previously chosen password in the password
field. Apache will verify your username/password combination and you
should be able to see the default trac screen again. You can spot a
small difference though: Above the navigation bar you should be able to
see a label called *logged in as admin*.

Now we are almost done configuring apache. We need to add a small
snippet at the top of our site configuration that is required to run the
webportal background daemon. But first we have to enable two more apache
modules called *mod_proxy* and *mod_proxy_http*. We can do that via the
following commands: ```
$ mkdir ~/trac && cd ~/trac
$ wget http://download.edgewall.org/trac/Trac-1.0.tar.gz
$ tar -xzvf Trac-1.0.tar.gz
$ cd Trac-1.0
$ sudo easy_install Trac==1.0
```6

These modules are required to bypass the ajax same-domain-policy. All
information and configuration options for mod_proxy and mod_proxy_http
can be found on Apache's
[mod_proxy](http://httpd.apache.org/docs/2.2/mod/mod_proxy.html) and
[mod_proxy_http](http://httpd.apache.org/docs/2.2/mod/mod_proxy_http.html)
page respectively. Now open /etc/apache2/sites-available/webportal and
paste the following lines at the top of the file:
```
$ mkdir ~/trac && cd ~/trac
$ wget http://download.edgewall.org/trac/Trac-1.0.tar.gz
$ tar -xzvf Trac-1.0.tar.gz
$ cd Trac-1.0
$ sudo easy_install Trac==1.0
```7

For the changes to take effect we need to restart our apache web server
```
$ mkdir ~/trac && cd ~/trac
$ wget http://download.edgewall.org/trac/Trac-1.0.tar.gz
$ tar -xzvf Trac-1.0.tar.gz
$ cd Trac-1.0
$ sudo easy_install Trac==1.0
```8 If anything doesn't work out, you can compare
your configuration to our final apache configuration. After following
our three steps above your apache webportal configuration file looks
like this: ```
$ mkdir ~/trac && cd ~/trac
$ wget http://download.edgewall.org/trac/Trac-1.0.tar.gz
$ tar -xzvf Trac-1.0.tar.gz
$ cd Trac-1.0
$ sudo easy_install Trac==1.0
```9

## Compiling plugin

First of all, get the latest source code from
[\|Github](https://github.com/ipa320/cob_web) ```
$ python
>>> import trac
>>> trac.__version__
'1.0'
```0
Create the python egg for trac, copy it into your environment's plugin
folder and restart your server: ```
$ python
>>> import trac
>>> trac.__version__
'1.0'
```1

When you browse to your trac environment under
<http://localhost/webportal> you can notice a new item called
*Robotcontrol* in the navigation menu right next to the items *View
Tickets* and *Search*. When you click on it, you will get the error
message **`'Exception: No Background Server running`**'. That's fine.

## Starting the webportal daemon

The next and final point is to start the webportal daemon that is
responsible for establishing ssh connections and responding to ajax
requests in the background. All we have to do is go to the directory
*/trac/cob_web/cob_webportal/common/src/robotcontrold*/. Running the
command ` ./robotcontrold ` yields a list of all available parameters
being:

  -- ------------------------------------------------------------------------------------------------------------------- -- --------------------------------------------------------------------------------------------------------- --
     **Parameter name**                                                                                                     **Explanation**                                                                                           
     <-2>**`'Required Parameters`**'                                                                                                                                                                                               
     \--timeout=                                                                                                            Set a timeout ( in seconds ) after which all running components for the active user are shut down.        
     \--trac=                                                                                                               Path to your trac environment. In our example: /usr/local/trac/webportal                                  
     \--log=                                                                                                                Path to your log file, e.g log.txt                                                                        
     \--webPort=                                                                                                            Port that you configured in your proxy configuration. In our example 81, see [#proxy_conf](#proxy_conf)   
     <-2>**`'Optional Parameters`**'                                                                                                                                                                                               
     \--console                                                                                                             Print log messages on stdout                                                                              
     \--logLevel=                                                                                                           Choose one of following log levels: DEBUG, INFO, WARN, ERROR                                              
     <-2>You configure the daemon to use either MySQL or sqlite. For MySQL the following parameters are interesting:                                                                                                                
     \--mysqlHost=                                                                                                          The hostname which runs the MySQL-Server                                                                  
     \--mysqlDB=                                                                                                            Databasename to use                                                                                       
     \--mysqlUser=                                                                                                          MySQL Username                                                                                            
     \--mysqlPw=                                                                                                            MySQL Passwort for given user                                                                             
     <-2>In case you prefer a sqlite database, the following parameter is for you                                                                                                                                                   
     \--sqliteDb=                                                                                                           Filename in which to store the database                                                                   
  -- ------------------------------------------------------------------------------------------------------------------- -- --------------------------------------------------------------------------------------------------------- --

Although all of the mysql and sqlite parameters are marked optional you
are required to use one of the two databases and setup the parameters
accordingly. If you want to run the webportal in a sandbox environment
you can use \--sqlite=:memory: to use a database stored only in your ram
memory. But be aware that any changes are lost after you shutdown the
server.

The server has to be started by the superuser at the moment. Furthermore
it's recommended to start the server in a separate screen, for example:
```
$ python
>>> import trac
>>> trac.__version__
'1.0'
```2 You can detach from the screen using the
keyboard shortcut *<Ctrl-a>d*. To reconnect to the screen run the
command ```
$ python
>>> import trac
>>> trac.__version__
'1.0'
```3 To learn more about screens see *man
screen*.

Once you have started the server and it's fully initialized (indicated
by the log message DEBUG - Serve forever in case you set your
debug-level to DEBUG and print messages to stdout like in the example
above) you can browse to <http://localhost/webportal> (don't forget to
login) click on Robotcontrol and you should be see the default webportal
interface. The default user *admin* is granted all available rights. If
you want to access the page using a different user, make sure to set
it's permissions first. You can do that via the *User Manager*.

As a first step you need to reserve the server instance using the server
**reservation link**. After that you need to setup a host system by
navigating to **host admin**. Make sure to **install screen** on every
client since it is required by webportal.
