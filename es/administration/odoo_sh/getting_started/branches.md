# Ramas

## Información general

La vista de ramas le proporciona información general de las distintas ramas de
su repositorio.

![../../../_images/interface-branches.png](../../../_images/interface-
branches.png)

## Etapas

Odoo.sh le ofrece tres diferentes etapas para sus ramas: producción, prueba y
desarrollo.

Puede cambiar la etapa de una rama al arrastrarla y soltarla en el título de
la sección de etapa.

![../../../_images/interface-branches-
stagechange.png](../../../_images/interface-branches-stagechange.png)

### Etapa de producción

Esta es la rama que contiene el código en el que se ejecuta su base de datos
de producción. Solo puede existir una rama de producción.

Cuando confirma sus cambios en esta rama, su servidor de producción se
actualiza con el código de la nueva revisión y luego se reinicia.

Si sus cambios requieren la actualización de un módulo, como un cambio en una
vista de formulario, y desea que se realice de forma automática, incremente el
número de versión del módulo en su archivo manifest (___manifest__.py_). La
plataforma se encargará de llevar a cabo la actualización durante la cual la
instancia no estará disponible de forma temporal por motivos de mantenimiento.

Este método es equivalente a realizar una actualización del módulo mediante el
menú «aplicaciones» o con `-u` en la [línea de
comandos](../../../developer/reference/cli.html).

En caso de que los cambios en la confirmación prevengan que el servidor se
reinicie, o si la actualización de los módulos falla, el servidor se restaura
automáticamente a la última revisión de código exitosa y la base de datos se
revierte a su estado previo a la actualización. Aún tiene acceso al registro
de la actualización fallida para que pueda solucionar los errores.

Los datos de demostración no se cargan, pues no se deben usar en una base de
datos de producción. No se realizan pruebas unitarias debido a que
incrementarían el tiempo en el que la base de datos de producción no está
disponible durante las actualizaciones.

Los usuarios que utilizan proyectos de prueba deben tomar en cuenta que su
rama de producción, junto con todas las ramas de prueba, volverán de forma
automática a la etapa de desarrollo después de 30 días.

### Etapa de prueba

Las ramas de prueba son para probar sus nuevas funciones con los datos de
producción, sin comprometer la base de datos de producción real con registros
de prueba. Crearán bases de datos que son duplicados neutralizados de la base
de datos de producción.

La neutralización incluye:

  * Deshabilitar acciones planificadas. Si desea probarlas, puede activar sus acciones de forma manual o volver a habilitarlas. Tome en cuenta que, con el fin de ahorrar recursos, la plataforma las activará con menor frecuencia si nadie usa la base de datos.

  * Deshabilitar correos electrónicos salientes al interceptarlos con mailcatcher. Se le proporciona una interfaz para visualizar los correos electrónicos que envió su base de datos. De esta forma, no debe preocuparse de enviar correos electrónicos de prueba a sus contactos.

  * Ajustes de proveedores de pago y de envío en el modo de prueba.

  * Deshabilitar servicios de compras dentro de la aplicación.

La base de datos más reciente seguirá activa de forma indefinida, las más
antiguas de la misma rama se pueden depurar para hacer espacio para las
nuevas. Serán válidas por 3 meses, luego deberá volver a crear la rama. Si
realiza cambios de configuración o de vista en estas bases de datos, asegúrese
de documentarlos o escribirlos directamente en los módulos de la rama con
archivos de datos XML que sobreescriban la configuración o vista
predeterminada.

En Odoo no se realizan las pruebas unitarias porque, hasta ahora, se utilizan
datos de demostración y no se cargan en la base de datos de producción. Si más
adelante Odoo es compatible con la ejecución de pruebas unitarias sin los
datos de demostración, Odoo.sh considerará ejecutar las pruebas en las bases
de datos de prueba.

### Etapa de desarrollo

Las ramas de desarrollo crean nuevas bases de datos con los datos de
demostración para ejecutar pruebas unitarias. Los módulos instalados son los
que usted incluye en sus ramas. Puede cambiar la lista de módulos a instalar
en sus [ajustes de proyecto](settings.html#odoosh-gettingstarted-settings-
modules-installation).

Cuando envía una nueva confirmación a una de estas ramas, se inicia un nuevo
servidor con una base de datos creada desde cero y la nueva revisión de la
rama. Se cargan los datos de demostración y se llevan a cabo las pruebas
unitarias de forma predeterminada. Esto verifica que sus cambios no dañen
ninguna de las funciones que prueban. Si lo desea, puede deshabilitar las
pruebas o permitir que se ejecuten pruebas específicas con etiquetas
personalizadas en los ajustes de la rama.

De forma similar a las ramas de prueba, los correos electrónicos no se envían
porque los intercepta un mailcatcher y las acciones planificadas no se activan
con tanta frecuencia porque la base de datos no está en uso.

Las bases de datos creadas para las ramas de desarrollo tienen una duración
estimada de tres días. Pasado este tiempo, pueden eliminarse de forma
automática para hacer espacio para nuevas bases de datos sin previo aviso.

### Fusionar ramas

Puede fusionar sus ramas con facilidad al arrastrarlas y soltarlas entre sí.

![../../../_images/interface-branches-merge.png](../../../_images/interface-
branches-merge.png)

Cuando desee probar los cambios de sus ramas de desarrollo con los datos de
producción, puede:

  * Fusionar la rama de desarrollo con su rama de prueba. Arrástrela y suéltela en la rama de prueba deseada.

  * Arrastrar y soltar la rama de desarrollo en el título de la sección de prueba, de esta forma se convierte en una rama de prueba.

Cuando sus cambios más recientes están listos para pasar a producción, puede
arrastrar y soltar su rama de prueba en su rama de producción para fusionarlas
y desplegar sus nuevas funciones en producción.

Si así lo desea, también puede fusionar sus ramas de desarrollo con su rama de
producción. Esto significa que se salta la validación de sus cambios con los
datos de producción a través de la rama de prueba.

Puede fusionar sus ramas de desarrollo entre sí, también puede hacerlo con sus
ramas de prueba.

Además, puede usar `git merge` desde su estación de trabajo para fusionar sus
ramas. Odoo.sh recibirá una notificación cuando suba las nuevas revisiones a
sus ramas.

Cuando fusiona una rama de prueba con la rama de producción solo fusiona el
código fuente. Cualquier cambio de configuración que haga en la base de datos
de prueba no pasará a la base de datos de producción.

Si prueba los cambios de configuración en las ramas de prueba y quiere que
apliquen para producción, puede:

  * Escribir los cambios de configuración en los archivos de datos XML que sobreescriben la configuración o vistas predeterminadas en sus ramas, luego cambie a una versión superior de su módulo en su archivo manifest (___manifest__.py_) para activar la actualización del módulo al fusionar su rama de prueba con su rama de producción. Esta es la mejor práctica para obtener una mejor escalabilidad de sus desarrollos, ya que utilizará las funciones de creación de versiones de Git para todos sus cambios de configuración y, por lo tanto, todos sus cambios tienen trazabilidad.

  * Copiar los cambios desde su base de datos de prueba y pegarlos en su base de datos de producción.

## Pestañas

### Historial

El resumen del historial de su rama incluye:

  * Los mensajes de las confirmaciones y sus autores.

  * Los diversos eventos vinculados a la plataforma, como los cambios de etapa, importaciones de bases de datos y restauraciones de las copias de seguridad.

![../../../_images/interface-branches-history.png](../../../_images/interface-
branches-history.png)

Para cada evento, en la esquina superior derecha se muestra un estado que
proporciona información sobre la operación actual de la base de datos
(instalación, actualización, importación de respaldo, etc.) o su resultado
(retroalimentación de pruebas, importaciones de respaldos exitosas, etc.).
Cuando una operación es exitosa, puede acceder a la base de datos mediante el
botón _Conectar_.

### Correos electrónicos

Esta pestaña contiene el mailcatcher. Muestra un resumen de los correos
electrónicos que envió su base de datos y está disponible para sus ramas de
desarrollo y de prueba, ya que los correos electrónicos de su base de datos de
producción se envían en lugar de ser interceptados.

![../../../_images/interface-branches-mails.png](../../../_images/interface-
branches-mails.png)

### Shell

Un acceso de shell a su contenedor. Puede realizar comandos básicos de Linux
(`ls`, `top`) y abrir un shell en su base de datos al escribir `psql`.

![../../../_images/interface-branches-shell.png](../../../_images/interface-
branches-shell.png)

Puede abrir varias pestañas y arrastrar y soltarlas para acomodar el diseño
como desee, lado a lado, por ejemplo.

Nota

No se garantiza que las instancias de shell sean de larga duración. Los shells
inactivos se pueden desconectar en cualquier momento para liberar recursos.

### Editor

Un entorno de desarrollo integrado (IDE) en línea para editar el código
fuente. También puede abrir terminales, consolas de Python e incluso consolas
de shell de Odoo.

![../../../_images/interface-branches-editor.png](../../../_images/interface-
branches-editor.png)

Puede abrir varias pestañas y arrastrar y soltarlas para acomodar el diseño
como desee, lado a lado, por ejemplo.

### Monitoreo

Este enlace contiene varias métricas de monitoreo de la compilación actual.

![../../../_images/interface-branches-
monitoring.png](../../../_images/interface-branches-monitoring.png)

Puede ampliar, cambiar el rango de tiempo o seleccionar una métrica específica
en cada gráfico. Las anotaciones disponibles en los gráficos pueden ayudarle a
relacionar los cambios en la compilación (importación de base de datos, push
de Git, etc.).

### Registros

Un editor para revisar los registros de su servidor.

![../../../_images/interface-branches-logs.png](../../../_images/interface-
branches-logs.png)

Hay distintos registros disponibles:

  * install.log: los registros de la instalación de la base de datos. En una rama de desarrollo, se incluyen los registros de las pruebas.

  * pip.log: los registros de la instalación de las dependencias de Python.

  * odoo.log: los registros del servidor en ejecución.

  * update.log: los registros de las actualizaciones de la base de datos.

  * pg_long_queries.log: los registros de las consultas de psql que tardan una cantidad inusual de tiempo.

Si se agregan nuevas líneas a los registros, se mostrarán de forma automática.
Si se desplaza al final de la página, el navegador se desplazará de forma
automática cada que se agregue una nueva línea.

Puede pausar la recuperación de registros si hace clic en el botón
correspondiente en la esquina superior derecha de la vista. La recuperación se
detiene en automático después de 5 minutos y puede reiniciarla al hacer clic
en el botón de Iniciar.

### Respaldos

Esta es una lista de respaldos disponibles para descargar y restaurar. Es
posible realizar una copia de seguridad manual e importar una base de datos.

![../../../_images/interface-branches-backups.png](../../../_images/interface-
branches-backups.png)

Odoo.sh hace respaldos diarios de la base de datos de producción. Mantiene 7
respaldos diarios, 4 semanales y 3 mensuales. Cada respaldo incluye el dump de
la base de datos, archivos almacenados (archivos adjuntos, campos binarios),
registros y sesiones.

Las bases de datos de prueba y de desarrollo no se respaldan. Sin embargo,
puede restaurar un respaldo de la base de datos de producción en sus ramas de
prueba, o recuperar manualmente los datos que se eliminaron por accidente de
la base de datos de producción.

La lista contiene los respaldos almacenados en el servidor que aloja su base
de datos de producción. Este servidor solo guarda un mes de respaldos, es
decir, 7 diarios y 4 semanales.

Los servidores de respaldo específicos guardan los mismos respaldos, así como
3 respaldos mensuales adicionales. Para restaurar o descargar uno de los
respaldos mensuales, [contáctenos](https://www.odoo.com/help).

Si fusiona una confirmación que actualiza la versión de uno o varios módulos
(en `__manifest__.py`), o sus dependencias de Python vinculadas (en
`requirements.txt`), Odoo.sh realiza un respaldo automático (se marca en la
lista con el tipo Actualización), ya que se cambiará el contenedor por la
instalación de nuevos paquetes pip o se cambiará la base de datos y se
activará la actualización del módulo. En ambos casos se realiza un respaldo,
ya que puede ocurrir algún error.

Si fusiona una confirmación que solo cambia parte del código sin las
modificaciones antes mencionadas, entonces Odoo.sh no realiza ningún respaldo
porque no se modifican ni el contenedor ni la base de datos y la plataforma lo
considera seguro. Como precaución adicional, puede hacer un respaldo manual
antes de hacer cambios grandes en sus fuentes de producción en caso de que
ocurra un error (estos respaldos manuales están disponibles por una semana).
Para evitar el abuso de la función, el límite es de 5 respaldos manuales por
día.

La función _Importar base de datos_ acepta archivos de bases de datos en los
formatos proporcionados por:

  * El gestor estándar de bases de datos de Odoo (disponible para servidores de Odoo alojados de forma local en `/web/database/manager`).

  * El gestor en línea de bases de datos de Odoo.

  * El botón de descarga de respaldo de Odoo.sh en la pestaña _Respaldos_.

  * El botón de descarga de dump de Odoo.sh en la [Vista de compilaciones](builds.html#odoosh-gettingstarted-builds).

### Actualizar

Está disponible para ramas de producción y de prueba de proyectos válidos.

Ver también

[Documentación de actualización](../../upgrade.html)

### Ajustes

Aquí puede encontrar algunos ajustes que solo aplican a la rama seleccionada.

![../../../_images/interface-branches-
settings.jpg](../../../_images/interface-branches-settings.jpg)

**Comportamiento después de una nueva confirmación**

Para las ramas de desarrollo y de prueba, puede cambiar el comportamiento de
las ramas después de una nueva confirmación. De forma predeterminada, una rama
de desarrollo creará una nueva compilación y la rama de prueba actualizará la
compilación anterior (consulte Etapa de producción). Esto es útil si la
función con la que está trabajando requiere ajustes específicos, así no deberá
volver a configurarlos manualmente en cada confirmación. Al elegir una nueva
compilación para una etapa de prueba, creará una nueva copia de la compilación
de producción cuando envíe sus cambios. Una rama que se regresa de un estado
de prueba a uno de desarrollo se establecerá como “No hacer nada” de forma
automática.

**Instalación de módulos**

Elija los módulos que se instalarán de forma automática en sus compilaciones
de desarrollo.

![../../../_images/interface-settings-
modulesinstallation.png](../../../_images/interface-settings-
modulesinstallation.png)

  * _Instalar solo mis módulos_ solo instalará los módulos de la rama. Esta es la opción predeterminada. Se excluyen los [submódulos](../advanced/submodules.html#odoosh-advanced-submodules).

  * _Instalación completa (todos los módulos)_ instalará los módulos de la rama, los módulos incluidos en los submódulos y todos los módulos estándar de Odoo. El conjunto de prueba se deshabilita al ejecutar la instalación completa.

  * _Instalar una lista de módulos_ instalará los módulos que se especifican en el campo debajo de esta opción. Debe colocar los nombres técnicos de los módulos separados por comas.

Si se habilitan las pruebas, el conjunto de módulos estándar de Odoo puede
tardar hasta 1 hora. Este ajuste solo aplica a compilaciones de desarrollo.
Las compilaciones de prueba duplican la compilación de producción y la
compilación de producción solo instala la base.

**Conjunto de prueba**

En el caso de las ramas de desarrollo, puede elegir habilitar o deshabilitar
el conjunto de prueba, se habilita de forma predeterminada. Cuando el conjunto
de prueba está habilitado, puede restringirlo al especificar [etiquetas de
prueba](../../../developer/reference/backend/testing.html#developer-reference-
testing-selection).

**Versión de Odoo**

Solo puede cambiar la versión de Odoo, para las ramas de desarrollo, si desea
probar un código actualizado o desarrollar funciones mientras su base de datos
está en el proceso de actualizarse a una nueva versión.

Además, para cada versión tiene dos opciones en cuanto a la actualización de
código.

  * Puede elegir beneficiarse de las últimas correcciones de bugs, seguridad y rendimiento de forma automática. Las fuentes de su servidor de Odoo se actualizarán cada semana. Esta es la opción “Más reciente”.

  * Puede elegir fijar las fuentes de Odoo a una revisión específica al seleccionarlas de una lista de fechas. Las revisiones vencen después de 3 meses y se le notificará por correo electrónico cuando se acerque la fecha de vencimiento. Si no toma ninguna medida, se establecerá a la última revisión de forma automática.

**Dominios personalizados**

Aquí puede configurar dominios adicionales para la rama seleccionada. Puede
agregar otros dominios _< name>.odoo.com_ o sus propios dominios
personalizados. Para hacer esto último, debe:

  * Ser propietario o comprar el nombre de dominio.

  * Agregar el nombre del dominio a esta lista.

  * Configurar el nombre de dominio con un registro `CNAME` establecido como el nombre de dominio de su base de datos de producción en el gestor de nombre de dominio de su registrador.

Por ejemplo, para asociar _www.miempresa.com_ con su base de datos
_miempresa.odoo.com_ :

  * En Odoo.sh, agregue _www.miempresa.com_ a los dominios personalizados de los ajustes de su proyecto.

  * En su gestor de nombre de dominio (por ejemplo, _godaddy.com_ , _gandi.net_ , _ovh.com_), configure _www.miempresa.com_ con un registro `CNAME` con _miempresa.odoo.com_ como valor.

No se aceptan los dominios simples (por ejemplo, _miempresa.com_):

  * Solo se pueden configurar al usar registros `A`.

  * Los registros `A` solo aceptan direcciones IP como valor.

  * La dirección IP de su base de datos puede cambiar después de una actualización, error de hardware o si cambia el alojamiento de su base de datos a otro país o continente.

Por lo tanto, los dominios simples podrían dejar de funcionar repentinamente
debido a este cambio de dirección IP.

Además, si desea que tanto _miempresa.com_ como _www.miempresa.com_ funcionen
con su base de datos, hacer que la primera dirección redirija a la segunda es
una de las [mejores prácticas de
SEO](https://developers.google.com/search/docs/fundamentals/seo-starter-
guide?visit_id=638237429119626675-609718300&rd=1&hl=es-419) (Consulte
_Proporciona una versión de una URL para llegar a un documento_) para tener
una URL principal. Por lo tanto, solo debe configurar _miempresa.com_ para que
redirija a _www.miempresa.com_. La mayoría de los gestores de dominios tienen
la función de configurar esta redirección, esto suele llamarse redirección
web.

**HTTPS/SSL**

Si la redirección se configura de forma correcta, la plataforma generará en
automático un certificado SSL con [Let’s
Encrypt](https://letsencrypt.org/about/) en una hora y podrá acceder a su
dominio mediante HTTPS.

Aunque por ahora no es posible configurar sus propios certificados SSL en la
plataforma de Odoo.sh, consideraremos agregar esta función si existe la
suficiente demanda.

**Cumplimiento de SPF y DKIM**

Si el dominio de las direcciones de correo electrónico de sus usuarios utiliza
SPF (Convenio de remitentes) o DKIM (DomainKeys Identified Mail) no olvide
autorizar a Odoo como host emisor en los ajustes de su nombre de dominio para
incrementar la entrega de sus correos salientes. Los pasos de configuración se
explican en la documentación sobre
[SPF](../../../applications/general/email_communication/email_domain.html#email-
communication-spf-compliant) y
[DKIM](../../../applications/general/email_communication/email_domain.html#email-
communication-dkim-compliant).

Advertencia

En caso de no configurar su SPF o DKIM para autorizar a Odoo como host emisor
podría ocasionar que sus contactos reciban sus correos en la bandeja de spam.

## Comandos de shell

En la esquina superior derecha de la vista se encuentran disponibles distintos
comandos de shell.

![../../../_images/interface-branches-
shellcommands.png](../../../_images/interface-branches-shellcommands.png)

Puede copiar cada comando al portapapeles para usarlo en una terminal, algunos
se pueden usar desde Odoo.sh al hacer clic en el botón de _Ejecutar_. En este
caso, aparecerá una ventana emergente que invitará al usuario a definir
marcadores de posición eventuales como `<URL>`, `<PATH>`, etc.

### Clonar

Descarga el repositorio de Git.

    
    
    $ git clone --recurse-submodules --branch master git@github.com:odoo/odoo.git
    

Esto clona el repositorio _odoo/odoo_.

  * `--recurse-submodules`: descarga los submódulos de su repositorio. También se descargan los submódulos incluidos en los submódulos.

  * `--branch`: verifica una rama específica del repositorio, en este caso _master_.

El botón de _Ejecutar_ no está disponible para este comando, ya que está
pensado para usarse en sus máquinas.

### Bifurcar

Crea una nueva rama según la rama actual.

    
    
    $ git checkout -b feature-1 master
    

Esto crea una nueva rama llamada _feature-1_ desde la rama _master_ y después
la comprueba.

    
    
    $ git push -u origin feature-1
    

Sube la nueva rama _feature-1_ a su repositorio remoto.

### Fusionar

Fusiona la rama actual con otra rama.

    
    
    $ git merge staging-1
    

Esto fusiona la rama _staging-1_ con la rama actual.

    
    
    $ git push -u origin master
    

Sube los cambios que agregó a la rama _master_ de su repositorio remoto.

### SSH

#### Configuración

Para poder utilizar SSH, debe configurar la clave pública de su perfil SSH (si
aún no lo ha hecho). Siga estos pasos:

  1. [Genere una nueva clave SSH](https://docs.github.com/es/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key).

  2. [Copie la clave SSH a su portapapeles](https://docs.github.com/es/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) (solo siga el primer paso de esta página).

  3. Pegue el contenido copiado en las claves SSH de su perfil y haga clic en «Agregar».

![../../../_images/SSH-key-pasting.png](../../../_images/SSH-key-pasting.png)

  4. La clave debe aparecer a continuación.

![../../../_images/SSH-key-appearing.png](../../../_images/SSH-key-
appearing.png)

#### Conexión

Para conectar sus compilaciones que usan SSH, utilice el siguiente comando en
una terminal:

    
    
    $ ssh <build_id>@<domain>
    

Encontrará un atajo para este comando en la pestaña SSH, en la esquina
superior derecha.

![../../../_images/SSH-panel.png](../../../_images/SSH-panel.png)

Si tiene los [permisos de acceso adecuados](settings.html#odoosh-
gettingstarted-settings-collaborators) en el proyecto, se le concederá acceso
SSH a la compilación.

Nota

No se garantiza que las conexiones SSH sean de larga duración. Las conexiones
inactivas se desconectarán en cualquier momento para liberar recursos.

### Submódulo

Agregue una rama de otro repositorio a su rama actual como un _submódulo_.

Los _submódulos_ le permiten usar módulos de otros repositorios en su
proyecto.

Puede encontrar más información sobre la función de submódulos en el capítulo
[Submódulos](../advanced/submodules.html#odoosh-advanced-submodules) de esta
documentación.

    
    
    $ git submodule add -b master <URL> <PATH>
    

Agrega la rama _master_ del repositorio _< URL>_ como un submódulo en la ruta
_< PATH>_ a su rama actual.

    
    
    $ git commit -a
    

Confirma todos sus cambios actuales.

    
    
    $ git push -u origin master
    

Sube los cambios que agregó a la rama _master_ de su repositorio remoto.

### Eliminar

Elimina una rama de su repositorio.

    
    
    $ git push origin :master
    

Elimina la rama en su repositorio remoto.

    
    
    $ git branch -D master
    

Elimina la rama en su copia local del repositorio.

