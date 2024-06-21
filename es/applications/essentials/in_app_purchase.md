# Compras dentro de la aplicación (IAP)

Las compras dentro de la aplicación (conocidas como IAP) son servicios
opcionales que mejoran las bases de datos de Konvergo ERP y cada uno de ellos
proporciona sus propias funciones. Consulte la lista completa de servicios en
el [catálogo de IAP de Konvergo ERP](https://iap.odoo.com/iap/all-in-app-services).

![El catálogo de compras dentro de la aplicación con varios servicios
disponibles en iap.odoo.com.](../../_images/iap.png) <div class="alert alert-success">
<p class="alert-title">
Example</p><p>El servicio de <b>SMS</b> envía mensajes de texto a sus contactos directo desde la base de datos. El servicio de <b>digitalización de documentos</b> digitaliza facturas de proveedores, gastos y currículums escaneados o en formato PDF con reconocimiento óptico de caracteres (OCR) e inteligencia artificial (IA).</p>
</div>

**No** es necesario que configure los servicios de IAP antes de usarlos. Los
usuarios de Konvergo ERP pueden hacer clic en el servicio en la aplicación para
activarlo. Sin embargo, cada servicio necesita de sus propios créditos
prepagados, y cuando se agotan, los usuarios **deben** comprar más para seguir
utilizándolos.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Los usuarios de Konvergo ERP Enterprise con una suscripción válida obtendrán créditos gratuitos para probar las funciones de compras dentro de la aplicación antes de que decidan comprar más créditos para la base de datos. Esto incluye bases de datos de demostración y capacitación, bases de datos educativas y bases de datos gratuitas de una sola aplicación.</p>
</div>

## Servicios de compras dentro de la aplicación

Tanto Konvergo ERP como externos proporcionan los servicios de IAP, y tienen una
amplia variedad de usos.

Konvergo ERP ofrece los siguientes servicios de IAP:

  * **Digitalización de documentos** : digitaliza facturas de proveedores, gastos y currículums escaneados o en formato PDF con reconocimiento óptico de caracteres e inteligencia artificial.

  * **Autocompletado de contactos** : completa los registros de contacto de forma automática con datos empresariales.

  * **SMS** : envía mensajes de texto SMS a sus contactos directo desde la base de datos.

  * **Generación de leads** : genera leads según un conjunto de criterios y convierte a los visitantes del sitio web en leads y oportunidades de calidad.

  * **Correo postal** : envía facturas de clientes y reportes de seguimiento por correo postal por todo el mundo.

  * **Identifíquese con itsme®️ para firmar sus documentos** : solicítele a los signatarios de _Firma electrónica_ de Konvergo ERP que proporcionen su identidad a través de la plataforma de identidad _itsme‍®_. Solo está disponible en Bélgica y los Países Bajos.

Visite el [catálogo de IAP de Konvergo ERP](https://iap.odoo.com/iap/all-in-app-
services) para obtener más información sobre los servicios disponibles por el
momento (los ofrecen desarrolladores externos a Konvergo ERP).

### Uso de los servicios de compras dentro de la aplicación

Los servicios de IAP están integrados con Konvergo ERP de forma automática y **no** es
necesario que los usuarios configuren ningún ajuste. Para utilizar un servicio
solo deberá interactuar con el desde cualquier lugar de la base de datos.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>El siguiente flujo está relacionado con el servicio de <em>SMS</em> de <abbr title="In-app purchases">IAP</abbr> que se utiliza desde el registro de un contacto.</p>
<p>Puede hacer esto si hace clic en el icono <b>📱 SMS</b> dentro de la base de datos.</p>
<img alt="El icono de SMS en un formulario de información de contacto típico ubicado dentro de una base de datos de Konvergo ERP." class="align-center" src="../../_images/sms-icon.png"/>
<p>Los siguientes pasos describen una de las maneras de utilizar el servicio <em>SMS</em> de <abbr title="In-app purchases">IAP</abbr> con Konvergo ERP:</p>
<p>Vaya a la aplicación Contactos y haga clic en un contacto con un número telefónico disponible en el campo <b>Teléfono</b> o <b>Celular</b> del formulario de contacto.</p>
<p>Busque el icono <b>📱 SMS</b> que aparecen de lado derecho de los campos <b>Teléfono</b> o <b>Celular</b>. Al hacer clic en el icono <b>📱 SMS</b> aparece la ventana emergente <b>Enviar mensaje de texto SMS</b>.</p>
<p>Escriba un mensaje en el campo <b>Mensaje</b> de la ventana emergente, haga clic en el botón <b>Enviar SMS</b>. Konvergo ERP enviará el mensaje, vía SMS, al contacto y registrará lo que envió en el <em>chatter</em> del formulario del contacto.</p>
<p>Los créditos prepagados para el servicio <em>SMS</em> de <abbr title="In-app purchases">IAP</abbr> se restan en automático de los créditos existentes una vez que se envió el mensaje SMS. Konvergo ERP le solicitará al usuario que compre más créditos en caso de que no haya suficientes para enviar el mensaje.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p>Consulte la siguiente documentación para obtener más información sobre cómo utilizar varios servicios de <abbr title="In-app purchases">IAP</abbr> e instrucciones más detalladas relacionadas con la funcionalidad de SMS en Konvergo ERP:</p>
<ul>
<li><p><a href="../sales/crm/acquire_leads/lead_mining">Minado de leads</a></p></li>
<li><p><a href="../sales/crm/optimize/partner_autocomplete">Enriquecer la base de contactos con la función Autocompletar contacto</a></p></li>
<li><p><a href="../marketing/sms_marketing/essentials/sms_essentials">Fundamentos de SMS</a></p></li>
</ul>
</div>

## Créditos de compras dentro de la aplicación

Cada que utiliza un servicio de IAP gasta los créditos prepagados para ese
servicio. Konvergo ERP le solicitará comprar más créditos cuando no cuenta con
suficientes para seguir utilizando un servicio. También pueden configurar
alertas por correo electrónico para cuando le queden pocos créditos.

Los créditos se compran en _paquetes_ con el [catálogo de IAP de
Konvergo ERP](https://iap.odoo.com/iap/all-in-app-services) y los precios son
específicos para cada servicio.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>El <a href="https://iap.odoo.com/iap/in-app-services/1">servicio de SMS</a> cuenta con cuatro paquetes disponibles en las siguientes denominaciones:</p>
<ul>
<li><p><b>Paquete inicial</b>: 10 créditos.</p></li>
<li><p><b>Paquete estándar</b>: 100 créditos.</p></li>
<li><p><b>Paquete avanzado</b>: 500 créditos.</p></li>
<li><p><b>Paquete experto</b>: 1000 créditos.</p></li>
</ul>
<img alt="Cuatro paquetes de créditos distintos para el servicio SMS de IAP." class="align-center" src="../../_images/packs.png"/>
<p>El número de créditos consumidos depende de la longitud del SMS y el país de destino.</p>
<p>Consulte la documentación sobre <a href="../marketing/sms_marketing/pricing/pricing_and_faq">Precios de SMS y preguntas frecuentes</a> para obtener más información.</p>
</div>

### Comprar créditos

De forma automática, la base de datos le solicitará comprar más créditos si no
cuenta con suficientes para realizar una tarea.

Los usuarios pueden acceder a Ajustes ‣ sección Contactos para consultar el
saldo actual de créditos para cada servicio y comprar más de forma manual. Una
vez allí, vaya a **Compras dentro de la aplicación de Konvergo ERP** y haga clic en
**Ver mis servicios**.

Esta acción abrirá la página **Mis servicios** en donde aparecen varios
servicios de IAP de la base de datos. Una vez allí, haga clic en un servicio
de IAP para abrir la página de **Información de la cuenta** , ahí podrá
comprar créditos adicionales.

#### Comprar créditos de forma manual

Siga estos pasos para comprar créditos de forma manual en Konvergo ERP:

Vaya a la aplicación Ajustes y escriba `Compras dentro de la aplicación` en la
**barra de búsqueda** o diríjase a la sección **Contactos**. Si va a la
sección **Contactos** section, busque **Compras dentro de la aplicación de
Konvergo ERP** y haga clic en **Ver mis servicios**.

![La aplicación Ajustes muestra el encabezado de Compras dentro de la
aplicación de Konvergo ERP y el botón Ver mis servicios.](../../_images/view-
services.png)

Esta acción abrirá la página de **Cuenta para compras dentro de la
aplicación** en donde aparecen varios servicios de IAP de la base de datos.
Una vez allí, haga clic en un servicio de IAP para abrir sus respectivos
detalles, también podrá comprar créditos adicionales.

Haga clic en el botón **Comprar créditos** de esa página. La acción anterior
abrirá la página **Comprar créditos para (Cuenta de compras dentro de la
aplicación)** en una nueva pestaña. Busque el paquete de créditos que desea
adquirir y haga clic en **Comprar**. Siga las indicaciones para proporcionar
los detalles de pago y confirmar su orden.

![La página del servicio de SMS en iap.odoo.com muestra cuatro paquetes de
créditos disponibles para comprar.](../../_images/buy-pack.png)

Una vez que la transacción haya terminado podrá usar los créditos en la base
de datos.

#### Notificación sobre pocos créditos

Reciba notificaciones cuando tenga pocos créditos para que no se quede sin
ellos al usar un servicio de IAP. Siga las instrucciones a continuación:

Vaya a la aplicación Ajustes y escriba `Compras dentro de la aplicación` en la
**barra de búsqueda**. En la sección **Contactos** section, busque **Compras
dentro de la aplicación de Konvergo ERP** y haga clic en **Ver mis servicios**.

Las cuentas de IAP disponibles aparecen en una vista de lista en la página
**Cuenta para compras dentro de la aplicación**. Allí haga clic en la cuenta
IAP deseada para ver los detalles de ese servicio.

En la página de detallles seleccione la casilla **Recibir advertencia de
límite**. Esta acción abrirá dos campos en el formulario: **Límite de
advertencia** y **Correo de contacto**.

En el campo **Límite de advertencia** escriba el número de créditos que Konvergo ERP
usará como límite mínimo para este servicio y en el campo **Correo de
contacto** escriba el correo electrónico en el que desea recibir la
notificación.

Konvergo ERP enviará una alerta de créditos bajos al **correo electrónico de
contacto** cuando el saldo o balance de créditos caiga por debajo de la
cantidad especificada en el **límite de advertencia**.

  *[IAP]: In-app purchases

