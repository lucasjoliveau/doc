# In-app purchases (IAP)

In-app purchases (IAP) are optional services that enhance Konvergo ERP databases. Each
service provides its own specific features and functionality. A full list of
services is available on the [Konvergo ERP IAP Catalog](https://iap.odoo.com/iap/all-
in-app-services).

![The IAP catalog with various services available on
IAP.Konvergo ERP.com.](../../_images/iap.png) <div class="alert alert-success">
<p class="alert-title">
Example</p><p>The <b>SMS</b> service sends text messages to contacts directly from the database, and the
<b>Documents Digitization</b> service digitizes scanned or PDF vendor bills, expenses, and
resumes with optical character recognition (OCR) and artificial intelligence (AI).</p>
</div>

IAP services do **not** need to be configured or set up before use. Konvergo ERP users
can simply click on the service in the app to activate it. However, each
service requires its own prepaid credits, and when they run out, users
**must** buy more in order to keep using it.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Enterprise Konvergo ERP users with a valid subscription get free credits to test IAP features before
deciding to purchase more credits for the database. This includes demo/training databases,
educational databases, and one-app-free databases.</p>
</div>

## IAP services

IAP services are provided by Konvergo ERP, as well as third-parties, and have a wide
range of uses.

The following IAP services are offered by Konvergo ERP:

  * **Documents Digitization** : digitizes scanned or PDF vendor bills, expenses, and resumes with OCR and AI.

  * **Partner Autocomplete** : automatically populates contact records with corporate data.

  * **SMS** : sends SMS text messages to contacts directly from the database.

  * **Lead Generation** : generates leads based on a set of criteria, and converts web visitors into quality leads and opportunities.

  * **Snailmail** : sends customer invoices and follow-up reports by post, worldwide.

  * **Signer identification with itsme®️** : ask document signatories in Konvergo ERP _Sign_ to provide their identity using the _itsme®_ identity platform, which is available in Belgium and the Netherlands.

For more information on every service currently available (offered from
developers other than Konvergo ERP), visit the [Konvergo ERP IAP
Catalog](https://iap.odoo.com/iap/all-in-app-services).

### Use IAP services

IAP services are automatically integrated with Konvergo ERP, and do **not** require
users to configure any settings. To use a service, simply interact with it
wherever it appears in the database.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>The following flow focuses on the <em>SMS</em> <abbr title="In-app purchases">IAP</abbr> service being used from a contact’s record.</p>
<p>This can be done by clicking the <b>📱 SMS</b> icon within the database.</p>
<img alt="The SMS icon on a typical contact information form located within an Konvergo ERP database." class="align-center" src="../../_images/sms-icon.png"/>
<p>One way to utilize the <em>SMS</em> <abbr title="In-app purchases">IAP</abbr> service with Konvergo ERP is showcased in the following steps:</p>
<p>First, navigate to the Contacts application, and click on a contact with a
mobile phone number entered in either the <b>Phone</b> or <b>Mobile</b> field of the
contact form.</p>
<p>Next, find the <b>📱 SMS</b> icon that appears to the right of the <b>Phone</b> or
<b>Mobile</b> fields. Click the <b>📱 SMS</b> icon, and a <b>Send SMS Text
Message</b> pop-up window appears.</p>
<p>Type a message in the <b>Message</b> field of the pop-up window. Then, click the
<b>Send SMS</b> button. Konvergo ERP then sends the message, via SMS, to the contact, and logs what
was sent in the <em>chatter</em> of the contact’s form.</p>
<p>Upon sending the SMS message, the prepaid credits for the <em>SMS</em> <abbr title="In-app purchases">IAP</abbr> service are automatically
deducted from the existing credits. If there are not enough credits to send the message, Konvergo ERP
prompts the user to purchase more.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p>For more information on how to use various <abbr title="In-app purchases">IAP</abbr> services, and for more in-depth instructions
related to SMS functionality in Konvergo ERP, review the documentation below:</p>
<ul>
<li><p><a href="../sales/crm/acquire_leads/lead_mining">Lead mining</a></p></li>
<li><p><a href="../sales/crm/optimize/partner_autocomplete">Enrich your contacts base with Partner Autocomplete</a></p></li>
<li><p><a href="../marketing/sms_marketing/essentials/sms_essentials">SMS essentials</a></p></li>
</ul>
</div>

## IAP credits

Every time an IAP service is used, the prepaid credits for that service are
spent. Konvergo ERP prompts the purchase of more credits when there are not enough
credits left to continue using a service. Email alerts can also be set up for
when credits are low.

Credits are purchased in _Packs_ from the [Konvergo ERP IAP
Catalog](https://iap.odoo.com/iap/all-in-app-services), and pricing is
specific to each service.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>The <a href="https://iap.odoo.com/iap/in-app-services/1">SMS service</a> has four packs available, in
denominations of:</p>
<ul>
<li><p><b>Starter Pack</b>: 10 credits</p></li>
<li><p><b>Standard Pack</b>: 100 credits</p></li>
<li><p><b>Advanced Pack</b>: 500 credits</p></li>
<li><p><b>Expert Pack</b>: 1,000 credits</p></li>
</ul>
<img alt="Four different packs of credits for the SMS IAP service." class="align-center" src="../../_images/packs.png"/>
<p>The number of credits consumed depends on the length of the SMS and the country of destination.</p>
<p>For more information, refer to the <a href="../marketing/sms_marketing/pricing/pricing_and_faq">SMS Pricing and FAQ</a> documentation.</p>
</div>

### Acheter des crédits

If there are not enough credits to perform a task, the database automatically
prompts the purchase of more credits.

Users can check the current balance of credits for each service, and manually
purchase more credits, by navigating to the Settings app ‣ Contacts section,
and beneath the **Konvergo ERP IAP** setting, click **View My Services**.

Doing so reveals a **My Services** page, listing the various IAP services in
the database. From here, click an IAP service to open its **Account
Information** page, where additional credits can be purchased.

#### Manually buy credits

To manually buy credits in Konvergo ERP, follow these steps:

First, go to the Settings application and type `IAP` in the **Search…** bar.
Alternatively users can scroll down to the **Contacts** section. Under the
**Contacts** section, where it says **Konvergo ERP IAP** , click **View My Services**.

![The Settings app showing the Konvergo ERP IAP heading and View My Services
button.](../../_images/view-services.png)

Doing so reveals an **IAP Account** page, listing the various IAP services in
the database. From here, click an IAP service to open details about it;
additional credits can be purchased from here.

On the following page, click the **Buy Credit** button. Doing so loads a **Buy
Credits for (IAP Account)** page in a new tab. From here, click **Buy** on the
desired pack of credits. Then, follow the prompts to enter payment details,
and confirm the order.

![The SMS service page on IAP.Konvergo ERP.com with four packs of credits available
for purchase.](../../_images/buy-pack.png)

Once the transaction is complete, the credits are available for use in the
database.

#### Low-credit notification

It is possible to be notified when credits are low, in order to avoid running
out of credits, while using an IAP service. To do that, follow this process:

Go to the Settings application, and type `IAP` in the **Search…** bar. Under
the **Contacts** section, where it says **Konvergo ERP IAP** , click **View My
Services**.

The available IAP accounts appear in a list view on the **IAP Account** page.
From here, click on the desired IAP account to view that service’s details.

On the details page, tick the **Receive threshold warning** checkbox. Doing so
reveals two fields on the form: **Warning Threshold** and **Contact Email**.

In the **Warning Threshold** field, enter an amount of credits Konvergo ERP should use
as the minimum threshold for this service. In the **Contact Email** field,
enter the email address that receives the notification.

Konvergo ERP sends a low-credit alert to the **Contact Email** when the balance of
credits falls below the amount listed as the **Warning Threshold**.

  *[IAP]: In-app purchases

