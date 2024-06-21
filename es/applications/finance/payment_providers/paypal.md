# PayPal

[Paypal](https://www.paypal.com/) es un proveedor de pago en líne
estadounidense disponible en todo el mundo y es uno de los pocos que no cobran
un cargo por suscripción.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Aunque PayPal está disponible en <a href="https://www.paypal.com/webapps/mpp/country-worldwide">más de 200 países y regiones</a>, solo <a href="https://developer.paypal.com/docs/reports/reference/paypal-supported-currencies">unas cuantas divisas son compatibles</a>.</p>
</div>

## Configuración en PayPal

Para acceder a los ajustes de su cuenta de PayPal, inicie sesión en PayPal,
abra los **Ajustes de la cuenta** y abra el menú **Pagos en el sitio web**.

![Menú de la cuenta de PayPal](../../../_images/paypal-account.png)
<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Tenga en cuenta que para que PayPal funcione <b>en Konvergo ERP</b>, <b>deben</b> estar activadas las opciones <a href="#paypal-auto-return"><span class="std std-ref">Retorno automático</span></a>, <a href="#paypal-pdt"><span class="std std-ref">PDT</span></a> y <a href="#paypal-ipn"><span class="std std-ref">IPN</span></a>.</p>
</div>

### Retorno automático

La función de **Retorno automático** redirige automáticamente a los clientes a
Konvergo ERP una vez que se procesó el pago.

Desde **Pagos en el sitio web** , vaya a Preferencias del sitio web ‣
Actualizar ‣ Retorno automático para pagos en el sitio web ‣ Retorno
automático y seleccione **Activado**. Introduzca la dirección de su base de
datos de Konvergo ERP (por ejemplo, `https://yourcompany.odoo.com`) en el campo **URL
de retorno** y luego haga clic en **Guardar**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Cualquier URL funciona. Konvergo ERP solo necesita que la opción esté activada pues usa otra URL.</p>
</div>

### Transferencia de datos de pago (PDT)

La PDT le permite recibir las confirmaciones de los pagos, muestra el estado
del pago a sus clientes y verifica la autenticidad de los mismos. Desde
Preferencias del sitio web ‣ Actualizar, baje hasta encontrar **Transferencia
de datos de pago** y seleccione **Activar**.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>PayPal le muestra su <b>Token de identificación PDT</b> tan pronto como estén activadas las opciones <a href="#paypal-auto-return"><span class="std std-ref">Retorno automático</span></a> y <a href="#paypal-pdt"><span class="std std-ref">Transferencia de datos de pago (PDT)</span></a>. Si necesita el <b>Token de identificación PDT</b>, desactive y reactive la <b>Transferencia de datos de pago</b> para mostrar el token de nuevo.</p>
</div>

### Notificación de pago instantáneo (IPN)

La IPN es similar a la **PDT** , pero activa más notificaciones, como la
notificación de devolución del cargo. Para activar las **IPN** , vaya a Pagos
en el sitio web ‣ Notificaciones de pago instantáneas ‣ Actualizar y haga clic
en **Elegir ajustes de IPN**. Introduzca una **URL de notificación** ,
seleccione **Recibir mensajes de IPN (Activado)** y luego en **Guardar**.

### Cuenta opcional PayPal

Le recomendamos no pedirle a sus clientes que inicien sesión con su cuenta de
Paypal en el momento del pago. Es mejor y más accesible que paguen con una
tarjeta de crédito o débito. Para evitar que inicien sesión vaya a Ajustes de
la cuenta ‣ Pagos en el sitio web ‣ Actualizar y seleccionarlo como
**Activado** para la **Cuenta opcional PayPal**.

### Formato de mensajes de pago

Si uso caracteres acentuados (o algo más que caracteres latinos básicos) para
el nombre de sus clientes o direcciones, entonces **debe** configurar el
formato de codificación de la solicitud de pago que envia Konvergo ERP a PayPal. Si no
lo hace, algunas transacciones fallarán sin notificarle.

Para hacerlo, vaya a su [cuenta de producción](https://www.paypal.com/cgi-
bin/customerprofileweb?cmd=_profile-language-encoding). Luego, haga clic en
**Más Opciones** y establezca los dos formatos de codificación como **UTF-8**.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><ul>
<li><p>Para pagos encriptados en sitio web y errores EWP_SETTINGS, revise la <a href="https://developer.paypal.com/docs/online/">documentación de Paypal</a>.</p></li>
<li><p>Configure su <a href="#paypal-testing"><span class="std std-ref">Cuenta de Paypal Sandbox</span></a>, luego entre a este <a href="https://sandbox.paypal.com/cgi-bin/customerprofileweb?cmd=_profile-language-encoding">enlace</a> para configurar el formato de codificación en un entorno de prueba.</p></li>
</ul>
</div>

## Ajustes en Konvergo ERP

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../payment_providers#payment-providers-add-new"><span class="std std-ref">Activar un proveedor de pago</span></a></p>
</div>

### Credenciales

Konvergo ERP necesita sus **Credenciales API** para conectarse con su cuenta de
PayPal. Para hacerlo, vaya a Contabilidad ‣ Configuración ‣ Proveedores de
pago y **Active** PayPal. Luego, introduzca las credenciales de su cuenta de
PayPal en la pestaña de **Credenciales** :

  * **Correo electrónico** : la dirección de correo electrónico para iniciar sesión en Paypal;

  * **Token de identidad** : la clave que se usa para verificar la autenticidad de las transacciones;

  * **Usar IPN** : actívelo para que PayPal funcione adecuadamente en Konvergo ERP.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Guarde el <b>Token de identidad PDT</b> para usarlo después.</p>
</div>

Para establecer el **Token de identificación PDT** , cambie a [modo
desarrollador](../../general/developer_mode#developer-mode) y obtenga el
token siguiendo los pasos de configuración en Transferencia de datos de pago
(PDT).

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Konvergo ERP no requiere el <b>ID de comerciante</b> de PayPal.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Si está usando PayPal en modo prueba, usando una <a href="#paypal-testing"><span class="std std-ref">Cuenta sandbox PayPal</span></a>, cambie el <b>Estado</b> a <b>Entorno de prueba</b>. Le recomendamos hacerlo en una base de datos de prueba de Konvergo ERP en lugar de su base de datos principal.</p>
</div>

### Tarifas adicionales

Puede cobrar [cuotas adicionales](../payment_providers#payment-providers-
extra-fees) a los clientes que elijan pagar con PayPal para cubrir los cargos
por servicio que le cobra PayPal a usted.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Puede consultar las <a href="https://www.paypal.com/webapps/mpp/paypal-fees">Tarifas de PayPal</a> para establecer las suyas.</p></li>
<li><p><a href="https://europa.eu/youreurope/citizens/consumers/shopping/pricing-payments/index_en.htm">Los comerciantes de la UE</a> no tienen permitido cobrar cuotas adicionales por pagar con tarjetas de crédito.</p></li>
</ul>
</div>

## Entorno de prueba

### Configuración

Gracias a las cuentas sandbox de PayPal, puede probar el flujo de pago
completo en Konvergo ERP.

Inicie sesión en el [Sitio de desarrolladro de
PayPal](https://developer.paypal.com/) usando sus credenciales de PayPal, lo
que crea dos cuentas sandbox:

  * Una cuenta de negocios (para usar como comerciante, por ejemplo [pp.merch01-facilitator@example.com](mailto:pp.merch01-facilitator%40example.com));

  * Una cuenta personal predeterminada (para usarla como comprador, por ejemplo, [pp.merch01-buyer@example.com](mailto:pp.merch01-buyer%40example.com)).

Inicie sesión en sandbox de PayPal usando la cuenta de comerciante y siga las
mismas instrucciones de configuración. Introduzca sus credenciales sanbox en
Konvergo ERP (Contabilidad ‣ Configuración ‣ Proveedores de pago‣ PayPal en la pestaña
de **Credenciales** , y asegúrese de que el estado esté en **Ambiente de
prueba**.

Ejecute una transacción de prueba desde Konvergo ERP con la cuenta sandbox personal.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Tenga en cuenta que para que PayPal funcione <b>en Konvergo ERP</b>, <b>deben</b> estar activadas las opciones <a href="#paypal-auto-return"><span class="std std-ref">Retorno automático</span></a>, <a href="#paypal-pdt"><span class="std std-ref">PDT</span></a> y <a href="#paypal-ipn"><span class="std std-ref">IPN</span></a>.</p>
</div>0

  *[PDT]: Transferencia de Datos de Pago
  *[IPN]: Notificación de pago instántaneo

