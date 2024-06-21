# Ajustes

## Información general

Los ajustes le permiten gestionar la configuración de su proyecto.

![../../../_images/interface-settings.png](../../../_images/interface-
settings.png)

## Nombre del proyecto

El nombre de su proyecto

![../../../_images/interface-settings-
projectname.png](../../../_images/interface-settings-projectname.png)

Esto define la dirección que se usará para acceder a la base de datos de
producción.

Las direcciones de sus compilaciones de prueba y de desarrollo derivan de este
nombre y se asignan automáticamente. Sin embargo, cuando cambia el nombre del
proyecto, solo las compilaciones futuras usarán el nuevo nombre.

## Colaboradores

Gestione los usuarios de Github que puedan acceder a su proyecto.

![../../../_images/interface-settings-
collaborators.png](../../../_images/interface-settings-collaborators.png)

Hay dos niveles de usuarios:

  * Admin: tiene acceso a todas las características de Konvergo ERP.sh.

  * Usuario: no tiene acceso a las configuraciones del proyecto ni a las bases de datos de producción o de prueba.

El grupo de usuarios está hecho para desarrolladores que puedan hacer
modificaciones en su código pero no tienen acceso a los datos de producción.
Los usuarios de este grupo no se pueden conectar a las bases de datos de
prueba ni de producción usando la función _1-click connect_ , pero por
supuesto, pueden usar su cuenta habitual, si tienen una, en estas bases de
datos usando sus credenciales de siempre.

Además, no pueden usar el webshell ni tienen acceso a los registros del
servidor.

|  | Usuario | Admin  
---|---|---|---  
Etapa de desarrollo | Historial | ● | ●  
| conectarse en 1-clic | ● | ●  
| Registros | ● | ●  
| Shell/SSH | ● | ●  
| Correos electrónicos | ● | ●  
| Actualizar | ● | ●  
| Ajustes | ● | ●  
Producción y Prueba | Historial | ● | ●  
| conectarse en 1-clic |  | ●  
| Registros |  | ●  
| Shell/SSH |  | ●  
| Correos electrónicos |  | ●  
| Monitoreo |  | ●  
| Respaldos |  | ●  
| Actualizar |  | ●  
| Ajustes | ●* | ●  
Estado |  | ● | ●  
Ajustes |  |  | ●  
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>* Solo en ramas en estado de prueba</p>
</div>

## Acceso público

Permita que el público acceda a sus compilaciones de desarrollo.

![../../../_images/interface-settings-public.png](../../../_images/interface-
settings-public.png)

Si está activado, esta opción expone las páginas de compilación de manera
pública, permitiéndole a los visitantes conectarse a sus compilaciones de
desarrollo.

Además, los visitantes tienen acceso a los registros, shell y correos
electrónicos en sus compilaciones de desarrollo.

Las compilaciones de producción y de prueba se excluyen, los visitantes solo
pueden ver sus estados.

## Dominios personalizados

Para configurar dominios adicionales, vaya a la [pestaña de
configuraciones](branches#odoosh-gettingstarted-branches-tabs-settings)
de las ramas correspondientes.

## Submódulos

Configure el despliegue de claves para los repositorios privados que usa como
submódulos en sus ramas para permitirle a Konvergo ERP.sh descargarlos.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Estos ajustes se requieren solo para <b>repositorios privados</b>. Si quiere saber como configurar sus submódulos, las instrucciones están disponibles en el capítulo <a href="../advanced/submodules#odoosh-advanced-submodules"><span class="std std-ref">Submódulos</span></a> de esta documentación.</p>
</div> ![../../../_images/interface-settings-
submodules.png](../../../_images/interface-settings-submodules.png)

Cuando un repositorio es privado, no es posible descargar públicamente sus
ramas y revisiones. Por esa razón, necesita configurar una clave de
implementación para Konvergo ERP.sh, y así el servidor Git le permita a nuestra
platafroma descargar las revisiones de este repositorio privado.

Para configurar la clave de implementación para el repositorio privado, siga
las siguientes instrucciones:

  * en el campo de entrada, pegue la URL SSH de su sub-repositorio privado y haga clic en _Agregar_ ,

    * Por ejemplo, _git@github.com:USERNAME/REPOSITORY.git_

    * puede ser otro servidor Git que no sea Github, como Bitbucket, Gitlab o inlcuso un servidor que usted mismo aloje

  * copie la clave pública,

    * debe verse como _ssh-rsa caracteres…más…caracteres…aquí…==_

  * en los ajustes del sub-repositorio privado, agregue la clave pública entre las claves de implementación

    * Github.com: Ajustes ‣ Claves de implementación ‣ Agrergar clave de implementación

    * Bitbucket.com: Ajustes ‣ Claves de acceso ‣ Agregar clave

    * Gitlab.com: Ajustes ‣ Repositorio‣ Claves de implementación

    * Alojamiento propio: adjunte la clave al archivo del usuario git authorized_keys file en su directorio .ssh

## Tamaño de almacenaje

Esta sección muestra el tamaño de almacenaje que utiliza su proyecto.

![../../../_images/interface-settings-storage.png](../../../_images/interface-
settings-storage.png)

El tamaño de almacenaje se calcula de la siguiente manera:

  * el tamaño de la base de datos de PostgreSQL

  * el tamaño de los archivos del disco disponibles en su contenedor: base de datos del repositorio de archivos, directorio del almacenaje de las sesiones…

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>En caso de que quiera analizar el uso del disco, puede activar la herramienta <a href="https://dev.yorhel.nl/ncdu/man">ncdu</a> en su Web Shell.</p>
</div>

Si el tamaño de su base de datos de producción excede lo que cubre su
suscripción, esta se sincronizará automáticamente con el nuevo tamaño.

## Workers de la base de datos

Aquí se pueden configurar trabajadores adicionales a la base de datos. Más
trabajadores ayudan a incrementar la carga de producción de lo que su base de
datos es capaz de manejar. Si quiere agregar más, automáticmanete se
sincronizará con su suscripción.

![../../../_images/interface-settings-workers.png](../../../_images/interface-
settings-workers.png) <div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Agregar más trabajadores no resolverá mágicamente todos los problemas de rendimiento. Solo permite que el servidor pueda manejar más conexiones al mismo tiempo. Si algunas operaciones son inusualmente lentas, es muy probable que exista un problema en el código, si no es a causa de la personalización de este, puede abrir un ticket <a href="https://www.odoo.com/help">aquí</a>.</p>
</div>

## Ramas de prueba

Las ramas adicionales de prueba le permiten desarrollar y probar mas
características al mismo tiempo. Si agrega más, se sincronizará
automáticamente con su suscripción.

![../../../_images/interface-settings-staging-
branches.png](../../../_images/interface-settings-staging-branches.png)

## Activación

Muestra el estado de la activación del proyecto. Puede cambiar el código de
activación del proyecto si lo necesita.

![../../../_images/interface-settings-
activation.png](../../../_images/interface-settings-activation.png)

