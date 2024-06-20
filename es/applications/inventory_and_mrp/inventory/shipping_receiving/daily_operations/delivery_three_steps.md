# Procesar entregas en tres pasos

Algunas empresas procesan altas cantidades de entregas todos los días y muchas
de ellas incluyen varios productos o necesitan un embalaje especial. Para que
este proceso sea eficiente, se necesita un paso de embalaje antes de enviar
los productos. Odoo tiene un proceso de tres pasos para entregar los
productos.

En el proceso de entrega de tres pasos predeterminado, los productos que
forman parte de una orden de entrega se recolectan en el almacén según su
estrategia de remoción y se llevan a una zona de empaquetado. Después de que
los artículos se empaquetaron en dentro de los distintos envíos en la zona
correspondiente, se llevan a una ubicación de salida antes de enviarlos. Es
posible modificar estos pasos si no se ajustan a las necesidades del negocio.

## Configuración

Odoo está configurado de forma predeterminada para [recibir y enviar bienes en
un solo paso](receipts_delivery_one_step.html#inventory-receipts-delivery-one-
step), así que deberá modificar los ajustes para utilizar las recepciones en
tres pasos. Primero, asegúrese de que la opción _Rutas multietapa_ se
encuentra habilitada en Inventario ‣ Configuración ‣ Ajustes ‣ Almacén. Tenga
en cuenta que al activar las rutas multietapa también activará las
_ubicaciones de almacenamiento_.

![Activar las rutas multietapa y las ubicaciones de almacenamiento en los
ajustes de la aplicación Inventario.](../../../../../_images/multi-step-
routes.png)

Después, debe configurar el almacén para las entregas en tres pasos. Vaya a la
aplicación Inventario ‣ Configuración ‣ Almacenes y haga clic en el almacén
que desee. Luego, seleccione Empaquetar artículos, enviar productos a
ubicación de salida y enviar (3 pasos) para los envíos salientes.

![Establecer la opción de envío saliente para entregar en tres
pasos.](../../../../../_images/three-step-warehouse-config.png)

Activar la recepción y entrega en tres pasos crea dos nuevas ubicaciones
internas: una _zona de empaquetado_ (WH/Zona de empaquetado) y una de _salida_
(WH/Salida). Para cambiar el nombre de estas ubicaciones, vaya a la aplicación
Inventario ‣ Configuración ‣ Ubicaciones, haga clic en la ubicación que desea
modificar y actualice el nombre.

## Entregar en 3 pasos (recolección, empaquetado y envío)

### Crear una orden de venta

Para crear una nueva cotización, vaya a la aplicación Ventas ‣ Nuevo, se
abrirá un formulario de cotización en blanco. Una vez allí, seleccione un
cliente, agregue un producto almacenable y haga clic en Confirmar.

El botón inteligente Entrega está ubicado en la parte superior derecha del
formulario de cotización. Al hacer clic en él aparecerá la orden de
recolección, la orden de empaquetado y la orden de entrega relacionadas con la
orden de venta.

![Después de confirmar la orden de venta, aparece el botón inteligente de
entrega que muestra sus tres artículos
relacionados.](../../../../../_images/three-step-delivery-so.png)

### Procesar una recolección

Una vez que confirme la orden de venta, se crearán las órdenes de recolección,
empaquetado y entrega. Para ver estos traslados, vaya a Inventario ‣
Operaciones ‣ Traslados.

![La operación de recolección aparece en estado "listo", mientras que las
operaciones de empaquetado y entrega están en espera de  otra
operación.](../../../../../_images/three-step-delivery-transfers.png)

El estado de la recolección será Listo, ya que el producto debe ser
recolectado de las existencias antes de que se pueda empaquetar. El estado de
las órdenes de empaquetado y de entrega será En espera de otra operación, pues
no pueden ocurrir hasta que se complete la recolección. El estado de la orden
de entrega cambiará a Listo cuando el empaquetado esté marcado como Hecho.

También puede encontrar los recibos en la aplicación _Inventario_. En el
tablero de Información general haga clic en el botón inteligente 1 por
procesar en la tarjeta kanban de Recibos.

![Puede ver la orden de recolección en la vista kanban en la aplicación
Inventario.](../../../../../_images/three-step-kanban-pick.png)

Haga clic en recolección a procesar. Si el producto tiene existencias
disponibles, Odoo las reserva de forma automática. Haga clic en Validar para
marcar la recolección como hecha y completar la transferencia a la Zona de
empaquetado, la orden de embalaje estará lista. Ya que los documentos estén
vinculados, los productos que se recolectaron con anterioridad se reservan en
automático en la orden de empaquetado.

![Haga clic en Validar para validar la
recolección.](../../../../../_images/validate-three-step-pick.png)

### Procesar un empaquetado

La orden de empaquetado estará lista para procesar una vez que se complete la
recolección, y puede encontrarla en la aplicación Inventario en la Vista
general del tablero. Haga clic en el botón inteligente 1 Por procesar en la
tarjeta kanban de Empacar.

![Puede ver la orden de empaquetado desde la vista kanban en Inventario.
](../../../../../_images/three-step-kanban-pack.png)

Haga clic en la orden de empaquetado asociada a la orden de ventas, luego haga
clic en Validar para completar el empaquetado.

![Haga clic en validar en la orden de empaquetado para transferir el producto
de la zona de empaquetado a  la ubicación de salida.
](../../../../../_images/validate-three-step-pack.png)

Una vez validada la orden de empaquetada, el producto deja la ubicación de
WH/Zona de empaquetado y se mueve a la ubicación de WH/Ubicación de salida.
Luego, el estado del documento cambiará a Hecho.

### Procesar una entrega

La orden de entrega estará lista para procesar una vez que se complete el
empaquetado, y puede encontrarla en la aplicación Inventario, en la Vista
general del tablero. Haga clic en el botón inteligente 1 Por procesar en la
tarjeta kanban de Ordenes de entrega

![La orden de entrega se puede ver desde la vista kanban de las Ordenes de
entrega. ](../../../../../_images/three-step-kanban-delivery.png)

Haga clic en la orden de entrega asociada con la orden de ventas, y luego haga
clic en Validar para completar el movimiento.

![Haga clic en validar en la orden de entrega para transferir el producto de
la ubicación de salida a la ubicación del cliente.
](../../../../../_images/three-step-delivery-out.png)

Una vez validada la orden de entrega, el producto deja la WH/Ubicación de
salida y se dirige a la ubicación de los Partners/Clientes. Luego, el estado
del documento cambiará a Hecho.

