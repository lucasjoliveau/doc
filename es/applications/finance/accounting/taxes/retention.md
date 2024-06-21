# Retención fiscal

Una retención fiscal, también llamada impuesto de retención, es un requisito
gubernamental para que el pagador de una factura de un cliente retenga o
deduzca impuestos del pago, y pague ese impuesto al gobierno. En la mayoría de
las jurisdicciones, esta retención se aplica a los ingresos laborales.

Con los impuestos normales, se añade el impuesto al subtotal para obtener el
total a pagar. En cambio, las retenciones se deducen del importe a pagar, ya
que el cliente pagará el impuesto.

Como ejemplo, en Colombia puede tener la siguiente factura:

![../../../../_images/retention03.png](../../../../_images/retention03.png)

En este ejemplo, la **empresa** que envió la factura debe $20 de impuestos al
**gobierno** y el **cliente** debe $10 de impuestos al **gobierno**.

## Configuración

En Konvergo ERP, una retención fiscal se define creando un impuesto negativo. Para una
retención del 10%, usted debería configurar el siguiente impuesto (disponible
a través de Configuración ‣ Impuestos):

![../../../../_images/retention04.png](../../../../_images/retention04.png)

Para que aparezca como retención en la factura, debe establecer un grupo
fiscal específico llamado **Retención** en su impuesto, en la pestaña
**Opciones avanzadas**.

![../../../../_images/retention02.png](../../../../_images/retention02.png)

Una vez definido el impuesto, puede utilizarlo en sus productos, órdenes de
venta o facturas.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si la retención es un porcentaje de un impuesto normal, cree un impuesto con un <b>cálculo de impuestos</b> como <b>grupo de impuestos</b> y establezca los dos impuestos en este grupo (impuesto normal y de retención).</p>
</div>

## Aplicación de las retenciones en las facturas

Una vez que haya creado su impuesto, puede utilizarlo en los formularios de
los clientes, en las órdenes de venta o en las facturas de los clientes. Puede
aplicar varios impuestos en una sola línea de factura de cliente.

![../../../../_images/retention01.png](../../../../_images/retention01.png)
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Cuando usted ve la factura del cliente en la pantalla, solo obtiene una línea de <b>Impuestos</b> que resume todos los impuestos (impuestos normales y retenciones). Pero cuando imprime o envía la factura, Konvergo ERP hace la división correcta entre todos los impuestos.</p>
</div>

La factura impresa mostrará los diferentes importes de cada grupo fiscal.

![../../../../_images/retention03.png](../../../../_images/retention03.png)
<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../taxes">Impuestos</a></p></li>
</ul>
</div>

