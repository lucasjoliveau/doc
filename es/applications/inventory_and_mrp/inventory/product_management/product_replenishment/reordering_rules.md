# Reglas de reabastecimiento

Las reglas de reordenamiento se utilizan para mantener los niveles de
existencias previstos sin sobrepasar un límite especificado. Esto se consigue
especificando una cantidad mínima por debajo de la cual no deben descender las
existencias y una cantidad máxima que no deben superar.

Puede configurar las reglas de reordenamiento para cada producto en función de
la ruta utilizada para reabastecerlo. Si un producto utiliza la ruta _Comprar_
, se crea una cotización cuando se activa la regla de reordenamiento. Si un
producto utiliza la ruta _Fabricación_ , se crea una orden de fabricación.
Esto es así independientemente de la ruta de reabastecimiento seleccionada.

Ver también

  * [Tutoriales de Odoo: Reglas de reordenamiento automáticas](https://www.youtube.com/watch?v=XEJZrCjoXaU)

  * [Tutoriales de Odoo: Reglas de reordenamiento manuales](https://www.youtube.com/watch?v=deIREJ1FFj4)

## Configurar productos con reglas de reabastecimiento

Para poder utilizar las reglas de reordenamiento de un producto, primero debe
configurarlo de forma adecuada. Para ello, vaya a Inventario ‣ Productos ‣
Productos, seleccione un producto existente o haga clic en Nuevo para crear
uno.

En el formulario del producto, en la pestaña Información general, asegúrese de
que el Tipo de producto esté configurado como Producto almacenable. Esto es
necesario porque Odoo solo realiza seguimiento de las cantidades en existencia
para productos almacenables y este número se utiliza para activar las reglas
de reordenamiento.

![Establezca el tipo de producto como
almacenable.](../../../../../_images/product-type.png)

A continuación, haga clic en la pestaña Inventario y seleccione una o más
rutas de la sección Rutas. Esto le indica a Odoo que ruta usar para
reabastecer el producto.

![Seleccione una o más rutas en la pestaña
Inventario.](../../../../../_images/select-routes1.png)

Si el producto se reordena utilizando la ruta Comprar, confirme que la casilla
Se puede comprar está activada bajo el nombre del producto. Esto hace que
aparezca la pestaña Comprar, haga clic en ella, especifique al menos un
proveedor y el precio al que venden el producto. De este modo Odoo sabrá a
cuál empresa debe comprar el producto.

![Especifique un proveedor y el precio en la pestaña
Compra.](../../../../../_images/specify-vendor1.png)

Si se reabastece el producto usando la ruta Fabricación, necesita tener al
menos una lista de materiales (LdM) asociada. Esto es necesario porque Odoo
solo crea órdenes de fabricación para productos con una LdM.

Si aún no existe una LdM para el producto, haga clic en el botón inteligente
Lista de materiales ubicado en la parte superior del formulario del producto.
Después, haga clic en Nuevo para configurar una nueva lista de materiales.

![El botón inteligente de lista de materiales en un formulario de
producto.](../../../../../_images/bom-smart-button.png)

## Crear nuevas reglas de reordenamiento

Vaya a Inventario ‣ Configuración ‣ Reglas de reordenamiento para crear una
nueva regla de reordenamiento. Haga clic en Nuevo y complete la nueva línea de
la siguiente manera:

  * Producto: el producto que se reabastece mediante la regla.

  * Ubicación: la ubicación donde se almacena el producto.

  * Cantidad mínima: La cantidad mínima que se puede pronosticar sin que se active la regla. Cuando las existencias pronosticadas son inferiores a esta cantidad, se creará una orden de reabastecimiento para el producto.

  * Cantidad máxima: la cantidad máxima hasta la que se reponen las existencias.

  * Cantidad múltiple: especifique si el producto se debe reabastecer por lotes con una cantidad determinada. Por ejemplo, reabastecer un producto en lotes de 20.

  * UdM: la unidad de medida que se utiliza para reordenar el producto. Este valor puede ser `unidades` o una unidad de medida específica para peso, longitud, etc.

![El formulario para crear una nueva regla de
reabastecimiento.](../../../../../_images/reordering-rule-form.png)

Truco

También es posible crear reglas de reordenamiento desde el formulario de cada
producto. Para ello, vaya a Inventario ‣ Productos ‣ Productos y seleccione
uno. Haga clic en el botón inteligente de Reglas de reordenamiento ‣ Nuevo y
complete la nueva línea con las instrucciones anteriores.

Obtenga más información sobre los siguientes campos de reglas de
reordenamiento para hacer uso avanzado de ellas:

  * Activadores

  * Días de visibilidad

  * Ruta preferida

Nota

Los campos anteriores no están disponibles de forma predeterminada, para
activarlos debe presionar el icono (deslizador) ubicado en la esquina derecha
y después seleccionar la columna deseada en el menú desplegable.

## Activador

Cuando las existencias se encuentren por debajo del mínimo de la regla de
reordenamiento, establezca el campo _Activar_ de la regla de reordenamiento en
_automático_ para crear órdenes de compra o fabricación de forma automática y
reabastecer las existencias.

Como alternativa, al establecer el _activador_ de la regla de reordenamiento
en _manual_ , aparecerá el producto y las existencias previstas en el _tablero
de reabastecimiento_. Allí, el gerente de aprovisionamiento puede revisar los
niveles de existencia, los plazos de espera y las fechas previstas de llegada.

Ver también

[Elegir una estrategia de reabastecimiento](strategies.html)

Truco

Vaya a Inventario ‣ Operaciones ‣ Reabastecimiento para acceder al tablero de
reabastecimiento.

Para habilitar el campo Activar, vaya a Inventario ‣ Configuración ‣ Reglas de
reordenamiento. Después, haga clic en el icono (deslizador) que está ubicado
en la parte derecha de los títulos de las columnas y habilite la opción
Activar desde el menú desplegable de opciones adicionales que aparece.

![Habilitar el campo Activar al seleccionarlo en el menú de opciones
adicionales.](../../../../../_images/enable-trigger.png)

En la columna Activar, seleccione Auto o Manual. Consulte las secciones que se
encuentran a continuación para obtener más información sobre los distintos
tipos de reglas de reordenamiento.

### Auto

Las reglas de reordenamiento automáticas, que se activan al establecer el
campo Activar de la regla de reordenamiento en Auto, generan órdenes de compra
o fabricación cuando:

  1. el planificador se ejecuta y la cantidad _disponible_ se encuentra por debajo del mínimo.

  2. una orden de venta se confirma y reduce la cantidad _prevista_ del producto por debajo del mínimo.

Truco

De forma predeterminada, el planificador está configurado para ejecutarse una
vez al día.

Asegúrese de haber habilitado el [modo de
desarrollador](../../../../general/developer_mode.html#developer-mode) para
activar una regla de reordenamiento de forma manual antes de que se ejecute el
planificador. Vaya a Inventario ‣ Operaciones ‣ Ejecutar planificador, ahí
aparecerá una ventana emergente, haga clic en el botón verde Ejecutar
planificador.

Tenga en cuenta que esto también activará _otras_ acciones programadas.

Example

El producto `Lámpara de oficina` tiene una regla de reordenamiento automática
que está configurada para activarse cuando la cantidad pronosticada se
encuentra por debajo del mínimo de `5.00`. Como el pronóstico actual es
`55.00`, entonces la regla de reordenamiento **no** se activa.

![La regla de reordenamiento automático en la página Reglas de
reordenamiento.](../../../../../_images/auto.png)

Si selecciona la ruta Comprar, entonces se genera una solicitud de cotización.
Para ver y gestionar las solicitudes de cotización, vaya a Compra ‣ Órdenes ‣
Solicitudes de cotización.

Si selecciona la ruta Fabricación, entonces se genera una orden de
fabricación. Para ver y gestionar las órdenes de fabricación, vaya a
Fabricación ‣ Operaciones ‣ Órdenes de fabricación.

Cuando no hay ninguna ruta seleccionada, Odoo elige la Ruta especificada en la
pestaña Inventario del formulario del producto.

### Manual

Las reglas de reordenamiento manuales, que se configuran al establecer el
campo Activar de la regla de reordenamiento en Manual, muestran un producto en
el tablero de reabastecimiento cuando la cantidad pronosticada se encuentra
por debajo del mínimo especificado. Los productos en este tablero se llaman
_necesidades_ , pues son necesarios para cumplir con las próximas órdenes de
venta para las que la cantidad pronosticada no es suficiente.

El tablero de reabastecimiento, al que puede acceder desde Inventario ‣
Operaciones ‣ Reabastecimiento, toma en cuenta los plazos de las órdenes de
venta, los niveles de existencias pronosticadas y los plazos de espera del
proveedor. Muestra las necesidades **solo** cuando es momento de volver a
ordenar los artículos.

Nota

En caso de que la ventana de un día para ordenar productos sea demasiado
corta, vaya a la sección de días de visibilidad para hacer que la necesidad
aparezca en el tablero de reabastecimiento con un número específico de días
por adelantado.

![Hacer clic en el botón Ordenar una vez en el tablero de reabastecimiento
para reabastecer las existencias.](../../../../../_images/manual.png)

## Días de visibilidad

Importante

Asegúrese de comprender los [plazos de
espera](../../shipping_receiving/advanced_operations_shipping/scheduled_dates.html)
antes de continuar con esta sección.

Al asignar reglas de reordenamiento manuales a un producto, los _días de
visibilidad_ hacen que el producto aparezca en el tablero de reabastecimiento
(Inventario ‣ Operaciones ‣ Reabastecimiento) con un cierto número de días por
adelantado.

Example

Un producto tiene una regla de reordenamiento manual configurada para que se
active cuando el nivel de existencias se encuentre por debajo de cuatro
unidades. La cantidad actual disponible es de diez unidades.

La fecha actual es 20 de febrero y la _fecha de entrega_ de la orden de venta
(en la pestaña Otra información) es el 3 de marzo, es decir, doce días a
partir de la fecha actual.

El [plazo de entrega del
proveedor](../../shipping_receiving/advanced_operations_shipping/scheduled_dates.html#inventory-
management-purchase-lt) es de cuatro días y el [plazo de entrega seguro para
la
compra](../../shipping_receiving/advanced_operations_shipping/scheduled_dates.html#inventory-
management-purchase-security-lt) es de un día.

Cuando el campo Días de visibilidad de la regla de reordenamiento está
configurado en cero, el producto aparece en el tablero de reabastecimiento
cinco días antes de la fecha de entrega, que en este caso corresponde al 27 de
febrero.

![Gráfico de representación de la necesidad y cuándo aparece en el tablero de
reabastecimiento: 27 de febrero.](../../../../../_images/need-dates.png)

Para visualizar el producto en el tablero de reabastecimiento en la fecha
actual, 20 de febrero, establezca los Días de visibilidad en `7.00`.

Para determinar el número de días de visibilidad necesarios para visualizar un
producto en el tablero de reabastecimiento deberá restar la _fecha de hoy_ de
la _fecha en la que aparece la necesidad_ en el tablero correspondiente.

\\[Días~de~visibilidad = Fecha~en~que~aparece~la~necesidad - Fecha~actual\\]

Example

Continuando con el ejemplo anterior, la fecha de hoy es el 20 de febrero y la
necesidad del producto aparece el 27 de febrero.

(27 de febrero - 20 de febrero = 7 días)

Configurar los días de visibilidad de forma incorrecta en menos de siete días
en este caso ocasiona que la necesidad **no** aparezca en el tablero de
reabastecimiento.

![Visualización del tablero de reabastecimiento con los días de visibilidad
correctos e incorrectos en su
configuración.](../../../../../_images/visibility-days.png)

## Ruta preferida

Odoo permite seleccionar varias rutas en la pestaña Inventario en cada
formulario de producto. Por ejemplo, es posible seleccionar tanto Comprar como
Fabricar, para permitir la funcionalidad de ambas rutas.

Odoo también permite que los usuarios establezcan una ruta preferida como
regla de reordenamiento de un producto. Esta es la ruta predeterminada de la
regla en caso de que hayan varias seleccionadas. Para seleccionar una ruta
preferida, vaya a Inventario ‣ Configuración ‣ Reglas de reordenamiento o a
Inventario ‣ Operaciones ‣ Reabastecimiento.

Haga clic dentro de la columna en la fila de una regla de reordenamiento,
aparecerá un menú desplegable con todas las rutas disponibles para esa regla.
Seleccione una para establecerla como ruta preferida.

![Establecer una ruta preferida desde el menú
desplegable](../../../../../_images/select-preferred-route.png)

Importante

Si se activan varias rutas para un producto pero no se establece ninguna ruta
preferida para su regla de reordenamiento, el producto se reordena utilizando
la ruta seleccionada que aparece en primer lugar en la pestaña Inventario del
formulario del producto.

  *[LdM]: Lista de materiales

