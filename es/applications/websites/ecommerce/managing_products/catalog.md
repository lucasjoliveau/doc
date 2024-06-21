# Catálogo

El catálogo de comercio electrónico es el equivalente a los estantes de una
tienda física: permite que los clientes vean sus productos. Mostrar las
categorías con claridad, las opciones disponibles, la clasificación y las
opciones de navegación te ayudará a estructurarlo de forma eficiente.

## Uso de categorías de productos

En Konvergo ERP, hay un **modelo de categoría específico** para su comercio
elecrónico. Usar categorías para sus productos le permite añadir un menú de
navegación en su página de comercio electrónico. Los visitantes pueden usarlo
para ver todos los productos bajo la categoría que seleccionen.

Para hacerlo, vaya a Sitio web ‣ Comercio electrónico ‣ Productos, seleccione
el producto que desea modificar, haga clic en la pestaña **Ventas** y
seleccione las **Categorías** que desee en la tienda del **comercio
electrónico**.

![Categorías de comercio electrónico en la pestaña de
ventas](../../../../_images/catalog-categories.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Un mismo producto puede aparecer en varias categorías de comercio electrónico.</p>
</div>

Cuando establezca las categorías de sus productos, vaya a la **página
principal de la tienda** y haga clic en Editar ‣ Personalizar pestaña. En la
opción **Categorías** , puede habilitar un menú en la parte **Izquierda** , en
la parte **Superior** , o en ambas. Si selecciona la categoría **Izquierda** ,
aparece la opción **Contraer categoría recursiva** que permite hacer que el
menú de la categoría **Izquierda** se pueda contraer.

![Opciones de categorías para su comercio
electrónico](../../../../_images/catalog-panel-categories.png)
<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="products">Gestión de productos</a></p>
</div>

### Navegación

Usar categorías en el comercio electrónico le permite organizar y dividir sus
productos. Sin embargo, si necesita un nivel adicional de categorización en su
catálogo, puede activar **filtros** como atributos u ordenar por.

#### Atributos

Los atributos se refieren a **características** de un producto, como **color**
o **material** , mientras que las variantes son las diferentes combinaciones
de atributos. Puede encontrar los **atributos y variantes** en Sitio Web ‣
Comercio electrónico ‣ Productos, seleccione un producto y abra la pestaña
**Atributos y variantes**.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../../../sales/sales/products_prices/products/variants">Variantes de producto</a></p></li>
</ul>
</div> ![Atributos y variantes de su
producto](../../../../_images/catalog-attributes.png)

Para activar el **filtrado por atributos** , vaya a la **página principal de
su tienda** , haga clic en Editar ‣ Personalizar pestaña y seleccione
**Izquierda** , **Arriba** , o ambas. Además, también puede activar el
**filtro por precios** para activar los filtros de precios.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El <b>filtro de precio</b> no depende de los <b>atributos</b>, por lo tanto, puede activarse por sí solo si así lo desea.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Puede utilizar los <b>filtros de atributos</b> aunque no trabaje con variantes de productos. Cuando agregue atributos a sus productos, asegúrese de especificar solo <em>un</em> valor por atributo. Konvergo ERP no crea variantes si no hay combinación posible.</p>
</div>

#### Ordenar por

Puede permitir que el usuario **clasifique manualmente el catálogo** gracias a
la barra de búsqueda. Desde la **página principal de la tienda** , haga clic
en Editar ‣ Personalizar; puede activar o desactivar la opción **Ordenar por**
así como el botón de **diseño**. También puede seleccionar la opción
**Clasificación predeterminada** del botón **Ordenar por**. La clasificación
predeterminada se aplica a _todas_ las categorías.

Las opciones de **clasificación** son:

  * Destacado

  * Llegadas más recientes

  * Nombre (A-Z)

  * Precio - bajo a alto

  * Precio - alto a bajo

Además, puede **editar manualmente** el orden de un producto en el catálogo,
solo debe ir a **la página principal de la tienda** y hacer clic en el
producto. En la sección **Producto** de la sección **Personalizar** , puede
reorganizar el orden haciendo clic en las flechas. `<<` `>>` mueve el producto
a la **extrema** derecha o a la izquierda, y `<` `>` mueve el producto **una**
fila a la derecha o a la izquierda. También es posible cambiar el orden de los
productos del catálogo en Sitio web ‣ Comercio electrónico ‣ Productos y
arrastrando y soltando los productos dentro de la lista.

![Reorganización de productos en el catálogo](../../../../_images/catalog-
reorder.png)

## Diseño de la página

### Página de categoría

Puede personalizar el diseño de la página de categorías utilizando el creador
de sitios web.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>La edición del diseño de la página de categoría es global; la edición del diseño de una categoría afecta a <em>todas</em> las páginas de categoría.</p>
</div>

Para ello, vaya a la página Categoría ‣ Editar ‣ Personalizar. Aquí puede
elegir el diseño, el número de columnas para mostrar los productos, etc. El
botón **descripción del producto** hace que la descripción del producto sea
visible desde la página de la categoría, debajo de la imagen del producto.

![Opciones de diseño de las páginas de
categorías.](../../../../_images/catalog-category-layout.png)
<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Puede elegir el tamaño de la tabla, pero tenga en cuenta que mostrar demasiados productos puede afectar el rendimiento y la velocidad de carga de la página.</p>
</div>

### Producto destacado

Puede destacar productos para hacerlos más visibles en la página de categoría
o de producto. En la página de su elección, vaya a Editar ‣ Personalizar y
haga clic en el producto a destacar. En la sección **Producto** , puede elegir
el tamaño de la imagen del producto haciendo clic en la tabla, y también puede
añadir una **cinta** o **insignia**. Esto muestra una cinta a través de la
imagen del producto que dice:

  * Oferta

  * Agotado

  * Sin existencias

  * Nuevo

De otra manera, puede activar el [modo de
desarrollador](../../../general/developer_mode) en la **plantilla del
producto** , y en la pestaña **Ventas** , cambiar o crear la cinta desde el
campo **Cinta**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El <a href="../../../general/developer_mode">modo de desarrollador</a> solo está pensado para usuarios experimentados que deseen tener acceso a herramientas avanzadas. El uso del <b>modo de desarrollador</b> <em>no</em> está recomendado para usuarios normales.</p>
</div> ![Cinta para destacar
producto](../../../../_images/catalog-product-highlight.png)

## Funciones adicionales

Puede acceder y activar botones adicionales como **añadir al carrito** ,
**lista comparativa** o **lista de deseos**. Para ello, vaya a la **página
principal de la tienda** y, al final de la categoría **Página de productos** ,
haga clic en los botones que desee utilizar. Los tres botones aparecen al
pasar el ratón sobre la imagen de un producto.

  * **Añadir al carrito** : añade un botón para [añadir el producto al carrito](../checkout_payment_shipping/cart);

  * **Lista de comparación** : añade un botón para **comparar** productos según su precio, variante, etc;

  * **Botón de lista de deseos** : añade un botón para añadir un producto a una **lista de deseos**.

![Botones de funciones para añadir al carrito, lista comparativa y lista de
deseos](../../../../_images/catalog-buttons.png) ![Aspecto de los botones al
pasar el ratón sobre ellos](../../../../_images/catalog-features.png)

## Agregar contenido

Puede utilizar **bloques de creación** para agregar contenido a la página de
categoría, con una variedad de bloques que van desde **Estructura** a
**Contenido dinámico**. Hay áreas específicas definidas para utilizar bloques
y se resaltan en la página al **arrastrar y soltar** un bloque.

![Áreas de bloques de creación](../../../../_images/catalog-content.png)

  * Si coloca un bloque de creación **en la parte superior** de la lista de productos, creará un nuevo encabezado de categoría específico para _esa_ categoría.

  * Si coloca un bloque de creación **en la parte superior** o **inferior** de la página será visible en _todas_ las páginas de categoría.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Añadir contenido a una página de categoría de comercio electrónico es beneficioso en términos de estrategia <b>SEO</b>. El uso de <b>palabras clave</b> vinculadas a los productos o a las categorías de comercio electrónico mejora el tráfico orgánico. Además, cada categoría tiene su propia URL específica a la que se puede apuntar y que es indexada por los motores de búsqueda.</p>
</div>

