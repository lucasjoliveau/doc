# Connect a footswitch

When working in a manufacturing environment, it’s always better for an
operator to have both hands available at all times. Konvergo ERP’s IoT box makes this
possible when using a footswitch.

In fact, with a footswitch, the operator is able to go from one screen to
another, and perform actions using their foot. This can be configured in just
a few steps on the work center in the _Manufacturing_ app.

## Connection

To connect a footswitch to the IoT box, connect the two devices via cable.
More often than not, this is done with a USB cable.

If the footswitch is a [supported device](https://www.odoo.com/page/iot-
hardware), there is no need to take further action, since it’ll be
automatically detected when connected.

![Footswitch recognized on the IoT box.](../../../../_images/footswitch-
dropdown.png)

## Link a footswitch to a work center in the Konvergo ERP Manufacturing app

To link a footswitch to an action, it first needs to be configured on a work
center. Navigate to Manufacturing app ‣ Configuration ‣ Work Centers. From
here, go to the desired **Work Center** in which the footswitch will be used,
and add the device in the **IoT Triggers** tab, under the **Device** column,
by selecting **Add a Line**. Doing so means the footswitch can be linked to an
option in the **Action** column drop-down, and optionally, a key can be added
to trigger it. An example of an **Action** in the _Manufacturing app_ could be
the **Validate** or **Mark as Done** buttons on a manufacturing work order.

![Footswitch trigger setup on the Konvergo ERP
database.](../../../../_images/footswitch-example.png) <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>It should be noted that the first listed trigger is chosen first. So, the order matters, and
these triggers can be dragged into any order. In the picture above, using the footswitch
automatically skips the part of the process that’s currently being worked on.</p>
</div>
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>On the <b>Work Order</b> screen, a status graphic indicates whether the database is
correctly connected to the footswitch.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../../inventory_and_mrp/manufacturing/management/using_work_centers#workcenter-iot"><span class="std std-ref">Integrate IoT devices</span></a></p>
</div>

  *[IoT]: Internet of Things
  *[USB]: Universal Serial Bus

