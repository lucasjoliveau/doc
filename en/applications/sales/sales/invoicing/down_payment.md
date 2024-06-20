# Down payments

A down payment is a partial payment made by the buyer when a sales contract is
concluded. This implies both parties’ (seller and buyer) full commitment to
honor the contract.

With a down payment, the buyer pays a portion of the total amount owed while
agreeing to pay the remaining amount at a later date. In turn, the seller
provides goods or services to the buyer after accepting the down payment,
trusting that the remaining amount will be paid later on.

## Create invoices

When a sales order is confirmed, the option to create an invoice becomes
available, via the Create Invoice button, located in the upper-left corner of
the sales order form. When clicked, a Create invoices pop-up appears.

![Create invoices pop-up form that appears in Odoo
Sales.](../../../../_images/create-invoices-popup-form.png)

Note

Invoices are automatically created as drafts, so they can be reviewed before
validation.

On the Create invoices pop-up, there are 3 options to choose from in the
Create Invoice field:

  * Regular invoice

  * Down payment (percentage)

  * Down payment (fixed amount)

Note

If Regular Invoice is selected, the other fields disappear, as they only
pertain to down payment configurations.

## Initial down payment request

On the Create invoices pop-up form, the down payment options are:

  * Down payment (percentage)

  * Down payment (fixed amount)

Once the desired down payment option is selected in the Create Invoice field
on the pop-up form, designate the desired amount, either as a percentage or a
fixed amount, in the Down Payment Amount field.

Then, select the appropriate income account for the invoice in the Income
Account field. Next, select a tax amount, if necessary, in the Customer Taxes
drop-down field.

![A create invoices pop-up form with down payment fields filled in with
information.](../../../../_images/create-invoices-popup-form-filled-out.png)

Once all fields are filled in with the desired information, click the Create
Draft Invoice button. Upon clicking this button, Odoo reveals the Customer
Invoice Draft.

In the Invoice Lines tab of the Customer Invoice Draft, the down payment that
was just configured in the Create invoices pop-up form appears as a Product.

![Down payment as a product in the invoice lines tab of a customer invoice
draft in Odoo.](../../../../_images/down-payment-product-inv-draft.png)

Note

When the Down payment product in the Invoice Lines tab is clicked, Odoo
reveals the product form for the down payment.

By default, the Product Type of down payment products generated for invoices
are set as Service, with the Invoicing Policy set to Prepaid/Fixed Price.

![Down payment product form with service product type and invoicing policy
field.](../../../../_images/down-payment-product.png)

This product can be edited/modified at any time.

Warning

If Based on Delivered Quantity (Manual) is chosen as the Invoicing Policy, an
invoice will **not** be able to be created.

## Example: request 50% down payment

Note

The following example involves a 50% amount down payment on a product (Cabinet
with Doors) with Ordered quantities as the Invoicing Policy.

![Cabinet with doors product form showcasing various details and
fields.](../../../../_images/cabinet-product-details.png)

See also

[Invoice based on delivered or ordered quantities](invoicing_policy.html)

First, navigate to Sales app ‣ New, and add a Customer to the quotation.

Then, click Add a product in the Order Lines tab, and select the Cabinet with
Doors product.

When the order is confirmed (via the Confirm button), the quotation turns into
a sales order. Once this occurs, create and view the invoice by clicking
Create Invoice.

![Cabinet with doors sales order that's been confirmed in the Odoo Sales
application.](../../../../_images/cabinet-sales-orders-confirmed.png)

Next, on the Create invoices pop-up window that appears, select Down payment
(percentage), and type `50` in the Down Payment Amount field.

Note

The Income Account and Customer Taxes fields are _not_ required fields, and
they will _not_ appear if they’ve already been preconfigured in previous down
payment requests.

For more information, check out the documentation on customer taxes
modification on down payments and income account modification on down
payments.

Lastly, click Create Draft Invoice to create and view the invoice draft.

Clicking Create Draft Invoice reveals the draft invoice, which includes the
down payment as a Product in the Invoice Lines tab.

From there, the invoice can be confirmed and posted by clicking Confirm.
Confirming the invoice changes the status from Draft to Posted. It also
reveals a new series of buttons at the top of the page.

![A sample draft invoice with down payment mentioned in Odoo
Sales.](../../../../_images/draft-invoice-sample.png)

From those buttons, the payment can be registered by clicking Register
Payment.

![Showcase of the Register Payment button on a confirmed customer
invoice.](../../../../_images/register-payment-button.png)

Doing so reveals a Register Payment pop-up form, which is auto-populated with
the necessary information. Confirm the information provided is correct and
make any necessary adjustments. When ready, click the Create Payment button.

![Showcase of the Register Payment pop-up window with create payment
button.](../../../../_images/register-payment-pop-up-window.png)

After clicking Create Payment, Odoo reveals the customer invoice, now with a
green In Payment banner in the upper-right corner.

![Customer Invoice with a green In Payment banner located in the upper-right
corner.](../../../../_images/customer-invoice-green-payment-banner.png)

Now, when the customer wants to pay the remaining amount of the order, another
invoice must be created. To do that, return to the sales order, via the
breadcrumb links.

Back on the sales order, a new Down Payments section is present in the Order
Lines tab, along with the down payment that was just invoiced and posted.

![The down payments section in the order lines tab of a sales
order.](../../../../_images/down-payments-section-order-lines.png)

Next, click the Create Invoice button.

On the Create invoices pop-up window that appears, there are two new fields:
Already invoiced and Amount to invoice.

![The deduct down payment option on the create invoices pop up in Odoo
Sales.](../../../../_images/create-invoices-pop-up-already-invoiced.png)

If the remaining amount is ready to be paid, select the Regular Invoice
option. Odoo will create an invoice for the exact amount needed to complete
the total payment, as indicated in the Amount to invoice field.

Once ready, click Create Draft Invoice.

Doing so reveals another Customer Invoice Draft page, listing _all_ the
invoices for that specific sales order in the Invoice Lines tab. Each invoice
line item displays all the necessary information related to each invoice.

To complete the flow, click Confirm, which changes the status of the invoice
from Draft to Posted. Then, click Register Payment.

Once again, the Register Payment appears, with all fields auto-populated with
the necessary information, including the remaining amount left to be paid on
the order.

![The second register payment pop-up form in Odoo
sales.](../../../../_images/second-register-payment-popup.png)

After confirming that information, click Create Payment. Doing so reveals the
final Customer Invoice with a green In Payment banner in the upper-right
corner. Also, both down payments are present in the Invoice Lines tab.

![The second down payment invoice with in payment banner in Odoo
Sales.](../../../../_images/second-down-payment-in-payment-invoice.png)

At this point, the flow is now complete.

Note

This flow is also possible with the Fixed amount down payment option.

Important

If a down payment is used with a product that has a Delivered quantities
invoicing policy, the down payments will **not** be able to be deducted when
it comes time to invoice the customer.

This is because, due to the invoicing policy, the product(s) would have to be
delivered _before_ creating the final invoice.

If nothing has been delivered, a Credit Note is created, which cancels the
draft invoice that was created after the down payment.

To utilize the Credit Note option, the _Inventory_ application must be
installed, in order to confirm the delivery. Otherwise, the delivered quantity
can be entered manually directly on the sales order.

## Customer taxes modification on down payments

To adjust the income account and customer taxes attached to a down payment,
navigate to the Products page (Sales app ‣ Products ‣ Products), search for
the `Down Payment` product in the search bar, and select it to reveal the
product detail page.

On the Down Payment product page, in the General Information tab, the customer
taxes can be modified in the Customer Taxes field.

![How to modify the income account link to down
payments.](../../../../_images/customer-taxes-field.png)

## Income account modification on down payments

To change or adjust the income account attached to the Down Payment product
page, the _Accounting_ app **must** be installed.

With the _Accounting_ app installed, the Accounting tab becomes available on
the product page. That tab will **not** be accessible without the _Accounting_
app installed.

In the Accounting tab, the income account can be changed in the Income Account
field, located in the Receivables section.

![How to modify the income account link to down
payments.](../../../../_images/income-account.png)

See also

[Invoice based on delivered or ordered quantities](invoicing_policy.html)

