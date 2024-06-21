# Sell stock from multiple warehouses using virtual locations

While keeping stock and selling inventory from one warehouse might work for
smaller companies, bigger companies might need to keep stock in, or sell from,
multiple warehouses in multiple locations.

Sometimes products included in a single sales order might take stock from two
(or more) warehouses; in Konvergo ERP, pulling products from multiple warehouses to
satisfy sales demands can be done using _virtual locations_.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>The solution in this document, describing the use of a virtual warehouse to fulfill orders for
multiple warehouses, has some limitations. Consider the following before proceeding:</p>
<ol class="arabic simple">
<li><p>When the <b>Warehouse</b> field is set to a virtual warehouse on a sales order, the
virtual warehouse’s address is indicated on the picking, packing, and delivery forms, <b>not</b>
the actual warehouse’s address.</p></li>
<li><p>Each location has a <code>warehouse_id</code> (hidden field). This means that the stock in the virtual
warehouse will <b>not</b> be the sum of the stock of the real warehouses, but rather the sum of
the stock in the locations whose warehouse ID is the virtual warehouse.</p></li>
</ol>
</div> <div class="alert alert-danger">
<p class="alert-title">
Danger</p><p>Potential limitation for those using <a href="../../shipping_receiving/daily_operations/receipts_delivery_two_steps">two</a> or <a href="../../shipping_receiving/daily_operations/delivery_three_steps">three-step
delivery</a>:</p>
<ol class="arabic simple">
<li><p>The output or packing zone on the various forms is incorrectly listed as the virtual
warehouse’s address.</p></li>
<li><p>There is no workaround for two or three-step deliveries.</p></li>
<li><p>Proceed <b>only</b> if setting a virtual warehouse’s address as the output or packing zone makes
sense for the company’s workflow.</p></li>
</ol>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>In order to create virtual locations in warehouses, and proceed to the following steps, the
<b>Storage Locations</b> and <b>Multi-Step Routes</b> features <b>must</b> be enabled.</p>
<p>To do so, go to Inventory app ‣ Configuration ‣ Settings, scroll down to the
<b>Warehouse</b> section, and enable the <b>Storage Locations</b> and
<b>Multi-Step Routes</b> options. Then, <b>Save</b> the changes to finish.</p>
</div>

## Create virtual parent location

Before creating any virtual stock locations, create a new warehouse that acts
as a _virtual_ warehouse — the _parent_ location of other physical warehouses.

<div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Why a "virtual" warehouse?</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>Virtual warehouses are great for companies with multiple physical warehouses. This is because a
situation might arise when one warehouse runs out of stock of a particular product, but another
warehouse still has stock on-hand. In this case, stock from these two (or more) warehouses could
be used to fulfill a single sales order.</p>
<p>The “virtual” warehouse acts as a single aggregator of all the inventory stored in a company’s
physical warehouses, and is used (for traceability purposes) to create a hierarchy of locations
in Konvergo ERP.</p>
</div></div></div></div>

To create a new warehouse, go to Inventory app ‣ Configuration ‣ Warehouses,
and click **Create**. From here, the warehouse **Name** and **Short Name** can
be changed, and other warehouse details can be changed under the **Warehouse
Configuration** tab.

Lastly, click **Save** to finish creating a _regular_ warehouse. Continue
following the steps below to finish configuring the virtual parent warehouse.

![New warehouse form.](../../../../../_images/stock-warehouses-create-
warehouse.png) <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../inventory_management/warehouses_locations">Warehouse configurations</a></p></li>
<li><p><a href="../../shipping_receiving/daily_operations/receipts_delivery_one_step#inventory-receipts-delivery-one-step-wh"><span class="std std-ref">Incoming and outgoing shipments</span></a></p></li>
<li><p><a href="../inventory_management/resupply_warehouses">Resupply from another warehouse</a></p></li>
</ul>
</div>

## Create child warehouses

Create at least two _child_ warehouses to link to the virtual warehouse.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>In order to take stock from multiple warehouses to fulfill a sales order, there needs to be at
least <b>two</b> warehouses acting as child locations of the virtual parent location warehouse.</p>
</div>

To do that, navigate to Inventory app ‣ Configuration ‣ Warehouses, click
**Create** , and follow the preceding instructions to configure the physical
stock locations.

<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="line-block">
<div class="line"><b>Parent Warehouse</b></div>
<div class="line"><b>Warehouse</b>: <code>Virtual Warehouse</code></div>
<div class="line"><b>Location</b>: <code>VWH/Stock</code></div>
</div>
<div class="line-block">
<div class="line"><b>Child Warehouses</b></div>
<div class="line"><b>Warehouses</b>: <code>Warehouse A</code> and <code>Warehouse B</code></div>
<div class="line"><b>Locations</b>: <code>WHA</code> and <code>WHB</code></div>
</div>
<img alt="Graphic of child locations 'WHA' and 'WHB' tied to the parent location." class="align-center" src="../../../../../_images/parent-location.png"/>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>While the virtual stock location will be changed to ‘View’ later, the <b>Location Type</b>
<b>must</b> be <b>Internal Location</b> at this point to <a href="#inventory-routes-link-to-vwh"><span class="std std-ref">link the child warehouses</span></a> in the next section.</p>
</div>

## Link child warehouses to virtual stock

To set physical warehouses as child locations of the virtual location
configured in the previous step, navigate to Inventory app ‣ Configuration ‣
Locations.

Remove any filters from the search bar. Then, click the physical warehouse
**Location** that was previously created to be a child location (e.g. `WHA`),
and click **Edit**.

Change the **Parent Location** field from **Physical Locations** to the
virtual warehouse’s **stock location** (e.g. `VWH/Stock`) from the drop-down
menu, and click **Save**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>To select the virtual warehouse’s stock location in the <b>Parent Location</b> drop-down
menu, the parent warehouse stock location (e.g. <code>VWH/Stock</code>) <b>must</b>  have its
<b>Location Type</b> set to <b>Internal Location</b>.</p>
</div> ![Set the child warehouse's *Parent Location* to the
virtual warehouse.](../../../../../_images/configure-physical-wh.png)

Repeat the preceding steps to configure two or more child warehouses.

Once complete, the virtual, parent warehouse (e.g. `VWH/Stock`) fulfills
orders using stock from child warehouses (e.g. `WHA` and `WHB`), if there is
insufficient stock in any one location.

## Set virtual stock location as ‘view’

Set the virtual stock location’s **Location Type** to **View** , as it is a
non-existent location used to group various physical warehouses together.

To do that, navigate to Inventory app ‣ Configuration ‣ Locations.

Click the virtual warehouse’s stock location (e.g. `VWH/Stock`) that was
previously created, from the **Locations** list.

On the location form, under the **Additional Information** heading, set the
**Location Type** to **View**. **Save** the changes.

![Warehouse location types in location creation
screen.](../../../../../_images/set-location-type-view.png)
<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>To view the total quantity across <b>all</b> linked child warehouses, go to the product form and
click the <b>On Hand</b> smart button.</p>
<img alt="Display stock across all linked warehouses." class="align-center" src="../../../../../_images/on-hand.png"/>
</div>

## Example: sell products from a virtual warehouse

To sell products from multiple warehouses using a virtual parent location, the
database must have at least **two** warehouses configured — with at least
**one** product, with quantity on-hand in each warehouse, respectively.

<div class="alert alert-danger">
<p class="alert-title">
Danger</p><p>Potential limitation for those using <a href="../../shipping_receiving/daily_operations/receipts_delivery_two_steps">two</a> or <a href="../../shipping_receiving/daily_operations/delivery_three_steps">three-step
delivery</a>:</p>
<ol class="arabic simple">
<li><p>The output or packing zone on the various forms is incorrectly listed as the virtual
warehouse’s address.</p></li>
<li><p>There is no workaround for two or three-step deliveries.</p></li>
<li><p>Proceed <b>only</b> if setting a virtual warehouse’s address as the output or packing zone makes
sense for the company’s workflow.</p></li>
</ol>
</div>0

Create a quotation for the product by navigating to the Sales app and clicking
**Create**. On the quote, add a **Customer** , and click **Add a product** to
add the two products stored in the two warehouses.

Then, click the **Other Info** tab on the sales order form. Under the
**Delivery** section, change the **Warehouse** field value to the virtual
warehouse that was previously created. Next, **Confirm** the sales order.

![Set virtual warehouse as the *Warehouse* field in sales order's *Other Info*
tab.](../../../../../_images/set-virtual-wh.png)

Then, click the **Delivery** smart button. From the warehouse delivery form,
confirm that the **Source Location** value matches the **Warehouse** field
value from the sales order. Both should list the virtual warehouse location.

Finally, on the warehouse delivery form, under the **Detailed Operations**
tab, confirm that the **Locations** in the **From** column for each product
match the child locations that are tied to the virtual parent location.

![Delivery order with matching source and child
locations.](../../../../../_images/delivery-order1.png) <div class="alert alert-danger">
<p class="alert-title">
Danger</p><p>Potential limitation for those using <a href="../../shipping_receiving/daily_operations/receipts_delivery_two_steps">two</a> or <a href="../../shipping_receiving/daily_operations/delivery_three_steps">three-step
delivery</a>:</p>
<ol class="arabic simple">
<li><p>The output or packing zone on the various forms is incorrectly listed as the virtual
warehouse’s address.</p></li>
<li><p>There is no workaround for two or three-step deliveries.</p></li>
<li><p>Proceed <b>only</b> if setting a virtual warehouse’s address as the output or packing zone makes
sense for the company’s workflow.</p></li>
</ol>
</div>1
<div class="alert alert-danger">
<p class="alert-title">
Danger</p><p>Potential limitation for those using <a href="../../shipping_receiving/daily_operations/receipts_delivery_two_steps">two</a> or <a href="../../shipping_receiving/daily_operations/delivery_three_steps">three-step
delivery</a>:</p>
<ol class="arabic simple">
<li><p>The output or packing zone on the various forms is incorrectly listed as the virtual
warehouse’s address.</p></li>
<li><p>There is no workaround for two or three-step deliveries.</p></li>
<li><p>Proceed <b>only</b> if setting a virtual warehouse’s address as the output or packing zone makes
sense for the company’s workflow.</p></li>
</ol>
</div>2

