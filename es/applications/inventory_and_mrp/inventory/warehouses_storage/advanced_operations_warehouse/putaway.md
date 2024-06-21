# Reglas de almacenamiento

El almacenamiento es el proceso de enrutamiento de productos a los lugares de
almacenamiento apropiados cuando llega el envío.

Konvergo ERP tiene la capacidad de realizar ese proceso a través de _reglas de
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

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="https://www.youtube.com/watch?v=nCQMf6sj_w8">Tutoriales de Konvergo ERP: Reglas de almacenamiento</a></p>
</div>

## Configuración

Para utilizar las reglas de almacenamiento, vaya a Inventario ‣ Configuración
‣ Ajustes y active la función **Rutas multietapa** ubicada en la sección
**Almacén**. La función **Ubicaciones de almacenamiento** también se habilita
en automático.

Por último, haga clic en **Guardar**.

![Activar las rutas multietapa en los ajustes de la aplicación
Inventario.](../../../../../_images/activate-multi-step-routes.png)

### Definir reglas de almacenamiento

Para gestionar dónde se enrutan ciertos productos para su almacenamiento, vaya
a la aplicación Inventario ‣ Configuración ‣ Reglas de almacenamiento. Utilice
el botón **Crear** para configurar una nueva regla de almacenamiento en un
**producto** o **categoría de producto**.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Es posible definir las reglas de almacenamiento por producto, categoría de producto o tipo de paquete (aunque para esto último, la función <em>Paquetes</em> debe estar habilitada en Inventario ‣ Configuración ‣ Ajustes).</p>
</div>

En la misma línea, la ubicación de **Cuando el producto llega a** es donde se
activa la regla de almacenamiento para crear una operación y mover el producto
a la ubicación **Almacenar en**.

Para que esto funcione, la ubicación **Almacenar en** debe ser una
_sububicación_ de la primera (por ejemplo, `WH/Stock/Frutas` es una ubicación
específica y nombrada dentro de `WH/Stock` para facilitar la búsqueda de los
productos que se almacenan aquí).

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>En una ubicación de almacén, <b>WH/Stock</b>, se encuentran las siguientes sububicaciones:</p>
<ul>
<li><p>WH/Stock/Frutas</p></li>
<li><p>WH/Stock/Vegetales</p></li>
</ul>
<p>Asegúrese de que todas las manzanas se almacenan en la sección de frutas. Complete el campo <b>Almacenar en</b> con la ubicación <code>WH/Stock/Frutas</code> cuando el <b>producto</b> <code>Manzana</code> llegue a <code>WH/Stock</code>.</p>
<p>Repita este paso para todos los productos y haga clic en <b>Guardar</b>.</p>
<img alt="Crear reglas de almacenamiento para manzanas y zanahorias." class="align-center" src="../../../../../_images/create-putaway-rules.png"/>
</div>

### Prioridad de las reglas de almacenamiento

Konvergo ERP selecciona una regla de almacenamiento según la siguiente lista de
prioridades (de más alta a más baja) hasta encontrar una coincidencia:

  1. Tipo de paquete y producto

  2. Tipo de paquete y categoría de producto

  3. Tipo de paquete

  4. Producto

  5. Categoría de producto

<div class="alert alert-success">
<p class="alert-title">
Example</p><blockquote>
<div><p>El producto <code>Lata de limonada</code> tiene configuradas las siguientes reglas de almacenamiento:</p>
<ol class="arabic simple">
<li><p>Al recibir un <code>pallet</code> (<b>Tipo de paquete</b>) de <code>Latas de limonada</code>, este se redirige a <code>WH/Stock/Pallets/PAL1</code>.</p></li>
<li><p>La <b>categoría de producto</b> de <code>Lata de limonada</code> es <code>Todos/bebidas</code> y cuando recibe una <code>caja</code> de cualquier artículo en esta categoría de producto estos se redirigen a <code>WH/Stock/Estante 1</code>.</p></li>
<li><p>Cualquier producto en un <code>pallet</code> se redirige a <code>WH/Stock/Pallets</code>.</p></li>
<li><p>El producto <code>Lata de limonada</code> se redirige a <code>WH/Stock/Estante 2</code>.</p></li>
<li><p>Los artículos en la categoría de productos <code>Todos/bebidas</code> se redirigen a <code>WH/Stock/Refrigerador pequeño</code>.</p></li>
</ol>
</div></blockquote>
<img alt="Algunos ejemplos de reglas de almacenamiento." class="align-center" src="../../../../../_images/putaway-example.png"/>
</div>

## Categorías de almacenamiento

Las _categorías de almacenamiento_ son atributos adicionales de las
ubicaciones que permiten que el usuario defina la cantidad de productos que se
pueden almacenar en la ubicación y cómo la ubicación selecciona las reglas de
almacenamiento.

### Configuración

Para habilitar las categorías de almacenamiento, vaya a Inventario ‣
Configuración ‣ Ajustes y active la función **Categorías de almacenamiento**
en la sección **Almacén**. Después, haga clic en **Guardar**.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>La función <b>Ubicaciones de almacenamiento</b> <b>debe</b> estar habilitada para activar las <b>categorías de almacenamiento</b>.</p>
</div>

### Definir categorías de almacenamiento

Para crear una categoría de almacenamiento, vaya a Inventario ‣ Configuración
‣ Categorías de almacenamiento y haga clic en **Nuevo**.

Una vez en el formulario de categoría de almacenamiento, escriba un nombre en
el campo **Categoría de almacenamiento**.

Hay opciones disponibles para limitar la capacidad por peso, producto o tipo
de paquete. El campo **Permitir nuevo producto** define cuándo la ubicación
está disponible para almacenar un producto:

  * **Si la ubicación está vacía** : se puede agregar un producto solo si la ubicación está vacía.

  * **Si los productos son los mismos** : se puede agregar un producto solo si ya hay un producto igual ahí.

  * **Permitir productos mezclados** : se pueden almacenar varios productos distintos al mismo tiempo en esta ubicación.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Cree reglas de almacenamiento para los artículos que se almacenan en palés y asegure la revisión de capacidad de almacenamiento en tiempo real al crear la categoría <code>Palés de alta frecuencia</code>.</p>
<p>Proporciónele un nombre a la <b>categoría de almacenamiento</b> y seleccione <b>Si los productos son los mismos</b> en el campo <b>Permitir nuevo producto</b>.</p>
<p>A continuación, defina la capacidad del paquete en la pestaña <b>Capacidad por paquete</b>. Especifique el número de paquetes para el <b>tipo de paquete</b> correspondiente y establezca un máximo de <code>2.00</code> <code>palés</code> para una ubicación específica.</p>
<img alt="Crear una categoría de almacenamiento en la página." class="align-center" src="../../../../../_images/storage-category.png"/>
</div>

Una vez que guarde los ajustes de categoría de almacenamiento, puede
vincularla a una ubicación.

Para ello, vaya a Inventario ‣ Configuración ‣ Ubicaciones y seleccione una
ubicación. Haga clic en **Editar** y seleccione la categoría creada en el
campo **Categoría de almacenamiento**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Asigne la categoría de almacenamiento <code>Palés de alta frecuencia</code> a la sububicación <code>WH/Stock/Pallets/PAL 1</code>.</p>
<img alt="Cuando se crea una categoría de almacenamiento, se puede vincular a una ubicación de almacén." class="align-center" src="../../../../../_images/location-storage-category.png"/>
</div>

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

