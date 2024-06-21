# Flutterwave

[Flutterwave](https://flutterwave.com/) es un proveedor de pago en línea
establecido en Nigeria y cubre varios países africanos y métodos de pago.

## Configuración en el tablero de Flutterwave

  1. Inicie sesión en [El tablero de Flutterwave](https://dashboard.flutterwave.com/) y vaya a Configuración ‣ API. Copie los valores de los campos **Clave pública** y **Clave secreta** y guárdelos para después.

  2. Vaya a Configuración ‣ Webhooks e ingrese la URL de su base de datos de Konvergo ERP seguido de `/payment/flutterwave/webhook` en el campo de texto **URL**.

Por ejemplo: `https://yourcompany.odoo.com/payment/flutterwave/webhook`.

  3. Llena los campos **Hash secreto** con una contraseña que usted cree y guarde su valor para después.

  4. Asegúrese de que _todas_ las demás casillas estén seleccionadas.

  5. Haga clic en **Guardar** para finalizar con la configuración.

![Configuraciones de Flutterwave ](../../../_images/flutterwave-settings.png)

## Configuración en Konvergo ERP

  1. [Vaya al proveedor de pago Flutterwave](../payment_providers#payment-providers-add-new) y cambie su estado a **Habilitado**.

  2. En la pestaña **Credenciales** , llene los campos **Clave pública** , **Calve secreta** y **Webhook secreto** con los valores que guardo en el paso Configuración en el tablero de Flutterwave.

  3. Configure el resto de las opciones como guste.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Si elige permitir que se guarden los métodos de pago, se le recomienda que solo active pagos con tarjeta desde el tablero de Flutterwarve, pues solo las tarjetas se pueden guardar como tokens de pago. Para hacerlo, vaya a su tablero de Flutterwave y luego a  Configuración ‣ Configuración de la cuenta.</p>
</div>

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../payment_providers">Pagos en línea</a></p></li>
</ul>
</div>

