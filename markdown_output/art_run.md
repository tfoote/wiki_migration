## Utility Commands

This package includes some utility commands that are useful for running
on the vehicle or working with generated data. See the \`art_run/bin\`
subdirectory for a complete list, it is rapidly evolving.

If you want to run these commands directly from the shell, add this to
the end of your \`/.bashrc\`: ```
ART_RUN=$(rospack find art_run)
if [ "$ART_RUN" != "" ] && [ -d $ART_RUN/bin ]
then export PATH=$ART_RUN/bin:$PATH
fi
```

## Launch Files

This package includes several launch files for running and monitoring
the vehicle. See the \`art_run/launch\` subdirectory for a complete
list.

Examples:

Run pilot Stage simulation using world and RNDF for UT Pickle Research
Campus (\`prc_large\`). ```
$ roslaunch art_run pilot_stage.launch
```

Control Stage simulation from the keyboard, using world and RNDF for
DARPA site visit at Southwest Research Institute (\`swri_site_visit\`).
```
$ WORLD=swri_site_visit roslaunch art_run key_stage.launch
```

Run pilot on the car with real servo devices. ```
$ roslaunch art_run pilot_drive.launch
```

Control pilot on the car using the joystick. ```
$ roslaunch art_run joy_drive.launch
```
