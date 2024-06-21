# Pricelists, discounts, and formulas

Konvergo ERP _Sales_ has a useful pricelist feature that can be tailored to fit any
unique pricing strategy.

A _pricelist_ is a list of prices (or price rules) that Konvergo ERP uses to determine
the appropriate price for a customer. These pricelists can be set with
specific criteria (such as time periods, minimum quantity sold, and more) in
order to apply certain prices or discounts.

Pricelists suggest certain prices, but they can always be overridden on the
sales order.

## Pricing strategy options

To choose a pricing strategy, first navigate to Sales app ‣ Configuration ‣
Settings. In the **Pricing** section, click the checkbox next to the
**Pricelists** feature.

Doing so reveals two additional options beneath it: **Multiple prices per
product** and **Advanced price rules (discounts, formulas)**. A link labeled
**Pricelists** also appears, which leads to a separate pricelists page,
wherein pricelists can be created and/or modified.

  * **Multiple prices per product** : provides the option to set several different prices per product.

  * **Advanced price rules (discounts, formulas)** : provides the option to create detailed price rules and apply discounts, margins, and roundings.

![How the pricelist feature setting looks in Konvergo ERP
Sales.](../../../../../_images/pricelist-feature-setting.png)

After clicking the checkbox beside the **Pricelists** feature, select one of
those two options, then click **Save** to save all changes.

## Pricelists

After activating and saving the **Pricelists** feature, the **Settings** page
reloads and, from here, either select the **Pricelists** link (beneath the
**Pricelists** feature on the **Settings** page), or navigate to Sales app ‣
Products ‣ Pricelists.

Either option reveals the **Pricelists** page, in which pricelists can be
created and/or modified at any time.

![How the pricelists page looks in Konvergo ERP
Sales.](../../../../../_images/pricelists-page.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The <b>Public Pricelist</b> is the default pricelist used with Konvergo ERP <em>Sales</em> and <em>eCommerce</em>.</p>
</div>

From the **Pricelists** page, either select the desired pricelist to edit, or
click **New** to create a new pricelist, which reveals a blank pricelist form
that can be configured in a number of different ways.

![How the pricelist detail form looks in Konvergo ERP
Sales.](../../../../../_images/pricelist-detail-form.png)

When creating a new pricelist, start by adding a name for the pricelist at the
top of the form, in the blank field. Next, select which **Currency** should be
used.

Then, if working in a multi-company environment, select which company this
pricelist should apply to in the **Company** field. If this field is left
blank, the pricelist is automatically applied to all companies in the
database.

### Price rules tab

The **Price Rules** tab functionality on a pricelist form varies depending on
the **Pricelists** setting chosen: either **Multiple prices per product** or
**Advanced price rules (discounts, formulas)**.

However, the **Time-based rules** tab and **Configuration** tab are always the
same, regardless of the chosen **Pricelists** setting.

#### Price rules tab (multiple prices per product)

With the **Multiple prices per product** setting activated, the **Price
Rules** tab on pricelist forms provides the option to add specific products,
with a specific price, to a pricelist.

To add a specific product and price to a pricelist form, click the **Price
Rules** tab, then click **Add a line** in the **Products** column. Then,
select the desired product for which a specific price should be applied.

Next, if necessary, select a product variant under the **Variants** column
(e.g. a specific product size, color, etc.). If no variants are selected, then
this price will apply to all variants of the product.

If a minimum amount of the product must be purchased in order to apply the
specific price, enter the amount under the **Min. Quantity** column.

To configure the price of the product for this specific pricelist, enter the
desired amount under the **Price** column. Then, there is the option to add a
**Start Date** and **End Date** to the configured product price, if desired.

To add another product line, click **Add a line** again, and repeat the
process. There is no limit to how many products can be added in the **Price
Rules** tab of a pricelist form.

For more information, check out the following section: Multiple prices per
product.

#### Price rules tab (advanced price rules)

With the **Advanced price rules (discounts, formulas)** setting activated, the
**Price Rules** tab on pricelist forms provides the option to configure
detailed price rules based on formulas.

Check out the Advanced price rules (discounts, formulas) section for detailed
steps on how to add advanced price rules to a pricelist.

### Time-based rules tab

Time-based rules are used specifically with [subscription
products](../../../subscriptions/products). Be sure to check out the Konvergo ERP
_Subscriptions_ [documentation](../../../subscriptions).

Under the **Time-based rules** tab, the same functionality of the **Price
Rules** tab is present, with the only difference being that a repeating time
period can be applied in the **Period** column.

After a **Product** and potential **Variant** are selected in the **Time-based
rules** tab, select the blank field in the **Period** column to reveal a drop-
down menu of pre-designated recurrence periods (e.g. `Monthly`, `Quarterly`,
`Weekly`, etc.).

New recurrence periods can also be directly created from this column, by
typing in the new name for the **Period** and then selecting **Create** to
create the time period, which can be edited later. Or, select **Create and
edit…** to reveal a pop-up form, in which the new recurrence period can be
directly configured.

![Custom time period pop-up form in Konvergo ERP Sales.](../../../../../_images/time-
period-popup.png)

From this **Create Period** pop-up form, add a **Name** , **Duration** , then
a **Unit** (e.g. `Days`, `Weeks`, etc.). When finished, click **Save and
Close**.

Lastly, add the desired price for this time-based rule in the **Price**
column.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../../subscriptions">Subscriptions</a></p>
</div>

### Configuration tab

Under the **Configuration** tab, there are a few options that can further
customize the pricelist.

![Configuration tab on pricelist detail form in Konvergo ERP
Sales.](../../../../../_images/configuration-tab.png)

From here, under the **Availability** section, in the **Country Groups**
field, certain country groups can be added to the pricelist. There is no limit
to how many country groups can be added in this field.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If no country is set for a customer, Konvergo ERP takes the first pricelist without any country group.</p>
</div>

Under the **Website** section, there are a few options that can be configured.
In the **Website** field, this pricelist can be applied to a specific website,
if working in a multi-website environment. If left blank, the pricelist will
be applied to all websites in the database.

Click the **Selectable** checkbox to have this pricelist as a selectable
option for customers to choose as they shop. If the **Selectable** box is left
unchecked, customers **cannot** select this pricelist for themselves as they
shop.

Lastly, there is the option to add an **E-commerce Promotional Code**. To add
a code, type in the desired promo code that, when entered during the checkout
process, applies the pricelist to the customer, even if the customer does not
fall into the previously-specified criteria.

#### Show discount percentage to customers

With Konvergo ERP _Sales_ , the option to show the public price _and_ the computed
discount percentage on the product catalog is available.

To do that, navigate to Sales app ‣ Configuration ‣ Settings, and in the
**Pricing** section, click the checkbox next to the **Discounts** feature, and
then click **Save** to save all changes.

After activating the **Discounts** feature, navigate to the pricelists page,
either by clicking the **Pricelists** link from the **Settings** page, or by
going to Sales app ‣ Products ‣ Pricelists.

On the **Pricelists** page, select the desired pricelist to edit. On the
pricelist form, click into the **Configuration** tab. In the **Configuration**
tab, at the bottom, a **Discounts** section is now available.

![What the discount options are on the configuration tab of a pricelist in
Konvergo ERP Sales.](../../../../../_images/configuration-discount-options.png)

The options available in this section are:

  * **Discount included in the price** : shows the customer only the final price with the discount already included.

  * **Show public price & discount to the customer**: shows the customer the public price _and_ the discount they’re earning.

## Customer pricelist application

While the default pricelist applied to any customer is the **Public
Pricelist** , Konvergo ERP provides the opportunity to directly apply a different
pricelist to customers on their contact form.

To do that, open the desired customer’s contact form, either by navigating to
Sales app ‣ Orders ‣ Customers and selecting the customer from the main
**Customers** page, or by clicking on the customer’s name on a sales order.

![Sample customer detail form in Konvergo ERP Sales.](../../../../../_images/customer-
detail-form.png)

On the desired customer’s contact form, under the **Sales & Purchase** tab, in
the **Sales** section, designate what pricelist should be applied to this
specific customer from the drop-down menu in the **Pricelist** field.

![The pricelist field in a customer detail form in Konvergo ERP
Sales.](../../../../../_images/customer-form-pricelist-field.png)

## Multiple prices per product

To apply several prices per individual product, select the **Multiple prices
per product** option, after enabling the **Pricelists** feature on the _Sales_
app setting page (Sales app ‣ Configuration ‣ Settings), and click **Save**.

Next, apply pricelists to specific products using the product form. Navigate
to the Sales app ‣ Products ‣ Products and select the product for which
multiple prices should be applied. Selecting a product from the **Products**
page reveals that specific product’s product form on a separate page.

On the product form, click the **Extra Prices** smart button, located at the
top of the form.

![How the extra prices smart button appears in Konvergo ERP
Sales.](../../../../../_images/extra-prices-smartbutton.png)

Doing so reveals a separate page displaying the **Price Rules** that are
specific to that particular product. Here, price rules can be edited or
created at any time.

![How the extra price rules per product page appears in Konvergo ERP
Sales.](../../../../../_images/price-rules-product-page.png)

To create a new price rule for a product from this specific **Price Rules**
page, click **New** to add a new, customizable row that has the desired
product already populated in the **Applied On** column.

Next, select which **Pricelist** this specific product price rule should apply
to, via the drop-down menu in the **Pricelist** column.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The <b>Public Pricelist</b> is the default pricelist used with Konvergo ERP <em>Sales</em> and <em>eCommerce</em>.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>To create a new pricelist from this page, type in the desired name of the new pricelist in the
<b>Pricelist</b> column, then select <b>Create</b> from the drop-down menu. All
pricelists can be modified at any time, by navigating to Sales app ‣ Products
‣ Pricelists. Pricelists can also be created on that specific <b>Pricelists</b> page, as
well.</p>
</div>

After the desired pricelist is added to the row, designate a **Min. Quantity**
for the price rule.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>If the <b>Min. Quantity</b> column is set to <code>2</code>, the new price in the <b>Price</b>
column will be applied to orders of 2 or more products. So, in theory, if a single product costs
$100, customers can be encouraged to buy more, if the <b>Price</b> is set at $85 per product
for a <b>Min. Quantity</b> of <code>2</code> products.</p>
</div>

Next, enter the desired amount in the **Price** column. Then, if needed, enter
a **Start Date** and **End Date** for the product’s price rule.

And lastly, if working in a multi-company environment, select which company
this price rule should be applied to in the **Company** field. Leaving this
field blank means the price rule applies for all companies in the database.

Click away from the row to activate Konvergo ERP’s auto-save capability, meaning that
newly-created price rule is now ready to be used.

Proceed to add as many unique price rules per product as desired. There is no
limit to how many price rules can be added per product.

With the price rule(s) in place for a specific product, customers who fall
into those corresponding pricelists automatically see those new prices
applied. The number of price rules applied to a particular product are also
displayed in the **Extra Prices** smart button, located on every product form.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When a price rule/pricelist is added to a product via the <b>Extra Prices</b> smart button,
it is also reflected on the pricelist itself. Similarly, when a price rule for a specific product
is added to a pricelist, it is also reflected on the product form via the <b>Extra
Prices</b> smart button.</p>
</div>

## Advanced price rules

The **Advanced price rules (discounts, formulas)** pricelist feature provides
the option to set price change rules based on discounts and formulas. These
changes can be relative to the product list/catalog price, the product’s cost,
or another pricelist.

To use advanced pricing rules, with discounts and formulas, select the
**Advanced price rules (discounts, formulas)** option, after enabling the
**Pricelists** feature on the _Sales_ app setting page (Sales app ‣
Configuration ‣ Settings), and click **Save**.

After activating and saving that **Pricelists** feature, the **Settings** page
reloads and, from here, either select the **Pricelists** link (beneath the
**Pricelists** feature on the **Settings** page), or navigate to Sales app ‣
Products ‣ Pricelists.

Either option reveals the **Pricelists** page, in which pricelists can be
created and/or modified at any time.

From the **Pricelists** page, select a desired pricelist to modify, or create
a new pricelist by clicking the **New** button.

On the pricelist form, under the **Price Rules** tab, click **Add a line** to
add an advanced price rule. Doing so reveals a **Create Pricelist Rules** pop-
up form, in which the advanced rule is configured.

![How the Create Pricelist Rules pop-up form looks in Konvergo ERP
Sales.](../../../../../_images/create-pricelist-rules-popup.png)

### Price computation

On this form, first choose one of the three **Computation** options:

  * **Fixed Price** : the price computation is based on a fixed price.

  * **Discount** : the price computation is based on a discount.

  * **Formula** : the price computation is based on a formula.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Each <b>Computation</b> option reveals its own computation-specific fields on the form.</p>
</div>

If **Fixed Price** is selected, enter the desired price in the **Fixed Price**
field below. If **Discount** is selected, enter the desired discount
percentage in the **Discount** field that appears.

If **Formula** is selected, a number of configurable options appear.

![The various formula computation options present in Konvergo ERP
Sales.](../../../../../_images/formula-computation-options.png)

To configure the **Formula** computation option, start by selecting an option
from the **Based on** field: **Sales Price** , **Cost** , or **Other
Pricelist**. This determines what the advanced price rule formula will be
based on.

Next, in the **Discount** field, determine how much of a discount should be
applied. It should be noted that a mark-up can be applied by setting a
negative discount in this field.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>To formulate a 100% markup (or 2 times the cost of the product), with a $5 minimum margin, set
the <b>Based on</b> field to <b>Cost</b>, the <b>Discount</b> to <code>-100</code>, and the
<b>Margins</b> to <code>5</code>. This is often seen in retail situations.</p>
<img alt="How it looks to formulate a markup cost with 5 dollar minimum margin in Konvergo ERP Sales." class="align-center" src="../../../../../_images/formula-markup-cost-example.png"/>
</div>

Then, in the **Extra Fee** field, specify a fixed amount to add (or subtract)
to the amount calculated with the discount. After that, enter a desired figure
in the **Rounding Method** field. The rounding method sets the price so that
it is a multiple of the value in the field.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Rounding is applied <em>after</em> the discount and <em>before</em> the surcharge.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../../subscriptions">Subscriptions</a></p>
</div>0

Lastly, specify the minimum amount of margin over the base price in the
**Margins** field.

Once all formula-related configurations are complete, Konvergo ERP provides an example
of the formula in a blue block to the right of the configurations.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../../subscriptions">Subscriptions</a></p>
</div>1

### Conditions

At the bottom of the **Create Pricelist Rules** pop-up form is the
**Conditions** section.

Here, start by selecting one of the options in the **Apply On** field:

  * **All Products** : the advanced pricelist rule will be applied to all products.

  * **Product Category** : the advanced pricelist rule will be applied to a specific category of products.

  * **Product** : the advanced pricelist rule will be applied to a specific product.

  * **Product Variant** : the advanced pricelist rule will be applied to a specific product variant.

If any of those options, apart from **All Products** , are selected, a new
option-specific field appears, in which the specific **Product Category** ,
**Product** , or **Product Variant** must be chosen.

Then, select a minimum quantity to be applied to the advanced pricelist rule
in the **Min. Quantity** field. Lastly, select a range of dates for the
pricelist item validation in the **Validity** field.

Once all configurations are complete, either click **Save & Close** to save
the advanced pricelist rule, or click **Save & New** to immediately create
another advanced pricelist rule on a fresh form.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../../subscriptions">Subscriptions</a></p>
</div>2 <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../../subscriptions">Subscriptions</a></p>
</div>3

