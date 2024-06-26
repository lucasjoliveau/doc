# Autenticación de inicio de sesión de Google

La _autenticación de inicio de sesión de Konvergo ERP_ es una función útil que permite
que los usuarios de Konvergo ERP inicien sesión en su base de datos desde su cuenta de
Goole.

Esto es muy útil, en especial si la empresa usa Workspace de Google y quiere
que los empleados se conecten a Konvergo ERP con su cuenta de Google.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Las bases de datos alojadas en Konvergo ERP.com no deben usar el inicio se sesión de Oauth si es el propietario o administrador de la misma, pues podría desvincular la base de datos de su cuenta de Konvergo ERP.com. Si Oauth está establecido para ese usuario, la base de datos ya no se podrá duplicar, renombrar o administrar desde el portal de Konvergo ERP.com.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../../productivity/calendar/google">Sincronizar el calendario de Google con Konvergo ERP</a></p></li>
<li><p><a href="../email_communication/google_oauth">Conectar Gmail con Konvergo ERP mediante Google OAuth</a></p></li>
</ul>
</div>

## Configuración

Integrar el inicio de sesión de Google requiere que se configure tanto _Konvergo ERP_
como _Google_.

### Tablero de la API de Google

  1. Vaya al [tablero de la API de Google](https://console.developers.google.com/).

  2. Asegúrese de que abrió el proyecto correcto. Si todavía no hay un proyecto, haga clic en **Crear proyecto** , llene el nombre del proyecto y los otros detalles de la empresa y después haga clic en **Crear**.

![Llenar los detalles de un nuevo proyecto.](../../../_images/new-project-
details.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Elija el nombre de la empresa desde el menú desplegable.</p>
</div>

#### OAuth pantalla de consentimiento

  1. En el lado izquierdo del menú haga clic en OAuth pantalla de consentimiento.

![Selección del menú de consentimiento de Google
OAuth](../../../_images/consent-selection.png)

  2. Elija una de las opciones (**Interno** / **Externo**) y haga clic en **Crear**.

![Elegir un tipo de usuario en el consentimiento de
OAuth.](../../../_images/consent.png) <div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>A las cuentas <em>personales</em> de Gmail solo se les permite ser el tipo de usuario <b>externo</b>. Esto significa que es posible que Google requiera una aprobación o que agregue <em>alcances</em>. Sin embargo, si usa una cuenta de <em>Google WorkSpace</em> podrá usar el tipo de usuario <b>interno</b>.</p>
<p>También tome en cuenta que siempre y cuando la conexión API se encuentre en el modo de prueba <em>externo</em> no necesitará que Google aprueba nada. El límite de usuarios en modo de prueba es 100.</p>
</div>

  3. Llene los detalles requeridos y la información de dominio, después haga clic en **Guardar y crear**.

  4. En la página de **Alcance** deje todos los campos como están y después haga clic en **Guardar y continuar**.

  5. Si sigue en el modo de prueba (_Externo_), para agregar las direcciones de correo que configuró en el paso **Usuarios de prueba** haga clic en **Add Users** (agregar usuarios) y después en el botón **Save and Continue** (guardr y continuar). Aparecerá un resumen del registro de la aplicación.

  6. Finalmente, navegue al final de la página y haga clic en **Back to Dashboard** (volver al tablero).

#### Credenciales

  1. En el menú del lado izquierdo haga clic en Credenciales.

![Menú de botones de las credenciales.](../../../_images/credentials-
button.png)

  2. Haga clic en **Crear credenciales** , y seleccione **ID de cliente de OAuth**.

![Selección del ID del cliente OAuth.](../../../_images/client-id.png)

  3. Seleccione **Aplicación Web** como **Tipo de aplicación**. Ahora configure las páginas permitidas a las que se va a redirigir Konvergo ERP.

Para lograrlo, en el campo de **URL de redirección autorizadas** ingrese el
dominio de su base de datos inmediatamente seguido por `/auth_oauth/signin`.
Por ejemplo: `https://midominio.odoo.com/auth_oauth/signin` y luego haga clic
en **Crear**.

  4. Ya que se creó el _cliente OAuth_ , aparecerá una pantalla con el **ID del cliente** y el **Secreto del cliente**. Copie el **ID del cliente** para después, ya que lo necesitará para realizar la configuración en Konvergo ERP, la cual explicaremos en los siguientes pasos.

### Autenticaciión de Google en Konvergo ERP

#### Recuperar el ID del cliente

Una vez que se completen los pasos previos, se generan dos llaves en el
tablero del API de Google, **ID del cliente** y **Secreto del cliente**. Copie
el **ID del cliente**.

![ID del cliente de Google OAuth que se generó.](../../../_images/secret-
ids.png)

#### Activación de Konvergo ERP

  1. Vaya a Ajustes generales de Konvergo ERP ‣ Integraciones y active la **Autenticación OAuth**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Es posible que Konvergo ERP le pida al usuario volver a iniciar sesión después de este paso.</p>
</div>

  2. Regrese a Ajustes generales ‣ Integraciones ‣ Autenticación OAuth, active la selección y **Guarde**. Después, regrese a Ajustes generales ‣ Integraciones ‣ Autenticación de Google y active la selección. Ahora llene el **ID del cliente** con la llave que obtuvo desde el tablero API de Google. Después haga clie en **Guardar**.

![Llenar el ID del cliente en los ajustes de Konvergo ERP.](../../../_images/odoo-
client-id.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>También puede acceder a la configuración de Google OAuth desde <b>Proveedores OAuth</b> abajo del título <b>Autenticación OAuth</b>  en Integraciones.</p>
</div>

## Inicie sesión en Konvergo ERP con Google

Para vincular su cuenta de Google con el perfil de Konvergo ERP, haga clic en
**Iniciar sesión con Google** la primera vez que inicie sesión en Konvergo ERP.

> ![Pantalla para cambiar la contraseña con el botón "Iniciar sesión con
> Google".](../../../_images/first-login.png)

Los usuarios existentes deben restablecer su contraseña para ir a la página de
Restablcer contraseña. Los usuarios nuevos puede hacer clic en **Acceder con
Google** en lugar de elegir una nueva contraseña.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="https://support.google.com/cloud/answer/6158849">Ayuda de Google Cloud Platform Console - Setting up OAuth 2.0</a></p></li>
</ul>
</div>

