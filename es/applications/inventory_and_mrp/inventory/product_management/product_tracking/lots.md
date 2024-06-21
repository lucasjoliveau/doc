# Números de lote

Los _lotes_ son una de las dos formas de identificar y rastrear productos en
Konvergo ERP. Por lo general representan un lote específico de productos que recibió,
almacenó, envió o fabricó de forma interna.

Los fabricantes asignan números de lote a grupos de producto que comparten
ciertas propiedades, de esta forma la trazabilidad es mucho más sencilla
durante todo el ciclo de vida del producto.

Los lotes son útiles para gestionar una gran cantidad de productos fabricados
o recibidos, y ayudan a rastrear el grupo al que pertenecen los artículos, lo
cual es útil para retiradas de productos o [fechas de
caducidad](expiration_dates).

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="serial_numbers">Usar números de serie para rastrear productos</a></p>
</div>

## Configuración

Habilite la función _Números de lote y serie_ para rastrear productos por
lotes. Después, vaya al formulario de cada producto para configurar el rastreo
por número de serie.

### Activar lotes y números de serie

Para rastrear productos por medio de lotes debe activar la función _Números de
serie y lote_. Vaya a Inventario ‣ Configuración ‣ Ajustes, busque la sección
**Trazabilidad** , haga clic en la casilla junto a **Números de serie y lote**
y luego haga clic en **Guardar**.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="expiration_dates">Trazabilidad de fechas de caducidad</a></p></li>
<li><p><a href="../../../barcode/operations/gs1_usage#barcode-operations-gs1-lots"><span class="std std-ref">Imprimir códigos de barra GS1 para lotes y números de serie</span></a></p></li>
</ul>
</div> ![Active las funciones de lote y número de serie desde los
ajustes del inventario.](../../../../../_images/enabled-lots-setting.png)

### Rastrear por lotes

Una vez que haya activado la función **úmeros de lote y de serie** , configure
cada producto que debe rastrear mediante lotes. Para ello, vaya a Inventario ‣
Productos ‣ Productos y elija el producto a configurar.

Vaya a la pestaña **Inventario** del formulario del producto. En la sección
**Trazabilidad** , seleccione la opción **Por lotes** en el campo
**Seguimiento**. Ahora podrá asignar números de lote nuevos o existentes a los
lotes que acaba de recibir o fabricar de este producto.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Si un producto tiene existencias disponibles antes de activar el seguimiento por lotes o números de serie, utilice un <a href="../../warehouses_storage/inventory_management/count_products">ajuste de inventario</a> para asignar números de lote a los productos existentes.</p>
</div> ![Función de seguimiento por lotes activada en el
formulario del producto.](../../../../../_images/tracking-product-form.png)

## Asignar lotes para envío y recepción

Asigna nuevos número de lotes a bienes entrantes en el formulario de
recepción. Al enviar productos salientes, seleccione productos con números de
lote específicos en el formulario de entrega.

### Al recibir

Puede asignar números de lote nuevos o existentes a bienes entrantes
directamente en las recepciones.

Para comenzar, vaya a la aplicación Compra para [crear y
confirmar](https://www.youtube.com/watch?v=o_uI718P1Dc) una orden de compra de
productos rastreados por números de lote. Después, haga clic en el botón
inteligente **Recibo** que aparece en la parte superior de la página para ir
al formulario correspondiente.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si quiere ver una recepción existente vaya a la aplicación Inventario, haga clic en la tarjeta de kanban <b>Recibos</b> y seleccione el recibo deseado.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Al hacer clic en <b>Validar</b> antes de asignar un número de lote ocurrirá un <b>error de usuario</b>. Esto indica que <b>debe</b> asignar un número de lote antes de validar la recepción.</p>
<img alt="Ventana emergente de error de usuario para agregar un lote o número de serie." class="align-center" src="../../../../../_images/user-error.png"/>
</div>

En el formulario de recepción, en la línea del producto en la pestaña
**Operaciones** , seleccione el icono **⦙≣ (lista con viñetas)** ubicado a la
derecha del producto rastreado por número de lote.

![Imagen del icono de lista con viñetas en la línea de
producto.](../../../../../_images/bulleted-list-icon.png)

El icono de lista con viñetas en la línea del producto.

Al hacerlo se abrirá la ventana emrergente **Operaciones detalladas** donde se
asignan tanto el **Lote o número de serie** como la cantidad **Hecha**.

Hay dos formas de asignar números de lote, de **manera manual** y al **copiar
y pegar**.

#### Asignación manual

Para asignar números de lotes de forma manual haga clic en **Agregar una
línea** y elija la ubicación en la que almacenará los productos en la columna
**Para**. Después escriba el **número de lote o serie** y especifique la
cantidad **hecha**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Haga clic en <b>Agregar una línea</b> para asignar varios números de lote o almacenar en varias ubicaciones y escriba un nuevo <b>número de serie o de lote</b> para las cantidades adicionales. Repita este proceso hasta que el total en la columna <b>Hecho</b> coincida con la <b>cantidad hecha</b> en la parte superior.</p>
</div> ![Ventana emergente an la que asigne las operaciones
detalladas del número de lote.](../../../../../_images/assign-lot-number-
popup.png)

#### Copiar y pegar

Haga clic en **Agregar una línea** en la hoja de cálculo con todos los números
de lote recibidos del proveedor (o elegidos de forma manual para asignarlos
durante la recepción). Copie y pegue los números de lote en la columna
**Número de lote/serie**.

![Lista de números de lote que se copiaron en una hoja de cálculo de
Excel.](../../../../../_images/lots-excel-spreadsheet.png)

![Números de lote que se copiaron a la línea de
número.](../../../../../_images/bulk-sn.png)

Números de lote copiados a la línea de número de lote, con cada número de lote
en su propia línea.

Konvergo ERP genera las líneas de números de lote necesarias en automático luego de
hacer clic fuera del campo de texto. Las cantidades en la columna **Hecho**
coinciden con la primera entrada. Ajuste las ubicaciones **Para** de forma
manual y las cantidades **Hecho** para cada número de lote según sea
necesario.

Ya que haya asignado números de lote a los productos, haga clic en
**Confirmar** para cerrar la ventana emergente. Después, haga clic en
**Validar** en el formulario de recibo.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="#inventory-product-management-lot-traceability"><span class="std std-ref">Reporte de trazabilidad para los números de lote</span></a></p>
</div>

### Sobre órdenes de entrega

Con Konvergo ERP es posible especificar qué números de lote para un producto se
elegirán para productos salientes en una orden de entrega.

Para comenzar, cree o seleccione una cotización existente en la aplicación
Ventas. El botón inteligente **Entrega** estará disponible luego de confirmar
la orden de venta, haga clic en él para ver el formulario de recibo de almacén
para esa orden de ventas en específico.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>También puede llegar a las órdenes de entrega desde la aplicación Inventario, haciendo clic en la tarjeta de kanban  <b>órdenes de envío</b>.</p>
</div>

Al hacer clic en el botón inteligente **Entrega** se abre el formulario de
orden de entrega en el que deberá seleccionar los números de lote para la
entrega. En la pestaña **Operaciones** , haga clic en el icono **⦙≣ (lista con
viñetas)** ubicado a la derecha del producto que rastrea por números de lote.
Al hacer clic en ese icono aparece la ventana emergente **Operaciones
detalladas**.

En la ventana emergente **Operaciones detalladas** deberá elegir un **número
de lote o de serie** con la cantidad **reservada** completa tomada de ese lote
en específico (si es que este tiene suficientes existencias).

Si no hay existencias suficientes en ese lote, las cantidades parciales de la
**Demanda** se tomarán de varios lotes, cambie la cantidad en la columna
**Hecho** para que solo incluya esa parte específica de la cantidad.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El lote seleccionado para las entregas varía según la estrategia de remoción que elija (<abbr title="Primeras entradas, primeras salidas">FIFO</abbr>, <abbr title="Últimas entradas, primeras salidas">UEPS</abbr> o <abbr title="Primero en expirar, primero en salir">PEPS</abbr>). También dependerá de la cantidad ordenada y si la cantidad disponible en un solo lote basta para completar la orden.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../../warehouses_storage/advanced_operations_warehouse/removal">Estrategias de remoción (PEPS, UEPS, LIFO)</a></p>
</div>

Después, haga clic en **Agregar una línea** , seleccione un **número de lote o
serie** distinto, aplique el resto de cantidades **hechas** y haga clic en
**Confirmar** para cerrar la ventana emergente. Por último, haga clic en el
botón **Validar** para entregar los productos.

![Ventana emergente de operaciones detalladas para números de lote de origen
en órdenes de venta.](../../../../../_images/detailed-operations.png)
<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="expiration_dates">Trazabilidad de fechas de caducidad</a></p></li>
<li><p><a href="../../../barcode/operations/gs1_usage#barcode-operations-gs1-lots"><span class="std std-ref">Imprimir códigos de barra GS1 para lotes y números de serie</span></a></p></li>
</ul>
</div>0

## Gestión de lotes

Para gestionar y ver los números de lote para productos en el tablero
**Lote/números de serie** vaya a Inventario ‣ Productos ‣ Lotes/números de
serie.

Los números de lote están agrupados por producto de forma predeterminada y al
seleccionar el menú desplegable para cada producto aparecen los números
existentes. Seleccione un número de lote para modificar o agregar detalles
vinculados al lote. También puede crear los números de lote desde esta página
al hacer clic en el botón **Nuevo**.

![Imagen del tablero "lotes/números de serie".](../../../../../_images/lot-
dashboard.png)

Mostrar los números de lote agrupados por productos en el tablero
**lote/número de serie**.

### Modificar lotes

Al hacer clic en un lote en el tablero **Lote/número de serie** se mostrará
una página separada donde puede ingresar información adicional sobre el lote.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="expiration_dates">Trazabilidad de fechas de caducidad</a></p></li>
<li><p><a href="../../../barcode/operations/gs1_usage#barcode-operations-gs1-lots"><span class="std std-ref">Imprimir códigos de barra GS1 para lotes y números de serie</span></a></p></li>
</ul>
</div>1

En el formulario de número de lote es posible modificar los siguientes campos:

  * **Lote/Número de serie** : cambiar el número de lote vinculado al **producto**.

  * **Referencia interna** : registra un número de lote o de serie alternativo que se utiliza dentro del almacén y difiere del que utiliza el proveedor o el fabricante.

  * **Empresa** : especificar en qué empresa está disponible el número de lote.

  * **Descripción** : agregar detalles adicionales sobre el lote o número de serie.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="expiration_dates">Trazabilidad de fechas de caducidad</a></p></li>
<li><p><a href="../../../barcode/operations/gs1_usage#barcode-operations-gs1-lots"><span class="std std-ref">Imprimir códigos de barra GS1 para lotes y números de serie</span></a></p></li>
</ul>
</div>2 ![Mostrar el formulario de número de
lote](../../../../../_images/lot-number.png) <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="expiration_dates">Trazabilidad de fechas de caducidad</a></p></li>
<li><p><a href="../../../barcode/operations/gs1_usage#barcode-operations-gs1-lots"><span class="std std-ref">Imprimir códigos de barra GS1 para lotes y números de serie</span></a></p></li>
</ul>
</div>3

### Reservar el número de lote para un producto

Para crear un número de lote para un producto, primero tiene que ir a
Inventario ‣ Productos ‣ Lote/número de serie y haga clic en **Nuevo**.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="expiration_dates">Trazabilidad de fechas de caducidad</a></p></li>
<li><p><a href="../../../barcode/operations/gs1_usage#barcode-operations-gs1-lots"><span class="std std-ref">Imprimir códigos de barra GS1 para lotes y números de serie</span></a></p></li>
</ul>
</div>4 <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="expiration_dates">Trazabilidad de fechas de caducidad</a></p></li>
<li><p><a href="../../../barcode/operations/gs1_usage#barcode-operations-gs1-lots"><span class="std std-ref">Imprimir códigos de barra GS1 para lotes y números de serie</span></a></p></li>
</ul>
</div>5

Una vez que se genere el nuevo **Lote/Número de serie** haga clic en el campo
vacío junto a **Producto** para mostrar el menú desplegable. En este menú,
seleccione el producto al que se le asignará este número.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="expiration_dates">Trazabilidad de fechas de caducidad</a></p></li>
<li><p><a href="../../../barcode/operations/gs1_usage#barcode-operations-gs1-lots"><span class="std std-ref">Imprimir códigos de barra GS1 para lotes y números de serie</span></a></p></li>
</ul>
</div>6

Luego de crear, guardar y asignar un nuevo número de lote al producto deseado,
el número de lote se guarda como un número de lote existente vinculado al
producto y podrá seleccionarlo al asignar números de lote a los productos de
una recepción o al realizar un ajuste de inventario.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="expiration_dates">Trazabilidad de fechas de caducidad</a></p></li>
<li><p><a href="../../../barcode/operations/gs1_usage#barcode-operations-gs1-lots"><span class="std std-ref">Imprimir códigos de barra GS1 para lotes y números de serie</span></a></p></li>
</ul>
</div>7

## Gestione lotes para diferentes tipos de operaciones

De forma predeterminada, solo es posible crear nuevos lotes al recibir
productos y no puede utilizar los números de lote existentes. En las órdenes
de venta solo puede utilizar números de lote existentes y no puede crear
nuevos en la orden de entrega.

Para cambiar si puede usar números de lote nuevos (o existentes) en cualquier
tipo de operación, vaya a Inventario ‣ Configuración ‣ Tipos de operaciones y
seleccione el tipo de operación deseado.

En el formulario del tipo de operación, en la sección **Números de lote y
serie** , seleccione la casilla **Crear nuevo** para permitir la creación de
nuevos números de lote durante este tipo de operación. Elija **Utilizar
existentes** si solo es posible seleccionar números de lote existentes.

![Activar el ajuste de trazabilidad en el formulario de tipo de
operaciones.](../../../../../_images/operations-type-form.png)
<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="expiration_dates">Trazabilidad de fechas de caducidad</a></p></li>
<li><p><a href="../../../barcode/operations/gs1_usage#barcode-operations-gs1-lots"><span class="std std-ref">Imprimir códigos de barra GS1 para lotes y números de serie</span></a></p></li>
</ul>
</div>8

## Trazabilidad

Los fabricantes y las empresas pueden consultar los reportes de trazabilidad
para ver el ciclo de vida completo de un producto: de dónde proviene, cuándo
llegó, dónde se almacenó y a quién se envió (y cuándo).

Para ver la trazabilidad completa de un producto, o agrupar por lotes, vaya a
la aplicación Inventario ‣ Productos ‣ Lotes/Números de serie. De esta manera
podrá ve el tablero de Lotes/Números de serie.

Aquí se enlistarán en automático todos los productos a los que se les haya
asignado un número de lote y se podrá expandir para mostrar los números de
lote que esos productos tienen asignados.

Para agrupar por lotes, primero elimine cualquier filtro de la **barra de
búsqueda**. Después, haga clic en el menú desplegable **Agrupar por** ,
seleccione **Agregar grupo personalizado** , elija **Número de lote/serie**
del menú desplegable y haga clic en **Aplicar**.

De esta manera mostrará todos los lotes o número de serie existentes y puede
expandir la lista para mostrar todas las cantidades de los productos que
tengan asignados ese número.

![Reporte de trazabilidad de los lotes y números de
serie.](../../../../../_images/group-by-number.png)

### Reporte de trazabilidad

Para ver un reporte completo del movimiento de existencias de un número de
lote, seleccione la línea del número de lote en el tablero **Número de serie o
lote** y, en el formulario correspondiente, haga clic en el botón inteligente
**Trazabilidad**.

![Imagen sobre el reporte de trazabilidad para un lote donde se muestran
movimientos de inventario.](../../../../../_images/traceability-report.png)
<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="expiration_dates">Trazabilidad de fechas de caducidad</a></p></li>
<li><p><a href="../../../barcode/operations/gs1_usage#barcode-operations-gs1-lots"><span class="std std-ref">Imprimir códigos de barra GS1 para lotes y números de serie</span></a></p></li>
</ul>
</div>9

