## Documentation

Package providing frames visualization tool.

### How to use

`view_frames` is a graphical debugging tool that creates a PDF graph
of your current transform tree.



```
$ rosrun tf2_tools view_frames.py
```

 You probably want to view the graph when you
are done, so a typical usage on Ubuntu systems is:



```
$ rosrun tf2_tools view_frames.py
$ evince frames.pdf
```

 Therefore an helpful shortcut to add in your
`.bashrc` is:



```
alias tf2='cd /var/tmp && rosrun tf2_tools view_frames.py && evince frames.pdf &'
```


