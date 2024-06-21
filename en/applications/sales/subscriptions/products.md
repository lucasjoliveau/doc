# Subscription products

By closely integrating with the Konvergo ERP _Sales_ app, the _Subscriptions_ app
enables users to sell subscription products alongside regular sales products.
While regular products are sold on a one-time basis, subscription products are
sold on a renewing basis, generating recurring revenue.

In Konvergo ERP, subscription products are also called _recurring_ products.

## Configure recurrence periods

To get started with subscriptions, the _recurrence periods_ must be properly
configured, as needed.

Recurrence periods are the time periods in which subscriptions renew. They
designate how often the customer pays for (and receives) subscription
products.

To configure recurrence periods, go to Subscriptions app ‣ Configuration ‣
Recurrence periods.

![The recurrence periods page in Konvergo ERP Subscriptions
application.](../../../_images/recurrence-periods-page.png)

The _Subscriptions_ app comes with some basic recurrence periods already
configured:

  * **Monthly**

  * **Quarterly**

  * **Weekly**

  * **2 Weeks**

  * **Yearly**

  * **3 Years**

  * **5 Years**

New recurrence periods can be added and/or edited at any time.

To create a new recurrence period, click **New** on the **Recurrence Periods**
page. Doing so reveals a blank recurrence period form.

![A recurrence period form in Konvergo ERP Subscriptions
application.](../../../_images/recurrence-period-form.png)

Then, type in the **Name** and **Duration** of the recurrence period, and
select the **Unit** that defines the duration.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>The unit <b>Days</b> <em>cannot</em> be used as a recurrence period on subscriptions. The daily
recurrence is meant for rentals, and <b>cannot</b> be added on recurring subscription sales orders.</p>
<p>This limitation is there to avoid sales orders that would generate daily invoices.</p>
</div>

## Product form configuration

To create a new subscription product, navigate to Subscriptions app ‣ Products
‣ Products, and click **New**.

Doing so reveals a blank product form, which can be configured and customized
in a number of ways.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>By default, the <b>Recurring</b> option is already enabled, prompting Konvergo ERP to recognize it
as a subscription product. Be sure to leave the <b>Recurring</b> and <b>Can be Sold</b>
options enabled.</p>
<p>The <b>Product Type</b> field is set to <b>Service</b> by default, as well. However,
subscription products <em>can</em> be set to other types, if needed.</p>
</div> ![A basic subscription product form in Konvergo ERP Subscriptions
application.](../../../_images/subscription-product-form.png)

### Time-based pricing

Once the desired fields in the **General Information** tab have been entered,
click the **Time-based pricing** tab on the product form.

![The time-based pricing tab on a subscription product form in Konvergo ERP
Subscriptions.](../../../_images/time-based-pricing-tab.png)

From here, click **Add a price** to begin defining recurring prices.

In the **Period** column, select a desired recurrence period. In the
**Pricelist** column, select a pricelist, if needed. Then, in the **Price**
column, enter the price for that recurrence period.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Daily</b> and <b>Hourly</b> periods <b>cannot</b> be used on recurring products.</p>
<img alt="The validation error pop-up window that appears in Konvergo ERP Subscriptions." class="align-center" src="../../../_images/validation-error-popup.png"/>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>There is <em>no limit</em> to how many lines can be added to the <b>Time-based pricing</b> table.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>An existing product can be made into a subscription product, simply by marking it as
<b>Recurring</b>, and configuring <b>Time-based pricing</b> on the product form.</p>
</div>

#### Pricelists

[Pricelists](../sales/products_prices/prices/pricing) can be used with
subscription products to give special pricing to customers included in
pricelists.

This can be configured either in the **Time-based pricing** tab of the product
form, or on the pricelist form in the _Sales_ application.

To create recurring price rules for specific pricelists in the **Time-based
pricing** tab of the product form, select a pricelist in the **Pricelist**
column.

![Pricelists in the "Time-based pricing" tab of the product
form.](../../../_images/pricelist-time-based-pricing.png)

When pricelists are added to the **Time-based pricing** tab, the pricelist
form in the _Sales_ app is automatically updated.

Time-based pricing rules can also be configured directly on the pricelist
form.

To do this, go to Sales app ‣ Products ‣ Pricelists, and select a pricelist
(or click **New** to create a new pricelist).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Pricelists are also accessible through the Konvergo ERP <em>Subscriptions</em> app by following the same menu
steps.</p>
</div>

Then, on the pricelist form, under the **Time-based rules** tab, click **Add a
line**.

![The time-based rules tab on a pricelist form in Konvergo ERP
Sales.](../../../_images/pricelist-form-time-based-rules-tab.png)

Then, select a subscription product in the **Products** column, and select a
recurrence period in the **Period** column. Lastly, enter a **Price** for that
particular product and period. Add as many lines as needed.

When **Time-based rules** are added to the pricelist form, the **Time-based
pricing** tab of the product form is automatically updated.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="ecommerce">Use subscriptions in the eCommerce shop</a></p>
</div>

