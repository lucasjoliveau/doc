# Sincronizar el calendario de Outlook con Konvergo ERP

Sincronizar el _calendario de Outlook_ de un usuario con Konvergo ERP es útil para
llevar registro de sus tareas y citas en todas las aplicaciones relacionadas.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../../general/users/azure">Autenticación de inicio de sesión de Microsoft Azure</a></p></li>
<li><p><a href="../../general/email_communication/azure_oauth">Conecte Microsoft Outlook 365 a Konvergo ERP con Azure OAuth</a></p></li>
</ul>
</div>

## Configuración de Microsoft Azure

Para sincronizar el _calendario de Outlook_ con el _calendario_ de Konvergo ERP
necesitará una cuenta de Microsoft _Azure_. Crear una cuenta no tiene costo
para los usuarios que nunca han probado o pagado por _Azure_. Consulte las
opciones relacionadas con las cuentas en el [sitio web de
Azure](https://azure.microsoft.com/es-mx/free/?WT.mc_id=A261C142F) para
obtener más información.

Consulte la [documentación de Microsoft](https://learn.microsoft.com/es-
mx/entra/identity-platform/quickstart-create-new-tenant) sobre la
configuración de un _ID de Microsoft Entra_ (antes conocido como Microsoft
_Azure Active Directory (Azure AD)_). Esta es una consola de API para
gestionar y registrar aplicaciones de Microsoft.

Los usuarios existentes de Microsoft _Entra ID_ deben iniciar sesión en el
[portal para desarrolladores de Microsoft
Azure](https://portal.azure.com/#home). Seleccione **Ver** en la sección
etiquetada como **Gestionar Microsoft Entra ID**.

### Registrar una aplicación

Después de iniciar sesión con su Microsoft _Entra ID_ , [registre una
aplicación](https://docs.microsoft.com/es-mx/azure/active-
directory/develop/quickstart-register-app).

Haga clic en el botón **\+ Agregar** del menú superior para crear una
aplicación y en el menú desplegable seleccione **Registro de aplicación**.

![Página de administración de Microsoft Azure con el menú + Agregar y Registro
de aplicaciones dentro de recuadros rojos.](../../../_images/app-register.png)

Proporcione un **nombre** único para la aplicación a conectar.

Elegir el **tipo de cuenta admitido** es muy importante, de lo contrario la
aplicación conectada no funcionará. Los usuarios que deseen conectar su
_calendario de Outlook_ con Konvergo ERP deben elegir la opción **Cuentas en cualquier
directorio organizativo y cuentas Microsoft personales (como Skype y Xbox)**
como **tipo de cuenta admitido**.

Al configurar el **identificador URI de redirección** , seleccione la opción
**Web** en el primer menú desplegable. Después, escriba el URI de la base de
datos de Konvergo ERP (URL) y agregue `/microsoft_account/authentication`.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Escriba <code>https://subasededatos.odoo.com/microsoft_account/authentication</code> en el <b>identificador URI de redirección</b>. Reemplace <code>subasededatos.odoo.com</code> con la <abbr title="Localizador de recursos uniforme">URL</abbr>.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Asegúrese de que la <abbr title="Localizador de recursos uniforme">URL</abbr> de la base de datos (dominio) que se usa en la URI sea idéntica al dominio configurado en el parámetro del sistema <code>web.base.url</code>.</p>
<p>Active el <a href="../../general/developer_mode#developer-mode"><span class="std std-ref">modo de desarrollador</span></a> para acceder a <code>web.base.url</code> y vaya a Ajustes ‣ menú de encabezado Técnico ‣ sección Parámetros ‣ Parámetros del sistema. Después, selecciónelo en la lista <b>Clave</b>  de la página de <b>parámetros del sistema</b>.</p>
</div> ![Los ajustes de "tipo de cuenta
admitido" e "identificador URI de redirección" en el portal de Microsoft Entra
ID.](../../../_images/azure-register-application.png)

Consulte la página [Restricciones y limitaciones del identificador URI de
redirección (dirección URL de respuesta)](https://docs.microsoft.com/es-
mx/azure/active-directory/develop/reply-url) de Microsoft para obtener más
información sobre las restricciones y limitaciones de los identificadores URI.

Por último, en la página de registro de la aplicación, haga clic en el botón
**Registrar** para completar el registro correspondiente. Se generará el **ID
de la Aplicación (cliente)**. Copie este valor, ya que lo necesitará más
adelante para la sección Configuración en Konvergo ERP.

![El ID de cliente de la aplicación aparece destacado en la sección esencial
de la aplicación recién creada.](../../../_images/app-client-id.png)

### Crear el secreto de cliente

La segunda credencial necesaria para completar la sincronización del
_calendario de Outlook_ de Microsoft es el _secreto del cliente_. El usuario
**debe** agregar un secreto del cliente, pues este permite que Konvergo ERP se
autentique a sí mismo sin necesidad de que el usuario haga algo más. Los
_certificados_ son opcionales.

Haga clic en Certificados y secretos en el menú izquierdo para agregar un
secreto del cliente y después haga clic en **\+ Nuevo secreto del cliente**
para crearlo.

![Página del nuevo secreto de cliente. El menú de certificados y secretos y la
nueva opción de secreto de cliente aparecen
destacadas.](../../../_images/client-secret.png)

Después escriba una **descripción** y seleccione cuándo **expira** el secreto
del cliente. Las opciones disponibles son: **90 días (3 meses)** , **365 días
(12 meses)** , **545 días (18 meses)** , **730 días (24 meses)** o
**Personalizado**. La opción **Personalizado** permite que el administrador
establezca una **fecha de inicio** y una **fecha de finalización**.

Para finalizar, haga clic en **Agregar** para **agregar un secreto del
cliente**.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Restablecer la sincronización puede ser complicado, así que le recomendamos que la fecha de vencimiento que configure el plazo máximo permitido en el secreto del cliente (24 meses o personalizado) para que no tenga que volver a realizar la sincronización pronto.</p>
</div>

Copie el **valor** , deberá usarlo en la siguiente sección.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Los valores del secreto del cliente solo son visibles después de crearlos, asegúrese de guardarlo <em>antes</em> de salir de la página.</p>
</div>

## Configuración en Konvergo ERP

En la base de datos de Konvergo ERP, vaya a Ajustes ‣ sección Integraciones y
seleccione la casilla ubicada junto a **Calendario de Outlook**. Recuerde
hacer clic en **Guardar** para implementar los cambios.

![La opción "Calendario de Outlook" activada.](../../../_images/outlook-
calendar-setting.png)

Desde el portal de Microsoft _Azure_ , en la sección **Resumen** de la
aplicación, copie el **ID de la aplicación (cliente)** en caso de que no lo
haya hecho y péguelo en el campo **ID del cliente** en Konvergo ERP.

![El "Client ID" en el portal de Microsoft Azure.](../../../_images/client-
id1.png)

Copie el **valor** anterior (el valor del secreto de cliente) y péguelo en el
campo **Secreto del cliente** en Konvergo ERP.

![El "secreto de cliente" que debe copiar de Microsoft a
Konvergo ERP.](../../../_images/client-secret-value.png)

En Konvergo ERP vaya a Ajustes ‣ Ajustes generales y haga clic en **Guardar**.

## Sincronizar con Outlook

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Konvergo ERP le recomendamos que primero haga una prueba de la sincronización del calendario de Outlook en una base de datos de prueba con un correo electrónico de prueba (es decir, uno que solo use para esto) antes de hacer la sincronización en una base de datos en producción.</p>
<p>Si el usuario tiene eventos pasados, presentes o futuros agendados en su calendario de Konvergo ERP antes de sincronizarlo con su calendario de Outlook, Outlook considerará estos eventos como eventos nuevos. Esto causará que se envíe una notificación de correo electrónico desde Outlook a todos los asistentes al evento.</p>
<p>Para evitar que se manden correos no deseados a asistentes pasados, presentes y futuros, el usuario debe agregar los eventos que tenga en el calendario de Konvergo ERP al calendario de Outlook antes de hacer la primera sincronización. Luego, borre todos los eventos del calendario de Konvergo ERP e inicie la sincronización.</p>
<p>Incluso después de sincronizar el calendario de Konvergo ERP con el de Outlook, este último le enviará una notificación a todos los participantes de los eventos siempre que se editen, (ya sea que se cree, borre, desarchive, o se cambie la fecha y hora del evento) sin excepciones. Esta es una limitación que no se puede solucionar desde Konvergo ERP.</p>
<p>Para resumir, una vez que un usuario sincroniza el calendario de Outlook con Konvergo ERP:</p>
<ul>
<li><p>Si crea un evento en Konvergo ERP, se enviará una invitación de Outlook a todos los asistentes al evento.</p></li>
<li><p>Si elimina un evento en Konvergo ERP, se enviará un correo de cancelación a todos los asistentes.</p></li>
<li><p>Si desarchiva un evento en Konvergo ERP, se enviará una invitación de Outlook a todos los asistentes al evento.</p></li>
<li><p>Si archiva un evento en Konvergo ERP, se enviará un correo de cancelación de Outlook a todos los asistentes al evento.</p></li>
<li><p>Si agrega un contacto el evento, se enviará un correo de invitación a todos los asistentes.</p></li>
<li><p>Si quita un contanto del evento, se enviará un correo de cancelación a todos los asistentes al evento.</p></li>
</ul>
</div>

### Sincronización del calendario de Konvergo ERP y Outlook

En la base de datos de Konvergo ERP, abra el módulo _Calendario_ y haga clic en el
botón de sincronización de **Outlook** ubicado en el lado derecho de la
página, abajo del calendario mensual.

![El botón para sincronizar "Outlook" en la aplicación Calendario de
Konvergo ERP.](../../../_images/outlook-sync-button.png)

La sincronización es un proceso bidireccional, lo que significa que los
eventos se concilian en ambas cuentas (en _Outlook_ y en Konvergo ERP). La página
redirige a una página de inicio de sesión de Microsoft que le pide al usuario
que inicie sesión en su cuenta, si aún no lo ha hecho. Por último, haga clic
en **Aceptar** para proporcionar los permisos necesarios.

![Proceso de autenticación en la página de OAuth de Microsoft
Outlook.](../../../_images/accept-terms.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Todos los usuarios que deseen usar la sincronización solo necesitan <a href="#outlook-sync"><span class="std std-ref">sincronizar su calendario con Outlook</span></a>. La configuración de la cuenta de Microsoft <em>Azure</em> solo se realiza una vez, ya que el ID de cliente y el secreto de cliente de los inquilinos de Microsoft <em>Entra ID</em> son únicos y ayudan al usuario a gestionar instancias específicas de los servicios en la nube de Microsoft para sus usuarios internos y externos.</p>
</div>
<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../../general/integrations/mail_plugins/outlook">Complemento de Outlook</a></p></li>
<li><p><a href="google">Sincronizar el calendario de Google con Konvergo ERP</a></p></li>
</ul>
</div>

## Solución de problemas relacionados a la sincronización

Es posible que en algunas ocasiones la cuenta del _calendario de Microsoft
Outlook_ no se sincronice de forma correcta con Konvergo ERP. Es posible consultar los
problemas de sincronización en los registros de la base de datos.

En estos casos es necesario solucionar los problemas de la cuenta y es posible
restablecerla con el botón **Restablecer cuenta**. Vaya a Ajustes ‣
Administrar usuarios, seleccione el usuario del que se debe modificar el
calendario y haga clic en la pestaña **Calendario**.

![Los botones para restablecer aparecen resaltados en la pestaña Calendario
del usuario.](../../../_images/outlook-reset.png)

Después, haga clic en el botón **Restablecer cuenta** del calendario correcto.

### Opciones de restablecimiento

Las siguientes opciones de restablecimiento están disponibles para solucionar
problemas de sincronización del _calendario de Microsoft Outlook_ con Konvergo ERP:

![Opciones de restablecimiento para el calendario de Outlook en
Konvergo ERP.](../../../_images/reset-calendar1.png)

**Eventos existentes del usuario** :

>   * **Dejarlos intactos** : no ocurren cambios en los eventos.
>
>   * **Eliminar de la cuenta actual del calendario de Microsoft** : elimina
> los eventos del _calendario de Microsoft Outlook_.
>
>   * **Eliminar de Konvergo ERP** : elimina los eventos del calendario de Konvergo ERP.
>
>   * **Eliminar de ambos** : elimina los eventos del _calendario de Microsoft
> Outlook_ y del calendario de Konvergo ERP.
>
>

**Siguiente sincronización** :

>   * **Sincronizar solo los eventos nuevos** : sincroniza los nuevos eventos
> en el _calendario de Microsoft Outlook_ y el calendario de Konvergo ERP.
>
>   * **Sincronizar todos los eventos existentes** : sincroniza todos los
> eventos en el _calendario de Microsoft Outlook_ y el calendario de Konvergo ERP.
>
>

Haga clic en **Confirmar** después de hacer la selección para modificar los
eventos del usuario y la sincronización del calendario.

