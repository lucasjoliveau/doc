# Sendcloud configuration

Sendcloud is a shipping service aggregator that facilitates the integration of
European shipping carriers with Konvergo ERP. Once integrated, users can select
shipping carriers on inventory operations in their Konvergo ERP database.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="https://support.sendcloud.com/hc/en-us/articles/360059470491-Konvergo ERP-integration">Sendcloud integration documentation</a></p>
</div>

## Setup in Sendcloud

### Create an account and activate carriers

To get started, go to [Sendcloud’s platform](https://www.sendcloud.com) to
configure the account and generate the connector credentials. Log in with the
Sendcloud account, or create a new one if needed.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>For new account creation, Sendcloud will ask for a <abbr title="Value-Added Tax Identification">VAT</abbr>
number or <abbr title="Economic Operators' Registration and Identification">EORI</abbr> number. After
completing the account setup, activate (or deactivate) the shipping carriers that will be used
in the Konvergo ERP database.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Konvergo ERP integration of Sendcloud works on free Sendcloud plans <em>only</em> if a bank account is linked,
since Sendcloud won’t ship for free. To use shipping rules, or individual custom carrier
contacts, a paid plan of Sendcloud is <b>required</b>.</p>
</div>

### Warehouse configuration

Once logged into the Sendcloud account, navigate to Settings ‣ Shipping ‣
Addresses, and fill in the field for **Warehouse address**.

![Adding addresses in the Sendcloud
settings.](../../../../../_images/settings-shipping.png)

To allow Sendcloud to process returns as well, a **Return Address** is
required. Under the **Miscellaneous section** , there is a field called
**Address Name (optional)**. The Konvergo ERP warehouse name should be entered here,
and the characters should be exactly the same.

<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="line-block">
<div class="line"><b>SendClould configuration</b></div>
<div class="line"><b>Miscellaneous</b></div>
<div class="line"><b>Address Name (optional)</b>: <code>Warehouse #1</code></div>
<div class="line"><b>Brand</b>: <code>Default</code></div>
</div>
<div class="line-block">
<div class="line"><b>Konvergo ERP warehouse configuration</b></div>
<div class="line"><b>Warehouse</b>: <code>Warehouse #1</code></div>
<div class="line"><b>Short Name</b>: <code>WH</code></div>
<div class="line"><b>Company</b>: <code>My company (San Francisco)</code></div>
<div class="line"><b>Address</b>: <code>My Company (San Francisco)</code></div>
</div>
<p>Notice how the inputs for the <b>Warehouse</b> field, for both the Konvergo ERP configuration and
the Sendcloud configuration, are the exact same.</p>
</div>

### Generate Sendcloud credentials

In the Sendcloud account, navigate to Settings ‣ Integrations in the menu on
the right. Next, search for **Konvergo ERP Native**. Then, click on **Connect**.

After clicking on **Connect** , the page redirects to the **Sendcloud API**
settings page, where the **Public and Secret Keys** are produced. The next
step is to name the **Integration**. The naming convention is as follows:
`Konvergo ERP CompanyName`, with the user’s company name replacing `CompanyName` (e.g.
`Konvergo ERP StealthyWood`).

Then, check the box next to **Service Points** and select the shipping
services for this integration. After saving, the **Public and Secret Keys**
are generated.

![Configuring the Sendcloud integration and receiving the
credentials.](../../../../../_images/public-secret-keys.png)

## Setup in Konvergo ERP

To ensure seamless Sendcloud integration with Konvergo ERP, install and link the
Sendcloud shipping connector to the Sendcloud account. Then, configure Konvergo ERP
fields, so Sendcloud can accurately pull shipping data to generate labels.

### Install Sendcloud shipping module

After the Sendcloud account is set up and configured, it’s time to configure
the Konvergo ERP database. To get started, go to Konvergo ERP’s **Apps** module, search for
the `Sendcloud Shipping` integration, and install it.

![Sendcloud Shipping module in the Konvergo ERP Apps
module.](../../../../../_images/sendcloud-mod.png)

### Sendcloud shipping connector configuration

Once installed, activate the **Sendcloud Shipping** module in Inventory ‣
Configuration ‣ Settings. The **Sendcloud Connector** setting is found under
the **Shipping Connectors** section.

After activating the **Sendcloud Connector** , click on the **Sendcloud
Shipping Methods** link below the listed connector. Once on the **Shipping
Methods** page, click **Create**.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p><b>Shipping Methods</b> can also be accessed by going to Inventory ‣
Configuration ‣ Delivery ‣ Shipping Methods.</p>
</div>

Fill out the following fields in the **New Shipping Method** form:

  * **Shipping Method** : type `Sendcloud DPD`.

  * **Provider** : select **Sendcloud** from the drop-down menu.

  * **Delivery Product** : set the product that was configured for this shipping method or create a new product.

  * In the **SendCloud Configuration** tab, enter the **Sendcloud Public Key**.

  * In the **SendCloud Configuration** tab, enter the **Sendcloud Secret Key**.

  * Manually **Save** the form by clicking the cloud icon next to the **Shipping Methods / New** breadcrumbs.

After configuring and saving the form, follow these steps to load the shipping
products:

  * In the **SendCloud Configuration** tab of the **New Shipping Method** form, click on the **Load your SendCloud shipping products** link.

  * Select the shipping products the company would like to use for deliveries and returns.

  * Click **Select**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Sample Sendcloud shipping products configured in Konvergo ERP:</p>
<div class="line-block">
<div class="line"><b>DELIVERY</b></div>
<div class="line"><b>Shipping Product</b>: <code>DPD Home 0-31.5kg</code></div>
<div class="line"><b>Carrier</b>: <code>DPD</code></div>
<div class="line"><b>Minimum Weight</b>: <code>0.00</code></div>
<div class="line"><b>Maximum Weight</b>: <code>31.50</code></div>
</div>
<p><b>Countries</b>: <code>Austria</code> <code>Belgium</code> <code>Bosnia</code> <code>Herzegovina</code> <code>Bulgaria</code> <code>Croatia</code> <code>Czech</code>
<code>Republic</code> <code>Denmark</code> <code>Estonia</code> <code>Finland</code> <code>France</code> <code>Germany</code> <code>Greece</code> <code>Hungary</code> <code>Iceland</code>
<code>Ireland</code> <code>Italy</code> <code>Latvia</code> <code>Liechtenstein</code> <code>Lithuania</code> <code>Luxembourg</code> <code>Monaco</code> <code>Netherlands</code>
<code>Norway</code> <code>Poland</code> <code>Portugal</code> <code>Romania</code> <code>Serbia</code> <code>Slovakia</code> <code>Slovenia</code> <code>Spain</code> <code>Sweden</code>
<code>Switzerland</code></p>
<div class="line-block">
<div class="line"><b>RETURN</b></div>
<div class="line"><b>Return Shipping Product</b>: <code>DPD Return 0-20kg</code></div>
<div class="line"><b>Return Carrier</b>: <code>DPD</code></div>
<div class="line"><b>Return Minimum Weight</b>: <code>0.00</code></div>
<div class="line"><b>Return Maximum Weight</b>: <code>20.00</code></div>
<div class="line"><b>Return Countries</b>: <code>Belgium</code> <code>Netherlands</code></div>
</div>
</div> ![Example of shipping products configured in
Konvergo ERP.](../../../../../_images/sendcloud-example.png) <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Sendcloud does not provide test keys when a company tests the sending of a package in Konvergo ERP. This
means if a package is created, the configured Sendcloud account will be charged, unless the
associated package is canceled within 24 hours of creation.</p>
<p>Konvergo ERP has a built-in layer of protection against unwanted charges when using test environments.
Within a test environment, if a shipping method is used to create labels, then those labels are
immediately canceled after the creation — this occurs automatically. The test and production
environment settings can be toggled back and forth from their respective smart buttons.</p>
</div>

### Shipping information

To use Sendcloud to generate shipping labels, the following information
**must** be filled out accurately and completely in Konvergo ERP:

  1. **Customer information** : when creating a quotation, ensure the selected **Customer** has a valid phone number, email address, and shipping address.

To verify, select the **Customer** field to open their contact page. Here, add
their shipping address in the **Contact** field, along with their **Mobile**
number and **Email** address.

  2. **Product weight** : ensure all products in an order have a specified **Weight** in the **Inventory** tab of their product form. Refer to the [Product weight section](third_party_shipper#inventory-shipping-receiving-configure-weight) of this article for detailed instructions.

  3. **Warehouse address** : ensure the warehouse name and address in Konvergo ERP match the previously defined warehouse in the Sendcloud setup. For details on warehouse configuration in Konvergo ERP, refer to the [warehouse configuration section](third_party_shipper#inventory-shipping-receiving-configure-source-address) of the third-party shipping documentation.

## Generate labels with Sendcloud

When creating a quotation in Konvergo ERP, add shipping and a **Sendcloud shipping
product**. Then, **Validate** the delivery. Shipping label documents are
automatically generated in the chatter, which include the following:

  1. **Shipping label(s)** depending on the number of packages.

  2. **Return label(s)** if the Sendcloud connector is configured for returns.

  3. **Customs document(s)** should the destination country require them.

Additionally, the tracking number is now available.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>When return labels are created, Sendcloud will automatically charge the configured Sendcloud
account.</p>
</div>

## FAQ

### Shipment is too heavy

If the shipment is too heavy for the Sendcloud service that is configured,
then the weight is split to simulate multiple packages. Products will need to
be put in different **Packages** to **Validate** the transfer and generate
labels.

**Rules** can also be set up in Sendcloud to use other shipping methods when
the weight is too heavy. However, note that these rules will not apply to the
shipping price calculation on the calculation on the sales order.

### Personal carrier contract

Use custom prices from a direct carrier contract, via CSV upload, by first
logging into Sendcloud, navigating to Settings ‣ Carriers ‣ My contracts, and
then selecting the intended contract.

![Navigate to the contracts section in
Sendcloud.](../../../../../_images/contracts.png)

Under the **Contract prices** section, click **Download CSV** and fill out the
contract prices in the **price** column of the CSV file template.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>Ensure the CSV file includes the correct prices to avoid any inaccuracies.</p>
</div> ![Show sample contract CSV from Sendcloud, highlighting
the price column.](../../../../../_images/price-csv.png)

**Upload** the completed CSV file to Sendcloud, then click **Save these
prices**.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="https://support.sendcloud.com/hc/en-us/articles/5163547066004">Sendcloud: How to upload contract prices with carriers</a></p>
</div>

### Measuring volumetric weight

Many carriers have several measures for weight. There is the actual weight of
the products in the parcel, and there is the _volumetric weight_ (Volumetric
weight is the volume that a package occupies when in transit. In other words
it is the physical size of a package).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>For new account creation, Sendcloud will ask for a <abbr title="Value-Added Tax Identification">VAT</abbr>
number or <abbr title="Economic Operators' Registration and Identification">EORI</abbr> number. After
completing the account setup, activate (or deactivate) the shipping carriers that will be used
in the Konvergo ERP database.</p>
</div>0 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>For new account creation, Sendcloud will ask for a <abbr title="Value-Added Tax Identification">VAT</abbr>
number or <abbr title="Economic Operators' Registration and Identification">EORI</abbr> number. After
completing the account setup, activate (or deactivate) the shipping carriers that will be used
in the Konvergo ERP database.</p>
</div>1

### Unable to calculate shipping rate

First, verify that the product being shipped has a weight that is supported by
the selected shipping method. If this is set, then verify that the destination
country (from the customer address) is supported by the carrier. The country
of origin (warehouse address) should also be supported by the carrier.

