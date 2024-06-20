# Utilizar actividades para los equipos de ventas

Las _actividades_ son tareas de seguimiento vinculadas a un registro en una
base de datos de _Odoo_. Estas se pueden programar desde cualquier página de
la base de datos que tenga un hilo del chatter, una vista de kanban, una vista
de lista o una vista de actividades de una aplicación.

![Información general de las actividades para leads y oportunidades en una
base de datos de Odoo.](../../../../_images/activities-view.png)

Actividades planificadas para leads y oportunidades.

## Tipos de actividades

La aplicación _CRM_ cuenta con un varios tipos de actividad preconfigurados,
para ver la lista vaya a CRM ‣ Configuración ‣ Tipos de actividad.

Nota

Hay otros tipos de actividad disponibles en la base de datos y puede
utilizarlos en diferentes aplicaciones. Para acceder a la lista completa de
tipos de actividad, vaya a Ajustes, diríjase a la sección Conversaciones y
haga clic en Tipos de actividad.

Los tipos de actividad preconfigurados para la aplicación _CRM_ son los
siguientes:

>   * Correo electrónico: agrega un recordatorio al chatter para indicarle al
> vendedor que debe enviar un correo electrónico.
>
>   * Llamada: abre un enlace de calendario donde el vendedor puede programar
> una hora para llamar al contacto.
>
>   * Reunión: abre un enlace de calendario donde el vendedor puede programar
> una hora para reunirse con el contacto.
>
>   * Por hacer: agrega una tarea de recordatorio general al chatter.
>
>   * Subir documento: agrega un enlace en la actividad donde es posible subir
> un documento externo. Tenga en cuenta que la aplicación _Documentos_ **no**
> es necesaria para utilizar este tipo de actividad.
>
>

Nota

Si instala otras aplicaciones, como _Ventas_ o _Contabilidad_ , habrá otros
tipos de actividad disponibles en la aplicación _CRM_.

### Crear un nuevo tipo de actividad

Para crear un nuevo tipo de actividad haga clic en el botón Nuevo ubicado en
la parte superior izquierda de la página, esta acción abrirá un formulario
vacío.

Primero, en la parte superior del formulario, elija un nombre para el nuevo
tipo de actividad.

#### Ajustes de actividad

##### Acción

El campo _Acción_ especifica el propósito de la actividad. Algunas acciones
activarán comportamientos específicos después de programar una actividad.

  * Si selecciona Subir documento. se agregará un enlace para subir un documento directamente a la actividad planeada en el chatter.

  * Si selecciona Llamada o Junta los usuarios tendrán la opción de abrir su calendario para agendar esta actividad.

  * Si selecciona Solicitar firma se agregará un enlace en el chatter de la actividad planeada. Al hacer clic en este enlace se abrirá una ventana emergente para solicitar la firma.

![Los ajustes de la actividad de un nuevo tipo de actividad. El campo Acción
aparece dentro de un recuadro rojo.](../../../../_images/action-field.png)

Nota

Las acciones disponibles que puede seleccionar en el tipo de actividad varían
dependiendo de las aplicaciones que tienen en la base de datos.

##### Usuario predeterminado

Para asignar esta actividad a un usuario específico de manera automática al
programar este tipo de actividad, seleccione un nombre desde el menú
desplegable Usuario predeterminado. Si este campo se deja en blanco, se
asignará una actividad al usuario que cree la actividad.

##### Resumen predeterminado

Para incluir notas al crear este tipo de actividad debe ingresarlas en el
campo Resumen predeterminado.

Nota

La información en los campos Usuario predeterminado y Resumen predeterminado
se incluye en la actividad creada. Sin embargo, se pueden alterar antes de que
la actividad se programe o se guarde.

#### Siguiente actividad

Para sugerir o activar una actividad de manera automática después de que una
actividad se marca como completada, se debe configurar el Tipo de
encadenamiento.

##### Sugerir la siguiente actividad

En el campo Tipo de encadenamiento seleccione Sugerir siguiente actividad. Al
hacerlo, el campo de abajo cambiará a Sugerir. Haga clic en este campo para
seleccionar las actividades que recomienda como actividades que le sigan a
este tipo de actividad.

![La sección Siguiente actividad en un formulario de nuevo tipo de
actividad.](../../../../_images/next-activity.png)

En el campo Horario seleccione una fecha límite predeterminada para estas
actividades. Para hacerlo, configure un número específico de Días, Semanas, o
Meses. Después, decida si debe pasar después de la fecha de finalización o
después de la fecha límite de actividad anterior.

Puede alterar la información del campo Horario antes de agendar la actividad.

Al completar todas las configuraciones, haga clic en Guardar.

Nota

Si una actividad tiene el Tipo de encadenamiento configurado como Sugerir
siguiente actividad y tiene actividades enlistadas en el campo Sugerir, los
usuarios obtendrán recomendaciones de actividades que pueden ser el siguiente
paso.

![Una ventana emergente de actividades programadas. Las actividades
recomendadas aparecen dentro de un recuadro
rojo.](../../../../_images/suggest-next-activity.png)

##### Activar la siguiente actividad

Si configura el Tipo de encadenamiento a Activar siguiente actividad hara que
la siguiente actividad se active de inmediato una vez que la actividad previa
se termine.

Si selecciona Activar la siguiente actividad en el campo Tipo de
encadenamiento, el campo de abajo cambiará a Activador. Desde el menú
desplegable del campo Activador seleccione la actividad que se debería iniciar
una vez que esta actividad se complete.

En el campo Horario seleccione una fecha límite predeterminada para estas
actividades. Para hacerlo, configure un número específico de Días, Semanas, o
Meses. Después, decida si debe pasar después de la fecha de finalización o
después de la fecha límite de actividad anterior.

Puede alterar la información del campo Horario antes de agendar la actividad.

Al completar todas las configuraciones, haga clic en Guardar.

Nota

Cuando el tipo de encadenamiento de una actividad es Activar la siguiente
actividad, al marcar la actividad como _Lista_ , la siguiente actividad que
aparece en el campo Activar iniciará de inmediato.

## Seguimiento de actividades

Para mantener el flujo actualizado con la vista más precisa del estado de las
actividades, tan pronto como se interactúe con un lead, es necesario que
marque la actividad asociada como _Hecho_. Esto garantiza que pueda programar
la siguiente actividad según sea necesario y también evita que el flujo se
sature con actividades vencidas.

El flujo es más efectivo cuando está actualizado y en orden con las
interacciones que está rastreando.

## Planes de actividades

Los tipos de actividad con el _tipo de encadenamiento_ configurado como
_Activar la nueva actividad_ permiten planificar con anticipación una
secuencia de actividades personalizadas. Una vez que una actividad se marca
como _Hecho_ , la siguiente actividad se programa de forma automática.

La función _tipo de encadenamiento_ de un tipo de actividad permite preparar
una secuencia de eventos que pueden ser útiles en el proceso de ventas.

Example

Un vendedor agrega un nuevo lead a su flujo y programa una actividad de tipo
_Correo electrónico_ para el día siguiente. Este tipo de actividad de correo
electrónico está configurado con los siguientes ajustes:

  * Tipo de encadenamiento: `Sugerir siguiente actividad`

  * Sugerir: `Llamada`, `Reunión`

  * Programar: `2 días después de la fecha límite de la actividad anterior`

Después de enviar un correo electrónico al lead, el vendedor hace clic en
¡Hecho! Prepare el siguiente en la ventana emergente de Programar pctividad.
Esto abre una nueva ventana emergente donde aparecen las actividades sugeridas
como recomendaciones para los siguientes pasos.

![Ventana emergente para programar una actividad con las actividades
recomendadas.](../../../../_images/recommended-activities.png)

Las actividades _sugeridas_ o _activadas_ pueden variar según distintos
factores. Consulte los siguientes ejemplos relacionados con algunas
secuencias:

Sample #1Sample #2Sample #3

  * Un vendedor agrega un lead al flujo y programa una actividad de tipo _Correo electrónico_.

  * La actividad _Correo electrónico_ sugiere programar una _llamada_ o una _reunión_ dentro de los dos días de la fecha límite anterior.

  * Las actividades _Llamada_ y _Reunión_ activan la actividad _Crear cotización_.

  * Después de enviar la cotización, la actividad _Seguimiento a la cotización_ se programa para después de cinco días.

  * Un lead se [agrega al flujo](../acquire_leads/generate_leads.html) a través del formulario de contacto del sitio web. El gerente de ventas asigna un vendedor y programa una actividad para una _llamada_.

  * La actividad _Llamada_ activa la actividad _Subir documento_ para que el vendedor pueda enviar la propuesta después de la llamada.

  * La actividad de tipo _Subir documento_ sugiere programar la actividad _Solicitar firma_ o una _reunión_ y el vendedor elige agendar una reunión.

  * Un gerente se da cuenta de que sus vendedores no le están proporcionando el seguimiento adecuado a sus leads y, como resultado, están perdiendo varios clientes valiosos.

  * El gerente crea un nuevo tipo de actividad con el nombre _Seguimiento_ y lo configura con Recordatorio como tipo de Acción.

  * El gerente hace que _Seguimiento_ sea la siguiente actividad activada o sugerida para todas las actividades de su equipo.

  * Después de que un vendedor planifique una actividad de _correo electrónico_ , se programa una actividad de _seguimiento_ para el día siguiente. Después de que programe una actividad de _reunión_ , se programa una actividad de _seguimiento_ para dos días después.

Ver también

  * [Actividades](../../../essentials/activities.html)

