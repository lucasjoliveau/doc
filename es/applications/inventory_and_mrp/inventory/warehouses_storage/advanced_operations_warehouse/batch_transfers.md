# Recolección por lotes

Una sola persona puede gestionar varias órdenes a la vez gracias a la
_recolección por lotes_. Esta función reduce el tiempo que toma recorrer la
misma ubicación dentro del almacén.

Al realizar recolecciones por lote, las órdenes se agrupan y se marcan en una
lista de recolección. Después de recolectar el lote, este se lleva a una
ubicación de salida, donde los productos se colocan en sus empaques de entrega
respectivos.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="#inventory-management-barcode-picking"><span class="std std-ref">Usar la aplicación Código de barras para recolecciones</span></a></p>
</div>

Como las órdenes _deben_ acomodarse en la ubicación de salida después de la
recolección, este método de recolección va mejor con empresas que tienen pocos
productos que acomodar cada vez. Acomodar productos de alta demanda en
ubicaciones de fácil acceso aumentará el número de órdenes que se realizan con
eficacia.

## Configuración

Para activar la opción de recolección por lotes, vaya a la aplicación
Inventario ‣ Configuración ‣ Ajustes. En la sección **Operaciones** marque la
caja **Translados por lote**.

![Active los *traslados por lote* en Inventario > Configuración > Ajustes.
](../../../../../_images/batch-transfer-checkbox.png)

Ya que el método de recolección por lote se usa para optimizar la operación
_de recolección_ dentro de Konvergo ERP, las **Ubicaciones de almacenamiento** y las
opciones para configurar las opciones de **las rutas multietapa** en la
sección **Almacén** también se tienen que marcar en la página de ajustes. Una
vez que termine, haga clic en **Guardar**.

![Active las *Ubicaciones de almacenamiento* y las *rutas multietapa* en
Inventario > Configuración > Ajustes.](../../../../../_images/locations-
routes-checkbox.png)

Finalmente, active la función de recolección en el almacén. Para esto, vaya a
la página de ajustes del almacén en la aplicación de Inventario ‣
Configuración ‣ Almacenes.

Seleccione el almacén que desea de la lista. Después, de las opciones
disponibles para **Envíos salientes** seleccione **Enviar artículos a
ubicación de salida y entregar (2 pasos)** o **Empaquetar artículos, enviar
productos a ubicación de salida y enviar (3 pasos)**.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../../shipping_receiving/daily_operations/receipts_delivery_two_steps#inventory-receipts-delivery-two-steps"><span class="std std-ref">Entrega en dos pasos</span></a></p></li>
<li><p><a href="../../shipping_receiving/daily_operations/delivery_three_steps#inventory-delivery-three-steps"><span class="std std-ref">Entrega en tres pasos</span></a></p></li>
</ul>
</div> ![Configuración de envíos salientes de 2 o 3 pasos.
](../../../../../_images/set-2-or-3-step-shipment.png)

## Crear traslados por lote

Crea traslados por lote de forma manual directo desde la aplicación Inventario
‣ Operaciones ‣ Traslados por lote. Haga clic en **nuevo** para crear un nuevo
traslado por lote.

En el formulario del traslado por lote completa los siguientes campos:

  * **Responsable** : empleado asignado a la recolección. Deje este campo en blanco si _ningún_ empleado puede hacer la recolección.

  * **Tipo de operación** : en el menú desplegable, seleccione el tipo de operación bajo el que se clasifica la recolección.

  * **Fecha programada** : especifica la fecha en la que el **responsable** debe completar el traslado a la ubicación de salida.

A continuación, en la lista de **traslados** , haga clic en **agregar una
línea** para abrir la ventana **Agregar: traslados**.

Si completó el campo **Tipo de operación** , la lista filtrará los registros
de traslado que coincidan con el **Tipo de operación** seleccionado.

Haga clic en el botón **Nuevo** para crear un nuevo traslado.

Una vez seleccionados los registros de traslado, haga clic en **Confirmar**
para confirmar la recolección de lotes.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Se ha asignado un nuevo traslado de lote al <b>responsable</b>, <code>Joel Willis</code>, para el <b>tipo de operación</b> de <code>recolección</code>. La <b>fecha programada</b> se establece en <code>11 de agosto</code>.</p>
<img alt="Vista del formulario *traslados por lotes*." class="align-center" src="../../../../../_images/batch-transfer-form.png"/>
<p>Si hace clic en el botón <b>Añadir una línea</b>, se abrirá la ventana <b>Añadir: traslado</b>, en la que solo se mostrarán los traslados. Esto se debe a que el <b>Tipo de operación</b> se ha establecido en <code>Recolectar</code> en el formulario de traslado por lotes.</p>
<p>Haga clic en la casilla de verificación junto a los traslados <code>WH/PICK/00001</code> y <code>WH/PICK/00002</code> para incluirlos en el nuevo traslado. Después, haga clic en el botón <b>Seleccionar</b> para cerrar la ventana <b>Añadir: traslados</b>.</p>
<img alt="Seleccione varios traslados desde la ventana *Añadir: traslados*." class="align-center" src="../../../../../_images/add-transfers-window.png"/>
</div>

### Añadir un lote de la lista de traslados

Existe otro método para crear traslados por lotes mediante la opción **Agregar
a lote** de una lista. Vaya al menú desplegable de la aplicación Inventario ‣
Operaciones y seleccione cualquiera de los **Traslados** para abrir una lista
filtrada de traslados.

![Mostrar todos los tipos de traslados en un menú desplegable: recibidos,
entregas, traslados internos, fabricaciones, traslados por lote,
triangulaciones.](../../../../../_images/transfers-drop-down.png)

En la lista de traslados seleccione la casilla de verificación ubicada a la
izquierda de las transferencias seleccionadas para añadirlas a un lote. A
continuación, vaya al botón **Acciones ⚙️ (engranaje)** y haga clic en
**Agregar a lote** en el menú desplegable.

![Uso del botón *Agregar a lote* desde la lista del botón de
*acción*.](../../../../../_images/add-to-batch.png)

Al hacerlo, se abrirá una ventana emergente **Añadir al lote** , en la que se
puede asignar el empleado **responsable** de la recolección.

Elija una de las dos opciones para agregar al **traslado por lote existente**
o cree un **nuevo traslado por lote**.

Si desea iniciar con un borrador, seleccione la casilla de verificación
**borrador**.

Termine el proceso al hacer clic en **confirmar**.

![Mostrar la ventana *Añadir al lote* para crear un traslado por
lotes.](../../../../../_images/add-to-batch-window.png)

## Procesar traslados en lote

Gestione los traslados por lotes en la página de la aplicación Inventario ‣
Operaciones ‣ Traslados por lote.

Desde aquí, seleccione el traslado deseado de la lista. A continuación, vaya
al formulario de traslado por lote e introduzca las cantidades **Hecho** de
cada producto en la pestaña **Operaciones detalladas**. Por último, seleccione
**Validar** para completar la recolección.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Asegúrese de que el traslado por lote se ha completado cuando el botón <b>Validar</b> aparezca resaltado en morado. Si en su lugar aparece el botón <b>Comprobar la disponibilidad</b> resaltado, significa que hay artículos en el lote que actualmente <em>no</em> están disponibles en existencias.</p>
</div> <div class="alert alert-success" id="inventory-management-batch-transfers-example">
<p class="alert-title">
Example</p><p>En un traslado por lotes que incluye productos de las recolecciones <code>WH/PICK/00001</code> y <code>WH/PICK/00002</code>, la pestaña <b>Operaciones detalladas</b> muestra que se ha realizado la recolección del producto <code>Armario con puertas</code> porque la columna <b>Hecho</b> coincide con el valor de la columna <b>Reservado</b>. Sin embargo, se han recogido cantidades de <code>0.00</code> para el otro producto, <code>Caja organizadora de cables</code>.</p>
<img alt="Mostrar traslado por lotes de productos de dos recolecciones en la pestaña *Operaciones detalladas*." class="align-center" src="../../../../../_images/process-batch-transfer.png"/>
</div>

Solo se muestran los productos en existencias en la pestaña **Operaciones
detalladas**

Para ver la lista completa de productos, vaya a la pestaña **Operaciones**. En
esta lista, la columna **Demanda** indica la cantidad necesaria para la orden.
La columna **Reservado** muestra las existencias disponibles para completar la
orden. Por último, la columna **Hecho** especifica los productos que se han
recolectado y están listos para el siguiente paso.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>El producto, <code>alfombrilla de escritorio</code>, es parte del mismo lote del <a href="#inventory-management-batch-transfers-example"><span class="std std-ref">ejemplo anterior</span></a> y solo es visible en la pestaña <b>Operaciones</b> porque no hay cantidades <b>Reservadas</b> en existencias para completar la recolección del lote.</p>
<p>Haga clic en el botón <b>Comprobar disponibilidad</b> para buscar las existencias de los productos disponibles.</p>
<img alt="Mostrar las cantidades reservadas no disponibles en la pestaña *Operaciones*." class="align-center" src="../../../../../_images/operations-tab.png"/>
</div>

### Crear orden parcial

Si en el formulario de traslado por lote la cantidad **hecha** del producto es
_menor_ a la cantidad **reservada** , aparecerá una ventana emergente.

En esta ventana tendrá la opción de **crear una orden parcial**.

Si hace clic en **Crear orden parcial** , se creará un nuevo traslado por lote
con los productos restantes de forma automática.

Si desea terminar la recolección _sin_ crear otra recolección por lote, haga
clic en **Sin orden parcial**.

Haga clic en **descartar** para cancelar la validación y regresar al
formulario de traslado por lote.

![Ventana emergente para crear orden parcial](../../../../../_images/create-
backorder.png)

## Procesar traslado por lote: aplicación Código de barras

Los traslados por lotes creados también aparecen en la aplicación Código de
barras, a la que se accede haciendo clic en el botón **Traslados por lote**.

De forma predeterminada, las recolecciones por lotes confirmadas aparecen en
la página **Traslados por lotes**. Haga clic en el traslado por lotes deseado
para abrir la lista detallada de productos para la recolección.

![Mostrar lista de traslados por completar desde la aplicación *Código de
barras*.](../../../../../_images/barcode-batch-transfers.png)

Siga las instrucciones que aparecen en la parte superior de la página con
fondo negro para el traslado por lotes seleccionado. Comience por escanear el
código de barras del producto para registrar un único producto para la
recolección. Si desea registrar varias cantidades, haga clic en el icono **✏️
(lápiz)** e introduzca las cantidades necesarias para la recolección.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Los productos de la misma orden están etiquetados con el mismo color a la izquierda. Las recolecciones completadas se destacan en verde.</p>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>En un traslado por lotes de 2 <code>Armarios con puertas</code>, 3 <code>Pantallas acústicas</code> y 4 <code>Escritorios para cuatro personas</code>, las etiquetas <code>3/3</code> y <code>4/4</code> <b>unidades</b> indican que las dos últimas recolecciones de productos se completaron con éxito.</p>
<p>Ya se han recogido <code>1/2</code> unidades del <code>armario con puertas</code>, y después de escanear el código de barras del producto para el segundo armario, Konvergo ERP solicita al usuario que <code>escanee un número de serie</code> para registrar el número de serie único para el <a href="../../product_management/product_tracking/serial_numbers#inventory-serial-numbers-configure"><span class="std std-ref">seguimiento del producto</span></a>.</p>
<img alt="Visualización de los productos a recoger en la vista de código de barras." class="align-center" src="../../../../../_images/barcode-products.png"/>
</div>

Una vez seleccionados todos los productos, haga clic en **validar** para
marcar el traslado por lotes como **Hecho**.

