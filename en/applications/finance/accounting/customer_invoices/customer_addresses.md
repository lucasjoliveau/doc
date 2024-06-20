# Delivery and invoice addresses

Companies often have multiple locations, and it is common that a customer
invoice should be sent to one address and the delivery should be sent to
another. Odoo’s **Customer Addresses** feature is designed to handle this
scenario by making it easy to specify which address to use for each case.

See also

[Invoicing processes](overview.html)

## Configuration

To specify a sales order’s invoice and delivery addresses, first go to
Accounting ‣ Configuration ‣ Settings. In the Customer Invoices section,
enable Customer Addresses and click Save.

On quotations and sales orders, there are now fields for Invoice Address and
Delivery Address. If the customer has an invoice or delivery address listed on
their contact record, the corresponding field will use that address by
default, but any contact’s address can be used instead.

## Invoice and deliver to different addresses

Delivery orders and their delivery slip reports use the address set as the
Delivery Address on the sales order. By default, invoice reports show both the
shipping address and the invoice address to assure the customer that the
delivery is going to the correct location.

Emails also go to different addresses. The quotation and sales order are sent
to the main contact’s email, as usual, but the invoice is sent to the email of
the address set as the Invoice Address on the sales order.

Note

  * Reports, such as the delivery slip and invoice report, can be [customized using Studio](../../../studio/pdf_reports.html).

  * If [Send by Post](snailmail.html) is checked when you click Send & Print, the invoice will be mailed to the invoice address.

