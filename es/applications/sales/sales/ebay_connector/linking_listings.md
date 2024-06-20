# Vincular anuncios existentes

Una vez que haya vinculado la cuenta de eBay, debe agregar los anuncios
existentes dentro de la cuenta de vendedor de eBay de forma manual a las
listas de productos de Odoo.

El proceso que debe seguir es el siguiente: primero desactive las acciones
programadas de eBay, luego agregue los productos y vincule los anuncios, por
último, active las acciones programadas de eBay.

Ver también

Para obtener más información relacionada al Conector de eBay puede visitar las
siguientes páginas:

  * [Configuración del Conector de eBay](setup.html)

  * [¿Cómo anunciar un producto?](manage.html)

  * [Solución de problemas del Conector de eBay](troubleshooting.html)

## Desactivar las acciones programadas de eBay

Para comenzar a vincular los anuncios existentes en eBay primero debe
desactivar las notificaciones de eBay en las acciones programadas de Odoo. El
motivo detrás de esto es que no haya órdenes ni sincronizaciones de datos de
eBay durante este proceso. Puede acceder a las acciones programadas al activar
el [modo de desarrollador](../../../general/developer_mode.html#developer-
mode), después vaya a Configuración ‣ Técnico ‣ Automatización ‣ Acciones
programadas.

Advertencia

El [Modo de desarrollador (modo de
depuración)](../../../general/developer_mode.html) debe estar activo para
garantizar que el usuario pueda visualizar el menú técnico.

Desactivar las acciones programadas permite que los usuarios sincronicen y
validen los datos de eBay antes de recibir órdenes. Estas son las acciones
programadas que debe desactivar temporalmente:

  * eBay: obtener nuevas órdenes: eBay envía las nuevas órdenes que aún no están en Odoo (según el campo client_order_reference o la referencia de la orden de venta). Este comando también actualiza las órdenes existentes cuando se realizan cambios en eBay. Las nuevas órdenes y las órdenes actualizadas se colocan en modo de borrador. Los clientes se crearán si aún no están en Odoo.

  * eBay: sincronizar las existencias: eBay muestra las existencias disponibles en Odoo.

  * eBay: actualizar categorías: eBay enviará actualizaciones mensuales de las categorías (solo hasta el cuarto nivel, una actualización manual es necesaria para los demás).

Para desactivar la notificación de eBay, seleccione la entrada de la lista de
Acciones programadas. Luego, en la página, haga clic en el botón de
alternancia Activo para desactivarlo.

### Sincronizar categorías de eBay

Para asegurarse de que los productos de Odoo para eBay tengan todas las
categorías disponibles en eBay, el siguiente paso es sincronizar las
categorías de eBay con Odoo.

Vaya a Ajustes ‣ Técnico ‣ Automatización ‣ Acciones programadas. Haga clic en
la acción programada con el nombre eBay: actualizar categorías y luego en
Ejecutar de forma manual.

Importante

Odoo solo reconoce las rutas de categorías de eBay hasta el cuarto nivel de
profundidad. Si un producto tiene una lista de más de cuatro, el campo de
categoría solo se llenará hasta ese nivel.

Si es necesario tener categorías de productos con más de cuatro rutas,
entonces los usuarios deben agregarlas manualmente. Estas se pueden importar
de forma manual en el modelo de Categoría de producto en Odoo y luego se deben
vincular individualmente al producto.

Los usuarios pueden importar las categorías de productos restantes de forma
manual en las categorías de productos de eBay con el menú Acción y la función
Importar.

## Vincular anuncios de eBay

Para agregar anuncios de eBay en Odoo podrá hacerlo de forma manual con el ID
del anuncio, también puede establecer un enlace automático para anuncios entre
Odoo y eBay.

Truco

Para obtener más información sobre cómo anunciar un producto consulte [la
documentación relacionada](manage.html#ebay-connector-listing).

### Enlace manual de anuncios

Para agregar un anuncio de eBay a los productos en Odoo, primero vaya a la
aplicación Ventas ‣ Productos ‣ Productos y seleccione el producto
correspondiente. Haga clic en Vender en eBay (ya sea en la pestaña eBay o en
el nombre del producto) y luego presione Guardar si es necesario.

Mientras aún está en el formulario del producto haga clic en Enlazar a anuncio
en el menú superior y escriba el ID del anuncio de eBay en la ventana
emergente (el ID del anuncio se encuentra en la URL del producto en eBay).

Example

Como ejemplo, en la URL
`www.ebay.com/itm/272222656444?hash=item3f61bc17bb:g:vJ0AAOSwslJizv8u`, el ID
del producto es `272222656444`. Una vez que haya ingresado el ID del anuncio
de eBay, su información se sincronizará en Odoo.

## Habilitar las acciones programadas de eBay

El siguiente paso es activar las notificaciones de eBay en las acciones
programadas en Odoo para que se intercambien las órdenes y los datos. Puede
acceder a las acciones programadas una vez que active el [modo de
desarrollador](../../../general/developer_mode.html#developer-mode) y luego
vaya a Ajustes ‣ Técnico ‣ Automatización ‣ Acciones programadas.

Activar las siguientes acciones programadas permitirá que los usuarios
sincronicen y validen los datos de eBay en automático.

  * eBay: obtener nuevas órdenes: eBay enviará todas las órdenes nuevas que aún no estén en Odoo (según el campo client_order_reference o la referencia de la orden de venta) y actualizará las órdenes si ha habido algún cambio en eBay. Las órdenes se colocarán en modo de borrador y se crearán los clientes si aún no están en Odoo.

  * eBay: sincronizar las existencias: eBay mostrará las existencias disponibles en Odoo.

  * eBay: actualizar categorías: eBay enviará actualizaciones mensuales de las categorías (solo hasta el cuarto nivel, es necesaria una actualización manual para los demás).

Nota

Si recibe una orden y el anuncio de la orden no está vinculado a un producto,
eBay creará un producto consumible en su lugar. Deberá modificar estos
productos consumibles en la _orden de venta_ mientras estén en estado de
borrador para representar un producto almacenable y luego el usuario podrá
vincularlos al anuncio a medida que van llegando.

Ver también

  * [¿Cómo anunciar un producto?](manage.html)

  * [Solución de problemas del Conector de eBay](troubleshooting.html)

  * [Configuración del Conector de eBay](setup.html)

