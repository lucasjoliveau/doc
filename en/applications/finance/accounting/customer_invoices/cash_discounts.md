# Cash discounts and tax reduction

**Cash discounts** are reductions in the amount a customer must pay for goods
or services offered as an incentive for paying their invoice promptly. These
discounts are typically a percentage of the total invoice amount and are
applied if the customer pays within a specified time. Cash discounts can help
the company maintain a steady cash flow.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>You issue a €100 invoice on the 1st of January. The full payment is due within 30 days, and you
also offer a 2% discount if your customer pays you within seven days.</p>
<p>The customer can pay €98 up to the 8th of January. After that date, they would have to pay €100
by the 31st of January.</p>
</div>

A tax reduction can also be applied depending on the country or region.

## Configuration

To grant cash discounts to customers, you must first set up the type of tax
reduction, verify the gain and loss accounts, and configure new payment terms.

### Tax reductions

Depending on the country or region, the base amount used to compute the tax
can vary, which can lead to a **tax reduction**.

To configure how the tax reduction is applied, go to Accounting ‣
Configuration ‣ Settings, and in the **Taxes** section, in the **Cash Discount
Tax Reduction** feature, select one of the three following options:

Always (upon invoice)

    

The tax is always reduced. The base amount used to compute the tax is the
discounted amount, whether the customer benefits from the discount or not.

On early payment

    

The tax is reduced only if the customer pays early. The base amount used to
compute the tax is the same as the sale: if the customer benefits from the
reduction, then the tax is reduced. This means that, depending on the
customer, the tax amount can vary after the invoice is issued.

Never

    

The tax is never reduced. The base amount used to compute the tax is the full
amount, whether the customer benefits from the discount or not.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>You issue a €100 invoice (tax-excluded) on the 1st of January, with a 21% tax rate. The full
payment is due within 30 days, and you also offer a 2% discount if your customer pays you within
seven days.</p>
<div class="sphinx-tabs docutils container">
<div aria-label="Tabbed content" role="tablist"><button aria-controls="panel-0-0-0" aria-selected="true" class="sphinx-tabs-tab" id="tab-0-0-0" name="0-0" role="tab" tabindex="0">Always (upon invoice)</button><button aria-controls="panel-0-0-1" aria-selected="false" class="sphinx-tabs-tab" id="tab-0-0-1" name="0-1" role="tab" tabindex="-1">On early payment</button><button aria-controls="panel-0-0-2" aria-selected="false" class="sphinx-tabs-tab" id="tab-0-0-2" name="0-2" role="tab" tabindex="-1">Never</button></div><div aria-labelledby="tab-0-0-0" class="sphinx-tabs-panel" id="panel-0-0-0" name="0-0" role="tabpanel" tabindex="0"><table class="table docutils">
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Due date</p></th>
<th class="head"><p>Total amount due</p></th>
<th class="head"><p>Computation</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>8th of January</p></td>
<td><p>€118.58</p></td>
<td><p>(€98 + (21% of €98))</p></td>
</tr>
<tr class="row-odd"><td><p>31st of January</p></td>
<td><p>€120.58</p></td>
<td><p>(€100 + (21% of €98))</p></td>
</tr>
</tbody>
</table>
</div><div aria-labelledby="tab-0-0-1" class="sphinx-tabs-panel" hidden="true" id="panel-0-0-1" name="0-1" role="tabpanel" tabindex="0"><table class="table docutils">
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Due date</p></th>
<th class="head"><p>Total amount due</p></th>
<th class="head"><p>Computation</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>8th of January</p></td>
<td><p>€118.58</p></td>
<td><p>(€98 + (21% of €98))</p></td>
</tr>
<tr class="row-odd"><td><p>31st of January</p></td>
<td><p>€121.00</p></td>
<td><p>(€100 + (21% of €100))</p></td>
</tr>
</tbody>
</table>
</div><div aria-labelledby="tab-0-0-2" class="sphinx-tabs-panel" hidden="true" id="panel-0-0-2" name="0-2" role="tabpanel" tabindex="0"><table class="table docutils">
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Due date</p></th>
<th class="head"><p>Total amount due</p></th>
<th class="head"><p>Computation</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>8th of January</p></td>
<td><p>€119.00</p></td>
<td><p>(€98 + (21% of €100))</p></td>
</tr>
<tr class="row-odd"><td><p>31st of January</p></td>
<td><p>€121.00</p></td>
<td><p>(€100 + (21% of €100))</p></td>
</tr>
</tbody>
</table>
</div></div>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p><a href="../reporting/tax_returns#tax-returns-tax-grids"><span class="std std-ref">Tax grids</span></a>, which are used for the tax report, are correctly
computed according to the <a href="#cash-discounts-tax-reductions"><span class="std std-ref">type of tax reduction</span></a> you
configured.</p></li>
<li><p>The <b>type of cash discount tax reduction</b> may be correctly pre-configured, depending on your
<a href="../../fiscal_localizations#fiscal-localizations-packages"><span class="std std-ref">fiscal localization package</span></a>.</p></li>
</ul>
</div>

### Cash discount gain/loss accounts

With a cash discount, the amount you earn depends on whether the customer
benefits from the cash discount or not. This inevitably leads to gains and
losses, which are recorded on default accounts.

To modify these accounts, go to Accounting ‣ Configuration ‣ Settings, and in
the **Default Accounts** section, select the accounts you want to use for the
**Cash Discount Gain account** and **Cash Discount Loss account**.

### Payment terms

Cash discounts are defined on [payment terms](payment_terms). Configure
them to your liking by going to Accounting ‣ Configuration ‣ Payment Terms,
and make sure to fill out the fields **Discount %** and **Discount Days**.

![Configuration of payment terms named "2/7 Net 30". The field "Description on
Invoices" reads: "Payment terms: 30 Days, 2% Early Payment Discount under 7
days".](../../../../_images/payment-terms.png) <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="payment_terms">Payment terms and installment plans</a></p>
</div>

## Apply a cash discount to a customer invoice

Apply a cash discount to a customer invoice by selecting the payment terms you
created. Konvergo ERP automatically computes the correct amounts, tax amounts, due
dates, and accounting records.

Under the **Journal Items** tab, you can display the discount details by
clicking on the “toggle” button and adding the **Discount Date** and
**Discount Amount** columns.

![An invoice of €100.00 with "2/7 Net 30" selected as payment terms. The
"Journal Items" tab is open, and the "Discount Date" and "Discount Amount"
columns are displayed.](../../../../_images/invoice-journal-entry.png)

The discount amount and due date are also displayed on the generated invoice
sent to the customer.

![An invoice of €100.00 with the following text added to the terms and
conditions: "30 Days, 2% Early Payment Discount under 7 days. 118.58 € due if
paid before 01/08/2023."](../../../../_images/invoice-print.png)

### Payment reconciliation

When you record a payment or reconcile your bank statements, Konvergo ERP takes the
customer payment’s date into account to define if they can benefit from the
cash discount or not.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If your customer pays the discount amount <em>after</em> the discount date, you can always decide
whether to mark the invoice as fully paid with a write-off or as partially paid.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../payments">Payments</a></p>
</div>

