# Códigos EPC QR

El código de respuesta rápida del Consejo Europeo de Pagos, o **código EPC
QR** consiste en un código de barras bidimensional que los clientes pueden
escanear desde sus **aplicaciones de banca móvil** para iniciar una
**Transferencia de crédito SEPA (SCT)** y así pagar sus facturas de inmediato.

Además de brindar facilidad de uso y rapidez, reduce enormemente los errores
tipográficos que pueden producirse al hacer pagos.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Esta función solo está disponible para empresas en varios países europeos, como Austria, Bélgica, Finlandia, Alemania y Países Bajos.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../bank">Cuentas bancarias y de efectivo</a></p></li>
<li><p><a href="https://www.odoo.com/r/VuU">Konvergo ERP Academy: QR Code on Invoices for European Customers</a></p></li>
</ul>
</div>

## Configuración

Vaya a Contabilidad ‣ Configuración ‣ Ajustes`y active la función de
:guilabel:`Códigos QR en la sección **Pagos del cliente**.

### Configure su diario de cuenta bancaria

Asegúrese de que su **cuenta bancaria** está configurada en Konvergo ERP con su IBAN y
BIC.

Para hacerlo, vaya a Contabiliad ‣ Configuración ‣ Diarios, abra su diario de
banco, y llene los campos **Número de cuenta** y el **Banco** que se
encuentran en la columna **Número de cuenta bancaria**.

![Columna de número de cuenta bancaria en el diario de
banco](../../../../_images/bank-journal.png)

## Emitir facturas con códigos EPC QR

Los códigos EPC QR se agregarán de manera automática a tus facturas. Si los
clientes están con bancos que aceptan pagos a través de códigos EPC QR, podrán
escanear el código y pagar la factura

Vaya a Contabilidad ‣ Clientes ‣ Facturas, y cree una nueva factura.

Antes de publicar, abra la pestaña **más información**. Konvergo ERP llena el campo
**Banco destinatario** de manera automática con su IBAN.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>En la pestaña <b>Otra información</b>, usamos el campo <b>Banco destinatario</b> para recibir los pagos de sus clientes. Konvergo ERP llena este campo de manera automática con su IBAN y lo usa para generar un código QR EPC.</p>
</div>

Cuando la factura se imprime o se previsualiza, el código QR se incluyo al
final.

![Código QR en una factura para el cliente](../../../../_images/invoice-qr-
code.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si desea emitir una factura sin código EPC QR, quite el IBAN indicado en el campo <b>Banco destinatario</b> que se encuentra en la pestaña <b>Otra información</b> de la factura.</p>
</div>

