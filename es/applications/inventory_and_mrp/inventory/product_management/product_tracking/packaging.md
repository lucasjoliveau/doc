# Empaquetado

En la aplicación _Inventario_ de Odoo, el _embalaje_ se refiere a contenedores
desechables que incluyen varias unidades de un producto en específico.
**Debe** definir el embalaje en el formulario individual de los productos.

Por ejemplo, es necesario configurar distintos paquetes para algunas latas de
refresco como un paquete de 6, un paquete de 12 o una caja de 36, pues los
embalajes **no** son genéricos, sino específicos para cada producto.

## Configuración

Vaya a Inventario ‣ Configuración ‣ Ajustes para utilizar embalajes. En la
sección Productos marque la casilla Empaquetado de los productos y haga clic
en Guardar.

![Habilitar embalajes con la opción "Empaquetado de los
productos".](../../../../../_images/enable-packagings.png)

## Crear embalajes

Es posible crear embalajes desde el formulario del producto o desde la página
Empaquetados de los productos.

### Desde el formulario del producto

Para crear embalajes en el formulario de un producto vaya a Inventario ‣
Productos ‣ Productos y seleccione uno.

En la pestaña Inventario, diríjase a la sección de Empaquetado y haga clic en
Agregar una línea. Complete los siguientes campos en la tabla:

  * Embalaje (obligatorio): nombre del embalaje que aparece en las órdenes de venta o compra como una opción de embalaje para el producto.

  * Cantidad incluida (obligatoria): cantidad de producto en el embalaje.

  * Unidad de Medida (obligatoria): unidad de medida para cuantificar el producto.

  * Ventas: seleccione esta opción si se trata de un embalaje que se utilizará en órdenes de venta.

  * Compra: seleccione esta opción si se trata de un embalaje que se utilizará en órdenes de compra.

Nota

Puede acceder a campos adicionales en la tabla de empaquetado si hace clic en
el icono (deslizadores) que está ubicado en la parte derecha de los títulos de
las columnas en la sección de Empaquetado, allí seleccione las opciones
deseadas en el menú desplegable que aparece.

![El icono de deslizadores que corresponde al menú de opciones
adicionales.](../../../../../_images/slide.png)

  * Código de barras: identificador para rastrear el empaquetado en movimientos de existencias o elaboración de órdenes con la [aplicación Código de barras](../../../barcode/operations/receipts_deliveries.html#barcode-operations-intro). Deje el campo vacío si no utiliza uno.

  * Empresa: indica que el empaquetado solo está disponible en la empresa seleccionada. Deje el campo vacío para que el empaquetado esté disponible en todas las empresas.

Example

Para crear un tipo de embalaje para seis unidades del producto `Refresco de
uva` primero haga clic en Agregar una línea. En la línea, nombre al
empaquetado como `Paquete de 6` y establezca la Cantidad incluida en `6`.
Repita este proceso para todos los embalajes adicionales.

![Crear caja de 6 latas para el producto.](../../../../../_images/create-
product-packaging.png)

### Desde la página de embalajes del producto

Para visualizar todos los embalajes creados vaya a Inventario ‣ Configuración
‣ Embalajes del producto. Esta acción abrirá la página de Empaquetado de los
productos con una lista completa de todos los embalajes creados para todos los
productos. Para crear un nuevo empaquetado, solo haga clic en Nuevo.

Example

Dos productos de refresco, que son `Refresco de uva` y `Refresco de dieta`,
tienen tres tipos de empaquetado configurados. En la página Empaquetado de los
productos cada producto se puede vender como un `Paquete de 6` que incluye 6
productos, `Paquete de 12` con 12 productos o una `Caja` con 32 productos.

![Lista de diferentes empaquetados para los
productos.](../../../../../_images/packagings.png)

## Aplicar empaquetados

Especifique los embalajes que se deben usar para los productos al crear una
orden de venta en la aplicación Ventas. El embalaje elegido aparece en la
orden de venta en el campo Empaquetado.

Example

18 latas del producto `Refresco de uva`. Este se envasa con tres paquetes tipo
_six-pack_.

![Asignar empaquetados en la línea de la orden de
venta.](../../../../../_images/packagings-sales-order.png)

Truco

Puede utilizar los empaquetados junto con la aplicación [Código de
barras](../../../barcode/setup/software.html#inventory-barcode-software) de
Odoo. Al recibir los productos de los proveedores, el número de unidades del
empaquetado se agrega de forma automática al número interno del producto si
escanea el código de barras en el empaquetado.

