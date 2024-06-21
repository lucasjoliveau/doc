# Conectar una caja IoT a Konvergo ERP

Una caja IoT (Internet de las cosas, por sus siglas en inglés) es un
dispositivo microordenador que permite la conexión de dispositivos de entrada
y salida a una base de datos de Konvergo ERP. Es necesario contar con una suscripción
a la caja IoT para poder utilizarla con una conexión segura. También necesita
una computadora para configurar la caja IoT.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="https://www.odoo.com/app/iot-faq">Preguntas frecuentes sobre la caja IoT</a></p>
</div>

Comience el proceso de configuración del IoT a través de la [aplicación
IoT](../../apps_modules#general-install) en la base de datos de Konvergo ERP,
puede descargarla desde Aplicaciones.

![La aplicación Internet de las cosas \(IoT\) en la base de datos de
Konvergo ERP.](../../../../_images/install-iot-app.png)

A continuación, una vez instalada la _aplicación IoT_ , vaya a Aplicación IoT
‣ Cajas IoT y haga clic en el botón **Conectar** ubicado en la esquina
superior izquierda del tablero de Cajas IoT.

![Conectar una caja IoT a la base de datos de
Konvergo ERP.](../../../../_images/connect-iot.png)

Se recomiendan dos formas de conectar el dispositivo IoT a la base de datos
mediante la _aplicación IoT_. Siga los pasos de cualquiera de las siguientes
dos secciones para conectar el dispositivo IoT mediante una conexión ethernet
por cable o mediante WiFi.

![Pasos de conexión mediante ethernet o WiFi.](../../../../_images/connect-
iot-box.png) <div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>La imagen de disco con la que la tarjeta SD de la caja <abbr title="Internet de las cosas">IoT</abbr> está formateada es única para la versión de la base de datos Konvergo ERP con la que la caja IoT está funcionando. Asegúrese de que la caja IoT tenga la imagen de disco más <a href="updating_iot#iot-config-flash"><span class="std std-ref">actualizada</span></a>.</p>
</div>

## Conexión ethernet

El siguiente es el proceso para conectar la caja IoT a través de un cable
ethernet a la base de datos de Konvergo ERP.

Comience por conectar todos los dispositivos por cable a la caja IoT
(ethernet, dispositivos USB, etc.). Si no puede, debería conectarse a una
pantalla HDMI. Lo siguiente es conectar la caja IoT a una fuente de
alimentación.

Una vez que la unidad se encienda, lea el _código de emparejamiento_ de la
pantalla o de la impresión de una impresora conectada a la caja IoT.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>De forma predeterminada, la caja IoT mostrará el <em>código de emparejamiento</em> durante un máximo de 5 minutos después de que se encienda la unidad. Transcurridos los 5 minutos, el <em>código de emparejamiento</em> desaparecerá por motivos de seguridad y la caja IoT deberá reiniciarse manualmente al desenchufar la unidad de la fuente de alimentación durante diez segundos y volviéndola a enchufar.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si no hay ninguna pantalla conectada a la caja IoT, se puede acceder al <em>código de emparejamiento</em> desde la página de inicio, solo debe hacer clic en el botón <b>Pantalla del PdV</b>. Si desea obtener más información sobre cómo acceder a la página de inicio de la caja IoT, visite <a href="#iot-connect-token"><span class="std std-ref">Conectar la caja IoT de forma manual utilizando el token</span></a>.</p>
</div>

Desde su equipo, vaya a la aplicación IoT ‣ Cajas IoT y haga clic en el botón
**Conectar** ubicado en la esquina superior izquierda del tablero de Cajas
IoT. Introduzca el _código de emparejamiento_ en el campo **Código de
emparejamiento** y haga clic en el botón **Emparejar**. La base de datos se
vinculará a la caja IoT y ésta aparecerá en la página Cajas IoT.

## Conexión wifi

El siguiente es el proceso para conectar la caja IoT vía WiFi a la base de
datos de Konvergo ERP.

Primero, asegúrese de que no haya ningún cable ethernet conectado a la caja
IoT. Después, conecte todos los dispositivos con cable a la caja IoT
(dispositivos USB, etc.).

Después de conectar los dispositivos, conecte la caja IoT a una fuente de
alimentación. Desde su equipo, vaya a la aplicación IoT ‣ Cajas IoT y, a
continuación, haga clic en el botón **Conectar** ubicado en la esquina
superior izquierda del tablero de Cajas IoT. Enseguida copie el **Token** de
la sección **Conexión WiFi** ya que lo tendrá que usar para vincular la base
de datos de Konvergo ERP a la caja IoT.

De nuevo en su equipo, vaya a las redes WiFi disponibles y conéctese a la red
WiFi de la caja IoT. La red WiFi distribuida por la caja IoT comenzará por
`IoTBox-xxxxxxxxxx`.

![Redes wifi disponibles en la computadora.](../../../../_images/connect-iot-
wifi.png)

Al conectarse al WiFi de la caja IoT, un navegador le redirigirá
automáticamente al asistente de configuración de la caja IoT. Asigne un nombre
a la caja IoT y pegue el _token_ previamente copiado en el campo **Token del
servidor** , y haga clic en :guilabel: `Siguiente`.

![Introduzca el token del servidor en la caja
IoT.](../../../../_images/server-token.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si el asistente de conexión WiFi de la caja IoT no se ejecuta, consulte la sección <a href="#iot-connect-token"><span class="std std-ref">conectar con token</span></a>.</p>
</div>

A continuación, seleccione la red WiFi a la que se conectará la caja IoT
(introduzca la contraseña si existe) y haga clic en **Conectar**. Espere unos
segundos y el navegador se redirigirá a la página de inicio de la caja IoT. Si
la conexión no se produce automáticamente, puede que sea necesario volver a
conectar el equipo de forma manual a la red WiFi original.

![Configurar el WiFi para la caja IoT.](../../../../_images/configure-wifi-
network-iot.png)

Después de completar cada paso, la caja IoT debería aparecer al navegar en la
aplicación IoT ‣ Cajas IoT en la base de datos de Konvergo ERP.

![Se ha configurado correctamente la caja IoT en la base de datos de
Konvergo ERP.](../../../../_images/iot-box-connected.png) <div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Puede que sea necesario reiniciar la caja IoT manualmente después de conectarse con éxito a través de WiFi para que la caja aparezca en la aplicación <em>IoT</em> de la base de datos de Konvergo ERP. Para ello, simplemente desconecte el dispositivo y vuelva a conectarlo a la fuente de alimentación después de diez segundos.</p>
</div>

## Conectar la caja IoT de forma manual utilizando el token

La conexión manual de la caja IoT a la aplicación IoT puede realizarse
mediante el _token_ desde una computadora. Puede encontrar el _token_ si va a
la aplicación IoT ‣ Cajas IoT y hace clic en **Conectar**.

En la sección **Conexión WiFi** de la página **Conectar una caja IoT** que
aparece, haga clic en **Copiar** a la derecha del **Token**. Deberá introducir
este token en la página de inicio de la caja IoT.

Para acceder a la página de inicio de la caja IoT introduzca la dirección IP
de la caja IoT en una ventana del navegador desde una computadora que esté en
la misma red que la caja IoT (preferentemente mediante una conexión Ethernet).

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Se puede acceder a la dirección IP desde la consola de administración del router a la que está conectada la caja IoT, o conectando una impresora a la caja IoT. Se imprimirá un recibo con la dirección IP de la caja IoT.</p>
</div>

En la página de inicio de la caja IoT, introduzca el _token_ en la sección
**Servidor** y haga clic en **Configurar**. A continuación, pegue el _token_
en el campo **Token del servidor** y haga clic en **Conectar**. La caja IoT se
vinculará a la base de datos de Konvergo ERP.

## Diagrama de la caja IoT

### Raspberry Pi 4

![../../../../_images/iot-box-schema.png](../../../../_images/iot-box-
schema.png)

El diagrama de la caja IoT de Konvergo ERP (Raspberry Pi 4) con etiquetas.

### Raspberry Pi 3

![../../../../_images/iox-box-schema-3.png](../../../../_images/iox-box-
schema-3.png)

El diagrama de la caja IoT de Konvergo ERP (Raspberry Pi 3) con etiquetas.

  *[IoT]: Internet de las cosas
  *[IP]: Protocolo de Internet

