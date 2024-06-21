# Autenticación de inicio de sesión de Microsoft Azure

La autenticación de inicio de sesión de Microsoft OAuth con Azure es una
función útil que permite que los usuarios de Konvergo ERP inicien sesión con su cuenta
de Microsoft Azure en su base de datos.

Esto es muy útil, en especial si la empresa usa un área de trabajo de Azure y
quiere que los empleados se conecten a Konvergo ERP con su cuenta de Microsoft.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Las bases de datos que estén alojadas en Konvergo ERP.com no pueden iniciar sesión con OAuth si el usuario es el dueño o administrador de la base de datos; si esto ocurre, la base de datos se desvinculará de su cuenta de Konvergo ERP.com. Si configura OAuth para ese usuario, ya no podrá duplicar, cambiar el nombre, o gestionar esa base de datos desde el portal de Konvergo ERP.com.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../../productivity/calendar/outlook">Sincronizar el calendario de Outlook con Konvergo ERP</a></p></li>
<li><p><a href="../email_communication/azure_oauth">Conecte Microsoft Outlook 365 a Konvergo ERP con Azure OAuth</a></p></li>
</ul>
</div>

## Configuración

Para poder integrar la función de inicio de sesión de Microsoft es necesario
realizar la configuración entre Microsoft y Konvergo ERP.

### Parámetros del sistema de Konvergo ERP

Primero active el [modo desarrollador](../developer_mode#developer-mode)
y después vaya a Ajustes ‣ Técnico ‣ Parámetros del sistema.

Haga clic en **Nuevo** y en el formulario en blanco agregue el parámetro
`auth_oauth.authorization_header` como **Clave** y ponga to `1` como
**Valor**. Después los cambios se guardarán de forma automática, pero también
puede dar clic en el **icono con forma de nube** para guardarlos de forma
manual.

### Tablero de Microsoft Azure

#### Crear una nueva aplicación

Ya que configuró los parámetros de sistema desde Konvergo ERP, ahora debe crear una
aplicación correspondiente dentro de Microsoft Azure. Para crear una nueva
aplicación, vaya al [portal de Microsoft Azure](https://portal.azure.com/).
Inicie sesión con la cuenta de la empresa de **Microsoft Outlook Office 365**
, si no tiene una, inicie sesión con su **cuenta de Microsoft** personal.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Para poder realizar los pasos de configuración a continuación es necesario iniciar sesión con un usuario que tenga acceso de administrador a los <em>ajustes de Azure</em>.</p>
</div>

Luego, vaya a la sección con el nombre :guilabel:`Gestionar Microsoft Entra ID
` (antes conocido como _Azure Active Directory_). Por lo general, la ubicación
de este enlace se encuentra en el centro de la página.

Haga clic en el icono **Add (+)** (Agregar) que se encuentra en el menú
superior y después seleccione **App registration** (registro de aplicación)
del menú desplegable. En la pantalla **Register an application** (registrar
una aplicación) cambie el campo **Name** (nombre) a `Inicio de sesión Konvergo ERP en
OAuth` u otro título que pueda reconocer. En la sección **Supported account
types** (tipos de cuenta compatibles) seleccione la opción **Accounts in this
organizational directory only (Default Directory only - Single tenant)** (Solo
las cuentas de este directorio organizativo (solo el directorio
predeterminado: inquilino único)).

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Los <b>Supported account types</b> (tipos de cuentas compatibles) dependen del tipo de cuenta de Microsoft y el uso que se le quiere dar a OAuth. Por ejemplo, ¿el inicio de sesión es para usuarios dentro de una organización o para darle acceso de portal al cliente? La configuración de arriba es para usuarios dentro de una organización.</p>
<p>Si la audiencia será usuarios del portal, elija <b>Personal Microsoft accounts only</b> (solo cuentas personales de Microsoft). Si la audiencia será usuarios de la empresa, elija <b>Accounts in this organizational directory only (Default Directory only - Single tenant)</b> (Solo las cuentas de este directorio organizativo (solo el directorio predeterminado: inquilino único)).</p>
</div>

En la sección **Redirect URL** (URL de redirección), seleccione **Web** como
la plataforma y después ingrese `https://<odoo base url>/auth_oauth/signin` en
el campo **URL**. La URL base de Konvergo ERP es el elemento canonical en el campo
**URL** por el cual se puede llegar a su instancia de Konvergo ERP (por ejemplo,
_mibasededatos.odoo.com_ si está alojado en Konvergo ERP.com). Después, haga clic en
**Registrar** para crear la aplicación.

#### Autentificación

Para editar la autenticación de la nueva aplicación haga clic en
**Authentication** (autenticación) que se encuentra en el menú de la
izquierda. Haga esto después de que se le haya redirigido a los ajustes de la
aplicación después del paso previo.

A continuación, deberá elegir qué tipo de _tokens_ son necesarios para la
autenticación OAuth. Estos tokens no son monetarios, sino tokens de
autenticación que se transfieren entre Microsoft y Konvergo ERP. Estos tokens no
tienen costo, solo se usan para propósitos de autenticación entre dos API.
Vaya hasta la parte inferior de la pantalla y marque las casillas que digan
**Access tokens (used for implicit flows)** (Tokens de acceso (para flujos
implícitos)) y **ID tokens (used for implicit and hybrid flows)** (Tokens de
ID (para flujos híbridos e implícitos)) para seleccionar los tokens que debe
proporcionar el punto de conexión.

![Ajustes de autenticación y tokens de punto de
conexión.](../../../_images/authentication-tokens.png)

Haga clic en **Guardar** para asegurar que sus cambios se guardaron

#### Obtener las credenciales

Ya que se creó y autenticó la aplicación en la consola de Microsoft Azure,
ahora necesitamos obtener las credenciales. Para hacerlo, haga clic en la
opción **Overview** (vista general) que se encuentra en la columna de la
derecha. Seleccione y copie el **Application (client) ID** (identificador de
aplicación [cliente]) en la ventana que aparece. Pegue esta credencial en el
portapapeles o un bloc de notas, ya que usaremos esta credencial en Konvergo ERP más
adelante.

Después de finalizar este paso, haga clic en **Endpoints** en la parte
superior del menú y haga clic en el _icono de copiar_ junto al campo
**Autorización del endpoint OAuth 2.0 (v2)**. Pegue este valor en el bloc de
notas.

![Credenciales de autorización de endpoint para la aplicación ID y OAuth 2.0
\(V2\) ](../../../_images/overview-azure-app.png)

### Configuración en Konvergo ERP

Por último, debe configurar algunos ajustes de OAuth para Microsoft Azure en
Konvergo ERP. Vaya a Ajustes ‣ Integraciones ‣ Autenticación OAuth y seleccione la
casilla para activar la función de inicio de sesión de OAuth. Haga clic en
**Guardar** para asegurarse de que sus cambios se guardaron y luego inicie
sesión en la base de datos una vez que la pantalla de inicio de sesión cargue.

Una vez más, vaya a Ajustes ‣ Integraciones ‣ Autenticación OAuth y haga clic
en **Proveedores OAuth**. Ahora, seleccione **Nuevo** en la parte superior
izquierda y escriba el nombre del proveedor como `Azure`.

Pegue el **ID de aplicación (cliente)** de la sección anterior en el campo
**ID del cliente**. Después de completar esto, pegue el nuevo valor
**Autenticación de endpoint OAuth 2.0 (v2)** en el campo **URL de
autorización**.

Para el campo **URL información del usuario** , pegue la siguiente URL:
`https://graph.microsoft.com/oidc/userinfo`

En el campo **Enfoque** , pegue el siguiente valor:`openid profile email`.
Luego, el logo de Windows se puede usar como la clase CSS en la pantalla de
inicio de sesión ingresando el siguiente valor: `fa fa-fw fa-windows`, en el
campo **Clase CSS**.

Seleccione la casilla junto al campo **Permitido** para habilitar el proveedor
OAuth. Finalmente, agregue `Microsoft Azure` al campo **Etiqueta del botón de
inicio de sesión**. Este texto aparecerá junto al logo de Windows en la página
de inicio de sesión.

![Configuración del proveedor de Konvergo ERP en la aplicación Ajustes.
](../../../_images/odoo-provider-settings.png)

Haga clic en **Guardar** para guardar los cambios y completar la configuración
de la autenticación de OAuth en Konvergo ERP.

### Flujos de experiencia del usuario

Para que un usuario inicie sesión en Konvergo ERP usando Microsoft Azure, el usuario
debe estar en la página de restablecimiento de contraseña de Konvergo ERP. Esta es la
única manera en la que Konvergo ERP se puede vincular a la cuenta de Microsoft Azure e
iniciar sesión.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Los usuarios ya existentes deben <a href="../users#users-reset-password"><span class="std std-ref">restablecer su contraseña</span></a> para acceder a la página de restablecimiento de contraseña de Konvergo ERP. En el caso de los nuevos usuarios de Konvergo ERP, deben hacer clic en el enlace de la invitación de nuevo usuario que recibieron por correo electrónico y luego hacer clic en <b>Microsoft Azure</b>. Los usuarios no deben establecer una contraseña nueva.</p>
</div>

Para iniciar sesión en Konvergo ERP por primera vez usando el proveedor Microsoft
Azure OAuth vaya a la página de restablecimiento de contaseña de Konvergo ERP (usando
el enlace de la invitación de usuario nuevo). Debe aparecer una página para
restablecer la contraseña. Luego, haga clic en la opción llamada **Microsoft
Azure**. Esta página lo redirigirá a la página de inicio de sesión de
Microsoft.

![Página de inicio de sesión de Microsoft Outlook.](../../../_images/odoo-
login.png)

Escriba el **correo electrónico de Microsoft** y haga clic en **Siguiente**.
Siga el proceso para iniciar sesión en la cuenta. Si activa la A2F deberá
completar un paso adicional.

![Ingresar credenciales de Microsoft.](../../../_images/login-next.png)

Finalmente, después de iniciar sesión en su cuenta, la página lo
redireccionará a una página de permisos donde se le invita al usuario a
**Acceptar** las condiciones en las que se señala que la aplicación Konvergo ERP
accederá a su información de Microsoft.

![Acepte las condiciones de Microsoft para permitir el acceso a la información
de su cuenta. ](../../../_images/accept-access.png)

  *[URL]: Localizador de recursos uniforme
  *[API]: Interfaz de programación de aplicaciones
  *[A2F]: Autenticación de dos factores

