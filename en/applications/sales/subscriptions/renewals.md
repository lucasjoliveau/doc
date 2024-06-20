# Renew a subscription

The key feature of a subscription business model is the recurring nature of
payments. In this model, customers pay a recurring amount in exchange for
access to a product or a service.

**The renewal of a subscription is the process followed by each customer when
willing to pursue a subscription.**

Each subscriber experiences this renewal process monthly, annually, or
sometimes more, depending on the duration of the contract. Most subscription
companies choose to automate their renewal processes but, in some cases,
manual subscription renewals are still the preferred option.

With **Odoo Subscriptions** , you can have all your subscriptions in one
application, suggest an automatic subscription renewal to your customers (as
well as a manual one) and, finally, filter all your subscriptions and easily
find those to renew (with the help of the tag _To renew_).

## Renew your first subscription

Before renewing a subscription, be sure to check out our documentation on how
to [Create a quotation](../subscriptions.html) using subscription products.
Indeed, once confirmed, a quotation becomes a sales order and a new
subscription is automatically created. Therefore, this subscription has the
status _In progress_. From there, you have the possibility to renew the
subscription. In the Other Info tab, underneath the To Renew section, you can
activate the _To renew_ option. When activated, a yellow tag automatically
appears in the upper right corner of the subscription.

![Renew your subscription with Odoo Subscriptions](../../../_images/renew-
your-subscription.png)

Important

The _To renew_ tag is automatically ticked when a payment fails. This
indicator also appears on the customer portal. To visualize that, you just
have to click on the _Customer preview_ button. The tag _To renew_ appears on
the top right corner.

![Customer preview of a renewal with Odoo
Subscriptions](../../../_images/customer-preview-of-a-renewal.png)

When a subscription needs to be renewed, you have the possibility to use a new
button called _Renewal quotation_. By clicking on it, a new quotation is
created. From there, start a basic sales flow allowing you to send the
quotation by email to your customers or to confirm it. It is better to first
_Send by email_ the quotation to your customers in order to have their
confirmation and, then, _Confirm_ it in **Odoo Sales**.

Note

In the Chatter of this new quotation, it is mentioned that “This renewal order
has been created from the previous subscription”. Once confirmed by your
customers, this quotation becomes a sales order and a new sale is mentioned in
the upper right corner of the subscription.

![Renew a quotation with Odoo Subscriptions](../../../_images/renew-a-
quotation.png)

By clicking on the _Sales_ button, you have a summary of your sales orders in
a list view. The only difference between your two quotations is the
description underneath the _Subscription Management_ category. There, you can
easily visualize which one is your renewal.

![Renewal as Subscription Management form in Odoo
Subscriptions](../../../_images/subscription-management-category.png)

## Visualize your subscriptions to renew

Finally, if you want to visualize all your subscriptions and easily find those
to renew, you can go to your _Subscriptions dashboard_ and use the filter _To
renew_.

![List view of all subscriptions and use of the filter to renew in Odoo
Subscriptions](../../../_images/subscriptions-dashboard-with-the-to-renew-
filter.png)

See also

  * [Subscriptions](../subscriptions.html)

  * [Subscription plans](plans.html)

  * [Subscription products](products.html)

