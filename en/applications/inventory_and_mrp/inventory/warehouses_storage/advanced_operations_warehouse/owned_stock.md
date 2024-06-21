# Consignment: buy and sell stock without owning it

Most of the time, products stored in a company’s warehouse are either
purchased from suppliers, or are manufactured in-house. However, suppliers
will sometimes let companies store and sell products in the company’s
warehouse, without having to buy those items up-front. This is called
_consignment_.

Consignment is a useful method for suppliers to launch new products, and
easily deliver to their customers. It’s also a great way for the company
storing the products (the consignee) to earn something back for their efforts.
Consignees can even charge a fee for the convenience of storing products they
don’t actually own.

## Enable the consignment setting

To receive, store, and sell consignment stock, the feature needs to be enabled
in the settings. To do this, go to Inventory ‣ Configuration ‣ Settings, and
under the **Traceability** section, check the box next to **Consignment** ,
and then click **Save** to finish.

![Enabled Consignment setting in Inventory
configuration.](../../../../../_images/owned-stock-enable-consignment.png)

## Receive (and store) consignment stock

With the feature enabled in Konvergo ERP, consignment stock can now be received into a
warehouse. From the main Inventory dashboard, click into the **Receipts**
section. Then, click **Create**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Consignment stock is not actually purchased from the vendor; it is simply received and stored.
Because of this, there are no quotations or purchase orders involved in receiving consignment
stock. So, <em>every</em> receipt of consignment stock will start by creating manual receipts.</p>
</div>

Choose a vendor to enter in the **Receive From** field, and then choose the
same vendor to enter in the **Assign Owner** field.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Since the products received from the vendor will be owned by the same vendor, the
<b>Receive From</b> and <b>Assign Owner</b> fields must match.</p>
</div>

Once the vendor-related fields are set, enter products into the **Product**
lines, and set the quantities to be received into the warehouse under the
**Done** column. If the **Units of Measure** feature is enabled, the UoM can
be changed, as well. Once all the consignment stock has been received,
**Validate** the receipt.

![Matching vendor fields in consignment Receipt
creation.](../../../../../_images/owned-stock-receipt-fields.png)

## Sell and deliver consignment stock

Once consignment stock has been received into the warehouse, it can be sold
the same as any other in-stock product that has the **Can Be Sold** option
enabled on the product form.

To create a sales order, navigate to the Sales app, and from the
**Quotations** overview, click **Create**. Next, choose a customer to enter
into the **Customer** field.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The <b>Customer</b> <em>must</em> be different from the <b>Vendor</b> that supplied the
consignment stock received (and stored) in the warehouse.</p>
</div>

Add the consignment product under the **Product** column in the order lines,
set the **Quantity** , and fill out any other pertinent product details on the
form. Once the quotation is complete, click **Confirm**.

![Sales order of consignment stock.](../../../../../_images/owned-stock-sales-
order.png)

Once the RFQ has been confirmed, it will become a sales order. From here, the
products can be delivered by clicking on the **Delivery** smart button, and
selecting **Validate** to validate the delivery.

## Traceability and reporting of consignment stock

Although consignment stock is owned by the vendor who supplied it, and not by
the company storing it in their warehouse, consignment products will _still_
appear in certain inventory reports.

To find inventory reports, go to Inventory ‣ Reporting, and choose a report to
view.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Since the consignee does not actually own consigment stock, these products are <em>not</em> reflected
in the <b>Stock Valuation</b> report, and have no impact on the consignee’s inventory
valuation.</p>
</div>

### Product moves report

To view all information about on-hand stock moves, navigate to the the
**Product Moves** dashboard by going to Inventory ‣ Reporting ‣ Product Moves.
For consignment products, the information in this report is the same as any
other product: the history of its product moves can be reviewed; the
**Quantity Done** and **Reference** document are available; and its
**Locations** are available, as well. The consignment stock will originate
from **Partner Location/Vendors**.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>To view a consignment product’s moves by ownership, select the <b>Group By</b> filter,
choose the <b>Add Custom Group</b> parameter, and then select <b>From Owner</b>, and
<b>Apply</b> to finish.</p>
</div> ![Consignment stock moves
history.](../../../../../_images/owned-stock-moves-history.png)
<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>To see forecasted units of consignment stock, go to Inventory ‣ Reporting ‣
Forecasted Inventory.</p>
</div>

### Stock on hand report

View the **Stock On Hand** dashboard by navigating to Inventory ‣ Reporting ‣
Inventory Report. From this report, the **Locations** of all stock on-hand are
displayed, in addition to the quantities per location. For consigment
products, the **Owner** column will be populated with the owner of those
products, or the original vendor who supplied the products in the first place.

  *[UoM]: Units of Measure
  *[RFQ]: Request for Quotation

