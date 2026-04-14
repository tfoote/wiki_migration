## Overview

The [phidgets_api](phidgets_api) package contains a C++ API built on top
of the [phidgets_c_api](phidgets_c_api) package.

The package provides a base \`Phidget\` class, from which all other
Phidgets inherit. Currently, we have implemented classes for the
following devices:

-   IMU sensor
    ([ PhidgetsSpatial 3/3/3](http://www.phidgets.com/products.php?product_id=1056_0 ))

```{=html}
<!-- -->
```
-   IR sensor
    ([ PhidgetIR ](http://www.phidgets.com/products.php?product_id=1055_0 ))

Creating a class is fairly easy - feel free to request devices to be
added to the stack. If you write a class for any device using the
following example as reference and submit a patch, we\'ll add it to the
package.

## Example

In this example, we go through creating an IMU phidget using the C++
API.

We first define the Imu class, which is inherited from the base
\`Phidget\` class:

```cplusplus
class Imu: public Phidget
{
  public:

    Imu();

  protected:
 
    CPhidgetSpatialHandle imu_handle_;
    
    void zero();
    void setDataRate(int rate);

    virtual void dataHandler(CPhidgetSpatial_SpatialEventDataHandle *data, int count);

  private:

    static int SpatialDataHandler(CPhidgetSpatialHandle spatial, void *userptr, CPhidgetSpatial_SpatialEventDataHandle *data, int count);
};
```

The \`Imu\` class has a \`CPhidgetSpatialHandle\`, which is a special
handle for the Phidget Spatial device. Different devices will have
different handle types.

The constructor needs to perform 4 operations:

-   create the device-specific handle,
-   pass the handle to the base class for intialization
-   ask the base class to register common Phidget callbacks
-   register IMU-specific callbacks

```cplusplus
Imu::Imu(): Phidget(), imu_handle_(0)
{
  // create the handle
  CPhidgetSpatial_create(&imu_handle_);

  // pass handle to base class
  Phidget::init((CPhidgetHandle)imu_handle_);

  // register base class callbacks
  Phidget::registerHandlers();
  
  // register imu data callback
  CPhidgetSpatial_set_OnSpatialData_Handler(
    imu_handle_, SpatialDataHandler, this);
}
```

The \`zero()\` and \`setDataRate\` functions implement sepcific calls to
the IMU device using the C API. The data handler function receives
spatial data events.

```cplusplus
void Imu::setDataRate(int rate)
{
  CPhidgetSpatial_setDataRate(imu_handle_, rate);
}

void Imu::zero()
{
  // zero (calibrate) gyro
  CPhidgetSpatial_zeroGyro(imu_handle_);
}
```

The \`SpatialDataHandler\` is a static callback function which forwards
the data to the correct \`Imu\` class instance.

```cplusplus
int Imu::SpatialDataHandler(CPhidgetSpatialHandle handle, void *userptr, CPhidgetSpatial_SpatialEventDataHandle *data, int count)
{
  // get the class instance from the userptr, and invoke the data handler
  ((Imu*)userptr)->dataHandler(data, count);
  return 0;
}
```

Finally, the virtual \`dataHandler\` function is the one which is called
back when Spatial data arrives. In this example, the function just
prints out a message. However, you can create a class which inherits
from the \`Imu\` class and overwrites this behavior.

```cplusplus
void Imu::dataHandler(CPhidgetSpatial_SpatialEventDataHandle *data, int count)
{
  printf("Empty data handler\n");
}
```

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports and
feature requests.

Please submit your tickets through
[github](https://github.com/ccny-ros-pkg/phidgets_drivers/issues/)
(requires github account) or by emailing the maintainers.
