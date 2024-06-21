# Conectar una impresora

La instalación de una impresora se puede hacer en unos cuantos pasos muy
fáciles. La impresora se puede usar para imprimir recibos, etiquetas, órdenes
o incluso reportes de diferentes aplicaciones de Konvergo ERP. Además, puede asignar
las acciones de una impresora como _acciones en un activador_ durante los
procesos de fabricación, o agregarlas a un punto de control o revisión de
calidad.

## Conexión

La Caja IoT es compatible con impresoras que se conectan a través de un puerto
USB, una red inalámbrica o Bluetooth. [Las impresoras
compatibles](https://www.odoo.com/page/iot-hardware) se detectan
automáticamente y aparecen en la lista de **Dispositivos** de la aplicación
_IoT_.

![Una impresora como aparecería en la lista de dispositivos de la aplicación
IoT. ](../../../../_images/printer-detected.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Es posible que la impresora tarde un par de minutos en aparecer en la lista de dispositivos en la aplicación <em>IoT</em>.</p>
</div>

## Vincular una impresora

### Vincular una impresora a las órdenes de trabajo

Puede vincular _órdenes de trabajo_ a las impresoras a través de un punto de
control de calidad para imprimir las etiquetas de los productos fabricados.

En la aplicación _Calidad_ , puede configurar un dispositivo en un punto de
control de calidad. Para hacerlo, vaya a la aplicación Calidad ‣ Control de
calidad ‣ Puntos de control, y abra el punto de control deseado al que estará
vinculada la impresora.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Debe adjuntar una <em>Operación de fabricación</em> y una <em>Operación de una orden de trabajo</em> a un punto de control de calidad antes de que el campo <b>Tipo</b> le muestre disponible la opción <b>Imprimir etiqueta</b>.</p>
</div>

Luego, edite el punto de control seleccionando el campo **Tipo** y haciendo
clic en **Imprimir etiqueta** en el menú desplegable de opciones. Al hacerlo,
aparecerá un campo llamado **Dispositivo** , donde podrá seleccionar el
_dispositivo_ que adjunto. **Guarde** los cambios.

![Esta es la configuración del punto de control de
calidad.](../../../../_images/printer-controlpoint.png)

Ahora podrá usar la impresora con el punto de control de calidad seleccionado.
Cuando el proceso de fabricación llegue al punto de control de calidad, la
base de datos le mostrará la opción de imprimir las etiquetas para un producto
en específico.

![../../../../_images/printer-prompt.png](../../../../_images/printer-
prompt.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>También puede acceder a los puntos de control de calidad en la aplicación IoT ‣ Dispositivos, y seleccionar el dispositivo. Hay una pestaña de <b>Puntos de control de calidad</b> donde se pueden agregar con el dispositivo.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>En un formulario detallado de una revisión de calidad, el <b>Tipo</b> de revisión se puede especifica en <b>Imprimir etiqueta</b>. Para crear nuevas revisiones de calidad, vaya a la aplicación Calidad ‣ Control de calidad ‣ Revisiones de calidad ‣ Nuevo.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../../../inventory_and_mrp/quality/quality_management/quality_control_points">Puntos de control de calidad</a></p></li>
<li><p><a href="../../../inventory_and_mrp/quality/quality_management/quality_alerts">Crear alertas de calidad</a></p></li>
</ul>
</div>

### Vincule una impresora a un centro de trabajo en la aplicación Fabricación

Para vincular una impresora a una acción, primero necesita configurarla en un
centro de trabajo. Vaya a la aplicación Fabricación ‣ Configuración ‣ Centros
de trabajo. Luego, seleccione el centro de trabajo que desee en donde se usará
la impresora. Agregue el dispositivo a la pestaña de **Activadores de IoT** en
la columna de **Dispositivo** haciendo clic en **Agregar una línea**.

Puede vincular la impresora a una de las siguientes opciones que aparecen en
el menú desplegable de **Acciones** : **Imprimir etiquetas** , **Imprimir
operación** , o **Imprimir recibo de envío**. También puede agregar una clave
para activar la acción.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Tenga en cuenta que se elije el primer activador en la lista. El orden de los activadores es importantes y puede arrastrarlos en el orden que desee.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>En la pantalla de <b>Orden de trabajo</b>, un estado gráfico indica si la base de datos está conectada de forma adecuada a la impresora.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../../../inventory_and_mrp/manufacturing/management/using_work_centers#workcenter-iot"><span class="std std-ref">Integración de dispositivos IoT</span></a></p>
</div>

### Vincular impresora a los reportes

También puede vincular un tipo de reporte a una impresora específica. En la
aplicación _IoT_ , vaya al menú **Dispositivos** y seleccione la impresora que
desea configurar.

Después, haga clic en **Editar** , vaya a la pestaña **Reportes de la
impresora** y haga clic en **Agregar una línea**. En la ventana emergente,
seleccione todos los tipos de **Reportes** que deben estar vinculados a esta
impresora.

![Los dispositivos de impresora enlistadas en el menú de dispositivos de IoT.
](../../../../_images/printers-listed.png)

Ahora, cada vez que seleccione **Imprimir** en el panel de control, en lugar
de descargar un PDF, aparecerá una ventana emergente con todas las impresoras
vinculadas al reporte. Luego, Konvergo ERP enviará el reporte a las impresoras
seleccionadas y lo imprimirá en automático.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../../../sales/point_of_sale/restaurant/kitchen_printing">Imprimir órdenes en el PdV</a></p>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>También puede configurar los reportes en el <b>Menú técnico</b> en el <a href="../../developer_mode#developer-mode"><span class="std std-ref">modo debug</span></a>. Para ello, vaya a la aplicación  Ajustes ‣ Menú técnico ‣ Acciones ‣ Reportes. Aquí podrá encontrar el reporte individual en la lista, dónde puede configurar un <b>Dispositivo IoT</b> en el reporte.</p>
</div>

