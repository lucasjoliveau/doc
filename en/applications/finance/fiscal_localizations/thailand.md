# Thailand

## Configuration

[Install](../../general/apps_modules#general-install) the **🇹🇭 Thailand**
localization package to get all the features of the Thai localization:

Name | Technical name | Description  
---|---|---  
**Thailand - Accounting** | `l10n_th` | Default [fiscal localization package](../fiscal_localizations#fiscal-localizations-packages)  
**Thailand - Accounting Reports** | `l10n_th_reports` | Country-specific accounting reports  
![Thailand localization modules](../../../_images/modules2.png)

## Chart of accounts and taxes

Konvergo ERP’s fiscal localization package for Thailand includes the following taxes:

  * VAT 7%

  * VAT-exempted

  * Withholding tax

  * Withholding income tax

## Tax report

Konvergo ERP allows users to generate Excel files to submit their VAT to the **Revenue
Department** of Thailand.

### Sales and purchase tax report

To generate a sales and purchase tax report, go to Accounting ‣ Reporting ‣
Tax Report. Select a specific time or time range on the tax report, and click
**VAT-202-01 (xlsx)** for purchase tax and **VAT-202-02 (xlsx)** for sales
tax.

![Thai purchase and sales taxes reports](../../../_images/tax-report.png)

### Withholding PND tax report

PND report data displays the summarized amounts of the applicable
**withholding corporate income tax returns (domestic)** from vendor bills
under the **PND53 (TH)** and **PND3 (TH)** tax reports. It is installed by
default with the Thai localization.

![PND tax reports](../../../_images/pnd-report.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Withholding corporate income tax returns (domestic) is the tax used in case the company has
withheld the tax from “<b>Personal (PND3)</b>” or “<b>Corporate (PND53)</b>” services provided such as
rental, hiring, transportation, insurance, management fee, consulting, etc.</p>
</div>

The PND tax report allows users to generate a CSV file for bills to upload on
the [RDprep for Thailand e-Filling application](https://efiling.rd.go.th/rd-
cms/).

To generate a PND CSV file, go to Accounting ‣ Reporting ‣ Tax Report, select
a specific time or time range on the tax report, and click **PND3** or
**PND53**.

This generates the `Tax Report PND3.csv` and `Tax Report PND53.csv` files that
lists all the vendor bill lines with the applicable withholding tax.

![PND3 and PND53 CSV files](../../../_images/pnd3-pnd53.png)
<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>Konvergo ERP cannot generate the PND or PDF report or <b>withholding tax certificate</b> directly. The
generated <code>Tax Report PND3.csv</code> and <code>Tax Report PND53.csv</code> files must be exported
to an external tool to convert them into a <b>withholding PND</b> report or a <b>PDF</b> file.</p>
</div>

## Tax invoice

The **tax invoice PDF** report can be generated from Konvergo ERP through the
**Invoicing** module. Users have the option to print PDF reports for normal
invoices and tax invoices. To print out **tax invoices** , users can click on
**Print Invoices** in Konvergo ERP. Regular invoices can be printed as **commercial
invoices** by clicking on Cog button (⚙️) ‣ Print ‣ Commercial Invoice.

![Commercial invoice printing](../../../_images/tax-invoice.png)

### Headquarter/Branch number settings

You can inform a company’s **Headquarters** and **Branch number** in the
**Contacts** app. Once in the app, open the **contact form** of the company
and under the **Sales & Purchase** tab:

  * If the contact is identified as a branch, input the **Branch number** in the **Company ID** field.

  * If the contact is a **Headquarters** , leave the **Company ID** field **blank**.

![Company Headquarter/Branch number](../../../_images/contact.png)
<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>This information is used in the <b>tax invoice</b> PDF report and PND <b>tax report</b> export.</p>
</div>

