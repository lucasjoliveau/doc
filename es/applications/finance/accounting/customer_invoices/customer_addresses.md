# Direcciones de entrega y de facturación

Es normal que las empresas tengan más de una oficina, por lo que también es
normal que la factura se deba enviar a una dirección mientras que la entrega
se tenga que realizar en otra. La función de **direcciones del cliente** de
Odoo está diseñada para poder ayudar en esta situación, ya que podrá
especificar qué dirección usar para qué caso.

Ver también

resumen

## Configuración

Para especificar la dirección de factura y entrega de una orden de venta,
primero vaya a Contabilidad ‣ Configuración ‣ Ajustes. En la sección Facturas
del cliente active Direcciones del cliente y haga clic en Guardar.

Ahora en las cotizaciones y órdenes de venta encontrará los campos para la
Dirección de factura y la Dirección de entrega. Si en el contacto del cliente
hay una dirección de factura o de entrega enlistadas, el campo correspondiente
utilizará esa dirección en automático, pero si no lo quiere así puede usar
cualquier dirección del contacto.

## Facturación y entrega en direcciones diferentes

Las órdenes de entrega y sus recibos de entrega usan la dirección del campo
Dirección de entrega de la orden de venta. De form predeterminada, los
reportes de facturación muestran tanto la dirección de envío como la dirección
de facturación para que el cliente pueda estar seguro de que la entrega se
realizará en la ubicación correcta.

Los correos también se envían a direcciones diferentes. La cotización y la
orden de venta se envían al correo electrónico principal del contacto, pero la
factura se envía al correo electrónico de la dirección en Dirección de factura
en la orden de venta.

Nota

  * [Con Studio](../../../studio/pdf_reports.html) puede personalizar documentos como el albarán o el reporte de facturación.

  * Si la opción [Enviar por correo postal](snailmail.html) está marcada cuando hace clic en Enviar e imprimir, la factura se enviará a la dirección de facturación.

