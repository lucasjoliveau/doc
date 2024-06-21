# SIX

Connecting a **SIX payment terminal** allows you to offer a fluid payment flow
to your customers and ease the work of your cashiers.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>Even though Worldline has acquired SIX Payment Services and both companies use Yomani payment
terminals, the firmware they run is different. Terminals received from Worldline are, therefore,
not compatible with this integration.</p>
</div>

## Configuration

### Install the POS IoT Six module

To activate the POS IoT Six module, go to **Apps** , remove the **Apps**
filter, and search for **POS IoT Six**. This module adds the necessary driver
and interface to your database to detect Six terminals.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This module replaces the <b>POS Six</b> module.</p>
</div>

### Connect an IoT box

Connecting a Six payment terminal to Konvergo ERP is requires [using a Raspberry Pi or
virtual (for Windows OS only) IoT
box](../../../../general/iot/config/connect).

### Configure the terminal ID

Navigate to your IoT Box homepage, where you can find the **Six payment
terminal** field once your database server is connected to the IoT box. Click
**Configure** , fill in the **Terminal ID** field with the ID received from
Six, and click **Connect**. Your Six terminal ID should appear in the
**Current Terminal Id** section.

![Setting the Six terminal ID](../../../../../_images/terminal-id.png)

Konvergo ERP automatically restarts the IoT box when the Six terminal ID is
configured. If your Six terminal is online, it will be automatically detected
and connected to the database. Check the IoT box homepage under the
**Payments** section to confirm the connection.

![Confirming the connection to the Six payment
terminal](../../../../../_images/id-configured.png)

### Configure the payment method

Enable the payment terminal [in the application
settings](../../configuration#configuration-settings) and [create the
related payment method](../../payment_methods). Set the journal type as
**Bank** and select **SIX IOT** in the **Use a Payment Terminal** field. Then,
select your terminal device in the **Payment Terminal Device** field.

![Creating a new payment method for the SIX payment
terminal](../../../../../_images/new-payment-method.png)

Once the payment method is created, you can select it in your POS settings. To
do so, go to the [POS’ settings](../../configuration#configuration-
settings), click **Edit** , and add the payment method under the **Payments**
section.

## Pay with a payment terminal

When processing a payment, select your Six payment method in the **Payment
Method** section and click **Send**. To cancel the payment request, click
**Cancel**. Once the payment is successful, the status switches to **Payment
Successful**.

![Paying with Six](../../../../../_images/payment.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Once your payment is processed, the type of card used and the transaction ID appear on the
payment record.</p></li>
<li><p>The language used for error messages is the same as the Six terminal. Configure the terminal to
change the language or contact Six.</p></li>
<li><p>By default, the port used by the Six terminal is <code>7784</code>.</p></li>
</ul>
</div>
<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If there are connection issues between the payment terminal and Konvergo ERP, you can still force the
payment validation in Konvergo ERP using the <b>Force Done</b> button.</p>
</div>

