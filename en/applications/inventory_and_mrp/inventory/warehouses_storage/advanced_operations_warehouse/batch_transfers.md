# Batch picking

_Batch picking_ enables a single picker to handle multiple orders at once,
reducing the time needed to navigate to the same location in a warehouse.

When picking in batches, orders are grouped and consolidated into a picking
list. After the picking, the batch is taken to an output location, where the
products are sorted into their respective delivery packages.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="#inventory-management-barcode-picking"><span class="std std-ref">Use Barcode app for pickings</span></a></p>
</div>

Since orders _must_ be sorted at the output location after being picked, this
picking method suits businesses with a few products that are ordered often.
Storing high-demand items in easily accessible locations can increase the
number of orders that are fulfilled efficiently.

## Configuration

To activate the batch picking option, begin by going to Inventory app ‣
Configuration ‣ Settings. Under the **Operations** section, check the **Batch
Transfers** box.

![Enable the *Batch Transfers* in Inventory > Configuration >
Settings.](../../../../../_images/batch-transfer-checkbox.png)

Since batch picking is a method to optimize the _pick_ operation in Konvergo ERP, the
**Storage Locations** and **Multi-Step Routes** options under the
**Warehouse** heading must also be checked on this settings page. When
finished, click **Save**.

![Enable *Storage Locations* and *Multi-Step Routes* Inventory > Configuration
> Settings.](../../../../../_images/locations-routes-checkbox.png)

Lastly, enable the warehouse picking feature, by navigating to the warehouse
settings page, which is accessible from Inventory app ‣ Configuration ‣
Warehouses.

From here, select the desired warehouse from the list. Then, from the radio
options available for **Outgoing Shipments** , select either the **Send goods
in output and then deliver (2 steps)** or **Pack goods, send goods in output
and then deliver (3 steps)**.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../../shipping_receiving/daily_operations/receipts_delivery_two_steps#inventory-receipts-delivery-two-steps"><span class="std std-ref">Delivery in two steps</span></a></p></li>
<li><p><a href="../../shipping_receiving/daily_operations/delivery_three_steps#inventory-delivery-three-steps"><span class="std std-ref">Delivery in three steps</span></a></p></li>
</ul>
</div> ![Set up 2-step or 3-step outgoing
shipments.](../../../../../_images/set-2-or-3-step-shipment.png)

## Create batch transfers

Manually create batch transfers directly from the Inventory app ‣ Operations ‣
Batch Transfers page. Click the **New** button to begin creating a batch
transfer.

On the batch transfer form, fill the following fields out accordingly:

  * **Responsible** : employee assigned to the picking. Leave this field blank if _any_ worker can fulfill this picking.

  * **Operation Type** : from the drop-down menu, select the operation type under which the picking is categorized.

  * **Scheduled Date** : specifies the date by which the **Responsible** person should complete the transfer to the output location.

Next, in the **Transfers** list, click **Add a line** to open the **Add:
Transfers** window.

If the **Operation Type** field was filled, the list will filter transfer
records matching the selected **Operation Type**.

Click the **New** button to create a new transfer.

Once the transfer records are selected, click **Confirm** to confirm the batch
picking.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>A new batch transfer assigned to the <b>Responsible</b>, <code>Joel Willis</code>, for the <code>Pick</code>
<b>Operation Type</b>. The <b>Scheduled Date</b> is set to <code>August 11</code>.</p>
<img alt="View of *Batch Transfers* form." class="align-center" src="../../../../../_images/batch-transfer-form.png"/>
<p>Clicking the <b>Add a line</b> button opens the <b>Add:Transfers</b> window,
displaying only pickings. This is because the <b>Operation Type</b> was set to <code>Pick</code> on the
batch transfer form.</p>
<p>Click the checkbox to the left of the transfers, <code>WH/PICK/00001</code> and <code>WH/PICK/00002</code>, to include
them in the new transfer. Then, click the <b>Select</b> button to close the
<b>Add:Transfers</b> window.</p>
<img alt="Select multiple transfers from the *Add:Transfers* window." class="align-center" src="../../../../../_images/add-transfers-window.png"/>
</div>

### Add batch from transfers list

Another method of creating batch transfers is available using the **Add to
batch** option in a list. Navigate to the Inventory app ‣ Operations drop-down
menu, and select any of the **Transfers** to open a filtered list of
transfers.

![Show all transfer types in a drop-down menu: Receipts, Deliveries, Internal
Transfers, Manufacturings, Batch Transfers,
Dropships.](../../../../../_images/transfers-drop-down.png)

On the transfers list, select the checkbox to the left of the selected
transfers to add in a batch. Next, navigate to the **Actions ⚙️ (gear)**
button, and click **Add to batch** from the resulting drop-down menu.

![Use *Add to batch* button, from the *Action* button's
list.](../../../../../_images/add-to-batch.png)

Doing so opens an **Add to batch** pop-up window, wherein the employee
**Responsible** for the picking can be assigned.

Choose from the two radio options to add to **an existing batch transfer** or
create **a new batch transfer**.

To begin with a draft, select the **Draft** checkbox.

Conclude the process by clicking **Confirm**.

![Show *Add to batch* window to create a batch
transfer.](../../../../../_images/add-to-batch-window.png)

## Process batch transfer

Handle batch transfers in the Inventory app ‣ Operations ‣ Batch Transfers
page.

From here, select the intended transfer from the list. Then, on the batch
transfer form, input the **Done** quantities for each product, under the
**Detailed Operations** tab. Finally, select **Validate** to complete the
picking.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Be certain the batch transfer is complete when the <b>Validate</b> button is highlighted in
purple. If the <b>Check Availability</b> button is highlighted instead, that means there are
items in the batch that are currently <em>not</em> available in-stock.</p>
</div> <div class="alert alert-success" id="inventory-management-batch-transfers-example">
<p class="alert-title">
Example</p><p>In a batch transfer involving products from pickings, <code>WH/PICK/00001</code> and <code>WH/PICK/00002</code>, the
<b>Detailed Operations</b> tab shows that the product, <code>Cabinet with Doors</code>, has been picked
because the <b>Done</b> column matches the value in the <b>Reserved</b> column.
However, <code>0.00</code> quantities have been picked for the other product, <code>Cable Management Box</code>.</p>
<img alt="Show batch transfer of products from two pickings in the *Detailed Operations* tab." class="align-center" src="../../../../../_images/process-batch-transfer.png"/>
</div>

Only in-stock products are visible in the **Detailed Operations** tab.

To view the complete product list, switch to the **Operations** tab. On this
list, the **Demand** column indicates the required quantity for the order. The
**Reserved** column shows the available stock to fulfill the order. Lastly,
the **Done** column specifies the products that have been picked, and are
ready for the next step.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>The product, <code>Desk Pad</code>, from the same batch as the <a href="#inventory-management-batch-transfers-example"><span class="std std-ref">example above</span></a>, is only visible in the <b>Operations</b>
tab because there are no <b>Reserved</b> quantities in-stock to fulfill the batch picking.</p>
<p>Click the <b>Check Availability</b> button to search the stock again for available products.</p>
<img alt="Show unavailable reserved quantities in the *Operations* tab." class="align-center" src="../../../../../_images/operations-tab.png"/>
</div>

### Create backorder

On the batch transfer form, if the **Done** quantity of the product is _less_
than the **Reserved** quantity, a pop-up window appears.

This pop-up window provides the option: **Create Backorder?**.

Clicking the **Create Backorder** button automatically creates a new batch
transfer, containing the remaining products.

Click **No Backorder** to finish the picking _without_ creating another batch
picking.

Click **Discard** to cancel the validation, and return to the batch transfer
form.

![Show the *Create Backorder* pop-up.](../../../../../_images/create-
backorder.png)

## Process batch transfer: Barcode app

Created batch transfers are also listed in the Barcode app, accessible by
selecting the **Batch Transfers** button.

By default, confirmed batch pickings appear on the **Batch Transfers** page.
On that page, click on the desired batch transfer to open the detailed list of
products for the picking.

![Show list of to-do batch transfers in *Barcode*
app.](../../../../../_images/barcode-batch-transfers.png)

For the chosen batch transfer, follow the instructions at the top of the page
in the black background. Begin by scanning the product’s barcode to record a
single product for picking. To record multiple quantities, click the **✏️
(pencil)** icon, and enter the required quantities for the picking.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Products from the same order are labeled with the same color on the left. Completed pickings are
highlighted in green.</p>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>In a batch transfer for 2 <code>Cabinet with Doors</code>, 3 <code>Acoustic Bloc Screens</code>, and 4 <code>Four Person
Desks</code>, the <code>3/3</code> and <code>4/4</code> <b>Units</b> indicate that the last two product pickings are
complete.</p>
<p><code>1/2</code> units of the <code>Cabinet with Doors</code> has already been picked, and after scanning the product
barcode for the second cabinet, Konvergo ERP prompts the user to <code>Scan a serial number</code> to record the
unique serial number for <a href="../../product_management/product_tracking/serial_numbers#inventory-serial-numbers-configure"><span class="std std-ref">product tracking</span></a>.</p>
<img alt="Display products to be picked in barcode view." class="align-center" src="../../../../../_images/barcode-products.png"/>
</div>

Once all the products have been picked, click on **Validate** to mark the
batch transfer as **Done**.

