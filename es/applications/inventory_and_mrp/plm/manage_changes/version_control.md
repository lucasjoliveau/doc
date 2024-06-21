# Control de versiones

Use la _Gestión del ciclo de vida del producto (PLM)_ de Konvergo ERP para gestionar
versiones anteriores de las LdM. Guarde instrucciones de ensamblaje antiguas,
detalles de los componentes y archivos pasados de diseño de los productos, al
mismo tiempo que mantiene fuera detalles anteriores de la LdM de producción.

Tenga a la mano versiones previas de la LdM para cuando sean necesarias.
Además, use el _PLM_ para rastrear que versión de la LdM estuvo activa en
fechas específicas para quitarlas del mercado o atender quejas de los
clientes.

Cada versión de la LdM se guarda en una _orden para cambio de ingeniería_ para
tener organizadas las pruebas y las mejoras sin interrumpir las operaciones
normales de fabricación.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="engineering_change_orders#plm-eco"><span class="std std-ref">Orden para cambio de ingeniería</span></a></p>
</div>

## Versión actual de la LdM

Para ver la versión actual de la LdM que se está utilizando en producción,
vaya a la Aplicación PLM ‣ Datos maestros ‣ Lista de materiales y seleccione
la LdM que desee de la lista. Luego, abra la pestaña **Varios** donde aparece
la **Versión** actual de la LdM.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>También puede acceder a las LdM desde la Aplicación Fabricación ‣ Productos ‣ Lista de materiales.</p>
</div> ![Vea la versión actual de la LdM en la pestaña
Varios.](../../../../_images/current-version.png)

## Historial de la versión

Para gestionar todas las versiones antiguas, actuales y futuras de una LdM,
primero vaya a la Aplicación Fabricación ‣ Productos ‣ Lista de Materiales y
haga clic en la LdM que desee.

Desde la página de la LdM, haga clic en el botón inteligente de orden para
cambio de ingeniería y cambie la vista al modo lista seleccionando el icono
**≣ (cuatro líneas horizontales)** ubicado en le esquina superior derecha.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El botón inteligente de la orden para cabio de ingeniería es visible en la LdM <b>solo</b> si está instalada la aplicación <em>PLM</em>.</p>
</div> ![Botón inteligente de orden para cambio de ingeniería en
una LdM.](../../../../_images/eco-smart-button.png)

En la lista de órdenes para cambio de ingeniería para el producto, vaya a la
barra de navegación ubicada en la parte superior y haga clic en el icono **▼
(flecha apuntando hacia abajo)** ubicado a la derecha para acceder al menú
desplegable de **Filtros**.

Luego, filtre por órdenes para cambio de ingeniería **Hechas** para ver: el
historial de la revisión de la LdM, el usuario **Responsable** que aplicó el
cambio y la **Fecha efectiva** de la LdM.

Haga clic en cada orden para cambio de ingeniería para ver los componentes
pasados y los archivos de diseño asociados con la LdM.

![Visualización del historial de revisión de la orden para cambio de
ingeniería para una LdM de un producto.](../../../../_images/eco-list.png)
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si el campo <b>Fecha efectiva</b> esta vacío, la fecha <b>Efectiva</b> de la orden para cambio de ingeniería se establece automáticamente a  <b>Tan pronto como sea posbile</b> y no se registran fechas en el historial de revisión de la LdM</p>
<img alt="Lista de fechas efectivas de una LdM." class="align-center" src="../../../../_images/no-effective-date.png"/>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Otra opción para revisar cuándo se empezó a utilizar la LdM es en el chatter y colocando el ratón sobre el tiempo en el que la orden para cambio de ingeniería se movió a <a href="eco_type#plm-eco-stage-config"><span class="std std-ref">etapa de cerrado</span></a>.</p>
</div>

## Archivos de diseño

Adjunte archivos de diseño asistido por computadora (CAD, por sus siglas en
inglés), PDF, imágenes u otro material de diseño a la LdM.

Para hacerlo, vaya a la Aplicación PLM ‣ Datos Maestros ‣ Lista de Materiales
y seleccione la LdM que desee. En dicha LdM vaya al _chatter_ y haga clic en
el icono de **📎 (clip)**.

Ahora aparecerán los archivos asociados con la LdM en la sección de
**Archivos**. Para agregar más archivos de diseño, haga clic en el botón
**Adjuntar archivos**.

![Icono de clip en el chatter para adjuntar archivos a una
LdM.](../../../../_images/attach-files.png)

### Gestione archivos de diseño en una orden para cambio de ingeniería

Agregue, modifique y elimine archivos de una orden para cambio de ingeniería.
Una vez confirmada y aplicada, los nuevos archivos estarán vinculados
automáticamente a la LdM de producción. Los archivos archivados se eliminarán
de la LdM pero todavía podrá acceder a ellos en la orden para cambio de
ingeniería.

Para gestionar los archivos de diseño en la orden para cambio de ingeniería,
vaya a la Aplicación PLM ‣ Cambios y seleccione la orden que desee. Luego,
abra la página de **Archivos adjuntos** haciendo clic en el botón inteligente
de **Documentos**.

Pase el cursor por encima de cada archivo adjunto para ver el icono **︙(tres
puntos verticales)**. Desde ahí, elija si quiere **Editar** , **Eliminar** o
**Descargar** el archivo. Cualquier cambio que le haga a estos archivos se
mantendrán dentro de la orden para cambio de ingeniería y se aplicarán a la
LdM de producción una vez:ref:`aplicados los cambios <plm/eco/apply-changes>`.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>En la orden para cambio de ingeniería <code>Fabricar 60% del teclado</code>, los archivos de diseño son de la LdM original <code>Teclado 100%</code>. Para reemplazar el PDF del teclado, haga clic en el botón inteligente <b>Documentos</b>.</p>
<img alt="Botón inteligente *Documentos* desde una orden para cambio de ingeniería activa. " class="align-center" src="../../../../_images/documents-smart-button.png"/>
<p>En la página de  <b>Archivos adjuntos</b>, pase el cursor sobre el archivo de diseño <code>Manual para teclado100%.pdf</code> y haga clic en el icono <b>︙ (trees puntos verticales)</b>. Luego, haga clic en la opción  <b>Eliminar</b> para archivar el archivo.</p>
<p>Luego, en la misma página de <b>Archivos adjuntos</b>, haga clic en el botón <b>Subir</b> para subir un nuevo archivo de diseño llamado <code>Manual para teclado 60%</code>.</p>
<img alt="Vista de la página *Archivos adjuntos desde el botón inteligente *Documentos*. Muestra un archivo archivado y uno recientemente añadido. " class="align-center" src="../../../../_images/attachments.png"/>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Los archivos archivados <b>no</b> se eliminan de forma permanente, aún puede acceder a ellos en la orden de cambio de ingeniería anterior o como un archivo archivado en la última <abbr title="Engineering Change Order">ECO</abbr> donde se realizó.</p>
</div>

## Aplicar transferencia de base

Konvergo ERP simplifica la resolución de conflictos de fusión para las órdenes de
cambio de ingeniería simultáneas en el mismo producto.

Pueden ocurrir conflictos cuando la LdM de producción se actualiza mientras
otras órdenes de cambio de ingeniería están modificando la versión anterior.
Las diferencias entre las listas de materiales nuevas y anteriores de
producción aparecen en la pestaña **Cambios de LdM de órdenes de cambio de
ingeniería anteriores** , visible solo bajo esta circunstancia.

Para resolver los conflictos y mantener los cambios de la ECO, haga clic en el
botón **Aplicar transferencia de base**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Se crean dos órdenes de cambio de ingeniería, <code>ECO0011</code> y <code>ECO0012</code>, mientras la versión actual de la lista de materiales es la número <code>5</code>. En la <code>ECO0011</code> se agregó un nuevo componente, <code>Estabilizador para la barra de espacio</code>, y luego se aplicaron los cambios. Esto quiere decir que la versión actual de la LdM ahora es la número <code>6</code>.</p>
<img alt="Aplicar cambios a una orden de cambio de ingeniería para actualizar la LdM de producción." class="align-center" src="../../../../_images/branch-change.png"/>
<p>Esto significa que la <code>ECO0012</code> está modificando una lista de materiales que no está actualizada. Como se muestra en la pestaña <b>Cambios de LdM de órdenes de cambio de ingeniería anteriores</b>, la <a href="#id1"><span class="problematic" id="id2">|LdM|</span></a> no incluye el <code>Estabilizador para la barra de espacio</code>.</p>
<p>Para garantizar que se mantengan los cambios aplicados con <code>ECO0011</code> cuando ocurran los cambios en la <code>ECO0012</code>, haga clic en el botón <b>Aplicar transferencia de base</b> para aplicar los cambios de la orden de cambio de ingeniería sin afectar los cambios que ya se habían hecho a la <code>ECO0012</code>.</p>
<img alt="Hacer clic en el botón *Aplicar transferencia de base* para actualizar la lista de materiales y que coincida con la de producción. " class="align-center" src="../../../../_images/merge-change.png"/>
</div>

  *[ECO]: Engineering Change Order

