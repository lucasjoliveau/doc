# Stripe

[Stripe](https://stripe.com/) es un proveedor de soluciones de pago en línea
con sede en Estados Unidos con el que las empresas pueden aceptar **tarjetas
de crédito** y otros métodos de pago.

Ver también

  * [Lista de países compatibles con Stripe](https://stripe.com/global)

  * [Lista de métodos de pago compatibles con Stripe](https://stripe.com/payments/payment-methods)

## Cree su cuenta de Stripe con Odoo

El método para obtener sus credenciales depende de su tipo de alojamiento:

Odoo OnlineOdoo.sh or On-premise

  1. [Vaya al proveedor de pago Stripe](../payment_providers.html#payment-providers-supported-providers) y haga clic en Conectar Stripe.

  2. Siga el proceso de configuración y confirme su dirección de correo cuando Stripe le envíe un correo de confirmación.

  3. Al final del proceso, haga clic en Agree and submit (estoy de acuerdo y enviar). Si se envió toda la información solicitada regresará a Odoo y se activará su proveedor de pago.

  4. Activar métodos de pago locales.

  1. [Vaya al proveedor de pago Stripe](../payment_providers.html#payment-providers-supported-providers) y haga clic en Conectar Stripe.

  2. Siga el proceso de configuración y confirme su dirección de correo cuando Stripe le envíe un correo de confirmación.

  3. Al final del proceso, haga clic en Agree and submit (estoy de acuerdo y enviar). Se le redirigirá al proveedor de pago **Stripe** dentro de Odoo

  4. Introduzca sus credenciales.

  5. Genere un webhook.

  6. Seleccione un [diario de pago](../payment_providers.html#payment-providers-journal).

  7. Configure el campo Estado como Habilitado.

  8. Activar métodos de pago locales.

Truco

  * Para usar una cuenta de Stripe existente, [active el modo desarrollador](../../general/developer_mode.html#developer-mode) y [active Stripe manualmente](../payment_providers.html#payment-providers-add-new). Entonces podrá completar sus credenciales, generar un webhook y establecer su proveedor de pago.

  * También puede probar Stripe con el [Modo de prueba](../payment_providers.html#payment-providers-test-mode) (modo de prueba de proveedores de pago). Para hacerlo, primero [inicie sesión en su tablero de Stripe](https://dashboard.stripe.com/dashboard) y cambie al **modo de prueba**. Después en Odoo [active el modo de Desarrollador](../../general/developer_mode.html#developer-mode), [vaya al proveedor de pago Stripe](../payment_providers.html#payment-providers-supported-providers), llene las credenciales de su API con las claves de prueba y configure elm:guilabel:`Estado` como Modo de prueba.

### Complete sus credenciales

Si necesita sus **credenciales API** para conectar con su cuenta de Stripe,
haga lo siguiente:

  1. Vaya a [la página de claves API de Stripe](https://dashboard.stripe.com/account/apikeys), o inicie sesión en su tablero de Stripe y vaya a :menuselection:`Desarrolladores –> Claves API.

  2. En la sección Standard keys (claves estándar) copie la Publishable key (clave pública) y la Secret key (clave secreta) y guárdelas para que pueda usarlas después.

  3. En Odoo [vaya al proveedor de pago de Stripe](../payment_providers.html#payment-providers-supported-providers).

  4. En la pestaña Credenciales llene los campos Clave pública y Clave secreta con los valores que guardó antes.

### Genere un webhook

Si necesita su **secreto de implementación Webhook** para conectarse con su
cuenta de Stripe, puede crear un webhook de manera automática o manual.

Create the webhook automaticallyCreate the webhook manually

Asegúrese de haber completado la información de sus Claves publicables y
secretas, luego haga clic en el botón Generar su webhook.

  1. Vaya a [la página de Webhooks de Stripe](https://dashboard.stripe.com/account/apikeys), o inicie sesión en su tablero de Stripe y vaya a Desarrolladores ‣ Webhooks.

  2. En la sección Hosted endpoints (puntos finales alojados) haga clic en Agregar un punto final. Después, en el campo Endpoint URL (URL del punto final) ingrese la URL de su base de datos de Odoo seguida por `/payment/stripe/webhook`, por ejemplo, `https://suempresa.odoo.com/payment/stripe/webhook`.

  3. Haga clic en Seleccionar eventos al final del formulario y después seleccione los siguientes eventos:

     * en la sección Charge (cargo): charge.refunded y charge.refund.updated;

     * en la sección Payment intent (intención de pago): payment_intent.amount_capturable_updated, payment_intent.succeeded y payment_intent.payment_failed;

     * en la sección Setup intent (intención de configuración): setup_intent.succeeded.

  4. Haga clic en Agregar eventos.

  5. Haga clic en Add endpoint (agregar punto final), después en Reveal (mostrar) y guarde su Signing secret (secreto de inicio de sesión) para después.

  6. En Odoo [vaya al proveedor de pago de Stripe](../payment_providers.html#payment-providers-supported-providers).

  7. En la pestaña Credenciales llene el Secreto de webhook con el valor que guardó antes.

Nota

Puede seleccionar otros eventos, pero no se pueden procesar con Odoo por el
momento.

## Activar métodos de pago locales

Los métodos de pago locales son métodos de pago que solo están disponibles
para proveedores, países y divisas específicas.

Odoo es compatible con los siguientes métodos de pago locales para Stripe:

  * Bancontact

  * EPS

  * giropay

  * iDEAL

  * Przelewy24 (P24)

Para adaptar la lista de métodos de pago activados, vaya a la pestaña
Configuración y edite la lista de guilabel:`Iconos de pago compatibles`.

Nota

  * Si no existe el registro de un ícono de pago en la base de datos y su método de pago correspondiente está en la lista anterior, se activa de forma automática con Stripe.

  * Si un método de pago no está en la lista anterior, no es admitido y no se puede activar.

## Activar Apple Pay

Para permitir que los clientes usen el botón de pago de Apple Pay para pagar
sus órdenes de comercio electrónico, vaya a la pestaña Configuración, active
Permitir el pago rápido y haga clic en Habilitar Apple Pay.

Ver también

  * [Pago exprés y Google Pay](../payment_providers.html#payment-providers-express-checkout)

  * [Pagos en línea](../payment_providers.html)

  * [Usar Stripe como terminal de pago en el punto de venta](../../sales/point_of_sale/payment_methods/terminals/stripe.html)

