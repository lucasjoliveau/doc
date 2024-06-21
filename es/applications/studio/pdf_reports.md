# Reportes en PDF

Con Studio, puede editar reportes en PDF existentes (por ejemplo, órdenes y
cotizaciones) o crear nuevos.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Para editar un reporte PDF estándar, le recomendamos enfáticamente <b>duplicarlo</b> y hacer los cambios en la versión duplicada, puesto que los cambios hechos a los reportes estándar se sobreescriben después de una actualización de Konvergo ERP. Para duplicar un reporte, vaya a Studio ‣ Reportes. Coloque el cursor en la esquina superior derecha del reporte, haga clic en el ícono de la elipsis vertical (<b>⋮</b>), y seleccione <b>Duplicar</b>.</p>
<img alt="Duplicación de un reporte PDF" src="../../_images/duplicate-report.png"/>
</div>

## Diseño predeterminado

El diseño predeterminado de los reportes se maneja fuera de Studio. Vaya a
Ajustes ‣ Empresas: Diseño del documento ‣ Configruación del diseño del
documento. Los ajustes del diseño aplican a todos los reportes pero solo de la
empresa actual.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Use <b>Descargar la vista previa del PDF</b> para ver como los diferentes ajustes pueden alterar el diseño de una simple factura.</p>
</div>

### Diseño

Hay cuatro diseños disponibles.

LightBoxedBoldStriped

![Ejemplo del diseño de reporte Light](../../_images/light.png)

![Ejemplo del diseño de reporte Con tabla ](../../_images/boxed.png)

![Ejemplo del diseño del reporte en Negritas](../../_images/bold.png)

![Ejemplo del diseño de reporte Subrayado](../../_images/striped.png)

### Tipo de letra

Están disponibles siete tipos de letra. Haga clic en los enlaces a
continuación para obtener una vista previa en [Google
Fonts](https://fonts.google.com/).

  * [Lato](https://fonts.google.com/specimen/Lato#type-tester)

  * [Roboto](https://fonts.google.com/specimen/Roboto#type-tester)

  * [Open Sans](https://fonts.google.com/specimen/Open+Sans#type-tester)

  * [Montserrat](https://fonts.google.com/specimen/Montserrat#type-tester)

  * [Oswald](https://fonts.google.com/specimen/Oswald#type-tester)

  * [Raleway](https://fonts.google.com/specimen/Raleway#type-tester)

  * [Tajawal](https://fonts.google.com/specimen/Tajawal#type-tester)

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p><b>Tajawal</b> es compatible con caracteres latinos y árabes.</p>
</div>

### Logo de la empresa

Suba un archivo de imagen para agregar un **Logo de la empresa**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Esto agrega el logo al registro de la empresa en el modelo <em>Empresa</em>, al que puede acceder si va a Ajustes generales ‣ Empresas ‣ Actualizar información.</p>
</div>

### Colores

Cambie los colores primarios y secundarios que usa en los reportes para
resaltar elementos importantes. Los colores predeterminados se generan
automáticamente con base en los colores del logo.

### Diseño del fondo

Cambie el **Diseño del fondo** del reporte:

  * **En blanco** : no se muestra nada.

  * **Geometrico** : se muestra una imagen con figuras geométricas de fondo.

  * **Personalizado** : suba una imagen personalizada para usarla de fondo.

### Lema de la empresa

El **Lema de la empresa** se muestra en el encabezado de Reportes externos.
Puede agregar varias líneas de texto.

### Detalles de la empresa

Los **Detalles de la empresa** se muestran en el encabezado de Reportes
externos. Puede agregar varias líneas de texto.

### Pie de página

Use el campo **Pie de página** para poner texto en el pie de página de los
Reportes externos”. Puede agrergar varias líneas de texto.

### Formato de papel

Use el campo de **Formato de papel** para cambiar el tamaño del papel de los
repórtes. Puede seleccionar **A4** (21 cm x 29.7 cm) o **Carta US** (21.59 cm
x 27.54 cm).

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Puede cambiar el <b>Formato del papel</b> en los reportes individuales. Abra la aplicación que contiene el reporte, luego vaya a Studio ‣ Reportes ‣ Seleccione o cree un reporte ‣ Reporte ‣ Seleccione un formato de papel.</p>
</div> ![Ventana emergente de configuración para el diseño
predeterminado de los reportes en PDF](../../_images/default-layout.png)

## Encabezado y pie de página

Al crear un reporte nuevo en Studio, primero debe elegir uno de entre tres
estilos de reporte. Esto se usa para determinar qué encabezado y pie de página
se mostrará. Para hacerlo, vaya a la aplicación en dónde quiere agregar un
nuevo reporte, luego al Botón de Studio ‣ Reportes ‣ Crear y seleccione
Externo, Interno o Vacío.

### Externo

El encabezado muestra el Logo de la empresa y varios valores establecidos en
el modelo _Empresa_ : el **Nombre de la empresa** , **Teléfono** , **Corre
electrónico** y **Sitio web**.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para cambiar la información de la empresa, vaya a Ajustes ‣ Empresas ‣ Actualizar información.</p>
</div> ![Ejemplo de un encabezado
externo](../../_images/external-header.png)

El pie de página muestra los valores establecidos en los campos para Pie de
página, Detalles de la empresa y Lema de la empresa, así como el número de
página.

![Ejemplo de pie de página externo](../../_images/external-footer.png)

### Interno

El encabezado muestra la fecha y hora actuales del usuario, el **nombre de la
empresa** y el número de página.

No hay pie de página.

### Vacío

No hay ni un encabezado ni un pie de página.

## Agregar una pestaña

Después de abrir un reporte existente o crear uno nuevo, vaya a la pestaña
**Agregar** para agregar o editar elementos. Los elementos están organizados
en cuatro categorías Bloque, Inline, Mesa y Columna.

### Bloque

Los elementos de bloque inician en una nueva línea y ocupan todo el ancho de
la página.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para establecer el ancho de un elemento selecciónelo y luego vaya a la pestaña <b>Opciones</b>.</p>
</div>

  * **Texto** : agregue cualquier texto, de forma predeterminada se usa un tamaño de fuente pequeño.

  * **Bloque de título** : agregue cualquier texto, de forma predeterminada se usa un tamaño de fuente más grande.

  * **Imagen** : agregue una imagen desde su dispositivo, desde una URL o seleccione una ya existente en su base de datos.

  * **Campo** : agregue el valor de un campo de forma dinámica.

  * **Campo y etiqueta** : agregue el valor y la etiqueta de un campo de forma dinámica.

  * **Bloque de dirección** : agregue de forma dinámica los valores, si los hay, de un contacto (modelo `res.partner`): _Nombre_ , _dirección_ , _teléfono_ , _móvil_ y _correo electrónico_.

![Ejemplo de un bloque de direcciones](../../_images/address-block.png)

### Inline

Los elementos en línea se utilizan alrededor de otros elementos, no inician en
una nueva línea y su ancho se adapta a la longitud del contenido.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para establecer el ancho y los márgenes de un elemento selecciónelo y luego vaya a la pestaña <b>Opciones</b>.</p>
</div>

  * **Texto** : agregue cualquier texto, de forma predeterminada se usa un tamaño de fuente pequeño.

  * **Campo** : agregue el valor de un campo de forma dinámica.

### Mesa

Los elementos de tabla se usan de forma conjunta para crear una tabla de
datos.

  * **Tabla de datos** : cree una tabla y, de forma dinámica, agregue una primera columna que muestre los valores del _nombre_ de los campos [Many2Many](fields#studio-fields-relational-fields-many2many) o [One2Many](fields#studio-fields-relational-fields-one2many) en su modelo.

![Ejemplo de una tabla de datos](../../_images/data-table.png)

  * **Columna de campo** : agregue una nueva columna a la tabla que muestra los valores de un [Campo relacionado](fields#studio-fields-relational-fields-related-field) al que se usa para crear la **Tabla de datos**.

  * **Texto en la celda** : agregue cualquier texto dentro de una celda de tabla existente.

  * **Campo en la celda** : agregue, dentro de la celda de una tabla existente, los valores de un [Campo relacionado](fields#studio-fields-relational-fields-related-field) al que se usa para crear la **Tabla de datos**.

  * **Subtotal y total** : agregue un valor de campo **Total** existente. Si existe un campo de **Impuestos** , las cantidades con y sin impuestos se agregan antes de la cantidad total.

### Columna

Las columnas se utilizan para agregar varios elementos de bloque en la misma
línea.

  * **Dos columnas** : agregue cualquier texto en dos columnas diferentes.

  * **Tres columnas** : agregue cualquier texto en tres columnas diferentes.

## Pestaña de reporte

En la pestaña **Reporte** están disponibles varias opciones de configuración.

  * **Nombre** : cambie el nombre del reporte. El nuevo nombre se cambia en todos lados (en Studio, en el botón **Imprimir** y para el nombre del archivo PDF).

  * **Formato del papel** : cambie el tamaño del papel del reporte.

  * **Agergar para imprimir** : agregue el reporte en el botón **🖶 Imprimir** que está disponible en el registro.

  * **Visibilidad limitada a los grupos** : limíte la disponibilidad del reporte en PDF a [grupos de usuarios](../general/users/access_rights) específicos.

## Pestaña de opciones

Seleccione un elemento en el reporte para acceder a sus opciones y editarlo.

![La pestaña Opciones para un elemento de texto](../../_images/text-options-
tab.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Puede seleccionar y editar varios elementos al mismo tiempo haciendo clic en las diferentes secciones o divisiones (por ejemplo, <code>div</code>, <code>table</code>, etc.).</p>
</div>

A continuación están algunas de las opciones más comunes:

  * **Márgenes** : agregue un espaciado en la parte **superior** , **derecha** , **inferior** e **izquierda** del elemento.

  * **Ancho** : establezca el ancho máximo del elemento.

  * **Visible si** : establezca bajo que condición(es) se debe mostrar el elemento.

  * **Visible para** : establezca para qué [grupos de usuarios](../general/users/access_rights) se debe mostrar el elemento.

  * **Quitar de la vista** : quitar el elemento de la vista del reporte.

  * **Decoración del texto** : ponga la fuente en negrita, cursiva o subráyela.

  * **Alineación** : alinee el elemento a la izquierda, al centro o a la derecha del reporte.

  * **Estilo de fuente** : use uno de los estilos de fuente predefinidos.

  * **Colores** : cambie el color de la fuente y el color del fondo.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Es posible que necesite seleccionar una sección o división sobre el elemento que desea editar para ver algunas de las opciones descritas anteriormente.</p>
</div>

