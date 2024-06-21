# Stripe

[Stripe](https://stripe.com/) is a United States-based online payment solution
provider allowing businesses to accept **credit cards** and other payment
methods.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://stripe.com/global">List of countries supported by Stripe</a></p></li>
<li><p><a href="https://stripe.com/payments/payment-methods">List of payment methods supported by Stripe</a></p></li>
</ul>
</div>

## Create your Stripe account with Konvergo ERP

La façon d’obtenir vos identifiants dépend de votre type d’hébergement :

Konvergo ERP OnlineKonvergo ERP.sh or On-premise

  1. [Navigate to the payment provider Stripe](../payment_providers#payment-providers-supported-providers) and click **Connect Stripe**.

  2. Go through the setup process and confirm your email address when Stripe sends you a confirmation email.

  3. At the end of the process, click **Agree and submit**. If all requested information has been submitted, you are then redirected to Konvergo ERP, and your payment provider is enabled.

  4. Activer les modes de paiement locaux.

  1. [Navigate to the payment provider Stripe](../payment_providers#payment-providers-supported-providers) and click **Connect Stripe**.

  2. Go through the setup process and confirm your email address when Stripe sends you a confirmation email.

  3. At the end of the process, click **Agree and submit** ; you are then redirected to the payment provider **Stripe** in Konvergo ERP.

  4. Remplissez vos identifiants.

  5. Générez un webhook.

  6. Select a [payment journal](../payment_providers#payment-providers-journal).

  7. Set the **State** field to **Enabled**.

  8. Activer les modes de paiement locaux.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><ul>
<li><p>To use an existing Stripe account, <a href="../../general/developer_mode#developer-mode"><span class="std std-ref">activate the Developer mode</span></a> and
<a href="../payment_providers#payment-providers-add-new"><span class="std std-ref">enable Stripe manually</span></a>. You can then <a href="#stripe-api-keys"><span class="std std-ref">Fill in your
credentials</span></a>, <a href="#stripe-webhook"><span class="std std-ref">generate a webhook</span></a>, and enable the
payment provider.</p></li>
<li><p>You can also test Stripe using the <a href="../payment_providers#payment-providers-test-mode"><span class="std std-ref">Mode test</span></a>. To do so, first,
<a href="https://dashboard.stripe.com/dashboard">log into your Stripe dashboard</a> and switch to the
<b>Test mode</b>. Then, in Konvergo ERP, <a href="../../general/developer_mode#developer-mode"><span class="std std-ref">activate the Developer mode</span></a>,
<a href="../payment_providers#payment-providers-supported-providers"><span class="std std-ref">navigate to the payment provider Stripe</span></a>,
<a href="#stripe-api-keys"><span class="std std-ref">fill in your API credentials</span></a> with the test keys, and set the
<b>State</b> field to <b>Test Mode</b>.</p></li>
</ul>
</div>

### Remplir vos identifiants

If your **API credentials** are required to connect with your Stripe account,
proceed as follows:

  1. Go to [the API keys page on Stripe](https://dashboard.stripe.com/account/apikeys), or log into your Stripe dashboard and go to Developers ‣ API Keys.

  2. In the **Standard keys** section, copy the **Publishable key** and the **Secret key** and save them for later.

  3. In Konvergo ERP, [navigate to the payment provider Stripe](../payment_providers#payment-providers-supported-providers).

  4. In the **Credentials** tab, fill in the **Publishable Key** and **Secret Key** fields with the values you previously saved.

### Générer un webhook

If your **Webhook Signing Secret** is required to connect with your Stripe
account, you can create a webhook automatically or manually.

Create the webhook automaticallyCreate the webhook manually

Make sure your Publishable and Secret keys are filled in, then click
**Generate your Webhook**.

  1. Go to the [Webhooks page on Stripe](https://dashboard.stripe.com/webhooks), or log into your Stripe dashboard and go to Developers ‣ Webhooks.

  2. In the **Hosted endpoints** section, click **Add endpoint**. Then, in the **Endpoint URL** field, enter your Konvergo ERP database’s URL, followed by `/payment/stripe/webhook`, e.g., `https://yourcompany.odoo.com/payment/stripe/webhook`.

  3. Click **Select events** at the bottom of the form, then select the following events:

     * in the **Charge** section: **charge.refunded** and **charge.refund.updated** ;

     * in the **Payment intent** section: **payment_intent.amount_capturable_updated** , **payment_intent.succeeded** and **payment_intent.payment_failed** ;

     * in the **Setup intent** section: **setup_intent.succeeded**.

  4. Click **Add events**.

  5. Click **Add endpoint** , then click **Reveal** and save your **Signing secret** for later.

  6. In Konvergo ERP, [navigate to the payment provider Stripe](../payment_providers#payment-providers-supported-providers).

  7. In the **Credentials** tab, fill the **Webhook Signing Secret** field with the value you previously saved.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>You can select other events, but they are currently not processed by Konvergo ERP.</p>
</div>

## Activer les modes de paiement locaux

Local payment methods are payment methods that are only available for specific
providers and for specific countries and currencies.

Konvergo ERP supports the following local payment methods for Stripe:

  * Bancontact

  * EPS

  * giropay

  * iDEAL

  * Przelewy24 (P24)

To adapt the list of enabled payment methods, go to the **Configuration** tab
and edit the list of **Supported Payment Icons**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>If a payment icon record does not exist in the database and its related local payment method is
listed above, it is automatically enabled with Stripe.</p></li>
<li><p>Si un mode de paiement local n’est pas répertorié ci-dessus, il n’est pas pris en charge et ne peut pas être activé.</p></li>
</ul>
</div>

## Activer Apple Pay

To allow customers to use the Apple Pay button to pay their eCommerce orders,
go to the **Configuration** tab, enable **Allow Express Checkout** , and click
**Enable Apple Pay**.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../payment_providers#payment-providers-express-checkout"><span class="std std-ref">Express checkout and Google Pay</span></a></p></li>
<li><p><a href="../payment_providers">Paiements en ligne</a></p></li>
<li><p><a href="../../sales/point_of_sale/payment_methods/terminals/stripe">Use Stripe as a payment terminal in Point of Sale</a></p></li>
</ul>
</div>

