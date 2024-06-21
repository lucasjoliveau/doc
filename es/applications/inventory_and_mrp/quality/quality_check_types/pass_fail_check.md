# Control de calidad tipo aprueba o falla

En la aplicación _Calidad_ de Konvergo ERP, uno de los tipos de control de calidad que
puede seleccionar al crear un nuevo punto de control de calidad es _Aprobar -
Fallar_. Los controles tipo _Aprobar - Fallar_ consisten en un campo de
entrada de texto que permite que la persona que lo realiza proporcione
criterios específicos que un producto debe cumplir para poder cumplir con el
control.

## Crear un control de calidad tipo Aprobar - Fallar

Hay dos formas en las que puede crear un punto de control de calidad de tipo
_Pasa - Falla_. Puede crear un control de calidad de manera manual o puede
configurar un punto de control de calidad para crear controles en automático
en un intervalo predeterminado.

Esta documentación solo incluye información sobre las opciones de
configuración pertenecientes a los controles y puntos de control de calidad de
tipo _Aprueba - Falla_. Si desea obtener un resumen completo de todas las
opciones de configuración disponibles al crear un control de calidad o puntos
de control de calidad, consulte la documentación sobre [controles de
calidad](../quality_management/quality_checks#quality-quality-management-
quality-checks) y [puntos de control de
calidad](../quality_management/quality_control_points#quality-quality-
management-quality-control-points).

### Control de calidad

Para crear un solo control de calidad tipo _Aprobar - Fallar_ , vaya a Calidad
‣ Control de calidad ‣ Controles de calidad y haga clic en **Nuevo**. Llene el
nuevo formulario de control de calidad como se indica aquí:

  * En el campo desplegable **Tipo** seleccione **Aprobar - Fallar**.

  * En el campo desplegable **Equipo** seleccione el equipo de control de calidad responsable por este control.

  * En el campo de texto **Instrucciones** de la pestaña **Notas** escriba las instrucciones sobre los criterios que se deben de cumplir para pasar el control de calidad.

![Un ejemplo de un control de calidad configurado para un tipo de control de
calidad Aprobar - Fallar.](../../../../_images/quality-check-form.png)

### Punto de control de calidad

Para crear un punto de control de calidad que genere controles de calidad de
tipo _Aprueba - Falla_ de forma automática, vaya a Calidad ‣ Control de
calidad ‣ Puntos de control y haga clic en **Nuevo**. Complete el formulario
del nuevo punto de control de calidad de la siguiente forma:

  * En el campo desplegable **Tipo** seleccione **Aprobar - Fallar**.

  * En el campo desplegable **Equipo** seleccione al equipo de calidad responsable de gestionar los controles creados por el punto de control de calidad.

  * En el campo de texto **Instrucciones** escriba las instrucciones sobre los criterios que se deben de cumplir para pasar el control de calidad.

![Un ejemplo de un punto de control de calidad configurado para un control de
calidad tipo Aprobar - Fallar.](../../../../_images/qcp-form.png)

## Control de calidad tipo Aprobar - Fallar

Hay muchas maneras en las que podemos procesar los controles de calidad tipo
_Medidas_. Si asignamos un control de calidad a una orden de fabricación,
inventario o trabajo específico, el control de calidad se puede procesar
directamente en la orden. También es posible procesar un control de calidad
desde la página del control de calidad.

### Desde la página de controles

Para procesar un control de calidad tipo _Medida_ vaya a Calidad ‣ Control de
calidad ‣ Controles de calidad y seleccione un control de calidad. Siga las
**Instrucciones** ver cómo realizar la medida.

Si se cumplen los criterios para pasar el control de calidad, haga clic en el
botón de **Aprobar** ubicado en la esquina superior izquierda de la página. Si
no se cumplen los criterios, haga clic en el botón de **No aprobar**.

### En una orden

Para procesar un control de calidad tipo _Aprobar - Fallar_ seleccione una
orden de fabricación o de inventario (recibo, entrega, devolución, etc.) que
necesita pasar por el control. Para seleccionar las órdenes de fabricación
vaya a Fabricación ‣ Operaciones ‣ Órdenes de fabricación y haga clic en una
orden. Para seleccionar una orden de inventario vaya a Inventario, haga clic
en el botón **# Por procesar** que se encuentra en la tarjeta de operación y
seleccione un orden.

En la orden de inventario o de fabricación seleccionada aparecerá un botón
morado de **Controles de calidad** en la parte superior de la orden. Haga clic
en el botón para abrir la ventana emergente de **Control de calidad** , lo que
mostrará todos los controles de calidad que se requieren para esa orden.

Para procesar el control de calidad tipo _Aprobar - Fallar_ siga las
instrucciones que se muestran en la ventana emergente **Control de calidad**.
Si se cumplen los criterios para el control de calidad, haga clic en el botón
**Aprobar** en la parte inferior de la ventana. Si los criterios no se
cumplen, haga clic en el botón **Fallar**.

![La ventana emergente de un control tipo Aprobar - Fallar en una orden de
fabricación o de inventario.](../../../../_images/pass-fail-check-pop-up.png)

Si se debe de crear una alerta de control de calidad, haga clic en el botón
**Alerta de calidad** que aparece en la parte superior de la orden de
fabricación o inventario después de que se falle el control de calidad. Al
hacer clic en esta botón, se abrirá un formulario nuevo de alerta de calidad
en una nueva página. Para obtener una guía completa sobre cómo llenar un
formulario de control de calidad, vea la documentación en [alertas de
calidad](../quality_management/quality_alerts#quality-quality-management-
quality-alerts).

### En una orden de trabajo

Al configurar un punto de control de calidad que se activa durante la
fabricación, también puede especificar una orden de trabajo en el campo
**Operación de orden de trabajo** del formulario del punto de control de
calidad. Si especifica una orden de trabajo, se creará un control de calidad
de tipo _Aprueba - Falla_ para esa orden de trabajo, no para toda la orden de
fabricación.

Los controles de calidad tipo _aprobar - fallar_ para órdenes de trabajo se
deben procesar desde la vista de tableta. Para hacerlo, primero vaya a
Fabricación ‣ Operaciones ‣ Órdenes de fabricación. Seleccione una orden de
fabricación que incluya una orden de trabajo que requiera un control de
calidad. Para abrir la vista de tableta haga clic en el botón **📱 (tableta)**
en la línea de la orden.

Ya que tenga la vista de tableta abierta, complete los pasos que se enlistan
el lado izquierdo de la pantalla hasta que llegue al paso _Aprobar - Fallar_
del control de calidad. Al llegar al control siga las instrucciones que
aparecen en la parte superior de la página. Si se cumplen los criterios del
control de calidad, haga clic en el botón **Aprobar** que se encuentra en la
parte superior derecha de la pantalla. Si los criterios no se cumplen, haga
clic en el botón **Fallar**.

![Un control de calidad tipo Aprobar - Fallar para una orden de trabajo de
fabricación.](../../../../_images/work-order-pass-fail-check.png)

Si se debe de crear una alerta de control de calidad, haga clic en el botón
**☰ (menú)** que aparece en la vista de tableta y seleccione **Alerta de
calidad** en la ventana emergente **Menú**. Aparecerá una ventana emergente de
**Alertas de calidad**. Para obtener una guía completa sobre cómo llenar un
formulario de control de calidad, vea la documentación en [alertas de
calidad](../quality_management/quality_alerts#quality-quality-management-
quality-alerts).

