# Display a Video Stream from ROS web_video_server Inside of a HTML5 Canvas

-   Maintainer: [Haoming Meng](https://github.com/Techming)
-   License: BSD
-   Bugtracker: <https://github.com/Techming/web-video-canvas/issues>
-   Source: <https://github.com/Techming/web-video-canvas>

## About

This repo is a fork from and developed based on
[mjpegcanvas](https://github.com/rctoris/mjpegcanvasjs) by
[Russell Toris](https://github.com/rctoris) (russell.toris@gmail.com).
Thanks for all the previous effort.

JSDoc can be found at <https://techming.github.io/web-video-canvas>

## Usage

### npm

It is recommended that you import this package via npm or yarn. Simply
run



```bash
npm install @techming/web-video-canvas // or
yarn add @techming/web-video-canvas
```



Once you installed the package, you can import the `View` or
`MultiStreamViewer` in your file:



```javascript
import { View } from '@techming/web-video-canvas';

const viewer = new Viewer({
  divID: 'mjpeg',
  host: 'localhost',
  port: '8080', // web_video_server default port
  width: 640,
  height: 480,
  topic: '/usb_cam_node/image_raw',
  type: 'png', // you can change to mjpeg, png, or ros_compressed
});
```



### Static Import

Pre-built files can be found in
[webvideocanvas.js](https://github.com/Techming/web-video-canvas/blob/master/build/webvideocanvas.js)
and
[webvideocanvas.min.js](https://github.com/Techming/web-video-canvas/blob/master/build/webvideocanvas.min.js)

## Source Code

Source code is available at
<https://github.com/Techming/web-video-canvas>. Pull requests should be
made to the `develop` branch.

## Support

Please send bug reports to the
[GitHub Issue Tracker](https://github.com/Techming/web-video-canvas/issues).
