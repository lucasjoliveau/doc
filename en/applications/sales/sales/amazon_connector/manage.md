# Amazon order management

## Order synchronization

Orders are automatically fetched from Amazon, and synchronized in Odoo, at
regular intervals.

The synchronization is based on the Amazon status: only orders whose status
has changed since the last synchronization are fetched from Amazon. This
includes changes on either end (Amazon or Odoo).

For _FBA_ (Fulfilled by Amazon), only _Shipped_ and _Canceled_ orders are
fetched.

For _FBM_ (Fulfilled by Merchant), the same is done for _Unshipped_ and
_Canceled_ orders. For each synchronized order, a sales order and customer are
created in Odoo (if the customer is not already registered in the database).

Note

When an order is canceled in Amazon, and was already synchronized in Odoo, the
corresponding sales order is automatically canceled in Odoo.

## Force synchronization

In order to force the synchronization of an order, whose status has **not**
changed since the previous synchronization, start by activating the [developer
mode](../../../general/developer_mode.html#developer-mode). This includes
changes on either end (Amazon or Odoo).

Then, navigate to the Amazon account in Odoo (Sales app ‣ Configuration ‣
Settings ‣ Connectors ‣ Amazon Sync ‣ Amazon Accounts), and modify the date
under Orders Follow-up ‣ Last Order Sync.

Be sure to pick a date that occurs prior to the last status change of the
desired order to synchronize and save. This will ensure synchronization occurs
correctly.

Tip

To immediately synchronize the orders of an Amazon account, switch to
[developer mode](../../../general/developer_mode.html#developer-mode), head to
the Amazon account in Odoo, and click Sync Orders. The same can be done with
pickings by clicking Sync Pickings.

## Manage deliveries in FBM

Whenever an FBM (Fulfilled by Merchant) order is synchronized in Odoo, a
picking is instantly created in the _Inventory_ app, along with a sales order
and customer record. Then, decide to either ship all the ordered products to
the customer at once, or ship products partially using backorders.

When a picking related to the order is confirmed, a notification is then sent
to Amazon, who, in turn, notifies the customer that the order (or a part of
it) is on its way.

Important

Amazon requires users to provide a tracking reference with each delivery. This
is needed to assign a carrier.

If the carrier doesn’t automatically provide a tracking reference, one must be
set manually. This rule applies to all Amazon marketplaces.

Tip

If the chosen carrier isn’t supported by Odoo, a carrier with the same name
can still be created (e.g. create a carrier named `easyship`). The name used
is **not** case sensitive, but be mindful to avoid typos. If there are typos,
Amazon will **not** recognize them. Next, create a delivery carrier named
`Self Delivery` to inform Amazon that the user will make the deliveries. Even
with this route, a tracking reference still **must** be entered. Remember, the
customer is notified by email about the delivery, and the carrier, along with
the tracking reference, are displayed in the email to the customer.

See also

[Third-party shipping
carriers](../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper.html)

## Follow deliveries in FBA

When an FBA (Fulfilled by Amazon) order is synchronized in Odoo, a stock move
is recorded in the _Inventory_ app for each sales order item. That way, it’s
saved in the system.

Inventory managers can access these stock moves by navigating to Inventory app
‣ Reporting ‣ Moves History.

For FBA orders, the stock move is automatically created in Odoo by the Amazon
connector, thanks to the shipping status of Amazon. When sending new products
to Amazon, the user should manually create a picking (delivery order) to
transfer these products from their warehouse to the Amazon location.

Tip

To follow _Amazon (FBA)_ stock in Odoo, make an inventory adjustment after
replenishing stock. An automated replenishment from reordering rules can also
be triggered on the Amazon location.

The Amazon location is configurable by accessing the Amazon account managed in
Odoo. To access Amazon accounts in Odoo navigate to Sales app ‣ Configuration
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
possible to send invoices directly to Amazon customers from Odoo. However, it
**is** possible to manually upload the generated invoices from Odoo to the
Amazon back-end.

Additionally, for B2B clients, it is currently required to manually retrieve
VAT numbers from the Amazon back-end **before** creating an invoice in Odoo.

Note

For [TaxCloud](../../../finance/accounting/taxes/taxcloud.html) users:
invoices created from Amazon sales orders are **not** synchronized with
TaxCloud, since Amazon already includes them in its own tax report to
TaxCloud.

Warning

TaxCloud integration will be decommissioned in Odoo 17+.

### Register payments

Since customers pay Amazon as an intermediary, creating a dedicated _Bank_
journal (e.g. named `Amazon Payments`), with a dedicated _Bank and Cash_
intermediary account is recommended.

Additionally, as Amazon makes a single monthly payment, selecting all the
invoices linked to a single payment is necessary when registering payments.

To do that, use the appropriate Journal dedicated to Amazon payments, and
select Batch Deposit as the Payment Method.

Then, select all the generated payments, and click Actions ‣ Create batch
payment ‣ Validate.

Tip

This same action can be performed with vendor bills from Amazon dedicated to
commissions.

When the balance is received in the bank account at the end of the month, and
the bank statements are recorded, credit the Amazon intermediary account by
the amount received.

## Follow Amazon sales in sales reporting

On the Amazon account profile in Odoo , a sales team is set under the Order
Follow-up tab.

This gives quick access to important metrics related to sales reporting. By
default, the Amazon account’s sales team is shared between all of the
company’s accounts.

If desired, the sales team on the account can be changed for another, in order
to perform a separate reporting for the sales of this account.

Tip

It is also possible to perform reporting on a per-marketplace basis.

First, remove the desired marketplace from the list of synchronized
marketplaces.

To access the list of synchronized marketplaces in Odoo, navigate to Sales app
‣ Configuration ‣ Settings ‣ Connectors ‣ Amazon Sync ‣ Amazon Accounts.

Then, create another registration for this account, and remove all other
marketplaces **except** the one to isolate.

Lastly, assign another sales team to one of the two registrations of the
account.

See also

  * [Amazon Connector features](features.html)

  * [Amazon Connector configuration](setup.html)

