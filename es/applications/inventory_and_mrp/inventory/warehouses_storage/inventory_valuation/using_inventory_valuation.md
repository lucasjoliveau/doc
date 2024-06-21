# Usar la valoración de inventario

La _valoración de inventario_ es el procedimiento contable por excelencia que
calcula el valor de las existencias a la mano. Una vez determinada, el importe
de la valoración de inventario se incorpora al valor global de una empresa.

En Konvergo ERP, este proceso se puede realizar de forma manual, los empleados del
almacén cuentan los productos físicamente, o de forma automática mediante la
base de datos.

## Valoración automática de inventario

Para usar Konvergo ERP para generar automáticamente un rastro de entradas de
valoración de inventario, primero vaya a la lista de categorías de productos.
Vaya a la aplicación Inventario ‣ Configuración ‣ Categorías de productos y
seleccione la categoría deseada. En el formulario, establezca la **valoración
de inventario** como **automatizada** y para el **método de costos**
seleccione cualquiera de las tres opciones.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p>:doc:` Configurar la valoración del inventario &lt;inventory_valuation_config&gt;`</p>
</div>

Para comprender cómo el movimiento de entrada y salida de productos a las
existencias afecta el valor global de la empresa, considere el siguiente
escenario de movimientos de productos y existencias.

### Recibir un producto

Para rastrear el valor de los productos entrantes, como una _mesa_ , configure
la categoría del producto en su formulario. Vaya a la aplicación Inventario ‣
Productos ‣ Productos y haga clic en el producto deseado. En el formulario de
producto, haga clic en el icono **➡️ (flecha derecha)** junto al campo de
**categoría de producto** , que abre un enlace interno para editar la
categoría de producto. Después, establezca el **método de costo** como
**Últimas entradas, primeras salidas (PEPS)** y la **valoración de
inventario** como **automatizada**.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Como alternativa, acceda al tablero de <b>categorías de productos</b> desde la aplicación Inventario ‣ Configuración ‣ Categorías de productos y seleccione la categoría de producto deseada.</p>
</div>

A continuación, suponga que se compran 10 mesas por un precio de $10.00 cada
una. La orden de compra de esas mesas indicará $100 como el subtotal de la
compra, además de costos adicionales o impuestos.

![Orden de compra con 10 mesas, producto con un valor de $10.00 cada
una.](../../../../../_images/purchase-order.png)

Después de seleccionar **Validar** en la orden de compra, el botón inteligente
**Valoración** está habilitado. Al hacer clic en este botón aparecerá un
reporte que muestra cómo la valoración del inventario para la mesa se vio
afectada por esta compra.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>El <a href="../../../../general/developer_mode#developer-mode"><span class="std std-ref">modo de desarrollador</span></a> <b>debe</b> estar habilitado para poder visualizar el botón inteligente <b>Valoración</b>.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>La función <a href="../advanced_operations_warehouse/owned_stock">consigna</a> permite que los artículos en existencias tengan propietarios. Por lo tanto, los productos que son de otras empresas no se toman en cuenta en la valoración del inventario de la empresa anfitriona.</p>
</div> ![Visualizar el botón Valoración
inteligente en un recibo, con el modo de desarrollador
habilitado.](../../../../../_images/valuation-smart-button.png)

Para un tablero completo que incluye la valoración de inventario de todos los
envíos de productos, ajustes de inventario y operaciones de almacén, consulte
el reporte de valoración de existencias.

### Entregar un producto

Siguiendo la misma lógica, cuando se envía una mesa a un cliente y sale del
almacén, la valoración de inventario disminuye. El botón inteligente
**valoración** en la orden de entrega muestra el registro de valoración de
existencias como lo hace en una orden de compra.

![Disminución de la valoración de inventario tras el envío de un
producto.](../../../../../_images/decreased-stock-valuation.png)

## Reporte de valoración de inventario

Para ver el valor actual de todos los productos en el almacén, primero
habilite el [modo de
desarrollador](../../../../general/developer_mode#developer-mode) y vaya
a la aplicación Inventario ‣ Reportes ‣ Valoración. El tablero de **valoración
de inventario** muestra registros detallados de los productos con la **fecha**
, **cantidad** , **valor unitario** y **valor total** del inventario.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>El <a href="../../../../general/developer_mode#developer-mode"><span class="std std-ref">modo de desarrollador</span></a> <b>debe</b> estar habilitado para poder visualizar la opción <b>valoración</b> en <b>reportes</b>.</p>
</div> ![Reporte de valoración de inventario que muestra varios
productos.](../../../../../_images/inventory-valuation-products.png)

El botón **Valoración a la fecha** ubicado en la esquina superior izquierda de
la página **valoración de existencias** revela una ventana emergente. En esta
puede ver y seleccionar la valoración de inventario de los productos
disponibles durante una fecha anterior especificada.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Podrá ver un registro detallado del valor de inventario de un producto, el movimiento de existencias y las existencias disponibles si selecciona el botón turquesa <b>➡️ (flecha derecha)</b> a la derecha del valor de la columna <b>Referencia</b>.</p>
</div>

### Actualizar el precio unitario de un producto

Para cualquier empresa, los plazos, fallos en la cadena de suministro y otros
factores de riesgo pueden contribuir a los costos invisibles. Aunque Konvergo ERP
intenta representar de forma precisa el valor del inventario, la _valoración
manual_ funciona como una herramienta adicional para actualizar el precio
unitario de productos.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>La valoración manual está diseñada para los productos que se pueden comprar y recibir por un costo mayor a 0 o tienen categorías de productos establecidas con el <b>método de costo</b> como <code>costo promedio (AVCO)</code> o <code>primeras entradas, primeras salidas (PEPS)</code>.</p>
</div> ![Botón para agregar una valoración manual al valor de
inventario de un producto.](../../../../../_images/add-manual-valuation.png)

Cree asientos de valoración manual en el tablero de **valoración de
existencias**. Primero, vaya a la aplicación Inventario ‣ Reportes ‣
Valoración. Después, para habilitar la función _revaloración de producto_ ,
seleccione Agrupar por ‣ Producto para organizar todos los registros por
producto. Haga clic en el icono gris **▶️ (triángulo desplegable)** para que
se muestren los artículos de la línea de valoración de existencias, así como
un botón turquesa **➕ (más)** a la derecha.

Haga clic en el botón turquesa **\+ (más)** para abrir el formulario de
**revaloración de producto**. Aquí, puede volver a calcular la valoración de
inventario de un producto si aumenta o disminuye el precio unitario de cada
producto.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Los botones <b>▶️ (triángulo desplegable)</b> y <b>➕ (más)</b> solo son visibles después de agrupar los asientos por producto.</p>
</div> ![Formulario de revaloración de producto que agrega un
valor de $1.00 por motivos de inflación.](../../../../../_images/product-
revaluation.png)

### Asientos contables de valoración de inventario

En Konvergo ERP, los registros automáticos de valoración de inventario también se
registran en el tablero correspondiente en la aplicación Contabilidad ‣
Contabilidad ‣ Asientos contables. En esta lista detallada de asientos
contables, los registros de valoración de inventario se identifican al
comprobar los valores en la columna **Diario** o al buscar el valor de columna
**Referencia** que coincide con la referencia de la operación del almacén (por
ejemplo, `WH/IN/00014` para recibos).

Al hacer clic en un asiento contable de valoración de inventario se abre un
registro _contable de partida doble_. Konvergo ERP genera estos registros para
rastrear el cambio de valor en la valoración del inventario a medida que los
productos entran y salen del almacén.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Para ver la valoración de inventario de 10 <em>mesas</em> con un costo de $10.00 cada una, vaya a la página asientos contables que se encuentra en la aplicación Contabilidad ‣ Contabilidad ‣ Asientos contables tras recibirlas del proveedor. Aquí, haga clic en la línea de diario donde el valor de la columna <b>Referencia</b> coincide con la referencia en el recibo, <code>WH/IN/00014</code>.</p>
<img alt="Página de valoración de inventario que muestra los productos de un envío." class="align-center" src="../../../../../_images/stock-valuation-product.png"/>
<p>La cuenta <code>provisional de existencias</code> es donde se retiene el dinero destinado para pagar a los proveedores por el producto. La cuenta de <code>valoración de inventario</code> almacena el valor de todas las existencias disponibles.</p>
<img alt="Asiento contable para la valoración de inventario de 10 mesas." class="align-center" src="../../../../../_images/inventory-valuation-entry.png"/>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="https://www.odoo.com/slides/slide/2795/share">Tutoriales de Konvergo ERP: valoración de inventario</a></p>
</div>

