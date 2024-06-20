# AsiaPay

[AsiaPay](https://www.asiapay.com/) is an online payments provider established
in Hong Kong and covering several Asian countries and payment methods.

## Configuration on AsiaPay Dashboard

  1. Log into [AsiaPay Dashboard](https://www.paydollar.com/b2c2/eng/merchant/index.jsp) and go to Profile ‣ Account Information. Copy the values of the Currency and Secure Hash fields and save them for later.

  2. Go to Profile ‣ Payment Account Settings and enable the options Return Value Link (Datefeed)

Enter your Odoo database URL followed by `/payment/asiapay/webhook` in the
Return Value Link (Datefeed) text field.

For example: `https://yourcompany.odoo.com/payment/asiapay/webhook`.

Click on Test to check if the webhook is working correctly.

  3. Click on Update to finalize the configuration.

## Configuration on Odoo

  1. [Navigate to the payment provider AsiaPay](../payment_providers.html#payment-providers-add-new) and change its state to Enabled.

  2. In the Credentials tab, fill the Merchant ID, Currency, and Secure Hash Secret with the values you saved at the step Configuration on AsiaPay Dashboard.

By default, the payment provider AsiaPay is configured to verify the secret
hash with the hash function `SHA1`. If a different function is set on your
account, activate the [developer
mode](../../general/developer_mode.html#developer-mode) and set the same value
to the field Secure Hash Function in Odoo.

  3. Configure the rest of the options to your liking.

See also

  * [Online payments](../payment_providers.html)
