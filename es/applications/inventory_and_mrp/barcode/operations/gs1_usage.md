# Uso del código de barras GS1

Los códigos de barras GS1 proporcionan un formato estandarizado que los
escáneres de códigos de barras pueden interpretar. Codifican la información en
una [estructura específica que se reconoce
internacionalmente](gs1_nomenclature.html#barcode-operations-gs1) y eso le
permite a los escáneres entender y procesar los datos de la cadena de
suministro de manera consistente.

_Código de barras_ de Odoo interpreta e imprime los códigos de barras GS1 y de
esa manera se automatiza la identificación y rastreo de productos en las
operaciones de almacén como la recepción, la recolección y el envío.

Las siguientes secciones contienen ejemplos de cómo Odoo usa los códigos de
barras GS1 que proporcionan los negocios para identificar artículos en común
en los almacenes y automatiza ciertos flujos de trabajo del almacén.

Importante

Odoo **no** crea códigos de barras GS1. Las empresas deben adquirir un número
global de artículo comercial (GTIN) de GS1. Luego, podrán combinar sus códigos
de barras GS1 existentes con un producto y la información de la cadena de
suministro (que también proporciona GS1) para crear códigos de barras en Odoo.

Ver también

  * [Compra de GTIN](https://www.gs1.org/standards/get-barcodes)

  * [Nomenclatura GS1](gs1_nomenclature.html#barcode-operations-gs1)

## Configuración de códigos de barras por producto, cantidad y lotes

Para crear un código de barras GS1 que contenga la información de los
productos, sus cantidades y números de lote, se usan los siguientes patrones
de código de barras e identificadores de aplicación (A.I. por sus siglas en
inglés):

Nombre | Nombre de regla | IA | Patrón de código de barras | Campo en Odoo  
---|---|---|---|---  
Producto | Código comercial global de artículo (GTIN) | 01 | (01)(\d{14}) | Campo Código de barras en un formulario de producto  
Cantidad | Conteo de artículos variables | 30 | (30)(\d{0,8}) | Campo Unidades en el formulario de transferencia  
Número de Lote | Lote o número de lote | 10 | (10)([!»%-/0-9:-?A-Z_a-z]{0,20}) | Lote en la ventana emergente de operaciones detalladas  
  
### Configuración

Primero, [active el rastreo de productos con
lotes](../../inventory/product_management/product_tracking/lots.html#inventory-
management-track-products-by-lots) en Inventario ‣ Configuración ‣ Ajustes y
seleccione la casilla de Lotes y números de serie en la sección de
Trazabilidad.

Configure el código de barras del producto en su formulario correspondiente en
la aplicación Inventario ‣ Productos ‣ Productos y seleccione el producto. En
el formulario, haga clic en Editar y en la pestaña Información general
complete el campo Código de barras con el [Número global de artículo comercial
(GTIN)](https://www.gs1.org/standards/get-barcodes) único de 14 dígitos que es
un número identificador universal de GS1.

Importante

Omita el identificador de aplicación `01` del patrón de código de barras del
GTIN del producto en su formulario correspondiente, pues solo se usa para
codificar varios códigos de barras en uno solo que contiene toda la
información detallada sobre el contenido del paquete.

Example

Para registrar un código de barras GS1 para el producto `Manzana Fuji`,
ingrese el GTIN de 14 dígitos `20611628936004` en el campo Código de barras
del formulario del producto.

![Ingrese el GTIN de 14 dígitos en el campo de código de barras dentro del
formulario de productos.](../../../../_images/barcode-field.png)

Truco

Para ver la lista de _todos_ los productos y sus códigos de barras
correspondientes en la base de datos de Odoo, vaya a Inventario ‣
Configuración ‣ Ajustes. En la sección Código de barras, haga clic en el botón
Configurar código de barras de los productos en la sección Escáner de código
de barras. Ingrese el GTIN de 14 dígitos en la columna Código de barras y haga
clic en Guardar.

![Vea la página de códigos de barra de productos desde los ajustes del
inventario.](../../../../_images/product-barcodes-page.png)

Después de activar la opción de rastrear el producto según el número de lote o
de serie, debe especificar que esta función se aplicará en cada producto. Vaya
a la pestaña Inventario en el formulario del producto y en la sección
Trazabilidad elija Por lotes.

![Activar el seguimiento del producto por lotes desde la pestaña "Inventario"
del formulario del producto.](../../../../_images/track-by-lots.png)

### Escanear el código de barras de un producto al recibirlo

Para asegurarnos de que Odoo interpreta bien el lote se interpreta desde el
código de barras al momento de la recepción, vaya a la aplicación Código de
barras para gestionar el [proceso de
recepción](receipts_deliveries.html#barcode-operations-scan-received-
products).

Desde el tablero de Escanear código de barras, haga clic en el botón
Operaciones y luego en el botón Recepciones para ver toda la lista de
recepciones de los proveedores que debe procesar. Las recepciones generadas
desde las órdenes de compra aparecen en la lista, pero puede crear nuevas
operaciones de recepción directamente desde la aplicación Código de barras con
el botón Crear.

En la lista de recibos, haga clic en la operación del almacén (`WH/IN`) para
escanear los códigos de barras de producto y su número de lote con el escáner.
El producto escaneado aparecerá en la lista de inmediato, solo tiene que hacer
clic en el botón con forma de ✏️ (lápiz) para abrir una ventana e ingresar las
cantidades de forma manual.

Example

Después de realizar una orden de compra para cincuenta manzanas, vaya a la
recepción asociada en la aplicación _Código de barras_.

Escanee el código de barras que contiene el GTIN, la cantidad y el número de
lote. Para realizar un prueba con el escáner del código de barras, abajo hay
un ejemplo de código de barras para las cincuenta manzanas Fuji en el Lote 2.

50 manzanas Fuji en Lot0002 |   
---|---  
Matriz 2D | ![Matriz 2D del código de barras GS1 de 50 manzanas Fuji con un número de lote asignado. ](../../../../_images/fuji-apples-barcode.png)  
Identificador de aplicación (producto) | 01  
Código de barras GS1 (producto) | 20611628936004  
Identificador de aplicación (cantidad) | 30  
Código de barras GS1 (cantidad) | 00000050  
Identificador de aplicación (lote) | 10  
Código de barras GS1 (# de lote) | LOT0002  
Código de barras GS1 completo | 0120611628936004 3000000050 10LOT0002  
  
[Si la configuración es correcta](gs1_nomenclature.html#barcode-operations-
troubleshooting), `50/50` Unidades procesadas se mostrarán y el botón de
Validar será verde. Haga clic en el botón Validar para completar la recepción.

![Escanee el código de barras de un producto al recibir un paquete en la
aplicación *Código de barras*.](../../../../_images/receive-50-apples.png)

## Configuración de códigos de barras para productos y cantidades sin unidad

Para construir un código de barras GS1 para productos que se miden en una
cantidad diferente a las unidades, por ejemplo, kilogramos, debemos usar los
siguientes patrones de códigos de barras:

Nombre | Nombre de regla | IA | Patrón de código de barras | Campo en Odoo  
---|---|---|---|---  
Producto | Código comercial global de artículo (GTIN) | 01 | (01)(\d{14}) | Campo Código de barras en un formulario de producto  
Cantidad en kilogramos | Conteo de artículos variables | 310[0-5] | (310[0-5])(\d{6}) | Campo Unidades en el formulario de transferencia  
  
### Escanear el código de barras de un producto al recibirlo

Para confirmar que Odoo interpreta bien las cantidades, cree una orden en la
aplicación _Compra_ en donde use la unidad de medida (UdM) correcta para los
productos que quiere comprar.

Ver también

[Simplificar las conversiones de unidades de proveedores con unidades de
medida](../../inventory/product_management/product_replenishment/uom.html#inventory-
product-replenishment-unit-conversion)

Ya que se realizó la orden, vaya a la aplicación Código de barras para
[recibir el envío del proveedor](receipts_deliveries.html#barcode-operations-
scan-received-products).

Example

En la recepción en la aplicación _Códigos de barras_ , reciba una orden de
`52.1 kg` de duraznos al escanear el código de barras que contiene el GTIN y
la cantidad de duraznos en kilogramos.

52.1 kilos de duraznos |   
---|---  
Matriz 2D | ![Matriz 2D del código de barras GS1 de 52.1 kg de duraznos.](../../../../_images/peaches-barcode.png)  
Identificador de aplicación (producto) | 01  
Código de barras GS1 (producto) | 00614141000012  
Identificador de aplicación (kg, 1 punto decimal) | 3101  
Código de barras GS1 (cantidad) | 000521  
Código de barras GS1 completo | 0100614141000012 3101000521  
  
[Si la configuración es correcta](gs1_nomenclature.html#barcode-operations-
troubleshooting), `52.1 / 52.1` kg se mostrarán y el botón Validar será verde.
Finalmente, haga clic en Validar para completar la validación.

![Pantalla para escanear el código de barras para una operación de recepción
en la aplicación Código de barras.](../../../../_images/scan-barcode-
peaches.png)

## Verificar los movimientos de productos

Con el objetivo de verificar aún más, las cantidades que se recibieron del
producto también se registran en el reporte Historial de movimientos, al que
puede acceder desde Inventario ‣ Reportes ‣ Historial de movimientos.

Los artículos en el reporte de Historial de movimientos se agrupan por
producto en automático. Para confirmar las cantidades recibidas, haga clic en
una línea de producto para abrir el menú desplegable, que muestra la lista de
_líneas de movimiento de inventario_ del producto. El movimiento de inventario
más reciente coincide con el número de referencia de la recepción del almacén
(por ejemplo, `WH/IN/00013`) y la cantidad que se procesó al escanear el
código de barras. Esto mostrará que los registros que se procesaron en la
aplicación _Código de barras_ se guardaron bien en el _Inventario_.

![Registro del movimiento de inventario al momento de la recepción de los 52.1
kg de duraznos.](../../../../_images/stock-moves-peach.png)

