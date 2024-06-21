# Conectar una herramienta de medición

Con la caja IoT de Konvergo ERP, puede conectar herramientas de medición a la base de
datos de Konvergo ERP para usarlas en la aplicación _Calidad_ en un punto de calidad o
una revisión de calidad, o para usarlo en un centro de trabajo durante un
proceso de fabricación.

Consulte la lista de dispositivos compatibles aquí: [dispositivos
compatibles](https://www.odoo.com/page/iot-hardware).

## Conectar con una USB

Para agregar un dispositivo conectado por USB, conecte el cable con la caja
IoT y el dispositivo aparecerá en la base de datos de Konvergo ERP.

![Herramienta de medición reconocida por la caja
IoT.](../../../../_images/device-dropdown.png)

## Conectar con Bluetooth

Active la función de Bluetooth en el dispositivo (consulte el manual del
dispositivo para obtener más información) y la caja IoT se conectará
automáticamente al dispositivo.

![Indicador Bluetooth en la herramienta de
medición.](../../../../_images/measurement-tool.jpeg)

## Vincule una herramienta de medición a un punto de control de calidad en el
proceso de fabricación

En la aplicación _Calidad_ un dispositivo se puede configurar en un punto de
control de calidad. Para ello, vaya a Calidad ‣ Control de calidad ‣ Puntos de
calidad, y abra el punto de control deseado al que debe estar vinculada la
herramienta de medición.

Después, edite el punto de control seleccionando el campo **Tipo** y haciendo
clic en **Medición** en el menú desplegable. Al hacerlo, se mostrará un campo
llamado **Dispositivo** donde puede seleccionar el dispositivo adjunto.

Además, puede configurar los campos **Norma** y **Tolerancia**. Si lo
requiere, **Guarde** los cambios.

La herramienta de medición está vinculada al punto de control de calidad
elegido. El valor, que generalmente debe modificar manualmente, se actualiza
de manera automática mientras usa la herramienta.

![Entrada de la herramienta de medición en la base de datos de Konvergo ERP.
](../../../../_images/measurement-control-point.png) <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>También puede acceder a los puntos de control de calidad en la aplicación IoT ‣ Dispositivos, y seleccionar el dispositivo. Hay una pestaña de <b>Puntos de control de calidad</b> donde se pueden agregar con el dispositivo.</p>
</div>
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>En un formulario detallado de una revisión de calidad, el  <b>Tipo</b> de revisión se puede especificar en  <b>Medición</b>. Acceda a una nueva página de detalles del control de calidad en la aplicación Calidad ‣ Control de calidad ‣ Revisiones de calidad ‣ Nuevo.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../../../inventory_and_mrp/quality/quality_management/quality_control_points">Puntos de control de calidad</a></p></li>
<li><p><a href="../../../inventory_and_mrp/quality/quality_management/quality_alerts">Crear alertas de calidad</a></p></li>
</ul>
</div>

## Vincular una herramienta de medición a un centro de trabajo en la
aplicación Fabricación

Para vincular una herramienta de medición a una acción, primero necesita
configurarla a un centro de trabajo. Para ello, vaya a a Fabricación ‣
Configuración ‣ Centros de trabajo. Luego, seleccione el centro de trabajo
deseado en el que usará la herramienta de medición.

En la página del centro de trabajo, agregue el dispositivo en la pestaña
**Activadores IoT** en la columna **Dispositivo** seleccionando **Agregar una
línea**. Luego, puede vincular la herramienta de medición a la opción en el
menú desplegable de **Acción** que aparece como **Tomar medidas**. Puede
agregar también una clave para activar la acción.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Tenga en cuenta que se elije el primer activador en la lista. El orden de los activadores es importantes y puede arrastrarlos en el orden que desee.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>En la pantalla de <b>Orden de trabajo</b>, un estado gráfico indica si la base de datos está conectada correctamente a la herramienta de medición.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../../../inventory_and_mrp/manufacturing/management/using_work_centers#workcenter-iot"><span class="std std-ref">Integración de dispositivos IoT</span></a></p>
</div>

