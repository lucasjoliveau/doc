# Configure reordering rules

For certain products, it is necessary to ensure that there is always a minimum
amount available on hand at any given time. By adding a reordering rule to a
product, it is possible to automate the reordering process so that a purchase
order is automatically created whenever the amount on hand falls below a set
threshold.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>The <em>Inventory</em> module must be installed to use reordering rules.</p>
</div>

## Configure products for reordering

Products must be configured in a specific way before a reordering rule can be
added to them.

Starting from the Inventory, Manufacturing, Purchase, or Sales module,
navigate to Products ‣ Products and then click **Create** to make a new
product. Alternatively, find a product that already exists in the database and
click into it’s product form.

Next, on the product form, enable reordering by checking the **Can be
Purchased** option underneathe the **Product Name** field. Finally, set the
**Product Type** to `Storable Product` under the **General Information** tab.

![Configure a product for reordering in Konvergo ERP.](../../../../_images/product-
configured-for-reordering.png)

## Add a reordering rule to a product

After properly configuring a product, a reordering rule can be added to it by
selecting the now visible **Reordering Rules** tab at the top of that
product’s form, and then clicking **Create** on the **Reordering Rules**
dashboard.

![Access reordering rules for a product from the product page in
Konvergo ERP.](../../../../_images/reordering-rules-tab.png)

Once created, the reordering rule can be configured to generate purchase
orders automatically by defining the following fields:

  * **Location** specifies where the ordered quantities should be stored once they are received and entered into stock.

  * **Min Quantity** sets the lower threshold for the reordering rule while **Max Quantity** sets the upper threshold. If the stock on hand falls below the minimum quantity, a new purchase order will be created to replenish it up to the maximum quantity.

> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>If <b>Min Quantity</b> is set to <code>5</code> and <b>Max Quantity</b> is set to <code>25</code> and the
stock on hand falls to four, a purchase order will be created for 21 units of the product.</p>
</div>

  * **Multiple Quantity** can be configured so that products are only ordered in batches of a certain quantity. Depending on the number entered, this can result in the creation of a purchase order that would put the resulting stock on hand above what is specified in the **Max Quantity** field.

> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>If <b>Max Quantity</b> is set to <code>100</code> but <b>Multiple Quantity</b> is set to order
the product in batches of <code>200</code>, a purchase order will be created for 200 units of the
product.</p>
</div>

  * **UoM** specifies the unit of measurement by which the quantity will be ordered. For discrete products, this should be set to `Units`. However, it can also be set to units of measurement like `Volume` or `Weight` for non-discrete products like water or bricks.

![Configure the reordering rule in Konvergo ERP.](../../../../_images/reordering-rule-
configuration1.png)

## Manually trigger reordering rules using the scheduler

Reordering rules will be automatically triggered by the scheduler, which runs
once a day by default. To trigger reordering rules manually, navigate to
Inventory ‣ Operations ‣ Run Scheduler. On the pop-up window, confirm the
manual action by clicking **Run Scheduler**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Manually triggering reordering rules will also trigger any other scheduled actions.</p>
</div>

## Manage reordering rules

To manage the reordering rules for a single product, navigate to that product
page’s form and select the **Reordering Rules** tab at the top of the form.

To manage all reordering rules for every product, go to Inventory ‣
Configuration ‣ Reordering Rules. From this dashboard, typical bulk actions in
Konvergo ERP can be performed such as exporting data or archiving rules that are no
longer needed. As well, the **Filters** , **Group By** or triple-dotted menu
on the form are available to search for and/or organize the reordering rules
as desired.

