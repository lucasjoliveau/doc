# Reabastecer desde otro almacén

Cuando utiliza la función de varios almacenes es común tener un almacén
principal que reabastece varias tiendas y, en este caso, cada tienda se
considera un almacén local. Cuando desea reabastecer un producto en una
tienda, el producto se ordena al almacén central. Konvergo ERP permite al usuario
configurar con facilidad qué almacenes pueden reabastecer a otros.

## Configuración

Para reabastecer desde otro almacén, primero vaya a Inventario ‣ Configuración
‣ Ajustes ‣ Almacén y active las **rutas multietapa**. Luego haga clic en
**guardar** para aplicar el ajuste.

![Habilitar las rutas multietapa en los ajustes de la aplicación
Inventario.](../../../../../_images/virtual-warehouses-settings.png)

Vaya a Inventario ‣ Configuración ‣ Almacenes para ver todos los almacenes
configurados.

Haga clic en **crear** para crear un nuevo almacén. Después, agregue el nombre
del almacén y también su **nombre corto**. Por último, haga clic en
**guardar** para finalizar la creación del almacén.

Regrese a la página de **almacenes** , abra el almacén que se reabastecerá de
un segundo almacén y luego haga clic en **editar**. En la pestaña
**configuración del almacén** vaya al campo **reabastecer de** y seleccione la
casilla junto al nombre del segundo almacén. En caso de que pueda hacer el
reabastecimiento desde más almacenes, seleccione sus respectivas casillas
también. Por último, haga clic en **guardar** para aplicar el ajuste. Ahora
Konvergo ERP sabe qué almacenes pueden reabastecer a este almacén.

![Abastecer un almacén desde otro en la pestaña "configuración del
almacén"](../../../../../_images/resupply-from-second-warehouse.png)

## Establecer una ruta en un producto

Una nueva ruta está disponible en todos los formularios de producto después de
configurar de qué almacenes se realizarán los reabastecimientos. La nueva ruta
aparece como **suministrar producto de [nombre del almacén]** en la pestaña
**inventario** en el formulario de producto. Utilice la ruta **suministrar
producto de [nombre del almacén]** con una regla de reordenamiento o con la
ruta de fabricación sobre pedido para reabastecer las existencias mediante un
movimiento de productos de un almacén a otro.

![Ajuste de ruta que permite el reabastecimiento de un producto desde un
segundo almacén.](../../../../../_images/product-resupply-route-settings.png)

Cuando se activa la regla de reordenamiento de un producto con la ruta
**suministrar producto de [nombre del almacén]** establecida, Konvergo ERP crea dos
recolecciones de forma automática. Una recolección es una _orden de entrega_
del segundo almacén, el cual contiene todos los productos necesarios; la
segunda, es una _recepción_ con los mismos productos desde el almacén
principal. Konvergo ERP lleva el seguimiento completo del movimiento de producto del
segundo almacén al principal.

La regla de reordenamiento del producto es el **documento origen** que aparece
en los registros de recolecciones y traslados creados por Konvergo ERP. La ubicación
entre la orden de entrega y la recepción es una ubicación de tránsito.

![Una regla de reordenamiento crea de forma automática dos recepciones de
existencias entre almacenes.](../../../../../_images/resupply-receipts-from-
reordering-rule.png) ![Una orden de almacén para reabastecer las existencias
de un almacén desde un segundo almacén.](../../../../../_images/second-
warehouse-delivery-order.png) ![Una recepción de existencias que se recibieron
de otro almacén.](../../../../../_images/second-warehouse-stock-receipt.png)

