# Direcciones de entrega y de facturación

Es normal que las empresas tengan más de una oficina, por lo que también es
normal que la factura se deba enviar a una dirección mientras que la entrega
se tenga que realizar en otra. La función de **direcciones del cliente** de
Konvergo ERP está diseñada para poder ayudar en esta situación, ya que podrá
especificar qué dirección usar para qué caso.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><span class="xref std std-doc">resumen</span></p>
</div>

## Configuración

Para especificar la dirección de factura y entrega de una orden de venta,
primero vaya a Contabilidad ‣ Configuración ‣ Ajustes. En la sección
**Facturas del cliente** active **Direcciones del cliente** y haga clic en
**Guardar**.

Ahora en las cotizaciones y órdenes de venta encontrará los campos para la
**Dirección de factura** y la **Dirección de entrega**. Si en el contacto del
cliente hay una dirección de factura o de entrega enlistadas, el campo
correspondiente utilizará esa dirección en automático, pero si no lo quiere
así puede usar cualquier dirección del contacto.

## Facturación y entrega en direcciones diferentes

Las órdenes de entrega y sus recibos de entrega usan la dirección del campo
**Dirección de entrega** de la orden de venta. De form predeterminada, los
reportes de facturación muestran tanto la dirección de envío como la dirección
de facturación para que el cliente pueda estar seguro de que la entrega se
realizará en la ubicación correcta.

Los correos también se envían a direcciones diferentes. La cotización y la
orden de venta se envían al correo electrónico principal del contacto, pero la
factura se envía al correo electrónico de la dirección en **Dirección de
factura** en la orden de venta.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p><a href="../../../studio/pdf_reports">Con Studio</a> puede personalizar documentos como el albarán o el reporte de facturación.</p></li>
<li><p>Si la opción <a href="snailmail">Enviar por correo postal</a> está marcada cuando hace clic en <b>Enviar e imprimir</b>, la factura se enviará a la dirección de facturación.</p></li>
</ul>
</div>

