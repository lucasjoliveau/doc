# Gestión de órdenes de Amazon

## Sincronización de órdenes

Las órdenes se obtienen en automático de Amazon y se sincronizan en Konvergo ERP en
intervalos regulares.

La sincronización está basada en el estado de Amazon: solo se obtienen las
órdenes cuyo estado ha cambiado desde la última sincronización en Amazon. Esto
incluye cambios tanto en Amazon como en Konvergo ERP.

Para las órdenes _FBA_ (gestionado por Amazon) solo se obtienen aquellas
_enviadas_ y _canceladas_.

Para las órdenes _FBM_ (gestionado por el vendedor), se hace lo mismo con las
órdenes _no enviadas_ y _canceladas_. Para cada orden sincronizada se crea una
orden de venta y un cliente en Konvergo ERP (si el cliente aún no está registrado en
la base de datos).

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Cuando se cancela una orden en Amazon y ya se había sincronizado en Konvergo ERP, entonces la orden de venta correspondiente se cancela de forma automática.</p>
</div>

## Forzar sincronización

Para forzar la sincronización de una orden cuyo estado **no** ha cambiado
desde la última sincronización, primero active el [modo de
desarrollador](../../../general/developer_mode#developer-mode). Esto
incluye cambios tanto en Amazon como en Konvergo ERP.

Vaya a la cuenta de Amazon en Konvergo ERP (aplicación Ventas ‣ Configuración ‣
Ajustes ‣ Conectores ‣ Sincronización con Amazon ‣ Cuentas de Amazon) y
modifique la fecha en Seguimiento de órdenes ‣ Última sincronización de
órdenes.

Asegúrese de elegir una fecha que ocurra antes del último cambio de estado de
la orden correspondiente para sincronizar y guarde, esto hará que la
sincronización se realice de forma adecuada.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para sincronizar de inmediato las órdenes de una cuenta de Amazon primero cambie al <a href="../../../general/developer_mode#developer-mode"><span class="std std-ref">modo de desarrollador</span></a>, después vaya a la cuenta de Amazon en Konvergo ERP y haga clic en <b>Sincronizar órdenes</b>. Puede hacer lo mismo con las recolecciones si hace clic en <b>Sincronizar recolecciones</b>.</p>
</div>

## Gestionar entregas en FBM

Al sincronizar una orden FBM (gestionado por el vendedor) en Konvergo ERP se crea una
recolección de forma instantánea en la aplicación _Inventario_ , además de una
orden de venta y un registro de cliente. Luego deberá decidir si enviar todos
los productos ordenados al cliente de una vez o enviarlos por partes con
órdenes parciales.

Al confirmar una recolección relacionada con la orden se envía una
notificación a Amazon, quien a su vez notifica al cliente que la orden (o
parte de ella) está en camino.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Amazon necesita que los usuarios proporcionen una referencia de seguimiento para cada entrega, esta es necesaria para asignar un transportista.</p>
<p>Si el transportista no proporciona una referencia de seguimiento de forma automática, entonces debe configurarse manualmente. Esta regla se aplica a todos los marketplaces de Amazon.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si el transportista que eligió no es compatible con Konvergo ERP puede crear uno con el mismo nombre (por ejemplo, puede crear un transportista llamado <code>easyship</code>). Este nombre no distingue entre mayúsculas y minúsculas, pero asegúrese de evitar errores tipográficos ya que en caso de que los haya, Amazon no los reconocerá. A continuación, cree un transportista con el nombre <code>Autoentrega</code> para informarle a Amazon que usted se encargará las entregas. Incluso con esta ruta <b>debe</b> ingresar una referencia de seguimiento. Recuerde que el cliente recibirá una notificación por correo electrónico sobre la entrega y el transportista junto con la referencia de seguimiento.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper">Transportistas externos</a></p>
</div>

## Seguimiento de entregas en FBA

Al sincronizar una orden FBA (gestionado por Amazon) en Konvergo ERP se registra un
movimiento de existencias en la aplicación _Inventario_ para cada artículo de
la orden de venta. De esta manera, queda almacenado en el sistema.

Los gerentes de inventario pueden acceder a estos movimientos desde la
aplicación Inventario ‣ Reportes ‣ Historial de movimientos.

Para las órdenes FBA, el movimiento de existencias se crea en Konvergo ERP en
automático a través del Conector de Amazon, gracias al estado de envío de
Amazon. Al enviar nuevos productos a Amazon, el usuario debe crear una
recolección (orden de entrega) de forma manual para trasladar estos productos
desde su almacén a la ubicación de Amazon.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para llevar seguimiento de las existencias de <em>Amazon (FBA)</em> en Konvergo ERP debe realizar un ajuste de inventario después de reabastecerlas. También puede activar un reabastecimiento automático desde las reglas de reordenamiento en la ubicación de Amazon.</p>
</div>

Puede configurar la ubicación de Amazon si accede a la cuenta de Amazon
gestionada en Konvergo ERP. Para acceder a las cuentas de Amazon en Konvergo ERP, vaya a la
aplicación Ventas ‣ Configuración ‣ Ajustes ‣ Conectores ‣ Sincronización con
Amazon ‣ Cuentas de Amazon.

Todas las cuentas de la misma empresa utilizan la misma ubicación de Amazon de
forma predeterminada, pero es posible monitorear las existencias filtradas por
marketplace.

Para hacerlo, primero deberá eliminar de la lista de marketplaces
sincronizados aquel en donde se encuentran las existencias correspondientes
para monitorearlas por separado. Puede acceder a esta lista desde la
aplicación Ventas ‣ Configuración ‣ Ajustes ‣ Conectores ‣ Sincronización con
Amazon ‣ Cuentas de Amazon.

A continuación, cree otro registro para esta cuenta y elimine todos los
marketplaces **excepto** el que desea aislar de los demás.

Por último, asigne otra ubicación de existencias al segundo registro de la
cuenta.

## Facturar y registrar pagos

### Emitir facturas

Debido a la política de Amazon de no compartir las direcciones de correo
electrónico de los clientes, **no** es posible enviarles las facturas
directamente desde Konvergo ERP. Sin embargo, **sí** es posible cargar de forma manual
las facturas generadas desde Konvergo ERP en el backend de Amazon.

Además, para los clientes B2B, por ahora es necesario obtener la
identificación fiscal de forma manual desde el backend de Amazon **antes** de
crear una factura en Konvergo ERP.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Para los usuarios de <a href="../../../finance/accounting/taxes/taxcloud">TaxCloud</a>: las facturas creadas a partir de órdenes de ventas de Amazon <b>no</b> se sincronizan con TaxCloud, Amazon ya las incluye en su propio reporte de impuestos a TaxCloud.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>La integración con TaxCloud será descontinuada en Konvergo ERP 17.</p>
</div>

### Registrar pagos

Como los clientes pagan a Amazon como intermediario, es recomendable que cree
un diario _bancario_ (con el nombre `Pagos de Amazon`, por ejemplo) con una
cuenta intermediaria _bancaria y de efectivo_ específica.

Además Amazon realiza un solo pago mensual, así que es necesario seleccionar
todas las facturas vinculadas a un solo pago al registrar los pagos.

Para hacer eso, use el **Diario** apropiado específico para los pagos de
Amazon y seleccione **Depósito por lotes** como **método de pago**.

Luego, seleccione todos los pagos generados y haga clic en Acciones ‣ Crear
pago por lotes ‣ Validar.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Puede realizar esta misma acción con las facturas de proveedores de Amazon destinadas a comisiones.</p>
<p>Cuando la cuenta bancaria recibe el saldo al final del mes y después de registrar los estados de cuenta bancarios, acredite la cuenta intermediaria de Amazon por el importe recibida.</p>
</div>

## Llevar seguimiento de las ventas de Amazon en los reportes de venta

El perfil de la cuenta de Amazon en Konvergo ERP cuenta con un equipo de ventas
establecido en la pestaña **Seguimiento de pedidos**.

Esto le proporciona acceso rápido a métricas importantes relacionadas con los
reportes de ventas. De forma predeterminada, el equipo de ventas de la cuenta
de Amazon se comparte entre todas las cuentas de la empresa.

Si lo desea, puede cambiar el equipo de ventas de la cuenta por otro para
realizar un reporte separado para las ventas de esta cuenta.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>También es posible realizar reportes para cada marketplace.</p>
<p>Primero debe eliminar el marketplace deseado de la lista de mercados sincronizados.</p>
<p>Para acceder a la lista de maketplaces sincronizados en Konvergo ERP vaya a la aplicación Ventas ‣ Configuración ‣ Ajustes ‣ Conectores ‣ Sincronización con Amazon ‣ Cuentas de Amazon.</p>
<p>Luego cree otro registro para esta cuenta y elimine todos los marketplaces <b>excepto</b> el que desea aislar.</p>
<p>Por último, asigne otro equipo de ventas a uno de los dos registros de la cuenta.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para sincronizar de inmediato las órdenes de una cuenta de Amazon primero cambie al <a href="../../../general/developer_mode#developer-mode"><span class="std std-ref">modo de desarrollador</span></a>, después vaya a la cuenta de Amazon en Konvergo ERP y haga clic en <b>Sincronizar órdenes</b>. Puede hacer lo mismo con las recolecciones si hace clic en <b>Sincronizar recolecciones</b>.</p>
</div>0

