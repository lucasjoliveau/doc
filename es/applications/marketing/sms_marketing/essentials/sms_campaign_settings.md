# Ajustes de campaña de SMS

Utilizar campañas de SMS con la aplicación _Marketing por SMS_ no solo es una
estrategia publicitaria eficaz, sino que también es una gran forma de
recordarle a las personas sobre sus próximos eventos, facturas emitidas y
mucho más.

Es necesario que habilite algunos ajustes y funciones específicas antes de
crear (y enviar) campañas de SMS.

## Ajuste de campaña de SMS

Para habilitar las campañas SMS en Konvergo ERP debe asegurarse de que la función
_Campañas de correo_ este activada en Marketing por correo electrónico ‣
Configuración ‣ Ajustes. Habilite la función **Campañas de correo** y
**guarde** los cambios.

![Vista del ajuste "campañas de correo" en Konvergo ERP.](../../../../_images/sms-
mailing-campaigns.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Activar la función <em>campañas de correo</em> en los <em>ajustes generales</em> también habilita la función <em>prueba A/B</em>.</p>
</div>

Una vez que habilite el ajuste, regrese a la aplicación Marketing por SMS.
Notará que el menú **campañas** ahora está disponible en el encabezado. De
igual forma, la pestaña **prueba A/B** ahora está disponible en todos los
formularios de plantilla de SMS.

## Pruebas A/B

Las **pruebas A/B** permiten realizar pruebas a cualquier SMS en comparación
con otras versiones en la misma campaña con el fin de saber qué versión tiene
más éxito con los resultados de participación y conversión.

En un formulario de plantilla de SMS, en la pestaña **Prueba A/B** , al inicio
solo hay una casilla con el nombre **Permitir pruebas A/B.**

Al seleccionarla, aparecen otras opciones.

![La pestaña de prueba A/B se ubica en el formulario de campaña en la
aplicación Marketing por SMS de Konvergo ERP.](../../../../_images/ab-tests-sms.png)

En el primer campo, introduzca el porcentaje de destinatarios al que desea
aplicar la prueba A/B.

Debajo del campo «porcentaje» se encuentra el campo **selección del ganador**
y se utilizará para determinar el resultado exitoso de una prueba A/B. Es
decir, esto le dice a Konvergo ERP cómo elegir al ganador de la prueba A/B.

Las siguientes secciones están disponibles: **manual** , **mayor índice de
clics** , **leads** , **cotizaciones** o **ingresos**.

Por último, se encuentra el campo **enviar final en**. Representa la fecha y
hora que Konvergo ERP utiliza como fecha límite para determinar la variación de correo
ganadora. Luego, Konvergo ERP envía esa variación ganadora a los demás destinatarios
que no formaron parte de la prueba.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Cree con rapidez distintas versiones del correo para agregar a la prueba A/B al hacer clic en el botón <b>crear una versión alterna</b>.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Recuerde que la variación de correo ganadora depende de los criterios que seleccionó en el campo <b>selección del ganador</b>.</p>
</div>

## Página de campañas

Para crear, editar o analizar cualquier campaña, haga clic en campañas en el
menú del encabezado de la aplicación **Marketing por SMS**. En la página de
**campañas** , cada campaña muestra información relacionada con los correos
vinculados a esa campaña (por ejemplo, el número de correos electrónicos,
publicaciones en redes sociales, mensajes de SMS y notificaciones push).

![Tablero donde se ven distintas campañas en la aplicación Marketing por SMS
de Konvergo ERP, separadas por etapa.](../../../../_images/campaigns-page.png)

## Plantillas de campaña

Haga clic en **crear** para crear una nueva campaña. Konvergo ERP abrirá un formulario
de plantilla de campaña en blanco para que lo complete. Por otro lado,
seleccione cualquier campaña creada previamente para duplicarla, revisarla o
editar su formulario de plantilla de campaña.

![Vista de una plantilla de campaña de SMS en la aplicación Marketing por SMS
de Konvergo ERP.](../../../../_images/sms-campaign-template.png)

En cada campaña, las opciones para **enviar nuevo correo** , **enviar SMS** ,
**enviar publicación de redes sociales** y **notificaciones push** están
disponibles en el formulario de la plantilla.

Cuando se agrega a la campaña una de esas opciones de comunicación, Konvergo ERP
creará una nueva pestaña correspondiente en el formulario de la plantilla, en
donde se pueden revisar o editar esos tipos de mensaje, junto con varios
conjuntos de datos relacionados con cada correo específico.

En la parte superior de la plantilla se encuentran varios botones analíticos.
Cuando se hace clic en ellos, Konvergo ERP abre las métricas detalladas relacionadas
con ese tema específico (por ejemplo, **interacciones** , **oportunidades** ,
etc.) en una página separada.

Debajo de los botones inteligentes se encuentran los campos **nombre de la
campaña** y **responsable**. Konvergo ERP también permite agregar varias **etiquetas**
(si es necesario).

## Enviar SMS mediante la aplicación Contactos

Puede enviar mensajes SMS desde el formulario de contacto de forma
predeterminada.

Para enviar un SMS de esta forma, vaya a la aplicación Contactos, seleccione
el contacto deseado en la base de datos y haga clic en el icono **SMS** del
formulario de contacto (que se encuentra ubicado junto al campo **Número de
teléfono**).

![El icono de SMS se ubica en el formulario de contacto de un individuo en la
aplicación Contactos de Konvergo ERP.](../../../../_images/sms-contact-form.png)

Para enviar un mensaje a varios contactos a la vez, vaya al tablero principal
de la aplicación Contactos, elija la **vista de lista** y seleccione todos los
contactos a los que desea enviar el mensaje. Luego, en **acción** , selecione
**enviar SMS**.

![Seleccione un número de contactos, haga clic en acción y seleccione "enviar
varios SMS".](../../../../_images/sms-contacts-action-send-message.png)

## Configurar plantillas de SMS para usos posteriores

Para configurar **plantillas de SMS** para usar en el futuro, active el [modo
desarrollador](../../../general/developer_mode#developer-mode). Para
hacerlo, vaya al tablero principal de Konvergo ERP y seleccione la aplicación Ajustes.
Luego, baje a la sección **herramientas de desarrollador** y haga clic en
**activar el modo de desarrollador**.

Una vez que active el _modo desarrollador_ , volverá al tablero principal de
Konvergo ERP, y ahora aparecerá un icono de bug, el cual se ubica en la esquina
superior derecha del tablero. Este icono de bug indica que el modo de
desarrollador está activo.

Regrese a la aplicación Ajustes. En los menús que ahora aparecen en la parte
superior seleccione Técnico ‣ Plantillas SMS para empezar a configurar las
plantillas de SMS para sus próximas campañas de marketing.

![Seleccione la opción "plantilla de SMS" en el menú desplegable técnico en la
aplicación Ajustes.](../../../../_images/sms-template-setting.png)

En el tablero de **plantillas de SMS** , Konvergo ERP abre una página entera con
plantillas de SMS. La vista de **lista** predeterminada muestra el nombre de
cada plantilla y a qué destinatarios se aplica.

En esta página puede editar o crear plantillas de SMS desde cero.

![La página de plantillas de SMS en Konvergo ERP está disponible después de habilitar
en el modo de desarrollador en los ajustes
generales.](../../../../_images/sms-template.png)

  *[SMS]: Servicio de mensajes cortos

