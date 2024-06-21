# Print shipping labels

Integrate Konvergo ERP with [third-party shipping carriers](third_party_shipper)
to automatically generate shipping labels that includes prices, destination
addresses, tracking numbers, and barcodes.

## Configuration

To generate labels for a third-party shipping carrier, first [install the
third-party shipping connector](third_party_shipper). Then, configure and
activate the [delivery method](third_party_shipper#inventory-shipping-
receiving-configure-delivery-method), being sure to set the **Integration
Level** to **Get Rate and Create Shipment** to generate shipping labels.
Finally, provide the company’s [source
address](third_party_shipper#inventory-shipping-receiving-configure-
source-address) and [product weights](third_party_shipper#inventory-
shipping-receiving-configure-weight).

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="third_party_shipper">Third-party shipping carriers</a></p>
</div> ![Set the "Get Rate and Create Shipment"
option.](../../../../../_images/integration-level.png)

## Print tracking labels

Tracking labels are generated after the delivery order (DO) is validated.

When both the _Sales_ and _Inventory_ apps are installed, begin on the Sales
app, and proceed to the desired quotation to add the shipping cost, confirm
the sales order, and validate the DO.

If only the _Inventory_ app is installed, create DOs directly in the Inventory
app , add the third-party carrier in the **Carrier** field, and validate the
DO.

### Add shipping on quotation

To generate a tracking label for an order, begin by creating a quotation in
Sales app ‣ Orders ‣ Quotations, clicking **New** , and filling out the
quotation form. Then, click the **Add Shipping** button in the bottom-right
corner of the quotation.

![Show the "Add Shipping" button on the
quotation.](../../../../../_images/add-shipping-button.png)

In the resulting pop-up window, select the intended carrier from the
**Shipping Method** drop-down menu. Clicking **Get Rate** displays the
shipping cost for the customer, via the third-party carrier in the **Cost**
field.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If clicking <b>Get Rate</b> results in an error, ensure the <a href="third_party_shipper#inventory-shipping-receiving-configure-source-address"><span class="std std-ref">warehouse’s address</span></a> and <a href="third_party_shipper#inventory-shipping-receiving-configure-weight"><span class="std std-ref">weight of products in the
order</span></a> are properly configured.</p>
</div>

Click **Add** to add the cost to the quotation, which is listed as the
[configured delivery product](delivery_method#inventory-shipping-
receiving-delivery-product). Finally, click **Confirm** on the quotation, and
click the **Delivery** smart button to access the DO.

![Show "Get rate" pop-up window.](../../../../../_images/get-rate.png)
<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>For users who do not have the <em>Sales</em> app installed, the shipping carrier is specified in a
delivery order’s <b>Carrier</b> field of the <b>Additional Info</b> tab.</p>
<img alt='Show the "Additional Info" tab of a delivery order.' class="align-center" src="../../../../../_images/additional-info-tab.png"/>
</div>

### Validate delivery order

On a delivery order form, navigate to the **Additional Info** tab to ensure
the third-party shipping carrier has been added to the **Carrier** field.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If the <em>Sales</em> app is not installed, the third-party carrier is set in the <b>Carrier</b>
field.</p>
</div>

After the items in the order have been packed, click **Validate** to get the
shipping carrier’s tracking number, and generate the shipping label.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Create or select an existing delivery order by going to the Inventory app, and
selecting the <b>Delivery Orders</b> card.</p>
</div>

The **Tracking Reference** number is generated in the **Additional Info** tab
of the delivery order. Click the **Tracking** smart button to access the
tracking link from the shipping carrier’s website.

The tracking label is found in PDF format in the chatter.

![Show generated shipping label in the
chatter.](../../../../../_images/shipping-label.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>For multi-package shipping, one label is generated per package. Each label appears in the
chatter.</p>
</div>

![Sample label generated from Konvergo ERP's shipping connector with
FedEx.](../../../../../_images/sample-label.png)

Sample label generated from Konvergo ERP’s shipping connector with FedEx.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../advanced_operations_shipping/invoicing">Shipping cost invoicing</a></p></li>
<li><p><a href="../advanced_operations_shipping/multipack">Multi-package shipments</a></p></li>
</ul>
</div>

  *[DO]: Delivery Order
  *[DOs]: Delivery Orders

