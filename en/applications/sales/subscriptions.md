# Subscriptions

Konvergo ERP _Subscriptions_ is used to run recurring businesses: sell new contracts,
[upsell customers](subscriptions/upselling), keep the churn under
control, and [generate reports](subscriptions/reports) on the main KPIs:
MRR, ARR, retention, churn, etc.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="https://www.odoo.com/slides/subscription-20">Konvergo ERP Tutorials: Subscriptions</a></p></li>
<li><p><a href="subscriptions/products">Subscription products</a></p></li>
<li><p><a href="subscriptions/ecommerce">Use subscriptions in the eCommerce shop</a></p></li>
<li><p><a href="subscriptions/plans">Subscription plans</a></p></li>
<li><p><a href="subscriptions/upselling">Upsell a subscription</a></p></li>
<li><p><a href="subscriptions/renewals">Renew a subscription</a></p></li>
<li><p><a href="subscriptions/closing">Close a subscription</a></p></li>
<li><p><a href="subscriptions/automatic_alerts">Automatic alerts</a></p></li>
<li><p><a href="subscriptions/reports">Reports</a></p></li>
</ul>
</div>

## Subscription quotations

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Sales orders with a defined recurrence become subscriptions.</p>
</div>

To create a new subscription, click on **New** from the _Subscription_ or the
[Sales](../sales) app. You can either:

  * Select a [subscription plan](subscriptions/plans) to prefill the quotation instantly, or

  * Fill out the quotation normally, making sure to select a recurrence and an end date if necessary and adding [recurrent products](subscriptions/products).

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>You can define different invoice and delivery addresses by enabling the <a href="../finance/accounting/customer_invoices/customer_addresses">Customer Addresses</a> feature.</p>
</div>

## Confirmation

Send the quotation to the customer for confirmation by clicking on **Send by
email** , or confirm it immediately by clicking on **Confirm**.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Click on <b>Customer Preview</b> to preview the customer portal where the customer can view
their quotation, sign and pay it, and communicate with you.</p>
</div>

## Automatic payments

You can require the customer to set an automatic payment method and pre-pay
the subscription’s first occurrence before they can confirm their quotation.
To do so, go to the **Other Info** tab of the quotation and check the
**Payment** option in the **Online confirmation** field.

If you leave **Payment** unchecked, the customer doesn’t have to pre-pay to
start the subscription. This means that the payment is not automatic and that
the customer must pay each invoice manually.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If the online confirmation requires a pre-payment, your customer can select only the
<a href="../finance/payment_providers#payment-providers-supported-providers"><span class="std std-ref">payment providers</span></a> that have the <a href="../finance/payment_providers#payment-providers-tokenization"><span class="std std-ref">tokenization
feature</span></a>. This ensures that the customer is automatically
charged at each new period.</p>
</div>

  * [Subscription products](subscriptions/products)
  * [Use subscriptions in the eCommerce shop](subscriptions/ecommerce)
  * [Subscription plans](subscriptions/plans)
  * [Upsell a subscription](subscriptions/upselling)
  * [Renew a subscription](subscriptions/renewals)
  * [Close a subscription](subscriptions/closing)
  * [Automatic alerts](subscriptions/automatic_alerts)
  * [Reports](subscriptions/reports)

  *[KPIs]: Key Performance Indicators
  *[MRR]: Monthly Recurring Revenue
  *[ARR]: Annual Recurring Revenue

