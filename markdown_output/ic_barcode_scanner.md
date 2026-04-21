## Overview

The `ic_barcode_scanner` provides a ROS wrapper nodelet/node to the
IC-Barcode library of The Imaging Source (TIS).

See <https://www.theimagingsource.com/support/documentation/ic-barcode>
for the API documentation of IC-Barcode and
<https://www.theimagingsource.com/support/downloads-for-linux/install/tisicbarcode>
for the download.

Please note that IC-Barcode is proprietary and only runs with a TIS
camera connected to your computer (however it then accepts images from
any source).

Also note that you could run all modern cameras of TIS inside ROS using
[camera_aravis](https://github.com/fkie-forks/camera_aravis).

## Usage

### Getting started

First, download and install IC-Barcode from the link above. It is
provided as a DEB package compatible with Ubuntu LTS. Then, download and
compile this ROS wrapper from
<https://github.com/fkie/ic_barcode_scanner>.

To use the wrapper, either run the `IcBarcodeScannerNodelet` or
`IcBarcodeScannerNode`, which both provide the same
interface/functionality.



```
rosrun ic_barcode_scanner IcBarcodeScannerNode
```



The nodelet/node only subscribes to the image input on demand, i.e. if
somebody listens to a barcode topic.

### Interface



```clearsilver
sub{
0.name = ~image
0.type = sensor_msgs/Image
0.desc = A stream of images where barcodes should be detected.
}

srv {
0.name = ~find_barcodes
0.type = ic_barcode_scanner/find_barcodes
0.desc = To look for barcodes in a single image use this service.
}

pub{
0.name = ~barcodes
0.type = ic_barcode_scanner/IcBarcodeResults
0.desc = Detections of barcodes. It contains positions as well as the carried information. A vector of `IcBarcodeResult` with a `Header` corresponding to the original `Image`.

1.name = ~image_barcodes
1.type = sensor_msgs/Image
1.desc = Barcode positions drawn as boundaries on the original `Image`.
}

param{
0.name = ~barcode_formats
0.type = integer
0.desc = A bitmask which defines what barcode formats we are looking for. See `enum ICBarcode_Format` of IC-Barcode for available options. For convenience, one could also (de-)select formats using [[dynamic_reconfigure]].
0.default = `ICBarcode_Format::IC_BARCODEFORMAT_ALL`

1.name = ~max_barcodes
1.type = integer
1.desc = Maximal number of reported barcodes per image.
1.default = `10`

2.name = ~image_transport
2.type = string
2.desc = Transport hints which image (compressed) format should be used.
2.default = `raw`

3.name = all options of `enum ICBarcode_Param` from IC-Barcode
3.type = integer
3.desc = e.g. `ICBarcode_Param::IC_BARCODEPARAMS_ORIENTATION` becomes `~orientation`
3.default = `-1`
}
```


