# Connect a printer

Printer installation can be done in a few easy steps. The printer can be used
to print receipts, labels, orders, or even reports from the different Konvergo ERP
apps. In addition, printer actions can be assigned as an _action on a trigger_
during the manufacturing process, or added onto a quality control point or a
quality check.

## Connection

The IoT box supports printers connected through USB, network connection, or
Bluetooth. [Supported printers](https://www.odoo.com/page/iot-hardware) are
detected automatically, and appear in the **Devices** list of the _IoT app_.

![The printer as it would appear in the IoT app devices
list.](../../../../_images/printer-detected.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The printer can take up to two minutes to appear in the <em>IoT app</em> devices list.</p>
</div>

## Link printer

### Link printer to work orders

_Work Orders_ can be linked to printers, via a quality control point, to print
labels for manufactured products.

In the _Quality app_ , a device can be set up on a quality control point. To
do that, go to the Quality app ‣ Quality Control ‣ Control Points, and open
the desired control point to which the printer will be linked.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>A <em>Manufacturing Operation</em> and <em>Work Order Operation</em> need to be attached to a quality control
point before the <b>Type</b> field allows for the <b>Print Label</b> option to be
selected.</p>
</div>

From here, edit the control point, by selecting the **Type** field, and
selecting **Print Label** from the drop-down menu of options. Doing so reveals
a field called **Device** , where the attached _device_ can be selected.
**Save** the changes, if required.

![This is the quality control point setup.](../../../../_images/printer-
controlpoint.png)

The printer can now be used with the selected quality control point. When the
quality control point is reached during the manufacturing process, the
database presents the option to print labels for a specific product.

![../../../../_images/printer-prompt.png](../../../../_images/printer-
prompt.png) <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Quality control points can also be accessed by navigating to IoT App ‣
Devices, then select the device. There is a <b>Quality Control Points</b> tab, where they
can be added with the device.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>On a quality check detail form, the <b>Type</b> of check can also be specified to
<b>Print Label</b>. To create new quality checks, navigate to Quality app
‣ Quality Control ‣ Quality Checks ‣ New.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../../../inventory_and_mrp/quality/quality_management/quality_control_points">Quality control points</a></p></li>
<li><p><a href="../../../inventory_and_mrp/quality/quality_management/quality_alerts">Create quality alerts</a></p></li>
</ul>
</div>

### Link a printer to a work center in the Manufacturing app

To link a printer to an action, it first needs to be configured on a work
center. To do that, navigate to Manufacturing app ‣ Configuration ‣ Work
Centers. From here, select the desired work center in which the printer will
be used. Next, add the device in the **IoT Triggers** tab, under the
**Device** column, by selecting **Add a Line**.

Then, the printer can be linked to either of the following options in the
**Actions** drop-down menu: **Print Labels** , **Print Operation** , or
**Print Delivery Slip**. A key can also be added to trigger the action.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>The first listed trigger on the form will be chosen first. So, the order matters, and these
triggers can be dragged into any order.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>On the <b>Work Order</b> screen, a status graphic indicates whether the database is
correctly connected to the printer.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../../inventory_and_mrp/manufacturing/management/using_work_centers#workcenter-iot"><span class="std std-ref">Integrate IoT devices</span></a></p>
</div>

### Link printer to reports

It’s also possible to link a type of report to a certain printer. In the _IoT
app_ , go to the **Devices** menu, and select the desired printer that needs
to be configured.

From here, click **Edit** , go to the **Printer Reports** tab, and select
**Add a line**. In the window that appears, check all the types of **Reports**
that should be linked to this printer.

![The printer devices listed in the IoT Devices
menu.](../../../../_images/printers-listed.png)

Now, each time **Print** is selected in the control panel, instead of
downloading a PDF, a pop-up appears which displays all the printer(s) linked
to the report. Then Konvergo ERP sends the report to the selected printer(s), and
automatically prints it.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../../sales/point_of_sale/restaurant/kitchen_printing">POS Order Printing</a></p>
</div> <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Reports can also be configured in the <b>Technical Menu</b> while in <a href="../../developer_mode#developer-mode"><span class="std std-ref">debug mode</span></a>. To do that, navigate to Settings App ‣ Technical Menu ‣
Actions ‣ Reports. From here, the individual report can be found in this list, where the
<b>IoT Device</b> can be set on the report.</p>
</div>

  *[IoT]: Internet of Things
  *[USB]: Universal Serial Bus

