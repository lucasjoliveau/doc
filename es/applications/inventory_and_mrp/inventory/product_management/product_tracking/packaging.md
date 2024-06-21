# Empaquetado

En la aplicación _Inventario_ de Konvergo ERP, el _embalaje_ se refiere a contenedores
desechables que incluyen varias unidades de un producto en específico.
**Debe** definir el embalaje en el formulario individual de los productos.

Por ejemplo, es necesario configurar distintos paquetes para algunas latas de
refresco como un paquete de 6, un paquete de 12 o una caja de 36, pues los
embalajes **no** son genéricos, sino específicos para cada producto.

## Configuración

Vaya a Inventario ‣ Configuración ‣ Ajustes para utilizar embalajes. En la
sección **Productos** marque la casilla **Empaquetado de los productos** y
haga clic en **Guardar**.

![Habilitar embalajes con la opción "Empaquetado de los
productos".](../../../../../_images/enable-packagings.png)

## Crear embalajes

Es posible crear embalajes desde el formulario del producto o desde la página
**Empaquetados de los productos**.

### Desde el formulario del producto

Para crear embalajes en el formulario de un producto vaya a Inventario ‣
Productos ‣ Productos y seleccione uno.

En la pestaña **Inventario** , diríjase a la sección de **Empaquetado** y haga
clic en **Agregar una línea**. Complete los siguientes campos en la tabla:

  * **Embalaje** (obligatorio): nombre del embalaje que aparece en las órdenes de venta o compra como una opción de embalaje para el producto.

  * **Cantidad incluida** (obligatoria): cantidad de producto en el embalaje.

  * **Unidad de Medida** (obligatoria): unidad de medida para cuantificar el producto.

  * **Ventas** : seleccione esta opción si se trata de un embalaje que se utilizará en órdenes de venta.

  * **Compra** : seleccione esta opción si se trata de un embalaje que se utilizará en órdenes de compra.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Puede acceder a campos adicionales en la tabla de <b>empaquetado</b> si hace clic en el icono <b>(deslizadores)</b> que está ubicado en la parte derecha de los títulos de las columnas en la sección de <b>Empaquetado</b>, allí seleccione las opciones deseadas en el menú desplegable que aparece.</p>
<img alt="El icono de deslizadores que corresponde al menú de opciones adicionales." class="align-center" src="../../../../../_images/slide.png"/>
</div>

  * **Código de barras** : identificador para rastrear el empaquetado en movimientos de existencias o elaboración de órdenes con la [aplicación Código de barras](../../../barcode/operations/receipts_deliveries#barcode-operations-intro). Deje el campo vacío si no utiliza uno.

  * **Empresa** : indica que el empaquetado solo está disponible en la empresa seleccionada. Deje el campo vacío para que el empaquetado esté disponible en todas las empresas.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Para crear un tipo de embalaje para seis unidades del producto <code>Refresco de uva</code> primero haga clic en <b>Agregar una línea</b>. En la línea, nombre al <b>empaquetado</b> como <code>Paquete de 6</code> y establezca la <b>Cantidad incluida</b> en <code>6</code>. Repita este proceso para todos los embalajes adicionales.</p>
<img alt="Crear caja de 6 latas para el producto." class="align-center" src="../../../../../_images/create-product-packaging.png"/>
</div>

### Desde la página de embalajes del producto

Para visualizar todos los embalajes creados vaya a Inventario ‣ Configuración
‣ Embalajes del producto. Esta acción abrirá la página de **Empaquetado de los
productos** con una lista completa de todos los embalajes creados para todos
los productos. Para crear un nuevo empaquetado, solo haga clic en **Nuevo**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Dos productos de refresco, que son <code>Refresco de uva</code> y <code>Refresco de dieta</code>, tienen tres tipos de empaquetado configurados. En la página <b>Empaquetado de los productos</b> cada producto se puede vender como un <code>Paquete de 6</code> que incluye 6 productos, <code>Paquete de 12</code> con 12 productos o una <code>Caja</code> con 32 productos.</p>
<img alt="Lista de diferentes empaquetados para los productos." class="align-center" src="../../../../../_images/packagings.png"/>
</div>

## Aplicar empaquetados

Especifique los embalajes que se deben usar para los productos al crear una
orden de venta en la aplicación Ventas. El embalaje elegido aparece en la
orden de venta en el campo **Empaquetado**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>18 latas del producto <code>Refresco de uva</code>. Este se envasa con tres paquetes tipo <em>six-pack</em>.</p>
<img alt="Asignar empaquetados en la línea de la orden de venta." class="align-center" src="../../../../../_images/packagings-sales-order.png"/>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Puede utilizar los empaquetados junto con la aplicación <a href="../../../barcode/setup/software#inventory-barcode-software"><span class="std std-ref">Código de barras</span></a> de Konvergo ERP. Al recibir los productos de los proveedores, el número de unidades del empaquetado se agrega de forma automática al número interno del producto si escanea el código de barras en el empaquetado.</p>
</div>

