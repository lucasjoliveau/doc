# Complemento de Gmail

El _complemento de Gmail_ integra una base de datos de Konvergo ERP con una bandeja de
entrada de Gmail. De esta forma, los usuarios pueden llevar seguimiento de
todo su trabajo entre Gmail y Konvergo ERP sin perder información.

## Usuarios de Konvergo ERP en línea

Para las bases de datos alojadas en Konvergo ERP en línea (u Konvergo ERP.sh), siga estos
pasos para configurar el complemento de Gmail.

### Instalar el complemento de Gmail

Primero, inicie sesión en la cuenta de Gmail que el usuario desea conectar con
Konvergo ERP.

En la bandeja de entrada de Gmail, haga clic en el icono del signo de más en
el panel que se encuentra a la derecha para agregar complementos. Si el panel
lateral no está visible, haga clic en el icono de flecha en la esquina
inferior derecha de la bandeja de entrada para verlo.

![Icono del signo de más en el panel lateral de la bandeja de entrada de
Gmail.](../../../../_images/gmail-side-panel.png)

Después, escriba `Konvergo ERP` en la barra de búsqueda y seleccione el **complemento
de bandeja de entrada de Konvergo ERP (Konvergo ERP Inbox Addin)**.

![Konvergo ERP Inbox Addin en Google Workspace
Marketplace.](../../../../_images/google-workspace-marketplace.png)

También puede ir a la página de **Konvergo ERP Inbox Addin** en [Google Workspace
Marketplace](https://workspace.google.com/marketplace/app/odoo_inbox_addin/873497133275).

Una vez que encuentre el complemento, haga clic en **Instalar** y luego en
**Continuar** para iniciar la instalación.

Seleccione la cuenta de Gmail que conectará con Konvergo ERP. Después, haga clic en
**Permitir** para proporcionar acceso a Konvergo ERP a la cuenta de Google. Google
mostrará una ventana emergente para confirmar que la instalación se realizó
con éxito.

### Configurar la base de datos de Konvergo ERP

Debe habilitar la función de **Complemento de correo** en la base de datos de
Konvergo ERP para usar el complemento de Gmail. Para habilitar la función, vaya a
Ajustes ‣ Ajustes generales. En la sección de **Integraciones** , active la
opción de **Complemento de correo** y luego haga clic en **Guardar**.

![La función de complemento de correo en los
ajustes.](../../../../_images/mail-plugin-setting.png)

### Configurar la bandeja de entrada de Gmail

En la bandeja de entrada de Gmail ahora aparece el icono morado de Konvergo ERP en el
panel lateral derecho. Haga clic para abrir la ventana del complemento de
Konvergo ERP. Después, haga clic en cualquier correo electrónico en la bandeja de
entrada. Presione **Autorizar acceso** en la ventana del complemento para
otorgar a Konvergo ERP acceso a la bandeja de entrada de Gmail.

![El botón de Autorizar acceso en la barra lateral derecha del panel del
complemento de Konvergo ERP.](../../../../_images/authorize-access.png)

Haga clic en **Iniciar sesión**. Luego, introduzca la URL de la base de datos
de Konvergo ERP que desea conectar con la bandeja de entrada de Gmail e inicie sesión
en la base de datos.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Utilice la URL general de la base de datos, no la de una página específica en la base de datos. Por ejemplo, utilice <code>https://miempresa.odoo.com</code> y no <code>https://miempresa.odoo.com/web#cids=1&amp;action=menu</code>.</p>
</div>

Por último, haga clic en **Permitir** para que Gmail pueda ingresar a la base
de datos de Konvergo ERP. El navegador mostrará un mensaje de **¡Éxito!**. Luego,
cierre la ventana. La bandeja de entrada de Gmail y la base de datos de Konvergo ERP
ahora están conectadas.

## Usuarios de Konvergo ERP con alojamiento local

Para las bases de datos con alojamiento en servidores distintos a los de Konvergo ERP
en línea (u Konvergo ERP.sh), siga los pasos a continuación para configurar el
complemento de Gmail.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Como parte de sus guías de seguridad, Google necesita que los creadores de complementos proporcionen una lista con las URL que se pueden utilizar en las acciones y los redireccionamientos que activan el complemento. Esto protege a los usuarios al garantizar, por ejemplo, que ningún complemento redirecciona a los usuarios a un sitio web malicioso. (Consulte más información en <a href="https://developers.google.com/apps-script/manifest/allowlist-url">Google Apps Script</a>.)</p>
<p>Como Konvergo ERP solo puede colocar en la lista el dominio <code>odoo.com</code> y no los dominios de cada servidor local único por cliente, los clientes con alojamiento local no pueden instalar el complemento de Gmail desde  Google Workspace Marketplace.</p>
</div>

### Instalar el complemento de Gmail

Primero, acceda al [repositorio de GitHub](https://github.com/odoo/mail-
client-extensions) para ver los complementos de correo de Konvergo ERP. A
continuación, haga clic en el botón verde de **Código** y haga clic en
**Descargar ZIP** para descargar los archivos del complemento de correo en la
computadora del usuario.

![Descargar el archivo ZIP del repositorio de Konvergo ERP en GitHub para obtener los
complementos de correo.](../../../../_images/gh-download-zip.png)

Abra el archivo ZIP en la computadora y vaya a mail-client-extensions-master ‣
gmail ‣ src ‣ views. Abra el archivo `login.ts` con cualquier software de
edición de texto como Bloc de notas (Windows), TextEdit (Mac) o Visual Studio
Code.

Elimine las siguientes tres líneas de texto del archivo `login.ts`:

    
    
    if (!/^https:\/\/([^\/?]*\.)?odoo\.com(\/|$)/.test(validatedUrl)) {
         return notify("The URL must be a subdomain of odoo.com");
    }
    

Al hacer lo anterior, elimina las restricciones del dominio `odoo.com` del
programa del complemento de Gmail.

Luego, en el archivo ZIP, vaya a mail-client-extensions-master ‣ gmail y abra
el archivo con el nombre **appsscript.json**. En la sección
**urlFetchWhitelist** sustituya todas las referencias a `odoo.com` con el
dominio de servidor único en Konvergo ERP del cliente.

En la misma carpeta de **gmail** , abra el archivo **README.md** y siga las
instrucciones para insertar los archivos del complemento de Gmail como un
proyecto de Google.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Para seguir las instrucciones del archivo <b>README.md</b>, su computadora debe ser capaz de ejecutar comandos de Linux.</p>
</div>

Después, comparta el proyecto de Google con la cuenta de Gmail que el usuario
desea conectar con Konvergo ERP, haga clic en **Publicar** y en **Desplegar desde el
manifiesto**. Por último, haga clic en **Instalar el complemento** para
instalar el plugin de Gmail.

### Configurar la base de datos de Konvergo ERP

Debe habilitar la función de **Complemento de correo** en la base de datos de
Konvergo ERP para usar el complemento de Gmail. Para habilitar la función, vaya a
Ajustes ‣ Ajustes generales. En la sección de **Integraciones** , active la
opción de **Complemento de correo** y luego haga clic en **Guardar**.

![La función de complemento de correo en los
ajustes.](../../../../_images/mail-plugin-setting.png)

### Configurar la bandeja de entrada de Gmail

En la bandeja de entrada de Gmail ahora aparece el icono morado de Konvergo ERP en el
panel lateral derecho. Haga clic para abrir la ventana del complemento de
Konvergo ERP. Después, haga clic en cualquier correo electrónico en la bandeja de
entrada. Presione **Autorizar acceso** en la ventana del complemento para
otorgar a Konvergo ERP acceso a la bandeja de entrada de Gmail.

![El botón de Autorizar acceso en la barra lateral derecha del panel del
complemento de Konvergo ERP.](../../../../_images/authorize-access.png)

Haga clic en **Iniciar sesión**. Luego, introduzca la URL de la base de datos
de Konvergo ERP que desea conectar con la bandeja de entrada de Gmail e inicie sesión
en la base de datos.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Utilice la URL general de la base de datos, no la de una página específica en la base de datos. Por ejemplo, utilice <code>https://miempresa.odoo.com</code> y no <code>https://miempresa.odoo.com/web#cids=1&amp;action=menu</code>.</p>
</div>

Por último, haga clic en **Permitir** para que Gmail pueda ingresar a la base
de datos de Konvergo ERP. El navegador mostrará un mensaje de **¡Éxito!**. Luego,
cierre la ventana. La bandeja de entrada de Gmail y la base de datos de Konvergo ERP
ahora están conectadas.

