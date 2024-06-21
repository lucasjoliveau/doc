# Lead enrichment

_Lead enrichment_ is a service that provides business information for a
contact attached to a lead. Lead enrichment is an In-App Purchase (IAP) that
requires credits to use, and is available for existing leads in an Konvergo ERP
database.

The information provided by lead enrichment can include general information
about the business (including full business name and logo), social media
accounts, **Company type** , **Founded** information, **Sectors** information,
the number of **Employees** , **Estimated revenue** , **Phone** number,
**Timezone** , and **Technologies Used**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Enterprise Konvergo ERP users with a valid subscription get free credits to test <abbr title="In-App Purchase">IAP</abbr> features before deciding to purchase more credits for the database. This includes
demo/training databases, educational databases, and one-app-free databases.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>The <em>leads</em> feature <b>must</b> be activated in the <em>CRM</em> settings page in order to use lead
enrichment. To access the <em>CRM</em> settings, navigate to CRM app ‣ Configuration
‣ Settings. Under the <b>CRM</b> section activate the <b>Leads</b> option and click
<b>Save</b>.</p>
</div>

## Lead enrichment set up

To set up lead enrichment in the _CRM_ application, navigate to CRM app ‣
Configuration ‣ Settings. Then, under the **Lead Generation** section, tick
the checkbox next to **Lead Enrichment** , and select either **Enrich leads on
demand only** or **Enrich all leads automatically**. Click the **Save** button
to activate the changes.

![CRM lead generation settings page, with lead enrichment activation
highlighted, and enrich leads on demand only
chosen.](../../../../_images/lead-enrichment-activate.png)

## Enrich leads

Enrichment of leads is based on the domain of the email address of the
customer set on the lead. There are two different ways that a lead can be
enriched: _automatically_ or _manually_.

### Automatically enrich leads

During set up, if **Enrich all leads automatically** was selected on the _CRM_
**Settings** page, then no action needs to be taken by the user to enrich the
lead. A scheduled action runs automatically, every sixty minutes, and
enrichment occurs on leads, after a remote database is contacted.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>To access the cron that runs for the automatic lead enrichment, activate <a href="../../../general/developer_mode#developer-mode"><span class="std std-ref">developer mode</span></a>, and navigate to Settings app ‣ Technical menu ‣ Automation
section ‣ Scheduled Actions. In the <b>Search…</b> bar, type in <code>CRM</code>. Click into the
result labeled <b>CRM: enrich leads (IAP)</b>, and make any necessary adjustments. In the
<b>Execute Every</b> field, enter a value greater than, or equal to, five minutes.</p>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>The following is an example of lead enrichment data that has been autocompleted successfully:</p>
<img alt="Chatter showing lead enrichment data." class="align-center" src="../../../../_images/lead-enrichment-data.png"/>
</div>

### Manually enrich leads

If the **Enrich leads on demand only** option was selected on the _CRM_
**Settings** page, when activating **Lead Enrichment** , each lead that a user
wishes to enrich **must** be manually enriched. This is achieved by clicking
the **Enrich** button in the top menu of the lead.

The same information will be retrieved at the same IAP credit cost (one per
enrichment). This method of enrichment is useful when every lead does not need
to be enriched, or cost is an issue.

![Manual enrich button feature highlighted on the CRM
lead.](../../../../_images/manual-enrichment.png) <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Manually enrich leads in bulk using the <em>list</em> view. First, navigate to CRM app
‣ Leads, and click the list view button (<b>☰ (three horizontal lines)</b> icon). Next,
tick the checkboxes for the leads that should be manually enriched. Finally, click the
<b>⚙️ Action</b> icon, and select <b>Enrich</b> from the resulting drop-down menu. This
can also be achieved from the <em>My Pipeline</em> page. To do so, simply open the <em>CRM</em> app, or
navigate to CRM app ‣ Sales ‣ My Pipeline. Either route reveals leads and
opportunities on the <b>Pipeline</b> page.</p>
</div>

## Pricing

Lead enrichment is an In-App Purchase (IAP) feature, and each enriched lead
costs one credit.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>See here for full pricing information: <a href="https://iap.odoo.com/iap/in-app-services/273">Lead Generation by Konvergo ERP IAP</a>.</p>
</div>

To buy credits, navigate to CRM app ‣ Configuration ‣ Settings. In the **Lead
Generation** section, under the **Lead Enrichment** feature, click on **Buy
Credits**.

![Buy credits from the lead enrichment settings.](../../../../_images/buy-
lead-enrichment-credits-setting.png)

Credits and balances may also be purchased by navigating to the Settings app.
In the **Contacts** section, under the **Konvergo ERP IAP** feature, click on **View
My Services**.

![Buy credits in the Konvergo ERP IAP settings.](../../../../_images/view-my-services-
setting1.png) <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../../essentials/in_app_purchase">In-app purchases (IAP)</a></p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>When collecting a company’s contact information, make sure to be aware of the latest EU
regulations. For more information about General Data Protection Regulation, refer to: <a href="http://odoo.com/gdpr">Konvergo ERP GDPR</a>.</p>
</div>

  *[IAP]: In-App Puchase

