# Fechas de vencimiento

En Konvergo ERP, puede usar las _fechas de vencimiento_ para gestionar y dar
seguimiento a los ciclos de vida de los productos perecederos en todas sus
etapas. El uso de estas fechas reduce las pérdidas de productos debido a
vencimientos inesperados y ayuda a evitar que envíe productos caducados a los
clientes.

En Konvergo ERP solo le puede agregar información de caducidad a productos que usen
_lotes_ o _números de serie_. Una vez que asignó un lote o número de serie,
podrá configurar una fecha de caducidad. Esto es muy util para empresas que
siempre, o casi siempre, venden productos perecederos, como empresas de
preparación de alimentos.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="lots">Números de lote</a></p></li>
<li><p><a href="serial_numbers">Usar números de serie para rastrear productos</a></p></li>
</ul>
</div>

## Activar las fechas de caducidad

Para activar el uso de _fechas de caducidad_ , vaya a la aplicación Inventario
‣ Configuración ‣ Ajustes, y navegue a la sección **Trazabilidad**. Después
haga clic en la caja para activar la función de **Lotes y números de serie**.

Una vez que active la función, aparecerá una nueva opción para activar las
**fechas de caducidad**. Marque la casilla para activar la función y asegúrese
de **Guardar** los cambios.

![Ajustes de los lotes y números de serie activados y fechas de caducidad
activados.](../../../../../_images/expiration-dates-enabled-settings.png)
<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Ya que haya activado la función <b>Lotes y números de serie</b> aparecerán más funciones para <b>Mostrar números de lote y de serie en recibos de entrega</b>, <b>Mostrar números de lote y de serie en las facturas</b> y para <b>Mostrar fecha de caducidad en las notas de remisión</b>. Activar estas funcionles le ayudará a tener trazabilidad completa, lo que facilitará la gestión de productos que se hayan retirado, a identificar «malos» lotes de productos y mucho más.</p>
</div>

## Configure fechas de caducidad en productos

Una vez que haya activado las funciones de **Fechas de caducidad** y **Lotes y
números de serie** en los ajustes de la aplicación Inventario, podrá
configurar a información de caducidad en productos individuales.

Para hacerlo, vaya a Inventario ‣ Productos ‣ Productos y seleccione un
producto para editarlo. Al seleccionar un producto se mostrará el formulario
de ese artículo en específico. Ya que esté en el formulario del producto, haga
clic en **Editar** en la esquina superior izquierda para realizar cambios.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Para que los productos se puedan rastrear con lotes o números de serie, o para configurar la información de caducidad, el <b>Tipo de producto</b> que aparezca en la pestaña de <b>Información general</b> <em>debe</em> ser <b>Producto almacenable</b>.</p>
</div>

Después, haga clic en la pestaña **Inventario** y baje a la sección titulada
**Trazabilidad**. Desde ahí asegúrese de que la casilla de **Por número de
serie único** o **Por lotes** esté marcada.

Una vez que esté, aparecerá una nueva casilla de **Fecha de caducidad** que
también debe estar marcada. Cuando ambas casillas estén marcadas, aparecerá un
nuevo campo llamado **Fechas** a la derecha.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si un producto tiene existencias a la mano antes de activar el seguimiento por lote o número de serie, es posible que necesite realizar un ajuste de inventario para poder asignar lotes a las existencias que ya tiene.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para procesar grandes cantidades de productos que se recibieron o se entregaron, le recomendamos rastrear los productos con lotes, para que varios productos se puedan rastrear con el mismo lote si ocurren problemas.</p>
</div> ![Configuración de fechas de caducidad
en el formulario del producto.](../../../../../_images/expiration-dates-
product-configuration.png)

En el campo de **fechas** hay cuatro categorías de información de caducidad
que debe configurar para el producto:

  * **Fecha de caducidad** : el número de días después de haber recibido los productos (ya sea de un proveedor o después de producirlos) en los que el producto ya no debería usarse o consumirse por seguridad.

  * **Consumir preferentemente antes de** : el número de días antes de la fecha de caducidad en la que los productos se empezarán a deteriorar **sin** que sean peligrosos todavía.

  * **Tiempo de remoción** : el número de días antes de la fecha de caducidad en los que el producto se debe quitar de existencias.

  * **Periodo de alerta** : el número de días antes de la fecha de caducidad en los que se debería enviar una alerta sobre los bienes en un lote que tengan un número de serie en especial.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Con los valores que ingrese en estos campos se calculará la fecha de caducidad para bienes que ingrese a sus existencias, no importa si los compró a un proveedor o si usted los fabricó.</p>
</div>

Ya que configuró toda la información de fecha de caducidad, haga clic en
**Guardar** para guardar todos los cambios.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si no ingresó ninguna información de caducidad al campo <b>Fechas</b>, puede asignar fechas (o lotes) de manera manual al recibir y entregar productos dentro y fuera del almacén. Incluso cuando ya están asignadas las fechas, las puede cambiar usted mismo si lo necesita.</p>
</div>

## Configure fechas de caducidad al momento de recibir el producto con lotes y
números de serie.

Puede generar fechas de caducidad para bienes **entrantes** directamente desde
la orden de compra. Para crear una orden de compra, vaya a Compra y haga clic
en **Crear** para crear una nueva solicitud de cotización.

Después, agregue un **Proveedor** y después haga clic en **Añadir un
producto** para agregar **Productos** a las líneas de productos.

Para elegir la cantidad que desea ordenar cambie el número de la columna
**Cantidad**. Haga clic en **Confirmar orden**. De esta manera convertirá la
Solicitud de cotización en una orden de compra.

Haga clic en el botón inteligente **Recepción** en la parte superior de la
orden de compra para llegar al formulario de recepción del almacén.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si hace clic en <b>Validar</b> antes de asignar un número de serie a las cantidades del producto ordenado, aparecerá una ventana emergente de <b>Error del usuario</b>, que le pedirá que ingrese un número de serie o lote para los productos ordenados. No se puede validar la <abbr title="RFQ en inglés">Solicitud de cotización</abbr> si no ha asignado un lote o un número de serie.</p>
<img alt="Ventana emergente de error del usuario cuando se valida una orden sin número de lote." class="align-center" src="../../../../../_images/expiration-dates-user-error-popup.png"/>
</div>

Desde aquí puede hacer clic en el icono de menú de **Opciones adicionales**
que se encuentra hasta la derecha de la línea del producto. Al hacer clic en
este icono, aparecerá una ventana emergente de **Operaciones detalladas**.

En esta ventana emergente haga clic en **Agregar una línea** y asigne un lote
o número de serie en el campo **Lote/número de serie**

De manera automática se llena una fecha de caducidad según la configuración en
el formulario del producto (si se configuró antes).

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si no ha configurado el campo <b>Fechas</b> en el formulario del producto, puede ingresar esta fecha de manera manual.</p>
</div>

Después de que se estableció la fecha de caducidad, marque **Hecho** en las
cantidades y haga clic en **Confirmar** para cerrar las ventanas emergentes.
Después, haga clic en **Validar**.

![Ventana emergente de operaciones detalladas en las que se muestran fechas de
caducidad para productos ordenados.](../../../../../_images/expiration-dates-
detailed-operations-popup.png)

Cuando valide que recibió un producto, aparecerá un botón de **Trazabilidad**.
Si hace clic en este botón podrá ver un **Reporte de trazabilidad**
actualizado en el que se incluye un documento de **referencia** , el
**producto** que está rastreando, el **Lote o número de serie** y más.

## Configurar fechas de caducidad en productos fabricados

También puede generar fechas de caducidad para productos que usted fabrique.
Para asignar fechas de caducidad a estos productos, debe completar una orden
de fabricación.

Para crear una **Orden de fabricación** vaya a Fabricación ‣ Operaciones ‣
Órdenes de fabricación y haga clic en **Crear**. Abra el menú extendible del
campo **Producto** y elija el producto que quiere crear, después elija la
guilabel:`Cantidad` que quiere producir.

![Orden de fabricación para un producto que tiene fecha de
caducidad.](../../../../../_images/expiration-dates-manufacturing-order.png)
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Para fabricar un producto, debe haber materiales por consumir en las líneas de la columna <b>Producto</b>. Para hacer esto debe crear una <b>Lista de materiales</b> para el  <b>Producto</b> o debe agregar materiales por consumir de manera manual, solo tiene que hacer clic en <b>Agregar una línea</b>.</p>
</div>

Ya que esté listo, haga clic en **Confirmar**.

Para asignar un número de lote, seleccione un número de lote existente desde
el menú desplegable junto a **Lote/Número de serie** o haga clic en el **+**
verde.

Después, seleccione un número de unidades para el campo **Cantidad** y después
haga clic en **Marcar como hecho**.

Haga clic en el icono **Enlace externo** en el campo de **Lote/Número de
serie** asignado. Aparecerá una ventana emergente donde se mostrará todos los
detalles de ese número específico.

En esa ventana emergente, vaya a la pestaña **Fechas** y podrá ver toda la
información sobre fecha de caducidad que había configurado antes en el
producto. Esta información también está disponible en el formulario de
detalles de ese producto en específico, para verlo vaya a Inventario ‣
Productos ‣ Lote/Número de serie.

![Pestaña de fechas con información de caducidad para un número de lote
específico.](../../../../../_images/expiration-dates-dates-tab-lot-number.png)

## Vender productos con fechas de caducidad

Los productos perecederos que tienen fecha de caducidad se venden de la misma
manera que cualquier otro tipo de producto. El primer paso es vender el
producto perecedero para crear una orden de venta.

Para hacer esto, vaya a Ventas ‣ Crear, cree una nueva cotización y llene la
información en la orden de venta.

Agregue un **Cliente** , haga clic en **Agregar un producto** para agregar los
productos deseados a las líneas de **Producto** y configure una **Cantidad**
para los productos.

Después haga clic en la pestaña **Other Info** tab. En la sección **Entrega**
cambie la **Fecha de entrega** a una fecha después de la fecha esperada y haga
clic en **la palomita verde** para confirmar la fecha. Finalmente, haga clic
en **Confirmar** para confirmar la orden de venta.

Después, haga clic en el botón inteligente de **Entrega** que se encuentra en
la parte superior de la orden de ventas para poder ver el formulario de
entrega del almacén.

En el formulario de recepción del almacén, haga clic en **Validar** , y
después en **Aplicar** en la ventana emergente que saldrá. Así podrá procesar
todas las cantidades **Hechas** de manera automática y podrá entregarle los
productos al cliente.

Si los productos se entregan antes de que configure la **Fecha de alerta** en
el formulario del producto, no se crearán advertencias.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Ya que haya activado la función <b>Lotes y números de serie</b> aparecerán más funciones para <b>Mostrar números de lote y de serie en recibos de entrega</b>, <b>Mostrar números de lote y de serie en las facturas</b> y para <b>Mostrar fecha de caducidad en las notas de remisión</b>. Activar estas funcionles le ayudará a tener trazabilidad completa, lo que facilitará la gestión de productos que se hayan retirado, a identificar «malos» lotes de productos y mucho más.</p>
</div>0 <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Ya que haya activado la función <b>Lotes y números de serie</b> aparecerán más funciones para <b>Mostrar números de lote y de serie en recibos de entrega</b>, <b>Mostrar números de lote y de serie en las facturas</b> y para <b>Mostrar fecha de caducidad en las notas de remisión</b>. Activar estas funcionles le ayudará a tener trazabilidad completa, lo que facilitará la gestión de productos que se hayan retirado, a identificar «malos» lotes de productos y mucho más.</p>
</div>1

## Ver las fechas de caducidad para lotes y números de sere.

Para ver (o agrupar) todos los productos con fecha de caducidad por lote, vaya
a Inventario ‣ Productos ‣ Lotes/Números de serie.

Quite todos los filtros de búsqueda automáticos de la barra **Buscar…**.
Después, haga clic en **Agrupar por** , elija **Agregar grupo personalizado**
y seleccione el parámetro **Fecha de caducidad** desde el menú desplegable.
Para aplicar el filtro haga clic en **Aplicar**

Si sigue estos pasos obtendrá un desglose de todos los productos perecederos,
como sus fechas de caducidad y el número de lote que se les asignó.

![Agrupar por fechas de caducidad en lotes y números de
serie.](../../../../../_images/expiration-dates-group-by-dates.png)

### Alertas de caducidad

Para ver alertas de caducidad vaya a Inventario ‣ Productos ‣ Lotes/Números de
serie.

Después, haga clic en el **Lote/Número de serie** que tenga productos
perecederos para mostrar el formulario que contiene el número de serie. En el
formulario de número de serie, haga clic en la pestaña **Fechas** para ver
toda la información de caducidad que se relaciona a los productos.

Para editar el formulario haga clic en **Editar** en la esquina superior
izquierda del formulario, después cambie la **Fecha de caducidad** a la fecha
de hoy (o antes) y haga clic en **Guardar** para guardar los cambios.

Después de guarder, el formulario de número de lote mostrará una **alerta de
caducidad** en rojo en la parte superior del formulario para indicar que los
productos de este lote ya caducaron o caducarán pronto. Desde aquí, regrese a
la página de **Lote/Número de serie** (a través de las migajas de pan).

Para ver la alerta de caducidad nueva, o cualquier alerta de caducidad para
productos que ya caducaron (o caducarán pronto), quite todos los filtros de
búsqueda de la barra **Buscar…** en el tablero de **Lote/Número de serie**.

Después, haga clic en **Filtros** y elija **alerta de caducidad**.

![Alerta de caducidad para un producto que ya
caducó.](../../../../../_images/expiration-dates-expiration-alert.png)

  *[Solicitud de cotización]: RFQ en inglés

