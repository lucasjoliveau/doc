# Alojamiento

## Cambiar la solución de alojamiento

Las instrucciones para cambiar el tipo de alojamiento de una base de datos
dependen de la solución que utiliza en ese momento y la solución a la que debe
mover la base de datos.

## Transferir una base de datos local

### A Konvergo ERP en línea

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><ul>
<li><p>Konvergo ERP en línea <em>no</em> es compatible con las <b>aplicaciones que no son estándar</b>.</p></li>
<li><p>La versión actual de la base de datos debe ser <a href="supported_versions">compatible</a>.</p></li>
</ul>
</div>

  1. Cree un [duplicado de la base de datos](on_premise#on-premise-duplicate).

  2. En este duplicado, desinstale todas las **aplicaciones que no son estándar**.

  3. Utilice el gestor de bases de datos para obtener un _dump con Filestore_.

  4. [Envíe un ticket a soporte](https://www.odoo.com/help) con la siguiente información:

     * su **número de suscripción** ,

     * la **URL** que desea utilizar para la base de datos (por ejemplo, `empresa.odoo.com`), y

     * el **dump** como archivo adjunto o un enlace al archivo (es necesario si el archivo pesa más de 60 MB).

  5. Konvergo ERP se asegura de que la base de datos sea compatible antes de publicarla en línea. Es posible que Konvergo ERP se ponga en contacto con usted si ocurren problemas técnicos durante el proceso.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>En situaciones donde el tiempo es limitado deberá <a href="https://www.odoo.com/help">enviar un ticket de soporte</a>  tan pronto como le sea posible programar su transferencia.</p>
</div>

### A Konvergo ERP.sh

Siga las instrucciones de la [sección Importar su base de
datos](odoo_sh/getting_started/create#odoo-sh-import-your-database) de la
documentación _Cree su proyecto_ de Konvergo ERP.sh.

## Transferir una base de datos de Konvergo ERP en línea

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Las <a href="supported_versions#supported-versions"><span class="std std-ref">versiones intermedias</span></a> de Konvergo ERP en línea no son compatibles con Konvergo ERP.sh ni de forma local. Si la base de datos que transferirá se ejecuta en una versión intermedia, entonces debe actualizarla a la siguiente <a href="supported_versions#supported-versions"><span class="std std-ref">versión principal</span></a>, espere su lanzamiento en caso de que sea necesario.</p>
<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Para transferir una base de datos en línea que se ejecuta en Konvergo ERP 16.3, primero tendría que actualizarla a Konvergo ERP 17.0.</p>
</div>
<div class="alert alert-tip">
<p class="alert-title">
Truco</p><p>Haga clic en el icono de engranaje (<b>⚙</b>) ubicado junto al nombre de la base de datos en el <a href="https://www.odoo.com/my/databases/">gestor de bases de datos de Konvergo ERP en línea</a> para visualizar su número de versión.</p>
</div>
<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Si hay una suscripción activa de Konvergo ERP vinculada a la base de datos que está migrando, comuníquese con un gerente de servicio al cliente o <a href="https://www.odoo.com/help">envíe un ticket de soporte</a> para completar la transferencia de la suscripción.</p>
</div>
</div>

### A local

  1. Inicie sesión en [el gestor de bases de datos de Konvergo ERP en línea](https://www.odoo.com/my/databases/) y haga clic en el icono de engranaje (**⚙**) ubicado junto al nombre de la base de datos para **descargar** una copia de seguridad. [Contacte al soporte de Konvergo ERP](https://www.odoo.com/help) si ocurre un error con la descarga porque el archivo es demasiado grande.

  2. Restaure la base de datos desde el gestor en su servidor local con la copia de seguridad.

### A Konvergo ERP.sh

  1. Inicie sesión en [el gestor de bases de datos de Konvergo ERP en línea](https://www.odoo.com/my/databases/) y haga clic en el icono de engranaje (**⚙**) ubicado junto al nombre de la base de datos para **descargar** una copia de seguridad. [Contacte al soporte de Konvergo ERP](https://www.odoo.com/help) si ocurre un error con la descarga porque el archivo es demasiado grande.

  2. Siga las instrucciones de la [sección Importar su base de datos](odoo_sh/getting_started/create#odoo-sh-import-your-database) de la documentación _Cree su proyecto_ de Konvergo ERP.sh.

## Transferir una base de datos de Konvergo ERP.sh

### A Konvergo ERP en línea

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Konvergo ERP en línea <em>no</em> es compatible con las <b>aplicaciones que no son estándar</b>.</p>
</div>

  1. Desinstale todas las **aplicaciones no estándar** en una compilación de prueba antes de hacerlo en la de producción.

  2. [Cree un ticket de soporte](https://www.odoo.com/help) incluyendo lo siguiente:

     * su **número de suscripción** ,

     * la **URL** que desee usar para la base de datos (por ejemplo, `company.odoo.com`),

     * la **rama** que debe migrar,

     * la **región** en la que quiere que su base de datos se aloje (América, Europa o Asia),

     * los usuarios que serán **administradores** , y

     * **cuándo** (y en qué zona horaria) desea que su base de datos esté funcionando.

  3. Konvergo ERP se asegura de que la base de datos sea compatible antes de publicarla en línea. Es posible que Konvergo ERP se ponga en contacto con usted si ocurren problemas técnicos durante el proceso.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>En situaciones donde el tiempo es limitado deberá <a href="https://www.odoo.com/help">enviar un ticket de soporte</a>  tan pronto como le sea posible programar su transferencia.</p></li>
<li><p>Seleccione la <b>región</b> más cercana a sus usuarios para reducir la latencia.</p></li>
<li><p>Los futuros <b>administradores</b> deben tener una cuenta en Konvergo ERP.com</p></li>
<li><p>La <b>fecha y hora</b> específicas en las que desea que la base de datos esté en funcionamiento son muy útiles para organizar el cambio de un servidor de Konvergo ERP.sh a los servidores de Konvergo ERP en línea.</p></li>
<li><p>Las bases de datos <b>no se pueden utilizar</b> durante la migración.</p></li>
</ul>
</div>

### A local

  1. Descargue un [respaldo de su base de datos de producción de Konvergo ERP.sh](odoo_sh/getting_started/branches#odoo-sh-branches-backups).

  2. Restaure la base de datos desde el gestor en su servidor local con la copia de seguridad.

