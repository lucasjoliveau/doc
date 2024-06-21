# Vincular anuncios existentes

Una vez que haya vinculado la cuenta de eBay, debe agregar los anuncios
existentes dentro de la cuenta de vendedor de eBay de forma manual a las
listas de productos de Konvergo ERP.

El proceso que debe seguir es el siguiente: primero desactive las acciones
programadas de eBay, luego agregue los productos y vincule los anuncios, por
último, active las acciones programadas de eBay.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p>Para obtener más información relacionada al Conector de eBay puede visitar las siguientes páginas:</p>
<ul>
<li><p><a href="setup">Configuración del Conector de eBay</a></p></li>
<li><p><a href="manage">¿Cómo anunciar un producto?</a></p></li>
<li><p><a href="troubleshooting">Solución de problemas del Conector de eBay</a></p></li>
</ul>
</div>

## Desactivar las acciones programadas de eBay

Para comenzar a vincular los anuncios existentes en eBay primero debe
desactivar las notificaciones de eBay en las acciones programadas de Konvergo ERP. El
motivo detrás de esto es que no haya órdenes ni sincronizaciones de datos de
eBay durante este proceso. Puede acceder a las **acciones programadas** al
activar el [modo de
desarrollador](../../../general/developer_mode#developer-mode), después
vaya a Configuración ‣ Técnico ‣ Automatización ‣ Acciones programadas.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>El <a href="../../../general/developer_mode">Modo de desarrollador (modo de depuración)</a> debe estar activo para garantizar que el usuario pueda visualizar el menú técnico.</p>
</div>

Desactivar las acciones programadas permite que los usuarios sincronicen y
validen los datos de eBay antes de recibir órdenes. Estas son las acciones
programadas que debe desactivar temporalmente:

  * **eBay: obtener nuevas órdenes** : eBay envía las nuevas órdenes que aún no están en Konvergo ERP (según el campo **client_order_reference** o la **referencia de la orden de venta**). Este comando también actualiza las órdenes existentes cuando se realizan cambios en eBay. Las nuevas órdenes y las órdenes actualizadas se colocan en modo de borrador. Los clientes se crearán si aún no están en Konvergo ERP.

  * **eBay: sincronizar las existencias** : eBay muestra las existencias disponibles en Konvergo ERP.

  * **eBay: actualizar categorías** : eBay enviará actualizaciones mensuales de las categorías (solo hasta el cuarto nivel, una actualización manual es necesaria para los demás).

Para desactivar la notificación de eBay, seleccione la entrada de la lista de
**Acciones programadas**. Luego, en la página, haga clic en el botón de
alternancia **Activo** para desactivarlo.

### Sincronizar categorías de eBay

Para asegurarse de que los productos de Konvergo ERP para eBay tengan todas las
categorías disponibles en eBay, el siguiente paso es sincronizar las
categorías de eBay con Konvergo ERP.

Vaya a Ajustes ‣ Técnico ‣ Automatización ‣ Acciones programadas. Haga clic en
la acción programada con el nombre **eBay: actualizar categorías** y luego en
**Ejecutar de forma manual**.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Konvergo ERP solo reconoce las rutas de categorías de eBay hasta el cuarto nivel de profundidad. Si un producto tiene una lista de más de cuatro, el campo de categoría solo se llenará hasta ese nivel.</p>
<p>Si es necesario tener categorías de productos con más de cuatro rutas, entonces los usuarios deben agregarlas manualmente. Estas se pueden importar de forma manual en el modelo de Categoría de producto en Konvergo ERP y luego se deben vincular individualmente al producto.</p>
</div>

Los usuarios pueden importar las categorías de productos restantes de forma
manual en las categorías de productos de eBay con el menú **Acción** y la
función **Importar**.

## Vincular anuncios de eBay

Para agregar anuncios de eBay en Konvergo ERP podrá hacerlo de forma manual con el ID
del anuncio, también puede establecer un enlace automático para anuncios entre
Konvergo ERP y eBay.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para obtener más información sobre cómo anunciar un producto consulte <a href="manage#ebay-connector-listing"><span class="std std-ref">la documentación relacionada</span></a>.</p>
</div>

### Enlace manual de anuncios

Para agregar un anuncio de eBay a los productos en Konvergo ERP, primero vaya a la
aplicación Ventas ‣ Productos ‣ Productos y seleccione el producto
correspondiente. Haga clic en **Vender en eBay** (ya sea en la pestaña
**eBay** o en el **nombre del producto**) y luego presione **Guardar** si es
necesario.

Mientras aún está en el formulario del producto haga clic en **Enlazar a
anuncio** en el menú superior y escriba el ID del anuncio de eBay en la
ventana emergente (el ID del anuncio se encuentra en la URL del producto en
eBay).

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Como ejemplo, en la URL <code>www.ebay.com/itm/272222656444?hash=item3f61bc17bb:g:vJ0AAOSwslJizv8u</code>, el ID del producto es <code>272222656444</code>. Una vez que haya ingresado el ID del anuncio de eBay, su información se sincronizará en Konvergo ERP.</p>
</div>

## Habilitar las acciones programadas de eBay

El siguiente paso es activar las notificaciones de eBay en las acciones
programadas en Konvergo ERP para que se intercambien las órdenes y los datos. Puede
acceder a las **acciones programadas** una vez que active el [modo de
desarrollador](../../../general/developer_mode#developer-mode) y luego
vaya a Ajustes ‣ Técnico ‣ Automatización ‣ Acciones programadas.

Activar las siguientes acciones programadas permitirá que los usuarios
sincronicen y validen los datos de eBay en automático.

  * **eBay: obtener nuevas órdenes** : eBay enviará todas las órdenes nuevas que aún no estén en Konvergo ERP (según el campo client_order_reference o la referencia de la orden de venta) y actualizará las órdenes si ha habido algún cambio en eBay. Las órdenes se colocarán en modo de borrador y se crearán los clientes si aún no están en Konvergo ERP.

  * **eBay: sincronizar las existencias** : eBay mostrará las existencias disponibles en Konvergo ERP.

  * **eBay: actualizar categorías** : eBay enviará actualizaciones mensuales de las categorías (solo hasta el cuarto nivel, es necesaria una actualización manual para los demás).

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si recibe una orden y el anuncio de la orden no está vinculado a un producto, eBay creará un producto consumible en su lugar. Deberá modificar estos productos consumibles en la <em>orden de venta</em> mientras estén en estado de borrador para representar un producto almacenable y luego el usuario podrá vincularlos al anuncio a medida que van llegando.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="manage">¿Cómo anunciar un producto?</a></p></li>
<li><p><a href="troubleshooting">Solución de problemas del Conector de eBay</a></p></li>
<li><p><a href="setup">Configuración del Conector de eBay</a></p></li>
</ul>
</div>

