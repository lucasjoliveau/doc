# Varios sitios web

Konvergo ERP le permite crear varios sitios web con la misma base de datos. Esto puede
ser útil, por ejemplo, si trabaja con varias marcas en su organización o para
crear sitios web separados para diferentes productos, servicios o incluso
distintas audiencias. En estos casos, tener distintos sitios web puede ayudar
a evitar confusiones, también facilita la adaptación de sus estrategias de
alcance digital para que pueda llegar al público correcto.

Puede diseñar y configurar cada sitio web de forma independiente con su propio
[nombre de dominio](domain_names), tema, páginas, menús,
[idiomas](translate),
[productos](../../ecommerce/managing_products/products), equipo de ventas
asignado, etc. También pueden compartir contenido y páginas entre ellos.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>El contenido duplicado (es decir, compartir páginas e información entre varios sitios web) puede tener un impacto negativo para la  <a href="../pages/seo">Optimización de motores de búsqueda (SEO)</a>.</p>
</div>

## Crear un sitio web

Siga estos pasos para crear un nuevo sitio web:

  1. Vaya a Sitio web ‣ Configuración ‣ Ajustes.

  2. Haga clic en **\+ Nuevo sitio web**.

![Botón de nuevo sitio web](../../../../_images/create-website.png)

  3. Especifique el **nombre** y el **dominio del sitio web**. Cada sitio web debe publicarse bajo su propio [dominio](domain_names).

  4. En caso de ser necesario, realice los ajustes correspondientes en **nombre de la empresa** , **idiomas** e **idioma predeterminado**.

  5. Haga clic en el botón **Crear**.

Ahora puede empezar a construir su nuevo sitio web.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>De forma predeterminada, todas las aplicaciones que haya instalado relacionadas con Sitio web (por ejemplo, <b>Comercio electrónico</b>, <b>Foro</b>, <b>Blog</b>, etc.) y sus páginas web relacionadas también están disponibles en el nuevo sitio. Puede eliminarlas cuando modifique el menú del sitio web.</p>
</div>

## Alternar entre sitios web

Para alternar entre sitios web, haga clic en el menú junto al botón **\+
Nuevo** en la esquina superior derecha y seleccione el sitio web al que desea
cambiar.

![Selector de sitios web](../../../../_images/switch-websites.png)
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Al cambiar de sitio web, se le redirige al otro en la misma página (URL) que el sitio actual. Si la página que está viendo no existe en el otro sitio web, se le redirige a una página de error 404. Una vez allí, haga clic en <b>Crear página</b>.</p>
<img alt="Crear una página desde una página de error 404" src="../../../../_images/404-create-page.png"/>
</div>

## Configuración específica del sitio web

La mayoría de los ajustes de los sitios web son específicos para cada uno de
ellos, lo que significa que se pueden habilitar o deshabilitar si es
necesario. Para adaptar los ajustes de un sitio web, vaya a Sitio web ‣
Configuración ‣ Ajustes. Seleccione el sitio web con el que trabajará en el
campo **Ajustes de sitio web** en la parte superior de la página
correspondiente, en el recuadro **amarillo**. Luego, adapte las opciones para
ese sitio web en específico.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Los sitios web se crean con la configuración predeterminada y esta no se transfiere de un sitio web a otro.</p></li>
<li><p>En un <a href="../../../general/companies">entorno multiempresa</a>, cada sitio web puede estar vinculado a una empresa específica en su base de datos para que solo sus datos relacionados (por ejemplo, productos, trabajos, eventos, etc.) aparezcan en el sitio web. Para mostrar datos específicos de la empresa, seleccione la empresa correspondiente en el campo <b>Empresa</b>.</p></li>
</ul>
</div>

### Disponibilidad del contenido

Las páginas, productos, eventos y otros que se crearon desde el frontend
(mediante el botón **\+ Nuevo**) solo están disponibles de forma
predeterminada en el sitio web en el que se crearon. Por otra parte, los
registros creados desde el backend están disponibles en todos los sitios web.
Puede cambiar la disponibilidad del contenido desde el backend, en el campo
**Sitio web**. Por ejemplo, para los productos, vaya a Comercio electrónico ‣
Productos, seleccione uno y luego vaya a la pestaña **Ventas** , para los
foros vaya a Configuración ‣ Foros y seleccione uno.

![Campo de sitio web en un formulario de foro](../../../../_images/forum-
multi-website.png)

Los registros y características pueden estar disponibles:

  * En todos los sitios web: deje el campo **Sitio web** vacío.

  * Solo en un sitio web: haga su elección en el campo **Sitio web** según corresponda.

  * En algunos sitios web: en este caso, debe duplicar el elemento, luego selecciónelo en el campo **Sitio web**.

#### Paginas de un sitio web

Para modificar el sitio web en el que publicará una página, siga estos pasos:

  1. Vaya a Sitio web‣ Sitio ‣ Páginas.

  2. Seleccione el sitio web en el que está publicada la página.

![Mostrar páginas por sitio web](../../../../_images/pages-switch-
websites.png)

  3. Marque la casilla junto a las páginas que desea modificar.

  4. Haga clic en el campo **Sitio web** y seleccione el sitio web, o déjelo vacío para publicar la página en todos los sitios web.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Cada sitio web debe tener su propia página de inicio, no puede utilizar la misma para varios sitios web.</p>
</div>

## Funciones de Comercio electrónico

Puede restringir funciones de Comercio electrónico como productos, categorías
de comercio electrónico, listas de precios, descuentos, proveedores de pagos,
etc. a un sitio web específico.

### Cuentas de cliente

Al habilitar la casilla **Cuentas de cliente compartidas** en los ajustes del
sitio web, [permite que sus clientes usen la misma
cuenta](../../ecommerce/ecommerce_management/customer_accounts) en todos
sus sitios web.

### Precios

Con las [listas de
precios](../../ecommerce/managing_products/price_management#ecommerce-
pricelists), los productos pueden tener un precio distinto en cada sitio web.
Se requiere la siguiente configuración:

  1. Vaya a Sitio web ‣ Configuración ‣ Ajustes.

  2. Vaya a la sección **Tienda - Productos** y seleccione la opción **Lista de precios** , luego seleccione **Múltiples precios por producto**.

  3. Haga clic en **Listas de precios** para definir listas nuevas o editar las que ya existen.

  4. Seleccione la lista de precios o haga clic en **Nuevo** para crear una, luego vaya a la pestaña **Configuración** y seleccione el **Sitio web** en el campo correspondiente.

## Reportes

### Analítica

Cada sitio web tiene sus propios datos analíticos. Para alternar entre sitios
web, haga clic en los botones ubicados en la esquina superior derecha.

![Alternar entre sitios web para obtener los datos
analíticos](../../../../_images/analytics-switch-websites.png)

### Otros datos para reportes

Otros datos para reportes, como los datos del tablero de Comercio electrónico,
análisis de ventas en línea y visitantes pueden agruparse por sitio web si es
necesario. Haga clic en **Agrupar por – > Sitio web**.

