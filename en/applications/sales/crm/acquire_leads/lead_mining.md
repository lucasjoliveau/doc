# Lead mining

Lead mining is a feature that allows CRM users to generate new leads directly
into their Konvergo ERP database. To ensure lead qualification, lead mining output is
determined by a variety of filtering criteria, such as the country, the
company size, and the industry.

## Configuration

To get started, go to CRM ‣ Configuration ‣ Settings and activate **Lead
Mining**.

![Activate lead mining in Konvergo ERP CRM settings.](../../../../_images/activate-
lead-mining.png)

## Generate leads

After the **Lead Mining** setting is activated, a new button called **Generate
Leads** is available to use in the **CRM** pipeline. Lead mining requests are
also available through CRM ‣ Configuration ‣ Lead Mining Requests, or through
CRM ‣ Leads ‣ Leads where the **Generate Leads** button is also available.

![The Generate Leads button to use the lead mining
feature.](../../../../_images/generate-leads-button.png)

Click on the **Generate Leads** button, and a window will appear offering a
variety of criteria by which to generate leads.

![The pop-up window with the selection criteria in order to generate leads in
Konvergo ERP.](../../../../_images/generate-leads-popup.png)

Choose to generate leads for **Companies** to get company information only, or
choose **Companies and their Contacts** to get company information as well as
individual employee contact information. When targeting **Companies and their
Contacts** , there is an option to filter contacts based on **Role** or
**Seniority**.

Additional filtering options include:

  * **Size** : filter leads based on the number of employees at the company

  * **Countries** : filter leads based on the country (or countries) they are located in

  * **States** : further filter leads based on the state they are located in, if applicable

  * **Industries** : filter leads based on the specific industry they work in

  * **Sales Team** : choose which Sales Team the leads will be assigned to

  * **Salesperson** : choose which person(s) on the Sales Team the leads will be assigned to

  * **Default Tags** : choose which tags are applied directly to the leads once found

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Make sure to be aware of the latest EU regulations when receiving contact information. Get more
information about the General Data Protection Regulation on <a href="http://odoo.com/gdpr">Konvergo ERP GDPR</a>.</p>
</div>

## Pricing

Lead mining is an _In-App Purchase_ feature and each generated lead costs one
credit.

Choosing to generate **Companies and their Contacts** costs one additional
credit for each contact generated.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>See here for full pricing information: <a href="https://iap.odoo.com/iap/in-app-services/167?">Lead Generation by Konvergo ERP IAP</a>.</p>
</div>

To buy credits, navigate to CRM ‣ Configuration ‣ Settings. In the **Lead
Generation** section, under the **Lead Mining** feature, click on **Buy
Credits**.

![Buy credits from the lead mining settings.](../../../../_images/buy-lead-
mining-credits-setting.png)

Credits may also be purchased by navigating to the Settings ‣ General
Settings. In the **In-App Purchases** section, under the **Konvergo ERP IAP** feature,
click on **View My Services**.

![Buy credits in the Konvergo ERP IAP settings.](../../../../_images/view-my-services-
setting.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Enterprise Konvergo ERP users with a valid subscription get free credits to test <abbr title="In-App Purchase">IAP</abbr> features before deciding to purchase more credits for the database. This includes
demo/training databases, educational databases, and one-app-free databases.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../../essentials/in_app_purchase">In-app purchases (IAP)</a></p>
</div>

