# Worldline

Connecting a payment terminal allows you to offer a fluid payment flow to your
customers and ease the work of your cashiers.

Important

  * Worldline payment terminals require an [IoT Box](../../../../general/iot.html).

  * Worldline is currently only available in Belgium, the Netherlands and Luxembourg.

  * Odoo is compatible with Worldline terminals that use the CTEP protocol (e.g., the Yomani XR and Yoximo terminals). If you have any doubts, contact your payment provider to ensure your terminal’s compatibility.

## Configuration

### Connect an IoT Box

Connecting a Worldline Payment Terminal to Odoo is a feature that requires an
IoT Box. For more information on how to connect one to your database, please
refer to the [IoT documentation](../../../../general/iot/config/connect.html).

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

Example

Here’s an IP address sequence: `10.30.19.4:8069`.

On the _Hostname screen_ , type 10 ‣ OK ‣ 30 ‣ OK ‣ 19 ‣ OK ‣ 4 ‣ OK ‣ OK.

Note

Your IoT box’s IP address is available in your IoT Box application’s database.

#### Port number

On the _Port number_ screen, enter **9001** (or **9050** for Windows) and
click on OK (_ECR protocol SSL no_) ‣ OK. Click on **Stop** three times; the
terminal automatically restarts.

Warning

For **Windows** IoT devices, it is necessary to add a firewall exception.
Follow the [additional instructions in the Windows IoT
documentation](../../../../general/iot/config/windows_iot.html#iot-windows-
wordline) to add the exception to Windows Firewall.

### Configure the payment method

Enable the payment terminal [in the application
settings](../../configuration.html#configuration-settings) and [create the
related payment method](../../payment_methods.html). Set the journal type as
Bank and select Worldline in the Use a Payment Terminal field. Then, select
your terminal device in the Payment Terminal Device field.

![../../../../../_images/worldline-payment-
terminals.png](../../../../../_images/worldline-payment-terminals.png)

Once the payment method is created, you can select it in your POS settings. To
do so, go to the [POS’ settings](../../configuration.html#configuration-
settings), click Edit, and add the payment method under the Payments section.

Tip

  * Technician password: `1235789`

  * To reach Wordline’s technical assistance, call `02 727 61 11` and choose “merchant”. Your call is automatically transferred to the desired service.

  * Configure the cashier terminal if you have both a customer and a cashier terminal.

  * To avoid blocking the terminal, check the initial configuration beforehand.

  * Set a fixed IP to your IoT Box’s router to prevent losing the connexion.

## Pay with a payment terminal

When processing a payment, select _Worldline_ as payment method. Check the
amount and click on _Send_. Once the payment is successful, the status changes
to _Payment Successful_.

Once your payment is processed, the type of card used and the transaction ID
appear on the payment record.

![../../../../../_images/worldline-
payment.png](../../../../../_images/worldline-payment.png)

Note

  * In case of connexion issues between Odoo and the payment terminal, force the payment by clicking on _Force Done_ , which allows you to validate the order. This option is only available after receiving an error message informing you that the connection failed.

  * To cancel the payment request, click on **cancel**.

