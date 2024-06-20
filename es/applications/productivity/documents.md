# Documentos

La aplicación **Documentos de Odoo** le permite almacenar, ver y gestionar
archivos dentro de Odoo.

Puede subir cualquier tipo de archivo (máximo 64 MB por archivo en Odoo en
línea) y organizarlos en varios espacios de trabajo.

Ver también

  * [Documentos de Odoo: página de producto](https://www.odoo.com/app/documents)

  * [Tutoriales de Odoo: fundamentos de Documentos](https://www.odoo.com/slides/slide/documents-basics-674)

  * [Tutoriales de Odoo: utilizar Documentos con su aplicación Contabilidad](https://www.odoo.com/slides/slide/using-documents-with-your-accounting-app-675?fullscreen=1#)

## Configuración

En Documentos ‣ Configuración ‣ Ajustes puede habilitar la centralización de
archivos adjuntos a un área específica de su actividad. Por ejemplo, si
selecciona recursos humanos, sus documentos de RR. HH. están disponibles de
forma automática en el espacio de trabajo de RR. HH., mientras que los
documentos relacionados con la nómina están disponibles de forma automática en
el subespacio de trabajo de nómina. Puede cambiar el espacio de trabajo
predeterminado al abrir el menú desplegable y editar sus propiedades al hacer
clic en el botón de enlace interno (➔).

![Habilitar la centralización de archivos adjuntos a un área específica de su
actividad.](../../_images/files-centralization.png)

Nota

  * tSi habilita la centralización de sus archivos y documentos contables, debe hacer clic en diarios y definir cada diario de forma independiente para facilitar la sincronización automática.

![Habilitar la centralización de archivos adjuntos en su
contabilidad.](../../_images/accounting-files-centralization.png)

  * Si selecciona un nuevo espacio de trabajo, los documentos existentes no se moverán. Solo los nuevos documentos que cree estarán en el nuevo espacio de trabajo.

## Espacios de trabajo

Los espacios de trabajo son carpetas jerárquicas que tienen su propio conjunto
de etiquetas y acciones. Hay espacios de trabajo predeterminados, pero puede
crear los suyos al ir a Documentos ‣ Configuración ‣ Espacios de trabajo y
hacer clic en crear.

Nota

Puede crear, editar o eliminar espacios y subespacios de trabajo al hacer clic
en el icono de engrane ⚙ en el menú que se encuentra a la izquierda.

![Crear subespacios de trabajo en el menú a la izquierda](../../_images/sub-
workspaces-creation.png)

## Etiquetas

Puede utilizar etiquetas en los espacios de trabajo para agregar un nivel de
diferenciación entre sus documentos. Se organizan por categoría y puede
utilizar filtros para organizarlos.

Nota

  * Las etiquetas de un espacio padre se aplican a los espacios de trabajo hijos de forma automática.

  * Puede crear y modificar etiquetas en Configuración ‣ Etiquetas.

  * Puede crear, editar o eliminar etiquetas al hacer clic en el icono de engrane ⚙, en el menú que se encuentra a la izquierda.

## Gestión de documentos

Al hacer clic en un documento específico, el panel a la derecha muestra
distintas opciones. En la parte superior pueden aparecer opciones adicionales:
descargar, compartir, remplazar, bloquear o dividir. También es posible abrir
el chatter o archivar el documento.

![Opciones en el panel a la derecha](../../_images/right-panel-options.png)

Posteriormente, puede modificar el nombre de su archivo al hacer clic en un
documento. Se puede asignar un contacto o un propietario. Se puede modificar
el espacio de trabajo y es posible acceder al asiento contable correspondiente
o agregar etiquetas.

Nota

  * El contacto es la persona relacionada con el documento y que se asignó a él. Solo puede ver el documento y no modificarlo. Por ejemplo: un proveedor en su base de datos es el contacto para su factura de proveedor.

  * De forma predeterminada, la persona que crea un documento es su propietario y tiene todos los derechos de acceso a él. Es posible cambiar el propietario de un documento. El empleado debe ser propietario del documento para que lo pueda ver en su página «mi perfil».

Por último, hay distintas acciones disponibles en la parte inferior del panel
a la derecha, dependiendo del espacio de trabajo donde almacena su documento.

## Acciones de flujo de trabajo

Las acciones de flujo de trabajo le ayudan a agilizar la gestión de sus
documentos y sus operaciones empresariales generales. Son acciones
automatizadas que puede crear y personalizar para cada espacio de trabajo. Por
ejemplo, crear documentos, procesar facturas, firmar, organizar archivos,
agregar etiquetas a un archivo o moverlo a otro espacio de trabajo con solo un
clic, entre otras. Las acciones de flujo de trabajo aparecen en el panel a la
derecha cuando se cumple con los criterios establecidos.

### Crear acciones de flujo de trabajo

Para crear acciones de flujo de trabajo, vaya a Documentos ‣ Configuración ‣
Acciones y luego haga clic en crear.

Nota

Una acción se aplica a todos los espacios de trabajo hijos del espacio de
trabajo padre seleccionado.

### Establecer las condiciones

Puede crear una nueva acción o editar una existente. Puede definir el nombre
de la acción y luego establecer las condiciones que hace que aparezca el botón
de acción (▶) en el panel que se ubica a la derecha cuando selecciona un
archivo.

Hay tres tipos principales de condiciones que puede establecer:

  1. Etiquetas: puede utilizar las condiciones contiene y no contiene, lo que significa que los archivos _deben tener o *no deben tener_ las etiquetas establecidas aquí.

  2. Contacto: los archivos deben estar vinculados al contacto establecido aquí.

  3. Propietario: los archivos deben estar vinculados al propietario establecido aquí.

![Ejemplo de una condición básica de acción de flujo de trabajo en la
aplicación Documentos de Odoo](../../_images/basic-condition-example.png)

Truco

Si no establece ninguna condición, el botón «acción» aparece para todos los
archivos dentro del espacio de trabajo seleccionado.

#### Tipo de condición avanzada: dominio

Importante

Se recomienda tener conocimiento sobre el desarrollo de Odoo para configurar
correctamente los filtros de _dominio_.

Para acceder a la condición _dominio_ , debe activar el [modo de
desarrollador](../general/developer_mode.html#developer-mode). Una vez hecho
esto, seleccione el tipo de condición dominio y haga clic en agregar filtro.

![Activar el tipo de condición "dominio" en la aplicación Documentos de
Odoo](../../_images/activate-domain-condition.png)

Para crear una regla, normalmente se selecciona un campo, un operador y un
valor. Por ejemplo, si desea agregar una acción de flujo de trabajo a todos
los archivos PDF en un espacio de trabajo, establezca el campo como _tipo de
medio_ , el operador como _contiene_ y el valor como _PDF_.

![Ejemplo de una condición de dominio de acción de flujo de trabajo en la
aplicación Documentos de Odoo](../../_images/domain-condition-example.png)

Haga clic en agregar nodo (icono de círculo con signo de más) y agregar rama
(icono de la elipsis) para aregar condiciones y subcondiciones. Después podrá
especificar si su regla debe coincidir con TODAS o NINGUNA de las condiciones.
También puede editar la regla directamente mediante el editor de código.

![Agregar un nodo o una rama a una condición de acción de flujo de trabajo en
la aplicación Documentos de Odoo](../../_images/use-domain-condition.png)

### Configurar las acciones

Seleccione la pestaña acciones para configurar su acción. Puede hacerlo
simultáneamente:

  * **Establecer contacto** : agrega un contacto al archivo, o remplaza un contacto existente por uno nuevo.

  * **Establecer propietario** : agrega un propietario al archivo, o remplaza un propietario existente por uno nuevo.

  * **Mover al espacio de trabajo** : mueve el archivo a cualquier espacio de trabajo.

  * **Crear** : crea uno de los siguientes elementos vinculados al archivo en su base de datos:

>     * **Plantilla de producto** : crea un producto que puede editar
> directamente.
>
>     * **Tarea** : crea una tarea del proyecto que puede editar directamente.
>
>     * **Solicitud de firma** : crea una nueva plantilla de firma para
> enviar.
>
>     * **Firmar directamente** : crea una plantilla de firma que se puede
> firmar directamente.
>
>     * **Factura de proveedor** : crea una factura de proveedor mediante OCR
> e IA para extraer información del contenido del archivo.
>
>     * **Factura de cliente** : crea una factura de cliente mediante OCR e IA
> para extraer la información del archivo.
>
>     * **Nota de crédito de proveedor** : crea una nota de crédito de
> proveedor mediante OCR e IA para extraer información del archivo.
>
>     * **Nota de crédito** : crea una nota de crédito de cliente mediante OCR
> e IA para extraer información del archivo.
>
>     * **Candidato** : crea una nueva solicitud de RR. HH. que puede editar
> directamente.

  * **Establecer etiquetas** : agrega, elimina y reemplaza cualquier número de etiquetas.

  * **Actividades - Marcar todas como hechas** : marca todas las actividades vinculadas al archivo como hechas.

  * **Actividades - Programar actividad** : crea una nueva actividad vinculada al archivo según la configuración de la acción. Puede optar por establecer la actividad en el propietario del documento.

![Ejemplo de una acción de flujo de trabajo en la aplicación Documentos
Odoo](../../_images/workflow-action-example.png)

## Digitalizar documentos con IA y reconocimiento óptico de caracteres (OCR)

Puede digitalizar los documentos disponibles en el espacio de trabajo de
finanzas. Seleccione el documento que desea digitalizar, haga clic en crear
factura de proveedor, crear factura de cliente o crear nota de crédito y luego
haga clic en enviar para digitalización.

Ver también

[Digitalización de documentos con tecnología de
IA](../finance/accounting/vendor_bills/invoice_digitization.html)

