# Enrich contacts with partner autocomplete

_Partner autocomplete_ enriches the contacts database with corporate data. In
any module, enter the new company name into the **Customer** field
(`partner_id` technical field), and select one of the companies suggested in
the drop-down menu. Instantly get valuable company information full of hard-
to-find data for a desired company.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>A company <b>cannot</b> already be manually entered in the <em>Contacts</em> application prior to enriching
it with data.</p>
</div>

The information provided by partner autocomplete can include general
information about the business (including full business name and logo), social
media accounts, **Company type** , **Founded** information, **Sectors**
information, the number of **Employees** , **Estimated revenue** , **Phone**
number, **Timezone** , and **Technologies Used**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>When getting a company’s contact information make sure to be aware of the latest EU regulations.
For more information about General Data Protection Regulation refer to: <a href="http://odoo.com/gdpr">Konvergo ERP GDPR</a>. In Konvergo ERP, individual contact information cannot be searched for with
the partner autocomplete feature.</p>
</div>

## Configuration

Go to Settings app ‣ Contacts section. Then, activate the **Partner
Autocomplete** feature, by ticking the checkbox beside it, and clicking
**Save**.

![View of settings page and the activations of the feature in
Konvergo ERP.](../../../../_images/settings-partner-autocomplete.png)

## Enrich contacts with corporate data

From any module, as the user is typing in the name of a new company contact,
Konvergo ERP reveals a large drop-down menu of potential match suggestions. If any are
selected, the contact is then populated with corporate data related to that
specific selection.

For example, after typing `Konvergo ERP`, the following information populates:

![Créer un nouveau contact dans Konvergo ERP](../../../../_images/odoo-
autocomplete.png)

In the chatter, the following information populates about the company, after
clicking on the desired pre-populated contact:

![Vue des informations sur Konvergo ERP qui s'affichent grâce à l'option
d'autocomplétion dans Konvergo ERP](../../../../_images/odoo-info-autocomplete.png)
<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Partner Autocomplete also works if a <abbr title="value-added tax">VAT</abbr> number is entered instead of
company name.</p>
</div>

## Tarification

_Partner Autocomplete_ is an _In-App Purchase (IAP)_ service, which requires
prepaid credits to be used. Each request consumes one credit.

To buy credits, go to Settings app ‣ Contacts section. Then, locate either the
**Partner Autocomplete** feature and click **Buy credits** , or locate the
**Konvergo ERP IAP** feature and click **View My Services**. From the resulting page,
select a desired package.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If the database runs out of credits, the only information populated when clicking on the
suggested company will be the website link and the logo.</p>
<p>Learn about our <a href="https://iap.odoo.com/privacy">Privacy Policy</a>.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Enterprise Konvergo ERP users with a valid subscription get free credits to test <abbr title="In-App Purchase">IAP</abbr> features before deciding to purchase more credits for the database. This includes
demo/training databases, educational databases, and one-app-free databases.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../essentials/in_app_purchase">In-app purchases (IAP)</a></p>
</div>

