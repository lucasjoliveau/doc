# Philippines

## Configuration

[Install](../../general/apps_modules#general-install) the **🇵🇭
Philippines** [fiscal localization
package](../fiscal_localizations#fiscal-localizations-packages) to get
all the default accounting features of the Philippine localization, such as a
chart of accounts, taxes, and the BIR 2307 report. These provide a base
template to get started with using Philippine accounting.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>When creating a new database and selecting the <code>Philippines</code> as a country, the fiscal
localization module <b>Philippines - Accounting</b> is automatically installed.</p></li>
<li><p>If the module is installed in an existing company, the <b>chart of accounts</b> and <b>taxes</b> will
<em>not</em> be replaced if there are already posted journal entries.</p></li>
<li><p>The BIR 2307 report is installed, but the withholding taxes may need to be manually created.</p></li>
</ul>
</div>

### Chart of accounts and taxes

A minimum configuration default chart of accounts is installed, and the
following types of taxes are installed and linked to the relevant account:

  * VAT 12%

  * VAT Exempt

  * Withholding taxes

For the withholding taxes (Configuration ‣ Taxes), there is an additional
**Philippines ATC** field under the **Philippines** tab.

![Philippines ATC code field set on taxes.](../../../_images/philippines-atc-
code.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Taxes’ ATC codes are used for the BIR 2307 report. If a tax is created manually, its ATC code
must be added.</p>
</div>

### Contacts

When a company or an individual (not belonging to a company) contact is
located in the Philippines, fill in the **Tax ID** field with their `Taxpayer
Identification Number (TIN)`.

For individuals not belonging to a company, identify them by using the
following additional fields:

  * **First Name**

  * **Middle Name**

  * **Last Name**

![Individual type contact with First, Middle, and Last Name
fields.](../../../_images/philippines-contact-individual.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>For both <b>Company</b> and <b>Individual</b>, the TIN should follow the
<code>NNN-NNN-NNN-NNNNN</code> format. The branch code should follow the last digits of the TIN, or else it
can be left as <code>00000</code>.</p>
</div>

## BIR 2307 report

**BIR 2307** report data, also known as [Certificate of Creditable Tax
Withheld at Source](https://www.bir.gov.ph/index.php/bir-
forms/certificates), can be generated for purchase orders and vendor
payments with the applicable withholding taxes.

To generate a BIR 2307 report, select one or multiple vendor bills from the
list view, and click Action ‣ Download BIR 2307 XLS.

![Multiple vendor bills selected with action to "Download BIR 2307
XLS".](../../../_images/philippines-multi-bill.png) <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>The same action can be performed on a vendor bill from the form view.</p>
</div>

A pop-up appears to review the selection, then click on **Generate**.

![Pop up menu to generate BIR 2307 XLS file.](../../../_images/philippines-
generate.png)

This generates the `Form_2307.xls` file that lists all the vendor bill lines
with the applicable withholding tax.

The process above can also be used for a _single_ vendor
[payment](../accounting/payments) if it is linked to one or more [vendor
bills](../accounting/payments) with applied withholding taxes.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>If no withholding tax is applied, then the XLS file will not generate records for those vendor
bill lines.</p></li>
<li><p>When grouping payments for multiple bills, Konvergo ERP splits the payments based on the contact. From
a payment, clicking Action ‣ Download BIR 2307 XLS generates a report that
only includes vendor bills related to that contact.</p></li>
</ul>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Konvergo ERP cannot generate the BIR 2307 PDF report or DAT files directly. The generated
<code>Form_2307.xls</code> file can be exported to an <em>external</em> tool to convert it to BIR DAT or PDF
format.</p>
</div>

