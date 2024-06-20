# Stripe

[Stripe](https://stripe.com/) is a United States-based online payment solution
provider allowing businesses to accept **credit cards** and other payment
methods.

Pour plus d'infos

  * [List of countries supported by Stripe](https://stripe.com/global)

  * [List of payment methods supported by Stripe](https://stripe.com/payments/payment-methods)

## Create your Stripe account with Odoo

La façon d’obtenir vos identifiants dépend de votre type d’hébergement :

Odoo OnlineOdoo.sh or On-premise

  1. [Navigate to the payment provider Stripe](../payment_providers.html#payment-providers-supported-providers) and click Connect Stripe.

  2. Go through the setup process and confirm your email address when Stripe sends you a confirmation email.

  3. At the end of the process, click Agree and submit. If all requested information has been submitted, you are then redirected to Odoo, and your payment provider is enabled.

  4. Activer les modes de paiement locaux.

  1. [Navigate to the payment provider Stripe](../payment_providers.html#payment-providers-supported-providers) and click Connect Stripe.

  2. Go through the setup process and confirm your email address when Stripe sends you a confirmation email.

  3. At the end of the process, click Agree and submit; you are then redirected to the payment provider **Stripe** in Odoo.

  4. Remplissez vos identifiants.

  5. Générez un webhook.

  6. Select a [payment journal](../payment_providers.html#payment-providers-journal).

  7. Set the State field to Enabled.

  8. Activer les modes de paiement locaux.

Astuce

  * To use an existing Stripe account, [activate the Developer mode](../../general/developer_mode.html#developer-mode) and [enable Stripe manually](../payment_providers.html#payment-providers-add-new). You can then Fill in your credentials, generate a webhook, and enable the payment provider.

  * You can also test Stripe using the [Mode test](../payment_providers.html#payment-providers-test-mode). To do so, first, [log into your Stripe dashboard](https://dashboard.stripe.com/dashboard) and switch to the **Test mode**. Then, in Odoo, [activate the Developer mode](../../general/developer_mode.html#developer-mode), [navigate to the payment provider Stripe](../payment_providers.html#payment-providers-supported-providers), fill in your API credentials with the test keys, and set the State field to Test Mode.

### Remplir vos identifiants

If your **API credentials** are required to connect with your Stripe account,
proceed as follows:

  1. Go to [the API keys page on Stripe](https://dashboard.stripe.com/account/apikeys), or log into your Stripe dashboard and go to Developers ‣ API Keys.

  2. In the Standard keys section, copy the Publishable key and the Secret key and save them for later.

  3. In Odoo, [navigate to the payment provider Stripe](../payment_providers.html#payment-providers-supported-providers).

  4. In the Credentials tab, fill in the Publishable Key and Secret Key fields with the values you previously saved.

### Générer un webhook

If your **Webhook Signing Secret** is required to connect with your Stripe
account, you can create a webhook automatically or manually.

Create the webhook automaticallyCreate the webhook manually

Make sure your Publishable and Secret keys are filled in, then click Generate
your Webhook.

  1. Go to the [Webhooks page on Stripe](https://dashboard.stripe.com/webhooks), or log into your Stripe dashboard and go to Developers ‣ Webhooks.

  2. In the Hosted endpoints section, click Add endpoint. Then, in the Endpoint URL field, enter your Odoo database’s URL, followed by `/payment/stripe/webhook`, e.g., `https://yourcompany.odoo.com/payment/stripe/webhook`.

  3. Click Select events at the bottom of the form, then select the following events:

     * in the Charge section: charge.refunded and charge.refund.updated;

     * in the Payment intent section: payment_intent.amount_capturable_updated, payment_intent.succeeded and payment_intent.payment_failed;

     * in the Setup intent section: setup_intent.succeeded.

  4. Click Add events.

  5. Click Add endpoint, then click Reveal and save your Signing secret for later.

  6. In Odoo, [navigate to the payment provider Stripe](../payment_providers.html#payment-providers-supported-providers).

  7. In the Credentials tab, fill the Webhook Signing Secret field with the value you previously saved.

Note

You can select other events, but they are currently not processed by Odoo.

## Activer les modes de paiement locaux

Local payment methods are payment methods that are only available for specific
providers and for specific countries and currencies.

Odoo supports the following local payment methods for Stripe:

  * Bancontact

  * EPS

  * giropay

  * iDEAL

  * Przelewy24 (P24)

To adapt the list of enabled payment methods, go to the Configuration tab and
edit the list of Supported Payment Icons.

Note

  * If a payment icon record does not exist in the database and its related local payment method is listed above, it is automatically enabled with Stripe.

  * Si un mode de paiement local n’est pas répertorié ci-dessus, il n’est pas pris en charge et ne peut pas être activé.

## Activer Apple Pay

To allow customers to use the Apple Pay button to pay their eCommerce orders,
go to the Configuration tab, enable Allow Express Checkout, and click Enable
Apple Pay.

Pour plus d'infos

  * [Express checkout and Google Pay](../payment_providers.html#payment-providers-express-checkout)

  * [Paiements en ligne](../payment_providers.html)

  * [Use Stripe as a payment terminal in Point of Sale](../../sales/point_of_sale/payment_methods/terminals/stripe.html)

