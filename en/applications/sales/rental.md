# Rental

**Odoo Rental** is a comprehensive solution to manage your rentals.

From a single view, you can send out quotations, confirm orders, schedule
rentals, register when products are picked up and returned, and invoice your
customers.

See also

  * [Odoo Rental: product page](https://www.odoo.com/app/rental)

  * [Odoo Tutorials: Rental](https://www.odoo.com/slides/rental-48)

## Rental Pricing

### Configuration

Go to Rental ‣ Products, select or create a product, and click on the
product’s _Rental_ tab. Under _Rental Pricing_ , click on _Add a price_. Then
choose a _Unit_ of time (hours, days, weeks, or months), a _Duration_ , and a
_Price_. You can add as many price lines as necessary, usually to give out
discounts for longer rental durations.

![Example of rental pricing configuration in Odoo
Rental](../../_images/rental-pricing-example.png)

Tip

Under _Reservations_ , you can add fines for any _Extra Hour_ or _Extra Day_.
You can also set a _Security Time_ , expressed in hours, to make the product
temporarily unavailable between two rental orders.

Note

If you want to rent a product created outside of the Rental app, do not forget
to tick _Can be Rented_ under the product’s name. By default, this option is
ticked when you create a product directly from the Rental app.

### Computing

Odoo always uses two rules to compute the price of a product when you create a
rental order:

  1. Only one price line is used.

  2. The cheapest line is selected.

Exercise

Consider the following rental pricing configuration for a product:

  * 1 day: $100

  * 3 days: $250

  * 1 week: $500

A customer wants to rent this product for eight days. What price will they
pay?

After an order is created, Odoo selects the second line as this is the
cheapest option. The customer has to pay three times ‘3 days’ to cover the
rental’s eight days, for a total of $750.

## Customer signature

You can ask your customers to sign a rental agreement outlining the
arrangement between you and your customers before they pick up products to
make sure your products are returned on time and in their original condition.
To do so, go to Rental ‣ Configuration ‣ Settings, activate _Digital
Documents_ , and _Save_.

![Digital Documents settings in Odoo Rental](../../_images/digital-documents-
settings.png)

Note

This feature requires the [Sign](../productivity/sign.html) app. If necessary,
Odoo installs it after activating _Digital Documents_.

Once the app settings are saved, you have the option to change the default
_Rental Agreement_ from the dropdown menu. You can pick any document already
uploaded to the _Sign_ app, or upload a new one to the _Sign_ app by clicking
on _Upload Template_.

To request a customer signature, select a confirmed rental order, click on
_Sign Documents_ , choose the document template and click on _Sign Documents_
again. On the next window, select your customer and click on _Sign Now_ to
start the signing process with your customer. Once the document is completed,
click on _Validate & Send Completed Document_.

See also

  * [Odoo Tutorials: Sign](https://www.odoo.com/slides/sign-61)

## Pickup and Return receipt

You can print and give your customers receipts when they pick up and/or return
products. To do so, open any rental order, click on _Print_ and select _Pickup
and Return Receipt_. Odoo then generates a PDF detailing all information about
the current status of the rented items: which were picked up, when they are
expected to be returned, which were returned, and potential rental delay
costs.

![Printing a Pickup and Return receipt in Odoo Rental](../../_images/print-
receipt1.png)

