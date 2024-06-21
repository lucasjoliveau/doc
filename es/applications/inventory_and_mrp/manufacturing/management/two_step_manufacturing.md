# Fabricación en dos pasos

La aplicación _Fabricación_ permite que los usuarios fabriquen productos en
tan solo uno, dos o tres pasos. Si utiliza la fabricación en dos pasos, Konvergo ERP
crea una orden de fabricación y un traslado de componentes, pero no genera un
traslado para el movimiento de los productos terminados al inventario. El
inventario se actualiza según la cantidad de productos fabricados, pero no se
realiza un seguimiento del traslado hacia y desde el inventario.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>El número de pasos utilizados en la fabricación se establece a nivel de almacén, esto permite que cada almacén utilice un número diferente de pasos. Si desea cambiar el número de pasos utilizado para un almacén específico, vaya a Inventario ‣ Configuración ‣ Almacenes y seleccione un almacén de la pantalla <b>Almacenes</b>.</p>
<p>En la pestaña <b>configuración del almacén</b>, vaya al campo de entrada guilabel:<code>Fabricación</code> y seleccione una de las tres opciones: <b>Fabricación (1 paso)</b>, <b>Elegir componentes y luego fabricar (2 pasos)</b>, o <b>Elegir componentes, fabricar y luego almacenar los productos (3 pasos)</b>.</p>
<img alt="El campo de entrada Fabricación en una página de configuración de almacén." class="align-center" src="../../../../_images/manufacturing-type2.png"/>
</div> <div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Debe configurar los productos correctamente antes de fabricarlos. Si desea obtener más información sobre cómo hacerlo, consulte la documentación sobre cómo <a href="configure_manufacturing_product#manufacturing-management-configure-manufacturing-product"><span class="std std-ref">configurar un producto para la fabricación</span></a>.</p>
</div>

## Crear una orden de fabricación

Si desea fabricar un producto en la aplicación de Konvergo ERP _Fabricación_ , vaya a
Fabricación ‣ Operaciones ‣ Órdenes de fabricación, y haga clic en **Nuevo**
para crear una nueva |orden de fabricación|.

En la nueva orden de fabricación, seleccione el producto a producir del menú
desplegable **producto**. El campo **lista de materiales** se autocompletará
con la lista de materiales asociada.

Si tiene un producto con más de una |lista de materiales| configurada, puede
seleccionar la |lista de materiales| específica en el campo **lista de
materiales** , y el campo **producto** se completa automáticamente con el
producto asociado.

Después de haber seleccionado una |lista de materiales|, las pestañas
**componentes** y **órdenes de trabajo** se completan de forma automática con
los componentes y operaciones especificados en la |lista de materiales|. Si
necesita agregar componentes u operaciones a la |lista de materiales| que esté
configurando, hágalo en las pestañas **componentes** y **órdenes de trabajo**
mediante el botón **agregar una línea**.

Por último, **confirme** la lista de materiales.

## Proceso de traslado de componentes de recolección

Después de confirmar una orden de fabricación de dos pasos, aparecerá un botón
inteligente para **traslados** en la parte superior de la página. Haga clic
para abrir el traslado de componentes seleccionados para la orden de
fabricación. Este traslado se utiliza para rastrear el movimiento de los
componentes desde los lugares donde se almacenan hasta el lugar donde se
utilizan para fabricar el producto.

Después de trasladar los componentes fuera de su ubicación de almacenamiento,
haga clic en **Validar** en la parte superior del traslado, luego presione
**Aplicar** en la ventana emergente **Traslado inmediato** que aparece. Al
hacerlo, se marca el traslado como **hecho** y se actualiza el inventario de
forma que refleje la cantidad de componentes trasladados.

Por último, regrese a la orden de fabricación mediante el enlace
**WH/MO/XXXXX** en la parte superior de la página.

![La orden de fabricación en un traslado de
componentes.](../../../../_images/mo-bread-crumb1.png)

## Proceso de orden de fabricación

Una orden de fabricación se procesa al completar todas las órdenes de trabajo
enumeradas en la pestaña **órdenes de trabajo**. Esto se puede hacer desde la
orden de fabricación o desde la vista de la tableta de órdenes de trabajo.

### Flujo básico

Si desea completar las órdenes de trabajo desde la orden de fabricación vaya a
Fabricación ‣ Operaciones ‣ Órdenes de fabricación y seleccione una orden de
fabricación.

Desde la página la de orden de fabricación seleccione la pestaña **órdenes de
trabajo**. Una vez que comience el trabajo en la primera orden de trabajo a
completar, haga clic en el botón **iniciar**. La aplicación _Fabricación_
inicia un temporizador que registra cuánto tiempo tarda en completar la orden
de trabajo.

![El botón de inicio para una orden de trabajo en una orden de
fabricación.](../../../../_images/start-button1.png)

Cuando se complete la orden de trabajo, haga clic en el botón **Hecho** para
esa orden de trabajo. Repita el mismo proceso para cada orden de trabajo
enumerada en la pestaña **órdenes de trabajo**.

![El botón "hecho" para una orden de trabajo en una orden de
fabricación.](../../../../_images/done-button2.png)

Una vez que completó todas las órdenes de trabajo, haga clic en **producir
todo** en la parte superior de la pantalla para marcar la orden de fabricación
como **hecha** y registrar los producto fabricado en inventario.

### Flujo en vista de tableta

Si desea completar las órdenes de trabajo para una orden de fabricación desde
la vista de tableta, vaya a Fabricación ‣ Operaciones ‣ Órdenes de
fabricación, y seleccione una orden de fabricación.

Ahora haga clic en la pestaña **órdenes de trabajo** y seleccione el botón **📱
(tableta)** en la línea de la primera orden de trabajo que se vaya a procesar.
Esto abrirá la vista de la tableta.

![El botón de vista de tableta para una orden de trabajo en una orden de
fabricación.](../../../../_images/tablet-view-button3.png)

Una vez que abra la vista de la tableta, la aplicación _Fabricación_ iniciará
automáticamente un temporizador que lleva un registro de cuánto tiempo falta
para completar la orden de trabajo. Después de completar la orden de trabajo,
haga clic en el botón **marcar como hecho** en la esquina superior derecha de
la vista de la tableta.

Si hace clic en **Marcar como hecho** con al menos una orden de trabajo por
completar, se abrirá una página que lista la siguiente orden de trabajo. Haga
clic en esa orden de trabajo para abrirla en la vista de tableta.

Una vez que termine la orden de trabajo final para la orden de fabricación,
aparecerá un botón **Marcar como hecho y cerrar orden de fabricación** en la
vista de la tableta además del botón **Marcar como Hecho**. Haga clic en
**Marcar como hecho y cerrar orden de fabricación** para marcar la orden de
fabricación como **hecha** y registrar los productos fabricados en el
inventario.

También puede completar la operación final con la orden de fabricación
abierta, solo debe hacer clic en **marcar como hecho**. Si desea hacerlo así,
podrá cerrar la orden de fabricación más tarde haciendo clic en el botón
**producir todo**.

