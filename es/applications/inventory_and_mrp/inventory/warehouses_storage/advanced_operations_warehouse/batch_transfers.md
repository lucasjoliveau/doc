# Recolección por lotes

Una sola persona puede gestionar varias órdenes a la vez gracias a la
_recolección por lotes_. Esta función reduce el tiempo que toma recorrer la
misma ubicación dentro del almacén.

Al realizar recolecciones por lote, las órdenes se agrupan y se marcan en una
lista de recolección. Después de recolectar el lote, este se lleva a una
ubicación de salida, donde los productos se colocan en sus empaques de entrega
respectivos.

Ver también

Usar la aplicación Código de barras para recolecciones

Como las órdenes _deben_ acomodarse en la ubicación de salida después de la
recolección, este método de recolección va mejor con empresas que tienen pocos
productos que acomodar cada vez. Acomodar productos de alta demanda en
ubicaciones de fácil acceso aumentará el número de órdenes que se realizan con
eficacia.

## Configuración

Para activar la opción de recolección por lotes, vaya a la aplicación
Inventario ‣ Configuración ‣ Ajustes. En la sección Operaciones marque la caja
Translados por lote.

![Active los *traslados por lote* en Inventario > Configuración > Ajustes.
](../../../../../_images/batch-transfer-checkbox.png)

Ya que el método de recolección por lote se usa para optimizar la operación
_de recolección_ dentro de Odoo, las Ubicaciones de almacenamiento y las
opciones para configurar las opciones de las rutas multietapa en la sección
Almacén también se tienen que marcar en la página de ajustes. Una vez que
termine, haga clic en Guardar.

![Active las *Ubicaciones de almacenamiento* y las *rutas multietapa* en
Inventario > Configuración > Ajustes.](../../../../../_images/locations-
routes-checkbox.png)

Finalmente, active la función de recolección en el almacén. Para esto, vaya a
la página de ajustes del almacén en la aplicación de Inventario ‣
Configuración ‣ Almacenes.

Seleccione el almacén que desea de la lista. Después, de las opciones
disponibles para Envíos salientes seleccione Enviar artículos a ubicación de
salida y entregar (2 pasos) o Empaquetar artículos, enviar productos a
ubicación de salida y enviar (3 pasos).

Ver también

  * [Entrega en dos pasos](../../shipping_receiving/daily_operations/receipts_delivery_two_steps.html#inventory-receipts-delivery-two-steps)

  * [Entrega en tres pasos](../../shipping_receiving/daily_operations/delivery_three_steps.html#inventory-delivery-three-steps)

![Configuración de envíos salientes de 2 o 3 pasos.
](../../../../../_images/set-2-or-3-step-shipment.png)

## Crear traslados por lote

Crea traslados por lote de forma manual directo desde la aplicación Inventario
‣ Operaciones ‣ Traslados por lote. Haga clic en nuevo para crear un nuevo
traslado por lote.

En el formulario del traslado por lote completa los siguientes campos:

  * Responsable: empleado asignado a la recolección. Deje este campo en blanco si _ningún_ empleado puede hacer la recolección.

  * Tipo de operación: en el menú desplegable, seleccione el tipo de operación bajo el que se clasifica la recolección.

  * Fecha programada: especifica la fecha en la que el responsable debe completar el traslado a la ubicación de salida.

A continuación, en la lista de traslados, haga clic en agregar una línea para
abrir la ventana Agregar: traslados.

Si completó el campo Tipo de operación, la lista filtrará los registros de
traslado que coincidan con el Tipo de operación seleccionado.

Haga clic en el botón Nuevo para crear un nuevo traslado.

Una vez seleccionados los registros de traslado, haga clic en Confirmar para
confirmar la recolección de lotes.

Example

Se ha asignado un nuevo traslado de lote al responsable, `Joel Willis`, para
el tipo de operación de `recolección`. La fecha programada se establece en `11
de agosto`.

![Vista del formulario *traslados por lotes*.](../../../../../_images/batch-
transfer-form.png)

Si hace clic en el botón Añadir una línea, se abrirá la ventana Añadir:
traslado, en la que solo se mostrarán los traslados. Esto se debe a que el
Tipo de operación se ha establecido en `Recolectar` en el formulario de
traslado por lotes.

Haga clic en la casilla de verificación junto a los traslados `WH/PICK/00001`
y `WH/PICK/00002` para incluirlos en el nuevo traslado. Después, haga clic en
el botón Seleccionar para cerrar la ventana Añadir: traslados.

![Seleccione varios traslados desde la ventana *Añadir:
traslados*.](../../../../../_images/add-transfers-window.png)

### Añadir un lote de la lista de traslados

Existe otro método para crear traslados por lotes mediante la opción Agregar a
lote de una lista. Vaya al menú desplegable de la aplicación Inventario ‣
Operaciones y seleccione cualquiera de los Traslados para abrir una lista
filtrada de traslados.

![Mostrar todos los tipos de traslados en un menú desplegable: recibidos,
entregas, traslados internos, fabricaciones, traslados por lote,
triangulaciones.](../../../../../_images/transfers-drop-down.png)

En la lista de traslados seleccione la casilla de verificación ubicada a la
izquierda de las transferencias seleccionadas para añadirlas a un lote. A
continuación, vaya al botón Acciones ⚙️ (engranaje) y haga clic en Agregar a
lote en el menú desplegable.

![Uso del botón *Agregar a lote* desde la lista del botón de
*acción*.](../../../../../_images/add-to-batch.png)

Al hacerlo, se abrirá una ventana emergente Añadir al lote, en la que se puede
asignar el empleado responsable de la recolección.

Elija una de las dos opciones para agregar al traslado por lote existente o
cree un nuevo traslado por lote.

Si desea iniciar con un borrador, seleccione la casilla de verificación
borrador.

Termine el proceso al hacer clic en confirmar.

![Mostrar la ventana *Añadir al lote* para crear un traslado por
lotes.](../../../../../_images/add-to-batch-window.png)

## Procesar traslados en lote

Gestione los traslados por lotes en la página de la aplicación Inventario ‣
Operaciones ‣ Traslados por lote.

Desde aquí, seleccione el traslado deseado de la lista. A continuación, vaya
al formulario de traslado por lote e introduzca las cantidades Hecho de cada
producto en la pestaña Operaciones detalladas. Por último, seleccione Validar
para completar la recolección.

Truco

Asegúrese de que el traslado por lote se ha completado cuando el botón Validar
aparezca resaltado en morado. Si en su lugar aparece el botón Comprobar la
disponibilidad resaltado, significa que hay artículos en el lote que
actualmente _no_ están disponibles en existencias.

Example

En un traslado por lotes que incluye productos de las recolecciones
`WH/PICK/00001` y `WH/PICK/00002`, la pestaña Operaciones detalladas muestra
que se ha realizado la recolección del producto `Armario con puertas` porque
la columna Hecho coincide con el valor de la columna Reservado. Sin embargo,
se han recogido cantidades de `0.00` para el otro producto, `Caja organizadora
de cables`.

![Mostrar traslado por lotes de productos de dos recolecciones en la pestaña
*Operaciones detalladas*.](../../../../../_images/process-batch-transfer.png)

Solo se muestran los productos en existencias en la pestaña Operaciones
detalladas

Para ver la lista completa de productos, vaya a la pestaña Operaciones. En
esta lista, la columna Demanda indica la cantidad necesaria para la orden. La
columna Reservado muestra las existencias disponibles para completar la orden.
Por último, la columna Hecho especifica los productos que se han recolectado y
están listos para el siguiente paso.

Example

El producto, `alfombrilla de escritorio`, es parte del mismo lote del ejemplo
anterior y solo es visible en la pestaña Operaciones porque no hay cantidades
Reservadas en existencias para completar la recolección del lote.

Haga clic en el botón Comprobar disponibilidad para buscar las existencias de
los productos disponibles.

![Mostrar las cantidades reservadas no disponibles en la pestaña
*Operaciones*.](../../../../../_images/operations-tab.png)

### Crear orden parcial

Si en el formulario de traslado por lote la cantidad hecha del producto es
_menor_ a la cantidad reservada, aparecerá una ventana emergente.

En esta ventana tendrá la opción de crear una orden parcial.

Si hace clic en Crear orden parcial, se creará un nuevo traslado por lote con
los productos restantes de forma automática.

Si desea terminar la recolección _sin_ crear otra recolección por lote, haga
clic en Sin orden parcial.

Haga clic en descartar para cancelar la validación y regresar al formulario de
traslado por lote.

![Ventana emergente para crear orden parcial](../../../../../_images/create-
backorder.png)

## Procesar traslado por lote: aplicación Código de barras

Los traslados por lotes creados también aparecen en la aplicación Código de
barras, a la que se accede haciendo clic en el botón Traslados por lote.

De forma predeterminada, las recolecciones por lotes confirmadas aparecen en
la página Traslados por lotes. Haga clic en el traslado por lotes deseado para
abrir la lista detallada de productos para la recolección.

![Mostrar lista de traslados por completar desde la aplicación *Código de
barras*.](../../../../../_images/barcode-batch-transfers.png)

Siga las instrucciones que aparecen en la parte superior de la página con
fondo negro para el traslado por lotes seleccionado. Comience por escanear el
código de barras del producto para registrar un único producto para la
recolección. Si desea registrar varias cantidades, haga clic en el icono ✏️
(lápiz) e introduzca las cantidades necesarias para la recolección.

Nota

Los productos de la misma orden están etiquetados con el mismo color a la
izquierda. Las recolecciones completadas se destacan en verde.

Example

En un traslado por lotes de 2 `Armarios con puertas`, 3 `Pantallas acústicas`
y 4 `Escritorios para cuatro personas`, las etiquetas `3/3` y `4/4` unidades
indican que las dos últimas recolecciones de productos se completaron con
éxito.

Ya se han recogido `1/2` unidades del `armario con puertas`, y después de
escanear el código de barras del producto para el segundo armario, Odoo
solicita al usuario que `escanee un número de serie` para registrar el número
de serie único para el [seguimiento del
producto](../../product_management/product_tracking/serial_numbers.html#inventory-
serial-numbers-configure).

![Visualización de los productos a recoger en la vista de código de
barras.](../../../../../_images/barcode-products.png)

Una vez seleccionados todos los productos, haga clic en validar para marcar el
traslado por lotes como Hecho.

