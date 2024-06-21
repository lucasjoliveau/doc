# Razorpay

[Razorpay](https://razorpay.com/) es un porveedor de pagos establecido en la
India y cubre más de 100 métodos de pago.

## Configuración en el tablero de RazorPay

  1. Inicie sesión en [el tablero de Razorpay](https://dashboard.razorpay.com/) y vaya a Configuración ‣ Claves API. Genere las nuevas claves y copie los valores de los campos **Clave ID** y de **Calve secreta** y guárdelos para después.

  2. Vaya a Configruación ‣ Webhooks, haga clic en **Crear un nuevo Webhook** , e ingrese la URL de su base de datos de Konvergo ERP seguido de `/payment/razorpay/webhook` en el campo de texto **URL Webhook**.

Por ejemplo: `https://example.odoo.com/payment/razorpay/webhook`.

  3. Llene el campo **Secreto** con la contraseña de su preferencia y guárdela para después.

  4. Asegúrese de que las casillas **pago.autorizado** , **pago.capturado** , **pago.fallido** , **reembolso.fallido** y **reembolso.procesado** estén seleccionadas.

  5. Haga clic en **Cree un Webhook** para finalizar con la configruación.

## Configuración en Konvergo ERP

  1. [Vaya al proveedor de pago Razorpay](../payment_providers#payment-providers-add-new) y cambie su estado a **Habilitado**.

  2. En la pestaña **Credenciales** , llene los campos **ID de clave** , **Clave secreta** , y **Webhook secreto** con los valores que guardo en el paso Configuración en el tablero de RazorPay.

  3. Configure el resto de las opciones como guste.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Si configura Konvergo ERP para que capture los importes manualmente:</p>
<ul>
<li><p>Tenga en cuenta que Razorpay no admite la <b>anulación manual</b> de una transacción.</p></li>
<li><p>Después de <b>cinco dias</b>, si no se ha capturado aún la transacción, se <b>anulará</b> automáticamente.</p></li>
</ul>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../payment_providers">Pagos en línea</a></p></li>
</ul>
</div>

