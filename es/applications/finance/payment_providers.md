# Pagos en línea

  * [Transferencias bancarias](payment_providers/wire_transfer.html)
  * [Adyen](payment_providers/adyen.html)
  * [Alipay](payment_providers/alipay.html)
  * [Servicios de pago de Amazon](payment_providers/amazon_payment_services.html)
  * [AsiaPay](payment_providers/asiapay.html)
  * [Authorize.Net](payment_providers/authorize.html)
  * [Buckaroo](payment_providers/buckaroo.html)
  * [Demostración](payment_providers/demo.html)
  * [Flutterwave](payment_providers/flutterwave.html)
  * [Mercado Pago](payment_providers/mercado_pago.html)
  * [Mollie](payment_providers/mollie.html)
  * [Ogone](payment_providers/ogone.html)
  * [PayPal](payment_providers/paypal.html)
  * [Razorpay](payment_providers/razorpay.html)
  * [SIPS](payment_providers/sips.html)
  * [Stripe](payment_providers/stripe.html)

Odoo integra varios **proveedores de pago** que le permitirán a sus clientes
pagar en línea a través de sus _portales de cliente_ o de _el sitio web de su
comercio electrónico_. Pueden pagar órdenes de venta, facturas o suscripciones
con pagos recurrentes con sus métodos de pago preferidos como las **tarjetas
de crédito**.

![Formulario de pago en línea](../../_images/online-payment.png)

Nota

Odoo delega el tratamiento de información sensible al proveedor de pago
certificado para que usted no se preocupe por cumplir con el PCI. Ninguna
información sensible (como números de tarjeta de crédito) se guarda en los
servidores de Odoo o en otras bases de datos de Odoo almacenadas en otras
partes. En su lugar, las aplicaciones de Odoo usan un número de referencia
único para la información guardada en los sistemas del proveedor de pago.

## Proveedores de pago admitidos

Para acceder a los proveedores de pago compatibles, vaya a Contabilidad ‣
Configuración ‣ Proveedores de pago o en Sitio web ‣ Configuración ‣
Proveedores de pago.

### Proveedores de pago en línea

| Flujo de pago desde | Tokenización | Captura manual | Reembolsos | Pago exprés | Cargos adicionales  
---|---|---|---|---|---|---  
[Adyen](payment_providers/adyen.html) | Odoo | ✔ | Solo completo | Completo y parcial |  |   
[Servicios de pago de Amazon](payment_providers/amazon_payment_services.html) | El sitio web del proveedor |  |  |  |  |   
[AsiaPay](payment_providers/asiapay.html) | El sitio web del proveedor |  |  |  |  |   
[Authorize.Net](payment_providers/authorize.html) | Odoo | ✔ | Solo completo | Solo completo |  |   
[Buckaroo](payment_providers/buckaroo.html) | El sitio web del proveedor |  |  |  |  |   
[Flutterwave](payment_providers/flutterwave.html) | El sitio web del proveedor | ✔ |  |  |  |   
[Mercado Pago](payment_providers/mercado_pago.html) | El sitio web del proveedor |  |  |  |  |   
[Mollie](payment_providers/mollie.html) | El sitio web del proveedor |  |  |  |  |   
[PayPal](payment_providers/paypal.html) | El sitio web del proveedor |  |  |  |  | ✔  
[Razorpay](payment_providers/razorpay.html) | El sitio web del proveedor |  | Solo completo | Completo y parcial |  |   
[SIPS](payment_providers/sips.html) | El sitio web del proveedor |  |  |  |  |   
[Stripe](payment_providers/stripe.html) | El sitio web del proveedor | ✔ | Solo completo | Completo y parcial | ✔ |   
  
Nota

  * Cada proveedor tiene su propio flujo de configuraciones, dependiendo de qué función esté disponible.

  * Algunos de estos proveedores de pago también se pueden agregar como [cuentas bancarias](accounting/bank.html), pero **no es** el mismo proceso que el de agregarlos como proveedores de pago. Los proveedores de pago le permiten a los clientes pagar en línea, mientras que las cuentas bancarias se agregan y configuran en la aplicación Contabilidad para hacer una [conciliación bancaria](accounting/bank/reconciliation.html).

Truco

Además de los proveedores de pago de siempre que están integrados con una API
como Stripe, PayPal o Adyen; Odoo incluye el [Proveedor de pago de
prueba](payment_providers/demo.html). Este proveedor le permite probar flujos
empresariales que involucran pagos en línea. No se requieren de credenciales
puesto que estos son pagos de prueba.

### Pagos bancarios

  * [Transferencias bancarias](payment_providers/wire_transfer.html)

Al seleccionar esta opción, Odoo muestra su información de pago con una
referencia de pago. Debe aprobar el pago de forma manual una vez que lo haya
recibido en su cuenta bancaria.

  * [Domiciliación bancaria SEPA](accounting/payments/batch_sdd.html)

Sus clientes pueden realizar una transferencia bancaria para registrar el
mandato de domiciliación bancaria SEPA y que el cargo se haga directamente a
su cuenta bancaria.

## Activar un proveedor de pago

Para agregar un nuevo proveedor de pago y hacer que los métodos de pago
relacionados estén disponibles para sus clientes, siga estos pasos:

  1. Vaya al sitio web del proveedor de pago, cree una cuenta y asegúrese de que tiene las credenciales API requeridas para uso externo. Odoo necesita estas credenciales para comunicarse con el proveedor de pago.

  2. En Odoo vaya a la sección Proveedores de pago en Contabilidad ‣ Configuración ‣ Proveedores de pago o Sitio web ‣ Configuración ‣ Proveedores de pago.

  3. Seleccione el proveedor y configure la pestaña Credenciales.

  4. Configure el campo Estado como Habilitado.

  5. Seleccione un diario de pago.

Nota

  * Los campos disponibles en la pestaña Credenciales dependen del proveedor de pago. Para más información consulte la documentación relacionada.

  * Una vez que active el proveedor de pago, se publicará de forma automática en su sitio web. Si desea desactivarlo, haga clic en el botón Publicado. Los clientes no pueden hacer pagos a través de un proveedor que no esté publicado, pero todavía pueden gestionar (borrar y asignar a una suscripción) los tokens existentes vinculados a dicho proveedor.

### Modo de prueba

Si desea probar un proveedor de pago, configure el campo Estado en el
formulario del proveedor de pago como Modo de prueba, después ingrese las
credenciales de prueba de su proveedor en la pestaña Credenciales.

Nota

De forma predeterminada, el proveedor de pago se mantendrá **sin publicar** en
el modo de prueba para que los visitantes no lo puedan ver.

Advertencia

Le recomendamos usar el modo de prueba en una base de datos duplicada o de
prueba para evitar crear problemas con la numeración de sus facturas.

## Formulario de pago

Puede cambiar la apariencia del proveedor de pago en su sitio web en la
pestaña Configuración del proveedor de pago seleccionado. Modifique el nombre
en el campo Se muestra como y adapte los Iconos de pago compatibles si es
necesario.

## Tokenización

Si el proveedor de pago es compatible con esta función, los clientes podrán
guardar los detalles de su método de pago para usarlos después. Para activar
esta función, vaya a la pestaña de Configuración del proveedor de pago
seleccionado y active Permitir guardar métodos de pago.

Un **token de pago** se crea en Odoo y se puede usar como método de pago para
pagos subsecuentes sin tener que ingresar otra vez los detalles del método de
pago. Esto es muy útil para la tasa de conversión de los comercios
electrónicos y para las suscripciones que usan pagos recurrentes.

Nota

Sigue cumpliendo con el PCI aún con esta función acitvada porque Odoo no
guarda los detalles de la tarjeta directamente. En lugar de eso, crea un token
de pago que solo guarda una referencia de los detalles de la tarjeta
almacenados en el servidor del proveedor de pago.

## Captura manual

Si el proveedor de pago es compatible con esta función, podrá autorizar y
capturar pagos en dos pasos en lugar de solo uno. Para activar esta función,
vaya a la pestaña de Configuración del proveedor de pago seleccionado y active
Capturar el importe manualmente.

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
factura vinculada y haga clic en el botón de Capturar transacción. Para
liberar los fondos, haga clic en el botón de Anular transacción.

Nota

  * Algunos proveedores de pago admiten la captura parcial del importe autorizado. El importe restante se puede capturar o anular. Estos proveedores tienen marcado del valor de **Completo y parcial** en la tabla anterior. Los proveedores que solo admiten la captura o anulación completa del importe tienen marcado el valor de **Solo completo**.

  * Los fondos no se reservan para siempre. Después de cierto tiempo, puede que se liberen automáticamente de vuelta al método de pago del cliente. Vaya a la documentación de su proveedor de pago para conocer la duración exacta de la reservación de fondos.

  * Odoo no admite esta función para todos los proveedores de pago pero algunos permiten la captura manual desde la interfaz de su sitio web.

## Reembolsos

Si su proveedor de pago admite esta función, puede reembolsar los pagos
directamente desde Odoo. No se tiene que activar primero. Para reembolsar el
pago de un cliente, vaya al pago y haga clic en el botón de Reembolsar.

Nota

  * Algunos proveedores de pago admiten el reembolso solo de una parte del importe. El restante se puede reembolsar también de manera opcional. Estos proveedores tienen marcado el valor de **Completo y parcial** en la tabla anterior. Los proveedores que solo admiten el reembolso completo del importe tienen marcado el valor de **Solo completo**.

  * Odoo no admite esta función en todos los proveedores de pago pero algunos permiten el reembolso de pagos desde la interfaz de su sitio web.

## Finalización de compra exprés

Si el proveedor de pago es compatible con esta función, puede dejar que los
clientes usen los botones de Google Pay y Apple Pay para pagar por las órdenes
de comercio electrónico. Al usar cualquiera de estos botones, pasarán
directamente desde el carrito a la página de confirmación sin tener que llenar
un formulario de contacto, ya que solo tienen que validar el pago en el
formulario de pago de Google o Apple.

Para activar esta función vaya a la pestaña Configuración del proveedor de
pago seleccionado y active Permitir el pago rápido.

Nota

Todos los precios que se muestran en el formulario de pago rápido siempre
incluyen los impuestos.

## Cuotas adicionales

Si el proveedor de pago es compatible con esta función, puede agregar cargos
adicionales para transacciones en línea. Los cargos se pueden configurar como
cantidades o porcentajes **fijos** , **variables** o ambos al mismo tiempo.
También podrán diferir dependiendo si la transacción es **doméstica** o
**internacional**.

Para activar esta función, vaya a la pestaña Cargos del proveedor de pago
seleccionado, active Agregar cuotas adicionales y haga los ajustes que desee.

Nota

Las cuotas se calculan sobre el precio con impuestos incluidos.

## Disponibilidad

Es posible configurar la disponibilidad del proveedor de pago si especifica el
monto máximo permitido y modifica tanto la Divisa como los Países en la
pestaña de Configuración.

### Divisas y países

Todos los proveedores de pago tienen una lista distinta de divisas y países
disponibles. Son el primer filtro durante las operaciones de pago, es decir,
el cliente no podrá usar los métodos de pago vinculados a un proveedor de pago
si su divisa o su país no está en la lista de compatibilidad. Como es posible
que haya errores, actualizaciones y otros problemas, puede agregar o eliminar
divisas o países de la lista de opciones compatibles de un proveedor de pago.

Nota

  * Los métodos de pago también tienen su propia lista de países y divisas compatibles que sirve como otro filtro durante las operaciones de pago.

  * Si la lista de países o divisas compatibles está vacía, significa que la lista es muy larga para mostrarse, u Odoo no tiene la información de este proveedor de pago. El proveedor de pago seguirá estando disponible, aunque es posible que el pago se rechace más adelante si el país o la divisa no son compatibles.

### Cantidad máxima

Puede restringir la Cantidad máxima que se puede pagar con el proveedor de
pago seleccionado. Deje el campo como `0.00` para que el proveedor de pago
esté disponible sin importar la cantidad del pago.

Importante

Esta función no se creó para que funcionara dentro de páginas en las que el
cliente puede actualizar la cantidad del pago, por ejemplo, el snippet de
**donación* y la página de **pago** cuando los [métodos de
envío](../websites/ecommerce/checkout_payment_shipping/shipping.html) están
activados.

## Diario de pagos

Se debe definir un [diario de pago](accounting/bank.html) en el que se
registren los pagos de un proveedor de pago en una **cuenta pendiente**. Para
hacerlo, vaya a la pestaña de Configuración del proveedor de pago seleccionado
y elija un diario de pago.

Nota

  * El diario de pago debe ser un diario de Banco.

  * Puede usar el mismo diario para varios proveedores de pago.

### Perspectiva contable

Desde una perspectiva de contabilidad, hay dos tipos de flujos de pago en
línea: los pagos que se depositan directamente en su cuenta bancaria y siguen
el flujo de [conciliación](accounting/bank/reconciliation.html) usual y los
pagos que vienen de proveedores de pago en línea externos que requieren que se
siga otro flujo de trabajo. Para estos pagos necesita pensar cómo quiere
registrar sus asientos de pago. Le recomendamos que hable con su contador para
obtener su opinión al respecto.

La cuenta bancaria definida para el diario de pago se usa de forma
predeterminada, pero también puede especificar una [cuenta
pendiente](accounting/bank.html#bank-outstanding-accounts) para cada proveedor
de pago y así separar los pagos provenientes de este proveedor del resto de
los pagos.

![Definir una cuenta pendiente para un proveedor de
pago.](../../_images/bank_journal.png)

Ver también

  * [Transferencias bancarias](payment_providers/wire_transfer.html)

  * [Adyen](payment_providers/adyen.html)

  * [Alipay](payment_providers/alipay.html)

  * [Authorize.Net](payment_providers/authorize.html)

  * [AsiaPay](payment_providers/asiapay.html)

  * [Buckaroo](payment_providers/buckaroo.html)

  * [Demostración](payment_providers/demo.html)

  * [Mercado Pago](payment_providers/mercado_pago.html)

  * [Mollie](payment_providers/mollie.html)

  * [Ogone](payment_providers/ogone.html)

  * [PayPal](payment_providers/paypal.html)

  * [Razorpay](payment_providers/razorpay.html)

  * [SIPS](payment_providers/sips.html)

  * [Stripe](payment_providers/stripe.html)

  * [Proveedores de pago](../websites/ecommerce/checkout_payment_shipping/payments.html)

  * [Cuentas bancarias y de efectivo](accounting/bank.html)

