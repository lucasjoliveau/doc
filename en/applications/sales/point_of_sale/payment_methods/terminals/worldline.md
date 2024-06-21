# Worldline

Connecting a payment terminal allows you to offer a fluid payment flow to your
customers and ease the work of your cashiers.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><ul>
<li><p>Worldline payment terminals require an <a href="../../../../general/iot">IoT Box</a>.</p></li>
<li><p>Worldline is currently only available in Belgium, the Netherlands and Luxembourg.</p></li>
<li><p>Konvergo ERP is compatible with Worldline terminals that use the CTEP protocol (e.g., the Yomani XR and
Yoximo terminals). If you have any doubts, contact your payment provider to ensure your
terminal’s compatibility.</p></li>
</ul>
</div>

## Configuration

### Connect an IoT Box

Connecting a Worldline Payment Terminal to Konvergo ERP is a feature that requires an
IoT Box. For more information on how to connect one to your database, please
refer to the [IoT documentation](../../../../general/iot/config/connect).

### Configure the protocol

From your terminal, click on “.” ‣ 3 ‣ stop ‣ 3 ‣ 0 ‣ 9. Enter the technician
password **“1235789”** and click on OK ‣ 4 ‣ 2. Then, click on Change ‣ CTEP
(as Protocole ECR) ‣ OK. Click on **OK** thrice on the subsequent screens
(_CTEP ticket ECR_ , _ECR ticket width_ , and _Character set_). Finally, press
**Stop** three times; the terminal automatically restarts.

### Set the IP address

From your terminal, click on “.” ‣ 3 ‣ stop ‣ 3 ‣ 0 ‣ 9. Enter the technician
password **“1235789”** and click on OK ‣ 4 ‣ 9. Then, click on Change ‣ TCP/IP
(_TCP physical configuration_ screen) ‣ OK ‣ OK (_TCP Configuration client_
screen).

Finally, set up the hostname and port number.

#### Hostname

To set up the hostname, enter your IoT box’s IP address’ sequence numbers and
press **OK** at each “.” until you reach the colon symbol.

Then, press **OK** twice.

<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="line-block">
<div class="line">Here’s an IP address sequence: <code>10.30.19.4:8069</code>.</div>
<div class="line">On the <em>Hostname screen</em>, type 10 ‣ OK ‣ 30 ‣ OK ‣ 19 ‣ OK ‣ 4
‣ OK ‣ OK.</div>
</div>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Your IoT box’s IP address is available in your IoT Box application’s database.</p>
</div>

#### Port number

On the _Port number_ screen, enter **9001** (or **9050** for Windows) and
click on OK (_ECR protocol SSL no_) ‣ OK. Click on **Stop** three times; the
terminal automatically restarts.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>For <b>Windows</b> IoT devices, it is necessary to add a firewall exception. Follow the
<a href="../../../../general/iot/config/windows_iot#iot-windows-wordline"><span class="std std-ref">additional instructions in the Windows IoT documentation</span></a> to add the
exception to Windows Firewall.</p>
</div>

### Configure the payment method

Enable the payment terminal [in the application
settings](../../configuration#configuration-settings) and [create the
related payment method](../../payment_methods). Set the journal type as
**Bank** and select **Worldline** in the **Use a Payment Terminal** field.
Then, select your terminal device in the **Payment Terminal Device** field.

![../../../../../_images/worldline-payment-
terminals.png](../../../../../_images/worldline-payment-terminals.png)

Once the payment method is created, you can select it in your POS settings. To
do so, go to the [POS’ settings](../../configuration#configuration-
settings), click **Edit** , and add the payment method under the **Payments**
section.

<div class="alert alert-info" id="worldline-yomani-info">
<p class="alert-title">
Tip</p><ul>
<li><p>Technician password: <code>1235789</code></p></li>
<li><p>To reach Wordline’s technical assistance, call <code>02 727 61 11</code> and choose “merchant”. Your call
is automatically transferred to the desired service.</p></li>
<li><p>Configure the cashier terminal if you have both a customer and a cashier terminal.</p></li>
<li><p>To avoid blocking the terminal, check the initial configuration beforehand.</p></li>
<li><p>Set a fixed IP to your IoT Box’s router to prevent losing the connexion.</p></li>
</ul>
</div>

## Pay with a payment terminal

When processing a payment, select _Worldline_ as payment method. Check the
amount and click on _Send_. Once the payment is successful, the status changes
to _Payment Successful_.

Once your payment is processed, the type of card used and the transaction ID
appear on the payment record.

![../../../../../_images/worldline-
payment.png](../../../../../_images/worldline-payment.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>In case of connexion issues between Konvergo ERP and the payment terminal, force the payment by
clicking on <em>Force Done</em>, which allows you to validate the order. This option is only available
after receiving an error message informing you that the connection failed.</p></li>
<li><p>To cancel the payment request, click on <b>cancel</b>.</p></li>
</ul>
</div>

