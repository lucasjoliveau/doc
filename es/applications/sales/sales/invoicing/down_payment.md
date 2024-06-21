# Anticipos

Un anticipo es un pago parcial que realiza el comprador cuando se celebra un
contrato de venta. Esto implica el compromiso total de ambas partes (vendedor
y comprador) de cumplir el contrato.

Con un anticipo, el comprador paga una parte del importe total adeudado
mientras acepta pagar la cantidad restante después. Por otra parte, el
vendedor le proporciona los bienes o servicios al comprador después de aceptar
el anticipo, confiando en que este le pagará el importe restante más adelante.

## Crear facturas

Cuando se confirma una orden de venta, se habilita la opción de crear una
factura mediante el botón **Crear factura** ubicado en la esquina superior
izquierda del formulario de orden de venta. Cuando hace clic, aparece la
ventana emergente **Crear facturas**.

![Ventana emergente para crear facturas que aparece en la aplicación
Ventas.](../../../../_images/create-invoices-popup-form.png)
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Las facturas se crean como borradores de forma automática para que las pueda revisar antes de validarlas.</p>
</div>

En la ventana emergente **Crear facturas** , hay 3 opciones para elegir en el
campo **Crear factura** :

  * **Factura normal**

  * **Anticipo (porcentaje)**

  * **Anticipo (importe fijo)**

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Los otros campos desaparecen si selecciona <b>factura normal</b>, ya que solo corresponden a las configuraciones de anticipos.</p>
</div>

## Solicitud inicial de un anticipo

En el formulario emergente para **crear facturas** , las opciones para
anticipos son:

  * **Anticipo (porcentaje)**

  * **Anticipo (importe fijo)**

Una vez que haya seleccionado la opción de anticipo deseada en el campo
**Crear factura** , indique el importe (ya sea como porcentaje o importe fijo)
en el campo **Importe del anticipo**.

Después, seleccione la cuenta de ingresos apropiada para la factura en el
campo **Cuenta de ingresos**. Después, seleccione la cantidad de impuestos en
el campo desplegable **Impuestos del cliente** , solo si es necesario.

![Un formulario emergente para crear facturas con la información apropiada en
los campos de anticipos.](../../../../_images/create-invoices-popup-form-
filled-out.png)

Una vez que los campos tengan la información deseada, haga clic en el botón
**Crear borrador de factura**. Una vez hecho eso, Konvergo ERP le mostrará el
**Borrador de la factura del cliente**.

En la pestaña **Líneas de factura** del **Borrador de la factura del cliente**
aparecerá como un guilabel:`Producto` el anticipo que acaba de configurar en
el formulario emergente **Crear facturas**.

![Anticipo como producto en la pestaña de líneas del borrador de la factura
del cliente en Konvergo ERP.](../../../../_images/down-payment-product-inv-draft.png)
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Cuando hace clic en el producto <b>Anticipo</b> desde la pestaña <b>Líneas de factura</b> aparecerá el formulario del producto para el anticipo.</p>
<p>De manera automática, el <b>Tipo de producto</b> de los anticipos generados para las facturas será <b>Servicio</b>, con la <b>política de facturación</b> configurada a <b>Precio fijo o de prepago</b>.</p>
<img alt="El formulario de producto con el tipo de producto servicio y el campo de política de facturación." class="align-center" src="../../../../_images/down-payment-product.png"/>
<p>Puede editar o modificar este producto en cualquier momento.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Si selecciona:guilabel:<code>Basado en cantidad entregada (manual)</code> como <b>política de facturación</b> <b>no</b> podrá crear una factura.</p>
</div>

## Por ejemplo: solicitar un anticipo del 50%

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El siguiente ejemplo involucra un anticipo del 50% en un producto (<b>Gabinete con puertas</b>) cuya <b>política de facturación</b> es <b>Cantidades ordenadas</b>.</p>
<img alt="El producto de gabinete con puertas donde se muestran varios detalles y campos." class="align-center" src="../../../../_images/cabinet-product-details.png"/>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="invoicing_policy">Facturar por cantidades entregadas u ordenadas</a></p>
</div>

Primero navegue a Ventas ‣ Nuevo y agregue un **Cliente** a la cotización.

Después, haga clic en **Agregar un producto** en la pestaña de **lineas de la
orden** y seleccione el producto **gabinete con puertas**.

Cuando se confirma la orden (al apretar el botón **Confirmar**) la cotización
se convertirá en una orden de venta. Una vez que esto suceda, para crear la
factura solo haga clic en **Crear factura**.

![Orden de venta de un gabinete con puertas que se confirmó en la aplicación
de Ventas.](../../../../_images/cabinet-sales-orders-confirmed.png)

Después, en la ventana emergente **Crear facturas** que aparece, seleccione
**Anticipo (porcentaje)** y escriba `50` en el campo **Importe del anticipo**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Los campos de <b>cuenta de ingresos</b> e <b>impuestos de clientes</b> <em>no</em> son campos obligatorios y <em>no</em> aparecerán si ya se configuraron en una solicitud de pago previa.</p>
<p>Para más información, revise nuestra documentación sobre <a href="#sales-invoicing-customer-tax-modification-down-payments"><span class="std std-ref">modificación de impuestos del cliente en anticipos</span></a> y <a href="#sales-invoicing-income-account-modification"><span class="std std-ref">modificación de la cuenta de ingresos en anticipos</span></a>.</p>
</div>

Finalmente, haga clic en **crear un borrador de factura** para crear un
borrador de factura.

Al hacer clic en **crear borrador de factura** se mostrará el borrador de la
factura, el cual incluye el anticipo como un **Producto** en la pestaña de
**líneas de factura**.

Aquí puede confirmar y publicar la factura, solo debe hacer clic en
**Confirmar** y el estado cambiará de **borrador** a **publicado**. También
muestra una nueva serie de botones en la parte superior de la página.

![Un borrador de factura donde se menciona un anticipo en la aplicación Ventas
de Konvergo ERP.](../../../../_images/draft-invoice-sample.png)

Puede registrar el pago si hace clic en **Registrar pago**.

![Mostrar el botón Registrar pago en una factura de cliente
confirmada.](../../../../_images/register-payment-button.png)

Al hacerlo se mostrará la ventana emergene **Registrar pago** , que se llenará
de forma automática con la información necesaria. Confirme que la información
sea correcta y haga los ajustes necesarios. Cuando esté listo, haga clic en el
botón **Crear pago**.

![Imagen de la ventana emergente para registrar pago con el botón crear
pago.](../../../../_images/register-payment-pop-up-window.png)

Después de hacer clic en **Crear pago** Konvergo ERP mostrará la factura del cliente,
ahora con un listón verde de **En proceso de pago** en la esquina superior
derecha.

![Factura del cliente con un listón En proceso de pago en la esquina superior
derecha.](../../../../_images/customer-invoice-green-payment-banner.png)

Cuando el cliente quiera pagar la cantidad restante de la orden, deberá crear
otra factura. Para ello, use las migas de pan para regresar a la orden de
venta.

En la orden de venta habrá una nueva sección de **Adelantos** en la pestaña
**Líneas de la orden** , junto con el anticipo que acaba de facturar.

![La sección de anticipos en la pestaña de las líneas de la orden en la orden
de ventas.](../../../../_images/down-payments-section-order-lines.png)

Después, haga clic en el botón **Crear factura**.

En la ventana emergente **Crear facturas** verá dos nuevos campos: **Ya se
facturó** y **importe a facturar**.

![La opción para deducir anticipo en la ventana emergente para crear facturas
en la aplicación Ventas de Konvergo ERP.](../../../../_images/create-invoices-pop-up-
already-invoiced.png)

Si ya se pagará la cantidad restante, seleccione la opción **Factura normal**.
Konvergo ERP creará una factura por la cantidad exacta que se necesita para completar
el total del pago, como se indica en el campo **Cantidad por facturar**.

Ya que esté listo, haga clic en **crear borrador de factura**.

Al hacer esto verá la página **borrador de factura de cliente** , la cual
enumerará _todas_ las facturas para esa orden de venta específica en la
pestaña **líneas de factura**. Cada elemento de línea de factura muestra toda
la información necesaria relacionada con cada factura.

Para completar el flujo, haga clic en **confirmar** , lo cual cambiará el
estado de la factura de **borrador** a **publicado**. Luego, haga clic en
**registrar pago**.

Una vez más, aparecerá **registrar pago** , con todos los campos
autocompletados con la información necesaria, incluido el monto restante que
queda por pagar en la orden.

![El segundo formulario emergente de registro de pago en las ventas de
Konvergo ERP.](../../../../_images/second-register-payment-popup.png)

Después de confirmar esa información, haga clic en **crear pago**. Al hacerlo,
se mostrará la **factura del cliente** final con un listón verde con la
leyenda **en proceso de pago** en la esquina superior derecha. Además, podrá
ver ambos pagos iniciales en la pestaña **líneas de factura**.

![La segunda factura del pago con el listón de pago en la aplicación Ventas de
Konvergo ERP.](../../../../_images/second-down-payment-in-payment-invoice.png)

Si llega a este punto ha terminado el flujo.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Este flujo también se puede realizar con la opción de anticipo por <b>importe fijo</b>.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Si se utiliza un anticipo para un producto que tiene una política de facturación por <b>cantidades entregadas</b>, <b>no</b> se podrá deducir al momento de crear la factura para el cliente.</p>
<p>Esto se debe a que, debido a la política de facturación, los productos se deben entregar <em>antes</em> de crear la última factura.</p>
<p>Si no ha entregado ningún producto se creará una <b>nota de crédito</b>, la cual cancelará el borrador de factura que se creó después del anticipo.</p>
<p>Si desea utilizar la opción de <b>nota de crédito</b>, deberá contar con la aplicación <em>Inventario</em> para poder confirmar la entrega. De lo contrario, puede registrar la cantidad entregada de forma manual directamente en la orden de venta.</p>
</div>

## Modificación de impuestos del cliente en los anticipos

Para ajustar la cuenta de ingresos y los impuestos del cliente vinculados a un
anticipo, vaya a la página de **productos** (aplicación Ventas ‣ Productos ‣
Productos), luego escriba `anticipo` en la barra de búsqueda y seleccione el
producto para abrir su página de detalles.

En la página del producto **anticipo** bajo la pestaña **información general**
, en el campo **impuestos del cliente** , podrá modificar los impuestos del
cliente.

![Cómo modificar el enlace de la cuenta de ingresos para los
anticipos.](../../../../_images/customer-taxes-field.png)

## Modificación de la cuenta de ingresos en los anticipos

Si desea cambiar o ajustar la cuenta de ingresos asociada a la página del
producto **anticipo** , **debe** contar con la aplicación _Contabilidad_.

Si tiene la aplicación _Contabilidad_ instalada, podrá ver la pestaña
**Contabilidad** en la página del producto. Si no tiene la aplicación
_Contabilidad_ **no** podrá ver esta pestaña.

En la pestaña **Contabilidad** , puede modificar la **cuenta de ingresos**
desde el campo correspondiente en la sección **Por cobrar**.

![Cómo modificar el enlace de la cuenta de ingresos para los
anticipos.](../../../../_images/income-account.png) <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="invoicing_policy">Facturar por cantidades entregadas u ordenadas</a></p>
</div>

