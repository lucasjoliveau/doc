# Adyen

Connecting an **Adyen payment terminal** allows you to offer a fluid payment
flow to your customers and ease the work of your cashiers.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><ul>
<li><p>Adyen payment terminals do not require an <a href="../../../../general/iot">IoT Box</a>.</p></li>
<li><p>Adyen terminals can be used in many countries, but not worldwide. Check the <a href="https://docs.adyen.com/point-of-sale/what-we-support/supported-languages/">List of countries
supported by Adyen</a>.</p></li>
<li><p>Adyen works only with businesses processing more than <b>$10 million annually</b> or invoicing a
minimum of <b>1,000 transactions per month</b>.</p></li>
</ul>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="https://docs.adyen.com/point-of-sale/what-we-support/payment-methods/">List of payment methods supported by Adyen</a></p></li>
<li><p><a href="https://docs.adyen.com/point-of-sale/what-we-support/select-your-terminals/">List of Adyen terminals</a></p></li>
</ul>
</div>

## Configuration

Start by creating your Adyen account on [Adyen’s
website](https://www.adyen.com/). Then, board your terminal following the
steps described on your terminal’s screen.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="https://docs.adyen.com/point-of-sale/user-manuals">Adyen Docs - Payment terminal quickstart guides</a></p>
</div>

### Generate an Adyen API key

The **Adyen API key** is used to authenticate requests from your Adyen
terminal. To generate an API key, go to your Adyen account ‣ Developers ‣ API
credentials, and **create** new credentials or select **existing** ones. Click
**Generate an API key** and save the key to paste it into the Konvergo ERP **Adyen API
key** field at the payment method creation.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="https://docs.adyen.com/development-resources/api-credentials#generate-api-key">Adyen Docs - API credentials</a>.</p></li>
</ul>
</div>

### Locate the Adyen terminal identifier

The **Adyen Terminal Identifier** is the terminal’s serial number, which is
used to identify the hardware.

To find this number, go to your Adyen account ‣ Point of Sale ‣ Terminals,
select the terminal to link with, and save its serial number to paste it into
the Konvergo ERP **Adyen Terminal Identifier** field at the payment method creation.

### Set the Event URLs

For Konvergo ERP to know when a payment is made, you must configure the terminal
**Event URLs**. To do so,

  1. Log in to [Adyen’s website](https://www.adyen.com/);

  2. Go to Adyen’s dashboard ‣ Point of Sale ‣ Terminals and select the connected terminal;

  3. From the terminal settings, click **Integrations** ;

  4. Set the **Switch to decrypted mode to edit this setting** field as **Decrypted** ;

  5. Click the **pencil icon** button and enter your server address, followed by `/pos_adyen/notification` in the **Event URLs** field;

  6. Click **Save** at the bottom of the screen to save changes.

### Configure the payment method

Enable the payment terminal [in the application
settings](../../configuration#configuration-settings) and [create the
related payment method](../../payment_methods). Set the journal type as
**Bank** and select **Adyen** in the **Use a Payment Terminal** field.

Finally, fill in the mandatory fields with your Adyen API key, Adyen Terminal
Identifier, and **Adyen Merchant Account**.

![../../../../../_images/payment-method1.png](../../../../../_images/payment-
method1.png)

Once the payment method is created, you can select it in your POS settings. To
do so, go to the [POS’ settings](../../configuration#configuration-
settings), click **Edit** , and add the payment method under the **Payments**
section.

## Pay with a payment terminal

When processing a payment, select **Adyen** as the payment method. Check the
amount and click on **Send**. Once the payment is successful, the status
changes to **Payment Successful**.

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
<li><p>To cancel the payment request, click on <b>cancel</b>.</p></li>
</ul>
</div>

