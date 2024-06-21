# Cluster picking

Cluster picking is an advanced order fulfillment approach derived from [batch
picking](batch_transfers#inventory-misc-batch-picking).

In this strategy, pickers load a cart with multiple packages, each designated
for a specific _sales order_ (SO). Then, the picker travels to each storage
location, and places the products directly in the package of the associated
order.

This method is most efficient for medium-sized companies, with high order
volumes, and relatively few unique products, since the method eliminates the
need for sorting products into packages for customers after picking.

However, cluster picking does have some disadvantages. For instance, urgent
orders cannot be prioritized, and optimized batches must be manually created
beforehand. As a result, the picking process can lead to bottlenecks.

<div class="alert alert-success" id="inventory-misc-cluster-picking-example">
<p class="alert-title">
Example</p><ol class="arabic simple">
<li><p><abbr title="Sales Order">SO</abbr> 1 calls for one apple and orange</p></li>
<li><p><abbr title="Sales Order">SO</abbr> 2 calls for one apple and banana</p></li>
<li><p><abbr title="Sales Order">SO</abbr> 3 calls for one apple, orange, and banana</p></li>
</ol>
<p>Apples are stored in Shelf A, oranges in Shelf B, and bananas in Shelf C.</p>
<p>To pick products for three orders at once, the cart is loaded with three empty packages.</p>
<p>Starting at Shelf A, the picker places apples into each package. Next, the picker navigates to
Shelf B, and places oranges in the packages designated for <abbr title="Sales Order">SO</abbr> 1 and <abbr title="Sales Order">SO</abbr> 3. Finally, the picker
pushes the cart to Shelf C, and loads packages for <abbr title="Sales Order">SO</abbr> 2 and <abbr title="Sales Order">SO</abbr> 3 with a banana, each.</p>
<p>With the packages for all three <abbr title="Sales Orders">SOs</abbr> packed, the picker pushes the cart to the output location,
where the packages are sealed and prepared for shipment.</p>
<img alt="Show example of fulfilling sales orders 2 and 3 at once." class="align-center" src="../../../../../_images/cluster-example.png"/>
</div>

## Configuration

To enable cluster picking, begin by navigating to Inventory app ‣
Configuration ‣ Settings. Under the **Operations** heading, activate the
**Packages** and **Batch Transfers** options.

![Activate *Packages* and *Batch Transfers* features in the
settings.](../../../../../_images/configs.png)

Since batch picking is used to optimize the _pick_ operation in Konvergo ERP, the
**Storage Locations** and **Multi-Step Routes** options, under the
**Warehouse** heading, must also be checked on this settings page.

_Storage locations_ allow products to be stored in specific locations they can
be picked from, while _multi-step routes_ enable the picking operation itself.

When finished, click **Save**.

![Enable *Storage Locations* and *Multi-Step Routes* Inventory > Configuration
> Settings.](../../../../../_images/locations-routes-checkbox1.png)

### Packages setup

After the **Packages** feature is enabled, navigate to Inventory app ‣
Products ‣ Packages, and click the **New** button to create a new package.

On the new package form, the **Package Reference** is pre-filled with the next
available `PACK` number in the system. **Pack Date** is automatically set to
the creation date of the form.

Set the **Package Use** field to **Reusable Box**.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../product_management/product_tracking/package">Packages</a></p>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>A package intended for cluster picking is named <code>CLUSTER-PACK-3</code> for easy identification. For
this workflow, the products are directly packed using their intended shipping boxes, so
<b>Package Use</b> is set to <b>Disposable Box</b>.</p>
<img alt="Create new package form." class="align-center" src="../../../../../_images/cluster-package.png"/>
</div>

## Create cluster batch

To see how cluster picking works in Konvergo ERP, navigate to the Sales app, and
create SOs that will be fulfilled together in the same batch. After confirming
an SO, the **Delivery** smart button becomes visible. Displayed inside the
icon is a number representing the amount of steps in the outgoing shipment
process.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Begin by creating three <abbr title="Sales Orders">SOs</abbr> for the apples, oranges, and bananas, as shown in the <a href="#inventory-misc-cluster-picking-example"><span class="std std-ref">example
above</span></a>.</p>
<p>After confirming the <abbr title="Sales Order">SO</abbr>, the <b>Delivery</b> smart button displays the number <code>2</code>,
indicating there are two operations to complete: <code>Pick</code> and <code>Delivery</code>.</p>
<img alt="Example sales order for an apple, orange, and banana." class="align-center" src="../../../../../_images/create-sales-order.png"/>
</div>

With the SOs created, orders now must be grouped into batches. To do so,
navigate to the _Inventory_ dashboard and select the operation type card,
**Delivery Orders** or **Pick** (whichever is the first operation in the
delivery flow).

Doing so displays a filtered list of outgoing operations with the **Ready**
status, indicating that all the products in the SO are in stock.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Cluster pick batches can be created for outgoing shipments in one, two, or three steps.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../../shipping_receiving/daily_operations/receipts_delivery_one_step#inventory-receipts-delivery-one-step"><span class="std std-ref">Delivery in one step</span></a></p></li>
<li><p><a href="../../shipping_receiving/daily_operations/receipts_delivery_two_steps#inventory-receipts-delivery-two-steps"><span class="std std-ref">Delivery in two steps</span></a></p></li>
<li><p><a href="../../shipping_receiving/daily_operations/delivery_three_steps#inventory-delivery-three-steps"><span class="std std-ref">Delivery in three steps</span></a></p></li>
</ul>
</div>

Click the checkbox to the left of the corresponding outgoing operation to add
them to the batch. With the desired pickings selected, click the **⚙️ Actions
(gear)** button, and select the **Add to batch** option from the resulting
drop-down menu.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>To create a cluster batch, as shown in the <a href="#inventory-misc-cluster-picking-example"><span class="std std-ref">example above</span></a>, in a warehouse configured with two-step outgoing
shipments, the following pick operations are selected:</p>
<ul>
<li><p><code>WH/PICK/00007</code>: linked to <abbr title="Sales Order">SO</abbr> 88 for one apple and orange.</p></li>
<li><p><code>WH/PICK/00008</code>: linked to <abbr title="Sales Order">SO</abbr> 89 for one apple and banana.</p></li>
<li><p><code>WH/PICK/00009</code>: linked to <abbr title="Sales Order">SO</abbr> 90 for one apple, orange, and banana.</p></li>
</ul>
<img alt="Use *Add to batch* button, from the *Action* button's list." class="align-center" src="../../../../../_images/select-picks.png"/>
</div>

Doing so opens an **Add to batch** pop-up window, wherein the employee
**Responsible** for the picking can be assigned.

Choose from the two options in the **Add to** field to either: add to **an
existing batch transfer** , or create **a new batch transfer**.

To create draft batch pickings to be confirmed at a later date, select the
**Draft** checkbox.

Conclude the process by clicking **Confirm**.

![Show *Add to batch* window to create a batch
transfer.](../../../../../_images/add-to-batch-window1.png)

## Process batches

To process batches, navigate to Inventory app ‣ Operations ‣ Batch Transfers.
Click on a batch to select it.

In the **Detailed Operations** tab, products that are to be picked are grouped
by location.

Under the **Source Package** or **Destination Package** field, enter the
package used for the picking.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Use the <b>Source Package</b> field when the picking package is configured as <em>reusable</em> on
the <a href="#inventory-misc-create-package"><span class="std std-ref">package form</span></a>. This means the products are temporarily
placed in a container during picking, before getting transferred to their final shipping box.</p>
<p>Alternatively, use the <b>Destination Package</b> field when the product is directly placed
in its <em>disposable</em> shipping box during picking.</p>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>Process the cluster batch for the three orders of apples, oranges, and bananas <a href="#inventory-misc-cluster-picking-example"><span class="std std-ref">example</span></a> by assigning each picking to a dedicated package.</p>
<p>At the storage location for apples, <code>WH/Stock/Shelf A</code>, assign the apples in all three pickings
to one of the three disposable packages, <code>CLUSTER-PACK-1</code>, <code>CLUSTER-PACK-2</code>, or <code>CLUSTER-PACK-3</code>.</p>
<p>Record this in Konvergo ERP using the <b>Destination Package</b> field in the <b>Detailed
Operations</b> tab.</p>
<img alt="Example of processing cluster pickings in *Inventory*." class="align-center" src="../../../../../_images/cluster-batch-example.png"/>
</div>

### In Barcode

To process cluster pickings directly from the _Barcode_ app, select the
**Batch Transfers** button from the _Barcode_ dashboard. Then, select the
desired batch.

On the batch transfer screen, the products in the picking are grouped by
location, and each line is color-coded to associate products in the same
picking together.

Then, follow the prompt to **Scan the source location** barcode for the
storage location of the first product. Then, scan the barcode for the product
and package to process the transfer.

Repeat this for all products, and click the **Validate** button.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>To find the package barcode, navigate to Inventory app ‣ Products ‣
Packages, select the desired package, click the <b>⚙️ (gear)</b> icon at the top of the
package form, and select the <b>Print</b> option.</p>
<p>Next, select one of the three print options to generate the package barcode from the
<b>Package Reference</b> field.</p>
<img alt="Display where the package barcode can be generated." class="align-center" src="../../../../../_images/find-package-barcode.png"/>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../product_management/product_tracking/package">Packages</a></p>
</div>0 <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../product_management/product_tracking/package">Packages</a></p>
</div>1

  *[SOs]: Sales Orders
  *[SO]: Sales Order

