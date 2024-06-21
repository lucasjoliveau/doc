# Tax return (VAT declaration)

Companies with a registered VAT number must submit a **tax return** on a
monthly or quarterly basis, depending on their turnover and the registration
regulation. A tax return - or VAT return - gives the tax authorities
information about the taxable transactions made by the company. The **output
tax** is charged on the number of goods and services sold by a business, while
the **input tax** is the tax added to the price when goods or services are
purchased. Based on these values, the company can calculate the tax amount
they have to pay or be refunded.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>You can find additional information about VAT and its mechanism on this page from the European
Commission: <a href="https://ec.europa.eu/taxation_customs/business/vat/what-is-vat_en">“What is VAT?”</a>.</p>
</div>

## Prerequisites

### Tax Return Periodicity

The configuration of the **Tax Return Periodicity** allows Konvergo ERP to compute
your tax return correctly and also to send you a reminder to never miss a tax
return deadline.

To do so, go to Accounting ‣ Configuration ‣ Settings. Under the **Tax Return
Periodicity** , you can set:

  * **Periodicity** : define here whether you submit your tax return on a monthly or quarterly basis;

  * **Reminder** : define when Konvergo ERP should remind you to submit your tax return;

  * **Journal** : select the journal in which to record the tax return.

![Configure how often tax returns have to be made in Konvergo ERP
Accounting](../../../../_images/tax_return_periodicity.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This is usually configured during the <a href="../get_started">app’s initial set up</a>.</p>
</div>

### Tax Grids

Konvergo ERP generates tax reports based on the **Tax Grids** settings that are
configured on your taxes. Therefore, it is crucial to make sure that all
recorded transactions use the right taxes. You can see the **Tax Grids** by
opening the **Journal Items** tab of any invoice and bill.

![see which tax grids are used to record transactions in Konvergo ERP
Accounting](../../../../_images/tax_return_grids.png)

To configure your tax grids, go to Accounting ‣ Configuration ‣ Taxes, and
open the tax you want to modify. There, you can edit your tax settings, along
with the tax grids that are used to record invoices or credit notes.

![Configure taxes and their tax grids in Konvergo ERP
Accounting](../../../../_images/tax_return_taxes.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Taxes and reports are usually already pre-configured in Konvergo ERP: a <a href="../../fiscal_localizations#fiscal-localizations-packages"><span class="std std-ref">fiscal localization package</span></a> is installed according to the country you select at the creation
of your database.</p>
</div>

## Close a tax period

### Tax Lock Date

Any new transaction whose accounting date prior to the **Tax Lock Date** has
its tax values moved to the next open tax period. This is useful to make sure
that no change can be made to a report once its period is closed.

Therefore, we recommend locking your tax date before working on your **Closing
Journal Entry**. This way, other users cannot modify or add transactions that
would have an impact on the **Closing Journal Entry** , which can help you
avoid some tax declaration errors.

To check the current **Tax Lock Date** , or to edit it, go to Accounting ‣
Accounting ‣ Actions: Lock Dates.

![Lock your tax for a specific period in Konvergo ERP
Accounting](../../../../_images/tax_return_lock.png)

### Tax Report

Once all the transactions involving taxes have been posted for the period you
want to report, open your **Tax Report** by going to Accounting ‣ Reporting ‣
Audit Reports: Tax Report. Make sure to select the right period you want to
declare by using the date filter, this way you can have an overview of your
tax report. From this view, you can easily access different formats of your
tax report, such as `PDF` and XLSX. These include all the values to report to
the tax authorities, along with the amount you have to pay or be refunded.

![download the PDF with your Tax Report in Konvergo ERP
Accounting](../../../../_images/tax_return_report.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If you forgot to lock your tax date before clicking on <b>Closing Journal Entry</b>, then
Konvergo ERP automatically locks your fiscal period on the same date as the accounting date of your
entry. This safety mechanism can prevent some fiscal errors, but it is advised to lock your tax
date manually before, as described above.</p>
</div>
<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../taxes">Taxes</a></p></li>
<li><p><a href="../get_started">Get started</a></p></li>
<li><p><a href="../../fiscal_localizations">Fiscal localizations</a></p></li>
</ul>
</div>

  *[VAT]: Value Added Tax

