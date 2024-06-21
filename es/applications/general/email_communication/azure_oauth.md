# Conecte Microsoft Outlook 365 a Konvergo ERP con Azure OAuth

Konvergo ERP es compatible con el Azure OAuth de Microsoft para Microsoft 365. Para
enviar y recibir correos seguros con un dominio personalizado, solo necesita
realizar algunos ajustes en la plataforma de Azure y en el backend de su base
de datos de Konvergo ERP. Esta configuración funciona ya sea con una dirección de
correo personal o una dirección creada con un dominio personalizado.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="https://learn.microsoft.com/es-mx/azure/active-directory/develop/quickstart-register-app">Microsoft Learn: Registro de una aplicación en la plataforma de identidad de Microsoft</a></p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../users/azure">Autenticación de inicio de sesión de Microsoft Azure</a></p></li>
<li><p><a href="../../productivity/calendar/outlook">Sincronizar el calendario de Outlook con Konvergo ERP</a></p></li>
</ul>
</div>

## Configuración en el portal de Microsoft Azure

### Crear una nueva aplicación

Primero, vaya al [portal de Microsoft Azure](https://portal.azure.com/).
Inicie sesión con la cuenta de **Microsoft Outlook Office 365** si tiene una,
de lo contrario inicie sesión con su **cuenta personal de Microsoft**.
Necesitará un usuario con acceso de administrador a los ajustes de Azure para
conecta y configurar los siguientes ajustes. Luego, vaya a la sección llamada
:guilabel:`Gestionar ID de Microsoft Entra (antes *Directorio activo de
Azure).

Ahora, haga clic en **Agregar (+)** en la parte superior del menú y seleccione
**Registro de aplicación**. En la pantalla de **Registre una aplicación** ,
cambie el nombre en **Nombre** a `Konvergo ERP` o algo que pueda reconocer. En la
sección **Tipos de cuentas compatibles** , seleccione guilabel:`Cuentas en
cualquier directorio organizacional (directorio Microsoft Entra ID -
Multitenant) y cuentas de Microsoft personales (por ejemplo, Skype, Xbox)`.

En la sección **Redirect URL** (redericción de URL) seleccione la plataforma
**Web** y después ponga `https://<odoo base url>/microsoft_outlook/confirm` en
el campo **URL**. La URL base de Konvergo ERP es el dominio canónico en el que su
instancia de Konvergo ERP puede ser contactada en el campo URL.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p><em>mydatabase.odoo.com</em>, donde <em>mydatabase</em> es el prefijo del subdominio de la base de datos, asumiendo que está alojada en Konvergo ERP.com.</p>
</div>

Una vez que se agregó la URL al campo, **registre** la aplicación para
crearla.

### Permisos de la API

Ahora tiene que configurar **los permisos del API**. Konvergo ERP necesita permisos
API para poder leer (IMAP) y enviar (SMTP) correos en la configuración de
Microsoft 365. Primero, haga clic en el enlace **permisos API** que se
encuentra en la barra izquierda del menú. Después, haga clic en el botón **(+)
Add a Permission** (agregar un permiso) y seleccione **Microsoft Graph**
(gráfica de Microsoft) en **Commonly Used Microsoft APIs** (API de Microsoft
que más se usan).

En la barra de búsqueda, busque **Delegated permissions** (permisos delegados)
y haga clic en **Add permissions** (agregar permisos) para cada uno:

  * **SMTP.Send**

  * **IMAP.AccessAsUser.All**

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El permiso <b>User.Read</b> se agregará de manera automática.</p>
</div> ![Los permisos para API que se necesitan para la
integración con Konvergo ERP están enlistados abajo de la gráfica de
Microsoft.](../../../_images/permissions.png)

## Asignación de usuarios y grupos

Después de agregar los permisos API regrese al **Overview** (resumen) de la
**aplicación** hasta arriba del menú de la barra lateral izquierda.

Ahora, agregue usuarios a esta aplicación. En la tabla de resumen
**Essentials** (esenciales) haga clic en el enlace llamado **Managed
Application in Local Directory** (aplicación gestionada en el directorio
local) o la última opción en el lado derecho inferior de la tabla.

![Para agregar usuarios o grupos haga clic en el enlace de Managed application
in local directory \(aplicación gestionada en el directorio local\) de la
aplicación que creó.](../../../_images/managed-application.png)

En el menú del lado izquierdo, seleccione **Users and Groups** (usuarios y
grupos). Después, haga clic en **(+) Add User/Group** (agregar un usuario o
grupo). Dependiendo de la cuenta podrá agregar ya sea un **grupo** y un
**usuario** o solo un **usuario**. En las cuentas personales solo es posible
agregar **usuarios**.

En **usuarios** o **grupos** , haga clic en **None Selected** (ninguno
seleccionado) y agrege los usuarios o el grupo de usuarios que enviará correos
desde **la cuenta de Microsoft** en Konvergo ERP. **Agregue** a los usuarios o grupos,
haga clic en guilabel:`Select` (seleccionar) y después **Assign** (asígnelos)
a la aplicación.

### Creación de credenciales

Ya que configuró la aplicación de Microsoft Azure, ahora necesita crear
credenciales para la configuración en Konvergo ERP. Estas credenciales incluyen
**Client ID** y **Client Secret**. Para empezar, podrá copiar el **Client ID**
desde la página **Overview** de la aplicación. El **Client ID** o el
**Application ID** se encuentra bajo **Display Name** en la parte de
**Essentials** del resumen de la aplicación.

![Application/Client ID que se encuentra en el resumen de la
aplicación.](../../../_images/application-id.png)

Ahora tiene que obtener el **Client Secret Value** (valor secreto del
cliente). Para obtener este valor haga clic en el botón **Certificates &
Secrets** (certificados y secretos) que se encuentra en el menú de la barra
izquierda. Ahora tendrá que producir un **Client Secret** (secreto de cliente)
y para hacerlo tiene que hacer clic en el botón **(+) New Client Secret**
(nuevo secreto del cliente).

Aparecerá una ventana en la derecha con el botón **Add a client secret**
(agregar un secreto de cliente). En **Description** (descripción) escriba
`Konvergo ERP Fetchmail` o algo que usted pueda reconocer y después agregue una
**expiration date** (fecha de caducidad).

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Si el primer secreto caduca, tendrá que configurar un <b>secreto de cliente nuevo</b>. Si esto ocurre, es posible que el servicio se interrumpa, así que configure esta fecha para que sea la fecha más lejana posible.</p>
</div>

Después de que haya ingresado estos dos valores haga clic en **Add**
(agregar). Así se crearán un **Client Secret Value** (valor secreto del
cliente) y un **ID secreto**. Es importante copiar el **Value** (valor) o el
**Client Secret Value** (valor secreto del cliente) en un bloc de notas ya que
estos valores se encriptarán una vez que deje esta página. No necesita el
**Secret ID** (ID secreto).

![Valor secreto del cliente o valor en las credenciales de la
aplicación.](../../../_images/secretvalue.png)

Si siguió todos los pasos, tendrá la información siguiente disponible para
agregarla a Konvergo ERP:

  * Un ID de cliente (**Client ID** o **Application ID**)

  * Un secreto del cliente (**Value** o **Client Secret Value**)

Este es el final de la configuración en el **portal de Microsoft Azure**.

## Configuración en Konvergo ERP

### Ingresar credenciales de Microsoft Outlook.

Primero, abra la base de datos de Konvergo ERP y vaya al módulo **Aplicaciones**.
Después, quite el filtro **Aplicaciones** de la barra de búsqueda y escriba
`Outlook`. Después de eso, instale el módulo llamado **Microsoft Outlook**.

Vaya a Ajustes ‣ Ajustes generales y asegúrese de que el botón **Servidores
personalizados de correo electrónico** , que se encuentra en la sección
**Conversaciones** esté activado. De esta manera aparecerá una nueva opción
llamada **credenciales de Outlook**.

**Guarde** el progreso.

Después, copie y pegue el **Client ID** (ID de la aplicación) y el **Client
Secret (valor secreto del cliente)** en los campos respectivos. Al finalizar,
**guarde** los cambios.

![Credenciales de Outlook en los ajustes generales de
Konvergo ERP.](../../../_images/outlookcreds.png)

### Configurar servidor de correos electrónicos salientes

En la página de los **ajustes generales** vaya a la parte de **Servidores
personalizados de correo electrónico** y haga clic en el enlace **Servidores
de correo saliente** para configurar su cuenta de Microsoft.

Cree un nuevo servidor de correo electrónico y marque la casilla de
**Outlook**. Ahora, llene el **nombre** (puede ser lo que sea) y el **nombre
se usuario** del correo electrónico de Microsoft Outlook.

Si el campo **Filtro «de»** está vacío, ingrese ya sea un [dominio o una
dirección de correo electrónico](email_servers#email-communication-
default).

Después, haga clic en **Conecte su cuenta de Outlook**.

Se abrirá una nueva ventana de Microsoft para completar **el proceso de
autorización**. Seleccione la misma dirección de correo electrónico que está
configurando en Konvergo ERP.

![Página de permito para permitir el acceso entre la nueva aplicación y
Konvergo ERP.](../../../_images/verify-outlook.png)

Haga clic en **sí** para permitir que Konvergo ERP acceda a su cuenta de Microsoft.
Después, la página lo redireccionará de regreso al **Servidor de correos
salientes** que acaba de crear. La configuración carga automáticamente el
**token** en Konvergo ERP y también aparecerá una etiqueta verde llamada **Token de
Outlook válido**.

![Indicador de que el token de Outlook es válido.](../../../_images/outlook-
token.png)

Ahora haga clic en **probar conexión** , debería aparecer un mensaje de
confirmación. Ahora, la base de datos de Konvergo ERP puede enviar correos seguros a
través de Microsoft Outlook con la ayuda de la autenticación OAuth.

#### Configuración con un solo servidor de correos electrónicos salientes

Configurar un solo servidor de salida es de las opciones más simples
disponibles para Microsoft Azure y no requiere derechos de acceso tan extensos
para los usuarios de la base de datos.

Debe usar una dirección de correo electrónico para enviar correos a todos los
usuarios dentro de la base de datos. Por ejemplo, se puede estructurar con un
alias de `notificaciones` (`notificaciones@ejemplo.com`) o un alias de
`contacto` alias (`contacot@ejemplo.com`). Esta dirección debe estar
establecida como **Filtrado DESDE** en el servidor. También debe coincidir con
la combinación clave `{mail.default.from}@{mail.catchall.domain}` en los
parámetros del sistema.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p>Puede obtener más información acerca del filtro desde, consulte: <a href="email_servers#email-communication-default"><span class="std std-ref">Utilizar una dirección de correo electrónico «De» predeterminada</span></a>.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Puede acceder a los <b>Parámetros del sistema</b> activando el <span class="xref std std-ref">modo desarrollador</span> en Ajustes ‣ Técnico‣ Parámetros‣ Parámetros del sistema.</p>
</div>

Al usar esta configuración, cada correo que se envíe desde la base de datos,
utilizará la dirección establecida en el buzón de `notificación`. Sin embargo,
debe tener en cuenta que el nombre del remitente aparecerá pero su dirección
de correo cambiará.

![Nombre desde un remitente real con un correo
estático.](../../../_images/from-name-remain.png) <div class="alert alert-success">
<p class="alert-title">
Example</p><p>Configuración para un solo servidor de correos salientes:</p>
<ul>
<li><p><em>Nombre de usuario</em> (inicio de sesión) del servidor de correo electrónico saliente = <code>notificaciones@ejemplo.com</code></p></li>
<li><p>Servidor de correo electrónico de salida <b>FROM Filtering = `notificaciones@ejemplo.com</b></p></li>
<li><p><code>mail.catchall.domain</code> en los parámetros del sistema = <code>ejemplo.com</code></p></li>
<li><p><code>mail.default.from</code> en los parámetros del sistema = <code>notificaciones</code></p></li>
</ul>
</div>

#### Configuración específica del usuario (varios usuarios)

Además de un servidor genérico para correo electrónico, es posible configurar
servidores de correo individuales para para usuarios dentro de una base de
datos. Estas direcciones de correo se deben configurar como **FROM Filtering**
en cada servidor individual para que esta configuración funcione.

Esta es la configuración más difícil de las dos configuraciones con Microsoft
Azure ya que requiere que configuremos servidores de correo para cada usuario,
de esta manera tendrán derechos de acceso a los ajustes y se podrá establecer
una conexión al servidor del correo.

##### Configurar

Tendrá que configurar un servidor diferente para cada usuario. Debe configurar
el filtro **FROM Filtering** de tal manera que solo se envíen correos de ese
usuario desde ese servidor. En otras palabras, tiene que configurar el
servidor de tal manera que solo el usuario que tenga la misma dirección de
correo que el filtro **FROM Filtering** pueda usar el servidor.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p>Puede obtener más información acerca del filtro desde, consulte: <a href="email_servers#email-communication-default"><span class="std std-ref">Utilizar una dirección de correo electrónico «De» predeterminada</span></a>.</p>
</div>

Debe configurar un servidor de respaldo para permitir que se envíen
**notificaciones**. El **FROM Filtering** de este servidor debe tener el valor
de `{mail.default.from}@{mail.catchall.domain}`.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Puede acceder a los <b>Parámetros del sistema</b> activando el <span class="xref std std-ref">modo desarrollador</span> en Ajustes ‣ Técnico‣ Parámetros‣ Parámetros del sistema.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../users/azure">Autenticación de inicio de sesión de Microsoft Azure</a></p></li>
<li><p><a href="../../productivity/calendar/outlook">Sincronizar el calendario de Outlook con Konvergo ERP</a></p></li>
</ul>
</div>0 <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../users/azure">Autenticación de inicio de sesión de Microsoft Azure</a></p></li>
<li><p><a href="../../productivity/calendar/outlook">Sincronizar el calendario de Outlook con Konvergo ERP</a></p></li>
</ul>
</div>2

### Configure un servidor de correo electrónico de llegada

La cuenta de llegada se debe configurar casi igual al servidor de salida. Vaya
al **menú técnico** y en **Servidores de correo entrante** **cree** una nueva
configuración. Seleccione el botón junto a **Autenticación OAuth de Outlook**
e inserte el **nombre de usuario de Microsoft Outlook** , después, haga clic
en **Conecte su cuenta de Outlook**. Recibirá un aviso que dirá **Token de
Outlook válido** , por lo que ahora solo tiene que **confirmar y probar** la
cuenta, que ya debería estar lista para recibir correos en la base de datos de
Konvergo ERP.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../users/azure">Autenticación de inicio de sesión de Microsoft Azure</a></p></li>
<li><p><a href="../../productivity/calendar/outlook">Sincronizar el calendario de Outlook con Konvergo ERP</a></p></li>
</ul>
</div>3

