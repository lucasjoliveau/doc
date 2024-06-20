# Compras dentro de la aplicación (IAP)

Las compras dentro de la aplicación (conocidas como IAP) son servicios
opcionales que mejoran las bases de datos de Odoo y cada uno de ellos
proporciona sus propias funciones. Consulte la lista completa de servicios en
el [catálogo de IAP de Odoo](https://iap.odoo.com/iap/all-in-app-services).

![El catálogo de compras dentro de la aplicación con varios servicios
disponibles en iap.odoo.com.](../../_images/iap.png)

Example

El servicio de SMS envía mensajes de texto a sus contactos directo desde la
base de datos. El servicio de digitalización de documentos digitaliza facturas
de proveedores, gastos y currículums escaneados o en formato PDF con
reconocimiento óptico de caracteres (OCR) e inteligencia artificial (IA).

**No** es necesario que configure los servicios de IAP antes de usarlos. Los
usuarios de Odoo pueden hacer clic en el servicio en la aplicación para
activarlo. Sin embargo, cada servicio necesita de sus propios créditos
prepagados, y cuando se agotan, los usuarios **deben** comprar más para seguir
utilizándolos.

Nota

Los usuarios de Odoo Enterprise con una suscripción válida obtendrán créditos
gratuitos para probar las funciones de compras dentro de la aplicación antes
de que decidan comprar más créditos para la base de datos. Esto incluye bases
de datos de demostración y capacitación, bases de datos educativas y bases de
datos gratuitas de una sola aplicación.

## Servicios de compras dentro de la aplicación

Tanto Odoo como externos proporcionan los servicios de IAP, y tienen una
amplia variedad de usos.

Odoo ofrece los siguientes servicios de IAP:

  * Digitalización de documentos: digitaliza facturas de proveedores, gastos y currículums escaneados o en formato PDF con reconocimiento óptico de caracteres e inteligencia artificial.

  * Autocompletado de contactos: completa los registros de contacto de forma automática con datos empresariales.

  * SMS: envía mensajes de texto SMS a sus contactos directo desde la base de datos.

  * Generación de leads: genera leads según un conjunto de criterios y convierte a los visitantes del sitio web en leads y oportunidades de calidad.

  * Correo postal: envía facturas de clientes y reportes de seguimiento por correo postal por todo el mundo.

  * Identifíquese con itsme®️ para firmar sus documentos: solicítele a los signatarios de _Firma electrónica_ de Odoo que proporcionen su identidad a través de la plataforma de identidad _itsme‍®_. Solo está disponible en Bélgica y los Países Bajos.

Visite el [catálogo de IAP de Odoo](https://iap.odoo.com/iap/all-in-app-
services) para obtener más información sobre los servicios disponibles por el
momento (los ofrecen desarrolladores externos a Odoo).

### Uso de los servicios de compras dentro de la aplicación

Los servicios de IAP están integrados con Odoo de forma automática y **no** es
necesario que los usuarios configuren ningún ajuste. Para utilizar un servicio
solo deberá interactuar con el desde cualquier lugar de la base de datos.

Example

El siguiente flujo está relacionado con el servicio de _SMS_ de IAP que se
utiliza desde el registro de un contacto.

Puede hacer esto si hace clic en el icono 📱 SMS dentro de la base de datos.

![El icono de SMS en un formulario de información de contacto típico ubicado
dentro de una base de datos de Odoo.](../../_images/sms-icon.png)

Los siguientes pasos describen una de las maneras de utilizar el servicio
_SMS_ de IAP con Odoo:

Vaya a la aplicación Contactos y haga clic en un contacto con un número
telefónico disponible en el campo Teléfono o Celular del formulario de
contacto.

Busque el icono 📱 SMS que aparecen de lado derecho de los campos Teléfono o
Celular. Al hacer clic en el icono 📱 SMS aparece la ventana emergente Enviar
mensaje de texto SMS.

Escriba un mensaje en el campo Mensaje de la ventana emergente, haga clic en
el botón Enviar SMS. Odoo enviará el mensaje, vía SMS, al contacto y
registrará lo que envió en el _chatter_ del formulario del contacto.

Los créditos prepagados para el servicio _SMS_ de IAP se restan en automático
de los créditos existentes una vez que se envió el mensaje SMS. Odoo le
solicitará al usuario que compre más créditos en caso de que no haya
suficientes para enviar el mensaje.

Ver también

Consulte la siguiente documentación para obtener más información sobre cómo
utilizar varios servicios de IAP e instrucciones más detalladas relacionadas
con la funcionalidad de SMS en Odoo:

  * [Minado de leads](../sales/crm/acquire_leads/lead_mining.html)

  * [Enriquecer la base de contactos con la función Autocompletar contacto](../sales/crm/optimize/partner_autocomplete.html)

  * [Fundamentos de SMS](../marketing/sms_marketing/essentials/sms_essentials.html)

## Créditos de compras dentro de la aplicación

Cada que utiliza un servicio de IAP gasta los créditos prepagados para ese
servicio. Odoo le solicitará comprar más créditos cuando no cuenta con
suficientes para seguir utilizando un servicio. También pueden configurar
alertas por correo electrónico para cuando le queden pocos créditos.

Los créditos se compran en _paquetes_ con el [catálogo de IAP de
Odoo](https://iap.odoo.com/iap/all-in-app-services) y los precios son
específicos para cada servicio.

Example

El [servicio de SMS](https://iap.odoo.com/iap/in-app-services/1) cuenta con
cuatro paquetes disponibles en las siguientes denominaciones:

  * Paquete inicial: 10 créditos.

  * Paquete estándar: 100 créditos.

  * Paquete avanzado: 500 créditos.

  * Paquete experto: 1000 créditos.

![Cuatro paquetes de créditos distintos para el servicio SMS de
IAP.](../../_images/packs.png)

El número de créditos consumidos depende de la longitud del SMS y el país de
destino.

Consulte la documentación sobre [Precios de SMS y preguntas
frecuentes](../marketing/sms_marketing/pricing/pricing_and_faq.html) para
obtener más información.

### Comprar créditos

De forma automática, la base de datos le solicitará comprar más créditos si no
cuenta con suficientes para realizar una tarea.

Los usuarios pueden acceder a Ajustes ‣ sección Contactos para consultar el
saldo actual de créditos para cada servicio y comprar más de forma manual. Una
vez allí, vaya a Compras dentro de la aplicación de Odoo y haga clic en Ver
mis servicios.

Esta acción abrirá la página Mis servicios en donde aparecen varios servicios
de IAP de la base de datos. Una vez allí, haga clic en un servicio de IAP para
abrir la página de Información de la cuenta, ahí podrá comprar créditos
adicionales.

#### Comprar créditos de forma manual

Siga estos pasos para comprar créditos de forma manual en Odoo:

Vaya a la aplicación Ajustes y escriba `Compras dentro de la aplicación` en la
barra de búsqueda o diríjase a la sección Contactos. Si va a la sección
Contactos section, busque Compras dentro de la aplicación de Odoo y haga clic
en Ver mis servicios.

![La aplicación Ajustes muestra el encabezado de Compras dentro de la
aplicación de Odoo y el botón Ver mis servicios.](../../_images/view-
services.png)

Esta acción abrirá la página de Cuenta para compras dentro de la aplicación en
donde aparecen varios servicios de IAP de la base de datos. Una vez allí, haga
clic en un servicio de IAP para abrir sus respectivos detalles, también podrá
comprar créditos adicionales.

Haga clic en el botón Comprar créditos de esa página. La acción anterior
abrirá la página Comprar créditos para (Cuenta de compras dentro de la
aplicación) en una nueva pestaña. Busque el paquete de créditos que desea
adquirir y haga clic en Comprar. Siga las indicaciones para proporcionar los
detalles de pago y confirmar su orden.

![La página del servicio de SMS en iap.odoo.com muestra cuatro paquetes de
créditos disponibles para comprar.](../../_images/buy-pack.png)

Una vez que la transacción haya terminado podrá usar los créditos en la base
de datos.

#### Notificación sobre pocos créditos

Reciba notificaciones cuando tenga pocos créditos para que no se quede sin
ellos al usar un servicio de IAP. Siga las instrucciones a continuación:

Vaya a la aplicación Ajustes y escriba `Compras dentro de la aplicación` en la
barra de búsqueda. En la sección Contactos section, busque Compras dentro de
la aplicación de Odoo y haga clic en Ver mis servicios.

Las cuentas de IAP disponibles aparecen en una vista de lista en la página
Cuenta para compras dentro de la aplicación. Allí haga clic en la cuenta IAP
deseada para ver los detalles de ese servicio.

En la página de detallles seleccione la casilla Recibir advertencia de límite.
Esta acción abrirá dos campos en el formulario: Límite de advertencia y Correo
de contacto.

En el campo Límite de advertencia escriba el número de créditos que Odoo usará
como límite mínimo para este servicio y en el campo Correo de contacto escriba
el correo electrónico en el que desea recibir la notificación.

Odoo enviará una alerta de créditos bajos al correo electrónico de contacto
cuando el saldo o balance de créditos caiga por debajo de la cantidad
especificada en el límite de advertencia.

  *[IAP]: In-app purchases

