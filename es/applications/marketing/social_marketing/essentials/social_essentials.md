# Fundamentos de marketing social

La aplicación _Marketing social_ de Konvergo ERP ayuda a quienes se encargan del
marketing de contenido a crear y programar publicaciones, gestionar varias
cuentas de redes sociales, analizar la efectividad del contenido e interactuar
directamente con los seguidores de las redes sociales en una ubicación
centralizada.

## Cuentas de redes sociales

Para crear publicaciones en redes sociales y analizar contenido con la
aplicación _Marketing social_ de Konvergo ERP, **debe** agregar las cuentas de redes
sociales como un _flujo_ en el tablero principal de la aplicación.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Tenga en cuenta que <b>no</b> puede agregar perfiles personales como flujo. El uso principal de la aplicación <em>Marketing social</em> de Konvergo ERP es gestionar y analizar cuentas empresariales en plataformas de redes sociales.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>La aplicación <em>Marketing social</em> tiene algunas limitaciones con respecto a las cuentas de redes sociales. Konvergo ERP <b>no puede</b> gestionar una cantidad grande de páginas distintas (por ejemplo, un aproximado de 40 páginas) en la misma empresa. Estas limitaciones también aplican en un entorno multiempresas, ya que están relacionadas con la forma en la que está construida la API.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Si se encuentra en un entorno multiempresas deberá activar una página a la vez para cada empresa, de lo contrario ocurrirá un error con los permisos.</p>
<p>Por ejemplo, si la Empresa 1 es la única empresa seleccionada desde el tablero principal de Konvergo ERP y activa la <em>Página 1 de Facebook</em> y la <em>Página 2 de Facebook</em>, entonces podrá acceder a esas páginas desde el tablero de <em>Marketing social</em>.</p>
<p>Sin embargo, si en la misma base de datos, el usuario agrega la Empresa 2 desde el menú desplegable de empresas en ubicado en la parte superior y trata de agregar los mismos flujos, entonces ocurre un error con los permisos.</p>
<img alt="Vista del error de permiso que aparece cuando intenta agregar flujos de forma incorrecta." class="align-center" src="../../../../_images/permission-error.png"/>
</div>

### Flujos de redes sociales

Para agregar una cuenta empresarial de redes sociales como flujo, vaya a la
aplicación Marketing social y seleccione el botón **Agregar un flujo** que
está ubicado en la esquina superior izquierda. Al hacerlo, se abrirá la
ventana emergente **Agregar un flujo**.

![Vista de la ventana emergente que aparece cuando selecciona "Agregar un
flujo" en Konvergo ERP.](../../../../_images/add-stream-social-popup.png)

Una vez que se encuentre en la ventana emergente **Agregar un flujo** ,
seleccione **Vincular una nueva cuenta** para un negocio desde cualquiera de
las siguientes plataformas populares de redes sociales: **Facebook** ,
**Instagram** , **LinkedIn** , **X o Twitter** y **YouTube**.

Después de hacer clic en una de las redes sociales desde la ventana emergente
**Agregar un flujo** , Konvergo ERP le redirigirá a la página de autorización de esa
red social en específico, allí debe otorgar permiso para que Konvergo ERP agregue esa
cuenta como un flujo en la aplicación _Marketing social_.

![Ejemplo de un tablero en la aplicación Marketing social con contenido y
flujos de redes sociales.](../../../../_images/social-marketing-dashboard.png)

Una vez que proporcionó la autorización necesaria, Konvergo ERP regresa al **Feed** en
el tablero principal de **Marketing social**. Allí aparece una nueva columna
con las publicaciones de esa cuenta. Puede agregar cuentas o flujos en
cualquier momento.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Puede agregar una página de <b>Facebook</b> siempre y cuando la cuenta que realiza esta acción tenga permisos de administrador de la página. Además, puede agregar diferentes páginas para distintos flujos.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Las cuentas de <b>Instagram</b> se agregan a través de un inicio de sesión de <b>Facebook</b>, pues utilizan la misma API. Esto quiere decir que una cuenta de <b>Instagram</b> debe estar vinculada a una cuenta de <b>Facebook</b> para que aparezca como un flujo en Konvergo ERP.</p>
</div>

### Posts

Si hace clic en una publicación de un flujo de redes sociales abrirá una
ventana emergente que muestra el contenido de esa publicación en específico,
junto con todos los datos relacionados a las interacciones, por ejemplo, me
gusta, comentarios y otros.

![Ejemplo de una ventana emergente de una publicación de redes sociales en la
aplicación Marketing social de Konvergo ERP.](../../../../_images/social-post-
popup.png)

Si lo desea, el usuario puede dejar un nuevo comentario en la publicación
desde la ventana emergente de la publicación. Solo debe escribir su comentario
en el campo **Escriba un comentario…** y luego presionar la tecla **Enter (o
Entrar)** para publicarlo.

### Crear leads a partir de comentarios

La aplicación _Marketing social_ de Konvergo ERP también le permite crear leads a
partir de los comentarios en sus redes sociales.

Para crear un lead desde alguno de los comentarios en una publicación de redes
sociales, haga clic en la publicación correspondiente en el tablero para abrir
la ventana emergente específica de esa publicación. Luego, vaya hasta el
comentario indicado y haga clic en el icono de **tres puntos verticales** que
se encuentra a la derecha de ese comentario.

Al hacerlo, abre un menú desplegable con la opción **Crear lead**.

![El menú desplegable junto a un comentario que muestra la opción para crear
un lead.](../../../../_images/create-lead-drop-down.png)

Una vez que hace clic en **Crear lead** desde el menú desplegable del
comentario, aparece la ventana emergente de **Convertir publicación a lead**.

![La ventana emergente de convertir publicación a lead que aparece en la
aplicación Marketing social de Konvergo ERP.](../../../../_images/convert-post-to-
lead-popup.png)

En esta ventana emergente puede seleccionar si **Crear un nuevo cliente** ,
**Vincular a un cliente existente** o **No vincular a un cliente**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si selecciona <b>Vincular a un cliente existente</b>, aparece un nuevo campo de <b>Cliente</b> debajo de esas opciones, allí puede elegir un cliente para vincularlo a este lead.</p>
</div>

Una vez que seleccionó una opción, haga clic en el botón **Convertir** en la
parte inferior de la ventana emergente **Convertir publicación a lead**. Esto
abrirá un nuevo formulario de detalle de lead donde puede agregar y procesar
la información necesaria.

![Nuevo formulario de detalles de un lead creado a partir de un comentario en
redes sociales en la aplicación Marketing social de
Konvergo ERP.](../../../../_images/new-lead-detail-form-comments.png)

### Estadísticas

Cuando agrega un flujo de cuenta de redes sociales al tablero de _Marketing
social_ , cada flujo también muestra y vincula los KPI específicos de esa
plataforma de redes sociales, en caso de que la plataforma cuente con ellos.

Para consultar las estadísticas y métricas relacionadas con los KPI de
cualquier cuenta de redes sociales, haga clic en el enlace **Información** que
se encuentra en la parte superior de cada flujo.

![Visualización del enlace de información que aparece en el tablero de la
aplicación Marketing social.](../../../../_images/social-marketing-insights-
link.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si se encuentra en un entorno multiempresa y no selecciona <em>todas</em> las páginas, entonces se le desautenticará.</p>
<p>Por ejemplo, si las empresas tienen 3 páginas de <em>Facebook</em> pero solo le proporciona acceso a 1 y luego intenta proporcionarle acceso a otra después, se le desautenticará y perderá el acceso a la información y las métricas de la página inicial.</p>
<p>Asegúrese de agregar <em>todas</em> las páginas para <em>todas</em> las empresas del entorno multiempresas para evitar que ocurra este error. Si una página se desautentica solo tiene que eliminar el flujo y volverlo a establecer.</p>
</div>

## Crear y publicar contenido en redes sociales

La aplicación _Marketing social_ de Konvergo ERP le permite crear y publicar contenido
para cuentas de redes sociales desde la aplicación.

Para crear contenido para sus cuentas de redes sociales, vaya a la
:menuselection:` aplicación Marketing social` y haga clic en el botón **Nueva
publicación** que está ubicado en la esquina superior derecha del tablero de
_Marketing social_.

![Botón "Nueva publicación" en el tablero principal de la aplicación Marketing
social de Konvergo ERP.](../../../../_images/new-post-button-social-marketing-
dashboard.png)

O, vaya a Marketing social ‣ Publicacioness y haga clic en **Nuevo**.

![Nuevo botón en la página de publicaciones sociales en la aplicación
Marketing social.](../../../../_images/new-button-social-posts-page.png)

Cualquiera de las rutas anteriores muestra una publicación de red social en
blanco que se puede personalizar y configurar de varias maneras diferentes.

![Página de detalle de una publicación de red social en blanco en la
aplicación de Marketing social.](../../../../_images/blank-post-detail-
page.png)

### Formulario de detalles de la publicación

El formulario de detalles de una publicación para redes sociales en la
aplicación _Marketing social_ de Konvergo ERP tiene muchas opciones configurables
disponibles.

#### Compañía

Si está trabajando en un entorno multiempresa, el primer campo en la sección
**Su publicación** del formulario de detalles de la publicación de redes
sociales es **Empresa**. En este campo, seleccione la empresa que debería
estar vinculada a esta publicación de redes sociales.

#### Publicar en

Si está trabajando en un entorno de una sola empresa, el primer campo en la
sección **Su publicación** del formulario de detalles de publicación de redes
sociales es **Publicar en**. En este campo debe determina en qué red social se
debe realizar esta publicación, o a qué visitantes del sitio web se debería
enviar esta publicación mediante notificación emergente; solo tiene que
seleccionar la caja a un lado de la o las opciones deseadas.

En esta sección podrá elegir, de manera automática, todas las cuentas de redes
sociales disponibles que ha vinculado a su base de datos. Si una cuenta de red
sociales no se a agregado a la aplicación _Marketing social_ , entonces no
aparecerá como opción para publicar en la plantilla.

Puede seleccionar varios flujos de redes sociales y sitios web en el campo
**Publicar en**. Siempre debe seleccionar al menos **una** de las opciones en
el campo **Publicar en**.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Asegúrese de <em>habilitar las notificaciones push del sitio web</em> en la aplicación <em>Sitio web</em> para que la opción <b>Notificaciones push</b> aparezca en el formulario de detalles de la publicación.</p>
<p>Para hacerlo, vaya a la aplicación de Sitio web ‣ Configuración ‣ Ajustes y active <b>Habilitar las notificaciones push del sitio wen</b>, llene los campos correspondientes y haga clic en <b>Guardar</b>.</p>
</div>

#### Mensaje

Luego está el campo **Mensaje**. Aquí se crea el contenido principal de la
publicación.

En el campo **Mensaje** escriba el mensaje que quiere enviar en la
publicación. Después, haga clic en cualquier lugar fuera del **Mensaje** para
ver ejemplos visuales sobre cómo se verá la publicación en todas las redes
sociales seleccionadas (así como en los sitios web como notificaciones push).

![Publicación de red social de ejemplo con muestras visuales de cómo se verá
en diferentes redes sociales.](../../../../_images/visual-samples-social-
media-outlets-preview.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>También puede agregar emojis directo al texto en el campo <b>Mensaje</b>, solo haga clic en el icono de <b>🙂 (cara sonriente)</b> ubicado en la parte derecha de la línea de este campo. Al hacer clic en este icono se muestra un menú desplegable que contiene varios emojis para elegir.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si selecciona <b>Twitter</b> en el campo <b>Publicar en</b>, aparecerá un contador de caracteres debajo del campo <b>Mensaje</b>.</p>
</div>

#### Adjuntar imágenes

Si se utilizarán imágenes en la publicación, haga clic en **Adjuntar
imágenes** en la parte inferior del campo **Mensaje**. Al hacer clic, Konvergo ERP
mostrará una ventana emergente en la que puede seleccionar la imagen que
quiere subir desde su disco duro.

Después de subir y adjuntar la imagen deseada, Konvergo ERP le mostrará una nueva
previsualización de la publicación en la que se incluirá la imagen en el lado
derecho del formulario.

![Imágenes de ejemplo de publicaciones con las imágenes agregadas en la
aplicación Marketing social de Konvergo ERP.](../../../../_images/attach-images-
visual-social-post-sample.png)

#### Campaña

Después, hay un campo **Campaña** que no es obligatorio, pero le da la opción
de adjuntar esta publicación a una campaña de marketing específica.

Para agregar esta publicación a una campaña existente, haga clic en el campo
vacío **Campaña** para mostrar un menú desplegable donde podrá ver todas las
campañas existentes en la base de datos. Seleccione la campaña que desea y
agréguela.

Para crear una nueva campaña directamente desde el formulario de detalles de
la publicación, empiece a escribir el nombre de la nueva campaña en el campo
en blanco **Campaña** y seleccione ya sea **Crear** o **Crear y editar**.

![Imagen del menú desplegable con las opciones Crear y Crear y
editar.](../../../../_images/campaign-drop-down-menu-options.png)

Si hace clic en **Crear** se creará una campaña que puede editar y
personalizar después.

Si hace clic en **Crear y editar…** se creará la campaña y se abrirá un
ventana emergente **Crear campaña** , donde podrá editar los campos
**Identificador de campañas** , **Responsable** y **Etiquetas**.

![Ventana emergente para crear una campaña que aparece en el formulario de
detalle de la publicación.](../../../../_images/create-campaign-popup.png)

Cuando se realicen todos los ajustes deseados, haga clic en **Guardar y
cerrar** para guardar la campaña y regresar al formulario de detalles de la
publicación.

#### Cuándo

En el campo **Cuando** , elija **Enviar ahora** o **Programar después**. Con
la primera opción, Konvergo ERP enviará la publicación de inmediato; con la segunda,
en una fecha y hora posteriores.

Si selecciona **Programar después** , aparecerá un nuevo campo de **Fecha
planificada**. Si hace clic en el campo vació aparecerá un calendario en el
que puede designar una fecha y una hora futuras.

![Ventana emergente donde se programa una fecha que aparece en un formulario
de detalles de la publicación en Konvergo ERP.](../../../../_images/schedule-post-
calendar-popup.png)

Después de seleccionar una fecha y hora deseadas, haga clic en **Aplicar**.
Después, Konvergo ERP realizará la publicación en esa fecha y hora específicas en la o
las cuentas de redes sociales predeterminadas.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>La aplicación <em>Marketing social</em> tiene algunas limitaciones con respecto a las cuentas de redes sociales. Konvergo ERP <b>no puede</b> gestionar una cantidad grande de páginas distintas (por ejemplo, un aproximado de 40 páginas) en la misma empresa. Estas limitaciones también aplican en un entorno multiempresas, ya que están relacionadas con la forma en la que está construida la API.</p>
</div>0

#### Opciones de notificaciones push

Si se elige una (o varias) opciones de **[Notificación Push]** en el campo
**Publicar en** , aparecerá una sección específica de **Opciones de
notificación push** en la parte inferior del formulario de detalle de la
publicación en redes sociales.

![Sección de opciones de la notificación push en un formulario de detalles de
publicación.](../../../../_images/push-notification-options-section.png)

Tome en cuenta que ninguno de estos campos son obligatorios.

El primer campo en esta sección es **Título de la notificación**. En este
campo hay una opción para agregar un título personalizado a la notificación
push que se enviará.

Para designar una página específica para activar la notificación push en el
sitio web ingrese el URL de la página en el campo **URL objetivo**. Así, una
vez que un visitante llegue a esta página, Konvergo ERP mostrará la notificación push.

Debajo de ese campo está la opción para agregar una **imagen del icono** a la
notificación push. Este es un icono que aparece a un lado de la notificación
push.

Para subir una nueva imagen, haga clic en el cicono **✏️ (lápiz)** al pasar el
cursor por encima del icono de cámara de **Imagen del icono**. Hacerlo
mostrará una ventana emergente en donde puede subir la imagen de icono que
quiera desde su disco duro.

Una vez que lo haya hecho, Konvergo ERP actualizará de forma automática la
previsualización de cómo el icono aparecerá en la notificación push.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>La aplicación <em>Marketing social</em> tiene algunas limitaciones con respecto a las cuentas de redes sociales. Konvergo ERP <b>no puede</b> gestionar una cantidad grande de páginas distintas (por ejemplo, un aproximado de 40 páginas) en la misma empresa. Estas limitaciones también aplican en un entorno multiempresas, ya que están relacionadas con la forma en la que está construida la API.</p>
</div>1

También está el campo **todos los registros** , con el cual puede editar un
grupo específico de destinatarios en la base de datos, según ciertos
criterios, además de que se puede aplicar para **todas** o **algunas** de las
reglas.

Para utilizar este campo haga clic en el botón **\+ Agregar condición** , el
cual hará que aparezca campo de regla tipo ecuación.

En este campo tipo ecuación de regla puede especificar la criteria que Konvergo ERP
tomará en cuanta al enviar esta publicación a una audiencia en especial.

![La configuración de las notificaciones push configuradas para coincidir la
cantidad de registros en la base de datos.](../../../../_images/push-
notification-condition.png)

Para agregar una regla adicional, haga clic en el icono **➕ (signo de más)** a
la derecha de la regla.

Para agregar una rama (una serie de reglas adicionales según la regla previa
que especifican más la audiencia objetivo), haga clic en el **icono de rama**
, ubicado a la derecha del icono **➕ (más)**.

Por último, haga clic en el icono **🗑️ (basura)** para borrar cualquier regla.

Los **registros** debajo de las reglas representan el tamaño de la audiencia
específica de destinatarios.

## Página de publicaciones

Para obtener un resumen completo de las publicaciones, vaya a la aplicación de
Marketing social ‣ Publicaciones, aquí tendrá acceso a todas las publicaciones
que se han creado y publicado con Konvergo ERP.

Hay cuatro opciones de vista diferentes para los datos en la página
**Publicaciones sociales** : _kanban_ , _calendario_ , _lista_ y _gráfica
dinámica_.

Las opciones de vista se encuentran en la esquina superior derecha de la
página **Publicaciones** , abajo de la barra de búsqueda.

Kanban viewCalendar viewList viewPivot view

Konvergo ERP mostrará las publicaciones en la vista de kanban de forma predeterminada.
Puede clasificar con mayor detalle la información en esta página con ayuda de
la barra lateral, donde puede ver, acceder y analizar todas las redes sociales
y las publicaciones conectadas.

En la esquina superior derecha encontrará el **icono de barra de gráfica
invertida** , el cual representa la vista de kanban.

![Vista de kanban de la página de publicaciones en la aplicación Marketing
social de Konvergo ERP.](../../../../_images/posts-page-kanban.png)

La opción de vista de calendario muestra una representación visual de las
publicaciones en un formato de calendario de cuándo se realizaron, o están
programadas. Esta opción proporciona una vista general clara de cualquier día,
semana o mes planificado. Konvergo ERP muestra todas las publicaciones en borradores,
programadas y publicadas.

Si hace clic en una fecha se mostrará un formulario de detalles de
publicaciones en blanco en el que podrá crear la publicación social y Konvergo ERP la
publicará en la fecha y hora específicas.

En la esquina superior derecha encontrará el **icono de calendario** , el cual
representa la vista de calendario.

![Ejemplo de la vista de calendario en la aplicación de Marketing social de
Konvergo ERP.](../../../../_images/calendar-view.png)

La opción de vista de lista es parecida a la de kanban, pero en lugar de
bloques individuales, muestra toda la información de la publicación en un
diseño de lista más despejado. Cada línea de la lista muestra las **cuentas de
redes sociales** , el **mensaje** y el **estado** de cada publicación.

La barra lateral izquierda organiza todas las publicaciones por **Estado** y
también enlista todas las redes sociales conectadas.

En la esquina superior derecha hay cuatro líneas verticales que representan la
vista de lista.

![Vista de la opción de lista en la página de publicaciones en la aplicación
Marketing social de Konvergo ERP.](../../../../_images/list-view2.png)

La opción de vista de tabla dinámica proporciona una tabla de cuadrícula
personalizable en su totalidad, en ella puede agregar y analizar diferentes
medidas de datos.

![Vista de la opción de tabla dinámica en la página de publicaciones en la
aplicación Marketing social de Konvergo ERP.](../../../../_images/pivot-view.png)

La opción de vista de tabla dinámica proporciona varias opciones de análisis,
brindándole un análisis profundo y detallado de varias publicaciones y
métricas.

Haga clic en cualquier **ícono ➕ (signo de más)** junto a una línea en la
tabla dinámica para mostrar más opciones métricas que puede agregar a la
cuadrícula.

Mientras está en la vista de tabla dinámica, estará disponible la opción de
**Insertar en una hoja de cálculo** , que se encuentra a la derecha del menú
desplegable **Medidas** , en la esquina superior izquierda de la página
**Publicaciones sociales**.

Junto a la opción **Insertar en una hoja de cálculo** hay tres opciones
específicas de la vista de tabla dinámica.

Las opciones son, de izquierda a derecha:

  * **Voltear eje** , voltea los ejes _X_ e _Y_ en la tabla de cuadrícula.

  * **Expandir todo** , expande cada línea en la cuadrícula, mostrando más información detallada relacionada.

  * **Descargar** , al hacer clic, descarga de manera instantánea la tabla dinámica como una hoja de cálculo.

## Visitantes

Para ver un resumen completo de todas las personas que han visitado el sitio
web conectado a la base de datos, vaya a Marketing Social ‣ Visitantes.

![Vista de la página de visitantes en la aplicación Marketing Social de Konvergo ERP.
](../../../../_images/visitors.png)

Aquí, Konvergo ERP proporciona una página detallada de toda la información pertinente
de los visitantes en la vista predefinida Kanban. Si los visitantes ya tienen
información de contacto en la base de datos, tendrá disponible la opción para
enviarles un **correo** o **SMS**.

Los datos de este visitante también se pueden ver en forma de lista o de
gráfico. Estas opciones de vista se ubican en la esquina superior derecha de
la página **Visitantes**.

## Página de redes sociales

Otra forma de vincular redes sociales rápido a la aplicación _Marketing
social_ es desde la página **Redes sociales**. Para ingresar a esta página,
vaya a la aplicación Marketing social ‣ Configuración ‣ Redes sociales.

En la página **Redes sociales** tiene una gama de opciones de redes sociales,
cada una con un botón para **vincular la cuenta** : **Facebook** ,
**Instagram** , **LinkedIn** , **Twitter** , **YouTube** , y **Notificaciones
push**.

![Vista de la página de redes sociales en la aplicación de Marketing Social.
](../../../../_images/social-media-page.png)

## Página de cuentas de redes sociales

Para ver una lista de todas las cuentas de redes sociales y sitios web que
están vinculados a una base de datos, vaya a la aplicación de Marketing social
‣ Configuración ‣ Cuentas de red social. Estas **cuentas de redes sociales**
muestran el **nombre** , el **Nombre de usuario** , la plataforma de **redes
sociales** , quién **creó la cuenta** y la **empresa** a la que está asociada.

![Vista de la página de cuentas de redes sociales en la aplicación de
Marketing Social de Konvergo ERP. ](../../../../_images/social-accounts-page.png)

Para editar/modificar cualquier cuenta de redes sociales en esta página,
simplemente seleccione la cuenta deseada en la lista de esta página, y luego
haga los ajustes que crea necesarios.

## Página de flujos sociales

Para ver una página separada con todos los flujos de redes sociales que ha
agregado al tablero principal de _Marketing social_ , vaya a la aplicación de
Marketing social ‣ Configuración ‣ Flujos sociales.

![Vista de la página de cuentas de redes sociales en la aplicación de
Marketing Social de Konvergo ERP. ](../../../../_images/social-streams-page.png)

Aquí, la infromación del flujo social se organiza en una lista con las **Redes
sociales** , el **Título** del flujo, el **Tipo** (por ejemplo,
**Publicaciones** , **Palabra clave** , etc.), quién lo **creó** y la **la
empresa** a la que está asociada.

Para modificar la información de cualquier flujo, simplemente haga clic en el
flujo que desee de la lista y haga los ajustes que crea necesarios.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>La aplicación <em>Marketing social</em> tiene algunas limitaciones con respecto a las cuentas de redes sociales. Konvergo ERP <b>no puede</b> gestionar una cantidad grande de páginas distintas (por ejemplo, un aproximado de 40 páginas) en la misma empresa. Estas limitaciones también aplican en un entorno multiempresas, ya que están relacionadas con la forma en la que está construida la API.</p>
</div>2

