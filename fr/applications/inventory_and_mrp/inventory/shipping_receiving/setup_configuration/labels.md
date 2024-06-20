# Print shipping labels

Integrate Odoo with [third-party shipping carriers](third_party_shipper.html)
to automatically generate shipping labels that includes prices, destination
addresses, tracking numbers, and barcodes.

## Configuration

To generate labels for a third-party shipping carrier, first [install the
third-party shipping connector](third_party_shipper.html). Then, configure and
activate the [delivery method](third_party_shipper.html#inventory-shipping-
receiving-configure-delivery-method), being sure to set the Integration Level
to Get Rate and Create Shipment to generate shipping labels. Finally, provide
the company’s [source address](third_party_shipper.html#inventory-shipping-
receiving-configure-source-address) and [product
weights](third_party_shipper.html#inventory-shipping-receiving-configure-
weight).

Pour plus d'infos

[Third-party shipping carriers](third_party_shipper.html)

![Set the "Get Rate and Create Shipment"
option.](../../../../../_images/integration-level.png)

## Print tracking labels

Tracking labels are generated after the delivery order (DO) is validated.

When both the _Sales_ and _Inventory_ apps are installed, begin on the Sales
app, and proceed to the desired quotation to add the shipping cost, confirm
the sales order, and validate the DO.

If only the _Inventory_ app is installed, create DOs directly in the Inventory
app , add the third-party carrier in the Carrier field, and validate the DO.

### Add shipping on quotation

To generate a tracking label for an order, begin by creating a quotation in
Sales app ‣ Orders ‣ Quotations, clicking New, and filling out the quotation
form. Then, click the Add Shipping button in the bottom-right corner of the
quotation.

![Show the "Add Shipping" button on the
quotation.](../../../../../_images/add-shipping-button.png)

In the resulting pop-up window, select the intended carrier from the Shipping
Method drop-down menu. Clicking Get Rate displays the shipping cost for the
customer, via the third-party carrier in the Cost field.

Important

If clicking Get Rate results in an error, ensure the [warehouse’s
address](third_party_shipper.html#inventory-shipping-receiving-configure-
source-address) and [weight of products in the
order](third_party_shipper.html#inventory-shipping-receiving-configure-weight)
are properly configured.

Click Add to add the cost to the quotation, which is listed as the [configured
delivery product](delivery_method.html#inventory-shipping-receiving-delivery-
product). Finally, click Confirm on the quotation, and click the Delivery
smart button to access the DO.

![Show "Get rate" pop-up window.](../../../../../_images/get-rate.png)

Astuce

For users who do not have the _Sales_ app installed, the shipping carrier is
specified in a delivery order’s Carrier field of the Additional Info tab.

![Show the "Additional Info" tab of a delivery
order.](../../../../../_images/additional-info-tab.png)

### Validate delivery order

On a delivery order form, navigate to the Additional Info tab to ensure the
third-party shipping carrier has been added to the Carrier field.

Important

If the _Sales_ app is not installed, the third-party carrier is set in the
Carrier field.

After the items in the order have been packed, click Validate to get the
shipping carrier’s tracking number, and generate the shipping label.

Note

Create or select an existing delivery order by going to the Inventory app, and
selecting the Delivery Orders card.

The Tracking Reference number is generated in the Additional Info tab of the
delivery order. Click the Tracking smart button to access the tracking link
from the shipping carrier’s website.

The tracking label is found in PDF format in the chatter.

![Show generated shipping label in the
chatter.](../../../../../_images/shipping-label.png)

Note

For multi-package shipping, one label is generated per package. Each label
appears in the chatter.

![Sample label generated from Odoo's shipping connector with
FedEx.](../../../../../_images/sample-label.png)

Sample label generated from Odoo’s shipping connector with FedEx.

Pour plus d'infos

  * [Shipping cost invoicing](../advanced_operations_shipping/invoicing.html)

  * [Expédition de plusieurs colis](../advanced_operations_shipping/multipack.html)

  *[DO]: Delivery Order
  *[DOs]: Delivery Orders

