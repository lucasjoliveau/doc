# Payment methods

To add a payment method, you first need to create it. Go to Point of Sale ‣
Configuration ‣ Payment Methods ‣ New, and set a name. Check **Identify
Customer** to allow this payment method _exclusively_ for registered
customers.

Then, select the **Journal**. Choose **Cash** to use this payment method for
cash payments, or **Bank** to use it for card payments.

![Creating a new payment method for a POS.](../../../_images/payment-
method.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Selecting a <b>bank</b> journal automatically adds the <b>Use a Payment Terminal</b>
field in which you can add your <a href="payment_methods/terminals">payment terminal’s information</a>.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="payment_methods/terminals">Payment terminals</a>.</p>
</div>

Once the payment method is created, you can select it in your POS settings. To
do so, go to the [POS’ settings](configuration#configuration-settings),
click **Edit** , and add the payment method under the **Payments** section.

  * [Payment terminals](payment_methods/terminals)
    * [Adyen](payment_methods/terminals/adyen)
    * [Ingenico](payment_methods/terminals/ingenico)
    * [SIX](payment_methods/terminals/six)
    * [Stripe](payment_methods/terminals/stripe)
    * [Vantiv](payment_methods/terminals/vantiv)
    * [Worldline](payment_methods/terminals/worldline)

