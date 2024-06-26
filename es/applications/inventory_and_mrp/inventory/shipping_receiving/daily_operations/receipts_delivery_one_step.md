# Procesar recepciones y entregas en un paso

De manera predeterminada, los envíos entrantes están configurados para que se
reciban directamente en las existencias. Por otro lado, los envíos salientes
están configurados para entregarse directamente de las existencias al cliente.
La configuración predeterminada para los almacenes en Konvergo ERP es la recepción y
la entrega en un paso.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Los envíos entrantes y salientes no necesitan configurarse con los mismos pasos. Por ejemplo, puede recibir productos en un paso, pero enviarlos en 3 pasos.</p>
</div>

En el siguiente ejemplo, un paso se usará tanto para las recepciones como para
las entregas.

## Configure el almacén

Si el almacén tiene una configuración diferente para las recepciones y envíos,
puede cambiarla fácilmente a la configuración en un solo paso.

Vaya a Inventario ‣ Configuración ‣ Almacenes y haga clic en el almacén que
desea editar. Luego, en la pestaña **Configuración del almacén** , en la
sección **Envíos** , seleccione **Recibir bienes directamente (1 paso)** para
los **Envíos entrantes** o **Entregar bienes directamente (1 paso)** para los
**Envíos salientes**.

![Establezca las opciones de envío entrantes y salientes para recibir y
entregar en un paso. ](../../../../../_images/one-step-warehouse-config.png)

## Recibir bienes directamente (1 paso)

### Crear una orden de compra

En el tablero de la aplicación principal Compras, comience creando una nueva
cotización haciendo clic en **Nuevo**. Luego, seleccione (o cree) un
**Proveedor** desde el menú desplegable del menú, agregue un **Producto**
almacenable a las líneas de orden, y haga clic en **Confirmar orden** para
finalizar la cotización y quede como una nueva orden de compra.

Aparecerá un botón inteligente de **Recepción** en la esquina superior derecha
del formulario de la orden de compra. Haga clic sobre él para ver el recibo
asociado para la orden de compra.

![Botón inteligente de recepción aparecerá en la orden de compra confirmada.
](../../../../../_images/one-step-po-receipt.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>También puede encontrar los recibos de las órdenes de compra en la aplicación Inventario. En la <b>Vista general</b> del tablero, haga clic en el botón <b># Por procesar</b> en la tarjeta kanban de  <b>Recepción</b>.</p>
<img alt="Botón inteligente de 1 Por procesar en la tarjeta kanban de recepción. " class="align-center" src="../../../../../_images/one-step-to-process-btn.png"/>
</div>

### Procesar la recepción

Al ver el recibo (asociado con la orden de compra anterior), haga clic en
**Validar** para completar el recibo.

![Valide la orden de compra a través del botón inteligente Validar.
](../../../../../_images/one-step-po-validate.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si tiene activadas las <b>Ubicaciones de almacenamiento</b>, al hacer clic en el icono de detalles <b>≣ (lista)</b> ubicado junto al icono de eliminar <b>🗑️ (papelera)</b>, aparecerá la ventana emergente de <b>Operaciones detalladas</b>. Esto le permitirá especificar las ubicaciones para los productos recibidos.</p>
<img alt="Seleccione la ubicación de almacenamiento para los productos que recibe en la  ventana emergente de Operaciones detalladas. " class="align-center" src="../../../../../_images/receive-storage-location.png"/>
</div>

Una vez validada la recepción, el producto deja la **Ubicación del proveedor**
y va a la **WH/Ubicación de almacenamiento**. Una vez que llega ahí, estará
disponible para fabricación, ventas, etc. Luego, el estado del documento
cambiará a **Hecho** , y así completar el proceso de recepción en un paso.

## Entregar bienes directamente (1 paso)

### Crear una orden de venta

Comience en el tablero principal de la aplicación Ventas, y cree una nueva
cotización haciendo clic en **Nuevo**. Luego, seleccione (o cree) un
**Cliente** desde el menú desplegable del campo, agregue un **Producto**
almacenable que tenga existencias a las líneas de la orden y haga clic en
**Confirmar** para finalizar la cotización como una orden de ventas.

Aparecerá un botón inteligente de **Recepción** en la esquina superior derecha
del formulario de la orden de compra. Haga clic sobre él para ver el recibo
asociado para la orden de compra.

Aparecerá un botón inteligente de **Entrega** en la esquina superior derecha
del formulario de la orden de ventas. Haga clic sobre él para que aparezca la
orden de entrega asociada para la orden de ventas.

![El botón inteligente de entrega aparecerá después de que se confirmó la
orden de ventas. ](../../../../../_images/one-step-sales-order.png)
<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>También puede encontrar las ordenes de entrega en la aplicación  Inventario. En la <b>Vista general</b> del tablero, haga clic en el botón inteligente <b># Por procesar</b> en <b>Ordenes de entrega</b> en la tarjeta kanban.</p>
<img alt="Botón inteligente de 1 Por procesar en la tarjeta kanban de Ordenes de entrega." class="align-center" src="../../../../../_images/one-step-delivery-to-process.png"/>
</div>

### Procesar la entrega

Al ver la orden de entrega (asociada con la orden de venta anterior), haga
clic en **Validar** para completar la entrega.

![Valide la orden de entrega.](../../../../../_images/validate-one-step-sales-
order.png)

Una vez validada la orden de recolección, el producto deja la **WH/Ubicación
de almacenamiento** y se mueve a la **Ubicación de Partners/Clientes**. Luego,
el estado del documento cambiará a **Hecho** , para completar la entrega en un
paso.

