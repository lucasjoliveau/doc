# Conectar una pantalla

En Konvergo ERP, la Caja IoT se puede conectar a una pantalla. Después de
configurarla, la pantalla se puede usar para mostrarle un Punto de Venta (PdV)
al cliente.

![../../../../_images/screen-pos-client-
display.png](../../../../_images/screen-pos-client-display.png)

Ejemplo de una orden de PdV (punto de venta) en una pantalla.

Acceda a la visualización del cliente en la página de inicio de la Caja IoT y
haga clic en el botón **Pantalla del PdV**. Para ir a la página de inicio de
la Caja IoT , vaya a la aplicación IoT ‣ Cajas IoT y haga clic en el enlace de
la página de inicio de la Caja IoT.

## Conexión

La forma de conexión entre la pantalla y la Caja IoT depende del modelo.

IoT Box model 4IoT Box model 3

Conecte hasta dos pantallas con cables micro-HDMI en un lado de la Caja IoT.
Si ambas pantallas están conectadas, pueden mostrar contenido diferente
(consulte el Uso de Pantalla).

Conecte la pantalla con un cable HDMI en un lado de la Caja IoT.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../config/connect#iot-connect-schema"><span class="std std-ref">Consulte el esquema Raspberry Pi</span></a>.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Las pantallas deben estar conectadas antes de encender la Caja IoT. Si ya está encendida, conecte las pantallas y reinicie la Caja IoT desconectándola por diez segundos y conectándola de nuevo a la fuente de energía.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>El uso de adaptadores HDMI/micro-HDMI puede ocasionar problemas que resultan en una pantalla negra sin información. Se recomienda usar el cable específico para la conexión de la pantalla.</p>
</div>

Si la conexión tuvo éxito, la pantalla debe mostrar la **pantalla de cliente
de PdV**.

![La pantalla predeterminada de "Pantalla del cliente del PdV" que aparece
cuando la pantalla se conecta exitosamente a una Caja IoT.
](../../../../_images/screen-pos-client-display-no-order.png)

La pantalla también debe aparecer en la lista de **Pantallas** en la página de
inicio de la Caja IoT. También puede acceder a la pantalla en la aplicación
IoT ‣ Dispositivos.

![Ejemplo del nombre de una pantalla que se muestra en la página de inicio de
la Caja IoT. ](../../../../_images/screen-screen-name-example.png)
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si no se detecta ninguna pantalla, aparecerá una pantalla predeterminada llamada <b>Pantalla distante</b>. Esto indica que no hay ningún hardware de pantalla conectado.</p>
<blockquote>
<div><img alt='El nombre de "pantalla distante" se utilizará si no se detecta ninguna pantalla.' class="align-center" src="../../../../_images/screen-no-screen.png"/>
</div></blockquote>
</div>

## Uso

### Mostrar órdenes del Punto de Venta a los clientes

Para usar la pantalla en la aplicación de _Punto de venta_ , vaya a Punto de
venta ‣ Configuración ‣ Punto de Venta, seleccione un PdV, haga clic en
**Editar** si es necesario y active la función de **Caja IoT**.

Luego, seleccione la pantalla desde el menú desplegable de **Pantalla del
cliente**. Luego haga clic en **Guardar**.

![Conectar la pantalla con la aplicación Punto de
venta.](../../../../_images/screen-pos-screen-config.png)

La pantalla ahora está disponible para las sesiones del PdV. Aparecerá un
icono de pantalla en el menú de la parte superior de la pantalla para indicar
el estado de conexión de la pantalla.

![El icono de pantalla en el Punto de venta muestra el estado de la conexión
con la pantalla.](../../../../_images/screen-pos-icon.png)

La pantalla mostrará automáticamente las órdenes del PdV y actualizarla cuando
se hagan cambios a la orden.

![Un ejemplo de una orden de PdV en una pantalla.](../../../../_images/screen-
pos-client-display.png)

### Mostrar un sitio web en la pantalla

Abra la vista de formulario en la aplicación IoT ‣ Dispositivos ‣ Pantalla del
cliente. Esto le permite al usuario escoger una URL de sitio web específica
para que aparezca en la pantalla usando el campo **Mostrar URL**.

  *[PdV]: Punto de Venta

