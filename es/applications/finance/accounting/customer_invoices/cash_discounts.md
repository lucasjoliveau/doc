# Descuentos por pronto pago y reducción de impuestos

Los **descuentos por pronto pago** son reducciones a la cantidad que un
cliente tiene que pagar por un bien o servicio ofrecidos como incentivo para
pagar su factura de manera rápida. Estos descuentos suelen ser un porcentaje
de la cantidad total en la factura y se aplican solo si el cliente paga en un
plazo específico. Los descuentos por pronto pago ayudan a que la empresa
mantenga un flujo de efectivo constante.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Crea una factura de €100 el primero de enero. El pago total se tiene que hacer dentro de los siguientes 30 días, pero también ofrece un descuento del 2% si el cliente paga dentro de los primeros 7 días.</p>
<p>El cliente puede pagar €98 hasta el 8 de enero. Después de esta fecha, tendrá que pagar €100 antes del 31 de enero.</p>
</div>

También se puede aplicar una reducción de impuestos dependiendo del país o la
región.

## Configuración

Para proporcionar descuentos a los clientes, priero debe de configurar un tipo
de reducción de impuestos, verificar las cuentas de pérdidas y ganancias y
configurar nuevos términos de pago.

### Reducciones de impuestos

Según el país o la región, la cantidad de base que se usa para calcular los
impuestos varía, lo que puede resultar en una **reducción de impuestos**.

Para configurar cómo funciona la reducción de impuestos, vaya a Contabilidad ‣
Configuración ‣ Ajustes. En la sección **Impuestos** vaya a la función
**Reducción de impuestos por diferencia de efectivo** y seleccione una de las
siguientes tres opciones:

Siempre (al facturar)

    

El impuesto siempre se reduce. La cantidad de base que se usa para calcular el
impuesto es la cantidad de diferencia, no importa si el cliente obtiene algún
beneficio o no.

En pago anticipado

    

El impuesto se reduce solo si el cliente paga antes. La cantidad de base que
se usa para calcular el impuesto es la misma que la venta: si el cliente
obtiene un beneficio de la reducción, entonces se reduce el impuesto. Esto
significa que la cantidad de los impuestos puede variar después de enviar la
factura, dependiendo del cliente.

Nunca

    

El impuesto no se reduce. La cantidad de base que se usa para calcular el
impuesto es la cantidad total, no importa si el cliente se beneficia o no del
descuento.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Supongamos que usted crea una factura de €100 (libre de impuestos) con una tasa tributaria del 21%, el 1 de enero. El pago completo se debe de realizar dentro de los próximos 30 días y también ofrece un descuento del 2% si su cliente paga dentro de los próximos 7 días.</p>
<div class="sphinx-tabs docutils container">
<div aria-label="Tabbed content" role="tablist"><button aria-controls="panel-0-0-0" aria-selected="true" class="sphinx-tabs-tab" id="tab-0-0-0" name="0-0" role="tab" tabindex="0">Always (upon invoice)</button><button aria-controls="panel-0-0-1" aria-selected="false" class="sphinx-tabs-tab" id="tab-0-0-1" name="0-1" role="tab" tabindex="-1">On early payment</button><button aria-controls="panel-0-0-2" aria-selected="false" class="sphinx-tabs-tab" id="tab-0-0-2" name="0-2" role="tab" tabindex="-1">Never</button></div><div aria-labelledby="tab-0-0-0" class="sphinx-tabs-panel" id="panel-0-0-0" name="0-0" role="tabpanel" tabindex="0"><table class="table docutils">
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Fecha límite</p></th>
<th class="head"><p>Importe total sin pagar</p></th>
<th class="head"><p>Cálculo</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>8 de enero</p></td>
<td><p>€118.58</p></td>
<td><p>(€98 + (21% of €98))</p></td>
</tr>
<tr class="row-odd"><td><p>31 de enero</p></td>
<td><p>€120.58</p></td>
<td><p>(€100 + (21% de €98))</p></td>
</tr>
</tbody>
</table>
</div><div aria-labelledby="tab-0-0-1" class="sphinx-tabs-panel" hidden="true" id="panel-0-0-1" name="0-1" role="tabpanel" tabindex="0"><table class="table docutils">
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Fecha límite</p></th>
<th class="head"><p>Importe total sin pagar</p></th>
<th class="head"><p>Cálculo</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>8 de enero</p></td>
<td><p>€118.58</p></td>
<td><p>(€98 + (21% of €98))</p></td>
</tr>
<tr class="row-odd"><td><p>31 de enero</p></td>
<td><p>€121.00</p></td>
<td><p>(€100 + (21% de €100))</p></td>
</tr>
</tbody>
</table>
</div><div aria-labelledby="tab-0-0-2" class="sphinx-tabs-panel" hidden="true" id="panel-0-0-2" name="0-2" role="tabpanel" tabindex="0"><table class="table docutils">
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Fecha límite</p></th>
<th class="head"><p>Importe total sin pagar</p></th>
<th class="head"><p>Cálculo</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>8 de enero</p></td>
<td><p>€119.00</p></td>
<td><p>(€98 + (21% de €100))</p></td>
</tr>
<tr class="row-odd"><td><p>31 de enero</p></td>
<td><p>€121.00</p></td>
<td><p>(€100 + (21% de €100))</p></td>
</tr>
</tbody>
</table>
</div></div>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p><a href="../reporting/tax_returns#tax-returns-tax-grids"><span class="std std-ref">Las tablas de impuestos</span></a>, que se usan para el reporte de impuestos, se calculan de manera correcta según el <a href="#cash-discounts-tax-reductions"><span class="std std-ref">tipo de reducción de impuestos</span></a> que configuró.</p></li>
<li><p>El <b>tipo de reducción de impuestos por diferencia de efectivo</b> puede preconfigurarse de manera correcta dependiendo del <a href="../../fiscal_localizations#fiscal-localizations-packages"><span class="std std-ref">paquete de localización fiscal</span></a> con el que cuenta.</p></li>
</ul>
</div>

### Cuentas de ganancias o pérdidas por descuentos pronto pago

Con el descuento por pronto pago, la cantidad que gana depende de cuánto se
beneficia el cliente o no del descuento. Esto siempre lleva a pérdidas o
ganancias, que se registran en cuentas predeterminadas.

Para modificar estas cuentas vaya a Contabilidad ‣ Configuración ‣ Ajustes. En
la sección **Cuentas predeterminadas** seleccione las cuentas que quiere usar
para la **Cuenta de ganancia por descuento de efectivo** y la **Cuenta de
pérdida por descuento de efectivo**.

### Términos de pago

Los descuentos por pronto pago se definen en los [términos de
pago](payment_terms). Para configurarlos como usted quiere vaya a
Contabilidad ‣ Configuración ‣ Términos de pago, y llene los campos **% de
descuento** and **Días de descuento**.

![Configuración de los términos de pago llamados "2/7 neto 30". El campo
"Descripción en las facturas" dice: "Términos de pago: 30 días, 2% de
descuento por pago anticipado antes de 7 días".](../../../../_images/payment-
terms.png) <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="payment_terms">Términos de pago y planes de pago a plazos</a></p>
</div>

## Aplicar un descuento por pronto pago a una factura

Para aplicar un descuento por pronto pago a una factura de cliente seleccione
los términos de pago que usted creó. Konvergo ERP calculará de manera automática las
cantidades correctas, los impuestos, las fechas de vencimiento y los registros
de contabilidad.

En la pestaña **asientos de diario** puede mostrar los detalles del descuento.
Para hacerlo tiene que hacer clic en el botón de «alternar» y agregar las
columnas **Fecha de descuento** e **Importe del descuento**.

![Una factura por €100.00 en la que se seleccionó "2/7 neto 30" como término
de pago. La pestaña de "asientos de diario" está abierta, y se muestran las
columnas de "Fecha de descuento" e "Importe de
descuento".](../../../../_images/invoice-journal-entry.png)

La cantidad del descuento y la fecha límite también se muestran en la factura
generada que se envía al cliente.

![Una factura de €100.00 con el texto a continuación agregado como términos y
condiciones: "30 días, 2% de descuento por pago anticipado antes de 7 días. El
total es de €118.58 si se paga antes del
01/08/2023."](../../../../_images/invoice-print.png)

### Conciliación de pagos

Cuando registra un pago o concilia sus estados de cuenta bancaria, Konvergo ERP toma
en cuenta la fecha del pago del cliente para definir si se pueden beneficiar
del descuento por pronto pago o no.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si el cliente realiza el pago de la cantidad con el descuento después de la fecha límite para obtener el descuento, usted es quien decide si marca el pago como completo o parcial.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../payments">Pagos</a></p>
</div>

