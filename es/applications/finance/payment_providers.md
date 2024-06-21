# Pagos en línea

  * [Transferencias bancarias](payment_providers/wire_transfer)
  * [Adyen](payment_providers/adyen)
  * [Alipay](payment_providers/alipay)
  * [Servicios de pago de Amazon](payment_providers/amazon_payment_services)
  * [AsiaPay](payment_providers/asiapay)
  * [Authorize.Net](payment_providers/authorize)
  * [Buckaroo](payment_providers/buckaroo)
  * [Demostración](payment_providers/demo)
  * [Flutterwave](payment_providers/flutterwave)
  * [Mercado Pago](payment_providers/mercado_pago)
  * [Mollie](payment_providers/mollie)
  * [Ogone](payment_providers/ogone)
  * [PayPal](payment_providers/paypal)
  * [Razorpay](payment_providers/razorpay)
  * [SIPS](payment_providers/sips)
  * [Stripe](payment_providers/stripe)

Konvergo ERP integra varios **proveedores de pago** que le permitirán a sus clientes
pagar en línea a través de sus _portales de cliente_ o de _el sitio web de su
comercio electrónico_. Pueden pagar órdenes de venta, facturas o suscripciones
con pagos recurrentes con sus métodos de pago preferidos como las **tarjetas
de crédito**.

![Formulario de pago en línea](../../_images/online-payment.png)
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Konvergo ERP delega el tratamiento de información sensible al proveedor de pago certificado para que usted no se preocupe por cumplir con el PCI. Ninguna información sensible (como números de tarjeta de crédito) se guarda en los servidores de Konvergo ERP o en otras bases de datos de Konvergo ERP almacenadas en otras partes. En su lugar, las aplicaciones de Konvergo ERP usan un número de referencia único para la información guardada en los sistemas del proveedor de pago.</p>
</div>

## Proveedores de pago admitidos

Para acceder a los proveedores de pago compatibles, vaya a Contabilidad ‣
Configuración ‣ Proveedores de pago o en Sitio web ‣ Configuración ‣
Proveedores de pago.

### Proveedores de pago en línea

| Flujo de pago desde | Tokenización | Captura manual | Reembolsos | Pago exprés | Cargos adicionales  
---|---|---|---|---|---|---  
[Adyen](payment_providers/adyen) | Konvergo ERP | ✔ | Solo completo | Completo y parcial |  |   
[Servicios de pago de Amazon](payment_providers/amazon_payment_services) | El sitio web del proveedor |  |  |  |  |   
[AsiaPay](payment_providers/asiapay) | El sitio web del proveedor |  |  |  |  |   
[Authorize.Net](payment_providers/authorize) | Konvergo ERP | ✔ | Solo completo | Solo completo |  |   
[Buckaroo](payment_providers/buckaroo) | El sitio web del proveedor |  |  |  |  |   
[Flutterwave](payment_providers/flutterwave) | El sitio web del proveedor | ✔ |  |  |  |   
[Mercado Pago](payment_providers/mercado_pago) | El sitio web del proveedor |  |  |  |  |   
[Mollie](payment_providers/mollie) | El sitio web del proveedor |  |  |  |  |   
[PayPal](payment_providers/paypal) | El sitio web del proveedor |  |  |  |  | ✔  
[Razorpay](payment_providers/razorpay) | El sitio web del proveedor |  | Solo completo | Completo y parcial |  |   
[SIPS](payment_providers/sips) | El sitio web del proveedor |  |  |  |  |   
[Stripe](payment_providers/stripe) | El sitio web del proveedor | ✔ | Solo completo | Completo y parcial | ✔ |   
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Cada proveedor tiene su propio flujo de configuraciones, dependiendo de qué función esté disponible.</p></li>
<li><p>Algunos de estos proveedores de pago también se pueden agregar como  <a href="accounting/bank">cuentas bancarias</a>, pero <b>no es</b> el mismo proceso que el de agregarlos como proveedores de pago. Los proveedores de pago le permiten a los clientes pagar en línea, mientras que las cuentas bancarias se agregan y configuran en la aplicación Contabilidad para hacer una <a href="accounting/bank/reconciliation">conciliación bancaria</a>.</p></li>
</ul>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Además de los proveedores de pago de siempre que están integrados con una API como Stripe, PayPal o Adyen; Konvergo ERP incluye el <a href="payment_providers/demo">Proveedor de pago de prueba</a>. Este proveedor le permite probar flujos empresariales que involucran pagos en línea. No se requieren de credenciales puesto que estos son pagos de prueba.</p>
</div>

### Pagos bancarios

  * [Transferencias bancarias](payment_providers/wire_transfer)

Al seleccionar esta opción, Konvergo ERP muestra su información de pago con una
referencia de pago. Debe aprobar el pago de forma manual una vez que lo haya
recibido en su cuenta bancaria.

  * [Domiciliación bancaria SEPA](accounting/payments/batch_sdd)

Sus clientes pueden realizar una transferencia bancaria para registrar el
mandato de domiciliación bancaria SEPA y que el cargo se haga directamente a
su cuenta bancaria.

## Activar un proveedor de pago

Para agregar un nuevo proveedor de pago y hacer que los métodos de pago
relacionados estén disponibles para sus clientes, siga estos pasos:

  1. Vaya al sitio web del proveedor de pago, cree una cuenta y asegúrese de que tiene las credenciales API requeridas para uso externo. Konvergo ERP necesita estas credenciales para comunicarse con el proveedor de pago.

  2. En Konvergo ERP vaya a la sección **Proveedores de pago** en Contabilidad ‣ Configuración ‣ Proveedores de pago o Sitio web ‣ Configuración ‣ Proveedores de pago.

  3. Seleccione el proveedor y configure la pestaña **Credenciales**.

  4. Configure el campo **Estado** como **Habilitado**.

  5. Seleccione un diario de pago.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Los campos disponibles en la pestaña <b>Credenciales</b> dependen del proveedor de pago. Para más información consulte <a href="#payment-providers-supported-providers"><span class="std std-ref">la documentación relacionada</span></a>.</p></li>
<li><p>Una vez que active el proveedor de pago, se publicará de forma automática en su sitio web. Si desea desactivarlo, haga clic en el botón <b>Publicado</b>. Los clientes no pueden hacer pagos a través de un proveedor que no esté publicado, pero todavía pueden gestionar <span class="dfn"><span>(borrar y asignar a una suscripción)</span></span> los tokens existentes vinculados a dicho proveedor.</p></li>
</ul>
</div>

### Modo de prueba

Si desea probar un proveedor de pago, configure el campo **Estado** en el
formulario del proveedor de pago como **Modo de prueba** , después ingrese las
credenciales de prueba de su proveedor en la pestaña **Credenciales**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>De forma predeterminada, el proveedor de pago se mantendrá <b>sin publicar</b> en el modo de prueba para que los visitantes no lo puedan ver.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Le recomendamos usar el modo de prueba en una base de datos duplicada o de prueba para evitar crear problemas con la numeración de sus facturas.</p>
</div>

## Formulario de pago

Puede cambiar la apariencia del proveedor de pago en su sitio web en la
pestaña **Configuración** del proveedor de pago seleccionado. Modifique el
nombre en el campo **Se muestra como** y adapte los **Iconos de pago
compatibles** si es necesario.

## Tokenización

Si el proveedor de pago es compatible con esta función, los clientes podrán
guardar los detalles de su método de pago para usarlos después. Para activar
esta función, vaya a la pestaña de **Configuración** del proveedor de pago
seleccionado y active **Permitir guardar métodos de pago**.

Un **token de pago** se crea en Konvergo ERP y se puede usar como método de pago para
pagos subsecuentes sin tener que ingresar otra vez los detalles del método de
pago. Esto es muy útil para la tasa de conversión de los comercios
electrónicos y para las suscripciones que usan pagos recurrentes.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Sigue cumpliendo con el PCI aún con esta función acitvada porque Konvergo ERP no guarda los detalles de la tarjeta directamente. En lugar de eso, crea un token de pago que solo guarda una referencia de los detalles de la tarjeta almacenados en el servidor del proveedor de pago.</p>
</div>

## Captura manual

Si el proveedor de pago es compatible con esta función, podrá autorizar y
capturar pagos en dos pasos en lugar de solo uno. Para activar esta función,
vaya a la pestaña de **Configuración** del proveedor de pago seleccionado y
active **Capturar el importe manualmente**.

Cuando autoriza un pago, los fondos se reservan en el método de pago del
cliente, pero no se cobran inmediatamente. Se cobran cuando usted captura
manualmente el pago más tarde. También puede anular la autorización para
cancelarla y liberar los fondos reservados. Capturar pagos manualmente es útil
en muchas situaciones:

  * Recibir la confirmación de pago y esperar hasta que la orden se envíe para capturar el pago.

  * Revisar y verificar que las órdenes sean legítimas antes de que se complete el pago y empiece el proceso de cumplimiento.

  * Evitar procesar cuotas potencialmente altas para reembolsos de pagos: los proveedores de pago no le cobrarán por anular una autorización.

  * Retener un depósito de seguridad para despúes devolverlo, menos cualquier deducción (por ejemplo, en caso de daños).

Para capturar el pago después de que se autorizo, vaya a la orden de ventas o
factura vinculada y haga clic en el botón de **Capturar transacción**. Para
liberar los fondos, haga clic en el botón de **Anular transacción**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Algunos proveedores de pago admiten la captura parcial del importe autorizado. El importe restante se puede capturar o anular. Estos proveedores tienen marcado del valor de <b>Completo y parcial</b> en la <a href="#payment-providers-online-providers"><span class="std std-ref">tabla anterior</span></a>. Los proveedores que solo admiten la captura o anulación completa del importe tienen marcado el valor de <b>Solo completo</b>.</p></li>
<li><p>Los fondos no se reservan para siempre. Después de cierto tiempo, puede que se liberen automáticamente de vuelta al método de pago del cliente. Vaya a la documentación de su proveedor de pago para conocer la duración exacta de la reservación de fondos.</p></li>
<li><p>Konvergo ERP no admite esta función para todos los proveedores de pago pero algunos permiten la captura manual desde la interfaz de su sitio web.</p></li>
</ul>
</div>

## Reembolsos

Si su proveedor de pago admite esta función, puede reembolsar los pagos
directamente desde Konvergo ERP. No se tiene que activar primero. Para reembolsar el
pago de un cliente, vaya al pago y haga clic en el botón de **Reembolsar**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Algunos proveedores de pago admiten el reembolso solo de una parte del importe. El restante se puede reembolsar también de manera opcional. Estos proveedores tienen marcado el valor de  <b>Completo y parcial</b> en la <a href="#payment-providers-online-providers"><span class="std std-ref">tabla anterior</span></a>. Los proveedores que solo admiten el reembolso completo del importe tienen marcado el valor de <b>Solo completo</b>.</p></li>
<li><p>Konvergo ERP no admite esta función en todos los proveedores de pago pero algunos permiten el reembolso de pagos desde la interfaz de su sitio web.</p></li>
</ul>
</div>

## Finalización de compra exprés

Si el proveedor de pago es compatible con esta función, puede dejar que los
clientes usen los botones de **Google Pay** y **Apple Pay** para pagar por las
órdenes de comercio electrónico. Al usar cualquiera de estos botones, pasarán
directamente desde el carrito a la página de confirmación sin tener que llenar
un formulario de contacto, ya que solo tienen que validar el pago en el
formulario de pago de Google o Apple.

Para activar esta función vaya a la pestaña **Configuración** del proveedor de
pago seleccionado y active **Permitir el pago rápido**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Todos los precios que se muestran en el formulario de pago rápido siempre incluyen los impuestos.</p>
</div>

## Cuotas adicionales

Si el proveedor de pago es compatible con esta función, puede agregar cargos
adicionales para transacciones en línea. Los cargos se pueden configurar como
cantidades o porcentajes **fijos** , **variables** o ambos al mismo tiempo.
También podrán diferir dependiendo si la transacción es **doméstica** o
**internacional**.

Para activar esta función, vaya a la pestaña **Cargos** del proveedor de pago
seleccionado, active **Agregar cuotas adicionales** y haga los ajustes que
desee.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Cada proveedor tiene su propio flujo de configuraciones, dependiendo de qué función esté disponible.</p></li>
<li><p>Algunos de estos proveedores de pago también se pueden agregar como  <a href="accounting/bank">cuentas bancarias</a>, pero <b>no es</b> el mismo proceso que el de agregarlos como proveedores de pago. Los proveedores de pago le permiten a los clientes pagar en línea, mientras que las cuentas bancarias se agregan y configuran en la aplicación Contabilidad para hacer una <a href="accounting/bank/reconciliation">conciliación bancaria</a>.</p></li>
</ul>
</div>0

## Disponibilidad

Es posible configurar la disponibilidad del proveedor de pago si especifica el
**monto máximo** permitido y modifica tanto la **Divisa** como los **Países**
en la pestaña de **Configuración**.

### Divisas y países

Todos los proveedores de pago tienen una lista distinta de divisas y países
disponibles. Son el primer filtro durante las operaciones de pago, es decir,
el cliente no podrá usar los métodos de pago vinculados a un proveedor de pago
si su divisa o su país no está en la lista de compatibilidad. Como es posible
que haya errores, actualizaciones y otros problemas, puede agregar o eliminar
divisas o países de la lista de opciones compatibles de un proveedor de pago.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Cada proveedor tiene su propio flujo de configuraciones, dependiendo de qué función esté disponible.</p></li>
<li><p>Algunos de estos proveedores de pago también se pueden agregar como  <a href="accounting/bank">cuentas bancarias</a>, pero <b>no es</b> el mismo proceso que el de agregarlos como proveedores de pago. Los proveedores de pago le permiten a los clientes pagar en línea, mientras que las cuentas bancarias se agregan y configuran en la aplicación Contabilidad para hacer una <a href="accounting/bank/reconciliation">conciliación bancaria</a>.</p></li>
</ul>
</div>1

### Cantidad máxima

Puede restringir la **Cantidad máxima** que se puede pagar con el proveedor de
pago seleccionado. Deje el campo como `0.00` para que el proveedor de pago
esté disponible sin importar la cantidad del pago.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Cada proveedor tiene su propio flujo de configuraciones, dependiendo de qué función esté disponible.</p></li>
<li><p>Algunos de estos proveedores de pago también se pueden agregar como  <a href="accounting/bank">cuentas bancarias</a>, pero <b>no es</b> el mismo proceso que el de agregarlos como proveedores de pago. Los proveedores de pago le permiten a los clientes pagar en línea, mientras que las cuentas bancarias se agregan y configuran en la aplicación Contabilidad para hacer una <a href="accounting/bank/reconciliation">conciliación bancaria</a>.</p></li>
</ul>
</div>2

## Diario de pagos

Se debe definir un [diario de pago](accounting/bank) en el que se
registren los pagos de un proveedor de pago en una **cuenta pendiente**. Para
hacerlo, vaya a la pestaña de **Configuración** del proveedor de pago
seleccionado y elija un **diario de pago**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Cada proveedor tiene su propio flujo de configuraciones, dependiendo de qué función esté disponible.</p></li>
<li><p>Algunos de estos proveedores de pago también se pueden agregar como  <a href="accounting/bank">cuentas bancarias</a>, pero <b>no es</b> el mismo proceso que el de agregarlos como proveedores de pago. Los proveedores de pago le permiten a los clientes pagar en línea, mientras que las cuentas bancarias se agregan y configuran en la aplicación Contabilidad para hacer una <a href="accounting/bank/reconciliation">conciliación bancaria</a>.</p></li>
</ul>
</div>3

### Perspectiva contable

Desde una perspectiva de contabilidad, hay dos tipos de flujos de pago en
línea: los pagos que se depositan directamente en su cuenta bancaria y siguen
el flujo de [conciliación](accounting/bank/reconciliation) usual y los
pagos que vienen de proveedores de pago en línea externos que requieren que se
siga otro flujo de trabajo. Para estos pagos necesita pensar cómo quiere
registrar sus asientos de pago. Le recomendamos que hable con su contador para
obtener su opinión al respecto.

La **cuenta bancaria** definida para el diario de pago se usa de forma
predeterminada, pero también puede especificar una [cuenta
pendiente](accounting/bank#bank-outstanding-accounts) para cada proveedor
de pago y así separar los pagos provenientes de este proveedor del resto de
los pagos.

![Definir una cuenta pendiente para un proveedor de
pago.](../../_images/bank_journal.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Cada proveedor tiene su propio flujo de configuraciones, dependiendo de qué función esté disponible.</p></li>
<li><p>Algunos de estos proveedores de pago también se pueden agregar como  <a href="accounting/bank">cuentas bancarias</a>, pero <b>no es</b> el mismo proceso que el de agregarlos como proveedores de pago. Los proveedores de pago le permiten a los clientes pagar en línea, mientras que las cuentas bancarias se agregan y configuran en la aplicación Contabilidad para hacer una <a href="accounting/bank/reconciliation">conciliación bancaria</a>.</p></li>
</ul>
</div>4

