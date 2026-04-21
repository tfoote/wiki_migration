## Documentation

!WifiComm allows multi-robot peer-2-peer style communication. The
discovery node works together with olsrd to publish information related
to available neighbors. A library is also available to allow for easy
opening and closing of foreign_relays, the method by which local topics
are published on a foreign roscore, thus providing the communication
channel.

## OLSR

You can download olsrd-0.6.0 from <http://www.olsr.org/>.

## ROS API



```clearsilver
node.0 {
name=wifi_discovery_node
desc=`wifi_discovery_node` uses olsrd to watch for neighbor robots. 
pub{
0.name= wifi_neighbours_list
0.type= wifi_comm/WiFiNeighboursList
0.desc= List of neighbors on the network provided by olsrd.
}
param {
0.name= /wifi_discovery_node/frequency
0.default= 1
0.type= int
0.desc= The update frequency of the neighbors list.
}
}
```



## Tutorials
