## ROS API

```clearsilver
node.0 {
srv{
0.name= available_voices
0.type= tts_server/AvailableVoices
0.desc= Queries server for what voices are available.  Note: some voice fonts available in Festival do not actually work.
}

srv{
1.name= say
1.type= tts_server/Say
1.desc= Requests for a string to be converted to speech.
}
}
```
