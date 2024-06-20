# Upsell a subscription

Subscriptions are recurrent and go on indefinitely. As time passes by, our
customers may want to modify them. We must then be able to adapt the prices or
change the products’ quantities to accommodate their needs. Two situations can
happen:

  1. **Loyal customers:** This kind of customers already trust you as a brand. Therefore, you are confident regarding what you offer since they keep paying for your products and services. Consequently, it is easier to sell them something additional than it would be to a new customer.

  2. **New customers:** For this kind of customers, you have to come with something new, something attractive. What about discounts? Typically, every subscription ends after a certain given time. Making these types of offers for new customers strengthens your relationships with them and also increases their retention.

**Upselling can make a subscription last longer!**

## Configuration

As previously explained, to upsell a subscription to new customers, it is
recommended to offer _Discounts_. To activate this option, go to Sales ‣
Configuration ‣ Settings and, under the _Pricing_ category, you have the
possibility to grant discounts on sales order lines.

![Activation of the discount option in Odoo
Sales](../../../_images/configuration-to-upsell-a-subscription.png)

## Upsell your first subscription

Before upselling a subscription, be sure to check out our documentation on how
to [Create a quotation](../subscriptions.html) using subscription products.
Indeed, once confirmed, a quotation becomes a sales order and a new
subscription is automatically created. Therefore, this subscription has the
status _In progress_. From there, you have the possibility to upsell your
subscription.

![Upsell your subscription with Odoo Subscriptions](../../../_images/upsell-
your-subscription.png)

By using the smart button _Upsell_ , you are able to create a new quotation
with new subscription products and send it to your customers for approval.

![Add products to your subscription via the upsell option in Odoo
Subscriptions](../../../_images/use-of-the-upsell-button-in-odoo-sales.png)

Important

When the quotation is confirmed by your customers, the products are added to
the initial subscription. Quotation prices are, then, prorated to the
remaining time of the current invoicing period.

Of course, before sending this new quotation to your customers, you can change
the unit price, taxes, and, even the discount you want to offer. The smart
button _Customer preview_ is useful for mimicking the customer’s reaction. In
this case, we can confidently say that the customer will _Sign and pay_ this
new quotation. When it is done, you have to go back in edit mode, confirm the
quotation, and click on the smart button _Subscriptions_ to visualize all
updates. From there, you can see that an additional line has been added to the
subscription with the new extra service the customer wanted to purchase.

![Visualize all your subscriptions updates with Odoo
Subscriptions](../../../_images/subscriptions-updates.png)

In addition, by clicking on the _Sales_ button, you have a summary of your
sales orders in a list view.

![List view of all sales orders created for a
subscription](../../../_images/sales-order-updates.png)

The only difference between your two sales orders is the description
underneath the _Subscription Management_ category. There, you can easily
visualize which one is your upselling.

See also

  * [Subscriptions](../subscriptions.html)

  * [Subscription plans](plans.html)

  * [Subscription products](products.html)

