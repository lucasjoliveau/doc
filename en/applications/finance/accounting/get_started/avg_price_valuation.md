# Average price on returned goods

_Average cost valuation_ (AVCO) is an inventory valuation method that
evaluates cost based on the total cost of goods bought or produced during a
period, divided by the total number of items on-hand. Inventory valuation is
used to:

  * reflect the value of a company’s assets;

  * keep track of the amount of unsold goods;

  * account for monetary value in goods that have yet to generate profit;

  * report on flow of goods throughout the quarter.

Because AVCO uses the weighted average to evaluate the cost, it is a good fit
for companies that sell only a few different products in large quantities. In
Konvergo ERP, this costing analysis is _automatically updated_ each time products are
received.

Thus, when shipments are returned to their supplier, Konvergo ERP automatically
generates accounting entries to reflect the change in inventory valuation.
However, Konvergo ERP does **not** automatically update the AVCO calculation, because
this can potentially create inconsistencies with inventory valuation.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This document addresses a specific use case for theoretical purposes. For instructions on how to
set up and use <abbr title="Average Cost Valuation">AVCO</abbr>, refer to the <a href="../../../inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/inventory_valuation_config">inventory valuation configuration</a>
doc.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../../../inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/using_inventory_valuation">Using inventory valuation</a></p></li>
<li><p><a href="../../../inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/inventory_valuation_config#inventory-inventory-valuation-config-costing-methods"><span class="std std-ref">Other inventory valuation methods</span></a></p></li>
</ul>
</div>

## Configuration

To use average cost inventory valuation on a product, navigate to Inventory ‣
Configuration ‣ Product Categories and select the category that will be using
AVCO. On the product category page, set **Costing Method** to `Average Cost
(AVCO)` and **Inventory Valuation** to `Automated`.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../../inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/inventory_valuation_config">Inventory valuation configuration</a></p>
</div>

## Using average cost valuation

The average cost method adjusts the inventory valuation when products are
received in the warehouse. This section explains how it works, but if the
explanation is unnecessary, skip to the return to supplier use case section.

### Formula

When new products arrive, the new average cost for each product is recomputed
using the formula:

\\[Avg~Cost = \frac{(Old~Qty \times Old~Avg~Cost) + (Incoming~Qty \times
Purchase~Price)}{Final~Qty}\\]

  * **Old Qty** : product count in stock before receiving the new shipment;

  * **Old Avg Cost** : calculated average cost for a single product from the previous inventory valuation;

  * **Incoming Qty** : count of products arriving in the new shipment;

  * **Purchase Price** : estimated price of products at the reception of products (since vendor bills may arrive later). The amount includes not only the price for the products, but also added costs, such as shipping, taxes, and [landed costs](../../../inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/integrating_landed_costs#inventory-reporting-landed-costs). At reception of the vendor bill, this price is adjusted;

  * **Final Qty** : quantity of on-hand stock after the stock move.

<div class="alert alert-warning" id="inventory-avg-cost-definite-rule">
<p class="alert-title">
Important</p><p>When products leave the warehouse, the average cost <b>does not</b> change. Read about why the
average cost valuation is <b>not</b> adjusted <a href="#inventory-avg-price-leaving-inventory"><span class="std std-ref">here</span></a>.</p>
</div>

### Compute average cost

To understand how the average cost of a product changes with each shipment,
consider the following table of warehouse operations and stock moves. Each is
a different example of how the average cost valuation is affected.

Operation | Incoming Value | Inventory Value | Qty On Hand | Avg Cost  
---|---|---|---|---  
|  | $0 | 0 | $0  
Receive 8 tables at $10/unit | 8 * $10 | $80 | 8 | $10  
Receive 4 tables at $16/unit | 4 * $16 | $144 | 12 | $12  
Deliver 10 tables | -10 * $12 | $24 | 2 | $12  
<div class="alert alert-dark" id="inventory-avg-cost-ex-1">
<p class="alert-title">
Exercise</p><p>Ensure comprehension of the above computations by reviewing the “Receive 8 tables at $10/unit”
example.</p>
<p>Initially, the product stock is 0, so all values are $0.</p>
<p>In the first warehouse operation, <code>8</code> tables are received at <code>$10</code> each. The average cost is
calculated using the <a href="#inventory-avg-cost-formula"><span class="std std-ref">formula</span></a>:</p>
<div class="math notranslate nohighlight">
\[Avg~Cost = \frac{0 + 8 \times $10}{8} = \frac{$80}{8} = $10\]</div>
<ul>
<li><p>Since the <em>incoming quantity</em> of tables is <code>8</code> and the <em>purchase price</em> for each is <code>$10</code>,</p></li>
<li><p>The inventory value in the numerator is evaluated to <code>$80</code>;</p></li>
<li><p><code>$80</code> is divided by the total amount of tables to store, <code>8</code>;</p></li>
<li><p><code>$10</code> is the average cost of a single table from the first shipment.</p></li>
</ul>
<p>To verify this in Konvergo ERP, in the <em>Purchase</em> app, order <code>8</code> quantities of a new product, <code>Table</code>,
with no previous stock moves, for <code>$10</code> each.</p>
<p>In the table’s <b>Product Category</b> field in the <b>General Information</b> tab of
the product form, click the <b>➡️ (arrow)</b> icon, to open an <b>External Link</b> to
edit the product category. Set the <b>Costing Method</b> to <code>Average Cost (AVCO)</code> and
<b>Inventory Valuation</b> to <code>Automated</code>.</p>
<p>Then, return to the purchase order. Click <b>Confirm Order</b>, and click <b>Receive
Products</b> to confirm receipt.</p>
<p>Next, check the inventory valuation record generated by the product reception by navigating to
Inventory ‣ Reporting ‣ Inventory Valuation. Select the drop-down for
<code>Table</code>, and view the <b>Total Value</b> column for the <em>valuation layer</em> (<span class="dfn"><span>inventory
valuation at a specific point in time = on-hand quantity * unit price</span></span>). The 8 tables in-stock
are worth $80.</p>
<img alt="Show inventory valuation of 8 tables in Konvergo ERP." class="align-center" src="../../../../_images/inventory-val-8-tables.png"/>
</div> <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>When the product category’s <b>Costing Method</b> is set to <b>AVCO</b>, then the
average cost of a product is also displayed on the <b>Cost</b> field, under the
<b>General Information</b> tab, on the product page itself.</p>
</div>

#### Product delivery (use case)

For outgoing shipments, outbound products have no effect on the average cost
valuation. Although the average cost valuation is not recalculated, the
inventory value still decreases because the product is removed from stock and
delivered to the customer location.

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>To demonstrate that the average cost valuation is not recalculated, examine the “Deliver 10
tables” example.</p>
<div class="math notranslate nohighlight">
\[Avg~Cost = \frac{12 \times $12 + (-10) \times $12}{12-10} = \frac{24}{2} = $12\]</div>
<ol class="arabic simple">
<li><p>Because 10 tables are being sent out to customers, the <em>incoming quantity</em> is <code>-10</code>. The
previous average cost (<code>$12</code>) is used in lieu of a vendor’s <em>purchase price</em>;</p></li>
<li><p>The <em>incoming inventory value</em> is <code>-10 * $12 = -$120</code>;</p></li>
<li><p>The old <em>inventory value</em> (<code>$144</code>) is added to the <em>incoming inventory value</em> (<code>-$120</code>), so
<code>$144 + -$120 = $24</code>;</p></li>
<li><p>Only <code>2</code> tables remain after shipping out <code>10</code> tables from <code>12</code>. So the current <em>inventory
value</em> (<code>$24</code>) is divided by the on-hand quantity (<code>2</code>);</p></li>
<li><p><code>$24 / 2 = $12</code>, which is the same average cost as the previous operation.</p></li>
</ol>
<p>To verify this in Konvergo ERP, sell <code>10</code> tables in the <em>Sales</em> app, validate the delivery, and then
review the inventory valuation record by going to in Inventory ‣ Reporting ‣
Inventory Valuation. In the topmost valuation layer, delivering <code>10</code> tables reduces the
product’s value by <code>-$120</code>.</p>
<p><b>Note</b>: What is not represented in this stock valuation record is the revenue made from this
sale, so this decrease is not a loss to the company.</p>
<img alt="Show how deliveries decrease inventory valuation." class="align-center" src="../../../../_images/inventory-val-send-10-tables.png"/>
</div>

## Return items to supplier (use case)

Because the price paid to suppliers can differ from the price the product is
valued at with the AVCO method, Konvergo ERP handles returned items in a specific way.

  1. Products are returned to suppliers at the original purchase price, but;

  2. The internal cost valuation remains unchanged.

The above example table is updated as follows:

Operation | Qty*Avg Cost | Inventory Value | Qty On Hand | Avg Cost  
---|---|---|---|---  
|  | $24 | 2 | $12  
Return 1 table bought at $10 | -1 * $12 | $12 | 1 | $12  
  
In other words, returns to vendors are perceived by Konvergo ERP as another form of a
product exiting the warehouse. To Konvergo ERP, because the table is valued at $12 per
unit, the inventory value is reduced by `$12` when the product is returned;
the initial purchase price of `$10` is unrelated to the table’s average cost.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>To return a single table that was purchased for <code>$10</code>, navigate to the receipt in the <em>Inventory</em>
app for the <a href="#inventory-avg-cost-ex-1"><span class="std std-ref">8 tables purchased in Exercise 1</span></a> by going to the
<b>Inventory Overview</b>, clicking on <b>Receipts</b>, and selecting the desired
receipt.</p>
<p>Then, click <b>Return</b> on the validated delivery order, and modify the quantity to <code>1</code> in
the reverse transfer window. This creates an outgoing shipment for the table. Select
<b>Validate</b> to confirm the outgoing shipment.</p>
<p>Return to Inventory ‣ Reporting ‣ Inventory Valuation to see how the
outgoing shipment decreases the inventory value by $12.</p>
<img alt="Inventory valuation for return." class="align-center" src="../../../../_images/inventory-valuation-return.png"/>
</div>

### Eliminate stock valuation errors in outgoing products

Inconsistencies can occur in a company’s inventory when the average cost
valuation is recalculated on outgoing shipments.

To demonstrate this error, the table below displays a scenario in which 1
table is shipped to a customer and another is returned to a supplier at the
purchased price.

Operation | Qty*Price | Inventory Value | Qty On Hand | Avg Cost  
---|---|---|---|---  
|  | $24 | 2 | $12  
Ship 1 product to customer | -1 * $12 | $12 | 1 | $12  
Return 1 product initially bought at $10 | -1 * $10 | **$2** | **0** | $12  
  
In the final operation above, the final inventory valuation for the table is
`$2` even though there are `0` tables left in stock.

<div class="admonition-correct-method alert">
<p class="alert-title">
Correct method</p><p>Use the average cost to value the return. This does not mean the company gets $12 back for a $10
purchase; the item returned for $10 is valued internally at $12. The inventory value change
represents a product worth $12 no longer being accounted for in company assets.</p>
</div>

## Anglo-Saxon accounting

In addition to using AVCO, companies that use **Anglo-Saxon accounting** also
keep a holding account that tracks the amount to be paid to vendors. Once a
vendor delivers an order, **inventory value** increases based on the vendor
price of the products that have entered the stock. The holding account (called
**stock input**) is credited and only reconciled once the vendor bill is
received.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../../../inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/inventory_valuation_config#inventory-inventory-valuation-config-accounting"><span class="std std-ref">Anglo-Saxon vs. Continental</span></a></p></li>
</ul>
</div>

The table below reflects journal entries and accounts. The _stock input_
account stores the money intended to pay vendors when the vendor bill has not
yet been received. To balance accounts when returning products that have a
price difference between the price the product is **valued at** and the price
it was bought for, a _price difference_ account is created.

Operation | Stock Input | Price Diff | Inventory Value | Qty On Hand | Avg Cost  
---|---|---|---|---|---  
|  |  | $0 | 0 | $0  
Receive 8 tables at $10 | ($80) |  | $80 | 8 | $10  
Receive vendor bill $80 | $0 |  | $80 | 8 | $10  
Receive 4 tables at $16 | ($64) |  | $144 | 12 | $12  
Receive vendor bill $64 | $0 |  | $144 | 12 | $12  
Deliver 10 tables to customer | $0 |  | $24 | 2 | $12  
Return 1 table initially bought at $10 | **$10** | **$2** | **$12** | 1 | $12  
Receive vendor refund $10 | $0 | $2 | $12 | 1 | $12  
  
### Product reception

#### Summary

At product reception, Konvergo ERP ensures companies can pay for goods that were
purchased by preemptively moving an amount matching the price of received
goods into the [liability account](cheat_sheet), **Stock Input**. Then,
once the bill has been received, the amount in the holding account is
transferred to _Accounts Payable_. Transfers into this account means the bill
has been paid. **Stock Input** is reconciled once the vendor bill is received.

Inventory valuation is a method of calculating how much each in-stock product
is worth internally. Since there is a difference between the price the product
is **valuated at** and the price the product was actually **purchased for** ,
the **Inventory Valuation** account is unrelated to the crediting and debiting
operations of the **Stock Input** account.

To conceptualize all this, follow the breakdown below.

#### Accounts balanced at received products

In this example, a company starts with zero units of a product, `table`, in
stock. Then, 8 tables are received from the vendor:

  1. The **Stock Input** account stores `$80` of credit owed to the vendor. The amount in this account is unrelated to the inventory value.

  2. `$80` worth of tables came **in** (**debit** the _Inventory Value_ account `$80`), and

  3. `$80` must be paid **out** for received goods (**credit** the _Stock Input_ account `$80`).

##### In Konvergo ERP

Konvergo ERP generates an accounting journal entry when shipments that use AVCO
costing method are received. Configure a **Price Difference Account** by
selecting the **➡️ (arrow)** icon next to the **Product Category** field on
the product page.

Under **Account Properties** , create a new **Price Difference Account** by
typing in the name of the account and clicking **Create and Edit**. Then set
the account **Type** as `Expenses`, and click **Save**.

![Create price difference account.](../../../../_images/create-price-
difference.png)

Then, receive the shipment in the _Purchase_ app or _Inventory_ app, and
navigate to the Accounting app ‣ Accounting ‣ Journal Entries. In the list,
find the **Reference** that matches the warehouse reception operation for the
relevant product.

![Show accounting entry of 8 tables from the
list.](../../../../_images/search-for-entry-of-tables.png)

Click on the line for 8 tables. This accounting journal entry shows that when
the 8 tables were received, the `Stock Valuation` account increased by `$80`.
Conversely, the **Stock Input** account (set as `Stock Interim (Received)`
account by default) is credited `$80`.

![Debit stock valuation and credit stock input 80
dollars.](../../../../_images/accounting-entry-8-tables.png)

#### Accounts balanced at received vendor bill

In this example, a company starts with zero units of a product, table, in
stock. Then, 8 tables are received from the vendor. When the bill is received
from vendor for 8 tables:

  1. Use `$80` in the **Stock Input** account to pay the bill. This cancels out and the account now holds `$0`.

  2. Debit **Stock Input** `$80` (to reconcile this account).

  3. Credit **Accounts payable** `$80`. This account stores the amount the company owes others, so accountants use the amount to write checks to vendors.

##### In Konvergo ERP

Once the vendor requests payment, navigate to the Purchase app ‣ Orders ‣
Purchase and select the PO for 8 tables. Inside the PO, select **Create
Bill**.

Switch to the **Journal Items** tab to view how `$80` is transferred from the
holding account, `Stock Interim (Received)` to `Accounts Payable`. **Confirm**
the bill to record the payment to the vendor.

![Show bill linked to the purchase order for 8
tables.](../../../../_images/receive-8-table-bill.png)

### On product delivery

In the above example table, when 10 products are delivered to a customer, the
**Stock Input** account is untouched because there are no new products coming
in. To put it simply:

  1. **Inventory valuation** is credited `$120`. Subtracting from inventory valuation represents `$120` worth of products exiting the company.

  2. Debit **Accounts Receivable** to record revenue from the sale.

![Show journal items linked to sale
order.](../../../../_images/sell-10-tables.png) <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../../../inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/using_inventory_valuation">Using inventory valuation</a></p></li>
<li><p><a href="../../../inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/inventory_valuation_config#inventory-inventory-valuation-config-costing-methods"><span class="std std-ref">Other inventory valuation methods</span></a></p></li>
</ul>
</div>0

### On product return

In the above example table, when returning 1 product to a vendor purchased at
`$10`, a company expects `$10` in the **Accounts Payable** account from the
vendor. However, **Stock Input** account must be debited `$12` because the
average cost is `$12` at the time of the return. The missing `$2` is accounted
for in the **Price Difference Account** , which is set up in the product’s
**Product Category**.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../../../inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/using_inventory_valuation">Using inventory valuation</a></p></li>
<li><p><a href="../../../inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/inventory_valuation_config#inventory-inventory-valuation-config-costing-methods"><span class="std std-ref">Other inventory valuation methods</span></a></p></li>
</ul>
</div>1

Summary:

  1. Debit **Stock Input** account `$10` to move the table from stock to stock input. This move is to indicate that the table is to be processed for an outgoing shipment.

  2. Debit **Stock Input** an additional `$2` to account for the **Price Difference**.

  3. Credit **Stock Valuation** `$12` because the item is leaving the stock.

![2 dollar difference expensed in Price Difference
account.](../../../../_images/expensing-price-difference-account.png)

Once the vendor’s refund is received,

  1. Credit **Stock Input** account `$10` to reconcile the price of the table.

  2. Debit **Accounts Payable** `$10` to have the accountants collect and register the payment in their journal.

![Return to get 10 dollars back.](../../../../_images/return-credit-note.png)

  *[AVCO]: Average Cost Valuation
  *[PO]: Purchase Order

