# Cree y procese las transferencias con código de barras

Puede usar la aplicación _Código de barras_ para procesar transferencias
internas para todos los tipos de productos, incluyendo las transferencias de
productos que se rastreen con números de lote o de serie. Las transferencias
se pueden crear desde cero en tiempo real con un lector de barras que se
compatible con la aplicación móvil de Konvergo ERP.

Para ver una lista de códigos de barras compatibles con Konvergo ERP, además de otros
hardware para la aplicación _Inventario_ , vaya a [la página de Konvergo ERP
Inventario • Hardware](https://www.odoo.com/app/inventory-hardware).

## Activar la aplicación Código de barras

Para utilizar la aplicación _Código de barras_ para procesar transferencias,
**debe** instalarla. Para esto tiene que habilitar la función desde la
configuración de la aplicación _Inventario_.

Para hacerlo, vaya a la aplicación de Inventario ‣ Configuración ‣ Ajustes.
Desplácese hacia abajo hasta la sección de Código de barras, y marque la
casilla junto a la función Lector de código de barras.

Una vez que la casilla esté marcada, haga clic en **Guardar** en la parte
superior de la página para guardar los cambios.

Cuando vuelva a cargar la página, aparecerán nuevas opciones en la función
**Lector de código de barras:** **nomenclatura de código de barras** (con el
menú desplegable correspondiente), puede seleccionar ya sea la **nomenclatura
predeterminada** o la **la nomenclatura predeterminada GS1**. La nomenclatura
seleccionada cambia la forma en la que los lectores de códigos de barra
interpretarán los códigos de barra en Konvergo ERP.

También hay una flecha de enlace interno **Configurar códigos de barras de
productos** , junto con un conjunto de botones de **Imprimir** para imprimir
comandos de códigos de barras y una hoja de demostración de códigos de barras.

![Activar la función de código de barras en los ajustes de la aplicación
Inventario.](../../../../_images/transfers-scratch-enabled-barcode-
setting.png)

Para obtener más información sobre la instalación y configuración de la
aplicación **Código de barras** , consulte las páginas de documentación
[Configurar su escáner de código de barras](../setup/hardware) y [Active
los códigos de barras en Konvergo ERP](../setup/software).

## Escanear códigos de barra para transferencias internas

Para crear y procesar transferencias internas para productos en un almacén
**debe** habilitar las funciones **ubicaciones de almacén** y **Rutas
multietapa**.

Para hacerlo, vaya a la aplicación de Inventario ‣ Configuración ‣ Ajustes.
Desplácese hacia abajo hasta la sección de Almacén, y marque las casillas
junto a **Ubicaciones de almacenamiento** y **Rutas multietapa**.

Después, haga clic en **Guardar** en la parte superior de la página para
guardar los cambios.

### Crear un traslado interno

Para procesar transferencias internas existentes, primero necesita existir una
transferencia interna creada y una operación por procesar.

Para crear una transferencia interna, vaya a la aplicación Inventario. Desde
el tablero **Resumen de inventario** ubique el recuadro **Transferencias
internas** y haga clic en el botón **0 por procesar**.

Después, haga clic en **Crear** en la parte superior izquierda de la página
resultante. Esto lo llevará a un nuevo formulario **Transferencia interna**.

En este formulario vacío, el campo **Tipo de operación** aparece en automático
como **Traslados internos**. En este campo, los campos **Ubicación de origen**
y **Ubicación de destino** están configurados como **WH/Stock** de forma
predeterminada, pero puede cambiarla a cualquier ubicación desde y a la que se
muevan los productos.

![Formulario de transferencia interna en blanco con ubicación de origen y de
destino.](../../../../_images/transfers-scratch-internal-transfer-form.png)

Una vez que haya seleccionado las ubicaciones deseada, puede agregar productos
a la transferencia. En la línea de **Producto** que se encuentra en la pestaña
de **Productos** haga clic en **Agregar un producto** y seleccione los
productos que desea agregar a la transferencia.

Una vez listo, haga clic en **Guardar** en la parte superior del formulario
para guardar la nueva transferencia interna. Una vez guardada, haga clic en el
icono **Operaciones detalladas** (cuatro líneas, en el extremo derecho de la
línea de **producto**) para abrir la ventana emergente **Operaciones
detalladas**.

![Ventana emergente de sobre operaciones detalladas de transferencia
interna.](../../../../_images/transfers-scratch-detailed-operations-popup.png)

Desde la ventana emergente, haga clic en **Agregar una línea**.

Después, en la columna **Para** , cambie la ubicación de **WH/Stock** a una
ubicación diferente a la que se tengan que mover los productos.

Después, en la columna **Listo** , cambie la cantidad a la cantidad que quiere
transferir. Una vez que esté listo, haga clic en **Confirmar** para cerrar la
ventana emergente.

### Escanear los códigos de barras para transferencias internas

Para procesar y escanear códigos de barras para transferencias internas vaya a
la aplicación Código de barras.

Una vez en la **aplicación Código de barras** , aparecerán una pantalla para
el **escaneo de código de barras** donde se muestran varias opciones.

Para procesar transferencias internas, haga clic en el botón **Operaciones**
en la parte inferior de la pantalla. Esto lo redirigirá a una pantalla de
Operaciones.

![Pantalla de inicio de la aplicación Lector de código de barras con un lector
de códigos de barras](../../../../_images/transfers-scratch-barcode-app.png)

En esta página ubique el recuadro **Transferencias internas** y haga clic en
el botón **# por procesar** para ver todas las transferencias internas
pendientes, después, seleccione la operación que quiere procesar. Esto lo
llevará a la pantalla de transferencia de código de barras.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Al usar la aplicación <em>Código de barras</em> sin la aplicación <em>Inventario</em> (<b>solo</b> si usa un lector de código de barras o la aplicación móvil de Konvergo ERP), los códigos de barras para cada transferencia del tipo de operación correspondiente se pueden escanear para procesarse sin problemas.</p>
<p>Se pueden escanear los productos que forman parte de una transferencia existente y también se pueden añadir nuevos productos a la transferencia. Una vez escaneados todos los productos, valide el traslado para proceder a los movimientos de inventario.</p>
</div>

Desde esta pantalla aparecerá una vista general de todas los productos por
procesar dentro de esa transferencia interna específica (**WH/INT/000XX**). En
la parte inferior de la pantalla hay opciones para **Agregar un producto** o
**validarlo** , dependiendo si los productos necesitan agregarse a la
operación, o si se debe validar toda la operación al mismo tiempo.

![Resumen de las recepciones en la transferencia por
escanear.](../../../../_images/transfers-scratch-receipts-overview.png)

Después, escanee el código de barras del producto para procesar la
transferencia interna.

O, para procesar y escanear cada producto de forma individual, seleccione una
línea de producto específica. Puede hacer clic en el botón **+1** para agregar
más cantidades de esa transferencia de producto, o en el icono de **lápiz**
para abrir una nueva pantalla y editar esa línea de producto.

En la ventana emergente del producto se muestra el producto y las unidades a
procesar con un teclado numérico. Debajo del nombre del producto, se puede
editar la línea **Cantidad**. Cambie el número de la línea por la cantidad que
aparece para transferir en el formulario de transferencia interna.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>En la operación de transferencia interna <code>WH/INT/000XX</code>, se mueven  <code>50 unidades</code> del <code>producto de transferencia</code> de <code>WH/Stock</code> a <code>WH/Stock/Shelf 1</code>. <code>[TRANSFER_PROD]</code> es la <b>referencia interna</b> configurada en el formulario del producto. Escanee el código de barras del <code>producto de transferencia</code> para recibir una unidad. Después, haga clic en el icono de <b>lápiz</b> para ingresar las cantidades transferidas de forma manual.</p>
<img alt="Editor de la línea de producto para transferencia individual en la aplicación Código de barras." class="align-center" src="../../../../_images/transfers-scratch-product-line-editor.png"/>
</div>

Además, puede hacer clic en los botones **+1** y **-1** para agregar o quitar
cantidades de un producto, además de que también puede usar el teclado de
números para agregar cantidades.

Debajo del teclado numérico hay dos líneas de **ubicación** que lee las
ubicaciones que se hayan especificado en el formulario de transferencia
interna, en este caso `WH/Stock` y `WH/Stock/Shelf 1`. Haga clic en estas
líneas para mostrar un menú desplegable de ubicaciones adicionales de entre
las cuales seleccionar.

Una vez que esté listo, haga clic en **Confirmar** para confirmar los cambios
realizados en la línea de producto.

Después, desde la página de resumen con todos los productos para procesar
dentro de esa transferencia (**WH/INT/000XX**) y haga clic en **Validar**. Ya
procesó la recepción y puede cerrar la aplicación _Código de barras_.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>También puede usar la aplicación <em>Código de barras</em> para escanear productos en transferencias internas que contengan números de lote únicos y números de serie.</p>
<p>Desde la pantalla de transferencia de código de barras, escanee el código de barras de un lote o número de serie, y Konvergo ERP automáticamente incrementa la cantidad del producto a la cantidad registrada en la base de datos. Si diferentes productos comparten el mismo número de lote o de serie, escanee primero el código de barras del producto y luego el código de barras del lote/número de serie.</p>
</div>

## Crear una transferencia desde cero

Además de procesas y escanear códigos de barras para transferencias existentes
que ya se habían creado, también puede usar la aplicación _Código de barras_
para crear transferencias desde cero, solo tiene que escanear un código de
barras impreso de tipo operación.

<div class="admonition-did-you-know alert">
<p class="alert-title">
¿Sabía que?</p><p>La aplicación <em>Código de barras</em> de Konvergo ERP proporciona datos de demostración con códigos de barras para explorar las características de la aplicación. Estos pueden usarse para realizar pruebas y pueden imprimirse desde la pantalla de inicio de la aplicación. Para acceder a estos datos de demostración, navegue a la aplicación de Código de barras y haga clic en la <b>hoja de códigos de barras de existencias</b> (en negrita y resaltado en azul) en la ventana emergente de información situada encima del escáner.</p>
<img alt="Aviso de datos de demostración en la pantalla principal de la aplicación Código de barras." class="align-center" src="../../../../_images/transfers-scratch-demo-data.png"/>
</div>

Para hacerlo, vaya a la aplicación Código de barras, donde verá una pantalla
en la que se le presentarán diversas opciones.

Si está usando un lector de código de barras de USB o bluetooth, puede
escanear el código de barras del producto desde esta pantalla.

Cuando utilice un teléfono inteligente como escáner de códigos de barras, haga
clic en el botón **Toque para escanear** (junto al icono de la cámara, en el
centro de la pantalla). Esto abre una pantalla emergente de **lector de código
de barras** que activa la cámara del dispositivo que se está utilizando.

Dirija la cámara hacia el código de barras impreso del tipo de operación para
escanearlo. Al hacerlo, se procesa el código de barras y se accede a una
pantalla de transferencia de códigos de barras.

Desde esta pantalla, se muestra un resumen de todos los productos a procesar
dentro de esa transferencia interna específica (**WH/INT/000XX**). Sin
embargo, dado que se trata de una nueva transferencia creada desde cero, no
debería haber ningún producto listado en la página.

Para añadir productos, escanee el código de barras del producto. Si el código
de barras no está disponible, introduzca manualmente el producto en el sistema
haciendo clic en el botón **Agregar producto** de la parte inferior de la
pantalla, y añada los productos y las cantidades de productos que deben
transferirse.

Una vez que esté listo, haga clic en **Confirmar** para confirmar los cambios
realizados en la línea de producto.

![Editor del producto en blanco en una transferencia interna desde
cero.](../../../../_images/transfers-scratch-blank-product-editor.png)

Después, desde la página de resumen con todos los productos para procesar
dentro de esa transferencia (**WH/INT/000XX**) y haga clic en **Validar**. Ya
procesó la transferencia interna y puede cerrar la aplicación _Código de
barras_.

