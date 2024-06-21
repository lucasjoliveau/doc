# Conversaciones

_Conversaciones_ de Konvergo ERP es una aplicación de comunicación interna que le
permite a lo usuarios comunicarse mediante mensajes, notas y archivos
adjuntos, todo mediante una ventana de chat que funciona no importa en qué
aplicación esté y en el tablero de _Conversaciones_.

## Seleccione sus preferencias de notificaciones

Para acceder a las preferencias específicas del usuario en la aplicación
_Conversaciones_ vaya a Ajustes ‣ Usuarios ‣ Usuario ‣ pestaña de Preferencia.

![Imagen de la pestaña de preferencias en Conversaciones de
Konvergo ERP.](../../_images/preferences-user.png)

El campo **Notificación** estará configurado de forma predeterminada con la
opción **Manejar por correo electrónico**. Con este ajuste Konvergo ERP enviará un
correo de notificación cada que envíe un mensaje desde el chatter, una nota
con una mención `@` (también desde el chatter) o una notificación para un
registro que el usuario sigue. También enviará una notificación al cambiar de
etapa (si configuró el envío de un correo, por ejemplo, si una tarea se marca
como **Hecha**).

Si selecciona **Gestionar en Konvergo ERP** , las notificaciones se muestran en la
_bandeja de entrada_ de la aplicación _Conversaciones_. Con los mensajes es
posible: responder con un emoji al **Agregar una reacción** , o puede
responder al mensaje si hace clic en **Responder**. También puede **marcar
mensajes como por realizar** si hace clic en la estrella, puede anclarlos si
hace clic en **Fijar** , o incluso **marcar el mensaje como no leído**.

![Imagen de un mensaje en la bandeja de entrada y las opciones de acción en
Conversaciones de Konvergo ERP.](../../_images/reactions-discuss.png)

Si hace clic en **Marcar como pendiente** en un mensaje, hará que aparezca en
la página **Destacados**. Si hace clic en **Marcar como leído** el mensaje se
moverá a **Historial**.

![Imagen de mensajes que se marcaron como por hacer en Conversaciones de
Konvergo ERP.](../../_images/starred-messages.png)

## Empiece a chattear

La primera vez que un usuario inicia sesión en su cuenta, Konvergo ERPBot envía un
mensaje donde se le pedirá permiso para enviar notificaciones de chats a su
computadora. Si lo acepta, el usuario recibirá notificaciones push en su
computadora de todos los mensajes que reciba, sin importar en qué parte de
Konvergo ERP se encuentre el usuario.

![Imagen de mensajes en el menú de mensajería en donde se resalta la solicitud
para enviar notificaciones push para la aplicación Conversaciones de
Konvergo ERP.](../../_images/odoobot-push.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para dejar de recibir notificaciones de escritorio, restablezca la configuración de notificaciones del navegador.</p>
</div>

Para iniciar un chat, vaya a la aplicación **Conversaciones** y haga clic en
el icono **\+ (más)** que se encuentra a un lado de **Mensajes directos** o
**Canales** en el menú izquierdo del tablero.

![Imagen del panel de Conversaciones donde se resaltan las secciones de
canales y mensajes directos en la aplicación Conversaciones de
Konvergo ERP.](../../_images/channels-direct-messages.png)

Una empresa también puede crear [canales privados y
públicos](discuss/team_communication) sin dificultades.

### Menciones en el chat y en el chatter

Para mencionar a un usuario en un chat o en un chatter, escriba `@nombre-de-
usuario`. Para mencionar un canal, escriba `#nombre-del-canal`. El usuario
mencionado recibirá una notificación en su _bandeja de entrada_ o por correo
electrónico, dependiendo de los ajustes de comunicación.

![Imagen de dos ventanas de mensajes de chat de Conversaciones de
Konvergo ERP.](../../_images/chat-windows.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Cuando se menciona a un usuario, la lista de búsqueda (lista de nombres) sugiere valores, en primer lugar, en función de los seguidores de la tarea y, en segundo lugar, en función de los empleados. Si el registro que se busca no coincide con un seguidor o un empleado, el alcance de la búsqueda se convierte en todos los contactos.</p>
</div>

### Estado del usuario

Es útil ver qué están haciendo sus colegas y qué tan rápido pueden responder a
los mensajes, por eso debe verificar su _estado_. El estado se muestra en el
lado izquierdo de el nombre de un contacto en la barra lateral
de:guilabel:`Discusiones`, en el _menú de mensajería_ y en el _chatter_.

  * Verde = en línea

  * Naranja = ocupado

  * Blanco = sin conexión

  * Avión = fuera de la oficina

![Vista del estado de los contactos en Conversaciones de
Konvergo ERP.](../../_images/status.png) <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="discuss/team_communication">Uso de canales para la comunicación en equipo</a></p></li>
<li><p><a href="../essentials/activities">Actividades</a></p></li>
</ul>
</div>

  * [Uso de canales para la comunicación en equipo](discuss/team_communication)
  * [Configurar servidores ICE con Twilio](discuss/ice_servers)

