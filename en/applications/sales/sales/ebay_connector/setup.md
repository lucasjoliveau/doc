# eBay connector setup

## Overview

Konvergo ERP’s eBay connector allows eBay listings to connect with Konvergo ERP products. Once
connected, [updates to the listings](linking_listings) can be made in
Konvergo ERP or in eBay. When an item sells on eBay, draft _sales orders_ are created
in Konvergo ERP for the user to review and confirm. Once the sales order is confirmed,
Konvergo ERP _Inventory_ and _Sales_ apps function standard to pull products out of
inventory, and allow the user to create invoices.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p>To learn more about the eBay connector visit these pages as well:</p>
<ul>
<li><p><a href="manage">How to list a product?</a></p></li>
<li><p><a href="linking_listings">Linking existing listings</a></p></li>
<li><p><a href="troubleshooting">Troubleshooting eBay connector</a></p></li>
</ul>
</div>

### eBay - Konvergo ERP linked fields

The following are eBay product details. Each of these eBay fields update
corresponding fields in Konvergo ERP.

  * eBay URL

  * eBay status

  * Quantity sold

  * Start date

  * Title

  * Subtitle

  * Item condition

  * Category

  * Category 2

  * Store category

  * Store category 2

  * Payment policy

  * Seller profiles

  * Postal code

  * Shipping policy

  * Listing type (fixed price or auction)

    * Starting price for Auction

    * Buy it now price

    * Fixed Price amount

  * Use stock quantity

  * Quantity on eBay

  * Duration

  * Allow best offer

  * Private listing

  * eBay description

  * eBay product image

  * Country

### eBay terms

_Variations_ group multiple products into one, with variation (or variant)
options. Variations can sync to Konvergo ERP’s attributes and values. Variations will
appear in drop down menus near the top of the page when viewing an eBay
listing. These are comparable to product variants in Konvergo ERP.

![An example on eBay of the variations that can be added to a
product.](../../../../_images/ebay-variation.png)

_Item specifics_ , located at the bottom of the listing, detail product-
specific information. These specifics don’t sync with Konvergo ERP fields by default;
a development is required to link these fields.

![Item specifics listed on an eBay product.](../../../../_images/item-
specifics.png)

_Sandbox_ and _Production_ are terms that are used to categorize the eBay
environments as either still in development/testing (_Sandbox_) or for use in
the real instance of the database with real customer information/dataset
(_Production_). It is recommended to start first in the _Sandbox_ to test, and
then following the processes below, create a _Production_ instance.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>eBay’s sandbox environment can be accessed by navigating to <a href="https://sandbox.ebay.com/">eBay’s sandbox portal</a> at <code>https://sandbox.ebay.com/</code>. eBay’s production environment can
be accessed by navigating to <a href="https://www.ebay.com/">eBay.com portal</a> or
<code>https://www.ebay.com/</code>.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>The environment selection <b>must</b> remain the same for all environment settings on eBay and on
Konvergo ERP throughout this setup.</p>
</div>

### eBay actions available on Konvergo ERP

The following are built-in actions in Konvergo ERP that add or update eBay listings:

  * **List** / **Link** : generate a new eBay listing with an Konvergo ERP product by clicking **List Item on eBay** or **Link With Existing eBay Listing**.

  * **Revise item** button: after making changes to an eBay listing in Konvergo ERP, save the record, and then click the **Revise Item** in Konvergo ERP to update the eBay listing.

  * **Relist** : if an item’s listing was ended early or **auto-relist** was not selected, a user can relist the item from Konvergo ERP. The start date will reset.

  * **End item’s listing** button: end a listing on eBay directly from Konvergo ERP.

  * **Unlink product listings** : users can unlink a product from the eBay listing; the listing will stay intact on eBay.

## Setup required on Konvergo ERP prior to eBay setup

To link eBay with Konvergo ERP, install the eBay module by navigating to the Konvergo ERP
dashboard and clicking into the **Apps** application. Search the term `eBay`
and install the `eBay Connector` module.

The following items must be configured before eBay is set up:

  * In Konvergo ERP, create and configure products that are intended to be listed in eBay. eBay does not import new products into Konvergo ERP. All products must first be created in Konvergo ERP, and then linked to listings.

    * Konvergo ERP does not allow multiple eBay listings to be linked per product in Konvergo ERP. If the company sells the same product for multiple listings, follow these instructions:

      * Set up one _base_ product (noted in the **Component** field of the BoM) from which all eBay listings will pull from. This will be a storable product so stock can be kept. Highlighted in green below, this product will be included in the kit on each subsequent “linked” product below.

      * Set up 2+ _linked_ products (noted in the **Product** field of the BoM, one for each eBay listing. The product type will be determined by the company’s accounting settings, as explained in the Konvergo ERP documentation. Highlighted in yellow below, each product should have a **BoM type** equal to **Kit** and have the base product as a **Component** of the kit. When this linked eBay product is sold, the delivery order created will have the base product listed in lieu of the linked product.

![Setting up bill of materials with base product and linked
products.](../../../../_images/products-odoo.png)

> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../../inventory_and_mrp/manufacturing/management/bill_configuration">Bill of materials</a></p>
</div>

  * eBay does not automatically create invoices for eBay orders that get pushed into Konvergo ERP. Set invoicing policy on eBay products: invoicing policy will dictate when the product can be invoiced. Since most eBay users collect payment before the product is shipped, “invoice on ordered” will allow users to mass create invoices for eBay orders every day.

  * Set the **Outgoing Shipments** route for the warehouse to **Deliver goods directly (1 step)**.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>When the <b>Outgoing Shipments</b> route is set to two or three steps, a known bug occurs:
eBay wrongly marks orders as delivered when the pick operation in Konvergo ERP is confirmed. The
expected behavior is to mark orders as delivered <b>after</b> the <em>delivery order</em> is confirmed.
This mislabeling prevents tracking numbers in eBay from being imported onto the delivery order.</p>
</div>

  * If the Accounting/Invoicing apps are installed, practice registering payment and reconciling invoices created from eBay orders with incoming eBay money.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../../finance/accounting/bank/reconciliation">Bank reconciliation</a></p>
</div>

  * Generate a marketplace account deletion/closure notification token. To begin, navigate to Sales app ‣ Configuration ‣ Settings. Under the **eBay** heading, change the mode to **Production** , and input random text values for the **Production Cert Key**. Then click the **Generate Token** button under the **eBay Marketplace Account Deletion/Closure Notifications** section. This token will be used during the setup on eBay for the deletion/closure notifications configuration.

![Generate a verification token in Konvergo ERP.](../../../../_images/generate-
token.png)

## Set up on eBay

### Set up eBay developer account

To start, create an eBay developer account via [eBay’s developer
portal](https://go.developer.ebay.com/). This site requires a different login
and password than the eBay account, though the same email address can be used
to register. The verification to create a developer account is around 24
hours.

### Set up eBay keyset

Once the eBay developer account is created, set up an application on [eBay’s
developer portal](https://go.developer.ebay.com/). Next, navigate to the **Hi
[username]** heading at top right of screen, then from the drop-down menu
options, click **Application Keysets**. Doing so opens a pop-up that prompts
the user to **Enter Application Title** (up to fifty characters), and choose a
development environment (**Sandbox** or **Production**). These two fields
generate first keyset. This application title is not saved until the keyset is
generated. Click on **Create a keyset** to generate the keyset.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>The newly created <em>production keyset</em> is disabled by default. Activate it by subscribing to the
eBay Marketplace ‘account deletion or closure notifications’ or by applying to eBay for an
exemption. Once enabled, the database can make 5000 calls per day using this keyset.</p>
</div> ![Disabled keyset present after creating a
keyset.](../../../../_images/disabled-keyset.png)

#### Configure account deletion / notification settings (Production)

To configure notifications or delete the database on a production environment,
navigate to the [eBay developer portal](https://go.developer.ebay.com/).
Configure the account deletion/notification settings in eBay by navigating to
the `Hi [username]` at top right of screen, then **Application Keysets**.

Next, click the **marketplace deletion/account closure notification** option
under the **Production** keyset column. Enter an email under **Email to notify
if marketplace account deletion notification endpoint is down**. Click
**Save** to enable the email.

Following this action, enter the **Marketplace account deletion notification
endpoint** URL provided by Konvergo ERP. This HTTPs endpoint is found in Konvergo ERP by
navigating to Sales app ‣ Configuration ‣ Settings, in the **eBay Marketplace
Account Deletion/Closure Notifications** field.

Clicking the **Generate Token** button in Konvergo ERP below this field creates a
verification token for the eBay production environment. In Konvergo ERP, **Copy** the
newly created token and navigate to eBay to fill in the **Verification token**
field. Click **Save** to enable the **Event Notification Delivery Method**.

![Configuring account deletion / notification settings in
eBay.](../../../../_images/account-closure.png)

After completing the above fields, click **Send Test Notification** to test
the new notifications. Proceed to the next step when the green check mark
appears. Revisit the above settings if the test post is not as expected.

After configuring notification settings, go back to the Application Keys page
to generate production keysets.

#### Creating the keyset

A successful setup of the notifications enables the ability to create
Production Keysets which are needed in the remainder of the Konvergo ERP
configuration. Navigate back to the Application Keys page generate a
production keyset.

The administrator is prompted to Confirm the Primary Contact. Enter or confirm
the account owner (the person legally responsible for the eBay API License
Agreement). Fill out **First Name** , **Last Name** , **Email** , **Phone**.
Then, select either the **Individual** or **Business** options.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The provided email address or phone number does <b>not</b> have to match the account’s. eBay uses
this information to contacting the business or individual in case of issues with user tokens.
Additional contacts can be added from the <b>Profile &amp; Contacts</b> page on eBay.</p>
</div>

Click on **Continue to Create Keys** to confirm the primary contact. The
**Application Keys** populates in a new screen and an email is also sent to
the developer account. An **App ID (Client ID)** , **Dev ID** , and **Cert ID
(Client Secret)** all populate.

![Application keys are populated after creating the app in
eBay.](../../../../_images/application-keys.png)

Copy these values down as they will be input into Konvergo ERP later in the process.

### Create eBay user token

Now, create a _user token_ in eBay by navigating to the `Hi [username]` at top
right of screen, then **User Access Tokens**.

![Generate user token s on the eBay developer
console.](../../../../_images/user-tokens.png)

Select the correct **Environment** : **Sandbox** for testing or **Production**
for the live database. Maintain the same selection for all environment
settings on both eBay and Konvergo ERP.

Next, select the radio button labeled **Auth’n’Auth**.

Choose **Sign in to Production** or **Sign in to Sandbox** to get a user token
in the chosen environment. This button varies based on the selection made
above for either **Sandbox** or **Production**.

Doing so triggers a a pop-up window to **Confirm your Legal Address**.
Complete the required fields, which are **First Name** , **Last Name** ,
**Primary Email** , **Legal Address** , and **Account Type**. For **Account
Type** , select either **Individual** or **Business**. To complete the
confirmation, click **Sign into eBay to get a Token**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>eBay will contact this individual or business should there be any issues with the application
keys. Other contacts can be added on the Profile &amp; Contacts eBay page.</p>
</div>

The administrator will be redirected to either a sandbox or production sign-in
page for eBay. This login is different than the eBay developer’s console, it
is the eBay account where the items will be sold on. This email and/or login
can differ from the eBay developer account.

Enter the **Email** or **Username** for the eBay account and sign into the
eBay account.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Should an additional user be needed for the sandbox simulation, a test user needs to be created.
Visit <a href="https://developer.ebay.com/sandbox/register">eBay’s Register for Sandbox form</a>. Detailed
instructions can be found on eBay’s help pages: <a href="https://developer.ebay.com/api-docs/static/gs_create-a-test-sandbox-user">Create a test Sandbox user</a>.</p>
</div>

### Grant application access

After signing into the production or sandbox environment, eBay presents the
administrator with an _agreement_ to grant access to the user’s eBay data.

Clicking **Agree** allows eBay to link the eBay account with the _application
programming interface_ (API). This agreement can be changed at any time by
visiting eBay’s account preferences.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>eBay’s sandbox environment can be accessed by navigating to <a href="https://sandbox.ebay.com/">eBay’s sandbox portal</a> at <code>https://sandbox.ebay.com/</code>. eBay’s production environment can
be accessed by navigating to <a href="https://www.ebay.com/">eBay.com portal</a> or
<code>https://www.ebay.com/</code>.</p>
</div>0

A **User Token** will populate on the screen. Make sure to copy this token
down as it will be used in the next steps along with the **Application
Keyset**.

![Generated user token and API explorer link on the eBay developer
console.](../../../../_images/user-token.png) <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>eBay’s sandbox environment can be accessed by navigating to <a href="https://sandbox.ebay.com/">eBay’s sandbox portal</a> at <code>https://sandbox.ebay.com/</code>. eBay’s production environment can
be accessed by navigating to <a href="https://www.ebay.com/">eBay.com portal</a> or
<code>https://www.ebay.com/</code>.</p>
</div>1

### API explorer

Now that the **Application Keyset** and **User Token** have been created, a
test can be executed via the [API
Explorer](https://developer.ebay.com/DevZone/build-test/test-
tool/default.aspx) to ensure that the API is configured correctly. This test
will execute a simple search using the API.

To begin the API test, click on **Get OAuth Application Token**. This will
populate the key into the **Token** field.

A basic search function is set to execute. Click on **Execute** to complete
the test. A successful test will respond with a **Call Response** of `200 OK`
with a corresponding **Time**.

## Entering credentials into Konvergo ERP

The previously copied **User Token** and **Application Keyset** are now ready
to be entered into the Konvergo ERP database.

Navigate back the eBay settings in Konvergo ERP (Sales app ‣ Configuration ‣ Settings
‣ eBay) and paste the following credentials from eBay into the corresponding
fields in Konvergo ERP.

Platform | Dev Key/ID | Token | App Key/ID | Cert Key/ID  
---|---|---|---|---  
eBay | Dev ID | User Token | App ID (Client ID) | Cert ID (Client Secret)  
Konvergo ERP | Developer Key | Production/Sandbox Token | Production/Sandbox App Key | Production/Sandbox Cert Key  
<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>eBay’s sandbox environment can be accessed by navigating to <a href="https://sandbox.ebay.com/">eBay’s sandbox portal</a> at <code>https://sandbox.ebay.com/</code>. eBay’s production environment can
be accessed by navigating to <a href="https://www.ebay.com/">eBay.com portal</a> or
<code>https://www.ebay.com/</code>.</p>
</div>2

Confirm that the setup is correct by saving the credentials in Konvergo ERP. Once the
initial setup is complete, a new menu tab in products will appear called
`eBay` with the option to **Sell on eBay**. See the [How to list a
product?](manage) documentation on how to list products.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>eBay’s sandbox environment can be accessed by navigating to <a href="https://sandbox.ebay.com/">eBay’s sandbox portal</a> at <code>https://sandbox.ebay.com/</code>. eBay’s production environment can
be accessed by navigating to <a href="https://www.ebay.com/">eBay.com portal</a> or
<code>https://www.ebay.com/</code>.</p>
</div>3 <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>eBay’s sandbox environment can be accessed by navigating to <a href="https://sandbox.ebay.com/">eBay’s sandbox portal</a> at <code>https://sandbox.ebay.com/</code>. eBay’s production environment can
be accessed by navigating to <a href="https://www.ebay.com/">eBay.com portal</a> or
<code>https://www.ebay.com/</code>.</p>
</div>5

  *[BoM]: Bill of Materials
  *[API]: Application Programming Interface

