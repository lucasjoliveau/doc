# AvaTax integration

Avalara’s _AvaTax_ is a cloud-based tax software. Integrating _AvaTax_ with
Konvergo ERP provides real-time and region-specific tax calculations when users sell,
purchase, and invoice items in Konvergo ERP. _AvaTax_ tax calculation is supported
with every United Nations charted country, including inter-border
transactions.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p><em>AvaTax</em> is only available for integration with databases/companies that have locations in the
United States and Canada. This means the fiscal position/country of a database can only be set to
the United States or Canada. For more information, reference this documentation:
<a href="#avatax-fiscal-country"><span class="std std-ref">Fiscal country</span></a>.</p>
</div>

_AvaTax_ accounts for location-based tax rates for each state, county, and
city. It improves remittance accuracy by paying close attention to laws,
rules, jurisdiction boundaries, and special circumstances (like, tax holidays,
and product exemptions). Companies who integrate with _AvaTax_ can maintain
control of tax-calculations in-house with this simple API integration.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Some limitations exist in Konvergo ERP while using <em>AvaTax</em> for tax calculation:</p>
<ul>
<li><p><em>AvaTax</em> is <b>not</b> supported in Konvergo ERP’s <em>Point of Sale</em> app, because a dynamic tax calculation
model is excessive for transactions within a single delivery address, such as stores or
restaurants.</p></li>
<li><p><em>AvaTax</em> and Konvergo ERP use the company address and <b>not</b> the warehouse address.</p></li>
<li><p>Exercise tax is <b>not</b> supported. This includes tobacco/vape taxes, fuel taxes, and other
specific industries.</p></li>
</ul>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p>Avalara’s support documents: <a href="https://community.avalara.com/support/s/document-item?language=en_US&amp;bundleId=dqa1657870670369_dqa1657870670369&amp;topicId=About_AvaTax&amp;_LANG=enus">About AvaTax</a></p>
</div>

## Set up on AvaTax

To use _AvaTax_ , an account with Avalara is required for the setup. If one
has not been set up yet, connect with Avalara to purchase a license: [Avalara:
Let’s Talk](https://www.avalara.com/us/en/get-started).

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Upon account setup, take note of the <em>AvaTax</em> <b>Account ID</b>. This will be needed in the
<a href="#avatax-credentials"><span class="std std-ref">Konvergo ERP setup</span></a>. In Konvergo ERP, this number is the <b>API ID</b>.</p>
</div>

Then, [create a basic company
profile](https://community.avalara.com/support/s/document-
item?bundleId=dqa1657870670369_dqa1657870670369&topicId=Create_a_Basic_company_profile&_LANG=enus).

### Create basic company profile

Collect essential business details for the next step: locations where tax is
collected, products/services sold (and their sales locations), and customer
tax exemptions, if applicable. Follow the Avalara documentation for creating a
basic company profile:

  1. [Add company information](https://community.avalara.com/support/s/document-item?bundleId=dqa1657870670369_dqa1657870670369&topicId=Add_your_company_information&_LANG=enus).

  2. [Tell us where the company collects and pays tax](https://community.avalara.com/support/s/document-item?bundleId=dqa1657870670369_dqa1657870670369&topicId=Tell_us_where_you_collect_and_pay_tax&_LANG=enus).

  3. [Verify jurisdictions and activate the company](https://community.avalara.com/support/s/document-item?bundleId=dqa1657870670369_dqa1657870670369&topicId=Verify_your_jurisdictions_and_activate_your_company&_LANG=enus).

  4. [Add other company locations for location-based filing](https://community.avalara.com/support/s/document-item?bundleId=dqa1657870670369_dqa1657870670369&topicId=Add_other_company_locations_for_location-based_filing&_LANG=enus).

  5. [Add a marketplace to the company profile](https://community.avalara.com/support/s/document-item?bundleId=dqa1657870670369_dqa1657870670369&topicId=Add_marketplace_transactions_to_your_company_profile&_LANG=enus).

### Connect to AvaTax

After creating the basic company profile in Avalara, connect to _AvaTax_. This
step links Konvergo ERP and _AvaTax_ bidirectionally.

Navigate to either Avalara’s [sandbox](https://sandbox.admin.avalara.com/) or
[production](https://admin.avalara.com/) environment. This will depend on
which type of Avalara account the company would like to integrate.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="https://knowledge.avalara.com/bundle/fzc1692293626742/page/sandbox-vs-production">Sandbox vs production environments in Avalara</a>.</p>
</div>

Log in to create the **License Key**. Go to Settings ‣ License and API Keys.
Click **Generate License Key**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>A warning appears stating: <code>If your business app is connected to Avalara solutions, the
connection will be broken until you update the app with the new license key. This action cannot
be undone.</code></p>
<p>Generating a new license key breaks the connection with existing business apps using the <em>AvaTax</em>
integration. Make sure to update these apps with the new license key.</p>
</div>

If this will be the first API integration being made with _AvaTax_ and Konvergo ERP,
then click **Generate license key**.

If this is an additional license key, ensure the previous connection can be
broken. There is **only** one license key associated with each of the Avalara
sandbox and production accounts.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Copy this key to a safe place. It is <b>strongly encouraged</b> to backup the license key for future
reference. This key cannot be retrieved after leaving this screen.</p>
</div>

## Konvergo ERP configuration

Before using _AvaTax_ , there are some additional configurations in Konvergo ERP to
ensure tax calculations are made accurately.

Verify that the Konvergo ERP database contains necessary data. The country initially
set up in the database determines the fiscal position, and aids _AvaTax_ in
calculating accurate tax rates.

### Fiscal country

To set the **Fiscal Country** , navigate to Accounting app ‣ Configuration ‣
Settings.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../fiscal_localizations">Fiscal localizations</a></p>
</div>

Under the **Taxes** section, set the **Fiscal Country** feature to **United
States** or **Canada**. Then, click **Save**.

### Company settings

All companies operating under the Konvergo ERP database should have a full and
complete address listed in the settings. Navigate to the Settings app, and
under the **Companies** section, ensure there is only one company operating
the Konvergo ERP database. Click **Update Info** to open a separate page to update
company details.

If there are multiple companies operating in the database, click **Manage
Companies** to load a list of companies to select from. Update company
information by clicking into the specific company.

Database administrators should ensure that the **Street…** , **Street2…** ,
**City** , **State** , **ZIP** , and **Country** are all updated for the
companies.

This ensures accurate tax calculations and smooth end-of-year accounting
operations.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../../../general/companies">Companies</a></p></li>
<li><p><a href="../get_started">Get started</a></p></li>
</ul>
</div>

### Module installation

Next, ensure that the Konvergo ERP _AvaTax_ module is installed. To do so, navigate to
the Apps application. In the **Search…** bar, type in `avatax`, and press
`Enter`. The following results populate:

Name | Technical name | Description  
---|---|---  
**Avatax** | `account_avatax` | Default _AvaTax_ module. This module adds the base _AvaTax_ features for tax calculation.  
**Avatax for SO** | `account_avatax_sale` | Includes the information needed for tax calculation on sales orders in Konvergo ERP.  
**Avatax for Subscriptions** | `account_avatax_sale_subscription` | This module includes the features required for tax calculation on subscriptions in Konvergo ERP.  
**Account Avatax - Ecommerce** | `website_sale_account_avatax` | Includes tax calculation features for the checkout process on Konvergo ERP eCommerce.  
**Account AvaTax - Ecommerce - Delivery** | `website_sale_delivery_avatax` | Includes tax calculation features for the delivery process on Konvergo ERP eCommerce.  
  
Click the **Install** button on the module labeled **Avatax** :
`account_avatax`. Doing so installs the following modules:

  * **Avatax** : `account_avatax`

  * **Avatax for SO** : `account_avatax_sale`

  * **Account Avatax - Ecommerce** : `website_sale_account_avatax`

Should _AvaTax_ be needed for Konvergo ERP _Subscriptions_ , or for delivery tax in
Konvergo ERP _eCommerce_ , then install those modules individually by clicking on
**Install**.

### Konvergo ERP AvaTax settings

To integrate the _AvaTax_ API with Konvergo ERP, go to Accounting app ‣ Configuration
‣ Settings section. The **AvaTax** fields in the **Taxes** section is where
the _AvaTax_ configurations are made and the credentials are entered in.

![Configure AvaTax settings](../../../../_images/avatax-configuration-
settings.png)

#### Prerequisites

First, select the **Environment** in which the company wishes to use _AvaTax_
in. It can either be **Sandbox** or **Production**.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p>For help determining which <em>AvaTax</em> environment to use (either <b>Production</b> or
<b>Sandbox</b>), visit: <a href="https://knowledge.avalara.com/bundle/fzc1692293626742/page/sandbox-vs-production">Sandbox vs Production environments</a>.</p>
</div>

#### Credentials

Now, the credentials can be entered in. The _AvaTax_ **Account ID** should be
entered in the **API ID** field, and the **License Key** should be entered in
the **API Key** field.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Some limitations exist in Konvergo ERP while using <em>AvaTax</em> for tax calculation:</p>
<ul>
<li><p><em>AvaTax</em> is <b>not</b> supported in Konvergo ERP’s <em>Point of Sale</em> app, because a dynamic tax calculation
model is excessive for transactions within a single delivery address, such as stores or
restaurants.</p></li>
<li><p><em>AvaTax</em> and Konvergo ERP use the company address and <b>not</b> the warehouse address.</p></li>
<li><p>Exercise tax is <b>not</b> supported. This includes tobacco/vape taxes, fuel taxes, and other
specific industries.</p></li>
</ul>
</div>0

For the **Company Code** field, enter the Avalara company code for the company
being configured. Avalara interprets this as `DEFAULT`, if it is not set. The
**Company Code** can be accessed in the Avalara management portal.

First, log into the _AvaTax_ portal
([sandbox](https://sandbox.admin.avalara.com/) or
[production](https://admin.avalara.com/)). Then, navigate to Settings ‣ Manage
Companies. The **Company Code** value is located in the row of the **Company**
in the **Company Code** column.

![AvaTax company code highlighted on the company details
page.](../../../../_images/company-code.png)

#### Transaction options

There are two transactional settings in the Konvergo ERP _AvaTax_ settings that can be
configured: **Use UPC** and **Commit Transactions**.

If the checkbox next to **Use UPC** is ticked, the transactions will use
Universal Product Codes (UPC), instead of custom defined codes in Avalara.
Consult a certified public accountant (CPA) for specific guidance.

Should the **Commit Transactions** checkbox be ticked, then, the transactions
in the Konvergo ERP database will be committed for reporting in _AvaTax_.

#### Address validation

The _Address Validation_ feature ensures that the most up-to-date address by
postal standards is set on a contact in Konvergo ERP. This is important to provide
accurate tax calculations for customers.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Some limitations exist in Konvergo ERP while using <em>AvaTax</em> for tax calculation:</p>
<ul>
<li><p><em>AvaTax</em> is <b>not</b> supported in Konvergo ERP’s <em>Point of Sale</em> app, because a dynamic tax calculation
model is excessive for transactions within a single delivery address, such as stores or
restaurants.</p></li>
<li><p><em>AvaTax</em> and Konvergo ERP use the company address and <b>not</b> the warehouse address.</p></li>
<li><p>Exercise tax is <b>not</b> supported. This includes tobacco/vape taxes, fuel taxes, and other
specific industries.</p></li>
</ul>
</div>1

Additionally, tick the checkbox next to the **Address validation** field.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Some limitations exist in Konvergo ERP while using <em>AvaTax</em> for tax calculation:</p>
<ul>
<li><p><em>AvaTax</em> is <b>not</b> supported in Konvergo ERP’s <em>Point of Sale</em> app, because a dynamic tax calculation
model is excessive for transactions within a single delivery address, such as stores or
restaurants.</p></li>
<li><p><em>AvaTax</em> and Konvergo ERP use the company address and <b>not</b> the warehouse address.</p></li>
<li><p>Exercise tax is <b>not</b> supported. This includes tobacco/vape taxes, fuel taxes, and other
specific industries.</p></li>
</ul>
</div>2

**Save** the settings to implement the configuration.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Some limitations exist in Konvergo ERP while using <em>AvaTax</em> for tax calculation:</p>
<ul>
<li><p><em>AvaTax</em> is <b>not</b> supported in Konvergo ERP’s <em>Point of Sale</em> app, because a dynamic tax calculation
model is excessive for transactions within a single delivery address, such as stores or
restaurants.</p></li>
<li><p><em>AvaTax</em> and Konvergo ERP use the company address and <b>not</b> the warehouse address.</p></li>
<li><p>Exercise tax is <b>not</b> supported. This includes tobacco/vape taxes, fuel taxes, and other
specific industries.</p></li>
</ul>
</div>3 <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Some limitations exist in Konvergo ERP while using <em>AvaTax</em> for tax calculation:</p>
<ul>
<li><p><em>AvaTax</em> is <b>not</b> supported in Konvergo ERP’s <em>Point of Sale</em> app, because a dynamic tax calculation
model is excessive for transactions within a single delivery address, such as stores or
restaurants.</p></li>
<li><p><em>AvaTax</em> and Konvergo ERP use the company address and <b>not</b> the warehouse address.</p></li>
<li><p>Exercise tax is <b>not</b> supported. This includes tobacco/vape taxes, fuel taxes, and other
specific industries.</p></li>
</ul>
</div>4

#### Test connection

After entering all the above information into the _AvaTax_ setup on Konvergo ERP,
click **Test connection**. This ensures the **API ID** and **API KEY** are
correct, and a connection is made between Konvergo ERP and the _AvaTax_ application
programming interface (API).

#### Sync parameters

Upon finishing the configuration and settings of the _AvaTax_ section, click
the **Sync Parameters** button. This action synchronizes the exemption codes
from _AvaTax_.

### Fiscal position

Next, navigate to Accounting app ‣ Configuration ‣ Accounting: Fiscal
Positions. A **Fiscal Position** is listed named, **Automatic Tax Mapping
(AvaTax)**. Click it to open _AvaTax’s_ fiscal position configuration page.

Here, ensure that the **Use AvaTax API** checkbox is ticked.

Optionally, tick the checkbox next to the field labeled: **Detect
Automatically**. Should this option be ticked, then, Konvergo ERP will automatically
apply this **Fiscal Position** for transactions in Konvergo ERP.

Enabling **Detect Automatically** also makes specific parameters, such as
**VAT required** , **Foreign Tax ID** , **Country Group** , **Country** ,
**Federal States** , or **Zip Range** appear. Filling these parameters filters
the **Fiscal Position** usage. Leaving them blank ensures all calculations are
made using this **Fiscal Position**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Some limitations exist in Konvergo ERP while using <em>AvaTax</em> for tax calculation:</p>
<ul>
<li><p><em>AvaTax</em> is <b>not</b> supported in Konvergo ERP’s <em>Point of Sale</em> app, because a dynamic tax calculation
model is excessive for transactions within a single delivery address, such as stores or
restaurants.</p></li>
<li><p><em>AvaTax</em> and Konvergo ERP use the company address and <b>not</b> the warehouse address.</p></li>
<li><p>Exercise tax is <b>not</b> supported. This includes tobacco/vape taxes, fuel taxes, and other
specific industries.</p></li>
</ul>
</div>5 <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Some limitations exist in Konvergo ERP while using <em>AvaTax</em> for tax calculation:</p>
<ul>
<li><p><em>AvaTax</em> is <b>not</b> supported in Konvergo ERP’s <em>Point of Sale</em> app, because a dynamic tax calculation
model is excessive for transactions within a single delivery address, such as stores or
restaurants.</p></li>
<li><p><em>AvaTax</em> and Konvergo ERP use the company address and <b>not</b> the warehouse address.</p></li>
<li><p>Exercise tax is <b>not</b> supported. This includes tobacco/vape taxes, fuel taxes, and other
specific industries.</p></li>
</ul>
</div>6

#### AvaTax accounts

Upon selecting the checkbox option for **Use AvaTax API** a new **AvaTax** tab
appears. Click into this tab to reveal two different settings.

The first setting is the **AvaTax Invoice Account** , while the second is,
**AvaTax Refund Account**. Ensure both accounts are set for smooth end-of-year
record keeping. Consult a certified public accountant (CPA) for specific
guidance on setting both accounts.

Click **Save** to implement the changes.

### Tax mapping

The _AvaTax_ integration is available on sale orders and invoices with the
included _AvaTax_ fiscal position.

#### Product category mapping

Before using the integration, specify an **Avatax Category** on the product
categories. Navigate to Inventory app ‣ Configuration ‣ Product Categories.
Select the product category to add the **AvaTax Category** to. In the **AvaTax
Category** field, select a category from the drop-down menu, or **Search
More…** to open the complete list of options.

![Specify AvaTax Category on products.](../../../../_images/avatax-
category.png)

#### Product mapping

_AvaTax_ Categories may be set on individual products, as well. To set the
**Avatax Category** navigate to Inventory app ‣ Products ‣ Products. Select
the product to add the **Avatax Category** to. Under the **General
Information** tab, on the far-right, is a selector field labeled: **Avatax
Category**. Finally, click the drop-down menu, and select a category, or
**Search More…** to find one that is not listed.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Some limitations exist in Konvergo ERP while using <em>AvaTax</em> for tax calculation:</p>
<ul>
<li><p><em>AvaTax</em> is <b>not</b> supported in Konvergo ERP’s <em>Point of Sale</em> app, because a dynamic tax calculation
model is excessive for transactions within a single delivery address, such as stores or
restaurants.</p></li>
<li><p><em>AvaTax</em> and Konvergo ERP use the company address and <b>not</b> the warehouse address.</p></li>
<li><p>Exercise tax is <b>not</b> supported. This includes tobacco/vape taxes, fuel taxes, and other
specific industries.</p></li>
</ul>
</div>7 ![Override product categories as
needed.](../../../../_images/override-avatax-product-category.png)
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Some limitations exist in Konvergo ERP while using <em>AvaTax</em> for tax calculation:</p>
<ul>
<li><p><em>AvaTax</em> is <b>not</b> supported in Konvergo ERP’s <em>Point of Sale</em> app, because a dynamic tax calculation
model is excessive for transactions within a single delivery address, such as stores or
restaurants.</p></li>
<li><p><em>AvaTax</em> and Konvergo ERP use the company address and <b>not</b> the warehouse address.</p></li>
<li><p>Exercise tax is <b>not</b> supported. This includes tobacco/vape taxes, fuel taxes, and other
specific industries.</p></li>
</ul>
</div>8 <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Some limitations exist in Konvergo ERP while using <em>AvaTax</em> for tax calculation:</p>
<ul>
<li><p><em>AvaTax</em> is <b>not</b> supported in Konvergo ERP’s <em>Point of Sale</em> app, because a dynamic tax calculation
model is excessive for transactions within a single delivery address, such as stores or
restaurants.</p></li>
<li><p><em>AvaTax</em> and Konvergo ERP use the company address and <b>not</b> the warehouse address.</p></li>
<li><p>Exercise tax is <b>not</b> supported. This includes tobacco/vape taxes, fuel taxes, and other
specific industries.</p></li>
</ul>
</div>9

  * [AvaTax use](avatax/avatax_use)
  * [Avalara (Avatax) portal](avatax/avalara_portal)

  *[API]: application programming interface

