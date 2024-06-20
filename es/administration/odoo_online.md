# Odoo en línea

[Odoo en línea](https://www.odoo.com/trial) proporciona bases de datos
privadas y nosotros nos encargamos de gestionarlas y alojarlas. Puede usarlas
para producción a largo plazo o para probar Odoo con detenimiento, incluso con
personalizaciones que no requieren código.

Nota

Odoo en línea no es compatible con módulos personalizados ni con nuestra
tienda de aplicaciones.

Es posible acceder a las bases de datos de Odoo en línea con cualquier
navegador web y no necesitan de instalación local.

Si lo que quiere es probar Odoo rápido, tenemos disponibles instancias de
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

Ver también

Si desea obtener más información sobre el proceso de actualización, consulte
la [documentación de actualización en línea de Odoo](upgrade.html#upgrade-
request-test-database).

## Duplicar

Cree una copia exacta de la base de datos, la cual puede usar para realizar
pruebas sin comprometer las operaciones diarias.

Importante

  * Haciendo clic en Para propósitos de prueba, todas las acciones externas (correos, pagos, entregas, ordenes, etc.) se deshabilitan de manera predeterminada en la base de datos duplicada.

  * Las bases de datos duplicadas expiran automáticamente después de 15 días.

  * Es posible hacer un máximo de cinco duplicados por base de datos. Contacte a [soporte](https://www.odoo.com/help) para cambiar este límite en circunstancias excepcionales.

## Renombrar

Cambie el nombre de la base de datos y su URL.

## Descargar

Descargue un archivo ZIP que contenga un respaldo de la base de datos.

Nota

Las bases de datos se respaldan todos los días de acuerdo al [acuerdo de nivel
de servicio de Odoo alojado en la nube](https://www.odoo.com/cloud-sla).

## Nombres de dominio

Utilice un [nombre de
dominio](../applications/websites/website/configuration/domain_names.html)
personalizado para acceder a la base de datos mediante otra URL.

Truco

Puede [registrar un nombre de dominio de forma
gratuita](../applications/websites/website/configuration/domain_names.html#domain-
name-register).

## Etiquetas

Agregue etiquetas para identificar y ordenar sus bases de datos con facilidad.

Truco

Puede buscar etiquetas en la barra de búsqueda.

## Eliminar

Elimine una base de datos de forma instantánea.

Peligro

Eliminar una base de datos significa que se perderán todos los datos de forma
permanente. La eliminación es instantánea y se aplica a todos los usuarios. Le
recomendamos crear una copia de seguridad de la base de datos antes de
eliminarla.

Lea con atención el mensaje de advertencia y continúe solo si comprende por
completo lo que implica eliminar una base de datos.

![El mensaje de advertencia que aparece antes de eliminar una base de
datos.](../_images/delete.png)

Nota

  * Solo un administrador puede eliminar una base de datos.

  * El nombre de la base de datos estará disponible inmediatamente para todos.

  * No es posible borrar una base de datos que ya expiró o que está vinculada a una suscripción. En ese caso, póngase en contacto con el [soporte de Odoo](https://www.odoo.com/help).

## Contáctenos

Acceda a la [página de soporte de Odoo](https://www.odoo.com/help) con los
detalles de su base de datos previamente ingresados.

## Invitar o eliminar usuarios

Para invitar usuarios, escriba el correo electrónico del nuevo usuario y haga
clic en Invitar. Para agregar varios usuarios, haga clic en Agregar más
usuarios.

![Invitar a un usuario a una base de datos](../_images/invite-users.png)

Para eliminar usuarios, selecciónelos y haga clic en Eliminar.

Ver también

  * [Usuarios](../applications/general/users.html)

  * [Cuentas de Odoo.com](odoo_accounts.html)

