## Meta-Documentation

Let\'s be honest. Documentation is hard. This package is an attempt to
make it easier.

Using the source code of your packages, this package applies a set of
regular expressions and parses out the basic node information,
particularly the type of information used by the
[CS/NodeAPI](StyleGuide#ROS_API) template,
([definition here](CS/NodeAPI)).

To generate your own documentation, run the following command.
```
rosrun roswiki_node roswiki [source code files]
```

You can list any number of source code files for a given node and the
output will be code that you can paste into the ROS wiki.

## Limitations

Not all of the information used by the wiki macros is parsed out. For
example, if a parameter is set, the regular expression will recognize
the name of the parameter being set, but not the value.

It should also be noted that this is a simple pattern matcher. No
complex scope resolution is done, nor even preprocessing.

## Patterns

Here are the patterns that roswiki_node currently looks for.

  -- ------------------------ -- -------------- -- -------------- --
                                 C++               Python         
     Name                        \<#00FF00\>o      \<#00FF00\>o   
     Subscriptions               \<#00FF00\>o      \<#00FF00\>o   
     Publications                \<#00FF00\>o      \<#00FF00\>o   
     Services Used               \<#00FF00\>o      \<#00FF00\>o   
     Services Called             \<#00FF00\>o      \<#00FF00\>o   
     Parameters Used             \<#FFFF00\>1      \<#00FF00\>o   
     Parameters Set              \<#00FF00\>o      \<#00FF00\>o   
     Transforms Used             \<#00ff00\>o      \<#00ff00\>o   
     Transforms Set              \<#FF0000\>x      \<#FF0000\>x   
     actionlib Goals             \<#FF0000\>x      \<#FF0000\>x   
     actionlib Feedback          \<#FF0000\>x      \<#FF0000\>x   
     actionlib Result            \<#FF0000\>x      \<#FF0000\>x   
     actionlib Actions Used      \<#FF0000\>x      \<#FF0000\>x   
  -- ------------------------ -- -------------- -- -------------- --

1\) Only parses the name of the service, not the type

## Additions

Are you a regular expression whiz? Tickets and patches are welcome for
adding new patterns.
[Submit here](http://sourceforge.net/tracker/?group_id=261576&atid=1333666)
or contact DavidLu
