# Optimización de motores de búsqueda (SEO)

La optimización para motores de búsqueda (con frecuencia abreviada como SEO)
es una estrategia de marketing digital para mejorar la visibilidad y el
posicionamiento de un sitio web en los resultados de un motor de búsqueda (por
ejemplo, Google). Consiste en optimizar varios elementos de su sitio web como
su contenido, la imagen que aparece cuando lo comparte en redes sociales, URL,
imágenes y velocidad de la página.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Konvergo ERP ofrece varios módulos para ayudarte a crear el contenido de tu sitio web, como <a href="../../ecommerce">Comercio electrónico</a>, <a href="../../blog">Blog</a>, <a href="../../elearning">eLearning</a> y <a href="../../forum">Foro</a>.</p></li>
<li><p>Todos los temas de Konvergo ERP usan <a href="https://getbootstrap.com/">Bootstrap</a>, un marco de trabajo para CSS, para renderizar de manera eficiente en el dispositivo correspondiente: escritorio, tableta o celular. Esto influye de forma positiva en el posicionamiento en los motores de búsqueda.</p></li>
</ul>
</div>

## Optimización de contenido

Para optimizar el SEO de una página web, primero acceda a ella y luego vaya a
Sitio web ‣ Sitio ‣ Optimizar SEO.

![Optimizar SEO](../../../../_images/optimize-seo.png)

### Etiquetas meta

Las etiquetas meta son elementos HTML que proporcionan información sobre un
sitio web a los motores de búsqueda y a sus visitantes. Son una parte
elemental para el SEO, pues ayudan a que los motores de búsqueda comprendan el
contenido y el contexto de una página web y también atraen visitantes por el
mismo motivo. Konvergo ERP cuenta con dos tipos de etiquetas meta:

  * Las etiquetas de **título** específico el título de una página web y en los motores de búsqueda aparecen como un enlace en el que se puede hacer clic. Deben ser concisas, descriptivas y relevantes para el contenido de la página. Es posible actualizar la etiqueta de título de su página web o dejarla vacía para usar el valor predeterminado según el contenido de la página.

  * Las etiquetas de **descripción** resumen el contenido de la página web y con frecuencia aparecen en los resultados del motor de búsqueda debajo del título. Se utilizan para invitar al usuario a visitar la página. Puede actualizar la etiqueta de descripción de su página web o dejarla vacía para usar el valor predeterminado según el contenido de la página.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>La tarjeta <b>Vista previa</b> muestra cómo se visualizarían las etiquetas de título y descripción en los resultados de búsqueda. Además, incluye la URL de su página.</p>
</div>

### Palabras clave

Las palabras claves son uno de los elementos clave del SEO. Un sitio web que
está bien optimizado para los motores de búsqueda utiliza palabras clave que
son relevantes para que los visitantes potenciales encuentren lo que están
buscando. En resumen, el SEO permite que los visitantes encuentren su sitio
con facilidad.

Escriba las palabras clave que considere esenciales en el campo **Palabra
clave** y haga clic en **Agregar** para visualizar cómo se utilizan en
distintos niveles de su contenido (H1, H2, título de la página, descripción de
la página, contenido de la página) y en las búsquedas relacionadas en Google.
La herramienta también sugiere palabras clave relevantes para aumentar el
tráfico web. Entre más palabras clave estén presentes en su página web, mejor.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Por cuestiones de SEO, le recomendamos encarecidamente que solo use un título H1 por página.</p>
</div>

### Imágenes para compartir en redes sociales

La imagen de su logotipo es la que aparece cuando comparte su página en redes
sociales, pero puede subir cualquier otra imagen al hacer clic en la flecha
que apunta hacia arriba.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>La tarjeta <b>Vista previa social</b> muestra cómo aparecería la información al compartirla.</p></li>
<li><p>Si cambia el título de alguna entrada del blog o el nombre de un producto, los cambios se aplican de forma automática en todas las partes de su sitio web. El enlace antiguo todavía funciona cuando los sitios web externos utilizan una <a href="../pages#website-url-redirection"><span class="std std-ref">redirección 301</span></a> para mantener el posicionamiento del SEO.</p></li>
</ul>
</div>

## Imágenes

El tamaño de las imágenes afecta de forma importante la velocidad de la
página. Es un criterio indispensable para los motores de búsqueda para
optimizar el posicionamiento SEO.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Compare el posicionamiento de su sitio web en <a href="https://pagespeed.web.dev/?utm_source=psi&amp;utm_medium=redirect">Google Page Speed</a> o en <a href="https://tools.pingdom.com/">Pingdom Website Speed Test</a>.</p>
</div>

En automático, Konvergo ERP comprime las imágenes que sube para reducir su peso y
mejorar la velocidad de carga de la página. Todas las imágenes incluidas en
los temas oficiales de Konvergo ERP también se comprimen de forma predeterminada. Si
está utilizando un tema de terceros, es posible que incluya imágenes que no
están comprimidas correctamente.

**Para modificar una imagen** de su sitio web, selecciónela, haga clic en
**Editar** , luego vaya a la pestaña **Personalizar** y ajuste el **ancho** en
la sección **Imagen**.

![Compresión de imágenes automatizada. ](../../../../_images/image-width.png)
<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Las etiquetas «alt» se utilizan para proporcionar contexto sobre lo que aparece en una imagen, se lo informan a los rastreadores de motores de búsqueda para que puedan indexar una imagen de manera adecuada. Desde la perspectiva de SEO, agregar palabras clave a las etiquetas alt en el campo <b>Descripción</b> es indispensable. Esta descripción se agrega al código HTML de su imagen y aparece cuando no es posible visualizar la imagen.</p>
</div>

## Funciones avanzadas

### Marcado de datos estructurados

El marcado de datos estructurados se encarga de generar fragmentos
enriquecidos en los resultados del motor de búsqueda. Gracias a esto, los
sitios web pueden enviar datos estructurados a los robots de los motores de
búsqueda que les ayudarán a comprender su contenido y crear mejores resultados
de búsqueda.

De forma predeterminada, Google es compatible con varios [fragmentos
enriquecidos](https://developers.google.com/search/blog/2009/05/introducing-
rich-snippets) para tipos de contenido como comentarios, personas, productos,
negocios, eventos y organizaciones.

Los microdatos son un conjunto de etiquetas, implementados desde HTML5, que
ayudan a que los motores de búsqueda comprendan mejor su contenido y lo
muestren de forma adecuada. Konvergo ERP implementa microdatos según lo definido en la
[especificación](https://schema.org/docs/gs) de schema.org para eventos,
productos de comercio electrónico, publicaciones de foros y direcciones de
contacto. Esto permite que las páginas de sus productos aparezcan en Google
con información adicional como su precio y su calificación:

![Snippets en los resultados del motor de búsqueda.
](../../../../_images/data-markup.png)

### robots.txt

Los archivos robots.txt se encargan de indicarle a los rastreadores de motores
de búsqueda a qué URL de su sitio puede acceder el rastreador para indexar su
contenido. Estos se usan principalmente para evitar sobrecargar su sitio con
solicitudes.

Los motores de búsqueda consultan el archivo robots.txt al indexar su sitio
web. Konvergo ERP crea uno de estos archivos de forma automática y está disponible en
`mibasededatos.odoo.com/robots.txt`.

Es posible controlar a qué páginas del sitio pueden acceder los rastreadores
de motores de búsqueda si edita el archivo robots.txt. Para agregar
instrucciones personalizadas al archivo, vaya a Sitio web ‣ Configuración ‣
Ajustes, busque la sección **SEO** y haga clic en **Editar robots.txt**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Si no desea que los robots rastreen la página <code>/sobre-nosotros</code> de su sitio puede editar el archivo robots.txt para agregar <code>Disallow: /sobre-nosotros</code>.</p>
</div>

### Mapa del sitio

El mapa del sitio señala las páginas del sitio web y su relación entre ellas a
los robots de los motores de búsqueda. Konvergo ERP genera un archivo `/sitemap.xml`
que incluye todas las URL. Por motivos de rendimiento, este archivo se
almacena en caché y se actualiza cada 12 horas.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Konvergo ERP creará un archivo de índice de mapa del sitio si su sitio web tiene muchas páginas, respetará <a href="http://www.sitemaps.org/protocol">el protocolo de sitemaps.org</a> y agrupará las URL del mapa del sitio en fragmentos de 45,000 por archivo.</p>
</div>

Cada entrada del mapa del sitio web tiene tres atributos que se calculan de
forma automática:

  * `<loc>`: la URL de una página.

  * `<lastmod>`: última fecha de modificación del recurso, se calcula de forma automática según el objeto relacionado. En el caso de una página relacionada con un producto, podría ser la última fecha de modificación del producto o de la página.

  * `<priority>`: es posible que los módulos implementen su algoritmo por prioridad según su contenido. Por ejemplo, la prioridad en un foro se puede asignar según el número de votos en una publicación en específico. Por otro lado, si se trata de una página web estática, esta se definirá por su campo de prioridad, este se encuentra normalizado (16 es el número predeterminado).

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para evitar que las páginas aparezcan en un mapa del sitio, vaya a Sitio ‣ Propiedades, haga clic en la pestaña <b>Publicar</b> y desactive la función <b>Indexado</b>.</p>
<blockquote>
<div><img alt='Desmarcar la casilla "Indexado".' src="../../../../_images/page-properties.png"/>
</div></blockquote>
</div>

### Atributos hreflang de HTML

De forma automática, Konvergo ERP incluye los atributos `hreflang` y `x-default` en el
código de las páginas con varios idiomas de su sitio web. Estos atributos HTML
son indispensables para que los motores de búsqueda cuenten con la información
relacionada al idioma y la segmentación geográfica de una página en
específico.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../configuration/translate">Traducciones</a></p>
</div>

