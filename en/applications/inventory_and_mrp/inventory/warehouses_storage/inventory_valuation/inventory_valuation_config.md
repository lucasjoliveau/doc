# Inventory valuation configuration

All of a company’s stock on-hand contributes to the valuation of its
inventory. That value should be reflected in the company’s accounting records
to accurately show the value of the company and all of its assets.

By default, Konvergo ERP uses a periodic inventory valuation (also known as manual
inventory valuation). This method implies that the accounting team posts
journal entries based on the physical inventory of the company, and that
warehouse employees take the time to count the stock. In Konvergo ERP, this method is
reflected inside each product category, where the **Costing Method** field
will be set to `Standard Price` by default, and the **Inventory Valuation**
field will be set to `Manual`.

![The Inventory Valuation fields are located on the Product Categories
form.](../../../../../_images/inventory-valuation-fields.png)

Alternatively, automated inventory valuation is an integrated valuation method
that updates the inventory value in real-time by creating journal entries
whenever there are stock moves initiated between locations in a company’s
inventory.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Automated inventory valuation is a method recommended for expert accountants, given the extra
steps involved in journal entry configuration. Even after the initial setup, the method will
need to be periodically checked to ensure accuracy, and adjustments may be needed on an ongoing
basis depending on the needs and priorities of the business.</p>
</div>

## Types of accounting

Accounting entries will depend on the accounting mode: _Continental_ or
_Anglo-Saxon_.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Verify the accounting mode by activating the <a href="../../../../general/developer_mode#developer-mode"><span class="std std-ref">Developer mode (debug mode)</span></a> and navigating to
Accounting app ‣ Configuration ‣ Settings.</p>
<p>Then, in the search bar, look for <b>Anglo-Saxon Accounting</b>, to see if the feature is
enabled. If it is <b>not</b> enabled, Continental accounting mode is in use.</p>
<img alt="Show the Anglo-Saxon accounting mode feature." class="align-center" src="../../../../../_images/anglo-saxon.png"/>
</div>

In _Anglo-Saxon_ accounting, the costs of goods sold (COGS) are reported when
products are sold or delivered. This means that the cost of a good is only
recorded as an expense when a customer is invoiced for a product. So for
**manual** valuation method, set the **Expense Account** to `Stock Valuation`
for the current asset type; for **automatic** valuation method, set the the
**Expense Account** to an _Expenses_ or a _Cost of Revenue_ type (e.g. `Cost
of Production`, `Cost of Goods Sold`, etc.).

In _Continental_ accounting, the cost of a good is reported as soon as a
product is received into stock. Because of this, the **Expense Account** can
be set to **either** _Expenses_ or a _Cost of Revenue_ type, however, it is
more commonly set to an _Expenses_ account.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="#inventory-management-config-inventory-valuation"><span class="std std-ref">Details about configuring Expense and Stock accounts</span></a></p>
</div>

## Configuration

Make changes to inventory valuation options by navigating to Inventory app ‣
Configuration ‣ Product Categories. In the **Inventory Valuation** section,
select the desired **Costing Method** and **Inventory Valuation** options.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>It is possible to use different valuation settings for different product categories.</p>
</div> ![Show inventory valuation configuration
options.](../../../../../_images/config-inventory-valuation.png)

### Costing method

From the product category’s configuration page, choose the desired **Costing
Method** :

  * **Standard Price** : the default costing method in Konvergo ERP. The cost of the product is manually defined on the product form, and this cost is used to compute the valuation. Even if the purchase price on a purchase order differs, the valuation will still use the cost defined on the product form.

  * **Average Cost (AVCO)** : calculates the valuation of a product based on the average cost of that product, divided by the total number of available stock on-hand. With this costing method, inventory valuation is _dynamic_ , and constantly adjusts based on the purchase price of products.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When choosing <b>Average Cost (AVCO)</b> as the <b>Costing Method</b>, changing the
numerical value in the <b>Cost</b> field for products in the respective product category
creates a new record in the <em>Inventory Valuation</em> report to adjust the value of the product.
The <b>Cost</b> amount will then automatically update based on the average purchase price
both of inventory on hand and the costs accumulated from validated purchase orders.</p>
</div>

  * **First In First Out (FIFO)** : tracks the costs of incoming and outgoing items in real-time and uses the real price of the products to change the valuation. The oldest purchase price is used as the cost for the next good sold until an entire lot of that product is sold. When the next inventory lot moves up in the queue, an updated product cost is used based on the valuation of that specific lot. This method is arguably the most accurate inventory valuation method for a variety of reasons, however, it is highly sensitive to input data and human error.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>Changing the costing method greatly impacts inventory valuation. It is highly recommended to
consult an accountant first before making any adjustments here.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="using_inventory_valuation">Using inventory valuation</a></p>
</div>

When the **Costing Method** is changed, products already in stock that were
using the **Standard** costing method **do not** change value; rather, the
existing units keep their value, and any product moves from then on affect the
average cost, and the cost of the product will change. If the value in the
**Cost** field on a product form is changed manually, Konvergo ERP will generate a
corresponding record in the _Inventory Valuation_ report.

### Inventory valuation

Inventory valuation in Konvergo ERP can be set to be updated manually or
automatically. While _Expense_ accounts apply to both, the _Stock Input_ and
_Stock Output_ accounts are only used for automated valuation.

Refer to the Expense and Stock input/output sections for details on
configuring each account type.

#### Expense account

To configure the _expense account_ , go to the **Account Properties** section
of the intended product category (Inventory app ‣ Configuration ‣ Product
Categories). Then, choose an existing account from the **Expense Account**
drop-down menu.

To ensure the chosen account is the correct **Type,** click the __**(right
arrow)** icon to the right of the account. Then, set the account type based on
the information below.

Anglo-SaxonContinental

AutomatedManual

In Anglo-Saxon accounting for automated inventory valuation, set the **Expense
Account** to the `Expenses` account. Then, click the __**(right arrow)** icon
to the right of the account.

In the pop-up window, choose **Expenses** or **Cost of Revenue** from the
**Type** drop-down menu.

![Show **Expense Account** field, and external link
icon.](../../../../../_images/external-link1.png)

To configure the **Expense Account** , choose **Stock Valuation** from the
field’s drop-down menu. Verify the account’s type by clicking the __**(right
arrow)** icon, and then ensure the **Type** is **Current Assets**.

![Show the **Expense Account** field.](../../../../../_images/manual-anglo-
saxon-expense.png)

AutomatedManual

Set the **Expense Account** to the **Expenses** or **Cost of Revenue** account
type.

Set the **Expense Account** to the **Expenses** or **Cost of Revenue** account
type.

#### Stock input/output (automated only)

To configure the **Stock Input Account** and **Stock Output Account** , go to
Inventory app ‣ Configuration ‣ Product Categories and select the desired
product category.

In the **Inventory Valuation** field, select **Automated**. Doing so makes the
**Account Stock Properties** section appear. These accounts are defined as
follows:

  * **Stock Valuation Account** : when automated inventory valuation is enabled on a product, this account will hold the current value of the products.

  * **Stock Journal** : accounting journal where entries are automatically posted when a product’s inventory valuation changes.

  * **Stock Input Account** : counterpart journal items for all incoming stock moves will be posted in this account, unless there is a specific valuation account set on the source location. This is the default value for all products in a given category, and can also be set directly on each product.

  * **Stock Output Account** : counterpart journal items for all outgoing stock moves will be posted in this account, unless there is a specific valuation account set on the destination location. This is the default value for all products in a given category, and can also be set directly on each product.

Anglo-SaxonContinental

In Anglo-Saxon accounting, the **Stock Input Account** and **Stock Output
Account** are set to _different_ **Current Assets** accounts. This way,
delivering products and invoicing the customer balance the _Stock Output_
account, while receiving products and billing vendors balance the _Stock
Input_ account.

To modify the account type, go to the click the __**(right arrow)** icon to
the right of the stock input/output account. In the pop-up window, choose
**Current Assets** from the **Type** drop-down menu.

![Display account setup page, highlighting the **Type**
field.](../../../../../_images/account-type.png)

The _Stock Input_ account is set to `Stock Interim (Received)`, a _Current
Asset_ account type.

In Continental accounting, the **Stock Input Account** and **Stock Output
Account** are set to **the same** **Current Assets** account. That way, one
account can be balanced when items are bought and sold.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>The stock input and output accounts are both set to <code>Stock Interim (Received)</code>, a
<b>Current Assets</b> account type. They can also be set to the <code>Stock Interim
(Delivered)</code>, as long as the input and output accounts are assigned to the <b>same</b>
account.</p>
<img alt="Show the Stock Input and Output accounts." class="align-center" src="../../../../../_images/continental-stock-account.png"/>
</div>

## Inventory valuation reporting

To start, go to Accounting ‣ Reporting ‣ Balance Sheet. At the top of the
dashboard, change the **As of** field value to **Today** , and adjust the
filtering **Options** to **Unfold All** in order to see all of the latest data
displayed, all at once.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../../../finance/accounting/get_started/cheat_sheet">Accounting cheat sheet</a></p>
</div>

Under the parent **Current Assets** line item, look for the nested **Stock
Valuation Account** line item, where the total valuation of all of the
inventory on hand is displayed.

Access more specific information with the **Stock Valuation Account** drop-
down menu, by selecting either the **General Ledger** to see an itemized view
of all of the journal entries, or by selecting **Journal Items** to review all
of the individualized journal entries that were submitted to the account. As
well, annotations to the **Balance Sheet** can be added by choosing
**Annotate** , filling in the text box, and clicking **Save**.

![See the full inventory valuation breakdown in Konvergo ERP Accounting
app.](../../../../../_images/stock-valuation-breakdown-in-accounting.png)

