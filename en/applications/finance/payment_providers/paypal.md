# PayPal

[Paypal](https://www.paypal.com/) is an American online payment provider
available worldwide, and one of the few that does not charge a subscription
fee.

Note

While PayPal is available in [over 200
countries/regions](https://www.paypal.com/webapps/mpp/country-worldwide), only
[a selection of currencies are
supported](https://developer.paypal.com/docs/reports/reference/paypal-
supported-currencies).

## Settings in PayPal

To access your PayPal account settings, log into PayPal, open the Account
Settings, and open the Website payments menu.

![PayPal account menu](../../../_images/paypal-account.png)

Important

Note that for PayPal to work **in Odoo** , the options Auto Return, PDT, and
IPN **must** all be enabled.

### Auto Return

The **Auto Return** feature automatically redirects customers to Odoo once the
payment is processed.

From Website payments, go to Website preferences ‣ Update ‣ Auto return for
website payments ‣ Auto return and select On. Enter the address of your Odoo
database (e.g., `https://yourcompany.odoo.com`) in the Return URL field, and
Save.

Note

Any URL does the job. Odoo only needs the setting to be enabled since it uses
another URL.

### Payment Data Transfer (PDT)

PDT allows to receive payment confirmations, displays the payment status to
the customers, and verifies the authenticity of the payments. From Website
preferences ‣ Update, scroll down to Payment data transfer and select On.

Tip

PayPal displays your **PDT Identity Token** as soon as Auto return and Payment
Data Transfer (PDT) are enabled. If you need the **PDT Identity Token** ,
disable and re-enable Payment data transfer to display the token again.

### Instant Payment Notification (IPN)

IPN is similar to **PDT** , but allows for more notifications, such as
chargeback notifications. To enable **IPN** , go to Website payments ‣ Instant
payment notifications ‣ Update and click Choose IPN settings. Enter a
Notification URL, select Receive IPN messages (Enabled), and Save.

### PayPal Account Optional

We advise not to prompt customers to log in with a PayPal account upon
payment. It is better and more accessible for customers to pay with a
debit/credit card. To disable that prompt, go to Account Settings ‣ Website
payments ‣ Update and select On for PayPal account optional.

### Payment Messages Format

If you use accented characters (or anything other than primary Latin
characters) for customer names or addresses, then you **must** configure the
encoding format of the payment request sent by Odoo to PayPal. If you do not,
some transactions fail without notice.

To do so, go to [your production account](https://www.paypal.com/cgi-
bin/customerprofileweb?cmd=_profile-language-encoding). Then, click More
Options and set the two default encoding formats as UTF-8.

Tip

  * For Encrypted Website Payments & EWP_SETTINGS error, please check the [Paypal documentation](https://developer.paypal.com/docs/online/).

  * Configure your Paypal Sandbox account, then follow this [link](https://sandbox.paypal.com/cgi-bin/customerprofileweb?cmd=_profile-language-encoding) to configure the encoding format in a test environment.

## Settings in Odoo

See also

[Enable a payment provider](../payment_providers.html#payment-providers-add-
new)

### Credentials

Odoo needs your **API Credentials** to connect with your PayPal account. To do
so, go to Accounting ‣ Configuration ‣ Payment Providers and Activate PayPal.
Then, enter your PayPal account credentials in the Credentials tab:

  * Email: the login email address in Paypal;

  * PDT Identity Token: the key used to verify the authenticity of transactions;

  * Use IPN: enable for PayPal to work properly in Odoo.

Tip

Save the PDT Identity Token for later use.

To set the PDT Identity Token, switch to [developer
mode](../../general/developer_mode.html#developer-mode) and retrieve the token
by following the configuration steps at Payment Data Transfer (PDT).

Note

The PayPal **Merchant ID** is not required in Odoo.

Important

If you are trying PayPal as a test, using a PayPal Sandbox account, change the
State to Test Mode. We recommend doing this on a test Odoo database rather
than on your main database.

### Extra fees

You can charge [extra fees](../payment_providers.html#payment-providers-extra-
fees) to customers choosing to pay with PayPal in order to cover the
transaction fees PayPal charges you.

Note

  * You can refer to [Paypal Fees](https://www.paypal.com/webapps/mpp/paypal-fees) to set up fees.

  * [Traders in the EU](https://europa.eu/youreurope/citizens/consumers/shopping/pricing-payments/index_en.htm) are not allowed to charge extra fees for paying with credit cards.

## Test environment

### Configuration

Thanks to PayPal sandbox accounts, you can test the entire payment flow in
Odoo.

Log into the [Paypal Developer Site](https://developer.paypal.com/) using your
PayPal credentials, which creates two sandbox accounts:

  * A business account (to use as merchants, e.g., [pp.merch01-facilitator@example.com](mailto:pp.merch01-facilitator%40example.com));

  * A default personal account (to use as shoppers, e.g., [pp.merch01-buyer@example.com](mailto:pp.merch01-buyer%40example.com)).

Log into PayPal sandbox using the merchant account and follow the same
configuration instructions. Enter your sandbox credentials in Odoo (Accounting
‣ Configuration ‣ Payment Providers ‣ PayPal in the Credentials tab, and make
sure the status is set on Test Mode. We recommend doing this on a test Odoo
database rather than your main database.

Run a test transaction from Odoo using the sandbox personal account.

See also

  * [Online payments](../payment_providers.html)

  *[PDT]: Payment Data Transfer
  *[IPN]: Instant Payment Notifications

