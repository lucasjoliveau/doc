# Ogone

[Ogone](https://www.ingenico.com/), also known as **Ingenico Payment
Services** is a France-based company that provides the technology involved in
secure electronic transactions.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../payment_providers#payment-providers-add-new"><span class="std std-ref">Enable a payment provider</span></a></p></li>
<li><p><a href="https://epayments-support.ingenico.com/get-started/">Ogone’s documentation</a>.</p></li>
</ul>
</div> <div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>The provider Ogone is deprecated. It is recommended to use <a href="stripe">Stripe</a> instead.</p>
</div>

## Settings in Ogone

### Create an API user

Log into your Ogone account and head to the **Configuration** tab.

You need to create an **API user** to be used in the creation of transactions
from Konvergo ERP. While you can use your main account to do so, using an **API user**
ensures that if the credentials used in Konvergo ERP are leaked, no access to your
Ogone configuration is possible. Additionally, passwords for **API users** do
not need to be updated regularly, unlike normal users.

To create an **API user** , go to Configuration ‣ Users and click on **New
User**. The following fields must be configured:

  * **UserID** : you can choose anything you want.

  * **User’s Name, E-mail and Timezone** : you can enter the information you want.

  * **Profile** : should be set to **Admin**.

  * **Special user for API** : should be checked.

After the creation of the user, you are required to generate a password. Save
the password and **UserID** , as they will be required later on during the
setup.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If you already have an user set up, make sure it is activated without any error. If not, simply
click the <b>Activate(Errors)</b> button to reset the user.</p>
</div>

### Set up Ogone for Konvergo ERP

Ogone must now be configured to accept payments from Konvergo ERP. Head to
Configuration ‣ Technical Information ‣ Global Security Parameters, select
**SHA-512** as **Hash Algorithm** and **UTF-8** as **character encoding**.
Then, go to the **Data and Origin verification** tab of the same page and
leave the URL field of the **e-Commerce and Alias Gateway** section blank.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If you need to use another algorithm, such as <code>sha-1</code> or <code>sha-256</code>, within Konvergo ERP, activate the
<a href="../../general/developer_mode#developer-mode"><span class="std std-ref">developer mode</span></a> and go to the <b>Payment Providers</b> page in
Accounting ‣ Configuration ‣ Payment Providers. Click on <b>Ogone</b>,
and in the <b>Credentials</b> tab, select the algorithm you wish to use in the
<b>Hash function</b> field.</p>
</div>

You are now required to generate **SHA-IN** passphrases. **SHA-IN** and **SHA-
OUT** passphrases are used to digitally sign the transaction requests and
responses between Konvergo ERP and Ogone. By using these secret passphrases and the
`sha-1` algorithm, both systems can ensure that the information they receive
from the other was not altered or tampered with.

Enter the same **SHA-IN** passphrase in both **Checks for e-Commerce & Alias
Gateway** and **Checks for DirectLink and Batch (Automatic)**. You can leave
the IP address field blank.

Your **SHA-IN** and **SHA-OUT** passphrases should be different, and between
16 and 32 characters long. Make sure to use the same **SHA-IN** and **SHA-
OUT** passphrases throughout the entire Ogone configuration, as Konvergo ERP only
allows a single **SHA-IN** and single **SHA-OUT** passphrase.

In order to retrieve the **SHA-OUT** key, log into your Ogone account, go to
Configuration ‣ Technical Information ‣ Transaction feedback ‣ All transaction
submission modes, and get or generate your **API Key** and **Client Key**. Be
careful to copy your API key as you’ll not be allowed to get it later without
generating a new one.

When done, head to Configuration ‣ Technical Information ‣ Transaction
Feedback and check the following options:

  * The **URL** fields for **HTTP redirection in the browser** can be left empty, as Konvergo ERP will specify these URLs for every transaction request.

  * **I would like to receive transaction feedback parameters on the redirection URLs** : should be checked.

  * **Direct HTTP server-to-server request** : should to be set to `Online but switch to a deferred request when the online request fails`.

  * Both **URL** fields should contain the same following URL, with `<example>` replaced by your database: `https://<example>/payment/ogone/return`.

  * **Dynamic eCommerce Parameters** should contain the following values: `ALIAS`, `AMOUNT`, `CARDNO`, `CN`, `CURRENCY`, `IP`, `NCERROR` `ORDERID`, `PAYID`, `PM`, `STATUS`, `TRXDATE`. Other parameters can be included (if you have another integration with Ogone that requires them), but are not advised.

  * In the **All transaction submission modes** section, fill out **SHA-OUT** passphrase and disable `HTTP request for status change`.

To allow your customers to save their credit card credentials for future use,
head to Configuration ‣ Alias ‣ My alias information. From this tab, you can
configure how the user can have its card details saved, for how long the
information is saved, if a checkbox to save the card information should be
displayed, etc.

## Settings in Konvergo ERP

To set up Ogone in Konvergo ERP, head to Accounting ‣ Configuration ‣ Payment
Providers and open the Ogone provider. In the **Credentials** tab, enter the
**PSPID** of your Ogone account, and fill out the other fields as configured
in your Ogone portal.

