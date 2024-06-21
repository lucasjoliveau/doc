# Companies

A centralized management environment allows you to select multiple companies
simultaneously and set their specific warehouses, customers, equipment, and
contacts. It provides you the ability to generate reports of aggregated
figures without switching interfaces, which facilitates daily tasks and the
overall management process.

## Manage companies and records

Go to Settings ‣ Manage Companies and fill in the form with your company’s
information. If a _Parent Company_ is selected, records are shared between the
two companies (as long as both environments are active).

![Overview of a new company's form in
Konvergo ERP](../../_images/create_js_store_us.png) <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Activate the <a href="developer_mode#developer-mode"><span class="std std-ref">developer mode</span></a> to choose a <em>Favicon</em> for each of your
companies, and easily identify them by the browser tabs. Set your favicons’ files size to 16x16
or 32x32 pixels. JPG, PNG, GIF, and ICO are extensions accepted.</p>
<img alt="View of a web browser and the favicon for a specific company chosen in Konvergo ERP" class="align-center" src="../../_images/favicon.png" style="height: 200px;"/>
</div>

Switch between or select multiple companies by enabling their selection boxes
to activate them. The grayed company is the one which environment is in use.
To switch environments, click on the company’s name. In the example below, the
user has access to three companies, two are activated, and the environment in
use is of _JS Store US_.

![View of the companies menu through the main dashboard in
Konvergo ERP](../../_images/multi_companies_menu_dashboard.png)

Data such as Products, Contacts, and Equipment can be shared or set to be
shown for a specific company only. To do so, on their forms, choose between:

  * _A blank field_ : the record is shared within all companies.

  * _Adding a company_ : the record is visible to users logged in to that specific company.

![View of a product's form emphasizing the company field in Konvergo ERP
Sales](../../_images/product_form_company.png)

## Employees’ access

Once companies are created, manage your employees’ [Access
Rights](users/access_rights) for _Multi Companies_.

![View of an user form emphasizing the multi companies field under the access
rights tabs in Konvergo ERP](../../_images/access_rights_multi_companies.png)

If a user has multiple companies _activated_ on his database, and he is
**editing** a record, the editing happens on the record’s related company.

Example: if editing a sale order issued under JS Store US while working on the
JS Store Belgium environment, the changes are applied under JS Store US (the
company from which the sale order was issued).

When **creating** a record, the company taken into account is:

  * The current company (the one active) or,

  * No company is set (on products and contacts’ forms for example) or,

  * The company set is the one linked to the document (the same as if a record is being edited).

## Documents’ format

To set documents’ formats according to each company, _activate_ and _select_
the respective one and, under _Settings_ , click on _Configure Document
Layout_.

![View of the settings page emphasizing the document layout field in
Konvergo ERP](../../_images/document_layout.png)

## Inter-Company Transactions

First, make sure each one of your companies is properly set in relation to:

  * [Chart of Accounts](../finance/accounting/get_started/chart_of_accounts)

  * [Taxes](../finance/accounting/taxes)

  * [Fiscal Positions](../finance/accounting/taxes/fiscal_positions)

  * [Journals](../finance/accounting/bank)

  * [Fiscal Localizations](../finance/fiscal_localizations)

  * [Pricelists](../sales/sales/products_prices/prices/pricing)

Now, activate the _Inter-Company Transactions_ option under _Settings_. With
the respective company _activated_ and _selected_ , choose if you would like
operations between companies to be synchronized at an invoice/bills level or
at a sales/purchase orders level.

![View of the settings page emphasizing the inter company transaction field in
Konvergo ERP](../../_images/inter_company_transactions.png)

  * **Synchronize invoice/bills** : generates a bill/invoice when a company confirms a bill/invoice for the selected company.

_Example:_ an invoice posted on JS Store Belgium, for JS Store US,
automatically creates a vendor bill on the JS Store US, from the JS Store
Belgium.

![View of an invoice for JS Store US created on JS Store Belgium in
Konvergo ERP](../../_images/invoice_inter_company.png)

  * **Synchronize sales/purchase order** : generates a drafted purchase/sales order using the selected company warehouse when a sales/purchase order is confirmed for the selected company. If instead of a drafted purchase/sales order you rather have it validated, enable _Automatic Validation_.

_Example:_ when a sale order for JS Store US is confirmed on JS Store Belgium,
a purchase order on JS Store Belgium is automatically created (and confirmed
if the _Automatic Validation_ feature was enabled).

![View of the purchase created on JS Store US from JS Store Belgium in
Konvergo ERP](../../_images/purchase_order_inter_company.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Products have to be configured as <em>Can be sold</em> and must be shared between the companies.</p>
</div>
<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Remember to test all workflows as an user other than the administrator.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../../developer/howtos/company">Multi-company Guidelines</a></p></li>
<li><p><a href="../finance/accounting/get_started/multi_currency">Multi-currency system</a></p></li>
</ul>
</div>

  * [Digest emails](companies/digest_emails)
  * [Email templates](companies/email_template)

