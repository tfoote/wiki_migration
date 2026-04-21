You can interpolate between the current grasp, and two different grasps
with this slider. Let\'s have a simple example:

-   you want to open the Hand, so you double click on the **opened**
    grasp in the grasp selector. This directly sets the Hand to this
    position.
-   Then you want to grasp a simple object with the **ventral** grasp,
    so you select the **ventral** in the **To:** grasp selector on the
    right hand side.
-   you start grabbing the object with this grasp, however in the middle
    of this process, you realize that the **ventral** grasp is not the
    best grasp for this object. You set the current pose as the
    reference grasp (by clicking on **Set As Reference**. You can then
    set the **From:** grasp (on the left hand side) to **ventral** and
    the **To:** grasp to **lateral** for example.
-   You can now try both grasp at the same time by either sliding the
    slider to the right or to the left. This gives you a fine control
    over your current grasp.

You can also save a current hand pose (obtained either by interpolating
between two grasps, or by moving then hand with the sliders) by clicking
on the **Save** button.

![Grasp controller\|width=600](attachment:grasp_controller.png)
