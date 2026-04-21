The digital camera node interfaces with standard USB cameras (e.g. the
Logitech Quickcam) using OpenCV and publishes image data using the
[image_transport](image_transport) model, which can automatically
generate compressed message types. That is, the theora streaming video
compression is only enabled when the image is actually requested
compressed, e.g. by calling

. 

```
/image_view image:=/image_raw theora
```



Notice that you have to compile theora separately, i.e. using

. 

```
rosmake theora_image_transport
```

 . 

```
rosmake compressed_image_transport
```


