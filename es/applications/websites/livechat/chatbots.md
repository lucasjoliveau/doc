# Bots de chat

Un _bot de chat_ es un programa diseñado para imitar una conversación con un
humano y funciona con un guion que debe seguir con pasos escritos previamente.
Los guiones están diseñados para pronosticar la respuesta de un visitante y
guiarlo mediante una serie de preguntas y respuestas de la misma manera que lo
haría algún miembro del equipo.

Puede personalizar los bots de chat para que desempeñen varias funciones como
proporcionar atención al cliente o crear leads y recopilar información de
contacto. El objetivo del bot de chat depende de la página del sitio web que
se le asigne, los mensajes en su guion y algunos otros criterios.

![Vista de la ventana de chat con un ticket del servicio de asistencia creado
mediante la aplicación Chat en vivo de Konvergo ERP.](../../../_images/chatbot-
visitor-view.png)

## Crear un bot de chat

Antes de crear un nuevo bot de chat debe instalar la aplicación _Chat en vivo_
en la base de datos, puede instalarla desde el menú de Aplicaciones. Busque
`Chat en vivo` en la **barra de búsqueda** y haga clic en **Instalar**.

También puede instalar y habilitar _Chat en vivo_ si se dirige a la aplicación
Sitio web ‣ Configuración ‣ Ajustes y selecciona la casilla etiquetada **Chat
en vivo**. Después de esto, la base de datos se actualizará y podrá acceder a
la aplicación _Chat en vivo_.

Abra la aplicación _Chat en vivo_ después de instalarla en la base de datos y
vaya a Configuración ‣ Bots de chat.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Cuando instala la aplicación <em>Chat en vivo</em>, se crea un bot de chat de muestra con el nombre <em>Bot de bienvenida</em>. Este bot tiene un guion preconfigurado con algunos pasos básicos, como preguntar por el correo electrónico de un visitante o enviar esa conversación a un operador.</p>
<p>Puede utilizar el <em>Bot de bienvenida</em> como base, ya que puede editar o eliminar los pasos existentes. También puede agregar nuevos pasos para personalizar el guion según sus necesidades.</p>
<p>Puede eliminar (o archivar) el <em>Bot de bienvenida</em>.</p>
<img alt="Vista del guion del bot de bienvenida en el Chat en vivo de Konvergo ERP." class="align-center" src="../../../_images/chatbot-welcome-bot.png"/>
</div>

Para crear un nuevo bot de chat, vaya a la página de **bots de chat**
(aplicación Chat en vivo ‣ Configuración ‣ Bots de chat) y haga clic en
**Nuevo**. Se abrirá una página con detalles para el bot de chat en blanco.

En la página de detalles para el bot de chat a completar, escriba la
información correspondiente en el **nombre del bot de chat** y haga clic en el
icono **editar imagen** en la esquina superior derecha del formulario para
agregar una imagen.

### Guion para el bot de chat

Una vez que creó y le proporcionó un nombre al nuevo bot de chat, debe crear
un guion. Las conversaciones del bot de chat siguen el guion adjunto compuesto
por líneas de diálogo, las cuales están diseñadas para proporcionar u obtener
información.

Para crear el guion que utilizará el bot, vaya a la pestaña **Guion** de la
página de detalles del bot de chat y haga clic en **Agregar una línea** para
abrir el formulario emergente **Crear pasos de guion**.

Debe llenar este formulario con cada línea de texto (diálogo) que el bot de
chat podría proporcionar durante la conversación.

Primero, escriba el contenido del mensaje en el campo **Mensaje** y luego
seleccione una opción en el menú desplegable **Tipos de paso**.

#### Tipos de paso

El **tipo de paso** seleccionado depende del propósito que tenga el mensaje.
Las opciones disponibles en el menú desplegable **Tipo de paso** se encuentran
a continuación, así como su uso y cualquier información adicional:

##### Texto

Este paso se utiliza para los mensajes donde no se espera o no es necesaria
una respuesta. Puede usar los pasos de texto para enviar un saludo o para
proporcionar información.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Los tipos de pasos de texto solo tienen como objetivo proporcionar información, pues no permiten que los visitantes escriban una respuesta. Además, necesitan pasos adicionales para poder continuar con la conversación.</p>
</div>

##### Pregunta

Este paso hace una pregunta y proporciona un conjunto de respuestas. El
visitante hace clic en una respuesta y como resultado crea un nuevo paso en la
conversación, también puede proporcionar un enlace opcional a una nueva página
web.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Es útil agregar una respuesta general (por ejemplo, «Algo más») a los pasos de preguntas. Esto ayuda a los visitantes a continuar la conversación, incluso si lo que necesitan no coincide exactamente con ninguna de las otras respuestas.</p>
</div>

##### Correo electrónico

Este paso solicita a los visitantes que proporcionen su dirección de correo
electrónico, esta se almacena y los miembros del equipo podrán utilizarla
después para realizar un seguimiento con información adicional.

Las únicas entradas aceptadas para este tipo de paso son las direcciones de
correo electrónico con un formato válido. Si un visitante intenta escribir
otra cosa, el bot de chat responderá que no reconoce la información enviada.

![Vista de un bot de chat que responde a un correo electrónico no
válido.](../../../_images/chatbot-invalid-email.png)

##### Teléfono

Al igual que el correo electrónico, este tipo de paso le pide al visitante que
proporcione su número de teléfono. Este se podrá utilizar después para hacer
un seguimiento con información adicional o para agendar demostraciones y otras
actividades.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Debido a la gran cantidad de formatos que tienen los números telefónicos en todo el mundo, en este tipo de paso <b>no</b> se valida el formato de las respuestas.</p>
</div>

##### Reenviar al operador

Este paso envía la conversación a un operador de chat en vivo activo para que
pueda seguir ayudando al visitante. La transcripción de la conversación se
transfiere al operador, y este podrá continuar donde se quedó el bot de chat.
Esto no solo ahorra tiempo para todas las partes involucradas, también puede
ayudar a calificar las conversaciones antes de que lleguen a los operadores.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si no hay ningún operador activo disponible en el canal, el bot de chat continúa la conversación con el visitante. Asegúrese de agregar pasos adicionales después de este para que la conversación no termine de forma repentina.</p>
<img alt="Vista de mensajes de seguimiento de un bot de chat cuando ningún operador de chat en vivo está disponible." class="align-center" src="../../../_images/chatbot-no-operator.png"/>
</div>

##### Entrada libre o multilínea

El paso denominado «entrada libre» permite que los visitantes respondan a las
preguntas sin proporcionar respuestas predefinidas. La información
proporcionada en estas respuestas se almacena en las transcripciones del chat.

Elija entre **Entrada libre** y **Entrada libre (multilínea)** según el tipo y
la cantidad de información que el visitante deba proporcionar.

##### Crear lead

Este paso crea un lead en la aplicación _CRM_. Seleccione una opción del menú
desplegable **Equipo de ventas** para asignar el lead que se creó a un equipo
específico.

##### Crear ticket

Este paso crea un
[ticket](../../services/helpdesk/overview/receiving_tickets) en la
aplicación _Servicio de asistencia_. Seleccione una opción del menú
desplegable **Equipo de servicio de asistencia** para asignar el ticket a un
equipo específico.

#### Solo si

Los guiones del bot de chat trabajan con una base «si - entonces», es decir,
la siguiente pregunta que se le hará al visitante está determinada por la
respuesta que proporcionó a la pregunta anterior.

Para continuar con la conversación, el formulario para un nuevo paso contiene
un campo etiquetado **Solo si**. En este campo se define la progresión de las
preguntas.

Puede dejar vacío este campo si espera que un paso siga todos los mensajes
anteriores. Sin embargo, si un mensaje **solo** debe enviarse de forma
condicional, según las respuestas anteriores, entonces agregue esas respuestas
a este campo.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Si hay alguna selección en el campo <b>Solo si</b>, el paso <b>no</b> se mostrará en una conversación a menos que haya seleccionado <b>todas</b> las respuestas. Solo incluya selecciones en este campo si son necesarias para mostrar este paso.</p>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>En el guion del <em>bot de bienvenida</em>, un visitante puede preguntar sobre los precios. Si el visitante selecciona esta respuesta, se incluye un paso para enviar la conversación a un operador. El bot de chat primero envía un mensaje que le informa al visitante que está en búsqueda de un operador disponible para chatear.</p>
<p>Sin embargo, este mensaje <b>solo</b> se debe enviar si el visitante solicita información de precios. En ese caso, la conversación sería la siguiente:</p>
<ul>
<li><p>Bot de bienvenida: «<em>¿Qué está buscando?</em>»</p></li>
<li><p>Visitante: «<b>Tengo una pregunta sobre los precios.</b>»</p></li>
<li><p>Bot de bienvenida: «<em>Mmmm, déjeme revisar si puedo encontrar a alguien que pueda ayudarle con eso…</em>»</p></li>
</ul>
<p>En el formulario de detalles del paso de tipo <b>texto</b> se seleccionó la respuesta <em>Tengo una pregunta sobre los precios</em> en el campo <b>Solo si</b>. Este paso <b>solo</b> aparece en las conversaciones donde se seleccionó esa respuesta.</p>
<img alt="Vista del formulario de nuevo mensaje, se resalta el campo Solo si." class="align-center" src="../../../_images/chatbot-only-if.png"/>
</div>

### Pruebas con el guion

Para garantizar que todos los visitantes tengan una experiencia satisfactoria
con el bot de chat, cada mensaje debe tener un desenlace natural. Debe probar
los guiones del bot de chat para verificar que los mensajes proporcionan
soluciones adecuadas y para comprender lo que el visitante ve cuando
interactúa con el bot.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Si hay una respuesta predefinida o proporcionada por el visitante que <b>no</b> tiene asignada una respuesta para continuar, la conversación se detiene. Como el visitante no puede volver a activar el bot de chat, tendrá que iniciar la conversación de nuevo, es decir, debe actualizar la ventana de chat o su navegador.</p>
</div>

Para probar el rendimiento de un bot de chat, primero haga clic en **Probar**
en la parte superior izquierda de la página del guion del bot de chat. Se le
redirigirá a la pantalla de prueba, responda las preguntas del bot de chat
como lo haría un visitante potencial del sitio.

Cuando el guion ya no tiene más mensajes para mostrar, en la parte inferior de
la ventana de chat aparece el mensaje _La conversación terminó… Reiniciar_.
Para iniciar una conversación con el primer mensaje del guion, haga clic en
**Reiniciar**. Para volver a la página del guion, haga clic en **Volver al
modo de edición** en la parte superior de la página.

## Agregar un bot de chat a un canal

Después de crear y probar su bot conversacional, debe agregarlo a un canal de
chat en vivo.

Abra la aplicación Chat en vivo y seleccione la tarjeta kanban de algún
**canal** o cree [uno nuevo](../livechat). Haga clic en la pestaña
**Reglas del canal**. Luego, abra una regla existente o cree una nueva con el
botón **Agregar una línea**.

En el formulario de detalles emergente **Crear reglas** , seleccione un **bot
de chat** en el campo correspondiente.

Si el bot conversacional **solo** debe estar activo si no hay operadores de
chat en vivo disponibles, marque la casilla con el nombre **Habilitado solo si
no hay un operador**.

![Vista de las reglas del canal, se resalta el campo Bot de
chat.](../../../_images/chatbot-add-to-channel.png) <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../livechat">Reglas del canal de chat en vivo</a></p>
</div>

