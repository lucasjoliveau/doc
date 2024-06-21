# Dependencias de la orden de trabajo

En algunas ocasiones puede ser necesario completar operaciones específicas
antes de empezar con otras. Con el objetivo de asegurar que las operaciones se
lleven a cabo en el orden correcto, _Fabricación_ cuenta con una configuración
de _dependencias de orden de trabajo_. Esta configuración permite _bloquear_
ciertas operaciones de una lista de materiales para permitir realizar otras
operaciones primero.

## Configuración

La configuración de las _dependencias de las órdenes de trabajo_ no está
disponible de forma predeterminada. Si desea activarla, vaya a Fabricación ‣
Configuración ‣ Ajustes y habilite la configuración **órdenes de trabajo** ,
si aún no está activa.

Una vez que habilite la configuración **órdenes de trabajo** , podrá ver la
configuración **dependencias de órdenes de trabajo** debajo de ella. Habilite
las **dependencias de órdenes de trabajo** , y no olvide hacer clic en
**guardar** para confirmar los cambios.

## Añadir dependencias a la lista de materiales

Las dependencias de la orden de trabajo se configuran en la lista de
materiales de un producto. Para hacerlo, vaya a Fabricación ‣ Productos ‣
Listas de materiales, seleccione una lista de materiales o cree una nueva
haciendo clic en **nuevo**.

<div class="admonition-learn-more alert">
<p class="alert-title">
Más información</p><p>Si desea obtener una guía completa sobre cómo configurar correctamente una nueva lista de materiales, consulte la documentación sobre la <a href="bill_configuration#manufacturing-management-bill-configuration"><span class="std std-ref">creación de una lista de materiales</span></a>.</p>
</div>

Si desea obtener la opción **Bloqueado por** en la configuración de la pestaña
**Operaciones** , vaya a la lista de materiales, haga clic en la pestaña
**varios** , active la casilla de verificación **dependencias de operación**.

![La casilla de dependencias de operación en la pestaña "varios" de una lista
de materiales.](../../../../_images/operation-dependencies.png)

A continuación, haga clic en la pestaña **Operaciones**. En la parte superior
derecha de la pestaña, haga clic en el botón de **ajustes** y active la
casilla **bloqueado por**. Al hacer esto, aparecerá el campo **bloqueado por**
para cada operación en la pestaña :guilabel: `operaciones`.

![La configuración de la pestaña operaciones en una lista de
materiales.](../../../../_images/operations-settings.png)

En la línea de la operación que se debe bloquear por otra operación, haga clic
en el campo **bloqueado por** , al hacer esto aparecerá una ventana emergente
llamada **abrir: operaciones**. En el campo desplegable **bloqueado por** de
la ventana emergente, seleccione la operación de bloqueo que se debe completar
_antes_ que la operación bloqueada.

![El campo desplegable "bloqueado por" de una operación en una lista de
materiales.](../../../../_images/blocked-by.png)

Por último, no olvide guilabel:`guardar` la lista de materiales.

## Planificar órdenes de trabajo con dependencias

Una vez que haya configurado las dependencias de la orden de trabajo en una
LdM, la aplicación _Fabricación_ podrá planificar cuándo se programarán las
órdenes de trabajo según sus dependencias. Si desea planificar las órdenes de
trabajo de una orden de fabricación, vaya a Fabricación ‣ Operaciones ‣
Órdenes de fabricación.

Después seleccione una orden de fabricación para un producto con dependencias
de órdenes de trabajo establecidas en su LdM. También puede crear una nueva
orden de fabricación, solo debe hacer clic en **nuevo**. Si decide crear una
nueva orden de fabricación, seleccione una LdM configurada con dependencias de
órdenes de trabajo en el campo desplegable **lista de materiales** y haga clic
en **confirmar**.

Después de confirmar la orden de fabricación, seleccione la pestaña **órdenes
de trabajo** para ver las órdenes de trabajo necesarias para completarla.
Cualquier orden de trabajo que no esté bloqueada por otra orden de trabajo
mostrará una etiqueta que diga `listo` como **estado**.

Las órdenes de trabajo que están bloqueadas por una o más órdenes de trabajo
muestran una etiqueta llamada `en espera de otra orden de trabajo` . Una vez
que se completen las órdenes de trabajo que las bloquean, la etiqueta se
actualizará a `listo`.

![Las etiquetas de estado para las órdenes de trabajo en una orden de
fabricación.](../../../../_images/work-order-status.png)

Si desea programar las órdenes de trabajo de la orden de fabricación, haga
clic en el botón **Plan** en la parte superior de la página. Al hacerlo, podrá
ver cómo se completa automáticamente el campo **fecha de inicio programada**
de cada orden de trabajo en la pestaña **órdenes de trabajo** con la fecha y
hora de inicio programadas. Una orden de trabajo bloqueada se programa al
final del período de tiempo especificado en el campo **Duración esperada** de
la orden de trabajo que la precede.

![El campo "fecha de inicio programada" de las órdenes de trabajo en una orden
de fabricación.](../../../../_images/scheduled-start-date.png)
<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Se crea una orden de fabricación para el Producto A. La orden de fabricación tiene dos operaciones: cortar y ensamblar. Cada operación tiene una duración esperada de 60 minutos, y la operación ensamblar está bloqueada por la operación cortar.</p>
<p>Se hice clic en el botón <b>plan</b> de la orden de producción a las 13:30 y se programa el inicio inmediato de la operación corte. Dado que la operación corte tiene una duración prevista de 60 minutos, la operación de ensamblaje está programada para comenzar a las 14:30.</p>
</div>

### Planeación por centro de trabajo

Si desea ver una representación visual de cómo se planifican las órdenes de
trabajo, vaya a la página **planeación de órdenes de trabajo** en Fabricación
‣ Planeación ‣ Planeación por centro de trabajo. Esta página muestra una línea
de tiempo de todas las órdenes de trabajo programadas para cada operación.

Si una orden de trabajo está bloqueada por la finalización de otra, la orden
de trabajo bloqueada se mostrará como programada para comenzar después de la
orden de trabajo que la bloquea. Además, una flecha conecta las dos órdenes de
trabajo, que va de la operación de bloqueo a la operación bloqueada.

![La flecha que conecta una orden de trabajo bloqueada con la orden de trabajo
que la bloquea.](../../../../_images/planning-arrow.png)

