# Cash discounts and tax reduction

**Cash discounts** are reductions in the amount a customer must pay for goods
or services offered as an incentive for paying their invoice promptly. These
discounts are typically a percentage of the total invoice amount and are
applied if the customer pays within a specified time. Cash discounts can help
the company maintain a steady cash flow.

Example

You issue a €100 invoice on the 1st of January. The full payment is due within
30 days, and you also offer a 2% discount if your customer pays you within
seven days.

The customer can pay €98 up to the 8th of January. After that date, they would
have to pay €100 by the 31st of January.

A tax reduction can also be applied depending on the country or region.

## Configuration

To grant cash discounts to customers, you must first set up the type of tax
reduction, verify the gain and loss accounts, and configure new payment terms.

### Tax reductions

Depending on the country or region, the base amount used to compute the tax
can vary, which can lead to a **tax reduction**.

To configure how the tax reduction is applied, go to Accounting ‣
Configuration ‣ Settings, and in the Taxes section, in the Cash Discount Tax
Reduction feature, select one of the three following options:

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

Example

You issue a €100 invoice (tax-excluded) on the 1st of January, with a 21% tax
rate. The full payment is due within 30 days, and you also offer a 2% discount
if your customer pays you within seven days.

Always (upon invoice)On early paymentNever

Due date | Total amount due | Computation  
---|---|---  
8th of January | €118.58 | (€98 + (21% of €98))  
31st of January | €120.58 | (€100 + (21% of €98))  
  
Due date | Total amount due | Computation  
---|---|---  
8th of January | €118.58 | (€98 + (21% of €98))  
31st of January | €121.00 | (€100 + (21% of €100))  
  
Due date | Total amount due | Computation  
---|---|---  
8th of January | €119.00 | (€98 + (21% of €100))  
31st of January | €121.00 | (€100 + (21% of €100))  
  
Note

  * [Tax grids](../reporting/tax_returns.html#tax-returns-tax-grids), which are used for the tax report, are correctly computed according to the type of tax reduction you configured.

  * The **type of cash discount tax reduction** may be correctly pre-configured, depending on your [fiscal localization package](../../fiscal_localizations.html#fiscal-localizations-packages).

### Cash discount gain/loss accounts

With a cash discount, the amount you earn depends on whether the customer
benefits from the cash discount or not. This inevitably leads to gains and
losses, which are recorded on default accounts.

To modify these accounts, go to Accounting ‣ Configuration ‣ Settings, and in
the Default Accounts section, select the accounts you want to use for the Cash
Discount Gain account and Cash Discount Loss account.

### Payment terms

Cash discounts are defined on [payment terms](payment_terms.html). Configure
them to your liking by going to Accounting ‣ Configuration ‣ Payment Terms,
and make sure to fill out the fields Discount % and Discount Days.

![Configuration of payment terms named "2/7 Net 30". The field "Description on
Invoices" reads: "Payment terms: 30 Days, 2% Early Payment Discount under 7
days".](../../../../_images/payment-terms.png)

See also

[Payment terms and installment plans](payment_terms.html)

## Apply a cash discount to a customer invoice

Apply a cash discount to a customer invoice by selecting the payment terms you
created. Odoo automatically computes the correct amounts, tax amounts, due
dates, and accounting records.

Under the Journal Items tab, you can display the discount details by clicking
on the “toggle” button and adding the Discount Date and Discount Amount
columns.

![An invoice of €100.00 with "2/7 Net 30" selected as payment terms. The
"Journal Items" tab is open, and the "Discount Date" and "Discount Amount"
columns are displayed.](../../../../_images/invoice-journal-entry.png)

The discount amount and due date are also displayed on the generated invoice
sent to the customer.

![An invoice of €100.00 with the following text added to the terms and
conditions: "30 Days, 2% Early Payment Discount under 7 days. 118.58 € due if
paid before 01/08/2023."](../../../../_images/invoice-print.png)

### Payment reconciliation

When you record a payment or reconcile your bank statements, Odoo takes the
customer payment’s date into account to define if they can benefit from the
cash discount or not.

Note

If your customer pays the discount amount _after_ the discount date, you can
always decide whether to mark the invoice as fully paid with a write-off or as
partially paid.

See also

[Payments](../payments.html)

