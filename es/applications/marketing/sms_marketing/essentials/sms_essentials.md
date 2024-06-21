# Fundamentos de SMS

El contacto por SMS en las estrategias de comunicación puede ayudar a las
empresas a expandir su alcance en el mercado, sobre todo en algunos países
donde hacer uso del correo electrónico no es muy común o incluso no se
utiliza.

La aplicación _Marketing por SMS_ también puede ayudar a aumentar las tasas de
conversión en torno a acciones valiosas, como el registro a eventos, pruebas
gratis, compras, etc., ya que los canales de marketing basados en texto y
móvil suelen tener mejores resultados de CTOR y CTR.

## Tablero de Marketing por SMS

Cuando se abre la aplicación, Konvergo ERP muestra el tablero principal de **Marketing
por SMS** , el cual muestra los diversos envíos de SMS que se han creado,
junto con la información pertinente y los datos relacionados con ese mensaje
en específico.

La vista de **kanban** es la que Konvergo ERP utiliza de forma predeterminada cuando
se abre la aplicación, muestra una visualización organizada de los SMS que se
han creado y cuál es su estado actual.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Un <abbr title="Servicio de mensajes cortos">SMS</abbr> puede estar en alguno de los siguientes estados: <b>Borrador</b>, <b>En cola</b>, <b>Enviando</b> o <b>Enviado</b>.</p>
</div>

En la esquina superior derecha del tablero principal de **Marketing por SMS**
hay varias opciones de vista entre las que elegir. Cada una de ellas ofrece
una visión única de la misma información del SMS.

La vista de **lista** proporciona los mismos datos útiles relacionados con el
envío de SMS, pero en un diseño de lista más tradicional.

La vista de **calendario** proporciona un calendario simple, lo que facilita
ver cuándo se enviarán los SMS (o cuando se enviaron). Si se hace clic en una
fecha futura, Konvergo ERP abre una plantilla de SMS en blanco que, una vez
completada, se programará para enviarse en esa fecha específica en el futuro.

Por último, la vista de **gráfico** muestra los mismos datos relacionados con
SMS en series de gráficos y diagramas. Konvergo ERP también proporciona varias formas
de ordenar y agrupar los datos para un análisis más detallado.

## Crear mensajes de SMS

Para empezar, haga clic en **crear** en el tablero principal de **Marketing
por SMS** , Konvergo ERP abrirá un formulario de plantilla de SMS en blanco, el cual
se puede configurar de distintas formas.

![Creación de una plantilla de Marketing por SMS.](../../../../_images/sms-
create.png)

Primero, agregue un **asunto** para el envío, el cual describe de qué trata.

A continuación, en el campo **destinatarios** , elija a quién se le enviará
este SMS. De forma predeterminada, Konvergo ERP selecciona **lista de correo**. Si
esta es la opción deseada en el campo **destinatarios** , especifique a qué
lista de correo Konvergo ERP debe enviar este SMS en el campo **seleccionar lista de
correo**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Vaya a Listas de correo ‣ Lista de correo para crear (o editar) una lista de correo. Ahí, Konvergo ERP muestra todas las listas de correo creadas con anterioridad, junto con varios tipos de datos relacionados con esa lista en específico (por ejemplo, número de contactos, envíos, destinatarios y otra información).</p>
<p>Consulte <a href="mailing_lists_blacklists">Listas de correo y listas de exclusión</a> para obtener más información sobre listas de correo y contactos.</p>
</div> ![Vista de la página de listas de correo en la aplicación
de Marketing por SMS.](../../../../_images/sms-mailing-list1.png)

Para abrir todas las posibles opciones del campo **Destinatarios** haga clic
allí y podrá ver todas las opciones disponibles en Konvergo ERP.

Cuando selecciona otro campo (que no sea **lista de correo**), aparece la
opción de especificar aún más ese campo elegido, ya sea con una ecuación de
filtro de destinatario predeterminada que aparece en automático (y se puede
personalizar para cualquier empresa). Si no hay una ecuación de filtro de
destinatario predeterminada, aparecerá el botón **Agregar filtro**.

Hacer clic en el botón **Agregar filtro** agrega campos de reglas de dominio
totalmente personalizables que se pueden configurar de forma similar a una
ecuación. Puede crear varias reglas de destinatario si es necesario.

Konvergo ERP solo enviará el SMS a los destinatarios que cumplan con los criterios
configurados en esos campos. Tome en cuenta que es posible agregar varias
reglas.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>En caso de seleccionar <b>contacto</b>, todos los registros de <em>contacto</em> en la base de datos de Konvergo ERP (proveedores, clientes, entre otros) recibirán el <abbr title="Servicio de mensajes cortos">SMS</abbr> de forma predeterminada, a menos hayan reglas de destinatarios más específicas.</p>
<p>Por ejemplo, el siguiente mensaje solo se enviará a los contactos de la base de datos que se ubican en los Estados Unidos (por ejemplo, <code>País</code> &gt; <code>Nombre del país</code> es igual a <code>Estados Unidos</code>) y que no formen parte de una lista de exclusión de correo (por ejemplo, <code>Lista de exclusión</code> &gt; <code>es</code> &gt; <code>no establecido</code>).</p>
<img alt="Contactos destinatarios en la aplicación Marketing por SMS." class="align-center" src="../../../../_images/contact-recipient.png"/>
</div>

### Escribir mensajes de SMS

Introduzca el contenido del SMS en el campo de texto de la pestaña **contenido
del SMS**. Puede incluir enlaces y emojis. Konvergo ERP muestra debajo del texto
cuántos caracteres se utilizan en el mensaje, junto con cuántos envíos de SMS
se necesitarán para entregar el mensaje completo.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Haga clic en el icono <b>información</b> para revisar el precio de enviar un <abbr title="servicio de mensajes cortos">SMS</abbr> para un país.</p>
</div> ![Icono para revisar precios de
SMS.](../../../../_images/sms-price-check.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Debe comprar créditos en Konvergo ERP para aprovechar al máximo la aplicación <em>Marketing por SMS</em>, los mensajes de <abbr title="servicio de mensajes cortos">SMS</abbr> no se enviarán si no tiene créditos.</p>
</div>
<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="https://iap-services.odoo.com/iap/sms/pricing">SMS en Konvergo ERP - Preguntas frecuentes</a></p>
</div>

### Rastrear los enlaces que se utilizan en mensajes de SMS

Cuando se usan enlaces en mensajes de SMS , Konvergo ERP genera de manera automática
rastreadores de enlaces para recopilar datos analíticos y métricas
relacionadas con esos enlaces específicos. Se pueden encontrar en
Configuración ‣ Rastrear enlaces.

![Página para rastrear enlaces de SMS.](../../../../_images/sms-link-
tracker.png)

## Configurar los ajustes de SMS

En la pestaña **Ajustes** de la plantilla de SMS se encuentra la opción para
**incluir enlace de exclusión**. Si se activa, el destinatario puede darse de
baja de la lista de correos para no recibir cualquier correo futuro.

También se puede determinar a un empleado como **Responsable** en la sección
**seguimiento** de la pestaña **Ajustes**.

![Pestaña ajustes de SMS.](../../../../_images/sms-settings-tab.png)

## Enviar mensajes SMS

Una vez que se crea un envío, elija el momento en que Konvergo ERP debe entregar el
mensaje entre las siguientes opciones:

  * **Enviar** : envía el mensaje de forma inmediata. Considere usar esta opción si la lista de destinatarios es sobresaliente, o en casos que involucran una fecha límite cercana, como una oferta relámpago.

  * **Planificar** : elija un día (y hora) para que Konvergo ERP haga el envío. Por lo general esta es la mejor opción para los mensajes relacionados con un evento específico. Este método también se puede utilizar para promover una oferta de tiempo limitado, o para ayudar a planificar la estrategia de contenido de una empresa con anticipación.

  * **Prueba** : permite enviar un SMS a uno o varios números con fines de prueba. Recuerde usar una coma entre números telefónicos si se usan varios números como destinatarios.

## Visualización de reportes

En la página **Reportes** (a la que puede acceder con la opción Reportes en el
menú superior) hay opciones para aplicar distintas combinaciones de
**filtros** y **medidas** para visualizar las métricas en diferentes
presentaciones (por ejemplo, las vistas de **gráfico** , **lista** y
**cohorte**).

Cada opción de vista métrica en **Reportes** permite un análisis más extenso
de rendimiento de los mensajes SMS.

Por ejemplo, mientras la vista predeterminada es **gráfico** , los datos de
los SMS se visualizan como diferentes gráficos y tablas que se pueden ordenar
y agrupar de varias maneras (p. ej., el menú desplegable guilabel:`Medidas`).

![Página de reportes en Marketing por SMS.](../../../../_images/sms-reporting-
page.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Las acciones automatizadas de Konvergo ERP permiten enviar mensajes SMS y para hacer uso de estas acciones es necesario contar con la aplicación <em>Studio</em>.</p>
<p>Vaya a Aplicaciones para instalar <em>Studio</em> de Konvergo ERP. En la <b>barra de búsqueda</b> escriba <code>studio</code>.</p>
<p>Haga clic en clic <b>Instalar</b> si aún no está instalada.</p>
<p>El estado de su suscripción cambiará a <em>Personalizado</em> al agregar la aplicación <em>Studio</em>, lo que aumenta el costo. Comuníquese con <a href="https://www.odoo.com/contactus">soporte</a> o su gerente de la base de datos si tiene alguna pregunta sobre este cambio.</p>
<p>Active el <a href="../../../general/developer_mode#developer-mode"><span class="std std-ref">modo de desarrollador</span></a> para utilizar acciones automatizadas, vaya a Ajustes ‣ menú Técnico ‣ sección Automatización ‣ Acciones automatizadas y después haga clic en <b>Nuevo</b> para crear una acción.</p>
<p>Escriba el <b>nombre de la acción</b> y seleccione el <b>modelo</b> en el que se implementará esta acción.</p>
<p>Asegúrese de que el botón <b>Activo</b> esté <em>encendido</em>, (está representado por un botón verde), solo así se llevará a cabo la acción automatizada.</p>
<p>Configure el campo <b>Activar</b> con <b>Al crear</b>, <b>Al actualizar</b>, <b>Al crear y actualizar</b>, <b>Al eliminar</b>, <b>Según la modificación de formulario</b> o <b>Según la condición de tiempo</b>.</p>
<p>Pueden aparecer otros campos según lo que haya elegido en el campo <b>Activar</b>.</p>
<p>Es posible crear un filtro de registros con un dominio en el campo <b>Aplicar en</b>. Asegúrese de haber seleccionado un modelo antes de establecer cualquier dominio en el campo anterior. Haga clic en <b>Editar dominio</b> para establecer los parámetros de registro.</p>
<p>Seleccione <b>Enviar mensaje de texto SMS</b> en el campo desplegable <b>Acción a realizar</b>, establezca la <b>plantilla de SMS</b> y elija si el mensaje SMS se debe <b>registrar como nota</b> con la casilla ubicada junto a la opción correspondiente.</p>
<img alt="Una plantilla de acción automatizada con las secciones de acción por realizar, plantilla de SMS y registrar como nota destacadas en rojo." class="align-center" src="../../../../_images/automated-action-sms.png"/>
<p>Para implementar la acción automatizada puede guardarla dirigiéndose a otra parte o de forma manual (con el icono <b>☁️ (nube)</b>).</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="sms_campaign_settings">Ajustes de campaña de SMS</a></p></li>
<li><p><a href="mailing_lists_blacklists">Listas de correo y listas de exclusión</a></p></li>
<li><p><a href="../../../essentials/in_app_purchase">Compras dentro de la aplicación (IAP)</a></p></li>
</ul>
</div>

  *[SMS]: servicio de mensajes cortos
  *[CTOR]: tasa de clics abiertos
  *[CTR]: tasa de clics

