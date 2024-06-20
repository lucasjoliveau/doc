# Recibos y facturas

## Recibos

Puede configurar los recibos en Punto de venta ‣ Configuración ‣ Punto de
venta, seleccione un PdV y baje a la sección facturas y recibos.

Para personalizar el **encabezado** y el **pie de página** , active la función
encabezado y pie de página y complete ambos campos con la información que se
debe imprimir en los recibos.

Para **imprimir recibos** de forma automática en cuanto se registre el pago,
habilite el ajuste impresión automática del recibo.

![Recibo de PdV](../../../_images/receipt.png)

Ver también

  * [Cuentas](restaurant/bill_printing.html)

  * [Impresoras ePOS](configuration/epos_printers.html)

### Volver a imprimir un recibo

En la interfaz de PdV, haga clic en órdenes, abra el menú desplegable de
selección que se encuentra al lado de la barra de búsqueda y cambie el filtro
predeterminado todas las órdenes activas a pagada. Después, seleccione la
orden correspondiente y haga clic en imprimir recibo.

![Botón de imprimir recibo desde el backend](../../../_images/print-
receipt.png)

Nota

Puede filtrar la lista de órdenes mediante la barra de búsqueda. Escriba su
referencia y haga clic en número de recibo, fecha o cliente.

## Facturas

El Punto de venta le permitirá emitir e imprimir facturas para [clientes
registrados](../point_of_sale.html#pos-customers) una vez que se realice el
pago; también podrá obtener todas las facturas antiguas.

Nota

Una factura creada en el Punto de venta creará un asiento en el [diario
bancario](../../finance/accounting/get_started/cheat_sheet.html#cheat-sheet-
journals) que haya configurado.

### Configuración

Para definir los diarios a utilizar en un PdV en específico, vaya a los
ajustes de [PdV](configuration.html#configuration-settings) y diríjase a la
sección de contabilidad. Ahí podrá determinar los diarios contables que se
usarán de forma predeterminada para las órdenes y las facturas en la sección
Diarios predeterminados.

![sección de contabilidad en los ajustes del punto de
venta](../../../_images/invoice-config.png)

### Facturar a un cliente

Al procesar el pago, haga clic en Factura bajo el nombre del cliente para
emitir una factura para esa orden.

Seleccione el método de pago y haga clic en validar. La **factura** se emite
de forma automática y se puede descargar o imprimir de inmediato.

Nota

Para poder emitir una factura, debe seleccionar a un
[cliente](../point_of_sale.html#pos-customers).

### Obtener facturas

Siga los siguientes pasos para obtener las facturas desde el **tablero de
PdV** :

  1. Acceda a todas las ordenes realizadas en su PdV en Punto de venta ‣ Órdenes ‣ Órdenes;

  2. Para obtener la factura de una orden, abra el **formulario de la orden** seleccione la orden y haga clic en factura.

![Botón inteligente de factura en el formulario de una
orden](../../../_images/invoice-smart-button.png)

Nota

  * Puede identificar las **órdenes facturadas** porque la columna estado indica que su estado es facturada.

  * Puede filtrar la lista de órdenes por facturar al hacer clic en filtros y facturada.

### Códigos QR para generar facturas

Los clientes pueden solicitar una factura mediante el escaneo de un **código
QR** impreso en su recibo. Al escanearlo, deben completar un formulario con su
información de facturación y hacer clic en obtener mi factura. Por un lado,
hacer esto genera una factura disponible para descarga. Por otro lado, el
estado de la orden en el backend de Odoo cambia de pagada o publicada a
facturada.

![Cambio en el estado de la orden](../../../_images/order-status.png)

Para utilizar esta función debe habilitar los códigos QR en los recibos en
Punto de venta ‣ Configuración ‣ Ajustes. Luego, seleccione el PdV en el campo
punto de venta, baje a la sección facturas y recibos y habilite la función
utilizar código QR en el recibo.

