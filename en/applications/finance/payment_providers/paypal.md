# PayPal

[Paypal](https://www.paypal.com/) is an American online payment provider
available worldwide, and one of the few that does not charge a subscription
fee.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>While PayPal is available in <a href="https://www.paypal.com/webapps/mpp/country-worldwide">over 200 countries/regions</a>, only <a href="https://developer.paypal.com/docs/reports/reference/paypal-supported-currencies">a selection of currencies are
supported</a>.</p>
</div>

## Settings in PayPal

To access your PayPal account settings, log into PayPal, open the **Account
Settings** , and open the **Website payments** menu.

![PayPal account menu](../../../_images/paypal-account.png)
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Note that for PayPal to work <b>in Konvergo ERP</b>, the options <a href="#paypal-auto-return"><span class="std std-ref">Auto Return</span></a>,
<a href="#paypal-pdt"><span class="std std-ref">PDT</span></a>, and <a href="#paypal-ipn"><span class="std std-ref">IPN</span></a> <b>must</b> all be enabled.</p>
</div>

### Auto Return

The **Auto Return** feature automatically redirects customers to Konvergo ERP once the
payment is processed.

From **Website payments** , go to Website preferences ‣ Update ‣ Auto return
for website payments ‣ Auto return and select **On**. Enter the address of
your Konvergo ERP database (e.g., `https://yourcompany.odoo.com`) in the **Return
URL** field, and **Save**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Any URL does the job. Konvergo ERP only needs the setting to be enabled since it uses another URL.</p>
</div>

### Payment Data Transfer (PDT)

PDT allows to receive payment confirmations, displays the payment status to
the customers, and verifies the authenticity of the payments. From Website
preferences ‣ Update, scroll down to **Payment data transfer** and select
**On**.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>PayPal displays your <b>PDT Identity Token</b> as soon as <a href="#paypal-auto-return"><span class="std std-ref">Auto return</span></a>
and <a href="#paypal-pdt"><span class="std std-ref">Payment Data Transfer (PDT)</span></a> are enabled. If you need the <b>PDT Identity
Token</b>, disable and re-enable <b>Payment data transfer</b> to display the token again.</p>
</div>

### Instant Payment Notification (IPN)

IPN is similar to **PDT** , but allows for more notifications, such as
chargeback notifications. To enable **IPN** , go to Website payments ‣ Instant
payment notifications ‣ Update and click **Choose IPN settings**. Enter a
**Notification URL** , select **Receive IPN messages (Enabled)** , and
**Save**.

### PayPal Account Optional

We advise not to prompt customers to log in with a PayPal account upon
payment. It is better and more accessible for customers to pay with a
debit/credit card. To disable that prompt, go to Account Settings ‣ Website
payments ‣ Update and select **On** for **PayPal account optional**.

### Payment Messages Format

If you use accented characters (or anything other than primary Latin
characters) for customer names or addresses, then you **must** configure the
encoding format of the payment request sent by Konvergo ERP to PayPal. If you do not,
some transactions fail without notice.

To do so, go to [your production account](https://www.paypal.com/cgi-
bin/customerprofileweb?cmd=_profile-language-encoding). Then, click **More
Options** and set the two default encoding formats as **UTF-8**.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><ul>
<li><p>For Encrypted Website Payments &amp; EWP_SETTINGS error, please check the <a href="https://developer.paypal.com/docs/online/">Paypal documentation</a>.</p></li>
<li><p>Configure your <a href="#paypal-testing"><span class="std std-ref">Paypal Sandbox account</span></a>, then follow this
<a href="https://sandbox.paypal.com/cgi-bin/customerprofileweb?cmd=_profile-language-encoding">link</a>
to configure the encoding format in a test environment.</p></li>
</ul>
</div>

## Settings in Konvergo ERP

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../payment_providers#payment-providers-add-new"><span class="std std-ref">Enable a payment provider</span></a></p>
</div>

### Credentials

Konvergo ERP needs your **API Credentials** to connect with your PayPal account. To do
so, go to Accounting ‣ Configuration ‣ Payment Providers and **Activate**
PayPal. Then, enter your PayPal account credentials in the **Credentials**
tab:

  * **Email** : the login email address in Paypal;

  * **PDT Identity Token** : the key used to verify the authenticity of transactions;

  * **Use IPN** : enable for PayPal to work properly in Konvergo ERP.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Save the <b>PDT Identity Token</b> for later use.</p>
</div>

To set the **PDT Identity Token** , switch to [developer
mode](../../general/developer_mode#developer-mode) and retrieve the token
by following the configuration steps at Payment Data Transfer (PDT).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The PayPal <b>Merchant ID</b> is not required in Konvergo ERP.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If you are trying PayPal as a test, using a <a href="#paypal-testing"><span class="std std-ref">PayPal Sandbox account</span></a>,
change the <b>State</b> to <b>Test Mode</b>. We recommend doing this on a test Konvergo ERP
database rather than on your main database.</p>
</div>

### Extra fees

You can charge [extra fees](../payment_providers#payment-providers-extra-
fees) to customers choosing to pay with PayPal in order to cover the
transaction fees PayPal charges you.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>You can refer to <a href="https://www.paypal.com/webapps/mpp/paypal-fees">Paypal Fees</a> to set up
fees.</p></li>
<li><p><a href="https://europa.eu/youreurope/citizens/consumers/shopping/pricing-payments/index_en.htm">Traders in the EU</a>
are not allowed to charge extra fees for paying with credit cards.</p></li>
</ul>
</div>

## Test environment

### Configuration

Thanks to PayPal sandbox accounts, you can test the entire payment flow in
Konvergo ERP.

Log into the [Paypal Developer Site](https://developer.paypal.com/) using your
PayPal credentials, which creates two sandbox accounts:

  * A business account (to use as merchants, e.g., [pp.merch01-facilitator@example.com](mailto:pp.merch01-facilitator%40example.com));

  * A default personal account (to use as shoppers, e.g., [pp.merch01-buyer@example.com](mailto:pp.merch01-buyer%40example.com)).

Log into PayPal sandbox using the merchant account and follow the same
configuration instructions. Enter your sandbox credentials in Konvergo ERP (Accounting
‣ Configuration ‣ Payment Providers ‣ PayPal in the **Credentials** tab, and
make sure the status is set on **Test Mode**. We recommend doing this on a
test Konvergo ERP database rather than your main database.

Run a test transaction from Konvergo ERP using the sandbox personal account.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Note that for PayPal to work <b>in Konvergo ERP</b>, the options <a href="#paypal-auto-return"><span class="std std-ref">Auto Return</span></a>,
<a href="#paypal-pdt"><span class="std std-ref">PDT</span></a>, and <a href="#paypal-ipn"><span class="std std-ref">IPN</span></a> <b>must</b> all be enabled.</p>
</div>0

  *[PDT]: Payment Data Transfer
  *[IPN]: Instant Payment Notifications

