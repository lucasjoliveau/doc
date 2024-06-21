# SIPS

[SIPS](https://sips.worldline.com/) is an online payments solution from the
multinational Worldline.

## Configuration

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../payment_providers#payment-providers-add-new"><span class="std std-ref">Enable a payment provider</span></a></p></li>
</ul>
</div>

### Credentials tab

Konvergo ERP needs your **API Credentials** to connect with your SIPS account, which
comprise:

  * **Merchant ID** : The ID solely used to identify the merchant account with SIPS.

  * **Secret Key** : The key to sign the merchant account with SIPS.

  * **Secret Key Version** : The version of the key, pre-filled.

  * **Interface Version** : Pre-filled, don’t change it.

You can copy your credentials from your SIPS environment info documentation,
in the section **PROD** , and paste them in the related fields under the
**Credentials** tab.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If you are trying SIPS as a test, with the <em>TEST</em> credentials, change the <b>State</b> to <em>Test
Mode</em>. We recommend doing this on a test Konvergo ERP database, rather than on your main database.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../payment_providers">Online payments</a></p></li>
</ul>
</div>

