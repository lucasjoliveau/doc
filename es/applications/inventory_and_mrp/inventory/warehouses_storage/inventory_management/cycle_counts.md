# Conteo por ciclos

Para la mayoría de las empresas solo es necesario contar el inventario una vez
al año. Así que luego de hacer un _ajuste de inventario_ en Konvergo ERP, la fecha del
próximo conteo se programará de forma predeterminada para el 31 de diciembre
del año en curso.

Sin embargo, para algunas empresas es esencial contar con un conteo de
inventario correcto en todo momento. Estas empresas usan _recuentos cíclicos_
para mantener los niveles de inventario importantes actualizados. El recuento
cíclico es un método que las empresas usan para contar su inventario más
seguido en algunas _ubicaciones_ para asegurarse de que el inventario físico
va con los registros de su inventario.

## Activar ubicaciones de inventario

En Konvergo ERP, los recuentos cíclicos se realizan según la ubicación. Por eso
necesita activar la función _ubicaciones de inventario_ antes de realizar un
recuento cíclico.

Para activar esta función, vaya a la aplicación Inventario ‣ Configuración ‣
Ajustes y baje a la sección **Almacén**. Haga clic en la casilla de
verificación junto a **Ubicaciones de almacenamiento** y guarde los cambios.

![Imagen donde se muestra la función ubicaciones de almacenamiento activada en
los ajustes de inventario. ](../../../../../_images/cycle-counts-enabled-
setting.png)

## Cambiar la frecuencia del recuento de inventario por ubicación

Ya que activó la función ubicaciones de almacenamiento, puede cambiar la
frecuencia del recuento de inventario dependiendo de las ubicaciones
específicas que se crear en un almacén.

Para ver y editar ubicaciones, vaya a la aplicación Inventario ‣ Configuración
‣ ubicaciones. Esto le mostrará la página de **Ubicaciones** donde están todas
las ubicaciones que se crearon y se enlistaron dentro del almacén.

Desde esta página, haga clic en una ubicación para mostrar la página de
ajustes e esa ubicación en específico. Haga clic en **Editar** para editar los
ajustes de la ubicación.

En la sección **Conteo cíclico** ubique el campo **Frecuencia de inventario
(días)** , que debería estar configurado a `0` (si no se ha editado la
ubicación antes). En este campo cambie el valor a cualquier número de días que
quiera.

![Ajuste de frecuencia en la ubicación.](../../../../../_images/cycle-counts-
location-frequency.png) <div class="alert alert-success">
<p class="alert-title">
Example</p><p>Una ubicación que necesita un recuento de inventario cada 30 días debe tener el valor de <b>Frecuencia de inventario (días)</b> en 30.</p>
</div>

Ya que se cambió la frecuencia al número de días deseados, haga clic en
**Guardar** para guardar los cambios. Ahora, cuando se aplique un ajuste de
inventario en esta ubicación, la siguiente fecha de recuento programada se
configurará en automático, según el valor que se ingresó en el campo
**Frecuencia de inventario (días)**.

## Recuento de inventario por ubicación

Para realizar un recuento cíclico en una ubicación en específico dentro de un
almacén, vaya a la aplicación de Inventario ‣ Operaciones ‣ Ajustes de
inventario. Se le redirigirá a una página de **ajustes de inventario** que
contenga todos los productos que están en existencias actualmente, con cada
producto enlistado en cada línea.

Desde esta página puede usar los botones **Filtros** y **Agrupar por** (que se
encuentran en la parte superior de la página, debajo de la barra **Buscar…**)
para seleccionar ubicaciones específicas y realizar recuentos de inventario.

![Página de ajustes de inventario. ](../../../../../_images/cycle-counts-
inventory-adjustments-page.png)

Para seleccionar una ubicación específica y ver todos los productos dentro de
esa ubicación, haga clic en **Agrupar por** y luego en **Agregar un grupo
específico** para mostrar un nuevo menú desplegable a la derecha.

Haga clic en **Ubicación** en el menú desplegable y después en **Aplicar**.
Ahora podrá ver menús desplegables condensados para cada ubicación en el
almacén que tenga productos en existencia. Podrá realizar el recuento cíclico
para todos los productos de esa ubicación.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>En almacenes grandes que tengan varias ubicaciones y un gran número de productos, es probable que sea más fácil buscar la ubicación específica que quiere. Para hacer esto, desde la página <b>Ajustes de inventario</b> haga clic en <b>Filtros</b>. Haga clic en <b>Agregar filtro personalizado</b> para mostrar un nuevo menú en la parte derecha. Si hace clic en este menú, se mostrarán tres menús desplegables.</p>
<p>Para el primer campo, haga clic y seleccione <b>Ubicación</b> en el menú desplegable. Para el segundo campo, deje el valor <b>contiene</b> tal cual está. Para el tercer campo, escriba el nombre de la ubicación que está buscando. Haga clic en <b>Aplicar</b> para que esa ubicación aparezca en la página.</p>
</div> ![Imagen en la que se muestran los filtros aplicados así
como la opción agrupar por en la página de ajustes.
](../../../../../_images/cycle-counts-filters.png)

## Cambiar la frecuencia de los recuentos de todo el inventario

Usualmente los recuentos cíclicos se realizan por ubicación, pero la fecha
programada para hacer un recuento de todo el inventario dentro de un almacén
también se puede cambiar de manera manual para que la fecha sea antes de la
que se muestra.

Para modificar la fecha planeada predeterminada vaya a Inventario ‣
Configuración ‣ Ajustes. Diríjase a la sección **Operaciones** y busque el
campo **Día y mes del inventario anual** , este incluye un campo desplegable
que de forma predeterminada está configurado con el `31` de **diciembre**.

![Imagen que muestra el campo frecuencia en los ajustes de la aplicación
Inventario. ](../../../../../_images/cycle-counts-frequency-settings.png)

Para cambiar el día, haga clic en el `31` y cámbielo a un día que entre en el
rango `1-31`, según el mes del año que desea.

Para cambiar el mes haga clic en **December** y podrá ver el menú desplegable
con los meses.

Ya que realizó todos los cambios, guárdelos.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="count_products">Ajustes de inventario</a></p>
</div>

