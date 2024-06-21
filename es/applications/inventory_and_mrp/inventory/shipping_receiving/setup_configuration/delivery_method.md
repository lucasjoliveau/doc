# Métodos de envío

La configuración de _Métodos de envío_ , si está activa en Konvergo ERP, agrega una
opción para calcular el costo de envío de las órdenes de venta y de los
carritos de un comercio electrónico

Cuando se integra con un [transportista
externo](third_party_shipper#inventory-shipping-third-party), los precios
de envío se calculan según la información de tarifas y embalaje del
transportista.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="third_party_shipper#inventory-shipping-third-party"><span class="std std-ref">Configurar un transportista externo</span></a></p></li>
<li><p><a href="https://www.odoo.com/slides/slide/delivery-prices-613?fullscreen=1">Tutoriales de Konvergo ERP: precios de envío</a></p></li>
</ul>
</div>

## Configuración

Instale el módulo _Costos de envío_ para calcular el costo de envío de las
órdenes de venta y comercio electrónico. Para ello, vaya a la aplicación
Aplicaciones desde el tablero principal de Konvergo ERP.

Luego, elimine el filtro **Aplicaciones** y escriba `Costos de envío` en la
barra **Buscar…** . Después de encontrar el módulo, haga clic en **Activar**
para instalarlo.

![Instalar el módulo *Costos de envío*.](../../../../../_images/install-
module.png)

## Agregar métodos de envío

Para configurar los métodos de envío, vaya a la aplicación Inventario ‣
Configuración ‣ Métodos de envío.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si la opción <b>Métodos de envío</b> no está disponible en el menú desplegable <b>Configuración</b>, siga estos pasos para verificar que la función está habilitada:</p>
<ol class="arabic simple">
<li><p>Vaya a la aplicación Inventario ‣ Configuración ‣ Ajustes.</p></li>
<li><p>Vaya a la sección <b>Envío</b> y marque la casilla <b>Métodos de envío</b> para activar esta función.</p></li>
</ol>
<img alt="Habilitar la función *Métodos de envío*, se marca la casilla desde Configuración &gt; Ajustes." class="align-center" src="../../../../../_images/enable-delivery1.png"/>
</div>

En la página **Métodos de envío** puede agregar un método si hace clic en
**Nuevo**. Esta acción abre un formulario para que proporcione algunos
detalles sobre el proveedor de envío, como:

  * **Método de envío** (_campo obligatorio_): el nombre del método de envío (por ejemplo, `tarifa plana de envío`, `entrega el mismo día`, etc.).

  * **Proveedor** (_campo obligatorio_): seleccione un servicio de entrega (por ejemplo, FedEx) si utiliza un [transportista externo](third_party_shipper#inventory-shipping-third-party). Asegúrese de que la integración con el transportista está instalada de manera correcta y seleccione el proveedor en el menú desplegable.

Para obtener más información sobre la configuración de métodos de envío
personalizados como el precio fijo, con reglas o las opciones para recoger en
la tienda, consulte las secciones que se encuentran a continuación.

  * **Sitio web** : configure métodos de envío para una página de comercio electrónico. Seleccione el sitio web aplicable en el menú desplegable o déjelo vacío para aplicar el método a todas las páginas web.

  * **Empresa** : si el método de envío debe aplicarse a una empresa en específico, selecciónela en el menú desplegable. Deje el campo vacío para aplicar ese método a todas las empresas.

  * **Producto de envío** (_campo obligatorio_): el producto que aparece en la línea de la orden de venta como el cargo por el envío.

  * **Gratis si el importe de la orden es superior a** : al seleccionar esta casilla, el cliente no pagará por el envío si el importe total de su orden es mayor al importe especificado.

Para consultar algunos ejemplos sobre cómo configurar métodos de envío
específicos, consulte las secciones que se encuentran a continuación.

### Precio fijo

Para configurar el mismo precio de envío para todas las órdenes, vaya a la
aplicación Inventario ‣ Configuración ‣ Métodos de envío. Haga clic en
**Nuevo** y, en el formulario de método de envío, establezca el **proveedor**
como la opción **precio fijo**. Al seleccionar esta opción, el campo **Precio
fijo** estará disponible, allí puede definir el importe de la tarifa fija de
envío.

Para habilitar el envío gratuito si el importe de la orden es mayor al
especificado, marque la casilla **Gratis si el importe de la orden es superior
a** y escriba el importe necesario.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Complete los siguientes campos para configurar una tarifa plana de envío con un costo de <code>$20</code> que pasa a ser gratis si el cliente gasta más de <code>$100</code>:</p>
<ul>
<li><p><b>Método de envío</b>: <code>Tarifa plana de envío</code>.</p></li>
<li><p><b>Proveedor</b>: <b>Precio fijo</b>.</p></li>
<li><p><b>Precio fijo</b>: <code>$20.00</code>.</p></li>
<li><p><b>Gratis si el importe de la orden es superior a</b>: <code>$100.00</code>.</p></li>
<li><p><b>Producto de envío</b>: <code>[ENVÍO] Tarifa plana</code>.</p></li>
</ul>
<img alt="Ejemplo de cómo completar un formulario para un método de envío." class="align-center" src="../../../../../_images/new-shipping-method.png"/>
</div>

### Por reglas

Para calcular el precio del envío con las reglas de precios, establezca el
campo **Proveedor** en la opción **Según las reglas**. De forma opcional,
puede ajustar el **margen en la tarifa** y el **margen adicional** para
incluir costos adicionales de envío.

#### Crear reglas de precios

Vaya a la pestaña **Precios** y haga clic en **Agregar una línea** , esta
acción abrirá la ventana **Crear reglas de precios**. Aquí la **condición**
relacionada con el peso, volumen, precio o cantidad del producto se compara
con una cantidad definida para calcular el **costo de envío**.

Una vez que haya terminado, haga clic en **Guardar y crear nuevo** para
agregar otra regla o en **Guardar y cerrar**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Para que los clientes paguen $20 por el envío de sus órdenes con cinco o menos productos, establezca la <b>condición</b> como <code>Cantidad &lt;= 5.00</code> y el <b>costo de envío</b> en <code>$20</code>.</p>
<img alt="La ventana para mostrar una regla de precios. Aquí se establece la condición y el costo del envío." class="align-center" src="../../../../../_images/pricing-rule.png"/>
</div>

Para restringir el envío a ciertos destinos en el sitio web de comercio
electrónico, vaya a la pestaña **Disponibilidad de destino** en el formulario
del método de envío y defina los **países** , **estados** y **prefijos de
código postal**. Deje estos campos vacíos si puede hacer envíos a cualquier
lugar.

#### Calcular costos de envío

El costo de envío es el **costo de envío** especificado en la regla que cumple
con la **condición** , sumado a cualquier cargo adicional del **margen en la
tarifa** y el **margen adicional**.

\\[Total = costo~de~envío~de~la~regla + (margen~en~la~tarifa \times
costo~de~envío~de~la~regla) + margen~adicional\\]

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Con las siguientes dos reglas configuradas:</p>
<ol class="arabic simple">
<li><p>Si la orden incluye cinco o menos productos, el envío cuesta $20.</p></li>
<li><p>Si la orden incluye más de cinco productos, el envío cuesta $50.</p></li>
</ol>
<p>El <b>margen en la tarifa</b> es <code>10%</code> y el <b>margen adicional</b> es <code>$9.00</code>.</p>
<img alt='Ejemplo con el método de envío "según las reglas" con los márgenes configurados.' class="align-center" src="../../../../../_images/delivery-cost-example.png"/>
<p>Cuando se aplica la primera regla, el costo de envío es de $31 (20 + (0.1 * 20) + 9) y cuando se aplica la segunda regla, el costo de envío es de $64 (50 + (0.1 * 50) + 9).</p>
</div>

### Recoger en tienda

Para que el cliente pueda ir por su orden a la tienda, seleccione **Recoger en
tienda** en el campo **Proveedor** y especifique la ubicación de recolección
en **Almacén**.

Para facturar al cliente por el costo de envío a la ubicación de recolección,
seleccione la opción **Obtener tarifa y crear el envío** en el campo **Nivel
de integración**. Luego, elija la opción **Costo estimado** o **Costo real**
en el campo **Política de facturación** para decidir si el cargo adicional de
envío en la orden de venta es el costo exacto del transportista.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../advanced_operations_shipping/invoicing">Invoice cost of shipping</a></p>
</div>

## Agregar un envío

Las órdenes de venta pueden incluir métodos de envío como si fueran productos
de entrega y aparecen como artículos de línea individuales. Vaya a la orden de
ventas deseada desde la aplicación Ventas ‣ Órdenes ‣ Órdenes.

Haga clic en el botón **Agregar envío** en la orden de venta. Esto abrirá la
ventana emergente **Agregar un método de envío** para que elija un **método de
envío** de la lista.

El **peso total del pedido** se completa de forma automática con el peso (que
debe definir en la pestaña **Inventario** de cada formulario de producto) de
los productos. Edite el campo para especificar el peso exacto y después haga
clic en **Agregar** para establecer el método de envío.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>La cantidad que definió en <b>peso total del pedido</b> sustituye el peso total que definió en los formularios de cada producto.</p>
</div>

El costo de envío aparece en una _línea de la orden de venta_ como el
**producto de envío** detallado en el formulario del método de envío.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>La orden de venta <code>S00088</code> incluye <code>Entrega de muebles</code>, un producto de envío con una tarifa fija de <code>$200</code>.</p>
<blockquote>
<div><img alt="La orden de envío en una línea de la orden de venta." class="align-center" src="../../../../../_images/delivery-product1.png"/>
</div></blockquote>
</div>

### Orden de envío

El método de envío que agregó a la orden de venta está vinculado a los
detalles del transportista en la orden de envío. Para agregar o cambiar el
método de envío desde allí, vaya a la pestaña **Información adicional** y
modifique el campo **Transportista**.

![Información del transportista en el formulario de
envío.](../../../../../_images/delivery-order.png)

