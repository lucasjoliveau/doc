# Local

## Registrar una base de datos

Para registrar su base de datos, escriba su código de suscripción en el
mensaje que aparece en el tablero de la aplicación. Si el registro es exitoso,
el mensaje cambiará a color verde y aparecerá la fecha de vencimiento de la
base de datos.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>La fecha de vencimiento también aparece en la parte inferior de la página Ajustes.</p>
</div>

## Duplicar una base de datos

Para duplicar una base de datos deberá acceder al gestor de bases de datos en
su servidor (`<odoo-server>/web/database/manager`). Por lo general deberá
duplicar su base de datos de producción en una base de datos de prueba
neutralizada. Puede hacerlo si marca la casilla de neutralización cuando
aparezca, esto ejecutará todos los scripts `neutralize.sql` para cada módulo
instalado.

## Mensajes de error comunes y soluciones

### Error de registro

El siguiente mensaje aparecerá en caso de que haya un error de registro.

![Mensaje de error de registro de la base de datos.](../_images/error-message-
sub-code.png)

Para solucionar este error:

  * Verifique la **validez de su suscripción a la versión Enterprise de Konvergo ERP**. Compruebe si los detalles de su suscripción tienen la etiqueta **En progreso** en su [cuenta de Konvergo ERP](https://accounts.odoo.com/my/subscription) o comuníquese con su gerente de cuenta.

  * Asegúrese de que **ninguna otra base de datos esté vinculada** al código de suscripción, ya que solo puede haber una base de datos vinculada por suscripción.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si necesita una base de datos de prueba o de desarrollo, puede <a href="#on-premise-duplicate"><span class="std std-ref">duplicar una base de datos</span></a>.</p>
</div>

  * Verifique que **ninguna base de datos comparta el mismo UUID** (es decir, el identificador único universal). Abra su [contrato de Konvergo ERP](https://accounts.odoo.com/my/subscription) y si dos o más bases de datos comparten el mismo UUID, entonces aparecerá su nombre.

![Mensaje de error del UUID de la base de datos](../_images/unlink-db-name-
collision.png)

Si eso es lo que ocurre, cambie de forma manual el UUID de las bases de datos
o [envíe un ticket de soporte](https://www.odoo.com/help).

  * Como la notificación de actualización debe poder conectarse a los servidores de validación de suscripción de Konvergo ERP, asegúrese de que los **ajustes de red y firewall** permitan que el servidor de Konvergo ERP abra conexiones salientes hacia:

    * `services.odoo.com` en el puerto `443` (u `80`).

    * Para despliegues anteriores, `services.openerp.com` en el puerto `443` (o `80`).

Debe mantener estos puertos abiertos incluso después de registrar una base de
datos, ya que la notificación de actualización se ejecuta una vez a la semana.

### Error por demasiados usuarios

El siguiente mensaje aparecerá si tiene más usuarios en una base de datos
local que el número asignado a su suscripción a la versión Enterprise de Konvergo ERP.

![Mensaje de error en la base de datos debido a demasiados
usuarios.](../_images/add-more-users.png)

Después de que el mensaje aparece, tiene 30 días para hacer algo antes de que
la base de datos expire. El conteo regresivo se actualiza diario.

Para solucionar este error puede:

  * **Agregar más usuarios** a su suscripción. Haga clic en el enlace **Actualice su suscripción** que aparece en el mensaje para validar la cotización adicional y pagar por los usuarios adicionales.

  * [Desactivar usuarios](../applications/general/users#users-deactivate) y **rechazar** la cotización adicional.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Si usa un plan de suscripción mensual, la base de datos se actualizará en automático para reflejar los usuarios que agregó. Si contrató un plan anual o multianual, aparecerá un mensaje de expiración en la base de datos. Puede crear la cotización adicional si hace clic en ese mensaje para actualizar su suscripción o <a href="https://www.odoo.com/help">enviar un ticket de soporte</a> para solucionar el problema.</p>
</div>

El mensaje de expiración desaparecerá de forma automática luego de unos días
después de que su base de datos tenga el número correcto de usuarios, cuando
ocurra la próxima verificación.

### Error por base de datos expirada

El siguiente mensaje aparecerá si su base de datos expira antes de renovar su
suscripción.

![Mensaje de error por base de datos expirada](../_images/database-
expired.png)

Este mensaje aparece si no hace algo antes de que termine la cuenta regresiva
de 30 días.

Para solucionar este error puede:

  * Haga clic en el enlace **Renueve su suscripción** que aparece en el mensaje y complete el proceso. Si paga mediante transferencia bancaria, su suscripción se renovará cuando recibamos el pago, eso puede tardar un par de días. Los pagos con tarjeta de crédito se procesan de inmediato.

  * [Envíe un ticket de soporte](https://www.odoo.com/help).

  * Paquete de instaladores
    * Linux
      * [Preparar](on_premise/packages#prepare)
      * [Repositorio](on_premise/packages#repository)
      * [Paquete de distribución](on_premise/packages#distribution-package)
    * [Windows](on_premise/packages#windows)
  * Instalación desde la fuente
    * Extraer los recursos
      * [Archivar](on_premise/source#archive)
      * [Git](on_premise/source#git)
    * Preparar
      * [Python](on_premise/source#python)
      * [PostgreSQL](on_premise/source#postgresql)
      * [Dependencias](on_premise/source#dependencies)
    * [Ejecutar Konvergo ERP](on_premise/source#running-odoo)
  * Actualizaciones para solucionar bugs
    * [Introducción](on_premise/update#introduction)
    * [En resumen](on_premise/update#in-a-nutshell)
    * [Paso 1: descargue una versión actualizada de Konvergo ERP](on_premise/update#step-1-download-an-updated-odoo-version)
    * [Paso 2: haga un respaldo de su base de datos](on_premise/update#step-2-make-a-backup-of-your-database)
    * Paso 3: instale la versión actualizada
      * [Instaladores de paquete](on_premise/update#packaged-installers)
      * [Instalación desde la fuente (Tarball)](on_premise/update#source-install-tarball)
      * [Instalación desde la fuente (GitHub)](on_premise/update#source-install-github)
      * [Docker](on_premise/update#docker)
  * Configuración del sistema
    * dbfilter
      * [Ejemplos de configuración](on_premise/deploy#configuration-samples)
    * PostgreSQL
      * [Ejemplo de configuración](on_premise/deploy#configuration-sample)
      * Configurar Konvergo ERP
        * [Ejemplo de configuración](on_premise/deploy#id3)
      * [SSL entre Konvergo ERP y PostgreSQL](on_premise/deploy#ssl-between-odoo-and-postgresql)
    * Servidor incorporado
      * [Cálculo del número de workers](on_premise/deploy#worker-number-calculation)
      * [Cálculo del tamaño de la memoria](on_premise/deploy#memory-size-calculation)
      * [Chat en vivo](on_premise/deploy#livechat)
      * [Ejemplo de configuración](on_premise/deploy#id5)
    * HTTPS
      * [Ejemplo de configuración](on_premise/deploy#id7)
      * [Reforzamiento de HTTPS](on_premise/deploy#https-hardening)
    * Konvergo ERP como una aplicación WSGI
      * [Workers de cron](on_premise/deploy#cron-workers)
      * [Chat en vivo](on_premise/deploy#id8)
    * Gestión de archivos y archivos adjuntos estáticos
      * [Gestión de archivos estáticos](on_premise/deploy#serving-static-files)
      * [Alojamiento de adjuntos](on_premise/deploy#serving-attachments)
    * Seguridad
      * [Bloquear ataques de fuerza bruta](on_premise/deploy#blocking-brute-force-attacks)
      * [Seguridad del gestor de la base de datos](on_premise/deploy#database-manager-security)
      * Restablecer la contraseña maestra
        * [Ubicar el archivo de configuración](on_premise/deploy#locate-configuration-file)
        * [Cambiar la contraseña anterior](on_premise/deploy#change-old-password)
        * [Reiniciar el servidor de Konvergo ERP](on_premise/deploy#restart-odoo-server)
        * [Usar la interfaz web para volver a encriptar la contraseña](on_premise/deploy#use-web-interface-to-re-encrypt-password)
    * [Navegadores compatibles](on_premise/deploy#supported-browsers)
  * Puerta de enlace del correo electrónico
    * [Prerrequisitos](on_premise/email_gateway#prerequisites)
    * [Para Postfix](on_premise/email_gateway#for-postfix)
    * [Para Exim](on_premise/email_gateway#for-exim)
  * IP de localización
    * [Instalación](on_premise/geo_ip#installation)
    * [Cómo probar la geolocalización GeoIP en su sitio web de Konvergo ERP](on_premise/geo_ip#how-to-test-geoip-geolocation-in-your-odoo-website)
  * Cambiar de Community a Enterprise
    * [En Linux, mediante un instalador](on_premise/community_to_enterprise#on-linux-using-an-installer)
    * [En Linux, usando el código fuente](on_premise/community_to_enterprise#on-linux-using-the-source-code)
    * [En Windows](on_premise/community_to_enterprise#on-windows)

