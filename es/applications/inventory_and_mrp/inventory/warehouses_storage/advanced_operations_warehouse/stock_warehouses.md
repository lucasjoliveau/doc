# Vender las existencias de varios almacenes mediante ubicaciones virtuales

Mientras que mantener existencias y vender inventario desde un almacén puede
ser útil para empresas más pequeñas, es posible que aquellas que son más
grandes necesiten mantener existencias en, o vender desde, varios almacenes en
diferentes ubicaciones.

A veces los productos incluidos en una sola orden de venta pueden utilizar
existencias de dos (o más) almacenes. En Konvergo ERP es posible tomar productos de
varios almacenes para cumplir con las demandas de ventas gracias a las
_ubicaciones virtuales_.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Este documento describe el uso de un almacén virtual para cumplir con órdenes de varios almacenes, pero tiene algunas limitaciones. Tome en cuenta lo siguiente antes de continuar:</p>
<ol class="arabic simple">
<li><p>Al establecer un almacén virtual en el campo <b>Almacén</b> de una orden de venta, la dirección del almacén virtual aparecerá en los formularios de recolección, embalaje y entrega, <b>no</b> la dirección del almacén real.</p></li>
<li><p>Cada ubicación tiene un <code>warehouse_id</code> (campo oculto). Esto indica que las existencias en el almacén virtual <b>no</b> serán la suma de aquellas en los almacenes reales, sino la suma de las existencias en las ubicaciones cuyo ID de almacén es el del almacén virtual.</p></li>
</ol>
</div> <div class="alert alert-danger">
<p class="alert-title">
Peligro</p><p>Hay una limitación potencial para quienes hacen uso de las <a href="../../shipping_receiving/daily_operations/receipts_delivery_two_steps">entregas en dos</a> o <a href="../../shipping_receiving/daily_operations/delivery_three_steps">en tres pasos</a>:</p>
<ol class="arabic simple">
<li><p>La zona de salida o de empaquetado en varios formularios aparece de forma incorrecta, pues indica la dirección del almacén virtual.</p></li>
<li><p>No hay ninguna solución alternativa para las entregas en dos o tres pasos.</p></li>
<li><p>Continúe con esto <b>solo</b> en caso de que en el flujo de trabajo de su empresa tenga sentido establecer la dirección de un almacén virtual como la zona de salida o empaquetado.</p></li>
</ol>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Para crear ubicaciones virtuales en almacenes y poder continuar con los siguientes pasos <b>debe</b> activar las funciones <b>Ubicaciones de almacenamiento</b> y <b>Rutas multietapa</b>.</p>
<p>Vaya a Inventario ‣ Configuración ‣ Ajustes, diríjase a la sección <b>Almacén</b>, habilite las opciones <b>Ubicaciones de almacén</b> y <b>Rutas multietapa</b> y haga clic en <b>Guardar</b>.</p>
</div>

## Crear una ubicación principal virtual

Cree un nuevo almacén antes de crear cualquier ubicación virtual para las
existencias. Este nuevo almacén funcionará como un almacén _virtual_ y será la
ubicación _principal_ de otros almacenes físicos.

<div class="accordion accordion-flush o_spoiler alert"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Why a "virtual" warehouse?</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>Los almacenes virtuales son ideales para las empresas con varios almacenes físicos. Esto se debe a que es posible que un almacén se quede sin existencias de un producto en específico, pero que otro aún tenga unidades disponibles. En este caso, las existencias de estos dos (o más) almacenes podrían utilizarse para realizar una única orden de venta.</p>
<p>Los almacenes «virtuales» funcionan como un agrupador único de todo el inventario guardado en los almacenes físicos de una empresa. Se utilizan, por motivos de trazabilidad, para crear jerarquías en las ubicaciones de Konvergo ERP.</p>
</div></div></div></div>

Vaya a Inventario ‣ Configuración ‣ Almacenes para crear un nuevo almacén y
haga clic en **Nuevo**. Desde aquí puede cambiar el **nombre** y el **nombre
corto** del almacén, también puede modificar otros de sus detalles en la
pestaña **Configuración del almacén**.

Por último, haga clic en **Guardar** para terminar de crear un almacén
_regular_. Siga los pasos que se encuentran abajo para terminar de configurar
el almacén principal virtual.

![Formulario de nuevo almacén.](../../../../../_images/stock-warehouses-
create-warehouse.png) <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../inventory_management/warehouses_locations">Configuraciones del almacén</a></p></li>
<li><p><a href="../../shipping_receiving/daily_operations/receipts_delivery_one_step#inventory-receipts-delivery-one-step-wh"><span class="std std-ref">Envíos entrantes y salientes</span></a></p></li>
<li><p><a href="../inventory_management/resupply_warehouses">Reabastecer desde otro almacén</a></p></li>
</ul>
</div>

## Crear almacenes secundarios

Cree al menos dos almacenes _secundarios_ para vincularlos al almacén virtual.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Para poder tomar existencias de varios almacenes y cumplir con una orden de venta, debe haber al menos <b>dos</b> almacenes que actúen como ubicaciones secundarias del almacén principal virtual.</p>
</div>

Vaya a: Inventario ‣ Configuración ‣ Almacenes, haga clic en **Nuevo** y siga
las instrucciones anteriores para configurar las ubicaciones físicas de
existencias.

<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="line-block">
<div class="line"><b>Almacén principal</b></div>
<div class="line"><b>Almacén</b>: <code>Almacén virtual</code></div>
<div class="line"><b>Ubicación</b>: <code>VWH/Stock</code>.</div>
</div>
<div class="line-block">
<div class="line"><b>Almacenes secundarios</b></div>
<div class="line"><b>Almacenes</b>: <code>Almacén A</code> y <code>Almacén B</code></div>
<div class="line"><b>Ubicaciones</b>: <code>WHA</code> y <code>WHB</code>.</div>
</div>
<img alt="Gráfico de las ubicaciones secundarias 'WHA' y 'WHB' vinculadas a la ubicación principal." class="align-center" src="../../../../../_images/parent-location.png"/>
</div> <div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>La ubicación virtual de existencias se cambiará a «Vista» después, pero el <b>tipo de ubicación</b> <b>debe</b> ser <b>Ubicación interna</b> en este punto para <a href="#inventory-routes-link-to-vwh"><span class="std std-ref">vincular los almacenes secundarios</span></a> en la siguiente sección.</p>
</div>

## Vincular almacenes secundarios a las existencias virtuales

Para establecer almacenes físicos como ubicaciones secundarias de la ubicación
virtual configurada en el paso anterior, vaya a Inventario ‣ Configuración ‣
Ubicaciones.

Elimine los filtros de la barra de búsqueda, haga clic en la **ubicación** del
almacén físico que creó para que sea una ubicación secundaria (por ejemplo,
`WHA`) y después haga clic en **Editar**.

Cambie el campo **Ubicación principal** de **ubicaciones físicas** a la
**ubicación de existencias** del almacén virtual (por ejemplo, `VWH/Stock`)
desde el menú desplegable. Después, haga clic en **Guardar**.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Para seleccionar la ubicación del almacén virtual en el menú desplegable <b>Ubicación principal</b>, la ubicación del almacén principal (por ejemplo, <code>VWH/Stock</code>) <b>debe</b> tener su <b>tipo de ubicación</b> configurado en <b>Ubicación interna</b>.</p>
</div> ![Establecer la *ubicación principal* del almacén
secundario en el almacén virtual.](../../../../../_images/configure-physical-
wh.png)

Repita los pasos anteriores para configurar dos o más almacenes secundarios.

Una vez que haya terminado, el almacén virtual principal (por ejemplo,
`VWH/Stock`) completa las órdenes con las existencias de los almacenes
secundarios (por ejemplo, `WHA` y `WHB`) en caso de que no haya suficientes en
alguna otra ubicación.

## Establecer la ubicación virtual de existencias como «Vista»

Establezca el **Tipo de ubicación** de la ubicación virtual de existencias en
**Vista** , ya que es una ubicación inexistente que se utiliza para agrupar
varios almacenes físicos.

Vaya a Inventario ‣ Configuración ‣ Ubicaciones.

En la lista de **Ubicaciones** , haga clic en la correspondiente al almacén
virtual de las existencias que ya había creado (por ejemplo, `VWH/Stock`).

En el formulario de ubicación, en la sección **Información adicional** ,
establezca el **Tipo de ubicación** a **Vista** y **guarde** los cambios.

![Tipos de ubicación de almacén en la pantalla de creación de
ubicaciones.](../../../../../_images/set-location-type-view.png)
<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para visualizar la cantidad total en <b>todos</b> los almacenes secundarios vinculadas, vaya al formulario del producto y haga clic en el botón inteligente <b>Disponible</b>.</p>
<img alt="Mostrar las existencias en todos los almacenes vinculados." class="align-center" src="../../../../../_images/on-hand.png"/>
</div>

## Ejemplos: vender productos de un almacén virtual

Para vender productos desde varios almacenes a través de una ubicación virtual
principal, la base de datos debe tener al menos **dos** almacenes configurados
con al menos **un** producto, y debe haber cantidad disponible en cada
almacén, respectivamente.

<div class="alert alert-danger">
<p class="alert-title">
Peligro</p><p>Hay una limitación potencial para quienes hacen uso de las <a href="../../shipping_receiving/daily_operations/receipts_delivery_two_steps">entregas en dos</a> o <a href="../../shipping_receiving/daily_operations/delivery_three_steps">en tres pasos</a>:</p>
<ol class="arabic simple">
<li><p>La zona de salida o de empaquetado en varios formularios aparece de forma incorrecta, pues indica la dirección del almacén virtual.</p></li>
<li><p>No hay ninguna solución alternativa para las entregas en dos o tres pasos.</p></li>
<li><p>Continúe con esto <b>solo</b> en caso de que en el flujo de trabajo de su empresa tenga sentido establecer la dirección de un almacén virtual como la zona de salida o empaquetado.</p></li>
</ol>
</div>0

Cree una cotización para el producto desde la aplicación Ventas y haga clic en
**Nuevo**. En la cotización agregue un **cliente** y luego haga clic en
**Agregar un producto** para agregar los dos productos almacenados en ambos
almacenes.

Luego, haga clic en la pestaña **Información adicional** en el formulario de
la orden de venta. En la sección **Entrega** , cambie el valor del campo
**Almacén** por el almacén virtual que ya había creado y **confirme** la orden
de venta.

![Establecer el almacén virtual en el campo *Almacén* en la pestaña
*Información adicional* de la orden de venta.](../../../../../_images/set-
virtual-wh.png)

Haga clic en el botón inteligente **Entrega** y en el formulario de entrega
del almacén verifique que el valor de la **Ubicación de origen** coincida con
el valor del campo **Almacén** del formulario de la orden de venta. Ambos
deben incluir la ubicación del almacén virtual.

Por último, en el formulario de entrega del almacén, en la pestaña
**Operaciones detalladas** , verifique que las **ubicaciones** de la columna
**Desde** para cada producto coincidan con las ubicaciones secundarias
vinculadas a la ubicación principal virtual.

![Orden de entrega con ubicaciones de origen y secundarias
coincidentes.](../../../../../_images/delivery-order1.png)
<div class="alert alert-danger">
<p class="alert-title">
Peligro</p><p>Hay una limitación potencial para quienes hacen uso de las <a href="../../shipping_receiving/daily_operations/receipts_delivery_two_steps">entregas en dos</a> o <a href="../../shipping_receiving/daily_operations/delivery_three_steps">en tres pasos</a>:</p>
<ol class="arabic simple">
<li><p>La zona de salida o de empaquetado en varios formularios aparece de forma incorrecta, pues indica la dirección del almacén virtual.</p></li>
<li><p>No hay ninguna solución alternativa para las entregas en dos o tres pasos.</p></li>
<li><p>Continúe con esto <b>solo</b> en caso de que en el flujo de trabajo de su empresa tenga sentido establecer la dirección de un almacén virtual como la zona de salida o empaquetado.</p></li>
</ol>
</div>1 <div class="alert alert-danger">
<p class="alert-title">
Peligro</p><p>Hay una limitación potencial para quienes hacen uso de las <a href="../../shipping_receiving/daily_operations/receipts_delivery_two_steps">entregas en dos</a> o <a href="../../shipping_receiving/daily_operations/delivery_three_steps">en tres pasos</a>:</p>
<ol class="arabic simple">
<li><p>La zona de salida o de empaquetado en varios formularios aparece de forma incorrecta, pues indica la dirección del almacén virtual.</p></li>
<li><p>No hay ninguna solución alternativa para las entregas en dos o tres pasos.</p></li>
<li><p>Continúe con esto <b>solo</b> en caso de que en el flujo de trabajo de su empresa tenga sentido establecer la dirección de un almacén virtual como la zona de salida o empaquetado.</p></li>
</ol>
</div>2

