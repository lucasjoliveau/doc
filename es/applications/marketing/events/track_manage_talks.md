# Seguimiento y gestión de las pláticas

Gracias a la aplicación Eventos de Konvergo ERP, podrá permitir que sus asistentes
propongan ponentes para los eventos.

## Configuración

Vaya a Eventos ‣ Configuración ‣ Ajustes y habilite **Horario y sesiones**.

Si activa esta función, aparecerán otras dos opciones: _Transmisión en vivo_ y
_Ludificación del evento_.

**Transmisión en vivo** permite la emisión de sesiones en línea gracias a su
integración con YouTube.

**Ludificación del evento** permite compartir un cuestionario con sus
asistentes, una vez finalizada una sesión (plática).

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p><b>Ludificación del evento</b> no es necesaria para que las sesiones aparezcan en la página del evento en el sitio web, pero puede mejorar la participación y la experiencia general de los asistentes.</p>
</div>

## Pláticas, propuestas de pláticas y agenda

Una vez activadas estas dos funciones, se añadirán automáticamente los
siguientes enlaces al menú situado en la página del evento del sitio web:
**Pláticas** , **Propuestas de pláticas** , y **Agenda**. Cualquier asistente
puede acceder libremente a estos elementos del menú y a su contenido.

El enlace **Pláticas** dirige al asistente a una página con todas las pláticas
de ese evento.

Mientras que el enlace **Propuestas de pláticas** dirige a los asistentes a un
formulario en el que pueden proponer pláticas para el evento.

El enlace **Agenda** dirige al asistente a una página con todas las pláticas
del evento, pero en formato de calendario/horario.

![Vista de la página web publicada y de las pláticas, propuestas de pláticas y
agenda](../../../_images/events-talk-proposal-header.png)

## Gestión de las propuestas de pláticas

Cuando los asistentes completen y envíen un formulario de propuesta de plática
en el sitio web, se creará inmediatamente una nueva **Propuesta** en el
backend del evento.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Todas las pláticas (Propuestas, Confirmadas, Anunciadas, etc.) están disponibles a través del botón inteligente <b>Sesiones</b> del formulario del evento.</p>
</div> ![Vista de la página de propuestas de pláticas destacando
la columna de propuesta](../../../_images/events-tracks-kanban.png)

Si se acepta una propuesta, mueva la etiqueta **Sesión de evento** a la fase
adecuada en la vista kanban (por ejemplo, `confirmada`, etc.). A continuación,
vaya al formulario de plantilla de ese evento en particular y haga clic en el
botón inteligente **Ir al sitio web** para acceder a la página de esa plática
específica en el sitio web.

Para hacer que una plática esté disponible vaya a la esquina superior derecha
y cambie el estado de **Sin publicar** a **Publicado**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Recuerde que si no publica una plática, nadie podrá verla.</p>
</div> ![Vista del sitio web en la que se ve el botón "Sin
publicar" en las pláticas propuestas de Eventos de
Konvergo ERP.](../../../_images/events-tracks-publish.png)

### Lista de asistentes y asistencia

Una vez que los asistentes se registren en un evento específico, serán parte
de la **lista de asistencia** del evento. Si desea ver la lista haga clic en
el botón inteligente guilabel:`asistentes` disponible en el formulario del
evento o en Reportes ‣ Asistencia .

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Cuando un asistente llegue al evento, se va a <b>confirmar su asistencia</b> y su estado cambiará a <b>Asistió.</b></p>
</div> ![Vista general de los eventos en vista
kanban](../../../_images/events-attendees-smartbutton.png)

Si desea analizar la **lista de asistentes** Konvergo ERP ofrece varias maneras de
visualizar la información. Cada vista es diferente, aunque presenta la misma
información; si desea cambiar el tipo de vista haga clic en los iconos
ubicados en la esquina superior derecha.

![Diferentes opciones de vista en la lista de
asistentes.](../../../_images/events-attendees-view-options.png)

La vista **kanban** muestra si los asistentes ya pagaron su boleto o sigue
pendiente.

La vista de **lista** muestra la información en forma de lista.

La vista de **calendario** proporciona una visualización clara del calendario
de la cantidad de asistentes en cada evento, para cada fecha.

La vista de **gráfico** muestra los asistentes de cada evento, a su vez ofrece
varios filtros y medidas personalizables para obtener un mejor análisis.

La vista **cohorte** muestra los datos de los asistentes para analizar de
mejor manera el número de fechas de registro.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si vende los boletos mediante órdenes de venta, se validarán los asistentes en cuanto se confirme la cotización.</p>
</div>

### Gestión de registros

Si selecciona un asistente, Konvergo ERP le mostrará el formulario con más información
de ese asistente específico.

Desde aquí se pueden enviar las insignias del evento de forma manual, solo
debe seleccionar **Enviar por correo electrónico**. También se puede
establecer el estado del **asistente** comó **asistió** , o puede cancelar el
registro mediante el botón **Cancelar registro**.

![Vista del formulario de un asistente en la que se hace énfasis el botón
Enviar por correo electrónico.](../../../_images/events-send-email-button.png)

### Reglas de generación de leads

Con Konvergo ERP, puede generar leads a partir de eventos.

Para crear y configurar una **regla de generación de leads** que se relacione
con eventos, vaya a la aplicación Eventos ‣ Configuración ‣ Generación de
leads.

En la página de **reglas de generación de leads** puede ver todas las
**reglas** configuradas, junto con todos los datos relacionados con dichas
reglas.

![Página de reglas de generación de leads en la aplicación Eventos de
Konvergo ERP.](../../../_images/events-lead-generation-rule-page.png)

Para crear una nueva **regla de generación de leads** , haga clic en **crear**
y complete el formulario de la **regla de generación de leads**.

![Plantilla de regla de generación de leads en la aplicación Eventos de
Konvergo ERP](../../../_images/events-lead-generation-rule-template.png)

Después de agregar el nombre de la regla, configure **cómo** se deberían crear
los leads (puede ser **por asistente** o **por orden**), y _cuándo_ se
deberían crear (cuando **se crean los asistentes** , cuando **se confirman** ,
o cuando **asistieron** al evento).

En la sección **para cualquiera de estos eventos** hay campos para agregar
esta regla a cualquier categoría de evento, empresa y/o evento en específico.
Para hacer que esta regla sea aún más específica, puede configurar una regla
de filtro de dominio para garantizar que la regla solo se aplique a un público
objetivo de asistentes en específico (puede hacerlo en la sección **si los
asistentes cumplen con las siguientes condiciones**).

Por último, en la sección **valores predeterminados de leads** elija un **tipo
de lead** , asígnelo a un **equipo de ventas** (y/o a un **vendedor**) y
agregue etiquetas a la regla si es necesario.

