The cobot_gui package allow the creation of a customizable gui to
control and check the status of your robot. This tool includes some
precreated plugins for common tools like RVIZ, Rqt or node manager and
also tools and libraries to add new qt applications. The modularity of
the gui makes easy the customization of the configuration.

## Software Requirements

To launch the default gui is required the installation of the airbus
plugin and dashboard packages. The cobot_gui includes:

-   [airbus_plugin_log_manager](airbus_plugin_log_manager)
-   [airbus_plugin_node_manager](airbus_plugin_node_manager)
-   [airbus_plugin_rqt](airbus_plugin_rqt)
-   [airbus_plugin_rviz](airbus_plugin_rviz)

Additionally the package
[airbus_pyqt_extend](wiki.ros.org/airbus_pyqt_extend) includes a library
to customise easily qt applications.

## Execution

A launch file is already generated to open a cobot_gui window with the
default configuration

```
roslaunch airbus_cobot_gui default.launch
```

![\|width=100%](attachment:cobot_gui.png)

The user can also call this launch file to run a different
configuration, using the input parameters \'\'config_path\'\' and
\'\'file_name\'\'

```
roslaunch airbus_cobot_gui default.launch config_path:='${PKG_NAME}/folder' file_name:='file.conf'
```

## Configuration

The configuration of the cobot_gui can be defined via a
[XML file](https://github.com/ipa320/airbus_coop/blob/master/airbus_cobot_gui/config/default.conf):

```
<?xml version="1.0"?>

<app mode="debug">
    <translate type="en"/>
    <window display-mode="-d">
        <default-size>
            <width>1280</width>
            <height>720</height>
        </default-size>
        <header>
            <dashboards src="${airbus_cobot_gui}/config/default_dashboards_register.xml">
            </dashboards>
        </header>
        <launcher default-view="Rviz" default-mode="manu">
            <plugins src="${airbus_cobot_gui}/config/default_plugins_register.xml">
                <plugin name="Rviz"/>
                <plugin name="Rqt"/>
                <group name="Monitoring" icon="${airbus_cobot_gui}/resources/images/icon_monitoring.png">
                    <plugin name="NodeManager"/>
                    <plugin name="LogManager"/>
                </group>
           </plugins>
        </launcher>
    </window>
</app>
``` For further information about the parameters
see:
<https://github.com/ipa320/airbus_coop/blob/master/airbus_cobot_gui/README.md#2--configuration>

## Create your own cobot_gui

The configuration of the cobot_gui is composed by two main components:

-   The dashboards: the external frame with direct access button to
    change the language, the mode to manual or overview the current
    status of diagnostic
-   The plugins: with an icon in the left side of the dashboard, can
    integrate a qt application in the main window of the gui.

The user is allow to create and add new dashboards and plugins, by
adding new entry lines to the dashboards_register.xml file and the
plugins_register.xml. See the package
[airbus_templates](https://github.com/ipa320/airbus_coop_tutorials/tree/master/airbus_templates)
as example.

The configuration file for this package include new registers files for
the dashboards and the plugins:

```
<?xml version="1.0"?>

<app mode="debug">
    <translate type="en"/>
    <window display-mode="-d">
        <default-size>
            <width>1280</width>
            <height>720</height>
        </default-size>
        <header>
            <dashboards src="${airbus_templates}/config/default_dashboards_register.xml">
                                <dashboard name="Template"/>
            </dashboards>
        </header>
        <launcher default-view="Template" default-mode="manu">
            <plugins src="${airbus_templates}/config/default_plugins_register.xml">
                                <plugin name="Template"/>
                <plugin name="Rviz"/>
                <plugin name="Rqt"/>
                <group name="Monitoring" icon="${airbus_cobot_gui}/resources/images/icon_monitoring.png">
                    <plugin name="NodeManager"/>
                    <plugin name="LogManager"/>
                </group>
           </plugins>
        </launcher>
    </window>
</app>
``` Where the
\'\'default_dashboards_register.xm\'\'l includes an entry for a new
dashboard:

```
<?xml version='1.0' encoding='utf8'?>
<dashboards-register>
        <dashboard label="Template" package="airbus_template_dashboard" />
</dashboards-register>
``` The package
[airbus_template_dashboard](https://github.com/ipa320/airbus_coop_tutorials/blob/master/airbus_template_dashboard/src/airbus_template_dashboard/dashboard.py)
define the python code of the qt level that will be popup inside your
cobot_gui.

For the plugins the procedure is almost the same, there is also a XML
file where the user can include new entries, for example:

```
<?xml version='1.0' encoding='utf8'?>
<plugins-register>
  <plugin label="Rviz"           package="airbus_plugin_rviz" />
  <plugin label="Rqt"            package="airbus_plugin_rqt" />
  <plugin label="NodeManager"    package="airbus_plugin_node_manager" />
  <plugin label="LogManager"     package="airbus_plugin_log_manager" />
  <plugin label="Template"       package="airbus_template_plugin" />
</plugins-register>
``` Being the package
[airbus_template_plugin](https://github.com/ipa320/airbus_coop_tutorials/blob/master/airbus_template_plugin/src/airbus_template_plugin/plugin.py)
where the plugin functions is defined.
