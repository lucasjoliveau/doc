# Alojamiento

## Cambiar la solución de alojamiento

Las instrucciones para cambiar el tipo de alojamiento de una base de datos
dependen de la solución que utiliza en ese momento y la solución a la que debe
mover la base de datos.

## Transferir una base de datos local

### A Odoo en línea

Importante

  * Odoo en línea _no_ es compatible con las **aplicaciones que no son estándar**.

  * La versión actual de la base de datos debe ser [compatible](supported_versions.html).

  1. Cree un [duplicado de la base de datos](on_premise.html#on-premise-duplicate).

  2. En este duplicado, desinstale todas las **aplicaciones que no son estándar**.

  3. Utilice el gestor de bases de datos para obtener un _dump con Filestore_.

  4. [Envíe un ticket a soporte](https://www.odoo.com/help) con la siguiente información:

     * su **número de suscripción** ,

     * la **URL** que desea utilizar para la base de datos (por ejemplo, `empresa.odoo.com`), y

     * el **dump** como archivo adjunto o un enlace al archivo (es necesario si el archivo pesa más de 60 MB).

  5. Odoo se asegura de que la base de datos sea compatible antes de publicarla en línea. Es posible que Odoo se ponga en contacto con usted si ocurren problemas técnicos durante el proceso.

Nota

En situaciones donde el tiempo es limitado deberá [enviar un ticket de
soporte](https://www.odoo.com/help) tan pronto como le sea posible programar
su transferencia.

### A Odoo.sh

Siga las instrucciones de la [sección Importar su base de
datos](odoo_sh/getting_started/create.html#odoo-sh-import-your-database) de la
documentación _Cree su proyecto_ de Odoo.sh.

## Transferir una base de datos de Odoo en línea

Importante

Las [versiones intermedias](supported_versions.html#supported-versions) de
Odoo en línea no son compatibles con Odoo.sh ni de forma local. Si la base de
datos que transferirá se ejecuta en una versión intermedia, entonces debe
actualizarla a la siguiente [versión
principal](supported_versions.html#supported-versions), espere su lanzamiento
en caso de que sea necesario.

Example

Para transferir una base de datos en línea que se ejecuta en Odoo 16.3,
primero tendría que actualizarla a Odoo 17.0.

Truco

Haga clic en el icono de engranaje (⚙) ubicado junto al nombre de la base de
datos en el [gestor de bases de datos de Odoo en
línea](https://www.odoo.com/my/databases/) para visualizar su número de
versión.

Advertencia

Si hay una suscripción activa de Odoo vinculada a la base de datos que está
migrando, comuníquese con un gerente de servicio al cliente o [envíe un ticket
de soporte](https://www.odoo.com/help) para completar la transferencia de la
suscripción.

### A local

  1. Inicie sesión en [el gestor de bases de datos de Odoo en línea](https://www.odoo.com/my/databases/) y haga clic en el icono de engranaje (⚙) ubicado junto al nombre de la base de datos para descargar una copia de seguridad. [Contacte al soporte de Odoo](https://www.odoo.com/help) si ocurre un error con la descarga porque el archivo es demasiado grande.

  2. Restaure la base de datos desde el gestor en su servidor local con la copia de seguridad.

### A Odoo.sh

  1. Inicie sesión en [el gestor de bases de datos de Odoo en línea](https://www.odoo.com/my/databases/) y haga clic en el icono de engranaje (⚙) ubicado junto al nombre de la base de datos para descargar una copia de seguridad. [Contacte al soporte de Odoo](https://www.odoo.com/help) si ocurre un error con la descarga porque el archivo es demasiado grande.

  2. Siga las instrucciones de la [sección Importar su base de datos](odoo_sh/getting_started/create.html#odoo-sh-import-your-database) de la documentación _Cree su proyecto_ de Odoo.sh.

## Transferir una base de datos de Odoo.sh

### A Odoo en línea

Importante

Odoo en línea _no_ es compatible con las **aplicaciones que no son estándar**.

  1. Desinstale todas las **aplicaciones no estándar** en una compilación de prueba antes de hacerlo en la de producción.

  2. [Cree un ticket de soporte](https://www.odoo.com/help) incluyendo lo siguiente:

     * su **número de suscripción** ,

     * la **URL** que desee usar para la base de datos (por ejemplo, `company.odoo.com`),

     * la **rama** que debe migrar,

     * la **región** en la que quiere que su base de datos se aloje (América, Europa o Asia),

     * los usuarios que serán **administradores** , y

     * **cuándo** (y en qué zona horaria) desea que su base de datos esté funcionando.

  3. Odoo se asegura de que la base de datos sea compatible antes de publicarla en línea. Es posible que Odoo se ponga en contacto con usted si ocurren problemas técnicos durante el proceso.

Nota

  * En situaciones donde el tiempo es limitado deberá [enviar un ticket de soporte](https://www.odoo.com/help) tan pronto como le sea posible programar su transferencia.

  * Seleccione la **región** más cercana a sus usuarios para reducir la latencia.

  * Los futuros **administradores** deben tener una cuenta en Odoo.com

  * La **fecha y hora** específicas en las que desea que la base de datos esté en funcionamiento son muy útiles para organizar el cambio de un servidor de Odoo.sh a los servidores de Odoo en línea.

  * Las bases de datos **no se pueden utilizar** durante la migración.

### A local

  1. Descargue un [respaldo de su base de datos de producción de Odoo.sh](odoo_sh/getting_started/branches.html#odoo-sh-branches-backups).

  2. Restaure la base de datos desde el gestor en su servidor local con la copia de seguridad.

