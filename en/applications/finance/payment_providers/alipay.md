# Alipay

[Alipay](https://www.alipay.com/) is an online payments platform established
in China by Alibaba Group.

Warning

The provider Alipay is deprecated. It is recommended to use
[AsiaPay](asiapay.html) instead.

## Configuration

See also

  * [Enable a payment provider](../payment_providers.html#payment-providers-add-new)

### Credentials tab

Odoo needs your **API Credentials** to connect with your Alipay account, which
comprise:

  * **Account** : Depending on where you are situated \- `Express Checkout` if your are a Chinese Merchant. \- `Cross-border` if you are not.

  * **Alipay Seller Email** : Your public Alipay partner email (for express checkout only).

  * **Merchant Partner ID** : The public partner ID solely used to identify the account with Alipay.

  * **MD5 Signature Key** : The signature key.

You can copy your credentials from your Alipay account, and paste them in the
related fields under the **Credentials** tab.

To retrieve them, log into your Alipay account, they are on the front page.

Important

If you are trying Alipay as a test, in the _sandbox_ , change the **State** to
_Test Mode_. We recommend doing this on a test Odoo database, rather than on
your main database.

See also

  * [Online payments](../payment_providers.html)

