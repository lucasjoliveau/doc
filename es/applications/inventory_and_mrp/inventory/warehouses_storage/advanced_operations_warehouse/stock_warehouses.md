# Vender las existencias de varios almacenes mediante ubicaciones virtuales

Mientras que mantener existencias y vender inventario desde un almacén puede
ser útil para empresas más pequeñas, es posible que aquellas que son más
grandes necesiten mantener existencias en, o vender desde, varios almacenes en
diferentes ubicaciones.

A veces los productos incluidos en una sola orden de venta pueden utilizar
existencias de dos (o más) almacenes. En Odoo es posible tomar productos de
varios almacenes para cumplir con las demandas de ventas gracias a las
_ubicaciones virtuales_.

Importante

Este documento describe el uso de un almacén virtual para cumplir con órdenes
de varios almacenes, pero tiene algunas limitaciones. Tome en cuenta lo
siguiente antes de continuar:

  1. Al establecer un almacén virtual en el campo Almacén de una orden de venta, la dirección del almacén virtual aparecerá en los formularios de recolección, embalaje y entrega, **no** la dirección del almacén real.

  2. Cada ubicación tiene un `warehouse_id` (campo oculto). Esto indica que las existencias en el almacén virtual **no** serán la suma de aquellas en los almacenes reales, sino la suma de las existencias en las ubicaciones cuyo ID de almacén es el del almacén virtual.

Peligro

Hay una limitación potencial para quienes hacen uso de las [entregas en
dos](../../shipping_receiving/daily_operations/receipts_delivery_two_steps.html)
o [en tres
pasos](../../shipping_receiving/daily_operations/delivery_three_steps.html):

  1. La zona de salida o de empaquetado en varios formularios aparece de forma incorrecta, pues indica la dirección del almacén virtual.

  2. No hay ninguna solución alternativa para las entregas en dos o tres pasos.

  3. Continúe con esto **solo** en caso de que en el flujo de trabajo de su empresa tenga sentido establecer la dirección de un almacén virtual como la zona de salida o empaquetado.

Nota

Para crear ubicaciones virtuales en almacenes y poder continuar con los
siguientes pasos **debe** activar las funciones Ubicaciones de almacenamiento
y Rutas multietapa.

Vaya a Inventario ‣ Configuración ‣ Ajustes, diríjase a la sección Almacén,
habilite las opciones Ubicaciones de almacén y Rutas multietapa y haga clic en
Guardar.

## Crear una ubicación principal virtual

Cree un nuevo almacén antes de crear cualquier ubicación virtual para las
existencias. Este nuevo almacén funcionará como un almacén _virtual_ y será la
ubicación _principal_ de otros almacenes físicos.

Why a "virtual" warehouse?

Los almacenes virtuales son ideales para las empresas con varios almacenes
físicos. Esto se debe a que es posible que un almacén se quede sin existencias
de un producto en específico, pero que otro aún tenga unidades disponibles. En
este caso, las existencias de estos dos (o más) almacenes podrían utilizarse
para realizar una única orden de venta.

Los almacenes «virtuales» funcionan como un agrupador único de todo el
inventario guardado en los almacenes físicos de una empresa. Se utilizan, por
motivos de trazabilidad, para crear jerarquías en las ubicaciones de Odoo.

Vaya a Inventario ‣ Configuración ‣ Almacenes para crear un nuevo almacén y
haga clic en Nuevo. Desde aquí puede cambiar el nombre y el nombre corto del
almacén, también puede modificar otros de sus detalles en la pestaña
Configuración del almacén.

Por último, haga clic en Guardar para terminar de crear un almacén _regular_.
Siga los pasos que se encuentran abajo para terminar de configurar el almacén
principal virtual.

![Formulario de nuevo almacén.](../../../../../_images/stock-warehouses-
create-warehouse.png)

Ver también

  * [Configuraciones del almacén](../inventory_management/warehouses_locations.html)

  * [Envíos entrantes y salientes](../../shipping_receiving/daily_operations/receipts_delivery_one_step.html#inventory-receipts-delivery-one-step-wh)

  * [Reabastecer desde otro almacén](../inventory_management/resupply_warehouses.html)

## Crear almacenes secundarios

Cree al menos dos almacenes _secundarios_ para vincularlos al almacén virtual.

Importante

Para poder tomar existencias de varios almacenes y cumplir con una orden de
venta, debe haber al menos **dos** almacenes que actúen como ubicaciones
secundarias del almacén principal virtual.

Vaya a: Inventario ‣ Configuración ‣ Almacenes, haga clic en Nuevo y siga las
instrucciones anteriores para configurar las ubicaciones físicas de
existencias.

Example

**Almacén principal**

Almacén: `Almacén virtual`

Ubicación: `VWH/Stock`.

**Almacenes secundarios**

Almacenes: `Almacén A` y `Almacén B`

Ubicaciones: `WHA` y `WHB`.

![Gráfico de las ubicaciones secundarias 'WHA' y 'WHB' vinculadas a la
ubicación principal.](../../../../../_images/parent-location.png)

Importante

La ubicación virtual de existencias se cambiará a «Vista» después, pero el
tipo de ubicación **debe** ser Ubicación interna en este punto para vincular
los almacenes secundarios en la siguiente sección.

## Vincular almacenes secundarios a las existencias virtuales

Para establecer almacenes físicos como ubicaciones secundarias de la ubicación
virtual configurada en el paso anterior, vaya a Inventario ‣ Configuración ‣
Ubicaciones.

Elimine los filtros de la barra de búsqueda, haga clic en la ubicación del
almacén físico que creó para que sea una ubicación secundaria (por ejemplo,
`WHA`) y después haga clic en Editar.

Cambie el campo Ubicación principal de ubicaciones físicas a la **ubicación de
existencias** del almacén virtual (por ejemplo, `VWH/Stock`) desde el menú
desplegable. Después, haga clic en Guardar.

Importante

Para seleccionar la ubicación del almacén virtual en el menú desplegable
Ubicación principal, la ubicación del almacén principal (por ejemplo,
`VWH/Stock`) **debe** tener su tipo de ubicación configurado en Ubicación
interna.

![Establecer la *ubicación principal* del almacén secundario en el almacén
virtual.](../../../../../_images/configure-physical-wh.png)

Repita los pasos anteriores para configurar dos o más almacenes secundarios.

Una vez que haya terminado, el almacén virtual principal (por ejemplo,
`VWH/Stock`) completa las órdenes con las existencias de los almacenes
secundarios (por ejemplo, `WHA` y `WHB`) en caso de que no haya suficientes en
alguna otra ubicación.

## Establecer la ubicación virtual de existencias como «Vista»

Establezca el Tipo de ubicación de la ubicación virtual de existencias en
Vista, ya que es una ubicación inexistente que se utiliza para agrupar varios
almacenes físicos.

Vaya a Inventario ‣ Configuración ‣ Ubicaciones.

En la lista de Ubicaciones, haga clic en la correspondiente al almacén virtual
de las existencias que ya había creado (por ejemplo, `VWH/Stock`).

En el formulario de ubicación, en la sección Información adicional, establezca
el Tipo de ubicación a Vista y guarde los cambios.

![Tipos de ubicación de almacén en la pantalla de creación de
ubicaciones.](../../../../../_images/set-location-type-view.png)

Truco

Para visualizar la cantidad total en **todos** los almacenes secundarios
vinculadas, vaya al formulario del producto y haga clic en el botón
inteligente Disponible.

![Mostrar las existencias en todos los almacenes
vinculados.](../../../../../_images/on-hand.png)

## Ejemplos: vender productos de un almacén virtual

Para vender productos desde varios almacenes a través de una ubicación virtual
principal, la base de datos debe tener al menos **dos** almacenes configurados
con al menos **un** producto, y debe haber cantidad disponible en cada
almacén, respectivamente.

Example

El producto `Soldado de juguete` está disponible en las ubicaciones con las
siguientes cantidades:

  * `WHA/Stock`: 1

  * `WHB/Stock`: 2

  * Los almacenes `WHA` y `WHB` son almacenes secundarios del almacén virtual `VWH`.

Cree una cotización para el producto desde la aplicación Ventas y haga clic en
Nuevo. En la cotización agregue un cliente y luego haga clic en Agregar un
producto para agregar los dos productos almacenados en ambos almacenes.

Luego, haga clic en la pestaña Información adicional en el formulario de la
orden de venta. En la sección Entrega, cambie el valor del campo Almacén por
el almacén virtual que ya había creado y confirme la orden de venta.

![Establecer el almacén virtual en el campo *Almacén* en la pestaña
*Información adicional* de la orden de venta.](../../../../../_images/set-
virtual-wh.png)

Haga clic en el botón inteligente Entrega y en el formulario de entrega del
almacén verifique que el valor de la Ubicación de origen coincida con el valor
del campo Almacén del formulario de la orden de venta. Ambos deben incluir la
ubicación del almacén virtual.

Por último, en el formulario de entrega del almacén, en la pestaña Operaciones
detalladas, verifique que las ubicaciones de la columna Desde para cada
producto coincidan con las ubicaciones secundarias vinculadas a la ubicación
principal virtual.

![Orden de entrega con ubicaciones de origen y secundarias
coincidentes.](../../../../../_images/delivery-order1.png)

Importante

> La ubicación de origen en el formulario de entrega del almacén y el Almacén
> en la pestaña Información adicional en el formulario de la orden de venta
> **deben** coincidir para que los productos de la orden de venta se extraigan
> de distintos almacenes.

  * Si el almacén virtual no está en el campo Ubicación de origen en el formulario de entrega de almacén, vuelva a intentar reservar el producto mediante alguna de las siguientes opciones:

    * Ejecute el planificador: active el [modo de desarrollador](../../../../general/developer_mode.html#developer-mode) y vaya a Inventario ‣ Operaciones ‣ Ejecutar planificador.

    * Haga clic en Comprobar disponibilidad en la orden de entrega.

  * Si el almacén virtual **no** está asignado al campo Almacén en la orden de venta, entonces deberá cancelarla y crear una nueva con el almacén virtual establecido en el campo Almacén.

  * Si el campo Almacén no está disponible en el formulario de la orden de venta, es posible que no haya configurado de forma correcta los distintos almacenes secundarios. Consulte la sección anterior para asegurarse de estar haciendo uso de los ajustes adecuados.

Truco

Para utilizar una ubicación _principal_ virtual como almacén predeterminado
para las órdenes de venta, cada vendedor debe tener asignado el almacén
virtual desde el menú desplegable junto a Almacén predeterminado en su
formulario de empleado.

![Ubicación de almacén predeterminada en el formulario del
empleado.](../../../../../_images/stock-warehouses-employee-form.png)

