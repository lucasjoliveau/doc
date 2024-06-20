# Control de calidad con instrucciones

En la aplicación _Calidad_ de Odoo, uno de los tipos de punto de control de
calidad que se puede seleccionar al crear un nuevo punto de control de calidad
es _Instrucciones_. Los controles tipo _Instrucciones_ consisten en un campo
de entrada de texto que le permite al creador ingresar instrucciones sobre
cómo se debe realizar el control.

Para obtener un resumen de cómo configurar un control de calidad o un punto de
control de calidad, consulte la documentación sobre [controles de
calidad](../quality_management/quality_checks.html#quality-quality-management-
quality-checks) y [puntos de control de
calidad](../quality_management/quality_control_points.html#quality-quality-
management-quality-control-points).

## Procesar un control de calidad de tipo instrucciones

Hay muchas maneras en las que podemos procesar los controles de calidad tipo
_instrucciones_. Si asignamos un control de calidad a una orden de
fabricación, inventario o trabajo específico, el control de calidad se puede
procesar directamente en la orden. También es posible procesar un control de
calidad desde la página del control de calidad.

### Proceso desde la página del control de calidad

Para procesar un control de calidad tipo _Instrucciones_ vaya a Calidad ‣
Control de calidad ‣ Controles de calidad y seleccione un control de calidad.
Siga las Instrucciones para completar el control.

Si un producto pasa el control de calidad, haga clic en Aprobado que se
encuentra en la parte superior derecha del formulario de control de calidad.
Si el producto no pasó la revisión, haga clic en Fallido.

### Procesar control de calidad en una orden

Para procesar un control de calidad tipo _Instrucciones_ seleccione una orden
de fabricación o de inventario (recibo, entrega, devolución, etc.) que
necesita pasar por el control. Para seleccionar las órdenes de fabricación
vaya a Fabricación ‣ Operaciones ‣ Órdenes de fabricación y haga clic en una
orden. Para seleccionar una orden de inventario vaya a Inventario, haga clic
en el botón # Por procesar que se encuentra en la tarjeta de operación y
seleccione un orden.

En la orden de fabricación o inventario seleccionada, aparecerá un botón
morado llamado Controles de calidad en la parte superior de la orden. Haga
clic en el botón para abrir la ventana emergente de Control de calidad, donde
podrá procesar los controles de calidad que se creen para la orden.

![La ventana emergente de Control de calidad en una orden de fabricación o de
inventario.](../../../../_images/quality-check-pop-up.png)

Para completar un control de calidad de _instrucciones_ siga las instrucciones
detalladas en la ventana emergente Control de calidad. Finalmente, haga clic
en Validar para confirmar que se completó el control.

Si encuentra un problema o defecto durante el control de calidad, es posible
que necesite crear una alerta de calidad para notificar al equipo
correspondiente. Para hacerlo, haga clic en el botón Alerta de calidad que
aparece en la parte superior de la orden de fabricación o inventario después
de validar un control de calidad.

Al hacer clic en Alerta de calidad se abrirá un formulario de alerta de
calidad en una nueva página. Para ver una guía completa sobre cómo llenar un
formulario de alerta de calidad, vea la documentación en [alertas de
calidad](../quality_management/quality_alerts.html#quality-quality-management-
quality-alerts).

### Procesamiento de un control de calidad en una orden de trabajo

Al configurar un punto de control de calidad que se activa con una orden de
fabricación, también puede especificar una orden de trabajo en el campo
Operación de orden de trabajo del formulario del punto de control de calidad.
Si especifica una orden de trabajo, se creará un control de calidad llamado
_Instrucciones_ para esa orden de trabajo en específico, en lugar de crearse
para toda la orden de fabricación.

Los controles de calidad configurados para órdenes de trabajo se deben
completar desde la vista de tableta. Para hacerlo, primero vaya a Fabricación
‣ Operations ‣ Órdenes de fabricación. Seleccione una orden de fabricación que
incluya una orden de trabajo que requiera un control de calidad. Para abrir la
vista de tableta haga clic en el botón 📱 (tableta) en la línea de la orden.

Ya que tenga la vista de tableta abierta, complete los pasos que se enlistan
el lado izquierdo de la pantalla hasta que llegue al paso _Instrucciones_ del
control de calidad. Al llegar al control, las instrucciones sobre cómo
completarlo aparecerán en la parte superior de la pantalla. Siga las
instrucciones, después, haga clic en guilabel:`Siguiente` para pasar al
siguiente paso.

![Un control de instrucciones para una orden de
trabajo](../../../../_images/work-order-instructions-check.png)

Si encuentra un problema o defecto durante el control de calidad, es posible
que necesite crear una alerta de calidad para notificárselo al equipo
correspondiente. Para hacerlo, haga clic en el botón ☰ (menú) en la vista de
tableta y después seleccione Alerta de calidad en la ventana emergente Menú.

Al hacer clic en Alerta de calidad se abrirá una ventana emergente de Alerta
de calidad desde la que se puede crear una alerta de calidad. Para ver una
guía completa sobre cómo llenar un formulario de alerta de calidad, vea la
documentación en [alertas de
calidad](../quality_management/quality_alerts.html#quality-quality-management-
quality-alerts).

