# Facturas de proveedor

En Konvergo ERP podemos registrar las facturas de proveedores de forma **manual** o
**automática** , mientras que el **reporte de cuentas por pagar pendientes**
proporciona una visión general de todas las facturas pendientes para ayudarnos
a pagar las cantidades correctas a tiempo.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p>Tutorial <a href="https://www.odoo.com/slides/slide/registering-a-vendor-bill-1683?fullscreen=1">Registrar una factura de proveedor</a></p></li>
<li><p><a href="../../inventory_and_mrp/purchase/manage_deals/manage">Gestionar facturas de proveedor</a></p></li>
</ul>
</div>

## Creación de factura

### Manualmente

Para crear una factura de proveedor de forma manual, vaya a Contabilidad ‣
Proveedores ‣ Facturas y haga clic en **Crear**.

### Automáticamente

Se pueden crear de forma automática las facturas de proveedores, solo se debe
**enviar un correo electrónico** a un [seudónimo de correo
electrónico](vendor_bills/invoice_digitization#invoice-digitization-
email-alias) vinculado al diario de compras, o **subir un PDF** en
Contabilidad ‣ Proveedores ‣ Facturas y, luego, hacer clic en **subir**.

## Finalización de la factura

Aunque la factura se cree de forma manual o automática, debe asegurarse de que
los siguientes campos se hayan completado correctamente:

  * **Proveedor** : Konvergo ERP completa la información registrada en órdenes de compra o facturas del proveedor.

  * **Referencia de factura** : añade la referencia de la orden de venta y se usa para hacer la [conciliación](payments#payments-matching) al recibir los productos.

  * **Autocompletar** : seleccione una factura u orden de compra para que el documento se complete de forma automática. Debe haber completado el campo de **proveedor** antes de este campo.

  * **Fecha de factura** : es la fecha de la emisión de la factura.

  * **Fecha contable** : es la fecha en la cuál se registra el documento en su contabilidad.

  * **Referencia de pago** : se indica automáticamente en el campo **Memo** al registrar un pago.

  * **Banco destinatario** : indica el número de cuenta al que se tiene que hacer el pago.

  * **Fecha de vencimiento** o **Términos** de la factura a pagar.

  * **Diario** : selecciona el diario en el cuál se registrará la factura y su [divisa](get_started/multi_currency).

![factura de proveedor](../../../_images/bill-completion.png)
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Las facturas se pueden <a href="vendor_bills/invoice_digitization">digitalizar</a> para agilizar la completación automática, solo debe hacer clic en <b>Enviar para digitalización</b>.</p></li>
<li><p>Si carga la factura verá el PDF de lado derecho, de esta manera podrá ver mejor su información.</p></li>
</ul>
</div>

## Confirmación de la factura

Haga clic en **confirmar** cuando termine un documento. El estado de su
documento cambiará a **Publicado** y se creará un asiento de diario según la
configuración de la factura.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Una vez que se confirme no podrá editarlo. Si desea hacer algún cambio, tendrá que hacer clic <b>Restablecer a borrador</b>.</p>
</div>

## Pago de la factura

Una vez pagada la factura del proveedor, haga clic en **Registrar pago** ,
esto hará que aparezca una nueva ventana.

Seleccione el **diario** , el **método de pago** , el **importe** a pagar
(completo o parcial), y la **divisa**. Konvergo ERP completa el campo **Memo** de
manera automática si la **referencia de pago** se estableció correctamente en
la factura de proveedor; se recomienda que seleccione el número de factura de
proveedor como referencia.

Una vez confirmada aparecerá una cinta con el mensaje **en proceso de pago**
hasta que se [concilie](bank/reconciliation) la factura.

## Reporte de cuentas antiguas por pagar

Si desea obtener una vista general de sus facturas de proveedor pendientes y
sus fechas de vencimiento correspondientes, use el **reporte de cuentas
antiguas por pagar**. Vaya a Contabilidad ‣ Reportes ‣ Reportes de contacto:
Cuenta antigua por pagar.

Haga clic en el nombre de un proveedor para ver la información de todas las
facturas con pagos pendientes, su importe, fechas de vencimiento, etc.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Si hace clic en el botón <b>Guardar</b> podrá exportar toda la información disponible como archivo PDF o XLSX y guardarlo en sus documentos.</p></li>
<li><p>Si su proveedor tiene órdenes parciales y le envía facturas cada que envía productos, es posible que reciba varias facturas.</p></li>
</ul>
</div>

  * [Digitalización de documentos con IA](vendor_bills/invoice_digitization)
  * [Activos no circulantes y fijos](vendor_bills/assets)
  * [Gastos diferidos y prepagos](vendor_bills/deferred_expenses)

