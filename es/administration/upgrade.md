# Actualizar

Una actualización es el proceso de trasladar su base de datos de una versión
anterior a una [versión compatible](supported_versions.html) más reciente (por
ejemplo, de Odoo 14.0 a Odoo 16.0). Es muy importante actualizar con
frecuencia, pues cada versión incluye funciones nuevas y mejoradas,
correcciones de errores y parches de seguridad.

Automatic upgrades: Odoo Online's Rolling Release process

El proceso de lanzamiento continuo permite a los clientes de Odoo en línea
actualizar su base de datos directamente desde el envío de un mensaje al
administrador de la base de datos tan pronto como se publique una nueva
versión. La invitación para actualizar solo se envía si no se detectan
problemas durante las pruebas automáticas.

![Verá el mensaje de actualización en la parte superior derecha de la base de
datos.](../_images/rr-upgrade-message.png)

Se recomienda hacer pruebas antes de la actualización. Si hace clic en quiero
probar primero, se le redirigirá al [administrador de bases de
datos](https://www.odoo.com/my/databases/), ahí podrá solicitar una base de
datos de prueba actualizada y verificar que no haya ninguna discrepancia.

**No** se recomienda hacer clic en actualizar ahora sin realizar pruebas
primero, ya que esto activa inmediatamente la actualización de la base de
datos de producción.

Si el proceso de lanzamiento continuo detecta un problema con la
actualización, se desactivará hasta que se resuelva el problema.

Una actualización no cubre:

>   * Cambiar a una versión anterior de Odoo
>
>   * [Cambiar de edición](on_premise/community_to_enterprise.html) (por
> ejemplo, de Community a Enterprise)
>
>   * [Cambiar el tipo de alojamiento](hosting.html#hosting-change-solution)
> (por ejemplo, de local a Odoo en línea)
>
>   * Migración de otro ERP a Odoo
>
>

Advertencia

Si su base de datos contiene módulos personalizados, se podrá actualizar solo
hasta que una versión de sus módulos personalizados que sea compatible con la
versión de Odoo a la que se quiere actualizar esté disponible. Para clientes
que quieran mantener sus módulos personalizados, recomendamos que el proceso
se haga en paralelo, solo deben solicitar una actualización de base de datos y
al mismo tiempo [actualizar el código de sus módulos
personalizados](../developer/howtos/upgrade_custom_db.html).

## Resumen del proceso de actualización

  1. Solicite una base de datos de prueba actualizada (consulte la obtención de una base de datos de prueba actualizada).

  2. Si aplica, actualice el código fuente de su módulo personalizado para que sea compatible con la nueva versión de Odoo (consulte [Upgrade a customized database](../developer/howtos/upgrade_custom_db.html)).

  3. Pruebe exhaustivamente la base de datos actualizada (consulte prueba de la nueva versión de la base de datos).

  4. Reporte cualquier problema que ocurra durante las pruebas a Odoo. Envíe un ticket con la opción [Duda relacionada con mi actualización (en fase de pruebas)](https://odoo.com/help?stage=migration).

  5. Una vez que se resuelvan todos los problemas y esté seguro de que la base de datos actualizada se puede utilizar como su base de datos principal, planifique la actualización de su base de datos de producción.

  6. Solicite la actualización de la base de datos de producción, no permita que esté en uso durante el tiempo que tome completar el proceso (consulte la actualización de la base de datos de producción).

  7. Reporte cualquier problema que ocurra durante la actualización a Odoo. Envíe un ticket con la opción [Duda relacionada con mi actualización (producción)](https://odoo.com/help?stage=post_upgrade).

## Obtener una base de datos de prueba actualizada

La [página de actualización](https://upgrade.odoo.com/) es la plataforma
principal para solicitar una base de datos actualizada. Sin embargo, según el
tipo de alojamiento, puede actualizar desde la línea de comandos (local), el
administrador de bases de datos en línea de Odoo
<<https://odoo.com/my/databases>>_, o su proyecto Odoo.sh
<<https://odoo.sh/project>>_.

Nota

La plataforma de actualización sigue la misma [política de
privacidad](https://www.odoo.com/privacy) que los demás servicios de Odoo.com.
Visite el [reglamento general de protección de
datos](https://www.odoo.com/gdpr) para obtener más información sobre cómo Odoo
maneja sus datos y privacidad.

Odoo OnlineOdoo.shOn-premise

Las bases de datos de Odoo en línea se pueden actualizar de forma manual a
través del [administrador de bases de datos](https://odoo.com/my/databases).

El administrador de la base de datos muestra todas las bases de datos
vinculadas a la cuenta del usuario. Las bases de datos que no están en la
versión más reciente de Odoo muestran un ícono de una flecha en un círculo
junto a su nombre, indicando que se pueden actualizar.

![El administrador de la base de datos con un botón de actualización junto al
nombre de la base de datos.](../_images/databases-page.png)

Haga clic en el icono de la **flecha en un círculo** para iniciar el proceso
de actualización. En la ventana emergente, complete la siguiente información:

  * La **versión** de Odoo a la que desea actualizar, generalmente es la última versión.

  * El **correo electrónico** que debe recibir el enlace a la base de datos actualizada

  * El propósito de la actualización, se establece como prueba de forma automática en su primera solicitud de actualización.

![La ventana emergente "Actualizar base de datos".](../_images/upgrade-
popup.png)

La etiqueta actualización en progreso se muestra junto al nombre de la base de
datos hasta que se complete. Una vez que se termine el proceso, se enviará un
correo electrónico con un enlace a la base de datos de prueba actualizada a la
dirección proporcionada. También podrá acceder a la base de datos desde el
administrador de la base de datos, solo debe hacer clic en la flecha
desplegable antes del nombre de la base de datos.

![Hacer clic en la flecha del menú mostrará la base de datos de prueba
actualizada.](../_images/access-upgraded-db.png)

Odoo.sh está integrado con la plataforma de actualización para hacer el
proceso de actualización más sencillo.

![Proyecto y pestañas de Odoo.sh ](../_images/odoo-sh-staging.png)

El **respaldo automático diario más reciente de producción** se envía a la
[plataforma de actualización](https://www.upgrade.odoo.com).

Una vez que la plataforma de actualización haya terminado de actualizar la
copia de seguridad y la haya cargado en la rama, se colocará en un **modo
especial** : cada vez que envíe una **confirmación a su rama** , se realizará
una **operación de restauración** de la copia de seguridad actualizada y una
**actualización de todos los módulos personalizados**. Esto le permite probar
sus módulos personalizados en una copia exacta de la base de datos
actualizada. Puede encontrar el archivo de registro del proceso de
actualización en su nueva compilación de preparación actualizada en:
file:`~/logs/upgrade.log`.

Importante

Si se trata de bases de datos con módulos personalizados es necesario
actualizar el código fuente con la versión objetivo de Odoo antes de que se
pueda realizar la actualización. Si no hay ninguno, se omitirá el modo
«actualizar al confirmar», se construirá la base de datos actualizada tan
pronto como se transfiera desde la plataforma de actualización y se saldrá del
modo de actualización.

Consulte la página [Upgrade a customized
database](../developer/howtos/upgrade_custom_db.html) para obtener más
información.

Puede iniciar el proceso de actualización estándar al escribir el siguiente
comando en la línea de comandos de la máquina donde se encuentra alojada la
base de datos.

    
    
    $ python <(curl -s https://upgrade.odoo.com/upgrade) test -d <your db name> -t <target version>
    

Puede utilizar el siguiente comando para mostrar la ayuda general y los
comandos principales.

    
    
    $ python <(curl -s https://upgrade.odoo.com/upgrade) --help
    

También puede solicitar una base de datos de prueba actualizada desde la
[página de actualización](https://upgrade.odoo.com/).

Importante

En las bases de datos que tienen módulos personalizados instalados, el código
fuente de estos módulos debe estar actualizado para la nueva versión de Odoo
antes de que se realice la actualización. Consulte [Upgrade a customized
database](../developer/howtos/upgrade_custom_db.html) para obtener más
dtalles.

Nota

  * Por razones de seguridad, solo la persona que envío la solicitud de actualización puede descargarla.

  * Por motivos de almacenaje, debe subir la copia de su base de datos sin un repositorio de archivos al servidor de actualización. Por lo tanto, la base de datos actualizada no contiene el repositorio de archivos de producción.

  * Antes de restaurar la base de datos actualizada, su repositorio de archivos debe estar unido a al repositorio de archivos de producción para que pueda realizar las pruebas bajo las mismas condiciones que la nueva versión.

  * La base de datos actualizada contiene:

    * Un archivo `dump.sql` que contiene la base de datos actualizada.

    * Una carpeta de `repositorio de archivos` que contiene los archivos que se extrajeron de los registros internos de la base de datos en archivos adjuntos (si es que hay) y nuevos archivos estándar de Odoo de la versión objetivo de Odoo (imágenes nuevas, iconos, logos de los proveedores de pago, etc.). Esta es la carpeta que debe fusionarse con el repositorio de archivos de producción para obtener el repositorio completo.

Nota

Puede solicitar múltiples bases de datos de prueba si desea probar una
actualización más de una vez.

Nota

Al completar una solicitud de actualización, el reporte de actualización se
adjunta al correo electrónico de actualización exitosa y además también está
disponible en la aplicación Conversaciones para los usuarios que forman parte
del grupo «Administración / Ajustes». Este reporte proporciona información
importante sobre los cambios introducidos por la nueva versión.

## Probar la nueva versión de la base de datos

Es muy importante que dedique tiempo a probar la base de datos de prueba
actualizada para asegurarse de no interrumpir sus actividades diarias debido a
un cambio en las vistas o en el comportamiento, incluso debido a un mensaje de
error una vez que la actualización esté activa.

Nota

Las bases de datos de prueba están neutralizadas y algunas de sus funciones
están deshabilitadas para evitar que afecten la base de datos de producción:

  1. Las actividades programadas están deshabilitadas.

  2. Los servidores de correo saliente se deshabilitan. Para esto, los que ya existen se archivan y además se agrega uno falso.

  3. Los proveedores de pago y los transportistas se restablecen a un entorno de prueba.

  4. La sincronización bancaria se deshabilita. En caso de que desee probarla, póngase en contacto con su proveedor de sincronización bancaria para que le proporcione las credenciales del entorno de prueba.

Le recomendamos probar tantos flujos empresariales como le sea posible para
asegurarse de que funcionen de forma correcta y para que se familiarice más
con la nueva versión.

Lista de verificación de prueba básica

  * ¿Hay vistas que están desactivadas en su base de datos de prueba pero activas en su base de datos de producción?

  * ¿Sus vistas habituales se muestran de forma correcta?

  * ¿Sus reportes (facturas, órdenes de ventas, etcétera) se están generando de manera correcta?

  * ¿Las páginas de su sitio web están funcionando de forma adecuada?

  * ¿Puede crear y modificar registros? (como órdenes de ventas, facturas, compras, usuarios, contactos, empresas, etcétera).

  * ¿Las plantillas de correo electrónico presentan errores?

  * ¿Las traducciones almacenadas tienen errores?

  * ¿Sus filtros de búsqueda están disponibles?

  * ¿Puede exportar sus datos?

Example of end-to-end testing

  * Verificar un producto aleatorio de su catálogo de productos y comparar sus datos de prueba y producción para comprobar que todo es igual (categoría del producto, precio de venta, precio de costo, proveedor, cuentas, rutas, etcétera).

  * Comprar el producto (aplicación Compra).

  * Confirmar su recepción (aplicación Inventario).

  * Verificar si la ruta para recibir el producto es la misma que estableció en la base de datos de producción (aplicación Inventario).

  * Vender el producto (aplicación Ventas) a un cliente aleatorio.

  * Abrir la base de datos con sus clientes (aplicación Contactos), seleccionar un cliente (o empresa) y verificar su información.

  * Enviar el producto (aplicación Compra).

  * Verificar si la ruta para enviar el producto es la misma que estableció en la base de datos de producción (aplicación Inventario).

  * Validar la factura del cliente (aplicación Facturación o Contabilidad).

  * Acreditar una factura (emitir una nota de crédito) y verificar si se comporta de la misma manera que en la base de datos de producción.

  * Verificar el reporte de resultados (aplicación Contabilidad).

  * Revisar de forma aleatoria sus impuestos, divisas, cuentas bancarias y año fiscal (aplicación Contabilidad).

  * Realizar todas las etapas de una orden en línea (aplicación Sitio web), desde la selección de productos en su tienda hasta el proceso de pago. Verificar si todo se comporta de la misma manera que en la base de datos de producción.

Esta lista **no** está completa. El ejemplo puede extenderse a otras de sus
aplicaciones según el uso que le da a Odoo.

Puede solicitar la ayuda de Odoo si ocurre algún problema durante las pruebas
de su base de datos de prueba actualizada, [envíe un ticket con la opción Duda
relacionada con mi actualización (en fase de
pruebas)](https://odoo.com/help?stage=migration). En cualquier caso, es muy
importante que nos haga saber cualquier problema que haya tenido durante las
pruebas para corregirlo antes de actualizar su base de datos de producción.

Es posible que haya algunas diferencias significativas en las vistas estándar,
funciones, campos y modelos al momento de realizar las pruebas. No es posible
revertir cada cambio de forma individual, sin embargo, si uno de los cambios
introducido por una nueva versión hace que una personalización tenga errores,
es responsabilidad de la persona que le da mantenimiento a su módulo
personalizado que sea compatible con la nueva versión de Odoo.

Truco

No olvide probar lo siguiente:

  * Integraciones con software externo (EDI, API, etcétera).

  * Flujos de trabajo compartidos entre varias aplicaciones (vender en línea con Comercio electrónico, convertir un lead en una orden de venta, entregar productos, etcétera).

  * Exportación de datos.

  * Acciones automatizadas.

  * Acciones del servidor en el menú de acción desde las vistas de formulario, así como al seleccionar varios registros en las vistas de lista.

## Actualizar la base de datos de producción

Una vez que terminó de realizar las pruebas y está seguro de que puede
utilizar la base de datos actualizada como su base de datos principal sin
ningún problema, es momento de planificar las acciones que llevará a cabo el
día de la activación. Puede planificarlas en colaboración con los analistas de
soporte de actualización de Odoo, [envía un ticket con la opción Duda
relacionada con mi actualización (fase de
pruebas)](https://odoo.com/help?stage=migration).

Su base de datos de producción no estará disponible mientras se actualiza. Le
recomendamos que realice la actualización en un momento en que el uso de la
base de datos es mínimo.

Como los scripts de actualización estándar y su base de datos evolucionan de
forma constante, también le recomendamos que con frecuencia solicite otra base
de datos de prueba actualizada, con la finalidad de asegurarse de que el
proceso de actualización se realiza con éxito, sobre todo si su finalización
toma mucho tiempo. **Además, le recomendamos ensayar todo el proceso de
actualización un día antes de actualizar la base de datos de producción.**

Importante

Empezar a usar la producción sin hacer pruebas primero puede ocasionar:

  * Que los usuarios no se ajusten a los cambios y nuevas funciones.

  * Que haya interrupciones en las actividades empresariales (por ejemplo, ya no contar con la posibilidad de validar una acción).

  * Que los clientes tengan una mala experiencia de usuario (por ejemplo, si un sitio web de comercio electrónico deja de funcionar de manera adecuada).

El proceso de actualización de una base de datos de producción es parecido a
la actualización de una base de datos de prueba salvo algunas excepciones.

Odoo OnlineOdoo.shOn-premise

El proceso es similar al que se lleva a cabo para obtener una base de datos de
pruebas actualizada, a excepción de la opción relacionada al propósito, debe
seleccionar Producción en lugar de Prueba.

Advertencia

Después de solicitar la actualización, la base de datos no estará disponible
hasta que termine la actualización. Una vez que el proceso haya finalizado, es
imposible volver a la versión anterior.

El proceso es similar al que se lleva a cabo para obtener una base de datos de
pruebas actualizada en la rama de Producción.

![Vista desde la pestaña de actualizar ](../_images/odoo-sh-prod.png)

El proceso **se activa al momento en que hace un nuevo commit** en la rama.
Esto permite que el proceso de actualización se sincronice con la
implementación del código fuente actualizado de los módulos personalizados. Si
no hay módulos personalizados, el proceso de actualización se activa de
inmediato.

Importante

La base de datos no está disponible durante todo el proceso. Si ocurre algún
error, la plataforma revierte la actualización de forma automática, como si se
tratara de una actualización regular. En caso de que el proceso sea exitoso,
se crea una copia de seguridad de la base de datos antes de la actualización.

La actualización de sus módulos personalizados debe ser exitosa antes de
completar todo el proceso de actualización. Asegúrese de que su actualización
de prueba sea éxitosa antes de intentarlo en producción. Para obtener más
información sobre cómo actualizar sus módulos personalizados consulte [Upgrade
a customized database](../developer/howtos/upgrade_custom_db.html).

El comando para actualizar una base de datos a producción es parecido al
comando para actualizar una base de prueba, solo debe reemplazar el argumento
`test` por `production`:

    
    
    $ python <(curl -s https://upgrade.odoo.com/upgrade) production -d <your db name> -t <target version>
    

En la [página del servicio de actualización](https://upgrade.odoo.com/)
también puede solicitar una base de datos de producción actualizada. Una vez
que haya cargado la base de datos, cualquier modificación que haga en su base
de datos de producción **no** estará presente en la base de datos actualizada.
Por este motivo le recomendamos que no la use durante el proceso de
actualización.

Importante

Al solicitar una base de datos actualizada para fines de producción, la copia
se envía sin los archivos almacenados. Por lo tanto, los archivos almacenados
de la base de datos actualizada deben fusionarse con los que corresponden a
producción antes de implementar la nueva versión.

Puede solicitar la ayuda de Odoo en caso de que haya un problema con su base
de datos de producción. Envíe un ticket con la opción [Duda relacionada con mi
actualización (producción)](https://odoo.com/help?stage=post_upgrade).

## Acuerdo de nivel de servicio (SLA, por sus siglas en inglés)

Con Odoo Enterprise, actualizar la base de datos a la versión más reciente es
**gratis** e incluye cualquier tipo de soporte requerido para rectificar
posibles discrepancias en la base de datos actualizada.

Tiene disponible información acerca de los servicios de actualización que
incluye la Licencia Enterprise en el [Acuerdo de Suscripción de Odoo
Enterprise](../legal/terms/enterprise.html#upgrade). Sin embargo, esta sección
aclara qué servicios de actualización puede esperar.

### Servicios de actualización que cubre el SLA

Las bases de datos alojadas en las plataformas en la nube de Odoo (Odoo en
línea y Odoo.sh) o que se alojan a si mismas (Local) se pueden beneficiar de
los servicios de actualización en todo momento para:

  * actualizar todas las **aplicaciones estándar** ;

  * actualizar todas las **personalizaciones creadas con la aplicación Studio** , siempre y cuando Studio siga instalado y la suscripción correspondiente siga activa; y

  * actualizar todos los **desarrollos y personalizaciones que cubre una suscripción de mantenimiento para las personalizaciones**.

Los servicios de actualización se limitan a una conversión técnica y la
adaptación de una base de datos (módulos estándar y datos) para hacerlos
compatibles con la versión objetivo de la actualización.

### Servicios de actualización que no cubre el SLA

Los siguientes servicios relacionados con la actualización **no** incluyen:

  * la **limpieza** de datos y configuraciones pre-existentes al momento de actualizar;

  * la actualización de **módulos personalizados creados internamente o por externos** , incluyendo partners de Odoo;

  * líneas de **código agregadas a módulos estándar** , por ejemplo, personalizaciones creadas fuera de la aplicación Studio, código introducido manualmente, y [acciones automatizadas usando código Python](../applications/studio/automated_actions.html#studio-automated-actions-action); y

  * **capacitación** para usar las funciones de la versión actualizada y flujos de trabajo.

Ver también

  * [Documentación de Odoo.sh](odoo_sh.html)

  * [Versiones compatibles de Odoo](supported_versions.html)

