# Reglas de almacenamiento

El almacenamiento es el proceso de enrutamiento de productos a los lugares de
almacenamiento apropiados cuando llega el envío.

Odoo tiene la capacidad de realizar ese proceso a través de _reglas de
almacenamiento_ que determinan de qué forma se moverán los productos a través
de las ubicaciones estipuladas en el almacén.

Cuando llega un envío, se generan operaciones según las reglas de
almacenamiento para mover los productos con eficacia a las ubicaciones
determinadas y asegurar que se puedan tomar con facilidad para elaborar las
próximas órdenes de envío.

En los almacenes que procesan tipos específicos de productos, las reglas de
almacenamiento también pueden evitar que las sustancias volátiles se almacenen
muy cerca y que, en su lugar, estas se guarden en otros lugares designados por
el gerente del almacén.

Ver también

[Tutoriales de Odoo: Reglas de
almacenamiento](https://www.youtube.com/watch?v=nCQMf6sj_w8)

## Configuración

Para utilizar las reglas de almacenamiento, vaya a Inventario ‣ Configuración
‣ Ajustes y active la función Rutas multietapa ubicada en la sección Almacén.
La función Ubicaciones de almacenamiento también se habilita en automático.

Por último, haga clic en Guardar.

![Activar las rutas multietapa en los ajustes de la aplicación
Inventario.](../../../../../_images/activate-multi-step-routes.png)

### Definir reglas de almacenamiento

Para gestionar dónde se enrutan ciertos productos para su almacenamiento, vaya
a la aplicación Inventario ‣ Configuración ‣ Reglas de almacenamiento. Utilice
el botón Crear para configurar una nueva regla de almacenamiento en un
producto o categoría de producto.

Importante

Es posible definir las reglas de almacenamiento por producto, categoría de
producto o tipo de paquete (aunque para esto último, la función _Paquetes_
debe estar habilitada en Inventario ‣ Configuración ‣ Ajustes).

En la misma línea, la ubicación de Cuando el producto llega a es donde se
activa la regla de almacenamiento para crear una operación y mover el producto
a la ubicación Almacenar en.

Para que esto funcione, la ubicación Almacenar en debe ser una _sububicación_
de la primera (por ejemplo, `WH/Stock/Frutas` es una ubicación específica y
nombrada dentro de `WH/Stock` para facilitar la búsqueda de los productos que
se almacenan aquí).

Example

En una ubicación de almacén, **WH/Stock** , se encuentran las siguientes
sububicaciones:

  * WH/Stock/Frutas

  * WH/Stock/Vegetales

Asegúrese de que todas las manzanas se almacenan en la sección de frutas.
Complete el campo Almacenar en con la ubicación `WH/Stock/Frutas` cuando el
producto `Manzana` llegue a `WH/Stock`.

Repita este paso para todos los productos y haga clic en Guardar.

![Crear reglas de almacenamiento para manzanas y
zanahorias.](../../../../../_images/create-putaway-rules.png)

### Prioridad de las reglas de almacenamiento

Odoo selecciona una regla de almacenamiento según la siguiente lista de
prioridades (de más alta a más baja) hasta encontrar una coincidencia:

  1. Tipo de paquete y producto

  2. Tipo de paquete y categoría de producto

  3. Tipo de paquete

  4. Producto

  5. Categoría de producto

Example

> El producto `Lata de limonada` tiene configuradas las siguientes reglas de
> almacenamiento:
>
>   1. Al recibir un `pallet` (Tipo de paquete) de `Latas de limonada`, este
> se redirige a `WH/Stock/Pallets/PAL1`.
>
>   2. La categoría de producto de `Lata de limonada` es `Todos/bebidas` y
> cuando recibe una `caja` de cualquier artículo en esta categoría de producto
> estos se redirigen a `WH/Stock/Estante 1`.
>
>   3. Cualquier producto en un `pallet` se redirige a `WH/Stock/Pallets`.
>
>   4. El producto `Lata de limonada` se redirige a `WH/Stock/Estante 2`.
>
>   5. Los artículos en la categoría de productos `Todos/bebidas` se redirigen
> a `WH/Stock/Refrigerador pequeño`.
>
>

![Algunos ejemplos de reglas de
almacenamiento.](../../../../../_images/putaway-example.png)

## Categorías de almacenamiento

Las _categorías de almacenamiento_ son atributos adicionales de las
ubicaciones que permiten que el usuario defina la cantidad de productos que se
pueden almacenar en la ubicación y cómo la ubicación selecciona las reglas de
almacenamiento.

### Configuración

Para habilitar las categorías de almacenamiento, vaya a Inventario ‣
Configuración ‣ Ajustes y active la función Categorías de almacenamiento en la
sección Almacén. Después, haga clic en Guardar.

Importante

La función Ubicaciones de almacenamiento **debe** estar habilitada para
activar las categorías de almacenamiento.

### Definir categorías de almacenamiento

Para crear una categoría de almacenamiento, vaya a Inventario ‣ Configuración
‣ Categorías de almacenamiento y haga clic en Nuevo.

Una vez en el formulario de categoría de almacenamiento, escriba un nombre en
el campo Categoría de almacenamiento.

Hay opciones disponibles para limitar la capacidad por peso, producto o tipo
de paquete. El campo Permitir nuevo producto define cuándo la ubicación está
disponible para almacenar un producto:

  * Si la ubicación está vacía: se puede agregar un producto solo si la ubicación está vacía.

  * Si los productos son los mismos: se puede agregar un producto solo si ya hay un producto igual ahí.

  * Permitir productos mezclados: se pueden almacenar varios productos distintos al mismo tiempo en esta ubicación.

Example

Cree reglas de almacenamiento para los artículos que se almacenan en palés y
asegure la revisión de capacidad de almacenamiento en tiempo real al crear la
categoría `Palés de alta frecuencia`.

Proporciónele un nombre a la categoría de almacenamiento y seleccione Si los
productos son los mismos en el campo Permitir nuevo producto.

A continuación, defina la capacidad del paquete en la pestaña Capacidad por
paquete. Especifique el número de paquetes para el tipo de paquete
correspondiente y establezca un máximo de `2.00` `palés` para una ubicación
específica.

![Crear una categoría de almacenamiento en la
página.](../../../../../_images/storage-category.png)

Una vez que guarde los ajustes de categoría de almacenamiento, puede
vincularla a una ubicación.

Para ello, vaya a Inventario ‣ Configuración ‣ Ubicaciones y seleccione una
ubicación. Haga clic en Editar y seleccione la categoría creada en el campo
Categoría de almacenamiento.

Example

Asigne la categoría de almacenamiento `Palés de alta frecuencia` a la
sububicación `WH/Stock/Pallets/PAL 1`.

![Cuando se crea una categoría de almacenamiento, se puede vincular a una
ubicación de almacén.](../../../../../_images/location-storage-category.png)

### Usar categorías de almacenamiento en reglas de almacenamiento

Para continuar con el ejemplo anterior, aplique la categoría de almacenamiento
`Palés de alta frecuencia` en las ubicaciones `PAL1` y `PAL2`. Configure las
reglas de almacenamiento de la siguiente forma:

Suponga que se recibe un palé de latas de limonada:

  * Si PAL1 y PAL2 están vacíos, el palé se redirigirá a WH/Existencias/Palés/PAL1.

  * Si PAL1 está lleno, el palé se redirigirá a WH/Existencias/Palés/PAL2.

  * Si PAL1 y PAL2 están llenos, el palé se redirigirá a WH/Existencias/Palés.

![Uso de categorías de almacenamiento en varias reglas de
almacenamiento.](../../../../../_images/smart-putaways.png)

