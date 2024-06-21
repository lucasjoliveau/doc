# Ubicaciones

Una _ubicación_ es un espacio específico dentro de un almacén. Puede ser un
estante, una sala, un pasillo, etc. Hay tres tipos de ubicaciones en Konvergo ERP:

  * Las _ubicaciones físicas_ son espacios dentro de un almacén que pertenece a la empresa del usuario. Estas pueden ser las áreas donde los artículos se almacenan como un pasillo o estante, o las áreas donde se realizan operaciones, como las zonas de carga y descarga.

  * Las _ubicaciones de contactos_ son iguales a las ubicaciones físicas, pero están dentro del almacén de un cliente o proveedor.

  * Las _ubicaciones virtuales_ son ubicaciones que no existen de forma física, pero allí se pueden colocar los artículos que no están en el inventario. Estos pueden ser artículos que aún no son parte de las existencias, como productos que están en camino al almacén o artículos que ya no están en el inventario debido a pérdidas u otros factores.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Debe habilitar los ajustes de <b>Ubicaciones de almacenamiento</b> para poder usarlas. Vaya a Inventario ‣ Configuración ‣ Ajustes, diríjase al encabezado <b>Almacén</b> y active la casilla <b>Ubicaciones de almacenamiento</b>.</p>
</div>

## Crear una nueva ubicación dentro de un almacén

En la aplicación **Inventario** , seleccione Configuración ‣ Ubicaciones ‣
Nuevo. Complete el formulario para la nueva ubicación con los siguientes
datos:

  * **Nombre de la ubicación** : el nombre que se utilizará para hacer referencia a la ubicación.

  * **Ubicación principal** : la ubicación o el almacén dentro del que está la nueva ubicación.

  * **Tipo de ubicación** : elija la categoría a la que pertenece la ubicación.

  * **Empresa** : la empresa que es propietaria del almacén donde se encuentra la ubicación.

  * **¿Es una ubicación de desecho?** : marque esta casilla si desea permitir que las mercancías que son desechos o están dañadas se almacenen en esta ubicación.

  * **¿Es una ubicación de devolución?** : marque esta casilla si desea permitir que devuelvan los productos a esta ubicación.

  * **Código de barras** : el número de código de barras que le asignó a la ubicación.

  * **Estrategia de remoción** : la [estrategia](../advanced_operations_warehouse/removal#inventory-routes-strategies-removal) que indica cómo deben tomarse los artículos del inventario.

![El formulario para crear una nueva ubicación.](../../../../../_images/new-
location-form.png)

## Crear jerarquías de ubicación

El ajuste que recibe el nombre de _Ubicación principal_ en el formulario de la
nueva ubicación permite que exista una ubicación dentro de un almacén u otra
ubicación. Cada ubicación puede servir como una ubicación principal y cada una
de ellas puede tener varias ubicaciones dentro, lo que permite la creación de
una estructura jerárquica casi infinita.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>La jerarquía de ubicaciones permite que un estante se encuentre dentro de un pasillo, que se encuentra dentro de una sala, que se encuentra dentro del almacén general.</p>
</div>

Para crear la jerarquía de ubicación descrita en el ejemplo anterior,
establezca el almacén como la ubicación principal de la sala, la sala como la
ubicación principal del pasillo y el pasillo como la ubicación principal del
estante. Esto se puede adaptar a una jerarquía de cualquier extensión.

