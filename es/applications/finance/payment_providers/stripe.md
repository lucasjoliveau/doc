# Stripe

[Stripe](https://stripe.com/) es un proveedor de soluciones de pago en línea
con sede en Estados Unidos con el que las empresas pueden aceptar **tarjetas
de crédito** y otros métodos de pago.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="https://stripe.com/global">Lista de países compatibles con Stripe</a></p></li>
<li><p><a href="https://stripe.com/payments/payment-methods">Lista de métodos de pago compatibles con Stripe</a></p></li>
</ul>
</div>

## Cree su cuenta de Stripe con Konvergo ERP

El método para obtener sus credenciales depende de su tipo de alojamiento:

Konvergo ERP OnlineKonvergo ERP.sh or On-premise

  1. [Vaya al proveedor de pago Stripe](../payment_providers#payment-providers-supported-providers) y haga clic en **Conectar Stripe**.

  2. Siga el proceso de configuración y confirme su dirección de correo cuando Stripe le envíe un correo de confirmación.

  3. Al final del proceso, haga clic en **Agree and submit** (estoy de acuerdo y enviar). Si se envió toda la información solicitada regresará a Konvergo ERP y se activará su proveedor de pago.

  4. Activar métodos de pago locales.

  1. [Vaya al proveedor de pago Stripe](../payment_providers#payment-providers-supported-providers) y haga clic en **Conectar Stripe**.

  2. Siga el proceso de configuración y confirme su dirección de correo cuando Stripe le envíe un correo de confirmación.

  3. Al final del proceso, haga clic en **Agree and submit** (estoy de acuerdo y enviar). Se le redirigirá al proveedor de pago **Stripe** dentro de Konvergo ERP

  4. Introduzca sus credenciales.

  5. Genere un webhook.

  6. Seleccione un [diario de pago](../payment_providers#payment-providers-journal).

  7. Configure el campo **Estado** como **Habilitado**.

  8. Activar métodos de pago locales.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><ul>
<li><p>Para usar una cuenta de Stripe existente,  <a href="../../general/developer_mode#developer-mode"><span class="std std-ref">active el modo desarrollador</span></a> y <a href="../payment_providers#payment-providers-add-new"><span class="std std-ref">active Stripe manualmente</span></a>. Entonces podrá <span class="xref std std-ref">completar sus credenciales</span>, <a href="#stripe-webhook"><span class="std std-ref">generar un webhook</span></a> y establecer su proveedor de pago.</p></li>
<li><p>También puede probar Stripe con el <a href="../payment_providers#payment-providers-test-mode"><span class="std std-ref">Modo de prueba</span></a> (modo de prueba de proveedores de pago). Para hacerlo, primero  <a href="https://dashboard.stripe.com/dashboard">inicie sesión en su tablero de Stripe</a> y cambie al <b>modo de prueba</b>. Después en Konvergo ERP <a href="../../general/developer_mode#developer-mode"><span class="std std-ref">active el modo de Desarrollador</span></a>, <a href="../payment_providers#payment-providers-supported-providers"><span class="std std-ref">vaya al proveedor de pago Stripe</span></a>, <a href="#stripe-api-keys"><span class="std std-ref">llene las credenciales de su API</span></a> con las claves de prueba y configure elm:guilabel:<code>Estado</code> como <b>Modo de prueba</b>.</p></li>
</ul>
</div>

### Complete sus credenciales

Si necesita sus **credenciales API** para conectar con su cuenta de Stripe,
haga lo siguiente:

  1. Vaya a [la página de claves API de Stripe](https://dashboard.stripe.com/account/apikeys), o inicie sesión en su tablero de Stripe y vaya a :menuselection:`Desarrolladores –> Claves API.

  2. En la sección **Standard keys** (claves estándar) copie la **Publishable key** (clave pública) y la **Secret key** (clave secreta) y guárdelas para que pueda usarlas después.

  3. En Konvergo ERP [vaya al proveedor de pago de Stripe](../payment_providers#payment-providers-supported-providers).

  4. En la pestaña **Credenciales** llene los campos **Clave pública** y **Clave secreta** con los valores que guardó antes.

### Genere un webhook

Si necesita su **secreto de implementación Webhook** para conectarse con su
cuenta de Stripe, puede crear un webhook de manera automática o manual.

Create the webhook automaticallyCreate the webhook manually

Asegúrese de haber completado la información de sus Claves publicables y
secretas, luego haga clic en el botón **Generar su webhook**.

  1. Vaya a [la página de Webhooks de Stripe](https://dashboard.stripe.com/account/apikeys), o inicie sesión en su tablero de Stripe y vaya a Desarrolladores ‣ Webhooks.

  2. En la sección **Hosted endpoints** (puntos finales alojados) haga clic en **Agregar un punto final**. Después, en el campo **Endpoint URL** (URL del punto final) ingrese la URL de su base de datos de Konvergo ERP seguida por `/payment/stripe/webhook`, por ejemplo, `https://suempresa.odoo.com/payment/stripe/webhook`.

  3. Haga clic en **Seleccionar eventos** al final del formulario y después seleccione los siguientes eventos:

     * en la sección **Charge** (cargo): **charge.refunded** y **charge.refund.updated** ;

     * en la sección **Payment intent** (intención de pago): **payment_intent.amount_capturable_updated** , **payment_intent.succeeded** y **payment_intent.payment_failed** ;

     * en la sección **Setup intent** (intención de configuración): **setup_intent.succeeded**.

  4. Haga clic en **Agregar eventos**.

  5. Haga clic en **Add endpoint** (agregar punto final), después en **Reveal** (mostrar) y guarde su **Signing secret** (secreto de inicio de sesión) para después.

  6. En Konvergo ERP [vaya al proveedor de pago de Stripe](../payment_providers#payment-providers-supported-providers).

  7. En la pestaña **Credenciales** llene el **Secreto de webhook** con el valor que guardó antes.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Puede seleccionar otros eventos, pero no se pueden procesar con Konvergo ERP por el momento.</p>
</div>

## Activar métodos de pago locales

Los métodos de pago locales son métodos de pago que solo están disponibles
para proveedores, países y divisas específicas.

Konvergo ERP es compatible con los siguientes métodos de pago locales para Stripe:

  * Bancontact

  * EPS

  * giropay

  * iDEAL

  * Przelewy24 (P24)

Para adaptar la lista de métodos de pago activados, vaya a la pestaña
**Configuración** y edite la lista de guilabel:`Iconos de pago compatibles`.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Si no existe el registro de un ícono de pago en la base de datos y su método de pago correspondiente está en la lista anterior, se activa de forma automática con Stripe.</p></li>
<li><p>Si un método de pago no está en la lista anterior, no es admitido y no se puede activar.</p></li>
</ul>
</div>

## Activar Apple Pay

Para permitir que los clientes usen el botón de pago de Apple Pay para pagar
sus órdenes de comercio electrónico, vaya a la pestaña **Configuración** ,
active **Permitir el pago rápido** y haga clic en **Habilitar Apple Pay**.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../payment_providers#payment-providers-express-checkout"><span class="std std-ref">Pago exprés y Google Pay</span></a></p></li>
<li><p><a href="../payment_providers">Pagos en línea</a></p></li>
<li><p><a href="../../sales/point_of_sale/payment_methods/terminals/stripe">Usar Stripe como terminal de pago en el punto de venta</a></p></li>
</ul>
</div>

