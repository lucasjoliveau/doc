# Order handling

When a customer orders on your eCommerce, there are **three** record types
required to be handle in Odoo:

  * Sales orders;

  * Delivery orders;

  * Invoices & legal requirements.

## Sales orders

### Order and payment status

The first step when a customer adds a product to his cart is the creation of a
quotation. Orders can be managed either from the **Website** or
[Sales](../../../sales/sales.html) app. eCommerce orders can automatically be
assigned to a specific sales team by going to Website ‣ Configuration ‣
Settings. In the **Shop - Checkout Process** section, select a Sales Team or
Salesperson to handle eCommerce orders.

![Assignment of online orders to a sales team or
salesperson](../../../../_images/handling-salesteam.png)

Orders can be found under Website ‣ eCommerce ‣ Orders/Unpaid Orders. Each
order goes through a different status:

  * **Quotation** : a new product is added to the cart, but the customer has _not_ gone through the checkout process yet;

  * **Quotation sent** : the customer has gone through the checkout process and confirmed the order, but the payment is not yet confirmed;

  * **Order** : the customer has gone through the checkout process, confirmed the order, and the payment is received.

![Statuses of eCommerce orders](../../../../_images/handling-status.png)

### Abandoned cart

An **abandoned cart** represents an order for which the customer did **not
finish** the checkout confirmation process. For these orders, it is possible
to send an **email reminder** to the customer automatically. To enable that
feature, go to Website ‣ Configuration ‣ Settings and in the Email & Marketing
section, enable Automatically send abandoned checkout emails. Once enabled,
you can set the **time-lapse** after which the email is sent and customize the
**email template** used.

Note

For abandoned cart emails, the customer must either have entered their contact
details during the checkout process; or be logged-in when they added the
product to their cart.

## Delivery orders

### Delivery flow

Once a quotation has been confirmed, a delivery order is automatically
created. The next step is to process this delivery.

Packing eCommerce orders usually requires picking the product, preparing the
packaging, printing the shipping label(s) and shipping to the customer.
Depending on the number of orders, strategy, or resources, those steps can be
considered as one or multiple actions in Odoo.

An automatic email can be sent to the customer when the transfer status in
Odoo is “done”. To do so, enable the feature in the settings of the
[Inventory](../../../inventory_and_mrp/inventory.html) app.

Note

If customers are allowed to pay when picking up their order in stores or by
wire transfer, the quotation is **not** be confirmed and the stock is **not**
be reserved. Orders must be confirmed manually to reserve products in stock.

See also

  * [Shipping cost invoicing](../../../inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/invoicing.html)

  * [Print shipping labels](../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/labels.html)

  * [Multi-package shipments](../../../inventory_and_mrp/inventory/shipping_receiving/advanced_operations_shipping/multipack.html)

### Returns and refunds

Customers can only return an order through an online form. It may not be
possible to return products depending on the return strategy or type of
product.

Full refunds can be directly sent to customers from within the order
interface. A refund-compatible payment provider needs to be enabled first.

See also

  * [Returns and refunds](../../../sales/sales/products_prices/returns.html)

  * [After-Sales services](../../../services/helpdesk/advanced/after_sales.html)

  * [Online payments](../../../finance/payment_providers.html)

## Invoice and legal requirements

The final step of an ecommerce order is to generate the invoice and send it to
the customer. Depending on the type of business (B2B or B2C), an invoice can
either be generated automatically (B2B) or on demand of the customer (B2C).
This process can be automated if (and when) the online payment is confirmed.

To automate invoicing, go to Website ‣ Configuration ‣ Settings and in the
Invoicing section, enable Automatic Invoice.

