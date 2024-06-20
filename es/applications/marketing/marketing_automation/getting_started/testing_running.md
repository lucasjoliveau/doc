# Probar y ejecutar campañas

La aplicación _Automatización de marketing_ de Odoo permite que los usuarios
prueben las campañas de marketing (y el envío de correos) antes de lanzarlos
de forma oficial para buscar errores y corregirlos antes de que lleguen a su
público objetivo.

## Probar campañas

Para probar una campaña de marketing, abra la aplicación Automatización de
marketing y seleccione la campaña que desea probar. Se abrirá el formulario de
detalles de dicha campaña.

En el formulario de detalles de la campaña, asegúrese de que la campaña ya
tenga actividades configuradas en el flujo de trabajo (o cree una campaña
siguiendo las instrucciones de [esta
documentación](workflow_activities.html)).

Nota

Debe utilizar la versión de producción de su base de datos para realizar las
pruebas de sus campañas de automatización de marketing. Las bases de datos
duplicadas (o de prueba) tienen capacidades muy limitadas para enviar correos
electrónicos.

Para comenzar una prueba, haga clic en el botón correspondiente que se
encuentra en la parte superior del formulario de la campaña, del lado derecho
del botón Iniciar.

![Botón para comenzar una prueba en un formulario de detaññes de una campaña
en la aplicación Automatización de marketing de
Odoo.](../../../../_images/launch-test.png)

Al hacer clic sobre él, aparecerá una ventana emergente para comenzar una
prueba.

![Ventana emergente para comenzar una prueba en Automatización de marketing de
Odoo. ](../../../../_images/launch-test-popup-window.png)

En la ventana emergente para comenzar una prueba, haga clic en el campo Elegir
o crear un contacto para generar un participante de prueba y aparecerá un menú
desplegable de contactos. Desde aquí, seleccione un contacto ya existente (o
cree uno nuevo) para comenzar la prueba.

Nota

Solo puede seleccionar un contacto en la ventana emergente comenzar una
prueba.

Para crear un nuevo contacto directamente desde la ventana emergente comenzar
una prueba, escriba el nombre del nuevo contacto en el campo en blanco y haga
clic en Crear y editar….

![Creación de un nuevo contacto directamente desde la ventana emergente para
comenzar una prueba en Odoo. ](../../../../_images/new-contact-from-launch-
test-popup.png)

Al hacerlo, se abrirá un formulario emergente en blanco para crear un
registro, en donde _deberá_ escribir información de contacto (correo
electrónico, celular, etc.) para que la prueba funcione. Cuando termine, haga
clic en Guardar y cerrar.

![Un formulario de contacto en blanco de una ventana emergente para comenzar
una prueba en Automatización de marketing en Odoo.](../../../../_images/blank-
contact-form.png)

Cuando estén completos todos los campos, haga clic en Guardar y cerrar para
regresar a la ventana emergente para comenzar una prueba.

Una que haya seleccionado un contacto, haga clic en Iniciar para abrir la
página de prueba de la campaña.

![Pantalla de prueba en la aplicación Automatización de marketing de
Odoo.](../../../../_images/test-screen.png)

En la página de prueba de la campaña podrá ver el nombre del registro en el
que se realiza la prueba, junto con la hora exacta en la que inició el flujo
de trabajo de prueba en el campo con el nombre El flujo de trabajo comenzó el.
Abajo, en la sección Flujo de trabajo, se encuentran las primeras actividades
que se encuentran a prueba.

Para iniciar una prueba, haga clic en el botón ejecutar, este se representa
con el icono ▶️ (botón de reproducir) junto a la primera actividad del flujo
de trabajo. Al hacer clic en él, la página volverá a cargar y Odoo le mostrará
los varios resultados (y datos analíticos) relacionados con esa actividad en
específico a medida que ocurren en tiempo real.

Nota

Si una actividad subordinada está programada debajo de una actividad
principal, esa actividad subordinada aparecerá con un poco de sangría en el
flujo de trabajo una vez que ejecute la actividad principal con el icono de ▶️
(botón de iniciar).

![Progreso de prueba del flujo de trabajo en la aplicación Automatización de
marketing de Odoo.](../../../../_images/workflow-test-progress.png)

Una vez que estén completas todas las actividades del flujo, la prueba
terminará y la barra de estado (ubicada en la esquina superior derecha) se
moverá a la etapa de Completado.

Para detener una prueba antes de que se completen todas las actividades del
flujo, haga clic en Detener, que se ubica en la esquina superior izquierda de
la página de prueba de la campaña.

## Lanzar campañas

Para iniciar una campaña, vaya a la aplicación Automatización de marketing y
seleccione la campaña que desee ejecutar.

En el formulario de detalles de la campaña, ya con todas las actividades
listas en la sección del flujo de trabajo, haga clic en Iniciar, que se ubica
en la esquina superior derecha, para lanzar oficialmente la campaña para su
audiencia objetivo que se especificó en el formulario de detalles.

Al hacer clic en Iniciar, comenzará la campaña y la barra de estado de la
campaña cambiará a En proceso, la cual está ubicada en la esquina superior
derecha del formulario de detalles de la campaña.

![El estado de la campaña de marketing establecido a en proceso, en la esquina
superior derecha](../../../../_images/campaign-running-status.png)

Nota

Si algunos participantes ya estaban activos dentro de una campaña y esta se
detuvo por cualquier razón, al hacer clic de nuevo en Iniciar aparecerá una
advertencia. Este mensaje le recomienda al usuario que haga clic en Actualizar
para aplicar cualquier modificación hecha a la campaña.

![Mensaje de advertencia emergente que advierte que el flujo de trabajo se ha
modificado en el formulario de una campaña de marketing.
](../../../../_images/workflow-modification-warning.png)

Tenga en cuenta que los participantes que ya habían completado una campaña
completa en su estado original, **pueden** volver a participar en la recién
modificada campaña, y puede crear nuevos seguimientos a partir de ellos.

Luego, a medida que los correos y las acciones se van activando en el Flujo de
trabajo, las estadísticas y datos relacionados a cada actividad aparecen en
cada bloque de actividades. También hay diferentes botones inteligentes
relacionados con las estadísticas que aparecen en la parte superior del
formulario de detalles de la campaña.

Estos botones inteligentes analíticos _también_ se poblarán con datos en
tiempo real a medida que avanza la campaña: plantillas, clics, pruebas,
participantes.

![La fila de botones inteligentes que aparece en una campaña de marketing en
proceso en Odoo.](../../../../_images/campaign-smart-buttons.png)

## Detener campañas

Para detener una campaña que está activa en ese momento, vaya a la aplicación
Automatización de marketing y seleccione la campaña que desea detener. En el
formulario de detalles de la campaña, haga clic en Detener que se ubica en la
esquina superior izquierda.

![Botón de detener en un formulario común de detalles de una campaña en la
aplicación Automatización de marketing de Odoo. ](../../../../_images/stop-
button-campaign-form.png)

Al hacerlo, la campaña se detiene oficialmente, y el estado cambia a Detenida
en la esquina superior derecha del formulario de detalles de la campaña.

![Estado de detenido de una campaña de marketing en un formulario de detalles
de una campaña en Automatización de marketing de Odoo.
](../../../../_images/campaign-stopped-status-bar.png)

Ver también

  * [Campañas de automatización de marketing](first_campaign.html)

  * [Dirigirse a un público](target_audience.html)

  * [Actividades del flujo de trabajo de una campaña](workflow_activities.html)

