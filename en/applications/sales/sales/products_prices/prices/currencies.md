# Foreign currencies

With Konvergo ERP, pricelists can be used to manage prices in a number of foreign
currencies. Specifically, Konvergo ERP has the ability to work with 167 total
currencies.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>In order to use multiple currencies in Konvergo ERP <em>Sales</em>, the <em>Accounting</em> application <b>must</b> be
installed.</p>
</div>

## Settings

Once the _Accounting_ app has been installed, foreign currencies can be added
to the database. Navigate to Accounting app ‣ Configuration ‣ Settings, scroll
to the **Currencies** section, and locate the **Main Currency** setting.

![How the main currency feature appears on settings page in Konvergo ERP
Accounting.](../../../../../_images/main-currency-setting-page.png)

Konvergo ERP automatically sets the main currency as the currency of the country the
company is based in.

To change the main currency of the company, select the drop-down menu in the
**Currency** field, select the desired currency, and be sure to **Save** the
changes.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>To ensure currency rates are updated automatically, enable the <em>automatic currency rates</em> feature
on the <em>Accounting</em> settings page (Accounting app ‣ Configuration ‣ Settings
‣ Currencies section).</p>
<img alt="How the main currency feature appears on settings page in Konvergo ERP Accounting." class="align-center" src="../../../../../_images/automatic-currency-rates.png"/>
<p>Click the checkbox beside the <b>Automatic Currency Rates</b> feature, choose a designated
bank to get the currency rates from in the <b>Service</b> field drop-down menu, and select
an <b>Interval</b> of time for the updates to take place. Then determine when the date of
the <b>Next Run</b> should be.</p>
<p>To instantly update the currency rates, click the <b>🔁 (circular arrows)</b> icon, located
to the right of the <b>Next Run</b> field.</p>
<p>When all configurations are complete, be sure to <b>Save</b> all changes.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>All payment methods <b>must</b> be in the same currency as the sales journal, or the company
currency, if the company currency is not set. If it is not the same, a <b>Validation
Error</b> message appears.</p>
</div>

## View, edit, and add currencies

To view, edit, and add currencies to the database, making them available on
pricelists and on the **Main Currency** drop-down menu, click the
**Currencies** link, located beneath the **Currency** field on the Accounting
app ‣ Settings page.

When the **Currencies** link is clicked, a separate **Currencies** page is
revealed.

![How the main currencies page appears in Konvergo ERP
Accounting.](../../../../../_images/main-currencies-page.png)

On this page, Konvergo ERP provides a master list of 167 global currencies. Each row
shows the corresponding **Currency** , **Symbol** , **Name** , date of the
**Last Update** , and **Current Rate** (compared to the default currency of
the country in which the company is based).

To the far right, there are two columns, which can be toggled on or off:

  * **Use on eBay** : this currency can be used with the connected eBay account (if applicable).

  * **Active** : this currency is activated, which means it can be added to a pricelist, or used as the main currency of the company, if desired (via Accounting app ‣ Configuration ‣ Settings ‣ Currencies section).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>By default, all the <b>Active</b> currency options are at the top of the list.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>It is recommended that <em>at least</em> one pricelist is created per <b>Active</b> currency. See
<a href="pricing">Pricelists, discounts, and formulas</a> to learn more about pricelist configuration.</p>
</div>

To toggle options on/off, click the toggle switch in the row for the
corresponding column. When _on_ the color of the switch is green. When _off_ ,
the color of the switch is grey.

### Currency detail form

To edit any currency on the **Currencies** page, click the desired currency to
reveal the detail form for that specific currency, and proceed to make any
necessary changes.

![How a currency detail form looks in Konvergo ERP
Accounting.](../../../../../_images/currency-detail-form.png)

On the currency detail form, the relevant currency code appears in the
**Currency** field. Beneath that, the name for the currency is in the **Name**
field.

Then, toggle the currency’s availability with the **Active** toggle: _on_ is
indicated with a green switch, and _off_ is indicated with a grey switch.

On the right of the currency detail form, the appropriate **Currency Unit**
(e.g. `Dollars`) and **Currency Subunit** (e.g. `Cents`) can be found.

If the currency is meant to be used for eBay purposes, toggle the **Use on
eBay** option to the desired activation.

Next, under the **Rates** tab, the various conversion rates can be viewed,
added, or deleted. Each row shows the **Date** of that specific rate, the
**Company** to which it is connected, followed by the **Unit per…** and **…per
Unit**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The <em>…</em> in each of the last two columns represents the main currency set for the company. For
example, if the main currency is set to <code>USD</code>, the columns are titled <b>Unit per USD</b>
and <b>USD per Unit</b>.</p>
</div>

To add a new rate, click **Add a line** in the **Rates** tab, and proceed to
fill in the necessary information in the aforementioned columns.

### Main currency detail form

If the selected currency is the main currency of the company, a blue banner
appears at the top of the currency detail form with the message: **This is
your company’s currency.**.

![How a main currency detail form looks in Konvergo ERP
Accounting.](../../../../../_images/main-currency-detail-form.png)

All the fields are the same as a typical currency detail form, but there will
**not** be a **Rates** tab because all other currency rates are based off the
main currency of the company.

## Create new currency

If a desired currency isn’t on the **Currencies** page, click the **New**
button to open a blank currency template form.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>The same <b>New</b> button is located in the upper-right corner of any currency detail form.</p>
</div> ![How a blank currency detail form looks in Konvergo ERP
Accounting.](../../../../../_images/blank-currency-detail-form.png)

On the blank currency detail form, proceed to enter the desired currency code
in the **Currency** field. Beneath that, enter the name for the currency in
the **Name** field.

Then, toggle the currency’s availability with the **Active** toggle switch.

On the right of the currency detail form, enter the appropriate **Currency
Unit** (e.g. `Dollars`) and appropriate **Currency Subunit** (e.g. `Cents`).

If the currency is meant to be used for eBay purposes, toggle the **Use on
eBay** to the desired activation.

Next, under the **Rates** tab, add a new rate by clicking **Add a line**.
Then, proceed to confirm and adjust the **Date** , **Company** , **Unit per…**
, and **…per Unit** fields to ensure all the auto-populated information is
accurate.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The <em>…</em> in each of the last two columns represents the main currency set for the company. For
example, if the main currency is set to <code>USD</code>, the columns are titled <b>Unit per USD</b>
and <b>USD per Unit</b>.</p>
</div>

## Currency-specific pricelists

It is recommended that _at least_ one pricelist is created per active currency
in the database. To create (or assign) a pricelist to a specific currency,
start by navigating to Sales app ‣ Products ‣ Pricelists.

From the **Pricelists** page, either select an existing pricelist to edit, or
click **New** to create a new pricelist.

On the pricelist detail form, for either a new or existing pricelist, adjust
the **Currency** field as desired.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="pricing">Pricelists, discounts, and formulas</a> to learn more about pricelist configuration.</p>
</div>

## Auto-conversion from public price

It should be noted that the public price seen on products is directly related
to the main currency the company has set, which is configured by navigating to
Accounting app ‣ Configuration ‣ Settings ‣ Currencies section ‣ Main Currency
‣ Currency drop-down menu.

The sales price automatically updates if the pricelist is changed to a
different pricelist that has a different currency than the company’s main
currency. The change in price is directly related to the updated conversion
rate for that currency.

## Set product prices

In order to have product prices set in place to avoid any changes in currency
rates, start by navigating to Sales app ‣ Products ‣ Products.

From the **Products** page, select the desired product to modify. Or, create a
new product by clicking the **New** button.

Then, on the product detail form, click the **Extra Prices** smart button,
located in the upper-left corner. Doing so reveals a separate **Price Rules**
page, specific to that particular product.

![How to set product prices based on foreign currency pricelists in Konvergo ERP
Sales.](../../../../../_images/price-rules-currencies.png)

Click **New** , and select the desired pricelist from the drop-down menu in
the **Pricelist** column.

The **Applied On** field is auto-populated with the product, so proceed to
enter in the desired figures in the **Min. Quantity** and **Price** fields.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The figure in the <b>Min. Quantity</b> field means the <b>Price</b> being set will
<b>only</b> trigger if at least that amount of product is purchased.</p>
</div>

If necessary, configure a **Start Date** and **End Date** for the set prices.
Leaving those columns blank ensures the set price will remain valid,
regardless of the date of sale.

If working in a multi-company environment, designate to which company this
price rule should be applied in the **Company** field. Leaving that field
blank ensures the price rule applies to all companies in the database.

With those configurations complete, regardless of any changes/updates in
conversion, whenever those designated pricelists are applied to a customer
trying to purchase this specific product, these pre-determined set prices
appear.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>To ensure currency rates are updated automatically, enable the <em>automatic currency rates</em> feature
on the <em>Accounting</em> settings page (Accounting app ‣ Configuration ‣ Settings
‣ Currencies section).</p>
<img alt="How the main currency feature appears on settings page in Konvergo ERP Accounting." class="align-center" src="../../../../../_images/automatic-currency-rates.png"/>
<p>Click the checkbox beside the <b>Automatic Currency Rates</b> feature, choose a designated
bank to get the currency rates from in the <b>Service</b> field drop-down menu, and select
an <b>Interval</b> of time for the updates to take place. Then determine when the date of
the <b>Next Run</b> should be.</p>
<p>To instantly update the currency rates, click the <b>🔁 (circular arrows)</b> icon, located
to the right of the <b>Next Run</b> field.</p>
<p>When all configurations are complete, be sure to <b>Save</b> all changes.</p>
</div>0

