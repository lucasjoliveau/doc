# United Kingdom

## Configuration

[Install](../../general/apps_modules#general-install) the **UK -
Accounting** and the **UK - Accounting Reports** modules to get all the
features of the UK localization.

Name | Technical name | Description  
---|---|---  
**UK - Accounting** | `l10n_uk` | 

  * CT600-ready chart of accounts
  * VAT100-ready tax structure
  * Infologic UK counties listing

  
**UK - Accounting Reports** | `l10n_uk_reports` | 

  * Accounting reports for the UK
  * Allows sending the tax report via the MTD-VAT API to HMRC.

  
![Konvergo ERP uk packages](../../../_images/uk.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Only UK-based companies can submit reports to HMRC.</p></li>
<li><p>Installing the module <b>UK - Accounting Reports</b> installs all two modules at once.</p></li>
</ul>
</div>
<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="https://www.gov.uk/government/organisations/hm-revenue-customs/">HM Revenue &amp; Customs</a></p></li>
<li><p><a href="https://www.gov.uk/government/publications/making-tax-digital/overview-of-making-tax-digital/">Overview of Making Tax Digital</a></p></li>
</ul>
</div>

## Chart of accounts

The UK chart of accounts is included in the **UK - Accounting** module. Go to
Accounting ‣ Configuration ‣ Accounting: Chart of Accounts to access it.

Setup your CoA by going to Accounting ‣ Configuration ‣ Settings ‣ Accounting
Import section and choose to **Review Manually** or **Import (recommended)**
your initial balances.

## Taxes

As part of the localization module, UK taxes are created automatically with
their related financial accounts and configuration.

Go to Accounting ‣ Configuration ‣ Settings ‣ Taxes to update the **Default
Taxes** , the **Tax Return Periodicity** or to **Configure your tax
accounts**.

To edit existing taxes or to **Create** a new tax, go to Accounting ‣
Configuration ‣ Accounting: Taxes.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../accounting/taxes">taxes</a></p></li>
<li><p>Tutorial: <a href="https://www.odoo.com/slides/slide/tax-report-and-return-1719?fullscreen=1">Tax report and return</a>.</p></li>
</ul>
</div>

### Making Tax Digital (MTD)

In the UK, all VAT-registered businesses have to follow the MTD rules by using
software to submit their VAT returns.

The **UK - Accounting Reports** module enables you to comply with the [HM
Revenue & Customs](https://www.gov.uk/government/organisations/hm-revenue-
customs/) requirements regarding [Making Tax
Digital](https://www.gov.uk/government/publications/making-tax-
digital/overview-of-making-tax-digital/).

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If your periodic submission is more than three months late, it is no longer possible to submit
it through Konvergo ERP, as Konvergo ERP only retrieves open bonds from the last three months. Your submission
has to be done manually by contacting HMRC.</p>
</div>

#### Register your company to HMRC before the first submission

Go to Accounting ‣ Reporting ‣ Tax report and click on **Connect to HMRC**.
Enter your company information on the HMRC platform. You only need to do it
once.

#### Periodic submission to HMRC

Import your obligations HMRC, filter on the period you want to submit, and
send your tax report by clicking **Send to HMRC**.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>You can use dummy credentials to demo the HMRC flow. To do so, activate the
<a href="../../general/developer_mode#developer-mode"><span class="std std-ref">developer mode</span></a> and go to General Settings ‣
Technical ‣ System Parameters. From here, search for <code>l10n_uk_reports.hmrc_mode</code> and change
the value line to <code>demo</code>. You can get such credentials from the <a href="https://developer.service.hmrc.gov.uk/api-test-user">HMRC Developer Hub</a>.</p>
</div>

#### Periodic submission to HMRC for multi-company

Only one company and one user can connect to HMRC simultaneously. If several
UK-based companies are on the same database, the user who submits the HMRC
report must follow these instructions before each submission:

  1. Log into the company for which the submission has to be done.

  2. Go to **General Settings** , and in the **Users** section, click **Manage Users**. Select the user who is connected to HMRC.

  3. Go to the **UK HMRC Integration** tab and click **Reset Authentication Credentials** or **Remove Authentication Credentials** button.

  4. You can now register your company to HMRC and submit the tax report for this company.

  5. Repeat the steps for other companies’ HMRC submissions.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>During this process, the <b>Connect to HMRC</b> button no longer appears for other UK-based
companies.</p>
</div>

  *[CoA]: chart of accounts

