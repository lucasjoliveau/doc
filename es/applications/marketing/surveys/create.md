# Fundamentos de las encuestas

Las empresas utilizan con frecuencia encuestas para recolectar información
valiosa de sus clientes y empleados, lo que les permite tomar decisiones
empresariales informadas.

En Odoo las encuestas se utilizan para recolectar la retroalimentación de los
clientes, evaluar el éxito de eventos recientes, medir la satisfacción de los
clientes (o empleados) y obtener mayor información sobre los cambios de
opinión en el mercado.

## Primeros pasos

Para empezar, acceda a la aplicación Encuestas y haga clic en Crear. Odoo lo
redireccionará a un formulario de plantilla de encuesta en blanco.

En el formulario de la encuesta agregue el título de la encuesta y también
puede agregar una imagen de portada si coloca el ratón sobre el icono de foto
y hace clic en el icono de editar (lápiz). Cuando se abra la ventana del
navegador de archivos, elija una imagen de sus computadora.

Debajo del título de la encuesta se encuentran varias pestañas en las cuales
se pueden crear y personalizar las preguntas y el formato de la encuesta.
Estas pestañas tienen los siguientes nombres:

  * Preguntas: la lista de preguntas que se incluirán en la encuesta.

  * Descripción: información contextual para mejorar la comprensión de la encuesta.

  * Opciones: ajustes de configuración de la encuesta.

![Las distintas pestañas que se pueden encontrar en una plantilla de
encuesta.](../../../_images/questions-description-options.png)

## Pestaña de preguntas

En la pestaña de preguntas puede agregar preguntas y secciones a la encuesta.
Las secciones dividen la encuesta en distintas partes para agrupar preguntas
similares. Para crear una sección, haga clic en agregar una sección y escriba
el nombre de la sección. Posteriormente, agregue preguntas o arrástrelas y
suéltelas en las secciones.

Hacer clic en Agregar una pregunta abre la ventana emergente crear secciones y
preguntas para crear y personalizar las preguntas de la encuesta.

![La ventana emergente de preguntas de la encuesta.](../../../_images/survey-
question-pop-up.png)

### Crear preguntas

En la ventana emergente crear secciones y preguntas escriba la pregunta en el
campo pregunta. Después, elija el tipo de pregunta. En la ventana de vista
previa puede ver cómo se ve el tipo de pregunta.

Elija uno de los siguientes tipos de preguntas:

  * Cuadro de texto con múltiples líneas

  * Cuadro de texto son una línea

  * Valor númerico

  * Fecha

  * Fecha y hora

  * Opción múltiple: solo una respuesta

  * Opción múltiple: se permiten varias respuestas

  * Matriz

Nota

Aparecerán diferentes funciones en las pestañas Respuestas y Opciones,
dependiendo del Tipo de pregunta elegida. Sin embargo, la pestaña Descripción
siempre queda igual, sin importar cual sea la pregunta elegida.

#### Crear secciones y preguntas

Una vez que seleccionó un Tipo de pregunta hay tres posibles pestañas donde
puede personalizar la información para la pregunta. Estas incluyen las
pestañas de Respuestas (si aplica), Descripción y Opciones.

Cada pestaña ofrece una variedad diferentes de funciones dependiendo de qué
Tipo de pregunta escogió.

Por ejemplo, en la pestaña de Opciones, pueden aparecer las siguientes
opciones:

  * Respuesta obligatoria: debe responder la pregunta.

  * Tipo de matriz: para preguntas de tipo matriz, seleccione si se puede seleccionar una o más opciones por fila.

  * Número de columnas: seleccione cuántas columnas se muestran.

  * Imágenes en las respuestas: permita las imágenes en las opciones de respuesta.

  * Visualización condicional: determina si la pregunta se muestra con base en la respuesta del participante de una pregunta previa.

  * Mostrar campo de comentarios: permita al participante escribir un comentario en un cuadro de texto.

  * Tiempo límite de la pregunta: para las encuestas en sesiones en vivo, establezca un tiempo límite para la pregunta.

##### Visualización condicional

Visualización condicional significa que la pregunta solo es visible si se
seleccionó la respuesta condicional específica en la pregunta anterior.

Cuando está seleccionada la casilla que está junto a Visualización
condicional, aparecerá el campo de Pregunta desencadenante. Seleccione una
pregunta de la encuesta.

Luego, aparecerá un campo de Respuesta desencadenante. Seleccione que
respuesta desencadenará la pregunta configurada como Visualización
condicional.

## Pestaña de opciones

En la plantilla del formulario de la encuesta principal, en la pestaña
Opciones, hay secciones de ajustes que puede modificar.

Estas secciones incluyen:

  * Preguntas: se enfoca en la presentación general de la encuesta

  * Puntaje: establece como se califica la encuesta

  * Candidatos: gestiona el acceso a la encuesta

  * Sesión en vivo: convierte la encuesta en una actividad grupal en tiempo real.

### Preguntas

Primero, seleccione el Diseño de la encuesta. Puede elegir de entre las
siguientes opciones:

  * Una página con todas las preguntas

  * Una página por sección

  * Una página por pregunta

Si selecciona la opción Una página por sección o Una página por pregunta,
aparecerá la opción Botón de retroceso. Si selecciona la opción de Botón de
retroceso, el participante podrá regresar a una pregunta mientras repsonde la
encuesta.

Entre las opciones de Diseño se encuentra el ajuste de Mostrar progreso como,
que indica cómo se muestra el progreso del participante. Se muestra como un
Porcentaje o un Número.

Después, hay una opción disponible para agregar un Tiempo límite de la
encuesta. Para activar esta opción, simplemente seleccione la casilla e
introduzca la cantidad de tiempo (en minutos) que tienen los participantes
para terminar la encuesta.

Después de la opción Tiempo límite de la encuesta hay una sección llamada
Selección de preguntas. Aquí, puede seleccionar que las preguntas aparezcan
Aleatorio por sección, es decir, puede configurar el número de preguntas
aleatorias por sección. Esta opción no se toma en cuenta en las sesiones en
vivo.

Ver también

[Preguntas cronometradas y aleatorias](time_random.html)

### Puntuación

Al decidir de qué manera aparecerá la Puntuación podrá escoger de entre las
siguientes opciones:

  * Sin puntaje

  * Puntaje con respuestas al final

  * Puntaje sin respuestas al final

Si selecciona la opción Puntaje con respuestas al final o Puntaje din
respuestas al final, aparecerá un campo de Porcentaje de puntaje obligatorio.
Establezca el puntaje de respuestas correctas necesarias para aprobar la
encuesta.

Luego, tendrá la opción de convertir la encuesta en una certificación. Para
hacerlo, seleccione la casilla que está junto a la opción Es una certificación
y aparecerán otros dos campos. Seleccione un color en el campo Plantilla de la
certificación y luego elija una Plantilla de correo electrónico. Cuando un
participante aprueba la certificación con el puntaje requerido, se le enviará
automáticamente un correo usando la plantilla seleccionada.

Si la función Dar insignia está activada y está establecida la opción Insignia
de certificación, el participante también recibirá una insignia al aprobar la
certificación.

Ver también

[Puntaje de las encuestas](scoring.html)

### Participantes

Para determinar el acceso a la encuesta, el Modo de acceso le permite escoger
de entre dos opciones: Cualquier persona que tenga el enlace y Solo personas
con invitación.

Debajo de la casilla Evaluación solo para gerentes, está la opción de Se
requiere inicio de sesión para solicitarle al participante que inicie sesión
para realizar la encuesta. Si está activada esta opción, también se completará
un campo de Limitar intentos, en el cual se definen el número de intentos que
tiene el participante para realizar la encuesta.

### Sesión en vivo

La sección Sesión en vivo está dedicada a los usuarios que realizan encuestas
en tiempo real, donde interactúan y obtienen respuestas de una audiencia en
vivo.

Personalice el Código de sesión aquí; los participantes necesitan este código
para acceder a la encuesta de la sesión en vivo. Premie a los participantes
cuando repondan rápidamente seleccionando la casilla Premiar respuestas
rápidas. Al seleccionarla, los asistentes obtendrán más puntos si responden
rápidamente.

## Pestaña de descripción

En la página principal de la plantilla de la encuesta está la pestaña de
Descripción, dónde puede agregar una descripción personalizada de la encuesta.
Esto se muestra debajo del título de la página principal de la encuesta, que
está en el frontend de la página web que creó a través de la aplicación Sitio
web de Odoo.

## Poner a prueba y compartir la encuesta

Una vez que creó y guardó la encuesta, haga una prueba para verificar que no
haya errores antes de enviarla a los participantes haciendo clic en el botón
Prueba que está en la esquina superior izquierda de la página de la plantilla
de la encuesta.

Al activar está función, Odoo lo redirecciona a una versión de prueba de la
encuesta en el frontend del sitio web. Esta página muestra como lucirá la
encuesta para los participantes. Realice la encuesta como lo haría el
participante para revisar que no haya errores.

Para regresar al formulario de la plantilla de la encuesta en el backend, solo
haga clic en el enlace que está en el panel azul en la parte superior de la
página que dice Está es una prueba. Editar encuesta. Una vez que Odoo lo
redirecciona a la plantilla de la encuesta en el backend, haga los cambios
necesarios antes de enviar oficialmente la encuesta a los participantes.

Cuando esté listo para compartir la encuesta con la audiencia, haga clic en el
botón Iniciar encuesta que está en el lado superior izquierdo del formulario
de la plantilla de la encuesta. Luego haga clic en Compartir.

En la ventana emergente que aparece, en el campo Destinatarios, agregue a los
destinatarios que recibirán la encuesta (para contactos ya existentes en la
base de datos de Odoo). También puede elegir el campo Correos adicionales
(para contactos que no quieran estar registrados en la base de datos de Odoo).
Finalmente, haga clic en Enviar.

Mientras recibe las respuestas, revíselas haciendo clic en el botón
inteligente de Respuestas en el formulario de la plantilla de la encuesta o en
el botón de Ver resultados que está en la esquina superior izquierda. Para
terminar la encuesta, haga clic en el botón de Cerrar en el formulario de la
plantilla de la encuesta.

