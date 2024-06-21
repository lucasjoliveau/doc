# Actualizar

Una actualización es el proceso de trasladar su base de datos de una versión
anterior a una [versión compatible](supported_versions) más reciente (por
ejemplo, de Konvergo ERP 14.0 a Konvergo ERP 16.0). Es muy importante actualizar con
frecuencia, pues cada versión incluye funciones nuevas y mejoradas,
correcciones de errores y parches de seguridad.

<div class="accordion accordion-flush o_spoiler alert" id="upgrade-faq-rolling-release"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Automatic upgrades: Konvergo ERP Online's Rolling Release process</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>El proceso de lanzamiento continuo permite a los clientes de Konvergo ERP en línea actualizar su base de datos directamente desde el envío de un mensaje al administrador de la base de datos tan pronto como se publique una nueva versión. La invitación para actualizar solo se envía si no se detectan problemas durante las pruebas automáticas.</p>
<img alt="Verá el mensaje de actualización en la parte superior derecha de la base de datos." src="../_images/rr-upgrade-message.png"/>
<p>Se recomienda hacer <a href="#upgrade-test-your-db"><span class="std std-ref">pruebas antes de la actualización</span></a>. Si hace clic en <b>quiero probar primero</b>, se le redirigirá al <a href="https://www.odoo.com/my/databases/">administrador de bases de datos</a>, ahí podrá solicitar una base de datos de prueba actualizada y verificar que no haya ninguna discrepancia.</p>
<p><b>No</b> se recomienda hacer clic en <b>actualizar ahora</b> sin realizar pruebas primero, ya que esto activa inmediatamente la actualización de la base de datos de producción.</p>
<p>Si el proceso de lanzamiento continuo detecta un problema con la actualización, se desactivará hasta que se resuelva el problema.</p>
</div></div></div></div>

Una actualización no cubre:

>   * Cambiar a una versión anterior de Konvergo ERP
>
>   * [Cambiar de edición](on_premise/community_to_enterprise) (por
> ejemplo, de Community a Enterprise)
>
>   * [Cambiar el tipo de alojamiento](hosting#hosting-change-solution)
> (por ejemplo, de local a Konvergo ERP en línea)
>
>   * Migración de otro ERP a Konvergo ERP
>
>

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Si su base de datos contiene módulos personalizados, se podrá actualizar solo hasta que una versión de sus módulos personalizados que sea compatible con la versión de Konvergo ERP a la que se quiere actualizar esté disponible. Para clientes que quieran mantener sus módulos personalizados, recomendamos que el proceso se haga en paralelo, solo deben <a href="#upgrade-request-test-database"><span class="std std-ref">solicitar una actualización de base de datos</span></a> y al mismo tiempo <a href="../developer/howtos/upgrade_custom_db">actualizar el código de sus módulos personalizados</a>.</p>
</div>

## Resumen del proceso de actualización

  1. Solicite una base de datos de prueba actualizada (consulte la obtención de una base de datos de prueba actualizada).

  2. Si aplica, actualice el código fuente de su módulo personalizado para que sea compatible con la nueva versión de Konvergo ERP (consulte [Upgrade a customized database](../developer/howtos/upgrade_custom_db)).

  3. Pruebe exhaustivamente la base de datos actualizada (consulte prueba de la nueva versión de la base de datos).

  4. Reporte cualquier problema que ocurra durante las pruebas a Konvergo ERP. Envíe un ticket con la opción [Duda relacionada con mi actualización (en fase de pruebas)](https://odoo.com/help?stage=migration).

  5. Una vez que se resuelvan todos los problemas y esté seguro de que la base de datos actualizada se puede utilizar como su base de datos principal, planifique la actualización de su base de datos de producción.

  6. Solicite la actualización de la base de datos de producción, no permita que esté en uso durante el tiempo que tome completar el proceso (consulte la actualización de la base de datos de producción).

  7. Reporte cualquier problema que ocurra durante la actualización a Konvergo ERP. Envíe un ticket con la opción [Duda relacionada con mi actualización (producción)](https://odoo.com/help?stage=post_upgrade).

## Obtener una base de datos de prueba actualizada

La [página de actualización](https://upgrade.odoo.com/) es la plataforma
principal para solicitar una base de datos actualizada. Sin embargo, según el
tipo de alojamiento, puede actualizar desde la línea de comandos (local), el
administrador de bases de datos en línea de Konvergo ERP
<<https://odoo.com/my/databases>>_, o su proyecto Konvergo ERP.sh
<<https://odoo.sh/project>>_.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>La plataforma de actualización sigue la misma <a href="https://www.odoo.com/privacy">política de privacidad</a> que los demás servicios de Konvergo ERP.com. Visite el <a href="https://www.odoo.com/gdpr">reglamento general de protección de datos</a> para obtener más información sobre cómo Konvergo ERP maneja sus datos y privacidad.</p>
</div>

Konvergo ERP OnlineKonvergo ERP.shOn-premise

Las bases de datos de Konvergo ERP en línea se pueden actualizar de forma manual a
través del [administrador de bases de datos](https://odoo.com/my/databases).

El administrador de la base de datos muestra todas las bases de datos
vinculadas a la cuenta del usuario. Las bases de datos que no están en la
versión más reciente de Konvergo ERP muestran un ícono de una flecha en un círculo
junto a su nombre, indicando que se pueden actualizar.

![El administrador de la base de datos con un botón de actualización junto al
nombre de la base de datos.](../_images/databases-page.png)

Haga clic en el icono de la **flecha en un círculo** para iniciar el proceso
de actualización. En la ventana emergente, complete la siguiente información:

  * La **versión** de Konvergo ERP a la que desea actualizar, generalmente es la última versión.

  * El **correo electrónico** que debe recibir el enlace a la base de datos actualizada

  * El **propósito** de la actualización, se establece como prueba de forma automática en su primera solicitud de actualización.

![La ventana emergente "Actualizar base de datos".](../_images/upgrade-
popup.png)

La etiqueta **actualización en progreso** se muestra junto al nombre de la
base de datos hasta que se complete. Una vez que se termine el proceso, se
enviará un correo electrónico con un enlace a la base de datos de prueba
actualizada a la dirección proporcionada. También podrá acceder a la base de
datos desde el administrador de la base de datos, solo debe hacer clic en la
flecha desplegable antes del nombre de la base de datos.

![Hacer clic en la flecha del menú mostrará la base de datos de prueba
actualizada.](../_images/access-upgraded-db.png)

Konvergo ERP.sh está integrado con la plataforma de actualización para hacer el
proceso de actualización más sencillo.

![Proyecto y pestañas de Konvergo ERP.sh ](../_images/odoo-sh-staging.png)

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

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Si se trata de bases de datos con módulos personalizados es necesario actualizar el código fuente con la versión objetivo de Konvergo ERP antes de que se pueda realizar la actualización. Si no hay ninguno, se omitirá el modo «actualizar al confirmar», se construirá la base de datos actualizada tan pronto como se transfiera desde la plataforma de actualización y se saldrá del modo de actualización.</p>
<p>Consulte la página <a href="../developer/howtos/upgrade_custom_db">Upgrade a customized database</a> para obtener más información.</p>
</div>

Puede iniciar el proceso de actualización estándar al escribir el siguiente
comando en la línea de comandos de la máquina donde se encuentra alojada la
base de datos.

    
    
    $ python <(curl -s https://upgrade.odoo.com/upgrade) test -d <your db name> -t <target version>
    

Puede utilizar el siguiente comando para mostrar la ayuda general y los
comandos principales.

    
    
    $ python <(curl -s https://upgrade.odoo.com/upgrade) --help
    

También puede solicitar una base de datos de prueba actualizada desde la
[página de actualización](https://upgrade.odoo.com/).

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>En las bases de datos que tienen módulos personalizados instalados, el código fuente de estos módulos debe estar actualizado para la nueva versión de Konvergo ERP antes de que se realice la actualización. Consulte <a href="../developer/howtos/upgrade_custom_db">Upgrade a customized database</a> para obtener más dtalles.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Por razones de seguridad, solo la persona que envío la solicitud de actualización puede descargarla.</p></li>
<li><p>Por motivos de almacenaje, debe subir la copia de su base de datos sin un repositorio de archivos al servidor de actualización. Por lo tanto, la base de datos actualizada no contiene el repositorio de archivos de producción.</p></li>
<li><p>Antes de restaurar la base de datos actualizada, su repositorio de archivos debe estar unido a al repositorio de archivos de producción para que pueda realizar las pruebas bajo las mismas condiciones que la nueva versión.</p></li>
<li><p>La base de datos actualizada contiene:</p>
<ul>
<li><p>Un archivo <code>dump.sql</code> que contiene la base de datos actualizada.</p></li>
<li><p>Una carpeta de <code>repositorio de archivos</code> que contiene los archivos que se extrajeron de los registros internos de la base de datos en archivos adjuntos (si es que hay) y nuevos archivos estándar de Konvergo ERP de la versión objetivo de Konvergo ERP (imágenes nuevas, iconos, logos de los proveedores de pago, etc.). Esta es la carpeta que debe fusionarse con el repositorio de archivos de producción para obtener el repositorio completo.</p></li>
</ul>
</li>
</ul>
</div>

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Puede solicitar múltiples bases de datos de prueba si desea probar una actualización más de una vez.</p>
</div> <div class="alert alert-primary" id="upgrade-upgrade-report">
<p class="alert-title">
Nota</p><p>Al completar una solicitud de actualización, el reporte de actualización se adjunta al correo electrónico de actualización exitosa y además también está disponible en la aplicación Conversaciones para los usuarios que forman parte del grupo «Administración / Ajustes». Este reporte proporciona información importante sobre los cambios introducidos por la nueva versión.</p>
</div>

## Probar la nueva versión de la base de datos

Es muy importante que dedique tiempo a probar la base de datos de prueba
actualizada para asegurarse de no interrumpir sus actividades diarias debido a
un cambio en las vistas o en el comportamiento, incluso debido a un mensaje de
error una vez que la actualización esté activa.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Las bases de datos de prueba están neutralizadas y algunas de sus funciones están deshabilitadas para evitar que afecten la base de datos de producción:</p>
<ol class="arabic simple">
<li><p>Las actividades programadas están deshabilitadas.</p></li>
<li><p>Los servidores de correo saliente se deshabilitan. Para esto, los que ya existen se archivan y además se agrega uno falso.</p></li>
<li><p>Los proveedores de pago y los transportistas se restablecen a un entorno de prueba.</p></li>
<li><p>La sincronización bancaria se deshabilita. En caso de que desee probarla, póngase en contacto con su proveedor de sincronización bancaria para que le proporcione las credenciales del entorno de prueba.</p></li>
</ol>
</div>

Le recomendamos probar tantos flujos empresariales como le sea posible para
asegurarse de que funcionen de forma correcta y para que se familiarice más
con la nueva versión.

<div class="admonition-basic-test-checklist alert">
<p class="alert-title">
Lista de verificación de prueba básica</p><ul>
<li><p>¿Hay vistas que están desactivadas en su base de datos de prueba pero activas en su base de datos de producción?</p></li>
<li><p>¿Sus vistas habituales se muestran de forma correcta?</p></li>
<li><p>¿Sus reportes (facturas, órdenes de ventas, etcétera) se están generando de manera correcta?</p></li>
<li><p>¿Las páginas de su sitio web están funcionando de forma adecuada?</p></li>
<li><p>¿Puede crear y modificar registros? (como órdenes de ventas, facturas, compras, usuarios, contactos, empresas, etcétera).</p></li>
<li><p>¿Las plantillas de correo electrónico presentan errores?</p></li>
<li><p>¿Las traducciones almacenadas tienen errores?</p></li>
<li><p>¿Sus filtros de búsqueda están disponibles?</p></li>
<li><p>¿Puede exportar sus datos?</p></li>
</ul>
</div> <div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Si su base de datos contiene módulos personalizados, se podrá actualizar solo hasta que una versión de sus módulos personalizados que sea compatible con la versión de Konvergo ERP a la que se quiere actualizar esté disponible. Para clientes que quieran mantener sus módulos personalizados, recomendamos que el proceso se haga en paralelo, solo deben <a href="#upgrade-request-test-database"><span class="std std-ref">solicitar una actualización de base de datos</span></a> y al mismo tiempo <a href="../developer/howtos/upgrade_custom_db">actualizar el código de sus módulos personalizados</a>.</p>
</div>0

Puede solicitar la ayuda de Konvergo ERP si ocurre algún problema durante las pruebas
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
personalizado que sea compatible con la nueva versión de Konvergo ERP.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Si su base de datos contiene módulos personalizados, se podrá actualizar solo hasta que una versión de sus módulos personalizados que sea compatible con la versión de Konvergo ERP a la que se quiere actualizar esté disponible. Para clientes que quieran mantener sus módulos personalizados, recomendamos que el proceso se haga en paralelo, solo deben <a href="#upgrade-request-test-database"><span class="std std-ref">solicitar una actualización de base de datos</span></a> y al mismo tiempo <a href="../developer/howtos/upgrade_custom_db">actualizar el código de sus módulos personalizados</a>.</p>
</div>1

## Actualizar la base de datos de producción

Una vez que terminó de realizar las pruebas y está seguro de que puede
utilizar la base de datos actualizada como su base de datos principal sin
ningún problema, es momento de planificar las acciones que llevará a cabo el
día de la activación. Puede planificarlas en colaboración con los analistas de
soporte de actualización de Konvergo ERP, [envía un ticket con la opción Duda
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

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Si su base de datos contiene módulos personalizados, se podrá actualizar solo hasta que una versión de sus módulos personalizados que sea compatible con la versión de Konvergo ERP a la que se quiere actualizar esté disponible. Para clientes que quieran mantener sus módulos personalizados, recomendamos que el proceso se haga en paralelo, solo deben <a href="#upgrade-request-test-database"><span class="std std-ref">solicitar una actualización de base de datos</span></a> y al mismo tiempo <a href="../developer/howtos/upgrade_custom_db">actualizar el código de sus módulos personalizados</a>.</p>
</div>2

El proceso de actualización de una base de datos de producción es parecido a
la actualización de una base de datos de prueba salvo algunas excepciones.

Konvergo ERP OnlineKonvergo ERP.shOn-premise

El proceso es similar al que se lleva a cabo para obtener una base de datos de
pruebas actualizada, a excepción de la opción relacionada al propósito, debe
seleccionar **Producción** en lugar de **Prueba**.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Si su base de datos contiene módulos personalizados, se podrá actualizar solo hasta que una versión de sus módulos personalizados que sea compatible con la versión de Konvergo ERP a la que se quiere actualizar esté disponible. Para clientes que quieran mantener sus módulos personalizados, recomendamos que el proceso se haga en paralelo, solo deben <a href="#upgrade-request-test-database"><span class="std std-ref">solicitar una actualización de base de datos</span></a> y al mismo tiempo <a href="../developer/howtos/upgrade_custom_db">actualizar el código de sus módulos personalizados</a>.</p>
</div>3

El proceso es similar al que se lleva a cabo para obtener una base de datos de
pruebas actualizada en la rama de **Producción**.

![Vista desde la pestaña de actualizar ](../_images/odoo-sh-prod.png)

El proceso **se activa al momento en que hace un nuevo commit** en la rama.
Esto permite que el proceso de actualización se sincronice con la
implementación del código fuente actualizado de los módulos personalizados. Si
no hay módulos personalizados, el proceso de actualización se activa de
inmediato.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Si su base de datos contiene módulos personalizados, se podrá actualizar solo hasta que una versión de sus módulos personalizados que sea compatible con la versión de Konvergo ERP a la que se quiere actualizar esté disponible. Para clientes que quieran mantener sus módulos personalizados, recomendamos que el proceso se haga en paralelo, solo deben <a href="#upgrade-request-test-database"><span class="std std-ref">solicitar una actualización de base de datos</span></a> y al mismo tiempo <a href="../developer/howtos/upgrade_custom_db">actualizar el código de sus módulos personalizados</a>.</p>
</div>4

La actualización de sus módulos personalizados debe ser exitosa antes de
completar todo el proceso de actualización. Asegúrese de que su actualización
de prueba sea **éxitosa** antes de intentarlo en producción. Para obtener más
información sobre cómo actualizar sus módulos personalizados consulte [Upgrade
a customized database](../developer/howtos/upgrade_custom_db).

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

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Si su base de datos contiene módulos personalizados, se podrá actualizar solo hasta que una versión de sus módulos personalizados que sea compatible con la versión de Konvergo ERP a la que se quiere actualizar esté disponible. Para clientes que quieran mantener sus módulos personalizados, recomendamos que el proceso se haga en paralelo, solo deben <a href="#upgrade-request-test-database"><span class="std std-ref">solicitar una actualización de base de datos</span></a> y al mismo tiempo <a href="../developer/howtos/upgrade_custom_db">actualizar el código de sus módulos personalizados</a>.</p>
</div>5

Puede solicitar la ayuda de Konvergo ERP en caso de que haya un problema con su base
de datos de producción. Envíe un ticket con la opción [Duda relacionada con mi
actualización (producción)](https://odoo.com/help?stage=post_upgrade).

## Acuerdo de nivel de servicio (SLA, por sus siglas en inglés)

Con Konvergo ERP Enterprise, actualizar la base de datos a la versión más reciente es
**gratis** e incluye cualquier tipo de soporte requerido para rectificar
posibles discrepancias en la base de datos actualizada.

Tiene disponible información acerca de los servicios de actualización que
incluye la Licencia Enterprise en el [Acuerdo de Suscripción de Konvergo ERP
Enterprise](../legal/terms/enterprise#upgrade). Sin embargo, esta sección
aclara qué servicios de actualización puede esperar.

### Servicios de actualización que cubre el SLA

Las bases de datos alojadas en las plataformas en la nube de Konvergo ERP (Konvergo ERP en
línea y Konvergo ERP.sh) o que se alojan a si mismas (Local) se pueden beneficiar de
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

  * la actualización de **módulos personalizados creados internamente o por externos** , incluyendo partners de Konvergo ERP;

  * líneas de **código agregadas a módulos estándar** , por ejemplo, personalizaciones creadas fuera de la aplicación Studio, código introducido manualmente, y [acciones automatizadas usando código Python](../applications/studio/automated_actions#studio-automated-actions-action); y

  * **capacitación** para usar las funciones de la versión actualizada y flujos de trabajo.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Si su base de datos contiene módulos personalizados, se podrá actualizar solo hasta que una versión de sus módulos personalizados que sea compatible con la versión de Konvergo ERP a la que se quiere actualizar esté disponible. Para clientes que quieran mantener sus módulos personalizados, recomendamos que el proceso se haga en paralelo, solo deben <a href="#upgrade-request-test-database"><span class="std std-ref">solicitar una actualización de base de datos</span></a> y al mismo tiempo <a href="../developer/howtos/upgrade_custom_db">actualizar el código de sus módulos personalizados</a>.</p>
</div>6

