# Suscripciones

La aplicación _Suscripciones_ se usa para manejar negocios recurrentes: vender
nuevos contratos, [hacer ventas adicionales a los
clientes](subscriptions/upselling), controlar el churn, y [generar
reportes](subscriptions/reports) en los KPIs: MRR, ARR, retención, churn,
etc.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="https://www.odoo.com/slides/subscription-20">Tutoriales de Konvergo ERP: Suscripción</a></p></li>
<li><p><a href="subscriptions/products">Productos de suscripción</a></p></li>
<li><p><a href="subscriptions/ecommerce">Use las suscripciones en la tienda de su comercio electrónico</a></p></li>
<li><p><a href="subscriptions/plans">Planes de suscripción</a></p></li>
<li><p><a href="subscriptions/upselling">Realice una venta adicional de una suscripción</a></p></li>
<li><p><a href="subscriptions/renewals">Renovar una suscripción</a></p></li>
<li><p><a href="subscriptions/closing">Cancelar una suscripción</a></p></li>
<li><p><a href="subscriptions/automatic_alerts">Alertas automáticas</a></p></li>
<li><p><a href="subscriptions/reports">Reportes</a></p></li>
</ul>
</div>

## Cotizaciones de suscripción

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Las ordenes de venta con una recurrencia definida se vuelven suscripciones.</p>
</div>

Para crear una nueva suscripción, haga clic en **Nuevo** en la aplicación
_Suscripciones_ o [Ventas](../sales). Puede:

  * Seleccionar un [plan de suscripción](subscriptions/plans) para pre-llenar la cotización de manera instantánea, o

  * Completar la cotización como haría de forma habitual, asegurándose de seleccionar una recurrencia y una fecha de finalización en caso de que fuera necesaria, además de agregar los [productos recurrentes](subscriptions/products).

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Puede definir diferentes direcciones de facturación y envío al activar la función  <a href="../finance/accounting/customer_invoices/customer_addresses">Direcciones de clientes</a> .</p>
</div>

## Confirmación

Envie la cotización al cliente para que la confirme haciendo clic en **Enviar
por correo** , o confírmela inmediatamente haciendo clic en **Confirmar**.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Haga clic en <b>Vista del cliente</b> para previsualizar el portal del cliente, donde podrá ver la cotización, firmar, pagar  y comunicarselo a usetd.</p>
</div>

## Pagos automáticos

Puede solicitar al cliente que establezca un método de pago automático y
realizar un prepago la primera vez de la suscripción antes de confirmar su
cotización. Para hacerlo, vaya a la pestaña **Más infromación** de la
cotización y seleccione la opción **Pago** en el campo **Confirmación en
línea**.

Si deja sin seleccionar **Pago** , el cliente no tiene que realizar un prepago
para comenzar la suscripción. Esto significa que el pago no es automático y
que el cliente debe pagar cada factura manualmente.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Si la confirmación en línea requiere un pago por anticipado, el cliente solo puede seleccionar los <a href="../finance/payment_providers#payment-providers-supported-providers"><span class="std std-ref">proveedores de pago</span></a> que tienen la <a href="../finance/payment_providers#payment-providers-tokenization"><span class="std std-ref">función de tokenización</span></a> habilitada. Esto asegura que se le cobre al cliente de forma automática cada nuevo periodo.</p>
</div>

  * [Productos de suscripción](subscriptions/products)
  * [Use las suscripciones en la tienda de su comercio electrónico](subscriptions/ecommerce)
  * [Planes de suscripción](subscriptions/plans)
  * [Realice una venta adicional de una suscripción](subscriptions/upselling)
  * [Renovar una suscripción](subscriptions/renewals)
  * [Cancelar una suscripción](subscriptions/closing)
  * [Alertas automáticas](subscriptions/automatic_alerts)
  * [Reportes](subscriptions/reports)

  *[KPIs]: Indicadores clave de rendimiento
  *[MRR]: Ingresos recurrentes mensuales
  *[ARR]: Ingresos recurrentes anuales

