## Introduction

The monitoring node retrieves data on the topics `/statistics`,
`/statistics_node` and `/statistics_host`. It then rates them according
to specifications stored in the parameter namespace
`/arni/specifications`. The resulting data are published on the topic
`/statistics_rated`.

## Used Parameters

For parameters shared across the arni packages see
[this list](arni#Used_Parameters).

  -- ------------------------------------------------------------------------------------ -- -------------------------------------------------------------------------------- -- -------------------------------------------------------------------------------------------------------------------------------------------------- --
     <style="border:1px solid #ccc;border-collapse:collapse;">**Parameter**              <style="border:1px solid #ccc;border-collapse:collapse;">**Default value**      <style="border:1px solid #ccc;border-collapse:collapse;">**Description**                                                                       
                                                                                                                                                                                 <(>**arni_processing provides a storage with rated data for the GUI widgets.**                                                                   
     <style="border:1px solid #ccc;border-collapse:collapse;">storage/timeout            <style="border:1px solid #ccc;border-collapse:collapse;">300(s)                 <style="border:1px solid #ccc;border-collapse:collapse;">The time in seconds since when data is considered old and will be removed.            
     <style="border:1px solid #ccc;border-collapse:collapse;">storage/auto_cleanup       <style="border:1px solid #ccc;border-collapse:collapse;">True                   <style="border:1px solid #ccc;border-collapse:collapse;">Enable or disable the automatic cleanup.                                              
     <style="border:1px solid #ccc;border-collapse:collapse;">storage/cleanup_timer      <style="border:1px solid #ccc;border-collapse:collapse;">30(s)                  <style="border:1px solid #ccc;border-collapse:collapse;">The time in s giving the interval of automatic cleanup.                               
                                                                                                                                                                                 <(>**Statistics about topics are generated from the `/statistics` topic and aggregated over time.**                                              
     <style="border:1px solid #ccc;border-collapse:collapse;">aggregation_window         <style="border:1px solid #ccc;border-collapse:collapse;">3(s)                   <style="border:1px solid #ccc;border-collapse:collapse;">The duration of time over which the processing node aggregates messages on a topic.   
                                                                                                                                                                                 <(>**Connections are tested if they still send data**                                                                                            
     <style="border:1px solid #ccc;border-collapse:collapse;">alive_interval             <style="border:1px solid #ccc;border-collapse:collapse;">5(s)                   <style="border:1px solid #ccc;border-collapse:collapse;">Interval to check all registered connections.                                         
     <style="border:1px solid #ccc;border-collapse:collapse;">alive_timer                <style="border:1px solid #ccc;border-collapse:collapse;">10(s)                  <style="border:1px solid #ccc;border-collapse:collapse;">Default timer afther when a connections is regarded as "dead".                      
                                                                                                                                                                                 <(>**All references for rating the incoming statistics are stored as specifications in a list on the parameterserver.**                          
     <style="border:1px solid #ccc;border-collapse:collapse;">/arni/specifications       <style="border:1px solid #ccc;border-collapse:collapse;">\[\]                   <style="border:1px solid #ccc;border-collapse:collapse;">See the Specification format below.                                                   
  -- ------------------------------------------------------------------------------------ -- -------------------------------------------------------------------------------- -- -------------------------------------------------------------------------------------------------------------------------------------------------- --

Additionaly some commands can be send as service calls:

  -- ----------------------------------------------------------------------------------------------------- -- --------------------------------------------------------------------------------- -- -------------------------------------------------------------------------------------------------------------------------------------------------- --
     <style="border:1px solid #ccc;border-collapse:collapse;">**Service**                                 <style="border:1px solid #ccc;border-collapse:collapse;">**Content**             <style="border:1px solid #ccc;border-collapse:collapse;">**Effect**                                                                            
     <style="border:1px solid #ccc;border-collapse:collapse;">/monitoring_node/reload_specifications      <style="border:1px solid #ccc;border-collapse:collapse;">std_srvs.srv.Empty      <style="border:1px solid #ccc;border-collapse:collapse;">Reloads all specifications from the namespace /arni/specifications (see Parameters)   
  -- ----------------------------------------------------------------------------------------------------- -- --------------------------------------------------------------------------------- -- -------------------------------------------------------------------------------------------------------------------------------------------------- --

## Specifications

The processing node rates the incoming statistics based on given
specifications. They are read from the namespace `/arni/specifications`.
There you might give your desired specifications for a given seuid
according to this format:

```
- n!example_node: # a seuid
    measurement1: [minvalue, maxvalue]
    # or
    measurement2: [value, deviation, "relative"]
```

You can pack these specifications as list items in one single list,
which will then overwrite the whole list when you load several lists or
add one more namespace block with the list like
`/arni/specifications/logical_unit1 = [], /arni/specifications/logical_unit2 = []`.
The latter method allows you to selectively unset specification blocks.
Learn more about the [seuid](arni#SEUID). Note that the measurement
fields can be basically every field in the respective
[messagetypes](arni_msgs). See theses for comments on units.

Additionally the field `alive_timer` determines when the specified item
is regarded as "dead" (see above). **Note** that this field expects a
single number unlike the other fields!

For reference all fields are listed below.

### Limit format

Usually the limits for a measurement are given as list with minimum and
maximum value. If a third parameter is set as "relative", the limits
will be calculated as `minvalue = value * (1 - deviation)` etc.

**Note**: If a measured value returns an array (for example
bandwidth_max for multiple network adapters) you can give an array of
such limits. If you receive more values than you defined limits, spare
values will be rated as *unknown*. If you don't give an array of
limits, the given limit will be used for each value.

### Specification Fields

#### Hosts

```
cpu_temp_mean (float32)
cpu_temp_stddev (float32)
cpu_temp_max (float32)

cpu_usage_mean (float32)
cpu_usage_stddev (float32)
cpu_usage_max (float32)

cpu_usage_core_mean (float32[])
cpu_usage_core_stddev (float32[])
cpu_usage_core_max (float32[])

cpu_temp_core_mean (float32[])
cpu_temp_core_stddev (float32[])
cpu_temp_core_max (float32[])

gpu_temp_mean (float32[])
gpu_temp_stddev (float32[])
gpu_temp_max (float32[])

gpu_usage_mean (float32[])
gpu_usage_stddev (float32[])
gpu_usage_max (float32[])

ram_usage_mean (float32)
ram_usage_stddev (float32)
ram_usage_max (float32)

message_frequency_mean (int32[])
message_frequency_stddev (int32[])
message_frequency_max (int32[])

bandwidth_mean (float32[])
bandwidth_stddev (float32[])
bandwidth_max (float32[])
```

#### Nodes

```
node_cpu_usage_mean (float32)
node_cpu_usage_stddev (float32)
node_cpu_usage_max (float32)

node_cpu_usage_core_mean (float32[])
node_cpu_usage_core_stddev (float32[])
node_cpu_usage_core_max (float32[])

node_gpu_usage_mean (float32[])
node_gpu_usage_stddev (float32[])
node_gpu_usage_max (float32[])

node_ramusage_mean (float32)
node_ramusage_stddev (float32)
node_ramusage_max (float32)
 
node_message_frequency_mean (float32)
node_message_frequency_stddev (float32)
node_message_frequency_max (float32)

node_bandwidth_mean (float32)
node_bandwidth_stddev (float32)
node_bandwidth_max (float32)

node_write_mean (float32)
node_write_stddev (float32)
node_write_max (float32)

node_read_mean (float32)
node_read_stddev (float32)
node_read_max  (float32)
```

#### Connections

Connections use the built-in
[Statistics messagetype](http://docs.ros.org/api/rosgraph_msgs/html/msg/TopicStatistics.html).
```
delivered_msgs (int32)
dropped_msgs (int32)
traffic (int32)
bandwidth (int32) # normalized traffic
period_mean (duration)
period_stddev (duration)
period_max (duration)
stamp_age_mean (duration)
stamp_age_stddev (duration)
stamp_age_max (duration)
```

#### Topics

Topics use a subset of these fields: ```
delivered_msgs (int32)
dropped_msgs (int32)
packages (int32) # number of packages included in the aggregation
packages_per_second (float32) # packages normalized over their timespan
traffic (int32)
bandwidth (float32) # normalized traffic
frequency (float32)
stamp_age_mean (duration)
stamp_age_stddev (duration)
stamp_age_max (duration)
```
