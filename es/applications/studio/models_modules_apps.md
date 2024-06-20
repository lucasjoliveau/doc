# Modelos, módulos y aplicaciones

Los modelos determinan la estructura lógica de una base de datos y cómo se
almacenan, organizan y manipulan los datos. En otras palabras, un modelo es
una tabla de información que se puede vincular con otras tablas. Un modelo
suele representar un concepto empresarial, como una _orden de venta_ , un
_contacto_ o un _producto_.

Los módulos y las aplicaciones contienen varios elementos, como modelos,
vistas, archivos de datos, controladores web y datos web estáticos.

Nota

Todas las aplicaciones son módulos. Los módulos más grandes e independientes
suelen denominarse aplicaciones, mientras que otros módulos suelen ser
complementos de dichas aplicaciones.

## Funciones sugeridas

Cuando se crea un nuevo modelo o aplicación con Studio, se puede optar por
añadir hasta 14 funciones que permitan acelerar el proceso de creación. Estas
características agrupan campos, configuraciones predeterminadas y vistas que
suelen utilizarse en conjunto para proporcionar cierta funcionalidad estándar.
La mayoría de estas funciones se pueden añadir después, pero añadirlas desde
el principio facilita mucho el proceso de creación del modelo. Además, en
algunos casos, estas funciones interactúan entre sí para aumentar su utilidad.

Example

La creación de un modelo con las funciones Foto y Etapas del flujo activadas
añade la imagen en el diseño de la tarjeta de la vista
[Kanban](views.html#studio-views-multiple-records-kanban).

![Combinación de las funciones de las etapas imagen y flujo en la vista
kanban](../../_images/picture-pipeline-kanban.png)

### Detalles de contacto

Si selecciona detalles del contacto se añadirá un campo [Many2One
field](fields.html#studio-fields-relational-fields-many2one) a la [vista de
formulario](views.html#studio-views-general-form) vinculada al modelo
_Contacto_ y dos de sus [Campos de relación](fields.html#studio-fields-
relational-fields-related-field): Teléfono y Correo electrónico. El campo
Contacto también se añade a la [vista de lista](views.html#studio-views-
multiple-records-list), y se activa la [vista de mapa](views.html#studio-
views-multiple-records-map).

Example

![Función de datos de contacto en la vista de
formulario](../../_images/contact1.png)

### Asignación de usuario

Si selecciona Asignación de usuario se añadirá un campo [Many2One
field](fields.html#studio-fields-relational-fields-many2one) a la [vista de
formulario](views.html#studio-views-general-form) que estará vinculado al
modelo _Contacto_ con el siguiente Dominio: `No se ha establecido un usuario
externo al cual compartir` lo que permitirá la selección exclusiva de
_usuarios internos_. Además, el widget many2one_avatar_user se usa para
mostrar el avatar del usuario. The Responsible field is also added to the
[List view](views.html#studio-views-multiple-records-list).

Example

![Función asignación de usuarios en la vista de
formulario](../../_images/user-assignment.png)

### Fecha y calendario

Si selecciona Fecha y Calendario agrega un campo de
[Fecha](fields.html#studio-fields-simple-fields-date) en el [formulario de
vista](views.html#studio-views-general-form) y activa la [vista de
calendario](views.html#studio-views-timeline-calendar).

### Rango de fechas y Gantt

Si selecciona Rango de fechas y Gantt se añadirán dos campos de
[Fecha](fields.html#studio-fields-simple-fields-date) en la [Vista de
formulario](views.html#studio-views-general-form) uno para establecer una
fecha de inicio y otro para establecer una fecha de finalización, por medio
del widget daterange. También se activará la vista de
[Gantt](views.html#studio-views-timeline-gantt).

### Etapas del flujo

Si selecciona Etapas del flujo, se activará la vista de Kanban, se añadirán
varios campos como [Prioridad](fields.html#studio-fields-simple-fields-
priority) y Estado Kanban, y tres etapas: Nuevo, En curso y Hecho. Se añaden
los campos Barra de estado del flujo y Estado de Kanban a la vista de
[Formulario](views.html#studio-views-general-form). También se añadirá el
campo de Color a la vista de Lista.

Nota

Se puede añadir la función Etapas del flujo después.

### Etiquetas

Si selecciona Etiquetas se añadirá un campo de [Etiquetas](fields.html#studio-
fields-relational-fields-tags) a las vistas de [Formulario](views.html#studio-
views-general-form) y [Lista](views.html#studio-views-multiple-records-list).
Esto creará un modelo de _etiquetas_ con derechos de acceso preconfigurados.

### Foto

Si selecciona Imagen se añadirá un [campo de Imagen](fields.html#studio-
fields-simple-fields-image) en la parte superior derecha de la [vista de
formulario](views.html#studio-views-general-form).

Nota

Se puede añadir la función Imagen después.

### Líneas

Si selecciona Líneas: se añadirá un campo de [Líneas](fields.html#studio-
fields-relational-fields-lines) dentro de una Pestaña en la vista de
[Formulario](views.html#studio-views-general-form)

### Notas

Si selecciona Notas se añadirá un campo [Html](fields.html#studio-fields-
simple-fields-html) a la vista de [Formulario](views.html#studio-views-
general-form) que utilizará todo el ancho del formulario.

### Valor monetario

Si selecciona Valor monetario se añadirá un campo
[monetario](fields.html#studio-fields-relational-fields-tags) a las vistas de
[Formulario](views.html#studio-views-general-form) y
[Lista](views.html#studio-views-multiple-records-list). También se activarán
las vistas de [Gráfico](views.html#studio-views-reporting-graph) y
[Pivote](views.html#studio-views-reporting-pivot)

Nota

Se añade y oculta un campo de _Divisa_ de la vista.

### Empresa

Si selecciona Empresa se añadirá un campo [Many2One](fields.html#studio-
fields-relational-fields-many2one) vinculado al modelo de _Empresa_ a las
vistas de [Formulario](views.html#studio-views-general-form) y
[Lista](views.html#studio-views-multiple-records-list).

Nota

Esto solo es útil en un entorno multiempresa.

### Orden Personalizado

Si selecciona Orden personalizado se añadirá un icono de arrastre que le
permitirá ordenar de forma manual los registros en la vista de
[Lista](views.html#studio-views-multiple-records-list).

Example

![Función de orden personalizado en la vista de lista](../../_images/list-
drag-handle.png)

### Chatter

Si selecciona Chatter se añadirán las funciones de Chatter (envío de mensajes,
registro de notas y programación de actividades) a la vista de
[Formulario](views.html#studio-views-general-form).

Nota

Se puede añadir la función Chatter después.

Example

![Función de chatter en la vista de formulario](../../_images/chatter1.png)

### Archivando

Si selecciona Archivando, se añadirá la acción Archivando a las vistas
[Formulario](views.html#studio-views-general-form) y
[Lista](views.html#studio-views-multiple-records-list). Esto hará que se
oculten los registros archivados de las búsquedas y vistas de manera
predeterminada.

## Exportar e importar personalizaciones

Cuando se realiza una personalización con Studio, se añade un nuevo módulo
llamado Personalizaciones de Studio a la base de datos.

Si desea exportar estas personalizaciones, vaya al Tablero principal ‣ Studio
‣ Personalizaciones ‣ Exportar. Ahí podrá descargar un archivo ZIP con todas
las personalizaciones.

Para importar e instalar estas personalizaciones en otra base de datos, debe
conectarse a la base de datos destino e ir al Tablero principal ‣ Studio ‣
Personalizaciones ‣ Importar. Ahí podrá subir el archivo ZIP exportado,
después haga clic en el botón Importar.

Advertencia

Antes de importar, asegúrese de que la base de datos de destino contenga las
mismas aplicaciones y módulos que la base de datos de origen. Studio no se
encargará de añadir los módulos subyacentes como dependencias del módulo
exportado.

