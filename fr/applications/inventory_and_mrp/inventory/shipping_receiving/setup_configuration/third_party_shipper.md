# Third-party shipping carriers

Users can link third-party shipping carriers to Konvergo ERP databases, in order to
verify carriers” delivery to specific addresses, [automatically calculate
shipping costs](delivery_method), and [generate shipping
labels](labels).

In Konvergo ERP, shipping carriers can be applied to a sales order (SO), invoice, or
delivery order. For tips on resolving common issues when configuring shipping
connectors, skip to the Troubleshooting section.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="dhl_credentials">Comment obtenir des identifiants DHL pour l’intégration avec Konvergo ERP ?</a></p></li>
<li><p><a href="sendcloud_shipping">Sendcloud configuration</a></p></li>
<li><p><a href="ups_credentials">Comment obtenir des identifiants UPS pour l’intégration avec Konvergo ERP ?</a></p></li>
</ul>
</div>

The following is a list of available shipping connectors in Konvergo ERP:

Transporteur | Region availability  
---|---  
FedEx | Tous  
[DHL](dhl_credentials) | Tous  
[UPS](ups_credentials) | Tous  
US Postal Service | États-Unis d’Amérique  
[Sendcloud](sendcloud_shipping) | EU  
Bpost | Belgique  
Easypost | Amérique du Nord  
Shiprocket | Inde  
  
## Configuration

To ensure proper setup of a third-party shipping carrier with Konvergo ERP, follow
these steps:

  1. Install the shipping connector.

  2. Set up delivery method.

  3. Activate production environment.

  4. Configure warehouse.

  5. Specify weight of products.

### Install shipping connector

To install shipping connectors, go to Inventory app ‣ Configuration ‣
Settings.

Under the **Shipping Connectors** section, tick the third-party shipping
carrier’s checkbox to install it. Multiple third-party shipping connectors can
be selected at once. Then, click **Save**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><a href="delivery_method">Delivery methods</a> can also be integrated with operations in the <em>Sales</em>,
<em>eCommerce</em>, and <em>Website</em> apps. To install, refer to the <a href="../../../../general/apps_modules#general-install"><span class="std std-ref">install apps and modules</span></a> documentation.</p>
</div> ![Options of available shipping connectors in
Konvergo ERP.](../../../../../_images/shipping-connectors.png)

### Delivery method

To configure the API credentials, and activate the shipping carrier, begin by
going to Inventory app ‣ Configuration ‣ Shipping Methods, and select the
desired delivery method.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The list often includes <b>two</b> delivery methods from the same <b>Provider</b>: one for
international shipping and one for domestic shipping.</p>
<p>Additional delivery methods can be created for specific purposes, such as <a href="../../product_management/product_tracking/packaging">packaging</a>.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="delivery_method">Configure delivery methods</a></p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Ensure the delivery method is published when it should be available on the <em>Website</em> app. To
publish a delivery method on the website, click the desired delivery method, then click the
<b>Unpublished</b> smart button. Doing so changes that smart button to read:
<b>Published</b>.</p>
</div>

The **Shipping Method** page contains details about the provider, including:

  * **Shipping Method** (_Required field_): the name of the delivery method (e.g. `FedEx US`, `FedEx EU`, etc.).

  * **Website** : configure shipping methods for an _eCommerce_ page that is connected to a specific website in the database. Select the applicable website from the drop-down menu, or leave it blank to apply the method to all web pages.

  * **Provider** (_Required field_): choose the third-party delivery service, like FedEx. Upon choosing a provider, the **Integration Level** , **Invoicing Policy** and **Insurance Percentage** fields become available.

  * **Integration Level** : choose **Get Rate** to simply get an estimated shipment cost on an SO or invoice.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Select <b>Get Rate and Create Shipment</b> to also <a href="labels">generate shipping labels</a>.</p>
</div>

  * **Company** : if the shipping method should apply to a specific company, select it from the drop-down menu. Leave the field blank to apply the method to all companies.

  * **Delivery Product** (_Required field_): the delivery charge name that is added to the SO or invoice.

  * **Invoicing Policy** : select and calculate an **Estimated cost** of shipping directly from the shipping carrier. If the **Real cost** of shipping is wanted instead, refer to this [doc about invoicing real shipping costs](../advanced_operations_shipping/invoicing).

  * **Margin on Rate** : specify an additional percentage amount added to the base shipping rate to cover extra costs, such as handling fees, packaging materials, exchange rates, etc.

  * **Free if order amount is above** : enables free shipping for orders surpassing a specified amount entered in the corresponding **Amount** field.

  * **Insurance Percentage** : specify a percentage amount of the shipping costs reimbursed to the senders if the package is lost or stolen in transit.

![Screenshot of a FedEx shipping method.](../../../../../_images/fedex.png)

**Shipping Method** configuration page for `FedEx US`.

In the **Configuration** tab, fill out the API credential fields (e.g. API
key, password, account number, etc.). Depending on the third-party shipping
carrier chosen in the **Provider** field, the **Configuration** tab will
contain different required fields. For more details about configuring specific
carriers” credentials, refer to the following documents:

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="dhl_credentials">DHL credentials</a></p></li>
<li><p><a href="sendcloud_shipping">Sendcloud credentials</a></p></li>
<li><p><a href="ups_credentials">UPS credentials</a></p></li>
</ul>
</div>

### Production environment

With the delivery method details configured, click the **Test Environment**
smart button to set it to **Production Environment**.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Setting the delivery method to <b>Production</b> creates <b>real</b> shipping labels, and users
are at risk of being charged through their carrier account (e.g. UPS, FedEx, etc.) <b>before</b>
users charge customers for shipping. Verify all configurations are correct before launching the
delivery method to <b>Production</b>.</p>
</div> ![Show the "Test Environment" smart
button.](../../../../../_images/production.png)

### Configuration de l’entrepôt

Ensure the warehouse’s **Address** (including ZIP code) and **Phone** number
are entered accurately. To do that, go to Inventory app ‣ Configuration ‣
Warehouses, and select the desired warehouse.

On the warehouse configuration page, open the warehouse contact page by
clicking the **Company** field.

![Highlight the "Company" field.](../../../../../_images/internal-link.png)

Verify that the **Address** and **Phone** number are correct, as they are
required for the shipping connector to work properly.

![Show company address and phone number.](../../../../../_images/company.png)

### Product weight

For the carrier integration to work properly, specify the weight of products
by going to Inventory app ‣ Products ‣ Products, and selecting the desired
product.

Then, switch to the **Inventory** tab, and define the **Weight** of the
product in the **Logistics** section.

![Display the "Weight" field in the Inventory tab of the product
form.](../../../../../_images/product-weight.png)

## Apply third-party shipping carrier

Shipping carriers can be applied on a SO, invoice, or delivery order.

After configuring the third-party carrier’s delivery method in Konvergo ERP, create or
navigate to a quotation by going to Sales app ‣ Orders ‣ Quotations.

### Sales order

To assign a third-party shipping carrier, and get an estimated cost of
shipping, begin by going to Sales app ‣ Orders ‣ Quotations. Create or select
an existing quotation, and add the cost of shipping through a third-party
carrier to a quotation, by clicking the **Add Shipping** button in the bottom-
right corner of the **Order Lines** tab.

![Show the "Add shipping" button at the bottom of a
quotation.](../../../../../_images/add-shipping1.png)

In the resulting **Add a shipping method** pop-up window, select the intended
carrier from the **Shipping Method** drop-down menu. The **Cost** field is
automatically filled based on:

  * the amount specified in the **Total Order Weight** field (if it is not provided, the sum of product weights in the order is used)

  * the distance between the warehouse’s source address and the customer’s address.

After selecting a third-party provider in the **Shipping Method** field, click
**Get Rate** in the **Add a shipping method** pop-up window to get the
estimated cost through the shipping connector. Then, click the **Add** button
to add the delivery charge to the SO or invoice.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../advanced_operations_shipping/invoicing">Charge customers for shipping after product delivery</a></p>
</div>

### Delivery order

For users making shipments without installing the _Sales_ app, assign the
shipping carrier to the delivery order, by first going to the Inventory app.
Then, from the **Inventory Overview** dashboard, select the **Delivery
Orders** operation type, and choose the desired delivery order that is not
already marked as **Done** or **Cancelled**.

In the **Additional info** tab, set the **Carrier** field to the desired
third-party shipping carrier. When the delivery method is set to production
mode, a **Tracking Reference** is provided.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="labels">Generate shipping labels</a></p>
</div> ![Show the delivery order's "Additional info"
tab.](../../../../../_images/delivery-info.png)

## Aide au dépannage

Since shipping connectors can sometimes be complex to set up, here are some
checks to try when things are not working as expected:

  1. Ensure the warehouse information (e.g., address and phone number) in Konvergo ERP is correct **and** matches the records saved in the shipping provider’s website.

  2. Verify that the [package type](../../product_management/product_tracking/package#inventory-warehouses-storage-package-type) and parameters are valid for the shipping carrier. To check, ensure the shipment can be directly created on the shipping carrier’s website.

  3. When encountering a price mismatch between Konvergo ERP’s estimated cost and the provider’s charge, first ensure the delivery method is set to production environment.

Then, create the shipment in both the carrier’s website and Konvergo ERP, and verify
the prices are the same across Konvergo ERP, the shipping provider, and in the _debug
logs_.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><a href="delivery_method">Delivery methods</a> can also be integrated with operations in the <em>Sales</em>,
<em>eCommerce</em>, and <em>Website</em> apps. To install, refer to the <a href="../../../../general/apps_modules#general-install"><span class="std std-ref">install apps and modules</span></a> documentation.</p>
</div>0

### Debug log

Track shipping data inconsistencies by activating debug logging. To do that,
go to the delivery method’s configuration page (Inventory app ‣ Configuration
‣ Shipping Method), and select the desired shipping method. Click the **No
Debugging** smart button to activate **Debug Requests**.

![Show the "No Debug" smart button.](../../../../../_images/no-debug.png)

With **Debug Requests** activated, each time the shipping connector is used to
estimate the cost of shipping, records are saved in the **Logging** report. To
access the report, turn on [developer
mode](../../../../general/developer_mode#developer-mode), and go to
Settings app ‣ Technical ‣ Database Structure section ‣ Logging.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><a href="delivery_method">Delivery methods</a> can also be integrated with operations in the <em>Sales</em>,
<em>eCommerce</em>, and <em>Website</em> apps. To install, refer to the <a href="../../../../general/apps_modules#general-install"><span class="std std-ref">install apps and modules</span></a> documentation.</p>
</div>1 ![Show how to find the "Logging" option from the
"Technical" menu.](../../../../../_images/log.png)

Click the _HTTP request_ line item to open a detailed page, and verify the
correct information is sent from Konvergo ERP to the shipping carrier. In the _HTTP
response_ , verify that the same information is received.

![Show debug request history in Settings > Technical >
Logging.](../../../../../_images/logging1.png)

  *[SO]: Sales Order

