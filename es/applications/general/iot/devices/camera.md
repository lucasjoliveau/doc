# Conectar una cámara

Es posible conectar una cámara a la caja IoT de una base de datos de Konvergo ERP en
pocos pasos. Una vez que una cámara está conectada a la caja IoT, puede usarla
en los procesos de fabricación o vincularla a un punto de control de calidad.
Esto le permite tomar fotografías cuando llega a un punto de control de
calidad elegido o cuando presiona una tecla específica durante la fabricación.

## Conexión

Para conectar una cámara a una caja IoT, solo conecte ambas con un cable. Esto
se suele hacer con un cable USB de algún tipo.

Si la cámara es [compatible](https://www.odoo.com/page/iot-hardware) no deberá
configurar nada, pues se detectará en cuanto la conecte.

![Cámara reconocida en la caja IoT.](../../../../_images/camera-dropdown.png)

## Vincular una cámara al punto de control de calidad de un proceso de
fabricación

En la aplicación Calidad, puede configurar un dispositivo en un **punto de
control de calidad**. Vaya a la aplicación Calidad ‣ Control de calidad ‣
Puntos de control y abra el **punto de control** deseado al que estará
vinculada la cámara.

En el formulario de punto de control, puede editar el punto de control si
selecciona el campo **Tipo** y hace clic en la opción **Tomar una foto** del
menú desplegable. Esto hace que aparezca el campo **Dispositivo** , en el que
puede seleccionar el _dispositivo_ adjunto. **Guarde** los cambios, si es
necesario.

![Configurar el dispositivo en el punto de control de
calidad.](../../../../_images/control-point-device.png)

Ahora podrá usar la cámara en el punto de control de calidad seleccionado.
Cuando llegue al punto de control de calidad del proceso de fabricación, la
base de datos le solicitará al operador que tome una foto.

![Interfaz gráfica del usuario del dispositivo en el punto de control de
calidad. ](../../../../_images/serial-number-picture.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>También puede acceder a los puntos de control de calidad en la aplicación IoT ‣ Dispositivos y seleccione el dispositivo que desee. Hay una pestaña de <b>Puntos de control de calidad</b> donde se pueden agregar con el dispositivo.</p>
</div>
<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>En un formulario de revisión de calidad, el <b>Tipo</b> de revisión también se puede especificar para <b>Tomar una foto</b>. Vaya a la aplicación Calidad ‣ Control de calidad ‣ Revisiones de calidad ‣ Nuevo para crear una nueva revisión de calidad desde la página de <b>Revisiones de calidad</b>.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../../../inventory_and_mrp/quality/quality_management/quality_control_points">Puntos de control de calidad</a></p></li>
<li><p><a href="../../../inventory_and_mrp/quality/quality_management/quality_alerts">Crear alertas de calidad</a></p></li>
</ul>
</div>

## Vincular una cámara a un centro de trabajo en la aplicación Fabricación

Para vincular una cámara a una acción, primero necesita configurarla en un
centro de trabajo. Vaya a Fabricación ‣ Configuración ‣ Centros de trabajo.
Luego, vaya al **Centro de trabajo** que desee y en donde usará la cámara para
mostrar el formulario detallado de ese centro de trabajo específico. Luego,
agregue el dispositivo en la pestaña **Activadores de IoT `, en la columna
:guilabel:`Dispositivos** y haga clic en **Agregar una línea**.

Ahora el dispositivo de la cámara se puede vincular a la opción de columna
desplegable de **Acción** que aparece como **Tomar una foto**. También puede
agregar una clave para activar la acción.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Se elije el activador que esté al inicio de la lista. El orden de activadores es importante y los puede arrastrar en el orden que desee.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>En la pantalla de guilabel:<code>Orden de trabajo</code>, un estado gráfico indica si la base de datos está conectada correctamente a la cámara.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../../../inventory_and_mrp/manufacturing/management/using_work_centers#workcenter-iot"><span class="std std-ref">Integración de dispositivos IoT</span></a></p>
</div>

  *[IoT]: Internet de las cosas
  *[USB]: Bus serie universal

