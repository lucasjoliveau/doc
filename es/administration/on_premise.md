# Local

## Registrar una base de datos

Para registrar su base de datos, escriba su código de suscripción en el
mensaje que aparece en el tablero de la aplicación. Si el registro es exitoso,
el mensaje cambiará a color verde y aparecerá la fecha de vencimiento de la
base de datos.

Truco

La fecha de vencimiento también aparece en la parte inferior de la página
Ajustes.

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

  * Verifique la **validez de su suscripción a la versión Enterprise de Odoo**. Compruebe si los detalles de su suscripción tienen la etiqueta En progreso en su [cuenta de Odoo](https://accounts.odoo.com/my/subscription) o comuníquese con su gerente de cuenta.

  * Asegúrese de que **ninguna otra base de datos esté vinculada** al código de suscripción, ya que solo puede haber una base de datos vinculada por suscripción.

Truco

Si necesita una base de datos de prueba o de desarrollo, puede duplicar una
base de datos.

  * Verifique que **ninguna base de datos comparta el mismo UUID** (es decir, el identificador único universal). Abra su [contrato de Odoo](https://accounts.odoo.com/my/subscription) y si dos o más bases de datos comparten el mismo UUID, entonces aparecerá su nombre.

![Mensaje de error del UUID de la base de datos](../_images/unlink-db-name-
collision.png)

Si eso es lo que ocurre, cambie de forma manual el UUID de las bases de datos
o [envíe un ticket de soporte](https://www.odoo.com/help).

  * Como la notificación de actualización debe poder conectarse a los servidores de validación de suscripción de Odoo, asegúrese de que los **ajustes de red y firewall** permitan que el servidor de Odoo abra conexiones salientes hacia:

    * `services.odoo.com` en el puerto `443` (u `80`).

    * Para despliegues anteriores, `services.openerp.com` en el puerto `443` (o `80`).

Debe mantener estos puertos abiertos incluso después de registrar una base de
datos, ya que la notificación de actualización se ejecuta una vez a la semana.

### Error por demasiados usuarios

El siguiente mensaje aparecerá si tiene más usuarios en una base de datos
local que el número asignado a su suscripción a la versión Enterprise de Odoo.

![Mensaje de error en la base de datos debido a demasiados
usuarios.](../_images/add-more-users.png)

Después de que el mensaje aparece, tiene 30 días para hacer algo antes de que
la base de datos expire. El conteo regresivo se actualiza diario.

Para solucionar este error puede:

  * **Agregar más usuarios** a su suscripción. Haga clic en el enlace Actualice su suscripción que aparece en el mensaje para validar la cotización adicional y pagar por los usuarios adicionales.

  * [Desactivar usuarios](../applications/general/users.html#users-deactivate) y **rechazar** la cotización adicional.

Importante

Si usa un plan de suscripción mensual, la base de datos se actualizará en
automático para reflejar los usuarios que agregó. Si contrató un plan anual o
multianual, aparecerá un mensaje de expiración en la base de datos. Puede
crear la cotización adicional si hace clic en ese mensaje para actualizar su
suscripción o [enviar un ticket de soporte](https://www.odoo.com/help) para
solucionar el problema.

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

  * Haga clic en el enlace Renueve su suscripción que aparece en el mensaje y complete el proceso. Si paga mediante transferencia bancaria, su suscripción se renovará cuando recibamos el pago, eso puede tardar un par de días. Los pagos con tarjeta de crédito se procesan de inmediato.

  * [Envíe un ticket de soporte](https://www.odoo.com/help).

  * Paquete de instaladores
    * Linux
      * [Preparar](on_premise/packages.html#prepare)
      * [Repositorio](on_premise/packages.html#repository)
      * [Paquete de distribución](on_premise/packages.html#distribution-package)
    * [Windows](on_premise/packages.html#windows)
  * Instalación desde la fuente
    * Extraer los recursos
      * [Archivar](on_premise/source.html#archive)
      * [Git](on_premise/source.html#git)
    * Preparar
      * [Python](on_premise/source.html#python)
      * [PostgreSQL](on_premise/source.html#postgresql)
      * [Dependencias](on_premise/source.html#dependencies)
    * [Ejecutar Odoo](on_premise/source.html#running-odoo)
  * Actualizaciones para solucionar bugs
    * [Introducción](on_premise/update.html#introduction)
    * [En resumen](on_premise/update.html#in-a-nutshell)
    * [Paso 1: descargue una versión actualizada de Odoo](on_premise/update.html#step-1-download-an-updated-odoo-version)
    * [Paso 2: haga un respaldo de su base de datos](on_premise/update.html#step-2-make-a-backup-of-your-database)
    * Paso 3: instale la versión actualizada
      * [Instaladores de paquete](on_premise/update.html#packaged-installers)
      * [Instalación desde la fuente (Tarball)](on_premise/update.html#source-install-tarball)
      * [Instalación desde la fuente (GitHub)](on_premise/update.html#source-install-github)
      * [Docker](on_premise/update.html#docker)
  * Configuración del sistema
    * dbfilter
      * [Ejemplos de configuración](on_premise/deploy.html#configuration-samples)
    * PostgreSQL
      * [Ejemplo de configuración](on_premise/deploy.html#configuration-sample)
      * Configurar Odoo
        * [Ejemplo de configuración](on_premise/deploy.html#id3)
      * [SSL entre Odoo y PostgreSQL](on_premise/deploy.html#ssl-between-odoo-and-postgresql)
    * Servidor incorporado
      * [Cálculo del número de workers](on_premise/deploy.html#worker-number-calculation)
      * [Cálculo del tamaño de la memoria](on_premise/deploy.html#memory-size-calculation)
      * [Chat en vivo](on_premise/deploy.html#livechat)
      * [Ejemplo de configuración](on_premise/deploy.html#id5)
    * HTTPS
      * [Ejemplo de configuración](on_premise/deploy.html#id7)
      * [Reforzamiento de HTTPS](on_premise/deploy.html#https-hardening)
    * Odoo como una aplicación WSGI
      * [Workers de cron](on_premise/deploy.html#cron-workers)
      * [Chat en vivo](on_premise/deploy.html#id8)
    * Gestión de archivos y archivos adjuntos estáticos
      * [Gestión de archivos estáticos](on_premise/deploy.html#serving-static-files)
      * [Alojamiento de adjuntos](on_premise/deploy.html#serving-attachments)
    * Seguridad
      * [Bloquear ataques de fuerza bruta](on_premise/deploy.html#blocking-brute-force-attacks)
      * [Seguridad del gestor de la base de datos](on_premise/deploy.html#database-manager-security)
      * Restablecer la contraseña maestra
        * [Ubicar el archivo de configuración](on_premise/deploy.html#locate-configuration-file)
        * [Cambiar la contraseña anterior](on_premise/deploy.html#change-old-password)
        * [Reiniciar el servidor de Odoo](on_premise/deploy.html#restart-odoo-server)
        * [Usar la interfaz web para volver a encriptar la contraseña](on_premise/deploy.html#use-web-interface-to-re-encrypt-password)
    * [Navegadores compatibles](on_premise/deploy.html#supported-browsers)
  * Puerta de enlace del correo electrónico
    * [Prerrequisitos](on_premise/email_gateway.html#prerequisites)
    * [Para Postfix](on_premise/email_gateway.html#for-postfix)
    * [Para Exim](on_premise/email_gateway.html#for-exim)
  * IP de localización
    * [Instalación](on_premise/geo_ip.html#installation)
    * [Cómo probar la geolocalización GeoIP en su sitio web de Odoo](on_premise/geo_ip.html#how-to-test-geoip-geolocation-in-your-odoo-website)
  * Cambiar de Community a Enterprise
    * [En Linux, mediante un instalador](on_premise/community_to_enterprise.html#on-linux-using-an-installer)
    * [En Linux, usando el código fuente](on_premise/community_to_enterprise.html#on-linux-using-the-source-code)
    * [En Windows](on_premise/community_to_enterprise.html#on-windows)

