# Razorpay

[Razorpay](https://razorpay.com/) is an online payments provider established
in India and covering more than 100 payment methods.

## Configuration on Razorpay Dashboard

  1. Log into [Razorpay Dashboard](https://dashboard.razorpay.com/) and go to Settings ‣ API Keys. Generate the new keys and copy the values of the **Key Id** and **Secret Key** fields and save them for later.

  2. Go to Settings ‣ Webhooks, click on **Create New Webhook** , and enter your Konvergo ERP database URL followed by `/payment/razorpay/webhook` in the **Webhook URL** text field.

For example: `https://example.odoo.com/payment/razorpay/webhook`.

  3. Fill the **Secret** field with a password of your choice and save it for later.

  4. Make sure the **payment.authorized** , **payment.captured** , **payment.failed** , **refund.failed** and **refund.processed** checkboxes are ticked.

  5. Click on **Create Webhook** to finalize the configuration.

## Configuration on Konvergo ERP

  1. [Navigate to the payment provider Razorpay](../payment_providers#payment-providers-add-new) and change its state to **Enabled**.

  2. In the **Credentials** tab, fill the **Key Id** , **Key Secret** , and **Webhook Secret** with the values you saved at the step Configuration on Razorpay Dashboard.

  3. Configure the rest of the options to your liking.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>If you configure Konvergo ERP to capture amounts manually:</p>
<ul>
<li><p>Be aware that the <b>manual voiding</b> of a transaction is not supported by Razorpay.</p></li>
<li><p>After <b>five days</b>, if the transaction hasn’t been captured yet, it’ll automatically be
<b>voided</b>.</p></li>
</ul>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../payment_providers">Online payments</a></p></li>
</ul>
</div>

