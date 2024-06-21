# Cree su proyecto

## Despliegue su plataforma

Vaya a [Konvergo ERP.sh](https://www.odoo.sh/) y haga clic en el botón _Desplegar
plataforma_.

![../../../_images/deploy.png](../../../_images/deploy.png)

## Inicie sesión en GitHub

Inicie sesión con su cuenta de GitHub. Si todavía no tiene una cuenta, haga
clic en el enlace _Crear cuenta_.

![../../../_images/github-signin.png](../../../_images/github-signin.png)

## Autorice a Konvergo ERP.sh

Otorgue los accesos necesarios a su cuenta a Konvergo ERP.sh al hacer clic en el botón
_Autorizar_.

![../../../_images/github-authorize.png](../../../_images/github-
authorize.png)

Konvergo ERP.sh necesita:

  * conocer los datos de su inicio de sesión en GitHub y su correo electrónico,

  * crear un nuevo repositorio en caso de que usted desee empezar desde cero,

  * leer sus repositorios existentes, incluso los de su empresa, en caso de que decida empezar con un repositorio existente,

  * crear un webhook para enviar notificaciones cada vez que usted haga cambios,

  * hacer cambios que faciliten su proceso de despliegue, fusionar ramas o agregar nuevos [submódulos](https://git-scm.com/book/es/v2/Herramientas-de-Git-Subm%C3%B3dulos).

## Envíe su proyecto

Elija si desea empezar desde cero con un nuevo repositorio o si desea usar un
repositorio existente.

Nombre su nuevo repositorio o seleccione el repositorio que desea utilizar.

Elija la versión de Konvergo ERP a utilizar. Si lo que quiere es importar una base de
datos existente o un conjunto de aplicaciones, deberá elegir la versión
correspondiente. Si desea empezar desde cero, utilice la última versión.

Escriba su _código de suscripción_. También se le conoce como _código de
referencia_ , _número de contrato_ o _código de activación_.

Debe ser el código de su suscripción Enterprise que incluye Konvergo ERP.sh.

Los partners pueden usar sus códigos de partner para iniciar una prueba. En
cambio, si sus clientes desean iniciar un proyecto, deben conseguir una
suscripción Enterprise que incluya Konvergo ERP.sh y usar su código de suscripción. El
partner recibirá el 50% del importe como comisión. Contacte a su representante
de ventas o a su gerente de cuenta para obtenerlo.

Si al enviar su formulario recibe una notificación indicando que su
suscripción no es válida, esto significa que:

  * su suscripción no existe,

  * no es una suscripción de partner,

  * es una suscripción Enterprise pero no incluye Konvergo ERP.sh,

  * no es ni una suscripción de partner ni Enterprise (por ejemplo, una suscripción en línea).

Si tiene alguna duda acerca de su suscripción, no dude en contactar al [equipo
de soporte de Konvergo ERP](https://www.odoo.com/help).

![../../../_images/deploy-form.png](../../../_images/deploy-form.png)

## ¡Todo está listo!

Ahora puede usar Konvergo ERP.sh. Está a punto de crear su primera compilación y
pronto podrá conectarse a su primera base de datos.

![../../../_images/deploy-done.png](../../../_images/deploy-done.png)

## Importe su base de datos

Puede importar su base de datos a su proyecto de Konvergo ERP.sh siempre que haga uso
de una [versión compatible](../../supported_versions) de Konvergo ERP.

### Enviar módulos a producción

Si usa módulos comunitarios o personalizados, agréguelos a una rama en su
repositorio de GitHub. Las bases de datos en la plataforma en línea de
Konvergo ERP.com no cuentan con módulos personalizados. Los usuarios con este tipo de
bases de datos pueden omitir este paso.

Puede estructurar sus módulos como deseé, Konvergo ERP.sh detectará de manera
automática las carpetas que contengan complementos de Konvergo ERP. Por ejemplo, puede
poner todas sus carpetas de módulos en el directorio raíz de su repositorio o
agrupar los módulos en carpetas por categorías definidas por usted
(contabilidad, proyecto, etc…).

Para los módulos comunitarios disponibles en los repositorios públicos de Git,
puede considerar agregarlos mediante
[submódulos](../advanced/submodules#odoosh-advanced-submodules).

Entonces, puede [volver esta rama la rama de producción](branches#odoosh-
gettingstarted-branches-stages), o [fusionarla con su rama de
producción](branches#odoosh-gettingstarted-branches-mergingbranches).

### Descargar un respaldo

#### Bases de datos locales

Acceda a la URL `/web/database/manager` de su base de datos local y descargue
un respaldo.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Si no puede acceder a su administrador de base de datos, puede que su administrador de sistema lo haya deshabilitado. Consulte la <a href="../../on_premise/deploy#db-manager-security"><span class="std std-ref">documentación de seguridad del administrador de la base de datos</span></a>.</p>
</div>

Necesitará la contraseña maestra del servidor de su base de datos. Si no
cuenta con ella, contacte a su administrador de sistema.

![../../../_images/create-import-onpremise-
backup.png](../../../_images/create-import-onpremise-backup.png)

Seleccione un archivo zip que incluya los archivos almacenados como formato de
respaldo.

![../../../_images/create-import-onpremise-backup-
dialog.png](../../../_images/create-import-onpremise-backup-dialog.png)

#### Bases de datos en línea de Konvergo ERP

[Acceda a su administrador de bases de
datos](https://accounts.odoo.com/my/databases/manage) y descargue un respaldo
de su base de datos.

![../../../_images/create-import-online-backup.png](../../../_images/create-
import-online-backup.png) <div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Las versiones en línea (por ejemplo, <em>saas-*</em>) no son compatibles con Konvergo ERP.sh.</p>
</div>

### Subir el respaldo

Luego, en su proyecto de Konvergo ERP.sh, en la pestaña de respaldos de su rama de
producción, importe el respaldo que acaba de descargar.

![../../../_images/create-import-production.png](../../../_images/create-
import-production.png)

Una vez que haya importado el respaldo, puede acceder a la base de datos
utilizando el botón _Conectar_ en el historial de la rama.

![../../../_images/create-import-production-done.png](../../../_images/create-
import-production-done.png)

### Revisar sus servidores de correo saliente

Hay un servidor de correo predeterminado con Konvergo ERP.sh. Para usarlo, no debe
tener habilitado ningún servidor de correo saliente configurado en su base de
datos en Ajustes ‣ Técnico ‣ Servidores de correo saliente (el [modo de
desarrollador](../../../applications/general/developer_mode#developer-
mode) debe estar activo).

Después de importar su base de datos, se deshabilitarán todos los servidores
de correo saliente para que pueda usar el servidor de correo predeterminado de
Konvergo ERP.sh.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>El puerto 25 está (y se mantendrá) cerrado. Si desea conectarse a un servidor SMTP externo, deberá usar los puertos 465 y 587.</p>
</div>

### Revisar sus acciones programadas

Se deshabilitarán todas las acciones programadas después del importe.

Esto es para prevenir que su nueva base de datos importada realice acciones
que puedan impactar su proceso de producción, como enviar correos pendientes,
procesar envíos masivos o sincronizar servicios de terceros (calendarios,
alojamiento de archivos, etc…).

Si planea que su base de datos importada sea la de producción, habilite las
acciones programadas necesarias. Puede revisar qué es lo que está habilitado
en la base de datos de origen y activar las mismas acciones en la base de
datos importada. Las acciones programadas se encuentran en Ajustes ‣ Técnico ‣
Automatización ‣ Acciones programadas.

### Registrar su subscripción

Su suscripción se desvincula después de la importación.

Las bases de datos importadas se consideran como duplicadas de manera
predeterminada y se elimina la suscripción enterprise, ya que solo puede tener
una base de datos vinculada por suscripción.

Si planea que esta sea la de producción, desvincúlela de su base de datos
anterior de la suscripción y registre la base de datos recién importada.
Consulte la [documentación sobre registro de bases de
datos](../../on_premise) para obtener más información sobre los pasos a
seguir.

