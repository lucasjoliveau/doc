# Process deliveries in three steps

Some companies process large amounts of deliveries every day, many of which
include multiple products or require special packaging. To make this
efficient, a packing step is needed before shipping out products. For this,
Odoo has a three step process for delivering goods.

In the default three-step delivery process, products that are part of a
delivery order are picked in the warehouse according to their removal
strategy, and brought to a packing zone. After the items have been packed into
the different shipments in the packing zone, they are brought to an output
location before being shipped. These steps can be modified if they do not fit
the needs of the business.

## Configuration

Odoo is configured by default to [receive and deliver goods in one
step](receipts_delivery_one_step.html#inventory-receipts-delivery-one-step),
so the settings need to be changed in order to utilize three step deliveries.
First, make sure the _Multi-Step Routes_ option is enabled in Inventory ‣
Configuration ‣ Settings ‣ Warehouse. Note that activating Multi-Step Routes
will also activate _Storage Locations_.

![Activate multi-step routes and storage locations in inventory
settings.](../../../../../_images/multi-step-routes.png)

Next, the warehouse needs to be configured for three step deliveries. To do
this, go to Inventory app ‣ Configuration ‣ Warehouses, and click on the
warehouse to edit. Then, select Pack goods, send goods in output and then
deliver (3 steps) for Outgoing Shipments.

![Set outgoing shipment option to deliver in three
steps.](../../../../../_images/three-step-warehouse-config.png)

Activating three-step receipts and deliveries creates two new internal
locations: a _Packing Zone_ (WH/Packing Zone), and _Output_ (WH/Output). To
rename these locations, go to Inventory app ‣ Configuration ‣ Locations, click
on the Location to change, and update the name.

## Deliver in three steps (pick + pack + ship)

### Create a sales order

To create a new quote, navigate to Sales app ‣ Create, which reveals a blank
quotation form. On the blank quotation form, select a Customer, add a storable
Product, and click Confirm.

A Delivery smart button appears in the top right of the quotation form.
Clicking it shows the picking order, packing order, and the delivery order
associated with the sales order.

![After confirming the sales order, the Delivery smart button appears showing
three items associated with it.](../../../../../_images/three-step-delivery-
so.png)

### Process a picking

The picking, packing, and delivery orders will be created once the sales order
is confirmed. To view these transfers, go to Inventory ‣ Operations ‣
Transfers.

![Ready status for the pick operation while the packing and delivery
operations are waiting another operation.](../../../../../_images/three-step-
delivery-transfers.png)

The status of the picking will be Ready, since the product must be picked from
stock before it can be packed. The status of the packing order and delivery
order will both be Waiting Another Operation, since the packing and delivery
cannot happen until the picking is completed. The status of the delivery order
will only change to Ready when the packing has been marked Done.

The receipt can also be found in the _Inventory_ application. In the Overview
dashboard, click the 1 To Process smart button in the Pick kanban card.

![The pick order can be seen in the Inventory Kanban
view.](../../../../../_images/three-step-kanban-pick.png)

Click on the picking to process. If the product is in stock, Odoo will
automatically reserve the product. Click Validate to mark the picking as done,
and complete the transfer to the Packing Zone. Then the packing order will be
ready. Since the documents are linked, the products which have been previously
picked are automatically reserved on the packing order.

![Validate the picking by clicking Validate.](../../../../../_images/validate-
three-step-pick.png)

### Process a packing

The packing order will be ready to be processed once the picking is completed,
and can be found in the Inventory application Overview dashboard. Click the 1
To Process smart button in the Pack kanban card.

![The packing order can be seen in the Inventory kanban
view.](../../../../../_images/three-step-kanban-pack.png)

Click on the packing order associated with the sales order, then click on
Validate to complete the packing.

![Click Validate on the packing order to transfer the product from the packing
zone to the output location.](../../../../../_images/validate-three-step-
pack.png)

Once the packing order is validated, the product leaves the WH/Packing Zone
location and moves to the WH/Output location. Then, the status of the document
will change to Done.

### Process a delivery

The delivery order will be ready to be processed once the packing is
completed, and can be found in the Inventory application Overview dashboard.
Click the 1 To Process smart button in the Delivery Orders kanban card.

![The delivery order can be seen in the Delivery Orders Kanban
view.](../../../../../_images/three-step-kanban-delivery.png)

Click on the delivery order associated with the sales order, then click on
Validate to complete the move.

![Click Validate on the delivery order to transfer the product from the output
location to the customer location.](../../../../../_images/three-step-
delivery-out.png)

Once the delivery order is validated, the product leaves the WH/Output
location and moves to the Partners/Customers location. Then, the status of the
document will change to Done.

