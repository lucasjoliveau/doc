# Adyen

[Adyen](https://www.adyen.com/) es una empresa neerlandesa que ofrece varias
posibilidades de pago en línea.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../payment_providers#payment-providers-add-new"><span class="std std-ref">Activar un proveedor de pago</span></a></p></li>
<li><p><a href="../payment_providers">Pagos en línea</a></p></li>
</ul>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Adyen solo trabaja con clientes que procesan <b>más</b> de <b>10 millones anualmente</b> o que facturan un <b>mínimo</b> de <b>1.000</b> transacciones <b>al mes</b>.</p>
</div>

## Configuración

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../payment_providers#payment-providers-add-new"><span class="std std-ref">Activar un proveedor de pago</span></a></p>
</div>

### Pestaña de credenciales

Konvergo ERP necesita sus **credenciales API** para conectarse con su cuenta de Adyen,
que comprenden:

  * **Cuenta de comerciante** : el código de la cuenta de comerciante que se usará con Adyen.

  * Clave API: La clave API del usuario del servicio web.

  * Clave de cliente: la clave de cliente del usuario de servicio web.

  * Clave HMAC: la clave HMAC (código de autorización de mensajes basado en hash, por su siglas en inglés) del webhook.

  * URL de API de pago: el URL base para los puntos finales del API de pago.

  * URL de API recurrente: el URL base para los puntos finales de API recurrente.

Puede copiar las credenciales de su cuenta de Adyen y pegarlas en los campos
relacionados en la pestaña de **Credenciales**.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Si está usando Adyen como prueba con una <em>cuenta de prueba</em> de Adyen, vaya a Contabilidad ‣ Configuración ‣ Proveedores de pago. Haga clic en <b>Adyen</b>, activar <b>Modo de prueba</b> e ingrese sus credenciales en la pestaña de <b>Credenciales</b>.</p>
</div>

#### Clave API y clave de cliente

Para obtener su Clave API y su Clave de cliente, inicie sesión en su cuenta de
Adyen y vaya a Desarrolladores ‣ Credenciales API.

  * Si ya tiene un usuario API, ábralo.

  * Si todavía no tiene un usuario API, haga clic en **Crear nuevas credenciales**.

Vaya a Ajustes del servidor ‣ Autenticación y copie o genere su **Clave API**.
Asegúrese de copiar su clave API pues no podrá obteneral después sin generar
una nueva.

Ahora vaya a Configuración del cliente ‣ Autenticación y copie o genere su
**Clave de cliente**. Aquí también puede permitir que se hagan pagos desde su
sitio web.

#### Clave HMAC

Para obtener la clave HMAC, necesitará configurar un webhook de `Notificación
estándar`. Para hacer esto, inicie sesión en su cuenta de Adyen y vaya a
Desarrolladores ‣ Webhooks ‣ Agregar webhook ‣ Agregar notificación estándar.

![Configure un webhook. ](../../../_images/adyen-add-webhook.png)

Ahí, en General ‣ Configuración del servidor ‣ URL, ingrese la dirección de su
servidor seguido de `/payment/adyen/notification`.

![Ingrese la notificación URL.](../../../_images/adyen-webhook-url.png)

Luego, vaya a Seguridad ‣ Clave HMAC ‣ Generar. Tenga cuidado y copie la clave
pues no se le permitira hacerlo después sin generar una nueva.

![Genere una clave HMAC y guárdela. ](../../../_images/adyen-hmac-key.png)

Debe guardar el webhook para finalizar su creación.

#### URLs de las API

Todas las URLs de las API de Adyen incluyen un prefijo específico de cada área
del cliente que genera Adyen. Para configurar las URLs, siga los siguientes
pasos:

  1. Inicie sesión en su cuenta de Adyen y vaya a Desarrolladores ‣ URLs de las API.

  2. Copie el **Prefijo** para su área de cliente en directo (por ejemplo, **centro de datos**) y guárdela para después.

![Copie el prefijo para las APIs de Adyen](../../../_images/adyen-api-
urls.png)

  3. En Konvergo ERP, [vaya al proveedor de pago Adyen](../payment_providers#payment-providers-add-new).

  4. En el campo **URL de la API de pago** , ponga la siguiente URL y reemplace `yourprefix` por el prefijo que guardo anteriormente: `https://yourprefix-checkout-live.adyenpayments.com/checkout`

  5. En el campo **URL recurrente de las API** , ponga la siguiente URL y reemplace `yourprefix` con el prefijo que guardo anteriormente: `https://yourprefix-pal-live.adyenpayments.com/pal/servlet/Recurring`.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si está usando Adyen en modo de prueba, puede usar la siguiente URL en su lugar:</p>
<ul>
<li><p><b>URL de la API de pago</b>: <code>https://checkout-test.adyen.com</code></p></li>
<li><p><b>URL recurrente de la API</b>: <code>https://pal-test.adyen.com/pal/servlet/Recurring</code></p></li>
</ul>
</div>

### Cuenta de Adyen

#### Permitir pagos de un origen específico

Para permitir pagos originados desde su sitio web, siga los pasos de Clave API
y clave de cliente para ir a su usuario de API y vaya a Agregar origenes
permitidos, luego agregue las URL desde donde se realizaran los pagos (las URL
de los servidores que alojan sus instancias de Konvergo ERP).

![Permite pagos originados desde un dominio específico.
](../../../_images/adyen-allowed-origins.png)

### Hacer una retención de tarjeta de crédito

Adyen le permite capturar un importe manualmente en lugar de hacer una
directa.

Para establecer la cuenta pendiente, active la opción **Capturar importe
manualmente** en Konvergo ERP, como se explica en [documentación sobre los proveedores
de pago](../payment_providers#payment-providers-manual-capture).

Luego, abra su Cuenta de comerciante de Adyen y vaya a Cuenta ‣ Configuración,
y cambie de **Retraso de captura** a **manual**.

![Configuración del retraso de captura en Adyen
](../../../_images/adyen_capture_delay.png) <div class="alert alert-warning">
<p class="alert-title">
Prudencia</p><ul>
<li><p>Si configura Konvergo ERP para realizar las capturas manualmente, asegúrese de establecer el <b>Retraso de captura</b> a <b>manual</b> en Adyen. De lo contrario, la transacción se bloqueará en el estado de autorizado en Konvergo ERP.</p></li>
<li><p>Konvergo ERP aún no admite las capturas parciales. Considere que si realiza una captura parcial desde la interfaz de Adyen, Konvergo ERP la considerará como una captura completa.</p></li>
</ul>
</div>
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Después de <b>7 dias</b>, si la transacción aún no se ha capturado, el cliente tiene derecho a <b>revocarla</b>.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../payment_providers">Pagos en línea</a></p>
</div>

