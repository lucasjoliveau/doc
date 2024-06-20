# United Kingdom

## Configuration

[Install](../../general/apps_modules.html#general-install) the UK - Accounting
and the UK - Accounting Reports modules to get all the features of the UK
localization.

Name | Technical name | Description  
---|---|---  
UK - Accounting | `l10n_uk` | 

  * CT600-ready chart of accounts
  * VAT100-ready tax structure
  * Infologic UK counties listing

  
UK - Accounting Reports | `l10n_uk_reports` | 

  * Accounting reports for the UK
  * Allows sending the tax report via the MTD-VAT API to HMRC.

  
![Odoo uk packages](../../../_images/uk.png)

Note

  * Only UK-based companies can submit reports to HMRC.

  * Installing the module UK - Accounting Reports installs all two modules at once.

See also

  * [HM Revenue & Customs](https://www.gov.uk/government/organisations/hm-revenue-customs/)

  * [Overview of Making Tax Digital](https://www.gov.uk/government/publications/making-tax-digital/overview-of-making-tax-digital/)

## Chart of accounts

The UK chart of accounts is included in the UK - Accounting module. Go to
Accounting ‣ Configuration ‣ Accounting: Chart of Accounts to access it.

Setup your CoA by going to Accounting ‣ Configuration ‣ Settings ‣ Accounting
Import section and choose to Review Manually or Import (recommended) your
initial balances.

## Taxes

As part of the localization module, UK taxes are created automatically with
their related financial accounts and configuration.

Go to Accounting ‣ Configuration ‣ Settings ‣ Taxes to update the Default
Taxes, the Tax Return Periodicity or to Configure your tax accounts.

To edit existing taxes or to Create a new tax, go to Accounting ‣
Configuration ‣ Accounting: Taxes.

See also

  * [taxes](../accounting/taxes.html)

  * Tutorial: [Tax report and return](https://www.odoo.com/slides/slide/tax-report-and-return-1719?fullscreen=1).

### Making Tax Digital (MTD)

In the UK, all VAT-registered businesses have to follow the MTD rules by using
software to submit their VAT returns.

The **UK - Accounting Reports** module enables you to comply with the [HM
Revenue & Customs](https://www.gov.uk/government/organisations/hm-revenue-
customs/) requirements regarding [Making Tax
Digital](https://www.gov.uk/government/publications/making-tax-
digital/overview-of-making-tax-digital/).

Important

If your periodic submission is more than three months late, it is no longer
possible to submit it through Odoo, as Odoo only retrieves open bonds from the
last three months. Your submission has to be done manually by contacting HMRC.

#### Register your company to HMRC before the first submission

Go to Accounting ‣ Reporting ‣ Tax report and click on Connect to HMRC. Enter
your company information on the HMRC platform. You only need to do it once.

#### Periodic submission to HMRC

Import your obligations HMRC, filter on the period you want to submit, and
send your tax report by clicking Send to HMRC.

Tip

You can use dummy credentials to demo the HMRC flow. To do so, activate the
[developer mode](../../general/developer_mode.html#developer-mode) and go to
General Settings ‣ Technical ‣ System Parameters. From here, search for
`l10n_uk_reports.hmrc_mode` and change the value line to `demo`. You can get
such credentials from the [HMRC Developer
Hub](https://developer.service.hmrc.gov.uk/api-test-user).

#### Periodic submission to HMRC for multi-company

Only one company and one user can connect to HMRC simultaneously. If several
UK-based companies are on the same database, the user who submits the HMRC
report must follow these instructions before each submission:

  1. Log into the company for which the submission has to be done.

  2. Go to General Settings, and in the Users section, click Manage Users. Select the user who is connected to HMRC.

  3. Go to the UK HMRC Integration tab and click Reset Authentication Credentials or Remove Authentication Credentials button.

  4. You can now register your company to HMRC and submit the tax report for this company.

  5. Repeat the steps for other companies’ HMRC submissions.

Note

During this process, the Connect to HMRC button no longer appears for other
UK-based companies.

  *[CoA]: chart of accounts

