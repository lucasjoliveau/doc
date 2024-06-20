# Paquetes

Un _paquete_ es un contenedor físico que incluye uno o más productos. Los
paquetes también son útiles para almacenar artículos en grandes cantidades.

Por lo general, los paquetes se utilizan para los siguientes fines:

  1. Agrupar productos para moverlos a granel.

  2. Shipping to customers: configure los tipos de paquetes para que coincidan con los requisitos de tamaño y peso de los transportistas, agilizar el proceso de embalaje y garantizar el cumplimiento de sus especificaciones de envío.

  3. Almacenar productos a granel.

El campo _Uso del paquete_ en el formulario correspondiente en Odoo solo será
visible luego de habilitar las funciones _Traslados por lote_ y _Paquetes_
(Inventario ‣ Configuración ‣ Ajustes).

El campo _Uso del paquete_ en los formularios pertinentes tiene la opción
_Caja desechable_ establecida de forma predeterminada. Seleccione _Caja
reutilizable_ **solo** al configurar paquetes destinados para preparar varias
órdenes.

La función opcional _Tipo de paquete_ se usa para [calcular el costo de
envío](../../shipping_receiving/setup_configuration/delivery_method.html),
según el peso real del envío. Cree tipos de paquetes para incluir el peso del
paquete (por ejemplo, de cajas, palés y otros contenedores de envío) en los
cálculos de costos de envío.

Nota

Por lo general los paquetes se usan en [la ruta de entrega en tres
pasos](../../shipping_receiving/daily_operations/delivery_three_steps.html),
pero también se pueden usar en cualquier flujo de trabajo que involucre
productos almacenables.

## Configuración

Para utilizar paquetes, primero vaya a Inventario ‣ Configuración ‣ Ajustes.
En la sección Operaciones active la función Paquetes y luego haga clic en
Guardar.

![Activar la función *Paquetes* en Inventario > Configuración >
Ajustes.](../../../../../_images/enable-pack.png)

## Empacar artículos

Puede agregar productos a los paquetes en cualquier traslado de las siguientes
formas:

  1. Al hacer clic en el icono Operaciones detalladas en la línea del producto.

  2. Con el botón Incluir en el paquete para colocar todo lo de un traslado en un paquete.

### Operaciones detalladas

En cualquier traslado de almacén (por ejemplo, una recepción u orden de
entrega) puede agregar un producto a un paquete si hace clic en el icono ⦙≣
(lista con viñetas) en la pestaña Operaciones.

![El icono "Operaciones detalladas" aparece en la línea del
producto.](../../../../../_images/detailed-operations1.png)

Esta acción abrirá la ventana emergente Operaciones detalladas del producto.

Para colocar el producto en un paquete, haga clic en Agregar una línea y
asigne el producto a un Paquete de destino. Seleccione un paquete existente o
cree uno nuevo, para esto deberá escribir el nombre del nuevo paquete y luego
seleccionar Crear….

![Asignar un paquete en el campo "Paquete de
destino".](../../../../../_images/destination-package.png)

Doce unidades del producto `Pantallas acústicas` se colocan en `PACK0000001`.

Después, especifique la cantidad de artículos que se colocarán en el paquete
en la columna Hecho. Repita los pasos anteriores para colocar el producto en
distintos paquetes. Haga clic en Confirmar para cerrar la ventana después de
que haya terminado.

Ver también

[Enviar una orden en varios
paquetes](../../shipping_receiving/advanced_operations_shipping/multipack.html)

### Incluir en el paquete

De forma alternativa, haga clic en el botón Incluir en el paquete en
**cualquier** traslado de almacén para crear un nuevo paquete y colocar todos
los artículos en el traslado en ese paquete recién creado.

Importante

El botón Incluir en el paquete aparece en las recepciones, órdenes de entrega
y otros formularios de traslado cuando la función _Paquetes_ está habilitada
en la aplicación Inventario ‣ Configuración ‣ Ajustes.

![Imagen en donde se puede visualizar cómo se hace clic en el botón "Incluir
en el paquete".](../../../../../_images/put-in-pack.png)

En el traslado por lotes `BATCH/00003` se hizo clic en el botón Incluir en el
paquete para crear el nuevo paquete `PACK0000002` y asignar todos los
artículos a este en el campo Paquete de destino.

## Tipo de paquete

Cree tipos de paquetes desde la aplicación Inventario ‣ Configuración ‣ Tipos
de paquetes, allí también podrá establecer dimensiones personalizadas y
límites de peso. Esta función se utiliza en su mayoría para calcular el peso
de los paquetes para los costos de envío.

Ver también

  * [Transportistas](../../shipping_receiving/setup_configuration/third_party_shipper.html)

  * [Métodos de envío](../../shipping_receiving/setup_configuration/delivery_method.html)

En la lista de Tipos de paquetes, abrirá un formulario vacío de tipo de
paquete al hacer clic en Nuevo. Los campos del formulario son los siguientes:

  * Tipo de paquete (obligatorio): defina el nombre del tipo de paquete.

  * Tamaño: defina las dimensiones del paquete en milímetros (mm). Los campos, de izquierda a derecha, definen la longitud, el ancho y la altura.

  * Peso: el peso de un paquete vacío (por ejemplo, una caja vacía, un palé).

Nota

Odoo calcula el peso del paquete sumando el peso del paquete vacío más el peso
de los artículos. Este último está disponible en el formulario de cada
producto en el campo Peso de la pestaña Inventario.

  * Peso máximo: el peso máximo de envío permitido en el paquete.

  * Código de barras: defina un código de barras para identificar el tipo de paquete al escanearlo.

  * Empresa: especifique una empresa para que el tipo de paquete esté disponible **solo** en la empresa seleccionada. Deje el campo vacío si está disponible en todas las empresas.

  * Transportista: especifique al transportista correspondiente para este tipo de paquete.

  * Código de transportista: defina un código vinculado al tipo de paquete.

![Tipo de paquete para una caja de 25 kilos de
FedEx.](../../../../../_images/package-type.png)

## Paquetes para varias órdenes

Para utilizar los _paquetes para varias órdenes_ , primero vaya a la
aplicación Inventario ‣ Configuración ‣ Ajustes y active la función Traslados
por lote, está ubicada en la sección Operaciones. Una vez que haya hecho esto,
el campo _Uso del paquete_ aparecerá en el formulario.

![Activar la función *Traslados por lote* en Inventario > Configuración >
Ajustes.](../../../../../_images/enable-batch.png)

Vaya a Inventario ‣ Productos ‣ Paquetes y haga clic en Nuevo para agregar
nuevos paquetes o seleccione uno existente. Esta acción abrirá el formulario
del paquete con los siguientes campos:

  * Referencia del paquete (obligatorio): el nombre del paquete.

  * Tipo de paquete: se utiliza para configurar las cajas de envío para enviar al cliente.

Nota

El tipo de paquete no es necesario para configurar paquetes de recolección
para varias órdenes.

  * Peso de envío: se utiliza para agregar el peso del paquete después de pesarlo.

  * Empresa: especifique una empresa para que el paquete esté disponible **solo** en la empresa seleccionada. Deje el campo vacío si está disponible en todas las empresas.

  * Ubicación: la ubicación actual del paquete.

  * Fecha de empaquetado: la fecha en que se creó el paquete.

  * Uso del paquete: seleccione Caja reutilizable si se trata de paquetes que se usarán para mover productos dentro del almacén o Caja desechable en caso de que los paquetes se usen para enviar productos a los clientes.

![Visualización del formulario de paquete para crear un paquete para varias
órdenes.](../../../../../_images/package.png)

Ver también

[Usar paquetes para preparar varias
órdenes](../../warehouses_storage/advanced_operations_warehouse/cluster_picking.html)

