# Konvergo ERP en línea

[Konvergo ERP en línea](https://www.odoo.com/trial) proporciona bases de datos
privadas y nosotros nos encargamos de gestionarlas y alojarlas. Puede usarlas
para producción a largo plazo o para probar Konvergo ERP con detenimiento, incluso con
personalizaciones que no requieren código.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Konvergo ERP en línea no es compatible con módulos personalizados ni con nuestra tienda de aplicaciones.</p>
</div>

Es posible acceder a las bases de datos de Konvergo ERP en línea con cualquier
navegador web y no necesitan de instalación local.

Si lo que quiere es probar Konvergo ERP rápido, tenemos disponibles instancias de
[demostración](https://demo.odoo.com) compartidas. No es necesario
registrarse, pero cada instancia está disponible por unas pocas horas.

## Gestión de bases de datos

Para gestionar una base de datos, vaya al [gestor de bases de
datos](https://www.odoo.com/my/databases) e inicie sesión como administrador.

Todas las opciones principales para la gestión de bases de datos están
disponibles al hacer clic sobre el nombre de la base de datos, a excepción de
la opción de actualizar. Para acceder a esa opción, haga clic en el ícono de
la **flecha dentro del circulo** que está a lado del nombre de la base de
datos. Solo aparecerá si hay una actualización disponible.

![Acceder a las opciones de gestión de las bases de datos.
](../_images/database-manager.png)

  * Actualizar

  * Duplicar

  * Renombrar

  * Descargar

  * Nombres de dominio

  * Etiquetas

  * Eliminar

  * Contáctenos

  * Invitar o eliminar usuarios

## Actualizar

Active una actualización para la base de datos.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p>Si desea obtener más información sobre el proceso de actualización, consulte la <a href="upgrade#upgrade-request-test-database"><span class="std std-ref">documentación de actualización en línea de Konvergo ERP</span></a>.</p>
</div>

## Duplicar

Cree una copia exacta de la base de datos, la cual puede usar para realizar
pruebas sin comprometer las operaciones diarias.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><ul>
<li><p>Haciendo clic en <b>Para propósitos de prueba</b>, todas las acciones externas (correos, pagos, entregas, ordenes, etc.) se deshabilitan de manera predeterminada en la base de datos duplicada.</p></li>
<li><p>Las bases de datos duplicadas expiran automáticamente después de 15 días.</p></li>
<li><p>Es posible hacer un máximo de cinco duplicados por base de datos. Contacte a <a href="https://www.odoo.com/help">soporte</a> para cambiar este límite en circunstancias excepcionales.</p></li>
</ul>
</div>

## Renombrar

Cambie el nombre de la base de datos y su URL.

## Descargar

Descargue un archivo ZIP que contenga un respaldo de la base de datos.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Las bases de datos se respaldan todos los días de acuerdo al <a href="https://www.odoo.com/cloud-sla">acuerdo de nivel de servicio de Konvergo ERP alojado en la nube</a>.</p>
</div>

## Nombres de dominio

Utilice un [nombre de
dominio](../applications/websites/website/configuration/domain_names)
personalizado para acceder a la base de datos mediante otra URL.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Puede <a href="../applications/websites/website/configuration/domain_names#domain-name-register"><span class="std std-ref">registrar un nombre de dominio de forma gratuita</span></a>.</p>
</div>

## Etiquetas

Agregue etiquetas para identificar y ordenar sus bases de datos con facilidad.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Puede buscar etiquetas en la barra de búsqueda.</p>
</div>

## Eliminar

Elimine una base de datos de forma instantánea.

<div class="alert alert-danger">
<p class="alert-title">
Peligro</p><p>Eliminar una base de datos significa que se perderán todos los datos de forma permanente. La eliminación es instantánea y se aplica a todos los usuarios. Le recomendamos crear una copia de seguridad de la base de datos antes de eliminarla.</p>
</div>

Lea con atención el mensaje de advertencia y continúe solo si comprende por
completo lo que implica eliminar una base de datos.

![El mensaje de advertencia que aparece antes de eliminar una base de
datos.](../_images/delete.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Solo un administrador puede eliminar una base de datos.</p></li>
<li><p>El nombre de la base de datos estará disponible inmediatamente para todos.</p></li>
<li><p>No es posible borrar una base de datos que ya expiró o que está vinculada a una suscripción. En ese caso, póngase en contacto con el <a href="https://www.odoo.com/help">soporte de Konvergo ERP</a>.</p></li>
</ul>
</div>

## Contáctenos

Acceda a la [página de soporte de Konvergo ERP](https://www.odoo.com/help) con los
detalles de su base de datos previamente ingresados.

## Invitar o eliminar usuarios

Para invitar usuarios, escriba el correo electrónico del nuevo usuario y haga
clic en **Invitar**. Para agregar varios usuarios, haga clic en **Agregar más
usuarios**.

![Invitar a un usuario a una base de datos](../_images/invite-users.png)

Para eliminar usuarios, selecciónelos y haga clic en **Eliminar**.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../applications/general/users">Usuarios</a></p></li>
<li><p><a href="odoo_accounts">Cuentas de Konvergo ERP.com</a></p></li>
</ul>
</div>

