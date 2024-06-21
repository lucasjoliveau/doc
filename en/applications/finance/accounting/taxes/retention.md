# Withholding taxes

A withholding tax, also called a retention tax, is a government requirement
for the payer of a customer invoice to withhold or deduct tax from the
payment, and pay that tax to the government. In most jurisdictions,
withholding tax applies to employment income.

With normal taxes, the tax is added to the subtotal to give you the total to
pay. As opposed to normal taxes, withholding taxes are deducted from the
amount to pay, as the tax will be paid by the customer.

As, an example, in Colombia you may have the following invoice:

![../../../../_images/retention03.png](../../../../_images/retention03.png)

In this example, the **company** who sent the invoice owes $20 of taxes to the
**government** and the **customer** owes $10 of taxes to the **government**.

## Configuration

In Konvergo ERP, a withholding tax is defined by creating a negative tax. For a
retention of 10%, you would configure the following tax (accessible through
Configuration ‣ Taxes):

![../../../../_images/retention04.png](../../../../_images/retention04.png)

In order to make it appear as a retention on the invoice, you should set a
specific tax group **Retention** on your tax, in the **Advanced Options** tab.

![../../../../_images/retention02.png](../../../../_images/retention02.png)

Once the tax is defined, you can use it in your products, sales order or
invoices.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If the retention is a percentage of a regular tax, create a Tax with a
<b>Tax Computation</b> as a <b>Tax Group</b> and set the two taxes in this group
(normal tax and retention).</p>
</div>

## Applying retention taxes on invoices

Once your tax is created, you can use it on customer forms, sales order or
customer invoices. You can apply several taxes on a single customer invoice
line.

![../../../../_images/retention01.png](../../../../_images/retention01.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When you see the customer invoice on the screen, you get only a
<b>Taxes line</b> summarizing all the taxes (normal taxes &amp; retentions).
But when you print or send the invoice, Konvergo ERP does the correct
grouping amongst all the taxes.</p>
</div>

The printed invoice will show the different amounts in each tax group.

![../../../../_images/retention03.png](../../../../_images/retention03.png)
<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../taxes">Taxes</a></p></li>
</ul>
</div>

