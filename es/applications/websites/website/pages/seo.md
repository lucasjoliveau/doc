# Optimización de motores de búsqueda (SEO)

La optimización para motores de búsqueda (con frecuencia abreviada como SEO)
es una estrategia de marketing digital para mejorar la visibilidad y el
posicionamiento de un sitio web en los resultados de un motor de búsqueda (por
ejemplo, Google). Consiste en optimizar varios elementos de su sitio web como
su contenido, la imagen que aparece cuando lo comparte en redes sociales, URL,
imágenes y velocidad de la página.

Nota

  * Odoo ofrece varios módulos para ayudarte a crear el contenido de tu sitio web, como [Comercio electrónico](../../ecommerce.html), [Blog](../../blog.html), [eLearning](../../elearning.html) y [Foro](../../forum.html).

  * Todos los temas de Odoo usan [Bootstrap](https://getbootstrap.com/), un marco de trabajo para CSS, para renderizar de manera eficiente en el dispositivo correspondiente: escritorio, tableta o celular. Esto influye de forma positiva en el posicionamiento en los motores de búsqueda.

## Optimización de contenido

Para optimizar el SEO de una página web, primero acceda a ella y luego vaya a
Sitio web ‣ Sitio ‣ Optimizar SEO.

![Optimizar SEO](../../../../_images/optimize-seo.png)

### Etiquetas meta

Las etiquetas meta son elementos HTML que proporcionan información sobre un
sitio web a los motores de búsqueda y a sus visitantes. Son una parte
elemental para el SEO, pues ayudan a que los motores de búsqueda comprendan el
contenido y el contexto de una página web y también atraen visitantes por el
mismo motivo. Odoo cuenta con dos tipos de etiquetas meta:

  * Las etiquetas de título específico el título de una página web y en los motores de búsqueda aparecen como un enlace en el que se puede hacer clic. Deben ser concisas, descriptivas y relevantes para el contenido de la página. Es posible actualizar la etiqueta de título de su página web o dejarla vacía para usar el valor predeterminado según el contenido de la página.

  * Las etiquetas de descripción resumen el contenido de la página web y con frecuencia aparecen en los resultados del motor de búsqueda debajo del título. Se utilizan para invitar al usuario a visitar la página. Puede actualizar la etiqueta de descripción de su página web o dejarla vacía para usar el valor predeterminado según el contenido de la página.

Nota

La tarjeta Vista previa muestra cómo se visualizarían las etiquetas de título
y descripción en los resultados de búsqueda. Además, incluye la URL de su
página.

### Palabras clave

Las palabras claves son uno de los elementos clave del SEO. Un sitio web que
está bien optimizado para los motores de búsqueda utiliza palabras clave que
son relevantes para que los visitantes potenciales encuentren lo que están
buscando. En resumen, el SEO permite que los visitantes encuentren su sitio
con facilidad.

Escriba las palabras clave que considere esenciales en el campo Palabra clave
y haga clic en Agregar para visualizar cómo se utilizan en distintos niveles
de su contenido (H1, H2, título de la página, descripción de la página,
contenido de la página) y en las búsquedas relacionadas en Google. La
herramienta también sugiere palabras clave relevantes para aumentar el tráfico
web. Entre más palabras clave estén presentes en su página web, mejor.

Truco

Por cuestiones de SEO, le recomendamos encarecidamente que solo use un título
H1 por página.

### Imágenes para compartir en redes sociales

La imagen de su logotipo es la que aparece cuando comparte su página en redes
sociales, pero puede subir cualquier otra imagen al hacer clic en la flecha
que apunta hacia arriba.

Nota

  * La tarjeta Vista previa social muestra cómo aparecería la información al compartirla.

  * Si cambia el título de alguna entrada del blog o el nombre de un producto, los cambios se aplican de forma automática en todas las partes de su sitio web. El enlace antiguo todavía funciona cuando los sitios web externos utilizan una [redirección 301](../pages.html#website-url-redirection) para mantener el posicionamiento del SEO.

## Imágenes

El tamaño de las imágenes afecta de forma importante la velocidad de la
página. Es un criterio indispensable para los motores de búsqueda para
optimizar el posicionamiento SEO.

Truco

Compare el posicionamiento de su sitio web en [Google Page
Speed](https://pagespeed.web.dev/?utm_source=psi&utm_medium=redirect) o en
[Pingdom Website Speed Test](https://tools.pingdom.com/).

En automático, Odoo comprime las imágenes que sube para reducir su peso y
mejorar la velocidad de carga de la página. Todas las imágenes incluidas en
los temas oficiales de Odoo también se comprimen de forma predeterminada. Si
está utilizando un tema de terceros, es posible que incluya imágenes que no
están comprimidas correctamente.

**Para modificar una imagen** de su sitio web, selecciónela, haga clic en
Editar, luego vaya a la pestaña Personalizar y ajuste el ancho en la sección
Imagen.

![Compresión de imágenes automatizada. ](../../../../_images/image-width.png)

Importante

Las etiquetas «alt» se utilizan para proporcionar contexto sobre lo que
aparece en una imagen, se lo informan a los rastreadores de motores de
búsqueda para que puedan indexar una imagen de manera adecuada. Desde la
perspectiva de SEO, agregar palabras clave a las etiquetas alt en el campo
Descripción es indispensable. Esta descripción se agrega al código HTML de su
imagen y aparece cuando no es posible visualizar la imagen.

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
muestren de forma adecuada. Odoo implementa microdatos según lo definido en la
[especificación](https://schema.org/docs/gs.html) de schema.org para eventos,
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
web. Odoo crea uno de estos archivos de forma automática y está disponible en
`mibasededatos.odoo.com/robots.txt`.

Es posible controlar a qué páginas del sitio pueden acceder los rastreadores
de motores de búsqueda si edita el archivo robots.txt. Para agregar
instrucciones personalizadas al archivo, vaya a Sitio web ‣ Configuración ‣
Ajustes, busque la sección SEO y haga clic en Editar robots.txt.

Example

Si no desea que los robots rastreen la página `/sobre-nosotros` de su sitio
puede editar el archivo robots.txt para agregar `Disallow: /sobre-nosotros`.

### Mapa del sitio

El mapa del sitio señala las páginas del sitio web y su relación entre ellas a
los robots de los motores de búsqueda. Odoo genera un archivo `/sitemap.xml`
que incluye todas las URL. Por motivos de rendimiento, este archivo se
almacena en caché y se actualiza cada 12 horas.

Nota

Odoo creará un archivo de índice de mapa del sitio si su sitio web tiene
muchas páginas, respetará [el protocolo de
sitemaps.org](http://www.sitemaps.org/protocol.html) y agrupará las URL del
mapa del sitio en fragmentos de 45,000 por archivo.

Cada entrada del mapa del sitio web tiene tres atributos que se calculan de
forma automática:

  * `<loc>`: la URL de una página.

  * `<lastmod>`: última fecha de modificación del recurso, se calcula de forma automática según el objeto relacionado. En el caso de una página relacionada con un producto, podría ser la última fecha de modificación del producto o de la página.

  * `<priority>`: es posible que los módulos implementen su algoritmo por prioridad según su contenido. Por ejemplo, la prioridad en un foro se puede asignar según el número de votos en una publicación en específico. Por otro lado, si se trata de una página web estática, esta se definirá por su campo de prioridad, este se encuentra normalizado (16 es el número predeterminado).

Truco

Para evitar que las páginas aparezcan en un mapa del sitio, vaya a Sitio ‣
Propiedades, haga clic en la pestaña Publicar y desactive la función Indexado.

> ![Desmarcar la casilla "Indexado".](../../../../_images/page-properties.png)

### Atributos hreflang de HTML

De forma automática, Odoo incluye los atributos `hreflang` y `x-default` en el
código de las páginas con varios idiomas de su sitio web. Estos atributos HTML
son indispensables para que los motores de búsqueda cuenten con la información
relacionada al idioma y la segmentación geográfica de una página en
específico.

Ver también

[Traducciones](../configuration/translate.html)

