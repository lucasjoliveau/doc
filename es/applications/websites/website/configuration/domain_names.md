# Nombres de dominio

Los nombres de dominio son direcciones basadas en texto que identifican
ubicaciones en línea, como sitios web. También son más fáciles de recordar,
así las personas pueden navegar por internet sin tener que hacer uso de
direcciones IP numéricas.

Las bases de datos de **Konvergo ERP en línea** y **Konvergo ERP.sh** usan un **subdominio**
del **dominio** de `odoo.com` de forma predeterminada (por ejemplo,
`miempresa.odoo.com`).

Sin embargo, puede hacer uso de un nombre de dominio personalizado y registrar
un nombre de dominio gratuito (solo está disponible para las bases de datos de
Konvergo ERP en línea) o configurar uno que ya le pertenezca.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="https://www.odoo.com/slides/slide/register-a-free-domain-name-1663">Tutoriales de Konvergo ERP: registrar un nombre de dominio gratis [video]</a></p>
</div>

## Registre un nombre de dominio gratis con Konvergo ERP

Para registrar un nombre de dominio gratuito por un año para su base de datos
de Konvergo ERP en línea, inicie sesión en su cuenta y vaya al [gestor de bases de
datos](https://www.odoo.com/my/databases). Haga clic en el icono de engranaje
(**⚙️**) ubicado junto al nombre de la base de datos y seleccione **Nombres de
dominio**.

![Acceder a la configuración de nombres de dominio de una base de
datos.](../../../../_images/domain-names.png)

Busque el nombre de dominio deseado y verifique su disponibilidad.

![Buscar un nombre de dominio disponible.](../../../../_images/domain-
search.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si la opción para registrar  un nombre de dominio no aparece, primero asegúrese de que la aplicación Sitio web está instalada.</p>
</div>

Seleccione el nombre de dominio deseado, complete el formulario de
**Propietario del dominio** y haga clic en **Registrar**. El nombre de dominio
elegido se vinculará a la base de datos.

![Completar la información del propietario de
dominio.](../../../../_images/domain-owner.png)

Después debe mapear su nombre de dominio a su sitio web de Konvergo ERP.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Recibirá un correo electrónico de verificación de <code>noreply@domainnameverification.net</code> en la dirección que proporcionó en el formulario <b>Propietario del dominio</b>. Es muy importante que verifique su dirección de correo electrónico, así mantendrá el dominio activo y podrá recibir la cotización de renovación antes de que venza.</p>
</div>

El registro del nombre de dominio es gratis durante el primer año. Después de
este periodo, Konvergo ERP continuará gestionando el dominio con **Gandi.net** , el
registrador de nombres de dominio, y se le cobrará la [tarifa de renovación de
Gandi.net](https://www.gandi.net/en/domain). Cada año, Konvergo ERP envía una
cotización de renovación a la dirección de correo electrónico que estableció
en el formulario **Propietario del dominio** varias semanas antes de la fecha
de vencimiento del dominio. El dominio se renueva de forma automática cuando
confirma la cotización.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Esta oferta solo está disponible para las bases de datos de <b>Konvergo ERP en línea</b>.</p></li>
<li><p>La oferta está limitada a <b>un</b> nombre de dominio por cliente.</p></li>
<li><p>La oferta está limitada al registro de un <b>nuevo</b> nombre de dominio.</p></li>
<li><p>La oferta está disponible para los planes de <em>una aplicación gratis</em>. Asegúrese de que su sitio web incluya suficiente contenido original para que Konvergo ERP verifique que su solicitud es legítima y respeta la <a href="https://www.odoo.com/acceptable-use">Política de uso aceptable de Konvergo ERP</a>. Recibimos varias solicitudes, así que su revisión puede tardar varios días.</p></li>
</ul>
</div>

### Registros DNS

Para gestionar los registros DNS de su dominio gratuito, abra el [gestor de
bases de datos](https://www.odoo.com/my/databases), haga clic en el icono de
engranaje (**⚙️**) ubicado junto al nombre de la base de datos, seleccione
**Nombres de dominio** y haga clic en **DNS**.

  * **A** : el registro A contiene la dirección IP del dominio. Se crea de forma automática y **no** se puede editar ni eliminar.

  * **CNAME** : los registros CNAME se encargan de reenviar un dominio o subdominio a otro dominio. Uno se crea de forma automática para asignar el subdominio `www.` a la base de datos. Si cambia el nombre de la base de datos, también **deberá** cambiar el nombre del registro CNAME.

  * **MX** : los registros MX le indican a los servidores a dónde enviar los correos electrónicos.

  * **TXT** : los registros TXT sirven para cumplir con distintos propósitos (por ejemplo, para verificar la propiedad de un nombre de dominio).

Cualquier modificación a los registros DNS puede tardar hasta **72 horas** en
propagarse a todos los servidores.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p><a href="https://www.odoo.com/help">Envíe un ticket de soporte</a> si necesita ayuda para gestionar su nombre de dominio.</p>
</div>

### Buzón de correo

La oferta de un año de dominio gratis **no** incluye buzón de correo, pero hay
dos opciones para vincular su nombre de dominio con uno.

#### Usar un subdominio

Puede crear un subdominio (por ejemplo, `subdominio.sudominio.com`) para
usarlo como un dominio de seudónimo para la base de datos. Esto permite que
los usuarios creen registros en la base de datos a partir de los correos
electrónicos que reciben en su seudónimo `correo@subdominio.sudominio.com`.

Para ello, abra el [gestor de bases de
datos](https://www.odoo.com/my/databases), haga clic en el icono de engranaje
(**⚙️**) ubicado junto al nombre de la base de datos y vaya a Nombres de
dominio ‣ DNS ‣ Agregar registro DNS ‣ CNAME. Después, escriba el subdominio
deseado en el campo **Nombre** (por ejemplo, `subdominio`), el dominio
original de la base de datos con un punto al final (por ejemplo,
`miempresa.odoo.com.`) en el campo **Contenido** y haga clic en **Agregar
registro**.

Luego, agregue el dominio del seudónimo como su _propio dominio_. Haga clic en
**Usar mi propio dominio** , escriba el dominio del seudónimo (por ejemplo,
`subdominio.sudominio.com`), haga clic en **Verificar** y luego en **Confirmo,
está listo**.

Por último, vaya a su base de datos y abra **Ajustes**. Habilite los
**servidores de correo electrónico personalizados** , escriba el **dominio del
seudónimo** (por ejemplo, `subdominio.sudominio.com`) y haga clic en
**Guardar**.

#### Usar un proveedor de correo electrónico externo

Es necesario que configure un registro MX para poder utilizar un proveedor de
correo electrónico externo. Para ello, abra el [gestor de bases de
datos](https://www.odoo.com/my/databases), haga clic en el icono de engranaje
(**⚙️**) ubicado junto al nombre de la base de datos, haga clic en Nombres de
dominio ‣ DNS ‣ Agregar registro DNS ‣ MX. Los valores que agregará a los
campos **Nombre** , **Contenido** y **Prioridad** dependen del proveedor de
correo electrónico externo.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="https://support.google.com/a/answer/174125?hl=es">Valores de los registros MX de Google Workspace</a></p></li>
<li><p><a href="https://learn.microsoft.com/es-mx/microsoft-365/admin/get-help-with-domains/create-dns-records-at-any-dns-hosting-provider?view=o365-worldwide#add-an-mx-record-for-email-outlook-exchange-online">Agregar un registro MX para el correo electrónico (Outlook, Exchange Online)</a></p></li>
</ul>
</div>

## Configurar un nombre de dominio existente

Si ya cuenta con un nombre de dominio, puede usarlo para su sitio web de Konvergo ERP.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Le recomendamos que siga estos tres pasos <b>en orden</b> para evitar cualquier problema con la <a href="#domain-name-ssl"><span class="std std-ref">validación de certificados SSL</span></a>:</p>
<ol class="arabic simple">
<li><p><a href="#domain-name-cname"><span class="std std-ref">Agregue un registro CNAME</span></a>.</p></li>
<li><p><a href="#domain-name-db-map"><span class="std std-ref">Mapee su nombre de dominio a su base de datos de Konvergo ERP</span></a>.</p></li>
<li><p><a href="#domain-name-website-map"><span class="std std-ref">Mapee su nombre de dominio a su sitio web de Konvergo ERP</span></a>.</p></li>
</ol>
</div>

### Agregar un registro CNAME

Es necesario que agregue un registro CNAME para reenviar su nombre de dominio
a la dirección de su base de datos de Konvergo ERP.

Konvergo ERP OnlineKonvergo ERP.sh

La dirección de destino del registro CNAME debe ser la dirección de su base de
datos tal como la definió al crearla (por ejemplo, `miempresa.odoo.com`).

La dirección de destino del registro CNAME debe ser la dirección principal del
proyecto, disponible en Konvergo ERP.sh si se dirige a Ajustes ‣ Nombre del proyecto,
o una rama específica (producción, preproducción o desarrollo) si se dirige a
Ramas ‣ seleccione la rama ‣ Ajustes ‣ Dominios personalizados y hace clic en
**¿Cómo configurar mi dominio?**. Un mensaje le indicará a qué dirección debe
apuntar su registro CNAME.

Las instrucciones específicas dependen de su servicio de alojamiento de DNS.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="https://www.godaddy.com/help/add-a-cname-record-19236">GoDaddy: agregar un registro CNAME</a></p></li>
<li><p><a href="https://www.namecheap.com/support/knowledgebase/article.aspx/9646/2237/how-to-create-a-cname-record-for-your-domain">Namecheap: Cómo crear un registro CNAME para su dominio</a></p></li>
<li><p><a href="https://docs.ovh.com/us/en/domains/web_hosting_how_to_edit_my_dns_zone/#add-a-new-dns-record">OVHcloud: agregar un nuevo registro DNS (en inglés)</a></p></li>
<li><p><a href="https://support.cloudflare.com/hc/en-us/articles/360019093151">Cloudflare: gestionar registros DNS (en inglés)</a></p></li>
</ul>
</div> <div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Konvergo ERP solo admite subdominios. Para utilizar su dominio simple <span class="dfn"><span>(un nombre de dominio sin ningún subdominio o prefijo)</span></span> (<code>sudominio.com</code>), cree una redirección 301 para dirigir a los visitantes a <code>www.sudominio.com</code>.</p>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>Usted es propietario del nombre de dominio <code>sudominio.com</code> y la dirección de su base de datos de Konvergo ERP en línea es <code>miempresa.odoo.com</code>. Es común que desee acceder a su base de datos de Konvergo ERP con el dominio <code>www.sudominio.com</code> pero también con el dominio simple <code>sudominio.com</code>.</p>
<p>Para ello, deberá crear un registro CNAME para el subdominio <code>www</code> en el que el destino sea <code>miempresa.odoo.com</code> y después crear una redirección (3010 redirección permanente o visible) para redirigir a los visitantes de <code>sudominio.com</code> a <code>wwww.sudominio.com</code>.</p>
</div>

### Mapear un nombre de dominio a una base de datos de Konvergo ERP

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si la opción para registrar  un nombre de dominio no aparece, primero asegúrese de que la aplicación Sitio web está instalada.</p>
</div>0

Konvergo ERP OnlineKonvergo ERP.sh

Abra el [gestor de bases de datos](https://www.odoo.com/my/databases), haga
clic en el icono de engranaje (**⚙️**) ubicado junto al nombre de la base de
datos y vaya a Nombres de dominio ‣ Utilizar mi propio dominio. Luego, escriba
el nombre de dominio (por ejemplo, `tudominio.com`), haga clic en
**Verificar** y luego en **Confirmo, está listo**.

![Mapear un nombre de dominio a una base de datos de Konvergo ERP en
línea](../../../../_images/map-database-online.png)

En Konvergo ERP.sh, vaya a Ramas ‣ seleccione su rama ‣ Ajustes ‣ Dominios
personalizados, escriba el nombre de dominio a agregar y haga clic en
**Agregar dominio**.

![Mapear un nombre de dominio a una rama de Konvergo ERP.sh](../../../../_images/map-
database-sh.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si la opción para registrar  un nombre de dominio no aparece, primero asegúrese de que la aplicación Sitio web está instalada.</p>
</div>1

#### Cifrado SSL (protocolo HTTPS)

El **cifrado SSL** permite que los visitantes naveguen por un sitio web a
través de una conexión segura. Aparece con el protocolo _https://_ al
principio de una dirección web en lugar del protocolo no seguro _http://_.

Konvergo ERP genera un certificado SSL distinto para cada dominio mapeado a una base
de datos, mediante [la autoridad de certificación Let’s Encrypt y el protocolo
ACME](https://letsencrypt.org/how-it-works/).

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si la opción para registrar  un nombre de dominio no aparece, primero asegúrese de que la aplicación Sitio web está instalada.</p>
</div>2 <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si la opción para registrar  un nombre de dominio no aparece, primero asegúrese de que la aplicación Sitio web está instalada.</p>
</div>3

#### URL web base de la base de datos

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si la opción para registrar  un nombre de dominio no aparece, primero asegúrese de que la aplicación Sitio web está instalada.</p>
</div>4

La _URL web base_ o _URL raíz_ de una base de datos afecta la dirección de su
sitio web principal y todos los enlaces que sus clientes recibieron (por
ejemplo, cotizaciones, enlaces al portal, entre otros).

Para convertir su nombre de dominio personalizado en la _URL web base_ de su
base de datos, primero acceda a su base de datos con su nombre de dominio
personalizado e inicie sesión como administrador (un usuario que forma parte
del grupo de permisos de acceso a los ajustes en Administración).

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si la opción para registrar  un nombre de dominio no aparece, primero asegúrese de que la aplicación Sitio web está instalada.</p>
</div>5 <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si la opción para registrar  un nombre de dominio no aparece, primero asegúrese de que la aplicación Sitio web está instalada.</p>
</div>6

### Mapear un nombre de dominio a un sitio web de Konvergo ERP

Mapear su nombre de dominio a su sitio web no es igual a mapearlo a su base de
datos:

  * Define su nombre de dominio como el principal para su sitio web, lo que ayuda a los buscadores a indexar su sitio web de forma correcta.

  * Define su nombre de domino como la URL base para su base de datos e incluye los enlaces del portal enviados por correo electrónico a sus clientes.

  * En caso de que tenga varios sitios web, mapea su nombre de dominio al sitio web correcto.

Vaya a Sitio web ‣ Configuración ‣ Ajustes. En caso de que tenga varios sitios
web, seleccione el que desea configurar. Escriba la dirección de su sitio web
(por ejemplo, `https://www.sudominio.com`) en el campo **Dominio** y haga clic
en **Guardar**.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si la opción para registrar  un nombre de dominio no aparece, primero asegúrese de que la aplicación Sitio web está instalada.</p>
</div>7 <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si la opción para registrar  un nombre de dominio no aparece, primero asegúrese de que la aplicación Sitio web está instalada.</p>
</div>8

  *[DNS]: Sistema de nombres de dominio

