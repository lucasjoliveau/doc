# Dividir y fusionar órdenes de fabricación

También en la aplicación _fabricación_ es posible crear órdenes de fabricación
para una sola unidad de un artículo o varias unidades del mismo artículo.
Puede que en algunos casos se necesite dividir una orden de fabricación que
contenga varias unidades en dos o más órdenes, o fusionar dos o más órdenes en
una sola orden.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Una orden de fabricación solo puede contener una unidad de producto, o varias unidades de un solo producto que utilicen las mismas listas de materiales. Como resultado, solo es posible fusionar órdenes de fabricación si cada orden contiene el mismo producto que está fabricando con la misma lista de materiales.</p>
</div>

## Dividir órdenes de fabricación

Si desea dividir una orden de fabricación en varias órdenes, vaya a
Fabricación ‣ Operaciones ‣ Órdenes de fabricación, seleccione una orden de
fabricación. En la parte superior de la página, junto al botón **Nuevo** ,
aparecerá el número de referencia de la orden de fabricación con un botón **⚙️
(configuración)** a su lado.

Haga clic en el botón **⚙️ (configuración)** para abrir la configuración
general de la orden de fabricación, luego seleccione **dividir**.

![Los botones configuración y dividir en una orden de
fabricación.](../../../../_images/settings-split.png)

Después de seleccionar **dividir** , aparecerá una ventana emergente llamada
**dividir producción**. En el campo **dividir en #** ingrese el número de
órdenes de fabricación en las que se debe dividir la orden original, luego
haga clic fuera del campo. Aparecerá una tabla con líneas para cada nueva
orden de fabricación que se creará mediante la división. Deberá ingresar el
número de unidades que se asignarán a cada nueva orden de fabricación en la
columna **cantidad a producir**. Por último, haga clic en **dividir** para
dividir la orden de fabricación.

![La ventana emergente "Dividir producción" para una orden de
fabricación.](../../../../_images/split-production-window.png)

Después de hacer clic en **dividir** , la orden de fabricación original se
dividirá en el número de órdenes que se especificó en el campo **dividir en
#**. Los números de referencia para las nuevas órdenes de fabricación son el
número de referencia de la orden original más las etiquetas _-###_ al final.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>La orden de fabricación <em>WH/MO/00012</em> está dividida en tres órdenes separadas. Los números de referencia para las nuevas órdenes son <em>WH/MO/00012-001</em>, <em>WH/MO/00012-002</em> y <em>WH/MO/00012-003</em>.</p>
</div>

## Fusionar órdenes de fabricación

Si desea fusionar dos o más órdenes de fabricación en una sola orden, vaya a
Fabricación ‣ Operaciones ‣ Órdenes de fabricación. Seleccione las órdenes de
fabricación a fusionar mediante la casilla de verificación a la izquierda del
nombre de cada orden.

![Seleccione las órdenes de fabricación a fusionar mediante las casillas de
verificación de cada una.](../../../../_images/select-orders.png)

Una vez que seleccione todas las órdenes de fabricación, hag clic en el botón
**acciones** en la parte superior de la página, luego seleccione **fusionar**
en el menú desplegable.

![Los botones de acción y fusión en la página de órdenes de
fabricación.](../../../../_images/actions-merge.png)

Las órdenes de fabricación seleccionadas se fusionan en una sola orden. El
número de referencia para la nueva orden de fabricación es el siguiente número
secuencial que _no_ se ha asignado previamente a una orden.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>El último número de referencia utilizado para una orden de fabricación fue <em>WH/MO/00012</em>. Se fusionan dos órdenes de fabricación, <em>WH/MO/00008</em> y <em>WH/MO/00009</em>, en una sola orden. El número de referencia para la orden de fabricación creada por la fusión es <em>WH/MO/00013</em>.</p>
</div>

Puede ver los los números de referencia de las órdenes de fabricación que se
fusionaron en el campo **origen** de la orden de fabricación creada por la
fusión.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Las órdenes de fabricación <em>WH/MO/00009</em> y <em>WH/MO/00010</em> se fusionan para crear <em>WH/MO/00011</em>. El campo de origen para <em>WH/MO/00011</em> lista tanto <em>WH/MO/00009</em> como <em>WH/MO/00010</em>.</p>
</div>

