# Payment terms and installment plans

**Payment terms** specify all the conditions of a sale’s payment to help
ensure customers pay their invoices correctly and on time.

Payment terms are generally defined on documents such as sales orders,
customer invoices, and vendor bills. Payment terms cover:

  * The due date(s)

  * Early payment discounts

  * Any other conditions on the payment

An **installment plan** allows the customers to pay an invoice in parts, with
the amounts and payment dates defined beforehand by the seller.

<div class="alert alert-success">
<p class="alert-title">
Example</p><dl class="simple">
<dt>Immediate Payment</dt><dd><p>The full payment is due on the day of the invoice’s issuance.</p>
</dd>
<dt>15 Days (or Net 15)</dt><dd><p>The full payment is due 15 days after the invoice date.</p>
</dd>
<dt>21 MFI</dt><dd><p>The full payment is due by the 21st of the month following the invoice date.</p>
</dd>
<dt>30% Advance End of Following Month</dt><dd><p>30% is due on the day of the invoice’s issuance. The remaining balance is due at the end of the
following month.</p>
</dd>
<dt>2% 10, Net 30 EOM</dt><dd><p>A 2% <a href="cash_discounts">cash discount</a> if the payment is received within ten days.
Otherwise, the full payment is due at the end of the month following the invoice date.</p>
</dd>
</dl>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Payment terms are not to be confused with <a href="../../../sales/sales/invoicing/down_payment">down payment invoices</a>. If, for a specific order, you issue
multiple invoices to your customer, that is neither a payment term nor an installment plan but
an invoicing policy.</p></li>
<li><p>This page is about the <em>payment terms</em> feature, not <a href="terms_conditions">terms &amp; conditions</a>, which can be used to declare contractual obligations regarding content
use, return policies, and other policies surrounding the sale of goods and services.</p></li>
</ul>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="https://www.odoo.com/slides/slide/payment-terms-1679">Konvergo ERP Tutorials: payment terms</a></p></li>
<li><p><a href="cash_discounts">Cash discounts and tax reduction</a></p></li>
</ul>
</div>

## Configuration

To create new payment terms, follow these steps:

  1. Go to Accounting ‣ Configuration ‣ Payment Terms and click on **New**.

  2. Enter a name in the **Payment Terms** field. This field is the name displayed in the database and is not customer-facing.

  3. Enter the text to be displayed on the document (sales order, invoice, etc.) in the **Description on the Invoice** field.

  4. Tick the **Display terms on invoice** checkbox to display a breakdown of each payment and its due date on the invoice report, if desired.

  5. In the **Terms** section, add a set of rules (terms) to define what needs to be paid and by which due date(s). Defining terms automatically calculates the payments’ due date(s). This is particularly helpful for managing **installment plans** (payment terms with multiple terms).

To add a term, click on **Add a line** , define its **Due Type** and **Value**
, and fill out the appropriate fields to define when the term is due,
including any [discounts](cash_discounts). Due dates are calculated by
taking the invoice/bill date, first adding the **Months** , and then adding
the **Days**. If the **End of month** toggle is enabled, the due date will
then be the end of that month, plus any **Days after End of month**.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>To instead specify a number of days <em>before the end of the month</em>, use a negative value in the
<b>Days after End of month</b> field.</p>
</div>

To test that your payment terms are configured correctly, enter an invoice
amount and invoice date in the **Example** section to generate the payments
that would be due and their due dates using these payment terms.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><ul>
<li><p>Terms are computed in the order of their due dates.</p></li>
<li><p>The <b>balance</b> should always be used for the last line.</p></li>
</ul>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>In the following example, 30% is due on the day of issuance, and the balance is due at the end of
the following month.</p>
<img alt="Example of Payment Terms. The last line is the balance due on the 31st of the following month." src="../../../../_images/configuration.png"/>
</div>

## Using payment terms

Payment terms can be defined using the **Payment Terms** field on:

  * **Contacts:** To automatically set default payment terms on a contact’s new sales orders, invoices, and bills. This can be modified in the contact form, under the **Sales & Purchase** tab.

  * **Quotations/Sales Orders:** To set specific payment terms automatically on all invoices generated from a quotation or sales order.

Payment terms can be defined using the **Due Date** field, with the **Terms**
drop-down list on:

  * **Customer invoices:** To set specific payment terms on an invoice.

  * **Vendor bills:** To set specific payment terms on a bill.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Setting payment terms on a vendor bill is mostly useful for managing vendor terms with multiple
installments or cash discounts. Otherwise, manually setting the <b>due date</b> is enough. If
payment terms are already defined, empty the field to select a date.</p>
</div>

## Journal entries

Invoices with specific payment terms generate different _journal entries_ ,
with one _journal item_ for every computed _due date_.

This makes for easier [follow-ups](../payments/follow_up) and
[reconciliation](../bank/reconciliation) since Konvergo ERP takes each due date
into account, rather than just the balance due date. It also helps to get an
accurate [aged receivable report](../customer_invoices#customer-invoices-
aging-report).

<div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="The amount debited to the account receivable is split into two journal items with distinct due dates" src="../../../../_images/journal-entry.png"/>
<p>In this example, an invoice of $1000 has been issued with the following payment terms: <em>30% is
due on the day of issuance, and the balance is due at the end of the following month.</em></p>
<table class="table docutils">
<colgroup>
<col style="width: 42%"/>
<col style="width: 25%"/>
<col style="width: 17%"/>
<col style="width: 17%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Account</p></th>
<th class="head"><p>Due date</p></th>
<th class="head"><p>Debit</p></th>
<th class="head"><p>Credit</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Account Receivable</p></td>
<td><p>February 21</p></td>
<td><p>300</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>Account Receivable</p></td>
<td><p>March 31</p></td>
<td><p>700</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>Product Sales</p></td>
<td></td>
<td></td>
<td><p>1000</p></td>
</tr>
</tbody>
</table>
<p>The $1000 debited to the account receivable is split into two distinct journal items. Both of
them have their own due date.</p>
</div>

