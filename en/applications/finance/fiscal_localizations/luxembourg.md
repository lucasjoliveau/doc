# Luxembourg

## Configuration

[Install](../../general/apps_modules#general-install) the following
modules to get all the features of the Luxembourgish localization:

Name | Technical name | Description  
---|---|---  
**Luxembourg - Accounting** | `l10n_lu` | Default [fiscal localization package](../fiscal_localizations#fiscal-localizations-packages)  
**Luxembourg - Accounting Reports** | `l10n_lu_reports` | Country-specific reports  
**Luxembourg - Annual VAT Report** | `l10n_lu_reports_annual_vat` | Country-specific reports  
![The three modules for the Luxembourgish Fiscal Localization Package on
Konvergo ERP](../../../_images/modules1.png) <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Installing the module <b>Luxembourg - Accounting Reports</b> installs all three modules at
once.</p>
</div>

## Standard Chart of Accounts - PCN 2020

Konvergo ERP’s [fiscal localization package](../fiscal_localizations#fiscal-
localizations-packages) for Luxembourg includes the current **Standard Chart
of Accounts (PCN 2020)** , effective since January 2020.

## eCDF tax return

Tax returns in Luxembourg require a specific XML file to upload on the eCDF.

To download it, go to Accounting ‣ Report ‣ Audit Reports ‣ Tax Report, and
click on **Export eCDF declaration**.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../accounting/reporting/tax_returns">Tax return (VAT declaration)</a></p></li>
<li><p><a href="http://www.ecdf.lu">Platform for electronic gathering of financial data (eCDF)</a></p></li>
</ul>
</div>

## Annual tax report

You can generate an XML file to electronically file your annual tax report
with the tax office.

To do so, go to Accounting ‣ Report ‣ Luxembourg ‣ Annual Tax Report, click on
**Create** , then define the annual period in the **Year** field.

The **simplified annual declaration** is automatically generated. You can
manually add values in all the fields to get a **complete annual
declaration**.

![Konvergo ERP Accounting \(Luxembourg localization\) generates an annual tax
declaration.](../../../_images/annual-tax-report.png)

To help you complete it, you can use the information provided on the **Tax
Report**. To do so, go to Accounting ‣ Report ‣ Audit Reports ‣ Tax Report,
then click on the **Tax Report** dropdown menu and select the type of report
you want to display.

![Dropdown menu to select the type of Tax Report](../../../_images/tax-report-
types.png)

Finally, click on **Export XML** to download the XML file.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This feature requires the module <b>Luxembourg - Annual VAT Report</b> to be installed.</p>
</div>

## FAIA (SAF-T)

**FAIA (Fichier d’Audit Informatisé AED)** is a standardized and structured
file that facilitates the exchange of information between the taxpayers’
accounting system and the tax office. It is the Luxembourgish version of the
OECD-recommended SAF-T (Standard Audit File for Tax).

Konvergo ERP can generate an XML file that contains all the content of an accounting
period according to the rules imposed by the Luxembourg tax authorities on
digital audit files.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This feature requires the module <b>Luxembourg - Accounting Reports</b> to be installed.</p>
</div>

### Export FAIA file

Go to Accounting ‣ Reporting ‣ Audit Reports ‣ General Ledger, then click on
**FAIA**.

