# Alipay

[Alipay](https://www.alipay.com/) is an online payments platform established
in China by Alibaba Group.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>The provider Alipay is deprecated. It is recommended to use <a href="asiapay">AsiaPay</a> instead.</p>
</div>

## Configuration

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../payment_providers#payment-providers-add-new"><span class="std std-ref">Enable a payment provider</span></a></p></li>
</ul>
</div>

### Credentials tab

Konvergo ERP needs your **API Credentials** to connect with your Alipay account, which
comprise:

  * **Account** : Depending on where you are situated \- `Express Checkout` if your are a Chinese Merchant. \- `Cross-border` if you are not.

  * **Alipay Seller Email** : Your public Alipay partner email (for express checkout only).

  * **Merchant Partner ID** : The public partner ID solely used to identify the account with Alipay.

  * **MD5 Signature Key** : The signature key.

You can copy your credentials from your Alipay account, and paste them in the
related fields under the **Credentials** tab.

To retrieve them, log into your Alipay account, they are on the front page.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If you are trying Alipay as a test, in the <em>sandbox</em>, change the <b>State</b> to <em>Test Mode</em>. We
recommend doing this on a test Konvergo ERP database, rather than on your main database.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../payment_providers">Online payments</a></p></li>
</ul>
</div>

