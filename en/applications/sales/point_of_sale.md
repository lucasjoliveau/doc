# Point of Sale

With **Konvergo ERP Point of Sale** , run your shops and restaurants easily. The app
works on any device with a web browser, even if you are temporarily offline.
Product moves are automatically registered in your stock, you get real-time
statistics, and your data is consolidated across all shops.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="https://www.odoo.com/slides/point-of-sale-28">Konvergo ERP Tutorials: Point of Sale Tutorials</a></p></li>
<li><p><a href="../general/iot">IoT Boxes Documentations</a></p></li>
</ul>
</div>

## Start a session

From the **POS dashboard** , click **New Session** , and at the **Opening Cash
Control** screen, click **Open Session** to start a POS session, or click
**Continue Selling** if the session is already opened.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><a href="point_of_sale/employee_login">Multiple users</a> can be logged into the same session at the
same time. However, the session can only be opened once on the same browser.</p>
</div>

## Sell products

Click on products to add them to the cart. To change the **quantity** , click
**Qty** and enter the number of products using the keypad. To add a
**discount** or modify the product **price** , click respectively **% Disc**
or **Price** and enter the amounts.

Once an order is completed, proceed to checkout by clicking **Payment**.
Select the **payment method** , enter the received amount, and click
**Validate**. Click **New Order** to move on to the next customer.

![POS session interface.](../../_images/pos-interface.png) <div class="alert alert-info">
<p class="alert-title">
Tip</p><ul>
<li><p>You can use both <code>,</code> and <code>.</code> on your keyboard as decimal separators.</p></li>
<li><p><b>Cash</b> is selected by default if you enter the amount without choosing a payment method.</p></li>
</ul>
</div>
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The system can only load a limited number of products for effective opening. Click
<b>Search more</b> if the desired product is not loaded automatically.</p>
</div>

## Set customers

Registering your customer is necessary to [collect their loyalty points and
grant them rewards](point_of_sale/pricing/loyalty), automatically apply
the [attributed pricelist](point_of_sale/pricing/pricelists), or
[generate and print an invoice](point_of_sale/receipts_invoices#receipts-
invoices-invoices).

You can create customers from an open POS session by clicking Customer ‣
Create, and filling in the contact information. You can also create customers
from the backend by going to Point of Sale ‣ Orders ‣ Customers and clicking
**New**. Then, fill in the information and save.

To set a customer during an order, access the list of customers by clicking
**Customer** on the POS interface. You can also set a customer at the payment
screen by clicking **Customer**.

## Customer notes

You can add **customer notes** about specific products directly from an open
POS session. For instance, to provide cleaning and maintenance tips. They can
also be used to track a customer’s particular request, such as not wanting the
product to be assembled for them.

To do so, select a product and click **Customer Note** on the pad. Doing so
opens a pop-up window in which you can add or modify content for the note.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Product notes from an <a href="point_of_sale/shop/sales_order">imported SO</a> are displayed
identically in the cart.</p>
</div> ![Customer note button and notes \(SO and POS session\) on
products in the cart](../../_images/customer-notes.png)

Customer notes appear on customers’ receipts and invoices similarly to how
they appear in the cart, under the related product.

![Customer receipt with notes from an SO and from the customer note
feature](../../_images/notes-receipt.png)

## Return and refund products

To return and refund a product,

  1. start a session from the **POS dashboard** ;

  2. click **Refund** and select the corresponding order;

  3. select the product and the quantity to refund using the keypad;

  4. click **Refund** to go back to the previous screen;

  5. once the order is completed, click **Payment** to proceed to the refund;

  6. click **Validate** and **New Order** to move on to the next customer.

![refund view from a POS](../../_images/refund.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>You can filter the <b>orders list</b> by <b>Receipt Number</b>, <b>Date</b> or
<b>Customer</b> using the search bar.</p></li>
<li><p>You can also refund a product by selecting the returned product from an open session, and
setting a negative quantity that equals the number of returned products. To do so, click
<b>Qty</b> and <b>+/-</b>, followed by the quantity of returned products.</p></li>
</ul>
</div>

## Close the POS session

To close your session, click **Close** in the upper right corner of your
screen; doing so opens the **Closing Control** pop-up screen. From this
screen, you can retrieve various information:

  * the number of orders made and the total amount made during the session;

  * the expected amounts grouped by payment method.

Before closing this window, count your cash using the calculator icon. Doing
so opens a pop-up window that computes the total amount in the cash drawer
depending on the coins and bills counted and added manually. Then, click
**Confirm** or **Discard** to close the window. The computed amount is set in
the **Counted** column, and the **Money Details** are specified in the
**Notes** section.

![How to close a POS session.](../../_images/closing-control.png)

Once you are done controlling the amounts, click **Close Session** to close
and go back to the **POS dashboard**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>You can let the session open by clicking <b>Backend</b> or abort and keep selling by
clicking <b>Discard</b>.</p></li>
<li><p>Depending on your setup, you might only be allowed to close a session if the expected cash
revenue equals the counted cash. To close it anyway, click <b>Ok</b> on the
<b>Payments Difference</b> screen.</p></li>
</ul>
</div> <div class="alert alert-info">
<p class="alert-title">
Tip</p><ul>
<li><p>It is strongly advised to close your POS session at the end of each day.</p></li>
<li><p>To look at all your previous sessions, go to Point of Sale ‣ Orders ‣
Sessions.</p></li>
</ul>
</div>

  * [Multi-employee management](point_of_sale/employee_login)
  * [Receipts and invoices](point_of_sale/receipts_invoices)
  * [Configuration](point_of_sale/configuration)
    * [ePOS printers](point_of_sale/configuration/epos_printers)
    * [Secure connection (HTTPS)](point_of_sale/configuration/https)
    * [Self-signed certificate for ePOS printers](point_of_sale/configuration/epos_ssc)
  * Shop features
    * [Sales orders](point_of_sale/shop/sales_order)
    * [Barcodes](point_of_sale/shop/barcode)
    * [Serial numbers and lots](point_of_sale/shop/serial_numbers)
    * [Ship later](point_of_sale/shop/ship_later)
    * [Customer display](point_of_sale/shop/customer_display)
  * [Restaurant features](point_of_sale/restaurant)
    * [Bills](point_of_sale/restaurant/bill_printing)
    * [Floors and tables management](point_of_sale/restaurant/floors_tables)
    * [Orders printing](point_of_sale/restaurant/kitchen_printing)
    * [Tips](point_of_sale/restaurant/tips)
  * Pricing features
    * [Discounts](point_of_sale/pricing/discounts)
    * [Discount tags (barcode scanner)](point_of_sale/pricing/discount_tags)
    * [Loyalty programs](point_of_sale/pricing/loyalty)
    * [Pricelists](point_of_sale/pricing/pricelists)
    * [Flexible taxes (fiscal positions)](point_of_sale/pricing/fiscal_position)
    * [Cash rounding](point_of_sale/pricing/cash_rounding)
  * [Payment methods](point_of_sale/payment_methods)
    * [Payment terminals](point_of_sale/payment_methods/terminals)
      * [Adyen](point_of_sale/payment_methods/terminals/adyen)
      * [Ingenico](point_of_sale/payment_methods/terminals/ingenico)
      * [SIX](point_of_sale/payment_methods/terminals/six)
      * [Stripe](point_of_sale/payment_methods/terminals/stripe)
      * [Vantiv](point_of_sale/payment_methods/terminals/vantiv)
      * [Worldline](point_of_sale/payment_methods/terminals/worldline)
  * [Reporting](point_of_sale/reporting)

