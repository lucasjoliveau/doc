# Stripe

Connecting a payment terminal allows you to offer a fluid payment flow to your
customers and ease the work of your cashiers.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><ul>
<li><p>Stripe payment terminals do not require an <a href="../../../../general/iot">IoT Box</a></p></li>
<li><p>Stripe terminals can be used in many countries, but not worldwide. Check the <a href="https://support.stripe.com/questions/global-availability-for-stripe-terminal">global
availability for Stripe Terminal</a>.</p></li>
<li><p>Stripe’s integration works with <a href="https://docs.stripe.com/terminal/smart-readers">Stripe Terminal smart readers</a></p></li>
</ul>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../../../../finance/payment_providers/stripe">Stripe as payment provider</a></p></li>
<li><p><a href="https://stripe.com/payments/payment-methods">List of payment methods supported by Stripe</a></p></li>
</ul>
</div>

## Configuration

### Configure the payment method

Activate **Stripe** in the settings by going to Point of Sale ‣ Configuration
‣ Settings ‣ Payment Terminals and enabling **Stripe**.

Then, create the payment method:

  * Go to Point of Sale ‣ Configuration ‣ Payment Methods, click **Create** , and complete the **Method** field with your payment method’s name;

  * Set the **Journal** field as **Bank** and the **Use a Payment Terminal** field as **Stripe** ;

  * Enter your payment terminal serial number in the **Stripe Serial Number** field;

  * Click **Don’t forget to complete Stripe connect before using this payment method.**

![payment method creation form](../../../../../_images/create-method-
stripe.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Click <b>Identify Customer</b> to allow this payment method <b>exclusively</b> for identified
customers. For any unidentified customers to be able to pay with Stripe, leave the
<b>Identify Customer</b> field unchecked.</p></li>
<li><p>The <b>Outstanding Account</b> and the <b>Intermediary Account</b> can stay empty to
use the default accounts.</p></li>
<li><p>Find your payment terminal serial number under the device or on <a href="https://dashboard.stripe.com">Stripe’s dashboard</a>.</p></li>
</ul>
</div>

### Connect Stripe to Konvergo ERP

Click **Connect Stripe**. Doing so redirects you automatically to a
configuration page. Fill in all the information to create your Stripe account
and link it with Konvergo ERP. Once the forms are completed, the API keys
(**Publishable Key** and **Secret Key**) can be retrieved on **Stripe’s**
website. To do so, click **Get your Secret and Publishable keys** , click the
keys to copy them, and paste them into the corresponding fields in Konvergo ERP. Your
terminal is ready to be configured in a POS.

![stripe connection form](../../../../../_images/stripe-connect.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>When you use <b>Stripe</b> exclusively in Point of Sale, you only need the <b>Secret Key</b> to use
your terminal.</p></li>
<li><p>When you use Stripe as <b>payment provider</b>, the <b>State</b> can stay set as
<b>Disabled</b>.</p></li>
<li><p>For databases hosted <b>On-Premise</b>, the <b>Connect Stripe</b> button does not work. To
retrieve the API keys manually, log in to your <a href="https://dashboard.stripe.com">Stripe dashboard</a>, type <code>API</code> in the search bar, and click
<b>Developers &gt; API</b>.</p></li>
</ul>
</div>

### Configure the payment terminal

Swipe right on your payment terminal, click **Settings** , enter the admin PIN
code, validate and select your network.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>The device must be connected to a secured WI-FI network.</p></li>
<li><p>Your Konvergo ERP database and payment terminal must share the same network.</p></li>
<li><p>You must enter the admin PIN code to access your payment terminal settings. By default, this
code is <code>07139</code>.</p></li>
</ul>
</div>

### Link the payment method to a POS

To add a **payment method** to your point of sale, go to Point of Sale ‣
Configuration ‣ Settings. Select the POS, scroll down to the **Payments**
section, and add your payment method for **Stripe** in the **Payment Methods**
field.

## Pay with a payment terminal

When processing a payment, select **Stripe** as the payment method. Check the
amount and click **Send**. Once the payment is successful, the status changes
to **Payment Successful**. To cancel the payment request, click **cancel**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><div class="line-block">
<div class="line">In case of connection issues between Konvergo ERP and the payment terminal, force the payment by
clicking on <b>Force Done</b>, which allows you to validate the order.</div>
<div class="line">This option is only available after receiving an error message informing you that the
connection failed.</div>
</div>
</li>
<li><p>The terminal must have at least 10% battery level to use it.</p></li>
<li><p>The device does not work for payments under €0.50.</p></li>
</ul>
</div>

## Troubleshooting

### Payment terminal unavailable in your Stripe account

If the payment terminal is unavailable in your Stripe account, you must add it
manually:

  1. Log into your [Stripe’s dashboard](https://dashboard.stripe.com) and go to Stripe dashboard ‣ Payments ‣ Readers ‣ Locations;

  2. Add a location by clicking the **\+ New** button or selecting an already created location;

  3. Click the **\+ New** button in the **Readers** box and fill in the required information.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>You must provide a <b>registration code</b>. To retrieve that code, swipe right on your device,
enter the admin PIN code (by default: <code>07139</code>), validate, and click <b>Generate a
registration code</b>.</p>
</div>

