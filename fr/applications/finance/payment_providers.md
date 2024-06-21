# Paiements en ligne

  * [Virements bancaires](payment_providers/wire_transfer)
  * [Adyen](payment_providers/adyen)
  * [Alipay](payment_providers/alipay)
  * [Amazon Payment Services](payment_providers/amazon_payment_services)
  * [AsiaPay](payment_providers/asiapay)
  * [Authorize.Net](payment_providers/authorize)
  * [Buckaroo](payment_providers/buckaroo)
  * [Démo](payment_providers/demo)
  * [Flutterwave](payment_providers/flutterwave)
  * [Mercado Pago](payment_providers/mercado_pago)
  * [Mollie](payment_providers/mollie)
  * [Ogone](payment_providers/ogone)
  * [PayPal](payment_providers/paypal)
  * [Razorpay](payment_providers/razorpay)
  * [SIPS](payment_providers/sips)
  * [Stripe](payment_providers/stripe)

Konvergo ERP embeds several **payment providers** that allow your customers to pay
online, on their _customer portals_ , or on your _eCommerce website_. They can
pay sales orders, invoices, or subscriptions with recurring payments using
their favorite payment methods, such as **credit cards**.

![Online payment form](../../_images/online-payment.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Konvergo ERP apps delegate the handling of sensitive information to the certified payment provider so
that you don’t ever have to worry about PCI compliance. No sensitive information (such as credit
card numbers) is stored on Konvergo ERP servers or Konvergo ERP databases hosted elsewhere. Instead, Konvergo ERP apps
use a unique reference number for the data stored safely in the payment providers” systems.</p>
</div>

## Fournisseurs de paiement pris en charge

To access the supported payment providers, go to Accounting ‣ Configuration ‣
Payment Providers or Website ‣ Configuration ‣ Payment Providers.

### Fournisseurs de paiement en ligne

| Flux de paiement depuis | Tokenization | Manual capture | Refunds | Express checkout | Extra fees  
---|---|---|---|---|---|---  
[Adyen](payment_providers/adyen) | Konvergo ERP | ✔ | Intégrale | Intégral et partiel |  |   
[Amazon Payment Services](payment_providers/amazon_payment_services) | The provider’s website |  |  |  |  |   
[AsiaPay](payment_providers/asiapay) | The provider’s website |  |  |  |  |   
[Authorize.Net](payment_providers/authorize) | Konvergo ERP | ✔ | Intégrale | Intégrale |  |   
[Buckaroo](payment_providers/buckaroo) | The provider’s website |  |  |  |  |   
[Flutterwave](payment_providers/flutterwave) | The provider’s website | ✔ |  |  |  |   
[Mercado Pago](payment_providers/mercado_pago) | The provider’s website |  |  |  |  |   
[Mollie](payment_providers/mollie) | The provider’s website |  |  |  |  |   
[PayPal](payment_providers/paypal) | The provider’s website |  |  |  |  | ✔  
[Razorpay](payment_providers/razorpay) | The provider’s website |  | Intégrale | Intégral et partiel |  |   
[SIPS](payment_providers/sips) | The provider’s website |  |  |  |  |   
[Stripe](payment_providers/stripe) | The provider’s website | ✔ | Intégrale | Intégral et partiel | ✔ |   
<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Each provider has its own specific configuration flow, depending on which feature is
available.</p></li>
<li><p>Some of these online payment providers can also be added as <a href="accounting/bank">bank accounts</a>, but this is <b>not</b> the same process as adding them as payment
providers. Payment providers allow customers to pay online, and bank accounts are added and
configured in the Accounting app to do a <a href="accounting/bank/reconciliation">bank reconciliation</a>.</p></li>
</ul>
</div> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>In addition to the regular payment providers that integrate with an API, such as Stripe, PayPal,
or Adyen, Konvergo ERP bundles the <a href="payment_providers/demo">Demo payment provider</a>. This payment
provider allows you to test business flows involving online payments. No credentials are required
as the demo payments are dummy payments.</p>
</div>

### Paiements bancaires

  * [Virement bancaire](payment_providers/wire_transfer)

When selected, Konvergo ERP displays your payment information with a payment
reference. You have to approve the payment manually once you have received it
in your bank account.

  * [Prélèvement SEPA](accounting/payments/batch_sdd)

Your customers can make a bank transfer to register a SEPA Direct Debit
mandate and get their bank account charged directly.

## Enable a payment provider

To add a new payment provider and make its related payment methods available
to your customers, proceed as follows:

  1. Go to the payment provider’s website, create an account, and make sure you have the API credentials requested for third-party use. These are necessary for Konvergo ERP to communicate with the payment provider.

  2. In Konvergo ERP, navigate to the **Payment providers** by going to Accounting ‣ Configuration ‣ Payment Providers or Website ‣ Configuration ‣ Payment Providers.

  3. Select the provider and configure the **Credentials** tab.

  4. Set the **State** field to **Enabled**.

  5. Select a payment journal.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>The fields available in the <b>Credentials</b> tab depend on the payment provider. Refer
to the <a href="#payment-providers-supported-providers"><span class="std std-ref">related documentation</span></a> for more
information.</p></li>
<li><p>Once you have enabled the payment provider, it is automatically published on your website.
If you wish to unpublish it, click the <b>Published</b> button. Customers cannot make
payments through an unpublished provider, but they can still manage
<span class="dfn"><span>(delete and assign to a subscription)</span></span> their existing tokens linked to such a provider.</p></li>
</ul>
</div>

### Mode test

If you wish to try the payment provider as a test, set the **State** field in
the payment provider form to **Test mode** , then enter your provider’s
test/sandbox credentials in the **Credentials** tab.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>By default, the payment provider remains <b>unpublished</b> in test mode so that it’s not visible to
visitors.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>We recommend using the test mode on a duplicate or a test database to avoid potential issues
with your invoice numbering.</p>
</div>

## Payment form

You can change the payment provider’s appearance on your website in the
**Configuration** tab of the selected payment provider. Modify its name in the
**Displayed as** field and adapt the **Supported Payment Icons** if necessary.

## Tokenisation

If the payment provider supports this feature, customers can save their
payment method details for later. To enable this feature, go to the
**Configuration** tab of the selected payment provider and enable **Allow
Saving Payment Methods**.

In this case, a **payment token** is created in Konvergo ERP to be used as a payment
method for subsequent payments without the customer having to enter their
payment method details again. This is particularly useful for the eCommerce
conversion rate and subscriptions that use recurring payments.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>You remain fully PCI-compliant when you enable this feature because Konvergo ERP does not store the card
details directly. Instead, it creates a payment token that only references the card details
stored on the payment provider’s server.</p>
</div>

## Capture manuelle

If the payment provider supports this feature, you can authorize and capture
payments in two steps instead of one. To enable this feature, go to the
**Configuration** tab of the selected payment provider and enable **Capture
Amount Manually**.

When you authorize a payment, the funds are reserved on the customer’s payment
method but not immediately charged. They are charged when you manually capture
the payment later on. You can also void the authorization to cancel it and
release the reserved funds. Capturing payments manually is helpful in many
situations:

  * Recevoir la confirmation du paiement et attendre que la commande soit expédiée pour capturer le paiement.

  * Examiner et vérifier que les commandes sont légitimes avant que le paiement ne soit effectué et que le processus d’exécution ne commence.

  * Avoid potentially high refund fees for refunded payments: payment providers will not charge you for voiding an authorization.

  * Hold a security deposit to return later, minus any deductions (e.g., in case of damages).

To capture the payment after it was authorized, go to the related sales order
or invoice and click the **Capture Transaction** button. To release the funds,
click the **Void Transaction** button.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Some payment providers support capturing only part of the authorized amount. The remaining
amount can then be either captured or voided. These providers have the value <b>Full and
partial</b> in the <a href="#payment-providers-online-providers"><span class="std std-ref">table above</span></a>. The providers that
only support capturing or voiding the total amount have the value <b>Full only</b>.</p></li>
<li><p>Les fonds ne sont probablement pas réservés pour toujours. Au bout d’un certain temps, ils peuvent être automatiquement reversés au mode de paiement du client. Consultez la documentation de votre fournisseur de paiement pour connaître la durée exacte de la réservation.</p></li>
<li><p>Konvergo ERP does not support this feature for all payment providers, but some allow the manual capture
from their website interface.</p></li>
</ul>
</div>

## Remboursements

If your payment provider supports this feature, you can refund payments
directly from Konvergo ERP. It does not need to be enabled first. To refund a customer
payment, navigate to it and click the **Refund** button.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Some payment providers support refunding only part of the amount. The remaining amount can then
optionally be refunded, too. These providers have the value <b>Full and partial</b> in the
<a href="#payment-providers-online-providers"><span class="std std-ref">table above</span></a>. The providers that only support
refunding the total amount have the value <b>Full only</b>.</p></li>
<li><p>Konvergo ERP does not support this feature for all payment providers, but some allow to refund payments
from their website interface.</p></li>
</ul>
</div>

## Paiement rapide

If the payment provider supports this feature, you can allow customers to use
the **Google Pay** and **Apple Pay** buttons and pay their eCommerce orders in
one click. When they use one of these buttons, customers go straight from the
cart to the confirmation page without filling out the contact form. They just
have to validate the payment on Google’s or Apple’s payment form.

To enable this feature, go to the **Configuration** tab of the selected
payment provider and enable **Allow Express Checkout**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>All prices shown on the express checkout payment form always include taxes.</p>
</div>

## Frais supplémentaires

If the payment provider supports this feature, you can add extra fees to
online transactions. Fees can be configured either as **fixed** amounts and
percentages, **variable** amounts and percentages, or both simultaneously.
They can also differ based on whether the transaction is **domestic** or
**international**.

To enable this feature, go to the **Fees** tab of the selected payment
provider, enable **Add Extra Fees** , and configure the settings to your
liking.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Each provider has its own specific configuration flow, depending on which feature is
available.</p></li>
<li><p>Some of these online payment providers can also be added as <a href="accounting/bank">bank accounts</a>, but this is <b>not</b> the same process as adding them as payment
providers. Payment providers allow customers to pay online, and bank accounts are added and
configured in the Accounting app to do a <a href="accounting/bank/reconciliation">bank reconciliation</a>.</p></li>
</ul>
</div>0

## Disponibilité

You can adapt the payment provider’s availability by specifying the **Maximum
Amount** allowed and modifying the **Currencies** and **Countries** in the
**Configuration** tab.

### Currencies and countries

All payment providers have a different list of available currencies and
countries. They serve as a first filter during payment operations, i.e., the
payment methods linked to the payment provider are not available for selection
if the customer’s currency or country is not in the supported list. As there
might be errors, updates, and unknowns in the lists of available currencies
and countries, adding or removing a payment provider’s supported currencies or
countries is possible.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Each provider has its own specific configuration flow, depending on which feature is
available.</p></li>
<li><p>Some of these online payment providers can also be added as <a href="accounting/bank">bank accounts</a>, but this is <b>not</b> the same process as adding them as payment
providers. Payment providers allow customers to pay online, and bank accounts are added and
configured in the Accounting app to do a <a href="accounting/bank/reconciliation">bank reconciliation</a>.</p></li>
</ul>
</div>1

### Maximum amount

You can restrict the **Maximum Amount** that can be paid with the selected
provider. Leave the field to `0.00` to make the payment provider available
regardless of the payment amount.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Each provider has its own specific configuration flow, depending on which feature is
available.</p></li>
<li><p>Some of these online payment providers can also be added as <a href="accounting/bank">bank accounts</a>, but this is <b>not</b> the same process as adding them as payment
providers. Payment providers allow customers to pay online, and bank accounts are added and
configured in the Accounting app to do a <a href="accounting/bank/reconciliation">bank reconciliation</a>.</p></li>
</ul>
</div>2

## Journal des paiements

A [payment journal](accounting/bank) must be defined for the payment
provider to record the payments on an **outstanding account**. To do so, go to
the **Configuration** tab of the selected payment provider and select a
**Payment Journal**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Each provider has its own specific configuration flow, depending on which feature is
available.</p></li>
<li><p>Some of these online payment providers can also be added as <a href="accounting/bank">bank accounts</a>, but this is <b>not</b> the same process as adding them as payment
providers. Payment providers allow customers to pay online, and bank accounts are added and
configured in the Accounting app to do a <a href="accounting/bank/reconciliation">bank reconciliation</a>.</p></li>
</ul>
</div>3

### Perspective comptable

From an accounting perspective, there are two types of online payment
workflows: the payments that are directly deposited into your bank account and
follow the usual [reconciliation](accounting/bank/reconciliation)
workflow, and those coming from third-party online payment providers and
require you to follow another accounting workflow. For these payments, you
need to consider how you want to record your payments” journal entries. We
recommend you ask your accountant for advice.

By default, the **Bank Account** defined for the payment journal is used, but
you can also specify an [outstanding account](accounting/bank#bank-
outstanding-accounts) for each payment provider to separate the provider’s
payments from other payments.

![Define an outstanding account for a payment
provider.](../../_images/bank_journal.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Each provider has its own specific configuration flow, depending on which feature is
available.</p></li>
<li><p>Some of these online payment providers can also be added as <a href="accounting/bank">bank accounts</a>, but this is <b>not</b> the same process as adding them as payment
providers. Payment providers allow customers to pay online, and bank accounts are added and
configured in the Accounting app to do a <a href="accounting/bank/reconciliation">bank reconciliation</a>.</p></li>
</ul>
</div>4

