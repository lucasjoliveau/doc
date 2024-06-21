# Variantes de producto

Usamos las variantes de producto para que productos únicos tengan diferentes
características y opciones que los clientes puedan elegir, como tamaño,
estilo, color, entre otras.

Puede gestionar las variantes de los productos en la plantilla de cada
producto, o si va a la página **Variantes de producto** o **Atributos**. Todas
estas opciones se encuentran dentro de la aplicación _Ventas_ de Konvergo ERP.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Una empresa de ropa tiene el siguiente desglose de variantes para una de sus camisetas más vendidas:</p>
<ul>
<li><p>Camiseta clásica unisex</p>
<ul>
<li><p>Color: azul, rojo, blanco, negro</p></li>
<li><p>Talla: CH, M, G, XG, XXG</p></li>
</ul>
</li>
</ul>
<p>Aquí, la <b>camiseta</b> es la plantilla del producto y <b>Camiseta: Azul, S</b> es una variante de producto específica.</p>
<p>El <b>tamaño</b> y el <b>color</b> son atributos y las opciones correspondientes (como <b>azul</b> y <b>S</b>) son los <b>valores</b>.</p>
<p>En este caso, hay un total de veinte variantes de producto diferentes: cuatro opciones de <b>color</b> multiplicadas por cinco opciones de <b>tamaño</b>. Cada variante tiene su propio inventario, total de ventas y otros registros similares en Konvergo ERP.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../../../../websites/ecommerce/managing_products/variants">Variantes de producto</a></p>
</div>

## Configuración

Para usar variantes de producto, **debe** activar las **variantes** en la
aplicación **Ventas** de Konvergo ERP.

Para hacerlo, vaya a la aplicación Ventas ‣ Configuración ‣ Ajustes, y ubique
la sección **Catálogo de producto** en la parte superior de la página.

En esta sección, marque la caja para activar la funcionalidad **Variantes**.

![Imagen sobre la activación de las variantes de productos en la página de
ajustes de la aplicación de Ventas.](../../../../../_images/activating-
variants-setting.png)

Después, haga clic en **Guardar** en la parte superior de la página de
**Ajustes**.

## Atributos

Antes de poder configurar las variantes de productos, **debe** crear los
atributos. Para crear, gestionar y modificar los atributos, vaya a la
aplicación de ventas ‣ Configuración ‣ Atributos.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El orden de los atributos en la página <b>Atributos</b> determina cómo aparecen en el <b>configurador de productos</b>, el tablero de <b>Punto de venta</b> y las páginas de <b>Comercio electrónico</b>.</p>
</div>

Para crear un nuevo atributo desde la página **Atributos** haga clic en
**Nuevo**. Así se mostrará un formulario de atributo en blanco que usted puede
personalizar y configurar de varias maneras.

![Un formulario de creación de atributos en blanco en la aplicación Ventas de
Konvergo ERP](../../../../../_images/attribute-creation.png)

Primero, cree un **Nombre de atributo** , como `Color` o `Tamaño`.

Después, en el campo opcional **Categoría** seleccione una categoría desde el
menú desplegable para agrupar atributos similares dentro de la misma sección
para ser más específicos y organizados.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Para ver los detalles relacionados a la categoría de atributos seleccionada, haga clic en el enlace del símbolo <b>➡️ (flecha)</b> que se encuentra a la derecha del campo <b>Categoría</b>. Así se mostrará el formulario de detalle de la categoría de ese atributo.</p>
<img alt="Una página de detalles de categoría de atributo estándar a la cual se puede entrar mediante el icono de flecha de enlace interno." class="align-center" src="../../../../../_images/attribute-category-internal-link.png"/>
<p>Aquí, el <b>Nombre de categoría</b> y la <b>Secuencia</b> se muestran en la parte superior, seguido por <b>atributos relacionados</b> asociados con la categoría. Puede arrastrar y soltar estos atributos en el orden de prioridad que quiera.</p>
<p>Puede agregar atributos directamente a la categoría, también puede hacer clic en <b>Agregar una lína</b>.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para crear una categoría de atributo directamente desde este campo, empiece a escribir el nombre de la nueva categoría. Después seleccione <b>Crear</b> o <b>Crear y editar…</b> en el menú desplegable que aparece.</p>
<p>Al hacer clic en <b>Crear</b>, se crea la categoría, la cual podrá editar después. Si hace clic en <b>Crear y editar…</b> se crea la categoría y aparece una ventana emergente para <b>Crear categoría</b>, en donde podrá personalizar y configurar la categoría de inmediato.</p>
</div>

Abajo del campo **Categoría** están las **Opciones de visualización**. El
**tipo de visualización** determina cómo se mostrará el producto en la tienda
en línea, en el tablero del **Punto de venta** y en el **Configurador del
producto**.

Las **Opciones de visualización** son:

  * **Radio** : las opciones aparecerán en una lista con botones de opción en la página de productos de la tienda en línea.

  * **Barra** : las opciones aparecerán como botones seleccionables en la página de la tienda en línea del producto.

  * **Seleccionar** : las opciones aparecen en un menú desplegable en la página del producto de la tienda en línea.

  * **Color** : las opciones aparecen como cuadrados pequeños de colores que representarán en la página del producto en la tienda en línea el código de color HTML que se haya seleccionado.

![Tipos de visualización en la configuración del producto en la tienda en
línea de Konvergo ERP.](../../../../../_images/display-types.png)

El campo **modo de creación de las variantes** le informa a Konvergo ERP cuándo debe
crear de manera automática una nueva variante, después de agregar un atributo
a un producto.

  * **Instantáneamente** : crea todas las variantes posibles tan pronto como se agregan atributos y valores a una plantilla de producto.

  * **Dinámicamente** : crea variantes **solo** cuando se agregan atributos y valores correspondientes a una orden de venta.

  * **Nunca (opción)** : nunca crea variantes de manera automática.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>El <b>modo de creación de las variantes</b> de un atributo no se puede editar después de que se agregó a un producto.</p>
</div>

Por último, el campo **Visibilidad del filtro de comercio electrónico**
determina si las opciones de este atributo serán visibles para el cliente
desde el frontend cuando estén comprando en la tienda en línea.

  * **Visible** : los clientes pueden ver los atributos de los valores desde el frontend.

  * **Oculto** : los clientes no pueden ver los atributes de valores desde el frontend.

### Valores de atributos

Los valores de los atributos se tienen que agregar en la pestaña **Valores de
atributo**. Puede agregar valores a un atributo a la vez si así lo necesita.

Para agregar un valor, haga clic en **Agregar una línea** en la pestaña
**Valores de atributo**.

Después, ingrese el nombre del valor en la columna **Valor**. Después, marque
la casilla en la columna **Es valor personalizado** , si el valor es
personalizado (es decir, el cliente brindará especificaciones únicas para este
valor en específico).

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si selecciona el <b>Tipo de visualización</b> - <b>Color</b>, aparecerá la opción para para agregar un código de color HTML en el lado derecho de la línea de valor, para que sea más fácil para los vendedores y clientes saber exactamente qué opción están seleccionando.</p>
<img alt="La pestaña de valores de atributo cuando se hace clic en agregar una línea, donde se muestran columnas personalizadas." class="align-center" src="../../../../../_images/attribute-value-add-a-line.png"/>
<p>Para elegir un color, haga clic en el círculo en blanco en la columna <b>Color</b>, lo cual mostrará una ventana emergente para seleccionar el color HTML.</p>
<img alt="Selección de un color desde la ventana emergente para seleccionar HTML que aparece en el formulario del atributo." class="align-center" src="../../../../../_images/picking-a-color.png"/>
<p>En esta ventana emergente, seleccione un color específico, solo tiene que arrastrar el seleccionador de color al tono que quiera y hacer clic para confirmar.</p>
<p>O seleccione un color específico, haga clic en el icono de <em>gotero</em> y seleccione el color deseado que pueda hacer clic en la pantalla.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>También puede crear atributos desde la plantilla de producto. Agregue una nueva línea y escriba el nombre en la pestaña <b>Variantes</b>.</p>
</div>

Una vez que se agrega un atributo a un producto, ese producto se enlista y se
puede acceder con el botón inteligente **Productos relacionados**. Ese botón
enlista todos los productos en la base de datos que están utilizando el
atributo.

## Variantes de producto

Una vez que se crea el atributo, úselo (junto con sus valores) para crear una
variante de producto. Para hacerlo, vaya a la aplicación Ventas ‣ Productos ‣
Productos y seleccione un producto existente para ver el formulario de
producto deseado. O, haga clic en **Crear** para crear un producto nuevo al
que le puede agregar una variante de producto.

En el formulario de producto, haga clic en le pestaña **Atributos y
variantes** para ver, gestionar y modificar los atributos y valores del
producto.

![La pestaña de atributos y valores en un producto común en Ventas de
Konvergo ERP.](../../../../../_images/attributes-values-tab.png)

Para agregar un atributo a un producto, y valores de atributo subsecuentes,
haga clic en **Agregar una línea** en la pestaña **Atributos y valores**.
Después, seleccione el atributo deseado del menú desplegable que aparece.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Puede crear atributos directamente desde la pestaña <b>Atributos y variantes</b> del formulario de producto. Para hacerlo, primero escriba el nombre del nuevo atributo en el campo en blanco y seleccione ya sea <b>Crear</b> o <b>Crear y editar…</b> desde el menú desplegable que aparece.</p>
<p>Al hacer clic en <b>Crear</b>, se crea el atributo, el cual podrá editar después. Si hace clic en <b>Crear y editar…</b> se crea el atributo y aparece una ventana emergente para <b>Crear el atributo</b>, en donde podrá personalizar y configurar la categoría de inmediato.</p>
</div>

Una vez que seleccione un atributo en la columna **Atributo** seleccione los
valores específicos de atributo que tiene que aplicar en el producto, desde el
menú desplegable disponible en la columna **Valores**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>No hay límite sobre cuántos valores puede agregar.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../../../../websites/ecommerce/managing_products/variants">Variantes de producto</a></p>
</div>0

### Configurar variantes

A la derecha de la línea de atributo está el botón **Configurar**. Al hacer
clic, Konvergo ERP mostrará una página separada con esos **Valores de variantes de
producto** específicos.

![Puede acceder a la página Valores de variantes de producto con el botón
Configurar en un formulario de producto.](../../../../../_images/product-
variant-values.png)

Aquí puede ver el nombre específico de **Valor** , **Índice de color HTML**
(si aplica) y el **Valor del precio adicional**.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../../../../websites/ecommerce/managing_products/variants">Variantes de producto</a></p>
</div>1

Cuando se hace clic en la página **Valores de variantes de producto** Konvergo ERP
mostrará una página a parte donde verá los detalles relacionados a los
valores.

![Una página de valores de la variante de producto a la que se puede acceder a
través de la página general Valores de variantes de
producto.](../../../../../_images/product-variant-value-page.png)

En esa página de detalles de la variante específica podrá encontrar los campos
**Valor** y **Valores de variantes de producto** , así como un campo **Excluir
para**.

En el campo **Excluir para** puede agregar **Plantillas de producto** y
**Valores de atributo** específicos. Al hacerlo, este valor de atributo
específico se excluirá de esos productos.

### Botón inteligente de variantes

Cuando un producto tiene atributos y variantes configurados en la pestaña
**Atributos y variantes** , aparecerá un botón **Variantes** en la parte
superior del formulario del producto. El botón inteligente **Variantes**
indica cuántas variantes están configuradas en ese producto en específico.

![El botón inteligente de variantes en la parte superior del formulario de
producto en Ventas.](../../../../../_images/variants-smart-button.png)

Cuando se hace clic en el botón inteligente **Variantes** , Konvergo ERP mostrará una
página separa donde podrá ver todas las combinaciones de variantes de
productos configuradas

![Puede acceder a la página de variantes mediante el botón inteligente
variantes en el formulario de producto de
Konvergo ERP.](../../../../../_images/variants-page.png)

## Impacto de variantes

Además de ofrecer opciones de productos más detalladas a los clientes, las
variantes de producto tienen sus propios impactos y puede aprovecharlas en
toda la base de datos de Konvergo ERP.

  * **Código de barras** : los códigos de barra están asociados con cada variante en lugar de cada plantilla de producto. Cada variante individual puede tener su propio código de barras o SKU.

  * **Precio** : cada variante de producto tiene su propio precio público, el cual es la suma de la plantilla del producto _y_ cargos adicionales para atributos particulares.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../../../../websites/ecommerce/managing_products/variants">Variantes de producto</a></p>
</div>2

  * **Inventario** : el inventario se cuenta por cada variante de producto individual. En el formulario de la plantilla del producto, el inventario refleja la suma de todas las variantes, pero el inventario real se calcula según las variantes individuales.

  * **Imagen** : cada variante de producto puede tener su propia imagen específica.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../../../../websites/ecommerce/managing_products/variants">Variantes de producto</a></p>
</div>3 <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../../../../websites/ecommerce/managing_products/variants">Variantes de producto</a></p>
</div>4

