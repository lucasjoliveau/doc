# Uso del código de barras GS1

Los códigos de barras GS1 proporcionan un formato estandarizado que los
escáneres de códigos de barras pueden interpretar. Codifican la información en
una [estructura específica que se reconoce
internacionalmente](gs1_nomenclature#barcode-operations-gs1) y eso le
permite a los escáneres entender y procesar los datos de la cadena de
suministro de manera consistente.

_Código de barras_ de Konvergo ERP interpreta e imprime los códigos de barras GS1 y de
esa manera se automatiza la identificación y rastreo de productos en las
operaciones de almacén como la recepción, la recolección y el envío.

Las siguientes secciones contienen ejemplos de cómo Konvergo ERP usa los códigos de
barras GS1 que proporcionan los negocios para identificar artículos en común
en los almacenes y automatiza ciertos flujos de trabajo del almacén.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Konvergo ERP <b>no</b> crea códigos de barras GS1. Las empresas deben adquirir un número global de artículo comercial (GTIN) de GS1. Luego, podrán combinar sus códigos de barras GS1 existentes con un producto y la información de la cadena de suministro (que también proporciona GS1) para crear códigos de barras en Konvergo ERP.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="https://www.gs1.org/standards/get-barcodes">Compra de GTIN</a></p></li>
<li><p><a href="gs1_nomenclature#barcode-operations-gs1"><span class="std std-ref">Nomenclatura GS1</span></a></p></li>
</ul>
</div>

## Configuración de códigos de barras por producto, cantidad y lotes

Para crear un código de barras GS1 que contenga la información de los
productos, sus cantidades y números de lote, se usan los siguientes patrones
de código de barras e identificadores de aplicación (A.I. por sus siglas en
inglés):

Nombre | Nombre de regla | IA | Patrón de código de barras | Campo en Konvergo ERP  
---|---|---|---|---  
Producto | Código comercial global de artículo (GTIN) | 01 | (01)(\d{14}) | Campo **Código de barras** en un formulario de producto  
Cantidad | Conteo de artículos variables | 30 | (30)(\d{0,8}) | Campo **Unidades** en el formulario de transferencia  
Número de Lote | Lote o número de lote | 10 | (10)([!»%-/0-9:-?A-Z_a-z]{0,20}) | **Lote** en la ventana emergente de operaciones detalladas  
  
### Configuración

Primero, [active el rastreo de productos con
lotes](../../inventory/product_management/product_tracking/lots#inventory-
management-track-products-by-lots) en Inventario ‣ Configuración ‣ Ajustes y
seleccione la casilla de **Lotes y números de serie** en la sección de
**Trazabilidad**.

Configure el código de barras del producto en su formulario correspondiente en
la aplicación Inventario ‣ Productos ‣ Productos y seleccione el producto. En
el formulario, haga clic en **Editar** y en la pestaña **Información general**
complete el campo **Código de barras** con el [Número global de artículo
comercial (GTIN)](https://www.gs1.org/standards/get-barcodes) único de 14
dígitos que es un número identificador universal de GS1.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Omita el identificador de aplicación <code>01</code> del patrón de código de barras del GTIN del producto en su formulario correspondiente, pues solo se usa para codificar varios códigos de barras en uno solo que contiene toda la información detallada sobre el contenido del paquete.</p>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>Para registrar un código de barras GS1 para el producto <code>Manzana Fuji</code>, ingrese el GTIN de 14 dígitos <code>20611628936004</code> en el campo <b>Código de barras</b> del formulario del producto.</p>
<img alt="Ingrese el GTIN de 14 dígitos en el campo de código de barras dentro del formulario de productos." class="align-center" src="../../../../_images/barcode-field.png"/>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Para ver la lista de <em>todos</em> los productos y sus códigos de barras correspondientes en la base de datos de Konvergo ERP, vaya a Inventario ‣ Configuración ‣ Ajustes. En la sección <b>Código de barras</b>, haga clic en el botón <b>Configurar código de barras de los productos</b> en la sección <b>Escáner de código de barras</b>. Ingrese el GTIN de 14 dígitos en la columna <b>Código de barras</b> y haga clic en <b>Guardar</b>.</p>
<img alt="Vea la página de códigos de barra de productos desde los ajustes del inventario." class="align-center" src="../../../../_images/product-barcodes-page.png"/>
</div>

Después de activar la opción de rastrear el producto según el número de lote o
de serie, debe especificar que esta función se aplicará en cada producto. Vaya
a la pestaña **Inventario** en el formulario del producto y en la sección
**Trazabilidad** elija **Por lotes**.

![Activar el seguimiento del producto por lotes desde la pestaña "Inventario"
del formulario del producto.](../../../../_images/track-by-lots.png)

### Escanear el código de barras de un producto al recibirlo

Para asegurarnos de que Konvergo ERP interpreta bien el lote se interpreta desde el
código de barras al momento de la recepción, vaya a la aplicación Código de
barras para gestionar el [proceso de
recepción](receipts_deliveries#barcode-operations-scan-received-
products).

Desde el tablero de **Escanear código de barras** , haga clic en el botón
**Operaciones** y luego en el botón **Recepciones** para ver toda la lista de
recepciones de los proveedores que debe procesar. Las recepciones generadas
desde las órdenes de compra aparecen en la lista, pero puede crear nuevas
operaciones de recepción directamente desde la aplicación Código de barras con
el botón **Crear**.

En la lista de recibos, haga clic en la operación del almacén (`WH/IN`) para
escanear los códigos de barras de producto y su número de lote con el escáner.
El producto escaneado aparecerá en la lista de inmediato, solo tiene que hacer
clic en el botón con forma de **✏️ (lápiz)** para abrir una ventana e ingresar
las cantidades de forma manual.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Después de realizar una orden de compra para cincuenta manzanas, vaya a la recepción asociada en la aplicación <em>Código de barras</em>.</p>
<p>Escanee el código de barras que contiene el GTIN, la cantidad y el número de lote. Para realizar un prueba con el escáner del código de barras, abajo hay un ejemplo de código de barras para las cincuenta manzanas Fuji en el Lote 2.</p>
<table class="colwidths-given table docutils">
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head stub"><p>50 manzanas Fuji en Lot0002</p></th>
<th class="head"></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><th class="stub"><p>Matriz 2D</p></th>
<td><img alt="Matriz 2D del código de barras GS1 de 50 manzanas Fuji con un número de lote asignado. " src="../../../../_images/fuji-apples-barcode.png"/>
</td>
</tr>
<tr class="row-odd"><th class="stub"><p>Identificador de aplicación (producto)</p></th>
<td><p>01</p></td>
</tr>
<tr class="row-even"><th class="stub"><p>Código de barras GS1 (producto)</p></th>
<td><p>20611628936004</p></td>
</tr>
<tr class="row-odd"><th class="stub"><p>Identificador de aplicación (cantidad)</p></th>
<td><p>30</p></td>
</tr>
<tr class="row-even"><th class="stub"><p>Código de barras GS1 (cantidad)</p></th>
<td><p>00000050</p></td>
</tr>
<tr class="row-odd"><th class="stub"><p>Identificador de aplicación (lote)</p></th>
<td><p>10</p></td>
</tr>
<tr class="row-even"><th class="stub"><p>Código de barras GS1 (# de lote)</p></th>
<td><p>LOT0002</p></td>
</tr>
<tr class="row-odd"><th class="stub"><p>Código de barras GS1 completo</p></th>
<td><p>0120611628936004 3000000050 10LOT0002</p></td>
</tr>
</tbody>
</table>
<p><a href="gs1_nomenclature#barcode-operations-troubleshooting"><span class="std std-ref">Si la configuración es correcta</span></a>, <code>50/50</code> <b>Unidades</b> procesadas se mostrarán y el botón de <b>Validar</b> será verde. Haga clic en el botón <b>Validar</b> para completar la recepción.</p>
<img alt="Escanee el código de barras de un producto al recibir un paquete en la aplicación *Código de barras*." class="align-center" src="../../../../_images/receive-50-apples.png"/>
</div>

## Configuración de códigos de barras para productos y cantidades sin unidad

Para construir un código de barras GS1 para productos que se miden en una
cantidad diferente a las unidades, por ejemplo, kilogramos, debemos usar los
siguientes patrones de códigos de barras:

Nombre | Nombre de regla | IA | Patrón de código de barras | Campo en Konvergo ERP  
---|---|---|---|---  
Producto | Código comercial global de artículo (GTIN) | 01 | (01)(\d{14}) | Campo **Código de barras** en un formulario de producto  
Cantidad en kilogramos | Conteo de artículos variables | 310[0-5] | (310[0-5])(\d{6}) | Campo **Unidades** en el formulario de transferencia  
  
### Escanear el código de barras de un producto al recibirlo

Para confirmar que Konvergo ERP interpreta bien las cantidades, cree una orden en la
aplicación _Compra_ en donde use la unidad de medida (**UdM**) correcta para
los productos que quiere comprar.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../../inventory/product_management/product_replenishment/uom#inventory-product-replenishment-unit-conversion"><span class="std std-ref">Simplificar las conversiones de unidades de proveedores con unidades de medida</span></a></p>
</div>

Ya que se realizó la orden, vaya a la aplicación Código de barras para
[recibir el envío del proveedor](receipts_deliveries#barcode-operations-
scan-received-products).

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>En la recepción en la aplicación <em>Códigos de barras</em>, reciba una orden de <code>52.1 kg</code> de duraznos al escanear el código de barras que contiene el GTIN y la cantidad de duraznos en kilogramos.</p>
<table class="colwidths-given table docutils">
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head stub"><p>52.1 kilos de duraznos</p></th>
<th class="head"></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><th class="stub"><p>Matriz 2D</p></th>
<td><img alt="Matriz 2D del código de barras GS1 de 52.1 kg de duraznos." src="../../../../_images/peaches-barcode.png"/>
</td>
</tr>
<tr class="row-odd"><th class="stub"><p>Identificador de aplicación (producto)</p></th>
<td><p>01</p></td>
</tr>
<tr class="row-even"><th class="stub"><p>Código de barras GS1 (producto)</p></th>
<td><p>00614141000012</p></td>
</tr>
<tr class="row-odd"><th class="stub"><p>Identificador de aplicación (kg, 1 punto decimal)</p></th>
<td><p>3101</p></td>
</tr>
<tr class="row-even"><th class="stub"><p>Código de barras GS1 (cantidad)</p></th>
<td><p>000521</p></td>
</tr>
<tr class="row-odd"><th class="stub"><p>Código de barras GS1 completo</p></th>
<td><p>0100614141000012 3101000521</p></td>
</tr>
</tbody>
</table>
<p><a href="gs1_nomenclature#barcode-operations-troubleshooting"><span class="std std-ref">Si la configuración es correcta</span></a>, <code>52.1 / 52.1</code> <b>kg</b> se mostrarán y el botón <b>Validar</b> será verde.  Finalmente, haga clic en <b>Validar</b> para completar la validación.</p>
<img alt="Pantalla para escanear el código de barras para una operación de recepción en la aplicación Código de barras." class="align-center" src="../../../../_images/scan-barcode-peaches.png"/>
</div>

## Verificar los movimientos de productos

Con el objetivo de verificar aún más, las cantidades que se recibieron del
producto también se registran en el reporte **Historial de movimientos** , al
que puede acceder desde Inventario ‣ Reportes ‣ Historial de movimientos.

Los artículos en el reporte de **Historial de movimientos** se agrupan por
producto en automático. Para confirmar las cantidades recibidas, haga clic en
una línea de producto para abrir el menú desplegable, que muestra la lista de
_líneas de movimiento de inventario_ del producto. El movimiento de inventario
más reciente coincide con el número de referencia de la recepción del almacén
(por ejemplo, `WH/IN/00013`) y la cantidad que se procesó al escanear el
código de barras. Esto mostrará que los registros que se procesaron en la
aplicación _Código de barras_ se guardaron bien en el _Inventario_.

![Registro del movimiento de inventario al momento de la recepción de los 52.1
kg de duraznos.](../../../../_images/stock-moves-peach.png)

