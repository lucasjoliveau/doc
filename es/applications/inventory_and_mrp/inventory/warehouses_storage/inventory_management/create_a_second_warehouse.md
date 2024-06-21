# Crear un segundo almacén

Un _almacén_ es un edificio físico o espacio donde se almacenan artículos. En
Konvergo ERP puede configurar varios almacenes y trasladar artículos almacenados entre
ellos.

De manera predeterminada, la plataforma de Konvergo ERP cuenta con un almacén ya
configurado con la dirección establecida que corresponde a la empresa. Para
crear un segundo almacén, seleccione Configuración ‣ Almacenes, luego haga
clic en **Crear** y configure el formulario como se indica a continuación:

  * **Almacén** : el nombre completo del almacén.

  * **Nombre corto** : el código abreviado con el que se hace referencia al almacén; el nombre corto para el almacén predeterminado en Konvergo ERP es **WH**.

  * **Empresa** : la empresa propietaria del almacén. Puede ser la empresa que es propietaria de la base de datos de Konvergo ERP o la de un cliente o proveedor.

  * **Dirección** : la dirección en la que se encuentra el almacén.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Las opciones que se encuentran a continuación solo aparecerán si la casilla <b>Rutas multietapa</b> está habilitada en Configuración ‣ Ajustes debajo de la opción <b>Almacenes</b>. Para obtener más información acerca de las rutas y como funcionan en Konvergo ERP, consulte <a href="use_routes#use-routes"><span class="std std-ref">Utilizar rutas y reglas pull y push</span></a>.</p>
</div>

  * **Envíos entrantes/salientes** : seleccione las rutas que los envíos entrantes o salientes deben seguir.

  * **Reabastecer a subcontratistas** : permita que los subcontratistas puedan reabastecerse desde este almacén.

  * **Fabricación para reabastecimiento** : permita que los artículos se fabriquen en este almacén.

  * **Fabricación** : seleccione la ruta que se debe seguir cuando se fabriquen bienes dentro del almacén.

  * **Comprar para reabastecer** : marque la casilla para autorizar la compra de productos que se deben entregar en el almacén.

  * **Formato de reabastecimiento** : seleccione los almacenes que pueden utilizarse para reabastecer el almacén que se está creando.

![Un formulario completado para crear un nuevo
almacén.](../../../../../_images/new-warehouse-configuration.png)
<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Al crear un segundo almacén activará de manera automática la función <em>ubicaciones de almacenamiento</em>, esta permite rastrear la ubicación de productos dentro de un almacén. Para activarla, vaya a Configuración ‣ Ajustes y haga clic en la casilla ubicada debajo de la opción <b>Almacén</b>.</p>
</div>

Después de que haya completado el formulario, haga clic en **guardar** y
creará el nuevo almacén.

## Agregar inventario a un nuevo almacén

Si crea un nuevo almacén que tiene un inventario existente asignado, debe
agregar los conteos de inventario a Konvergo ERP para que el inventario que aparece en
la base de datos refleje lo que hay en el almacén físico. Para agregar
inventario a un nuevo almacén, vaya a Inventario ‣ Operaciones ‣ Ajustes de
inventario, y luego haga clic en **crear**. Complete el formulario de ajuste
de inventario con la siguiente información:

  * **Referencia de inventario** : el nombre o código con el que se puede hacer referencia al ajuste de inventario.

  * **Ubicaciones** : las ubicaciones donde se almacena el inventario. Incluye el nuevo almacén y cualquier ubicación interna en la que se agregará el inventario.

  * **Productos** : incluya todos los productos que serán agregados en el inventario o déjelos en blanco para seleccionar cualquier producto en el siguiente paso.

  * **Incluir productos agotados** : esto incluirá los productos con una cantidad igual a cero. No afecta a los ajustes de inventario de los nuevos almacenes, ya que no tienen inventario existente.

  * **Fecha contable** : fecha utilizada por los equipos contables para la teneduría de libros relacionados con el inventario.

  * **Empresa** : es la empresa propietaria del inventario; puede establecerse como la empresa del usuario o como un cliente o proveedor.

  * **Cantidades contadas** : elija si las cantidades contadas para los productos que se agregan deben ser existencias predeterminadas disponibles o cero. No afecta a los ajustes de inventario para los nuevos almacenes, ya que no tienen inventario existente.

![Un formulario completado para un ajuste de
inventario.](../../../../../_images/inventory-adjustment-configuration.png)

Una vez que el formulario esté correctamente configurado, haga clic en
**Comenzar inventario** para pasar a la siguiente página, donde podrá añadir
productos al ajuste de inventario. Haga clic en **Crear** para agregar un
nuevo producto y, luego, complete la línea del producto como se indica a
continuación:

  * **Producto** : el producto que se agregará al inventario.

  * **Ubicación** : la ubicación en la que se encuentra almacenado actualmente el producto dentro del almacén. Puede establecerse como el almacén general o una ubicación dentro del almacén.

  * **Número de lote/serie** : el lote al que pertenece el producto o el número de serie que utiliza para identificarlo.

  * **Disponible** : la cantidad total del producto almacenado en la ubicación para la que se está ajustando el inventario. Debe ser cero para una nueva ubicación o almacén.

  * **Contado** : la cantidad de producto que se está agregando al inventario.

  * **Diferencia** : la diferencia entre los valores _Disponible y *Contado_. Se actualizará de forma automática para reflejar el valor introducido en la columna **Contado**.

  * **UdM** : la unidad de medida utilizada para contar el producto.

![Incluye una línea por cada producto que se agrega al
inventario.](../../../../../_images/product-line-configuration.png)

Después de agregar todos los productos ya almacenados en el nuevo almacén,
haga clic en **Validar inventario** para completar el ajuste del inventario.
Los valores de la columna **Disponible** se actualizarán para reflejar los de
la columna **Contados** y los productos agregados aparecerán en el inventario
del nuevo almacén.

