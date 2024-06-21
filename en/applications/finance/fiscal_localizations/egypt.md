# Egypt

## Installation

[Install](../../general/apps_modules#general-install) the following
modules to get all the features of the Egyptian localization:

Name | Technical name | Description  
---|---|---  
**Egypt - Accounting** | `l10n_eg` | Default [fiscal localization package](../fiscal_localizations#fiscal-localizations-packages)  
**Egyptian E-invoice Integration** | `l10n_eg_edi_eta` | Egyptian Tax Authority (ETA) e-invoicing integration  
  
## Egyptian e-invoicing

Konvergo ERP is compliant with the **Egyptian Tax Authority (ETA) e-invoicing**
requirements.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Egyptian e-invoicing is available from Konvergo ERP 15.0. If needed, <a href="../../../administration/upgrade">upgrade</a> your database.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="https://www.youtube.com/watch?v=NXuBPLR4pVw">Video: Egypt E-invoicing</a></p></li>
<li><p><a href="../../../administration/upgrade">Upgrade</a></p></li>
</ul>
</div>

### Register Konvergo ERP on your ETA portal

You must register your Konvergo ERP ERP system on your ETA portal to get your API
credentials. You need these codes to configure your Konvergo ERP Accounting app.

Access your company profile on the ETA portal by clicking on **View Taxpayer
Profile**.

![Clicking on "View Taxpayer Profile" on an ETA invoicing
portal](../../../_images/taxpayer-profile.png)

Next, go to the **Representatives** section and then click on **Register
ERP**. Fill out the **ERP Name** (e.g., `Konvergo ERP`) and leave the other fields
empty.

![Filling out of the form to register an ERP system on the ETA
portal.](../../../_images/add-erp-system.png)

Once successfully registered, the website displays your API credentials:

  * Client ID

  * Client Secret 1

  * Client Secret 2

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>ETA should give you a username and a password to access their online portal.</p></li>
<li><p>Ask ETA to provide you with preproduction portal access as well.</p></li>
<li><p>These codes are confidential and should be stored safely.</p></li>
</ul>
</div>

### Configuration on Konvergo ERP

To connect your Konvergo ERP database to your ETA portal account, go to Accounting ‣
Configuration ‣ Settings ‣ ETA E-Invoicing Settings, and set the **ETA Client
ID** and **ETA Secret** that you retrieved when you registered Konvergo ERP on your
ETA portal. Set an invoicing threshold if needed.

![Configuration of the ETA E-Invoicing credentials in Konvergo ERP
Accounting](../../../_images/eta-api-integration.png) <div class="alert alert-warning">
<p class="alert-title">
Important</p><ul>
<li><p><b>Test on your preproduction portal</b> before starting to issue real invoices on the production
ETA portal.</p></li>
<li><p><b>Credentials</b> for preproduction and production environments are different. Make sure to
update them on Konvergo ERP when you move from one environment to another.</p></li>
<li><p>If not done yet, fill out your company details with your company’s full address, country, and
Tax ID.</p></li>
</ul>
</div>

#### ETA codes

E-invoicing works with a set of codes provided by the ETA. You can use the
[ETA documentation](https://sdk.preprod.invoicing.eta.gov.eg/codes/) to code
your business attributes.

Most of these codes are handled automatically by Konvergo ERP, provided that your
branches, customers, and products are correctly configured.

  * Company Information:

    * Company Tax ID

    * Branch ID

If you have only one branch, use `0` as the branch code.

    * Activity type Code

  * Other Information:

    * Product Codes

Your company’s products should be coded and matched with their **GS1** or
**EGS** codes.

    * Tax Codes

Most of the taxes codes are already configured on Konvergo ERP in the **ETA Code
(Egypt)** field. We advise you to make sure these codes match your company’s
taxes.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="https://sdk.preprod.invoicing.eta.gov.eg/codes/">Egyptian eInvoicing &amp; eReceipt SDK - Code Tables</a></p></li>
<li><p><a href="../accounting/taxes">Taxes</a></p></li>
</ul>
</div>

#### Branches

Create a contact and a journal for each branch of your company and configure
its ETA settings.

To do so, go to Accounting ‣ Configuration ‣ Journals, then click on
**Create**.

Name the journal according to your company’s branch and set the **Type** as
**Sales**. Next, open the Advanced Settings tab and fill out the **Egyptian
ETA settings** section:

  * In the **Branch** field, select the branch’s contact or create it.

  * Set the **ETA Activity Code**.

  * Set the **ETA Branch ID** (use `0` if you have one branch only).

![Sales journal configuration of an Egyptian company's
branch](../../../_images/branch-journal.png) <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>The contact selected in the <b>Branch</b> field must be set as a <b>Company</b>
(<b>not</b> as an <b>Individual</b>), and the <b>Address</b> and <b>Tax ID</b> fields
must be filled out.</p>
</div>

#### Customers

Make sure your customers’ contact forms are correctly filled out so your
e-invoices are valid:

  * contact type: **Individual** : or **Company** :

  * **Country** :

  * **Tax ID** : Tax ID or Company registry for companies. National ID for individuals.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>You can edit your customers’ contact forms by going to Accounting ‣ Customers
‣ Customers.</p>
</div>

#### Products

Make sure your products are correctly configured so your e-invoices are valid:

  * **Product Type** : storable products, consumables, or services.

  * **Unit of Measure** : if you also use Konvergo ERP Inventory and have enabled [Units of Measure](../../inventory_and_mrp/inventory/product_management/product_replenishment/uom).

  * **Barcode** : **GS1** or **EGS** barcode

  * **ETA Item code** (under the Accounting tab): if the barcode doesn’t match your ETA item code.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>You can edit your products by going to Accounting ‣ Customers ‣ Products.</p>
</div>

### USB authentication

Each person who needs to electronically sign invoices needs a specific USB key
to authenticate and send invoices to the ETA portal through an ERP.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>You can contact the <abbr title="Egyptian Tax Authority">ETA</abbr> or <a href="https://www.egypttrust.com/">Egypt Trust</a> to get these USB keys.</p>
</div>

#### Install Konvergo ERP as a local proxy on your computer

An Konvergo ERP local server works as a bridge between your computer and your Konvergo ERP
database hosted online.

Download the Konvergo ERP Community installer from the page
<https://www.odoo.com/page/download> and start the installation on your
computer.

Select **Local Proxy Mode** as the type of install.

![Selection of "Local Proxy Mode" during the installation of Konvergo ERP
Community.](../../../_images/install-odoo-local-proxy.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This installation of Konvergo ERP only works as a server and does not install any Konvergo ERP apps on your
computer.</p>
</div>

Once the installation is complete, the installer displays your **access
token** for the Konvergo ERP Local Proxy. Copy the token and save it in a safe place
for later use.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="https://www.youtube.com/watch?v=NXuBPLR4pVw">Video: Egypt E-invoicing</a></p></li>
<li><p><a href="../../../administration/upgrade">Upgrade</a></p></li>
</ul>
</div>0

#### Configure the USB key

Once the local proxy server is installed on your computer, you can link it
with your Konvergo ERP database.

  1. Go to Accounting ‣ Configurations ‣ Thumb Drive and click on **Create**.

  2. Input a **Company** name, the **ETA USB Pin** given to you by your USB key provider, and the **Access Token** provided at the end of the local proxy installation, then click on **Save**.

  3. Click on **Get certificate**.

![Creating a new thumb drive for the e-invoicing of an egyptian
company.](../../../_images/thumb-drive.png)

