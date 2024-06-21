# Amazon order management

## Order synchronization

Orders are automatically fetched from Amazon, and synchronized in Konvergo ERP, at
regular intervals.

The synchronization is based on the Amazon status: only orders whose status
has changed since the last synchronization are fetched from Amazon. This
includes changes on either end (Amazon or Konvergo ERP).

For _FBA_ (Fulfilled by Amazon), only _Shipped_ and _Canceled_ orders are
fetched.

For _FBM_ (Fulfilled by Merchant), the same is done for _Unshipped_ and
_Canceled_ orders. For each synchronized order, a sales order and customer are
created in Konvergo ERP (if the customer is not already registered in the database).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When an order is canceled in Amazon, and was already synchronized in Konvergo ERP, the corresponding
sales order is automatically canceled in Konvergo ERP.</p>
</div>

## Force synchronization

In order to force the synchronization of an order, whose status has **not**
changed since the previous synchronization, start by activating the [developer
mode](../../../general/developer_mode#developer-mode). This includes
changes on either end (Amazon or Konvergo ERP).

Then, navigate to the Amazon account in Konvergo ERP (Sales app ‣ Configuration ‣
Settings ‣ Connectors ‣ Amazon Sync ‣ Amazon Accounts), and modify the date
under Orders Follow-up ‣ Last Order Sync.

Be sure to pick a date that occurs prior to the last status change of the
desired order to synchronize and save. This will ensure synchronization occurs
correctly.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>To immediately synchronize the orders of an Amazon account, switch to <a href="../../../general/developer_mode#developer-mode"><span class="std std-ref">developer mode</span></a>, head to the Amazon account in Konvergo ERP, and click <b>Sync Orders</b>. The
same can be done with pickings by clicking <b>Sync Pickings</b>.</p>
</div>

## Manage deliveries in FBM

Whenever an FBM (Fulfilled by Merchant) order is synchronized in Konvergo ERP, a
picking is instantly created in the _Inventory_ app, along with a sales order
and customer record. Then, decide to either ship all the ordered products to
the customer at once, or ship products partially using backorders.

When a picking related to the order is confirmed, a notification is then sent
to Amazon, who, in turn, notifies the customer that the order (or a part of
it) is on its way.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Amazon requires users to provide a tracking reference with each delivery. This is needed to
assign a carrier.</p>
<p>If the carrier doesn’t automatically provide a tracking reference, one must be set manually. This
rule applies to all Amazon marketplaces.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If the chosen carrier isn’t supported by Konvergo ERP, a carrier with the same name can still be created
(e.g. create a carrier named <code>easyship</code>). The name used is <b>not</b> case sensitive, but be mindful
to avoid typos. If there are typos, Amazon will <b>not</b> recognize them. Next, create a delivery
carrier named <code>Self Delivery</code> to inform Amazon that the user will make the deliveries. Even with
this route, a tracking reference still <b>must</b> be entered. Remember, the customer is notified by
email about the delivery, and the carrier, along with the tracking reference, are displayed in
the email to the customer.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper">Third-party shipping carriers</a></p>
</div>

## Follow deliveries in FBA

When an FBA (Fulfilled by Amazon) order is synchronized in Konvergo ERP, a stock move
is recorded in the _Inventory_ app for each sales order item. That way, it’s
saved in the system.

Inventory managers can access these stock moves by navigating to Inventory app
‣ Reporting ‣ Moves History.

For FBA orders, the stock move is automatically created in Konvergo ERP by the Amazon
connector, thanks to the shipping status of Amazon. When sending new products
to Amazon, the user should manually create a picking (delivery order) to
transfer these products from their warehouse to the Amazon location.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>To follow <em>Amazon (FBA)</em> stock in Konvergo ERP, make an inventory adjustment after replenishing stock. An
automated replenishment from reordering rules can also be triggered on the Amazon location.</p>
</div>

The Amazon location is configurable by accessing the Amazon account managed in
Konvergo ERP. To access Amazon accounts in Konvergo ERP navigate to Sales app ‣ Configuration
‣ Settings ‣ Connectors ‣ Amazon Sync ‣ Amazon Accounts.

All accounts of the same company use the same Amazon location, by default.
However, it is possible to follow the stock filtered by marketplace.

To do that, first remove the marketplace, where the desired stock to follow
separately can be found, from the list of synchronized marketplaces, which can
be found by navigating to Sales app ‣ Configuration ‣ Settings ‣ Connectors ‣
Amazon Sync ‣ Amazon Accounts.

Next, create another registration for this account, and remove all
marketplaces— **except** the marketplace this is desired to be isolated from
the others.

Lastly, assign another stock location to the second registration of the
account.

## Invoice and register payments

### Issue invoices

Due to Amazon’s policy of not sharing customer email addresses, it is **not**
possible to send invoices directly to Amazon customers from Konvergo ERP. However, it
**is** possible to manually upload the generated invoices from Konvergo ERP to the
Amazon back-end.

Additionally, for B2B clients, it is currently required to manually retrieve
VAT numbers from the Amazon back-end **before** creating an invoice in Konvergo ERP.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>For <a href="../../../finance/accounting/taxes/taxcloud">TaxCloud</a> users: invoices created from
Amazon sales orders are <b>not</b> synchronized with TaxCloud, since Amazon already includes them in
its own tax report to TaxCloud.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>TaxCloud integration will be decommissioned in Konvergo ERP 17+.</p>
</div>

### Register payments

Since customers pay Amazon as an intermediary, creating a dedicated _Bank_
journal (e.g. named `Amazon Payments`), with a dedicated _Bank and Cash_
intermediary account is recommended.

Additionally, as Amazon makes a single monthly payment, selecting all the
invoices linked to a single payment is necessary when registering payments.

To do that, use the appropriate **Journal** dedicated to Amazon payments, and
select **Batch Deposit** as the **Payment Method**.

Then, select all the generated payments, and click Actions ‣ Create batch
payment ‣ Validate.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>This same action can be performed with vendor bills from Amazon dedicated to commissions.</p>
<p>When the balance is received in the bank account at the end of the month, and the bank statements
are recorded, credit the Amazon intermediary account by the amount received.</p>
</div>

## Follow Amazon sales in sales reporting

On the Amazon account profile in Konvergo ERP , a sales team is set under the **Order
Follow-up** tab.

This gives quick access to important metrics related to sales reporting. By
default, the Amazon account’s sales team is shared between all of the
company’s accounts.

If desired, the sales team on the account can be changed for another, in order
to perform a separate reporting for the sales of this account.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>It is also possible to perform reporting on a per-marketplace basis.</p>
<p>First, remove the desired marketplace from the list of synchronized marketplaces.</p>
<p>To access the list of synchronized marketplaces in Konvergo ERP, navigate to Sales app
‣ Configuration ‣ Settings ‣ Connectors ‣ Amazon Sync ‣ Amazon Accounts.</p>
<p>Then, create another registration for this account, and remove all other marketplaces <b>except</b>
the one to isolate.</p>
<p>Lastly, assign another sales team to one of the two registrations of the account.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>To immediately synchronize the orders of an Amazon account, switch to <a href="../../../general/developer_mode#developer-mode"><span class="std std-ref">developer mode</span></a>, head to the Amazon account in Konvergo ERP, and click <b>Sync Orders</b>. The
same can be done with pickings by clicking <b>Sync Pickings</b>.</p>
</div>0

