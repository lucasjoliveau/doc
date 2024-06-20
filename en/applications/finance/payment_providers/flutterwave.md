# Flutterwave

[Flutterwave](https://flutterwave.com/) is an online payments provider
established in Nigeria and covering several African countries and payment
methods.

## Configuration on Flutterwave Dashboard

  1. Log into [Flutterwave Dashboard](https://dashboard.flutterwave.com/) and go to Settings ‣ API. Copy the values of the Public Key and Secret Key fields and save them for later.

  2. Go to Settings ‣ Webhooks and enter your Odoo database URL followed by `/payment/flutterwave/webhook` in the URL text field.

For example: `https://yourcompany.odoo.com/payment/flutterwave/webhook`.

  3. Fill the Secret hash with a password that you generate and save its value for later.

  4. Make sure _all_ the remaining checkboxes are ticked.

  5. Click on **Save** to finalize the configuration.

![Flutterwave settings](../../../_images/flutterwave-settings.png)

## Configuration on Odoo

  1. [Navigate to the payment provider Flutterwave](../payment_providers.html#payment-providers-add-new) and change its state to Enabled.

  2. In the Credentials tab, fill the Public Key, Secret Key, and Webhook Secret with the values you saved at the step Configuration on Flutterwave Dashboard.

  3. Configure the rest of the options to your liking.

Important

If you choose to allow saving payment methods, it is recommended to only
enable card payments from Flutterwave dashboard, as only cards can be saved as
payment tokens. To do so, go to your Flutterwave Dashboard and then to
Settings ‣ Account Settings.

See also

  * [Online payments](../payment_providers.html)
