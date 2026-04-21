## ROS API



```clearsilver
node.0 {
name=tf_broadcaster_laser
desc= tf broadcaster node for the LSE Roomba robot equipped with an Hokuyo laser.
}
node.1 {
name=tf_broadcaster_sonar
desc= tf broadcaster node for the LSE Roomba robot equipped with an array of 5 Devantech SRF08 sonars.
}
node.2 {
name=tf_broadcaster_nose
desc= tf broadcaster node for the LSE Roomba robot equipped with an Hokuyo laser and a LSE MOX nose.
}
node.3 {
name=tf_broadcaster_multi
desc= Experimental node for synchronizing multiple robot tf from different roscores. 
}
```



## Related Turials

-   [Running the navigation stack on the Roomba](lse_roomba_toolbox/Tutorials/navigation on the Roomba)
