# Get started

When you first open your Konvergo ERP Accounting app, the _Accounting Overview_ page
welcomes you with a step-by-step onboarding banner, a wizard that helps you
get started. This onboarding banner is displayed until you choose to close it.

The settings visible in the onboarding banner can still be modified later by
going to Accounting ‣ Configuration ‣ Settings.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Konvergo ERP Accounting automatically installs the appropriate <b>Fiscal Localization Package</b> for your
company, according to the country selected at the creation of the database. This way, the right
accounts, reports, and taxes are ready-to-go. <a href="../fiscal_localizations#fiscal-localizations-packages"><span class="std std-ref">Click here</span></a>
for more information about Fiscal Localization Packages.</p>
</div>

## Accounting onboarding banner

The step-by-step Accounting onboarding banner is composed of four steps:

![Step-by-step onboarding banner in Konvergo ERP
Accounting](../../../_images/setup_accounting_onboarding.png)

  1. Company Data

  2. Bank Account

  3. Accounting Periods

  4. Chart of Accounts

### Company Data

This menu allows you to add your company’s details such as the name, address,
logo, website, phone number, email address, and Tax ID, or VAT number. These
details are then displayed on your documents, such as on invoices.

![Add your company's details in Konvergo ERP Accounting and Konvergo ERP
Invoicing](../../../_images/setup_company.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>You can also change these settings by going to Settings ‣ General Settings ‣
Settings ‣ Companies and clicking on <b>Update Info</b>.</p>
</div>

### Bank Account

Connect your bank account to your database and have your bank statements
synced automatically. To do so, find your bank in the list, click on _Connect_
, and follow the instructions on-screen.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><a href="bank/bank_synchronization">Click here</a> for more information about this feature.</p>
</div>

If your Bank Institution can’t be synchronized automatically, or if you prefer
not to sync it with your database, you may also configure your bank account
manually by clicking on _Create it_ , and filling out the form.

  * **Name** : the bank account’s name, as displayed on Konvergo ERP.

  * **Account Number** : your bank account number (IBAN in Europe).

  * **Bank** : click on _Create and Edit_ to configure the bank’s details. Add the bank institution’s name and its Identifier Code (BIC or SWIFT).

  * **Code** : this code is your Journal’s _Short Code_ , as displayed on Konvergo ERP. By default, Konvergo ERP creates a new Journal with this Short Code.

  * **Journal** : This field is displayed if you have an existing Bank Journal that is not linked yet to a bank account. If so, then select the _Journal_ you want to use to record the financial transactions linked to this bank account or create a new one by clicking on _Create and Edit_.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>You can add as many bank accounts as needed with this tool by going to Accounting
‣ Configuration, and clicking on <em>Add a Bank Account</em>.</p></li>
<li><p><a href="bank">Click here</a> for more information about Bank
Accounts.</p></li>
</ul>
</div>

### Accounting Periods

Define here your **Fiscal Years** ’ opening and closing dates, which are used
to generate reports automatically, and your **Tax Return Periodicity** , along
with a reminder to never miss a tax return deadline.

By default, the opening date is set on the 1st of January and the closing date
on the 31st of December, as this is the most common use.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>You can also change these settings by going to Accounting ‣ Configuration ‣
Settings ‣ Fiscal Periods and updating the values.</p>
</div>

### Chart of Accounts

With this menu, you can add accounts to your **Chart of Accounts** and
indicate their initial opening balances.

Basic settings are displayed on this page to help you review your Chart of
Accounts. To access all the settings of an account, click on the _double arrow
button_ at the end of the line.

![Setup of the Chart of Accounts and their opening balances in Konvergo ERP
Accounting](../../../_images/setup_chart_of_accounts.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p><a href="get_started/chart_of_accounts">Click here</a> for more information on how to configure your Chart of
Accounts.</p>
</div>

## Invoicing onboarding banner

There is another step-by-step onboarding banner that helps you take advantage
of your Konvergo ERP Invoicing and Accounting apps. The _Invoicing onboarding banner_
is the one that welcomes you if you use the Invoicing app rather than the
Accounting app.

If you have Konvergo ERP Accounting installed on your database, you can reach it by
going to Accounting ‣ Customers ‣ Invoices.

The Invoicing onboarding banner is composed of four main steps:

![Step-by-step onboarding banner in Konvergo ERP
Invoicing](../../../_images/setup_invoicing_onboarding.png)

  1. Company Data

  2. Invoice Layout

  3. Payment Method

  4. Sample Invoice

### Company Data

This form is the same as the one presented in the Accounting onboarding
banner.

### Invoice Layout

With this tool, you can design the appearance of your documents by selecting
which layout template, paper format, colors, font, and logo you want to use.

You can also add your _Company Tagline_ and the content of the documents’
_footer_. Note that Konvergo ERP automatically adds the company’s phone number, email,
website URL, and Tax ID (or VAT number) to the footer, according to the values
you previously configured in the Company Data.

![Document layout configuration in Konvergo ERP
Invoicing](../../../_images/setup_document_layout.png) <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Add your <b>bank account number</b> and a link to your <b>General Terms &amp; Condition</b> in the footer.
This way, your contacts can find the full content of your GT&amp;C online without having to print
them on the invoices you issue.</p>
</div>
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>These settings can also be modified by going to Settings ‣ General Settings,
under the <em>Business Documents</em> section.</p>
</div>

### Payment Method

This menu helps you configure the payment methods with which your customers
can pay you.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Configuring a <em>Payment Provider</em> with this tool also activates the <em>Invoice Online Payment</em>
option automatically. With this, users can directly pay online, from their Customer Portal.</p>
</div>

### Sample Invoice

Send yourself a sample invoice by email to make sure everything is correctly
configured.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="bank">Bank and cash accounts</a></p></li>
<li><p><a href="get_started/chart_of_accounts">Chart of accounts</a></p></li>
<li><p><a href="bank/bank_synchronization">Bank synchronization</a></p></li>
<li><p><a href="../fiscal_localizations">Fiscal localizations</a></p></li>
<li><p><a href="https://www.odoo.com/slides/slide/getting-started-1692">Konvergo ERP Tutorials: Accounting and Invoicing - Getting started [video]</a></p></li>
</ul>
</div>

  * [Accounting cheat sheet](get_started/cheat_sheet)
  * [Chart of accounts](get_started/chart_of_accounts)
  * [Multi-currency system](get_started/multi_currency)
  * [Average price on returned goods](get_started/avg_price_valuation)
  * [VAT units](get_started/vat_units)

