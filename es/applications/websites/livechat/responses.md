# Comandos y respuestas predefinidas

En la aplicación _Chat en vivo_ de Konvergo ERP, el usuario puede realizar acciones
específicas tanto dentro de la ventana de chat como en otras de nuestras
aplicaciones mediante _comandos_. Esta aplicación también incluye _respuestas
predeterminadas_ , las cuales son sustituciones personalizadas y
preconfiguradas que permiten que los usuarios utilicen atajos en lugar de
respuestas más largas para responder a algunas de las preguntas y comentarios
más comunes.

Tanto los comandos como las respuestas predeterminadas ahorran tiempo y
permiten que los usuarios mantengan un nivel de consistencia en sus
conversaciones.

## Ejecutar un comando

Los _comandos_ del chat en vivo son palabras clave que activan acciones
preconfiguradas. Cuando un _operador_ participa en una conversación con un
cliente o visitante del sitio web puede ejecutar un comando al escribir `/`
seguido del comando.

Los comandos y las acciones que resultan de estos solo son visibles en la
ventana de conversación del operador de chat en vivo. Un cliente no verá los
comandos que utiliza el operador en una conversación desde su vista del chat.

![Vista de la ventana de chat con un ticket del servicio de asistencia creado
mediante la aplicación Chat en vivo de Konvergo ERP.](../../../_images/responses-
ticket-link.png)

A continuación encontrará más información sobre los comandos disponibles.

### Ayuda

Si un operador escribe `/ayuda` en la ventana del chat, aparecerá un mensaje
con información que incluye los tipos de entrada potenciales que puede hacer.

  * Escriba `@nombre_de_usuario` para mencionar a un usuario en la conversación. Ese usuario recibirá una notificación en su bandeja de entrada o correo electrónico, según la configuración de sus notificaciones.

  * Escriba `#canal` para mencionar un canal de _Conversaciones_.

  * Escriba `/comando` para ejecutar un comando.

  * Escriba `:atajo` para insertar una respuesta predefinida.

![Vista del mensaje que se generó mediante el comando /ayuda en la aplicación
Chat en vivo de Konvergo ERP.](../../../_images/responses-help.png)
<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../../productivity/discuss">Conversaciones</a></p></li>
<li><p><a href="../../productivity/discuss/team_communication">Uso de canales para la comunicación en equipo</a></p></li>
</ul>
</div>

### Servicio de asistencia y búsqueda en el servicio de asistencia

Los comandos `/helpdesk` y `/helpdesk_search` permiten que los operadores
creen tickets para el servicio de asistencia desde una conversación y que
busquen tickets que ya existen por palabra clave o número.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Solo puede usar los comandos <code>/helpdesk</code> y <code>/helpdesk_search</code> si instaló la aplicación <em>Servicio de asistencia</em>. Además, el <em>Chat en vivo</em> debe estar activo en algún equipo del <em>Servicio de asistencia</em>. Para activar <b>Chat en vivo</b>, vaya a la aplicación Servicio de asistencia ‣ Configuración ‣ Equipos y seleccione uno. Desplácese a la sección <b>Canales</b> y marque la casilla etiquetada como <b>Chat en vivo</b>.</p>
</div>

#### Crear un ticket desde un chat en vivo

Si un operador escribe `/helpdesk` en la ventana del chat, se utiliza la
conversación para crear un ticket para el _Servicio de asistencia_.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>En la versión 16.3, el comando para crear un nuevo ticket es <code>/ticket</code> y solo funcionará con las bases de datos que usen esa versión.</p>
</div>

Después de escribir el comando `/helpdesk`, escriba un título para el ticket
en la ventana de chat y presione la tecla `enter`.

![Vista de los resultados de una búsqueda en el servicio de asistencia en una
conversación de chat en vivo.](../../../_images/helpdesk.png)

El equipo de _Servicio de asistencia_ con el chat en vivo habilitado recibirá
el ticket recién creado. Si más de un equipo tiene esta función habilitada,
entonces se asignará en automático según la prioridad del equipo.

La transcripción de la conversación se agregará al nuevo ticket, en la pestaña
**Descripción**.

Para acceder al nuevo ticket, haga clic en el enlace de la ventana de chat.
También puede ir a la aplicación Servicio de asistencia y luego hacer clic en
el botón **Tickets** de la tarjeta kanban para el equipo correspondiente.

#### Buscar un ticket desde un chat en vivo

Si un operador escribe `/helpdesk_search` en la ventana de chat, podrá buscar
en los tickets de _Servicio de asistencia_ por número o palabra clave.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>En la versión 16.3, el comando para buscar en los tickets del <em>Servicio de asistencia</em> es <code>/search_tickets</code> y solo funcionará con las bases de datos que usen esa versión.</p>
</div>

Después de ingresar el comando `/helpdesk_search`, escriba una palabra clave o
un número de ticket y presione la tecla `enter`. Si se encuentran uno o más
tickets relacionados, se generará una lista de enlaces en la ventana de la
conversación.

![Vista de los resultados de una búsqueda en el servicio de asistencia en una
conversación de chat en vivo.](../../../_images/helpdesk-search.png)
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Solo el operador podrá ver los resultados del comando de búsqueda, el cliente no.</p>
</div>

### Historial

Si un operador escribe `/historial` en la ventana de chat, se generará una
lista de las páginas más recientes que el visitante ha visto en el sitio web
(hasta 15).

![Vista de los resultados del comando /historial en una conversación de chat
en vivo.](../../../_images/responses-history.png)

### Lead

Si un operador escribe `/lead` en la ventana de chat, creará un _lead_ en la
aplicación _CRM_.

![Vista de los resultados de un comando /lead en una conversación de chat en
vivo.](../../../_images/responses-lead.png) <div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Solo puede utilizar el comando <code>/lead</code> si instaló la aplicación <em>CRM</em>.</p>
</div>

Después de escribir `/lead`, proporcione un título para este lead y luego
presione `Enter`. Aparecerá un enlace con el título del lead, haga clic en él
o vaya a la aplicación CRM para ver el **flujo**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Solo el operador puede ver y acceder al enlace del lead, el cliente no.</p>
</div>

Se agregará la transcripción de esa conversación en específico (donde se creó
el lead) de chat en vivo a la pestaña **Notas internas** del formulario de
lead.

En la pestaña **Información adicional** del formulario del lead, aparecerá
**Chat en vivo** como **fuente**.

### Ausencia

Un operador puede salir de la conversación si escribe `/leave` en la ventana
de chat. Este comando no hace que el cliente salga de la conversación o que
esta termine de forma automática.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../../sales/crm/acquire_leads">Obtener leads</a></p></li>
<li><p><a href="../../services/helpdesk/overview/getting_started">Primeros pasos con Servicio de asistencia</a></p></li>
</ul>
</div>

## Respuestas predefinidas

Las _respuestas predefinidas_ son aquellas que cuentan con un _atajo_ para
proporcionar una respuesta más larga. Cuando un operador escribe el atajo,
este se reemplaza en automático por la respuesta de _sustitución_ completa en
la conversación.

### Crear respuestas predefinidas

Para crear una nueva respuesta predefinida, vaya a la aplicación Chat en vivo
‣ Configuración ‣ Respuestas predefinidas ‣ Nuevo.

Aquí deberá escribir el comando para el atajo en el campo **Acceso rápido**.

Después, haga clic en el campo **Sustitución** y escriba el mensaje
personalizado que enviará a los visitantes en lugar del acceso rápido. Haga
clic en **Guardar**.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Intente relacionar el atajo al asunto de la sustitución. Cuanto más fácil sea para los operadores recordarlo, más fácil será usar las respuestas predefinidas en las conversaciones.</p>
</div>

### Usar respuestas predefinidas en una conversación de chat en vivo

Para usar una respuesta predefinida durante una conversación de chat en vivo,
escriba dos puntos (`:`) en la ventana de chat y luego el atajo.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Un operador se encuentra conversando con un visitante. Al escribir <code>:</code> tendrá acceso a una lista de respuestas disponibles y podrá seleccionar una de la lista o continuar escribiendo. Si desea usar la respuesta predefinida <code>'Lamento escuchar eso.'</code>, deberá escribir <code>:disculpa</code>.</p>
</div> ![Vista de una ventana de chat y el uso de una respuesta
predefinida en la aplicación Chat en vivo de Konvergo ERP.](../../../_images/canned-
responses.png) <div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Solo puede usar los comandos <code>/helpdesk</code> y <code>/helpdesk_search</code> si instaló la aplicación <em>Servicio de asistencia</em>. Además, el <em>Chat en vivo</em> debe estar activo en algún equipo del <em>Servicio de asistencia</em>. Para activar <b>Chat en vivo</b>, vaya a la aplicación Servicio de asistencia ‣ Configuración ‣ Equipos y seleccione uno. Desplácese a la sección <b>Canales</b> y marque la casilla etiquetada como <b>Chat en vivo</b>.</p>
</div>0

