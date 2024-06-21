# Pronóstico de futuras facturas por pagar

En Konvergo ERP, puede configurar **Términos de pago** y **seguimientos** automáticos
para gestionar los pagos.

## Configuración: términos de pago

Para gestionar las condiciones de los vendedores usamos **términos de pago**.
Esto nos permite dar seguimiento de las fechas límite en las facturas. Algunos
ejemplos de **términos de pago** son:

  * 50% dentro de 30 días

  * 50% dentro de 45 días

Para crearlos, vaya a Contabilidad ‣ Configuración ‣ Facturación: términos de
pago y haga clic en guilabel:`Crear` para agregar nuevos términos. Haga clic
en los términos de pago existentes para modificarlos.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="https://www.odoo.com/slides/slide/payment-terms-1679?fullscreen=1">Tutoriales de Konvergo ERP: términos de pago</a></p>
</div>

Una vez que haya definido **términos de pago** puede asignarlos a un vendedor
para que se usen de manera predeterminada. Para hacerlo vaya a Proveedores ‣
Proveedores y haga clic en la pestaña **Ventas y compra** y seleccione un
**término de pago** específico. De esta manera, siempre que compre de este
proveedor, Konvergo ERP procesará el término de pago elegido de manera automática.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si no configura un término de pago específico en un proveedor, todavía puede configurar una en la factura de un proveedor.</p>
</div>

## Pronóstico de las facturas a pagar con el reporte de cuentas antiguas por
pagar

Para rastrear las cantidades que se le deben de pagar a los proveedores, use
el reporte **Cuenta antigua por pagar**. Para acceder a él vaya a Contabilidad
‣ Reportes ‣ Reportes de contactos: Cuenta antigua por pagar. Este reporte le
brindará un resumen pro proveedor de las cantidades por pagar, comparadas a la
fecha límite (que se calcula en cada factura usando los términos). Este
reporte le indica cuánto tendrá que pagar en los siguientes meses.

## Seleccionar facturas por pagar

Puede obtener una lista de sus facturas de proveedor en Proveedores ‣
Facturas. Para ver solo las facturas que necesita pagar, haga clic en Filtros
‣ Facturas por pagar. Para ver solo los pagos que no se han realizado,
seleccione el filtro **Atrasado**.

También puede agrupar facturas dependiendo de la fecha límite, para hacerlo
haga clic en Agrupar por ‣ Fecha de vencimiento y seleccione un periodo.

