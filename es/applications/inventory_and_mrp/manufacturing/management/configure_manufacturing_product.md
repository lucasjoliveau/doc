# Configuración del producto a fabricar

Para fabricar un producto con la aplicación _Fabricación_ de Konvergo ERP, el producto
debe estar configurado de forma correcta. Esto consiste en habilitar la ruta
_Fabricación_ y configurar una lista de materiales (LdM) para el producto. Una
vez que haya completado estos pasos, puede seleccionar el producto al crear
una nueva orden de fabricación.

## Activar la ruta de fabricación

La ruta de fabricación se activa para cada producto desde su propia página.
Vaya a Fabricación ‣ Productos ‣ Productos y seleccione un producto existente
o cree uno **nuevo** con el botón correspondiente.

En la página del producto, seleccione la pestaña **Inventario** y active la
casilla **Fabricación** en la sección **Rutas**. Esto le indica a Konvergo ERP que el
producto se puede fabricar.

![La ruta de fabricación en la pestaña Inventario en la página de un
producto.](../../../../_images/manufacturing-route.png)

## Configurar una lista de materiales (LdM)

A continuación, debe configurar una lista de materiales (LdM) para el producto
para que Konvergo ERP sepa cómo se fabrica. Una LdM es una lista de los componentes y
operaciones que se necesitan para fabricar un producto.

Para crear una LdM para un producto específico, vaya a Fabricación ‣ Productos
‣ Productos y seleccione el producto. En la página del producto, haga clic en
el botón inteligente **Lista de materiales** en la parte superior de la
página, luego seleccione **Nuevo** para configurar una nueva LdM.

![El botón inteligente de lista de materiales en la página de un
producto.](../../../../_images/bom-smart-button1.png)

En |a LdM, el campo **Producto** se completa en automático. Especifique el
número de unidades que produce la LdM en el campo **Cantidad**.

Para agregar un componente a la LdM seleccione la pestaña **Componentes** y
haga clic en **Agregar una línea** , elija un componente del menú desplegable
**Componente** y escriba la **cantidad** en el campo correspondiente. Continúe
agregando componentes en nuevas líneas hasta que haya terminado de incluir
todos.

![La pestaña Componentes en una lista de
materiales.](../../../../_images/components-tab.png)

A continuación, seleccione la pestaña **Operaciones** , haga clic en **Agregar
una línea** y aparecerá la ventana emergente **Crear operaciones**.
Especifique el nombre de la **operación** a agregar (por ejemplo, ensamblaje,
corte, etc.) en el campo correspondiente y, en el menú desplegable **Centro de
trabajo** , seleccione el lugar donde se realizará la operación. Por último,
haga clic en **Guardar y cerrar** para terminar de agregar operaciones o en
**Guardar y crear nuevo** para agregar más.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>La pestaña <b>Operaciones</b> solo aparece si la función <b>Órdenes de trabajo</b> está activada. Vaya a Fabricación ‣ Configuración ‣ Ajustes y seleccione la casilla <b>Órdenes de trabajo</b>.</p>
</div> ![La pestaña Operaciones en una lista de
materiales.](../../../../_images/operations-tab1.png) <div class="admonition-learn-more alert">
<p class="alert-title">
Más información</p><p>La sección anterior proporciona instrucciones para crear una lista de materiales básica que permita fabricar un producto en Konvergo ERP. Sin embargo, no es un resumen exhaustivo de todas las opciones de configuración disponibles. Para obtener más información sobre las listas de materiales, consulte la documentación sobre cómo  <a href="bill_configuration#manufacturing-management-bill-configuration"><span class="std std-ref">crear una lista de materiales</span></a>.</p>
</div>

